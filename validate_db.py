#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_db.py — 拍摄格式码率资料库 完整性校验门禁
=================================================
在推送前运行，捕获「同类 bug」：
  [HARD] 1) 内部数学自洽：gbh = mbs*3600/1024、gbm = gbh/60、1TB 时长
  [HARD] 2) 十进制/二进制口径：official_rate 含「X MB/s 十进制」则 mbs = X*0.953674
  [HARD] 3) 官方表去重：(model,codec,resolution,fps) 唯一
  [HARD] 4) 官方表单帧一致性：同 (model,resolution,codec) 内 per-frame=mbs/fps 须一致(±15%)
  [WARN] 5) 实测表单帧一致性：同上，但慢动作(传感器≠交付)按传感器帧率比对，偏差>15% 标「异模式/疑似误标」
  [WARN] 6) 命名词表：codec 含 "OG" 但无 "Open Gate" 字样

退出码：0=通过(含 WARN)；1=存在 HARD 错误（应阻断推送）
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OFFICIAL = os.path.join(HERE, "specs_official.csv")
MEASURED = os.path.join(HERE, "specs_measured.csv")

DEC = 0.953674  # 十进制 MB/s -> 二进制 MB/s


def to_num(s):
    s = (s or "").replace(",", "").replace("，", "").strip()
    if s == "":
        return None
    try:
        return float(s)
    except Exception:
        return None


def fps_to_int(s):
    s = (s or "").lower().strip()
    s = s.replace("fps", "").replace("p", "").replace(" ", "")
    try:
        return int(round(float(s)))
    except Exception:
        return None


def parse_tb_minutes(txt):
    """解析 '28 min' / '1h04m' / '55 min（1TB @25fps）' -> 分钟数，失败返回 None。"""
    if not txt:
        return None
    m = re.search(r"(\d+)\s*h\s*(\d+)\s*m", txt)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    m = re.search(r"(\d+(?:\.\d+)?)\s*min", txt)
    if m:
        return float(m.group(1))
    m = re.search(r"(\d+)\s*h", txt)
    if m:
        return int(m.group(1)) * 60
    return None


def calc_tb_minutes(mbs_binary):
    if not mbs_binary:
        return None
    dec = mbs_binary / DEC
    sec = 1_000_000.0 / dec
    return sec / 60.0


def parse_decimal_from_rate(txt):
    """提取 '≈ 297.7 MB/s 十进制' 中的数值。"""
    if not txt:
        return None
    m = re.search(r"([\d.]+)\s*MB/s\s*十进制", txt)
    if m:
        return float(m.group(1))
    return None


class Report:
    def __init__(self):
        self.hard = []
        self.warn = []

    def h(self, msg):
        self.hard.append(msg)

    def w(self, msg):
        self.warn.append(msg)

    def has_error(self):
        return len(self.hard) > 0


