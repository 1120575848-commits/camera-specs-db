#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
query.py — 拍摄格式 / 码率资料库 确定性查询工具
=============================================
直接读本地 CSV（不经过网络搜索），按 机型/编码/分辨率/帧率 精确过滤，
输出「单机 + N 台合计」的 GB/h 表。下游 AI / 用户直接调用，秒级出表。

用法示例：
  python3 query.py "ALEXA Mini" -n 3
  python3 query.py "ALEXA 35" -n 3 --codec ARRIRAW --fps 25
  python3 query.py "ALEXA 35" --codec "Open Gate" --fps 25 --count 3

退出码：
  0 = 命中并出表
  2 = 库内未收录该机型（供上层判断「补数据 / 用外部数据」）
  3 = 参数错误
"""
import csv
import os
import sys
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
OFFICIAL = os.path.join(HERE, "specs_official.csv")
MEASURED = os.path.join(HERE, "specs_measured.csv")

DEC = 0.953674  # 十进制 MB/s -> 二进制 MB/s


# ---------- 工具函数 ----------
def to_num(s):
    s = (s or "").replace(",", "").replace("，", "").strip()
    if s == "":
        return None
    try:
        return float(s)
    except Exception:
        return None


def fps_to_int(s):
    """解析帧率：支持 '25p' / '25 fps' / '25'。先去 'fps' 再去 'p'，避免 'fps' 里的 p 误删。"""
    s = (s or "").lower().strip()
    s = s.replace("fps", "")
    s = s.replace("p", "")
    s = s.replace(" ", "")
    try:
        return int(round(float(s)))
    except Exception:
        return None


def norm_codec(s):
    """把 Open Gate / OG 归一，便于等价匹配。"""
    return (s or "").lower().replace("open gate", "og")


def one_tb_minutes(mbs_binary):
    """1TB(=1000GB 十进制) 录制时长（分钟）。
    与 specs_official.csv 的 tb_record_time 同一口径：十进制速率 = 二进制/DEC。"""
    if not mbs_binary:
        return None
    dec = mbs_binary / DEC  # MB/s 十进制
    sec = 1_000_000.0 / dec  # 1TB=1e12 B / (dec*1e6 B/s)
    return sec / 60.0


# ---------- 数据加载 ----------
def load_official():
    rows = []
    with open(OFFICIAL, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mbs = to_num(r.get("mbs_binary", ""))
            rows.append({
                "src": "official",
                "brand": r.get("brand", ""),
                "model": r.get("model", ""),
                "alias": r.get("alias", ""),
                "codec": r.get("codec", ""),
                "resolution": r.get("resolution", ""),
                "fps": fps_to_int(r.get("fps", "")),
                "sensor_fps": None,
                "deliver_fps": fps_to_int(r.get("fps", "")),
                "mbs": mbs,
                "gbh": to_num(r.get("gbh_binary", "")),
                "tb_min": one_tb_minutes(mbs),
                "covered": r.get("covered", ""),
                "source": r.get("source", ""),
                "note": r.get("note", ""),
                "samples": None,
            })
    return rows


def load_measured():
    rows = []
    with open(MEASURED, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            sensor = fps_to_int(r.get("传感器帧率", ""))
            deliver = fps_to_int(r.get("素材帧率", ""))
            mbs = to_num(r.get("码流MB/s", ""))
            rows.append({
                "src": "measured",
                "brand": r.get("品牌", ""),
                "model": r.get("机型", ""),
                "alias": r.get("别名", ""),
                "codec": r.get("编码", ""),
                "resolution": r.get("分辨率", ""),
                "fps": deliver if deliver else sensor,  # 对外口径用交付帧率
                "sensor_fps": sensor,
                "deliver_fps": deliver,
                "mbs": mbs,
                "gbh": to_num(r.get("GB/h", "")),
                "tb_min": one_tb_minutes(mbs),
                "covered": "",
                "source": "",
                "note": ("慢动作" if (sensor and deliver and sensor != deliver) else ""),
                "samples": to_num(r.get("样本数", "")),
            })
    return rows


# ---------- 匹配 ----------
def match(rows, model, codec=None, res=None, fps=None):
    model_l = (model or "").lower()
    out = []
    for r in rows:
        m = (r["model"] or "").lower()
        if model_l not in m and model_l not in (r["alias"] or "").lower():
            continue
        if codec:
            if norm_codec(codec) not in norm_codec(r["codec"]):
                continue
        if res:
            if res.lower() not in (r["resolution"] or "").lower():
                continue
        if fps is not None and r["fps"] is not None and r["fps"] != fps:
            continue
        out.append(r)
    return out


# ---------- 输出 ----------
def fmt_tb(minutes):
    if minutes is None:
        return "—"
    if minutes >= 60:
        h = int(minutes // 60)
        m = int(round(minutes % 60))
        return f"{h}h{m:02d}m"
    return f"{int(round(minutes))} min"


def render(model, hits, count):
    # 只保留有具体 GB/h 的行（剔除纯百分比档，如 HDE 仅给比例无绝对码率）
    hits = [h for h in hits if h["gbh"] is not None]
    if not hits:
        return None
    # 去重：同 (codec,resolution,fps,src,sensor_fps) 只留一条
    seen = set()
    uniq = []
    for r in hits:
        key = (r["codec"], r["resolution"], r["fps"], r["src"], r["sensor_fps"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(r)
    uniq.sort(key=lambda x: (x["gbh"] or 0), reverse=True)

    print(f"\n=== 查询结果：{model}（{count} 台）===")
    print(f"匹配格式 {len(uniq)} 条（按数据量降序）：\n")
    w = 7 + len(str(count))
    hdr = f"{'#':>2}  {'编码':<26} {'分辨率':<11} {'帧率':>4}  {'MB/s':>8}  {'GB/h·台':>9}  {'GB/h·%d台' % count:>{w}}  {'1TB':>7}"
    print(hdr)
    print("-" * (len(hdr) + 6))
    for i, r in enumerate(uniq, 1):
        gbh = r["gbh"] or 0
        slow = " [慢动作]" if r.get("note") == "慢动作" else ""
        fps_s = f"{r['fps']}p" if r["fps"] is not None else "—"
        print(f"{i:>2}  {r['codec'][:25]:<26} {r['resolution']:<11} "
              f"{fps_s:>4}  {(r['mbs'] or 0):>8.2f}  {gbh:>9.1f}  "
              f"{gbh*count:>{w-1}.1f}  {fmt_tb(r['tb_min']):>7}{slow}")
    print()
    # 推荐：ARRIRAW / 未压缩 中数据量最大者（排除慢动作）
    rec = None
    for r in uniq:
        if r.get("note") == "慢动作":
            continue
        if "raw" in r["codec"].lower() or "未压缩" in r["codec"]:
            if rec is None or (r["gbh"] or 0) > (rec["gbh"] or 0):
                rec = r
    if rec is None and uniq:
        rec = uniq[0]
    if rec:
        print(f"★ 推荐（最大格式 / ARRIRAW）：{rec['codec']} {rec['resolution']} @"
              f"{rec['fps']}p → 单机 {rec['gbh']:.1f} GB/h，{count} 台 "
              f"{rec['gbh']*count:.1f} GB/h（≈ {rec['gbh']*count/1024:.2f} TiB/h）")
    return uniq


def main():
    ap = argparse.ArgumentParser(description="拍摄格式码率资料库查询")
    ap.add_argument("model", help="机型名，如 ALEXA Mini / ALEXA 35 / VENICE")
    ap.add_argument("-n", "--count", type=int, default=1, help="相机台数（默认 1）")
    ap.add_argument("--codec", help="编码过滤，如 ARRIRAW / ProRes / Open Gate")
    ap.add_argument("--res", help="分辨率过滤，如 4608x3164")
    ap.add_argument("--fps", type=int, help="帧率过滤，如 25")
    args = ap.parse_args()

    if not os.path.exists(OFFICIAL):
        print("✗ 找不到 specs_official.csv", file=sys.stderr)
        return 3

    allrows = load_official() + load_measured()
    hits = match(allrows, args.model, codec=args.codec, res=args.res, fps=args.fps)

    if not hits:
        print(f"✗ 库内未收录「{args.model}」"
              + (f" / {args.codec}" if args.codec else "")
              + (f" / {args.res}" if args.res else "")
              + (f" / {args.fps}p" if args.fps else "")
              + " 的精确匹配。")
        print("  → 可选：补进库（Agent 模式）或用外部官方数据并标注「非本库」。")
        return 2

    render(args.model, hits, args.count)
    return 0


if __name__ == "__main__":
    sys.exit(main())