def validate_official(rep):
    rows = []
    with open(OFFICIAL, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mbs = to_num(r.get("mbs_binary", ""))
            gbh = to_num(r.get("gbh_binary", ""))
            gbm = to_num(r.get("gbm_binary", ""))
            fps = fps_to_int(r.get("fps", ""))
            rows.append({
                "no": r.get("no", "?"),
                "model": r.get("model", ""),
                "codec": r.get("codec", ""),
                "resolution": r.get("resolution", ""),
                "fps": fps,
                "mbs": mbs,
                "gbh": gbh,
                "gbm": gbm,
                "tb_raw": r.get("tb_record_time", ""),
                "rate": r.get("official_rate", ""),
            })

    # 1) 内部数学 + 2) 十进制口径
    for r in rows:
        if r["mbs"] and r["gbh"]:
            gbh_calc = r["mbs"] * 3600 / 1024
            if abs(gbh_calc - r["gbh"]) > max(1.0, 0.01 * r["gbh"]):
                rep.h(f"[官方] no{r['no']} {r['model']} {r['codec']}：gbh 自洽失败 "
                      f"计算={gbh_calc:.1f} 存储={r['gbh']:.1f}")
        if r["gbh"] and r["gbm"]:
            gbm_calc = r["gbh"] / 60.0
            if abs(gbm_calc - r["gbm"]) > max(0.05, 0.01 * r["gbm"]):
                rep.h(f"[官方] no{r['no']} {r['model']} {r['codec']}：gbm 自洽失败 "
                      f"计算={gbm_calc:.2f} 存储={r['gbm']:.2f}")
        tb_calc = calc_tb_minutes(r["mbs"])
        tb_raw = parse_tb_minutes(r["tb_raw"])
        if tb_calc and tb_raw and abs(tb_calc - tb_raw) / tb_raw > 0.10:
            rep.h(f"[官方] no{r['no']} {r['model']} {r['codec']}：1TB 时长不一致 "
                  f"计算={tb_calc:.1f}min 存储={tb_raw:.1f}min")
        dec = parse_decimal_from_rate(r["rate"])
        if dec and r["mbs"]:
            exp = dec * DEC
            if abs(exp - r["mbs"]) > max(2.0, 0.02 * dec):
                rep.h(f"[官方] no{r['no']} {r['model']} {r['codec']}：十进制/二进制口径不符 "
                      f"官方十进制={dec} -> 应≈{exp:.2f} 实际={r['mbs']:.2f}")

    # 3) 去重
    seen = {}
    for r in rows:
        key = (r["model"], r["codec"], r["resolution"], r["fps"])
        if None in key:
            continue
        if key in seen:
            rep.h(f"[官方] 重复键 {key}：no{seen[key]} 与 no{r['no']}")
        else:
            seen[key] = r["no"]

    # 4) 官方表单帧一致性（HARD）
    groups = {}
    for r in rows:
        if not (r["mbs"] and r["fps"]):
            continue
        groups.setdefault((r["model"], r["resolution"], r["codec"]), []).append(r)
    for (model, res, codec), grp in groups.items():
        if len(grp) < 2:
            continue
        pfs = [x["mbs"] / x["fps"] for x in grp]
        med = sorted(pfs)[len(pfs) // 2]
        for x, pf in zip(grp, pfs):
            if abs(pf - med) / med > 0.15:
                rep.h(f"[官方] {model} {res} {codec}：单帧不一致 "
                      f"no{x['no']} {pf:.2f} MiB/帧 vs 中位 {med:.2f} MiB/帧")

    # 6) 命名 OG/Open Gate
    for r in rows:
        if "OG" in r["codec"] and "Open Gate" not in r["codec"]:
            rep.w(f"[官方] no{r['no']} {r['model']} {r['codec']}：含 'OG' 但无 'Open Gate' 字样（检索友好性）")


def validate_measured(rep):
    rows = []
    with open(MEASURED, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            sensor = fps_to_int(r.get("传感器帧率", ""))
            deliver = fps_to_int(r.get("素材帧率", ""))
            mbs = to_num(r.get("码流MB/s", ""))
            gbh = to_num(r.get("GB/h", ""))
            rows.append({
                "no": r.get("序号", "?"),
                "model": r.get("机型", ""),
                "codec": r.get("编码", ""),
                "resolution": r.get("分辨率", ""),
                "sensor": sensor, "deliver": deliver,
                "status": r.get("编码核对状态", ""),
                "mbs": mbs, "gbh": gbh,
            })

    # 内部数学（GB/h = mbs*3600/1024）
    for r in rows:
        if r["mbs"] and r["gbh"]:
            gbh_calc = r["mbs"] * 3600 / 1024
            if abs(gbh_calc - r["gbh"]) > max(1.0, 0.01 * r["gbh"]):
                rep.h(f"[实测] no{r['no']} {r['model']} {r['resolution']} {r['codec']}："
                      f"gbh 自洽失败 计算={gbh_calc:.1f} 存储={r['gbh']:.1f}")

    # 5) 单帧一致性（WARN）—— 慢动作按传感器帧率比对
    groups = {}
    for r in rows:
        if not (r["mbs"] and r["deliver"]):
            continue
        groups.setdefault((r["model"], r["resolution"], r["codec"]), []).append(r)
    for (model, res, codec), grp in groups.items():
        non_slow = [x for x in grp if x["sensor"] == x["deliver"]]
        if not non_slow:
            continue
        med = sorted(x["mbs"] / x["deliver"] for x in non_slow)[len(non_slow) // 2]
        for x in non_slow:
            pf = x["mbs"] / x["deliver"]
            if abs(pf - med) / med > 0.15:
                rep.w(f"[实测] no{x['no']} {model} {res} {codec}：非慢动作单帧异常 "
                      f"{pf:.2f} MiB/帧 vs 中位 {med:.2f}（疑似误标）")
        for x in grp:
            if x["sensor"] != x["deliver"] and x["sensor"]:
                pf = x["mbs"] / x["sensor"]  # 慢动作按传感器帧率
                if abs(pf - med) / med > 0.15:
                    if "慢动作" in (x["status"] or ""):
                        continue  # 已标记，不再重复告警
                    rep.w(f"[实测] no{x['no']} {model} {res} {codec}：慢动作单帧异常 "
                          f"{pf:.2f} MiB/帧(传感器{x['sensor']}fps) vs 中位 {med:.2f} "
                          f"—— 异模式/降数据，勿线性外推")


def main():
    rep = Report()
    print("========== 校验 specs_official.csv ==========")
    validate_official(rep)
    print("========== 校验 specs_measured.csv ==========")
    validate_measured(rep)

    print("\n================= 校验摘要 =================")
    for m in rep.hard:
        print("  [HARD] " + m)
    for m in rep.warn:
        print("  [WARN] " + m)
    print(f"\n  HARD 错误: {len(rep.hard)} | WARN 警告: {len(rep.warn)}")
    if rep.has_error():
        print("  → 存在 HARD 错误，应阻断推送。")
        return 1
    print("  → 通过（WARN 仅提醒，不阻断）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
