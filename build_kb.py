#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_kb.py — 由 specs_official.csv 生成 v14 派生数据（单一真源，杜绝手工漂移）
=====================================================================
运行：python3 build_kb.py

生成：
  1. specs_25p.csv          —— 25p 基准换算表（含 24p / 25p / 50p 三档预换算值）
  2. aliases.csv            —— 别名单一真源（官方 alias 列 + 实测锚点 note 列 + 口语补充）
  3. resolution_ladders.csv —— 机型 → 官方分辨率档位（降档按档位逐级下降用）
  4. AI_PACK.md §3 数据区   —— 整段由 CSV 重生成（规则手写、数据自动生成）

设计要点：
  - 对外 TB 统一按 1 TB = 10^12 B ≈ 1000 GB 取约数；库内 GB/h 保留二进制计算口径。
    两者差异属允许误差范围，不追求 1024 的数学精确（见 README 精度口径）。
  - 帧率换算：per_frame = GB/h ÷ 源帧率；24p = ×24，25p = ×25，50p = ×50。
    库内已有对应帧率行时优先取库内值，没有的才用本表（允许误差，不抠细节）。
"""
import csv
import os
import re
from collections import OrderedDict, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
OFFICIAL = os.path.join(BASE, "specs_official.csv")
ANCHORS = os.path.join(BASE, "measured_anchors.csv")
PACK = os.path.join(BASE, "AI_PACK.md")

SEP25 = "## 3. 速查数据"
SEP4 = "## 4. 容量 / 备份 / 报价口径"


def num(s):
    s = (s or "").replace(",", "").replace("，", "").strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def fps_int(s):
    s = (s or "").lower().strip().replace("fps", "").replace("p", "").replace(" ", "")
    try:
        v = float(s)
        return int(round(v)) if v > 0 else None
    except ValueError:
        return None


def fmt(v, nd=1):
    return "" if v is None else f"{v:.{nd}f}"


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- 1. 25p 基准表
# 主力机型：客户最常问、且示范里用到的格式。其余行仍进 specs_25p.csv 全量表，
# 但 AI_PACK 只内嵌这张精简表，避免单文件包过大。
KEY_ROWS = [
    ("ALEXA 35", "ARRIRAW 未压缩 4.6K 3:2 Open Gate (OG)"),
    ("ALEXA 35", "ARRIRAW HDE（高密度编码）"),
    ("ALEXA 35", "ProRes 4444 4K UHD"),
    ("ALEXA 35", "ProRes 4444 4.6K 3:2 Open Gate (OG)"),
    ("ALEXA Mini LF", "ARRIRAW 4.5K LF 3:2 Open Gate (OG)"),
    ("MPC-3628 / CineAlta VENICE 2 8K", "X-OCN XT 8.6K 3:2"),
    ("MPC-3628 / CineAlta VENICE 2 8K", "X-OCN ST 8.6K 3:2"),
    ("MPC-3628 / CineAlta VENICE 2 8K", "X-OCN LT 8.6K 3:2"),
    ("MPC-3628 / CineAlta VENICE 2 8K", "X-OCN XT 8.2K 17:9"),
    ("MPC-3628 / CineAlta VENICE 2 8K", "X-OCN ST 8.2K 17:9"),
    ("MPC-3628 / CineAlta VENICE 2 8K", "X-OCN LT 8.2K 17:9"),
    ("MPC-3626 / CineAlta VENICE 2 6K", "X-OCN XT 6K 3:2"),
    ("Inspire 3 / X9-8K Air", "ProRes RAW 8.1K Full Frame"),
    ("Inspire 3 / X9-8K Air", "CinemaDNG 8.1K Full Frame"),
    ("Inspire 3 / X9-8K Air", "ProRes 422 HQ 4K Full Frame"),
    ("V-RAPTOR [X] 8K VV", "REDCODE RAW HQ 8K 17:9"),
    ("V-RAPTOR [X] 8K VV", "REDCODE RAW HQ 6K 17:9"),
    ("ILME-FX6V", "XAVC-I QFHD"),
    ("ILME-FX3 / FX3A", "XAVC S 4K"),
    ("ILCE-7SM3", "XAVC HS 4K"),
]
SHORT_NAME = {
    "ALEXA 35": "ARRI ALEXA 35",
    "ALEXA Mini LF": "ARRI ALEXA Mini LF",
    "MPC-3628 / CineAlta VENICE 2 8K": "Sony VENICE 2 8K",
    "MPC-3626 / CineAlta VENICE 2 6K": "Sony VENICE 2 6K",
    "Inspire 3 / X9-8K Air": "DJI Inspire 3",
    "V-RAPTOR [X] 8K VV": "RED V-RAPTOR [X]",
    "ILME-FX6V": "Sony FX6",
    "ILME-FX3 / FX3A": "Sony FX3",
    "ILCE-7SM3": "Sony A7S III",
}


def build_25p(rows):
    out = []
    for d in rows:
        gbh = num(d.get("gbh_binary", ""))
        fps = fps_int(d.get("fps", ""))
        # 无帧率 / 无码率的行不参与换算（如「全档上限」「随拍摄帧率」）
        if not gbh or not fps:
            continue
        pf = gbh / fps
        g24, g25, g50 = pf * 24, pf * 25, pf * 50
        out.append({
            "brand": d["brand"], "model": d["model"], "alias": d["alias"],
            "codec": d["codec"], "resolution": d["resolution"].replace("x", "×"),
            "fps_src": d["fps"], "gbh_24p": fmt(g24), "gbh_25p": fmt(g25),
            "gbh_50p": fmt(g50),
            # 对外 TB/h：十进制 10^12 B 近似 = GB/h ÷ 1000，取约数
            "tb_h_25p": fmt(g25 / 1000, 2), "tb_30min_25p": fmt(g25 / 2000, 2),
            "basis": "derived_fps",
        })
    # HDE：官方未给固定码率，按同机型未压缩 ARRIRAW 的 55% 估算，单独标 basis
    for d in rows:
        if "HDE" not in d["codec"]:
            continue
        base = next((x for x in out if x["model"] == d["model"]
                     and "ARRIRAW 未压缩 4.6K 3:2" in x["codec"]), None)
        if not base:
            continue
        g25 = float(base["gbh_25p"]) * 0.55
        out.append({
            "brand": d["brand"], "model": d["model"], "alias": d["alias"],
            "codec": d["codec"], "resolution": d["resolution"].replace("x", "×"),
            "fps_src": "25p", "gbh_24p": fmt(g25 * 24 / 25), "gbh_25p": fmt(g25),
            "gbh_50p": fmt(g25 * 2), "tb_h_25p": fmt(g25 / 1000, 2),
            "tb_30min_25p": fmt(g25 / 2000, 2), "basis": "estimated_hde",
        })

    fields = ["brand", "model", "alias", "codec", "resolution", "fps_src",
              "gbh_24p", "gbh_25p", "gbh_50p", "tb_h_25p", "tb_30min_25p", "basis"]
    with open(os.path.join(BASE, "specs_25p.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    return out


def key_25p_table(rows25):
    idx = {(r["model"], r["codec"]): r for r in rows25}
    lines = [
        "| 机型 | 编码 | 分辨率 | 25p GB/h | 对外 1 小时 | 对外 30 分钟 |",
        "|---|:---:|:---:|---:|---:|---:|",
    ]
    def pretty(gbh):
        """≥1000 GB/h 用 TB，不足用 GB；对外十进制取约数。"""
        if gbh is None:
            return "—"
        return (f"{gbh / 1000:.1f} TB" if gbh >= 1000 else f"{gbh:.0f} GB")

    for model, codec in KEY_ROWS:
        r = idx.get((model, codec))
        if not r:
            continue
        g25 = float(r["gbh_25p"])
        lines.append(f"| {SHORT_NAME.get(model, model)} | {codec} | {r['resolution']} | "
                     f"{r['gbh_25p']} | {pretty(g25)} | {pretty(g25 / 2)} |")
    return lines


# ---------------------------------------------------------------- 2. 别名表
# 口语补充：报告 / 客户常说的话，官方 alias 列里没有
EXTRA_ALIASES = [
    ("阿莱 A35", "ALEXA 35", "model"),
    ("艾丽莎 35", "ALEXA 35", "model"),
    ("A35", "ALEXA 35", "model"),
    ("35", "ALEXA 35", "model"),
    ("威尼斯", "MPC-3628 / CineAlta VENICE 2 8K", "model"),
    ("威尼斯2", "MPC-3628 / CineAlta VENICE 2 8K", "model"),
    ("威尼斯二代", "MPC-3628 / CineAlta VENICE 2 8K", "model"),
    ("悟3", "Inspire 3 / X9-8K Air", "model"),
    ("悟 3", "Inspire 3 / X9-8K Air", "model"),
    ("Inspire 3", "Inspire 3 / X9-8K Air", "model"),
    ("如影4D", "RONIN 4D", "model"),
    ("禅思 X9", "RONIN 4D", "model"),
    ("狗13", "HERO13 Black", "model"),
    ("狗 13", "HERO13 Black", "model"),
    ("双子座", "DSMC2 GEMINI 5K S35", "model"),
    ("猛禽X", "V-RAPTOR [X] 8K VV", "model"),
    ("科莫多X", "KOMODO-X 6K S35", "model"),
    ("尼康 ZR", "ZR", "model"),
    ("ZR", "ZR", "model"),
    ("A7S3", "ILCE-7SM3", "model"),
    ("S3", "ILCE-7SM3", "model"),
    ("M4", "ILCE-7M4", "model"),
    ("M3", "ILCE-7M3", "model"),
    ("FX6", "ILME-FX6V", "model"),
    ("FX3", "ILME-FX3 / FX3A", "model"),
    ("阿莱", "", "brand"),
    ("ARRI", "", "brand"),
    ("Sony", "", "brand"),
    ("索尼", "", "brand"),
    ("大疆", "", "brand"),
    ("DJI", "", "brand"),
    ("RED", "", "brand"),
    ("小飞机", "", "family"),
    ("航拍小飞机", "", "family"),
]
SPLIT = re.compile(r"\s*[/／·、,，|]\s*")

# 实测锚点里的 key 是「报告代号」，先统一换成规格表里的官方 model 名，
# 否则别名命中后去规格表查会扑空。空串 = 品牌/未记录机型，不指向具体型号。
ANCHOR_CANON = {
    "MPC-3628": "MPC-3628 / CineAlta VENICE 2 8K",
    "ARRI ALEXA Mini LF": "ALEXA Mini LF",
    "ARRI ALEXA 35": "ALEXA 35",
    "ARRI ALEXA Mini": "ALEXA Mini",
    "RONIN 4D": "Ronin 4D",
    "ILME-FX3": "ILME-FX3 / FX3A",
    "ILME-FX3A": "ILME-FX3 / FX3A",
    "NIKON ZR": "ZR",
    "ARRI": "",
    "Sony": "",
    "（未记录）": "",
    # ILME-FX5 为报告代号，官方 Cinema Line 未见此型号：保留原值、库内标「待人工修正」
}


def build_aliases(official, anchors):
    pairs = []
    # 品牌词 / 家族词一律不指向具体机型，优先于任何 model 映射
    reserved = {a.lower().replace(" ", ""): k
                for a, c, k in EXTRA_ALIASES if k in ("brand", "family")}

    def add(alias, canonical, kind):
        a = (alias or "").strip().strip("（）()").strip()
        if not a or len(a) > 40 or a in ("—", "-", "–"):
            return
        # 明显不是称呼的说明性文字，跳过
        if any(x in a for x in ("报告", "官方", "未记录", "待核", "Cinema Line", "改进款")):
            return
        lk = a.lower().replace(" ", "")
        if lk in reserved and reserved[lk] != kind:
            kind, canonical = reserved[lk], ""
        pairs.append((a, canonical, kind))

    for d in official:
        for p in SPLIT.split(d.get("alias", "")):
            add(p, d["model"], "model")
        add(d["model"], d["model"], "model")
    for a in anchors:
        if a.get("type") != "CAMERA_MAX_GBH":
            continue
        raw = a.get("key", "")
        key = ANCHOR_CANON.get(raw, raw)
        kind = "brand" if not key else "model"
        for p in SPLIT.split(a.get("note", "")):
            add(p, key, kind)
        add(raw, key, kind)
    for a, c, k in EXTRA_ALIASES:
        add(a, c, k)

    # 去重：同一别名只留一条；brand / family 不指向具体机型
    seen = {}
    for a, c, k in pairs:
        lk = a.lower().replace(" ", "")
        if lk in seen:
            old = seen[lk]
            if old[2] in ("brand", "family"):
                continue  # 品牌 / 家族词不许被具体机型覆盖
            if k == "model" and old[2] != "model":
                seen[lk] = (a, c, k)
            continue
        seen[lk] = (a, c, k)

    out = sorted(seen.values(), key=lambda x: (x[2], x[1], x[0]))
    with open(os.path.join(BASE, "aliases.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["alias", "canonical", "kind"])
        w.writerows(out)
    return out


def alias_table(aliases):
    """AI_PACK 内嵌：按规范机型聚合，一行一个 canonical，别名用 / 串起来。"""
    groups = defaultdict(list)
    for a, c, k in aliases:
        if k == "model" and c:
            groups[c].append(a)
    lines = [
        "| 客户可能这么说 | 对应规范机型 |",
        "|---|---|",
    ]
    for canonical in sorted(groups):
        vals = []
        for a in groups[canonical]:
            if a == canonical or a.lower().replace(" ", "") == canonical.lower().replace(" ", ""):
                continue
            if a not in vals:
                vals.append(a)
        if vals:
            lines.append(f"| {' / '.join(vals)} | {canonical} |")
    lines.append("")
    lines.append("`阿莱 / ARRI / 索尼 / Sony / 大疆 / DJI / RED` 这类**只说到品牌**，"
                 "以及「小飞机 / 航拍小飞机」，都不对应具体机型 —— 按追问例外先问清型号，不要硬套。")
    return lines


# ---------------------------------------------------------------- 3. 分辨率档位
def build_ladders(official):
    by_model = defaultdict(dict)
    for d in official:
        m = re.search(r"(\d+)\s*[x×]\s*(\d+)", d.get("resolution", ""))
        if not m:
            continue
        w, h = int(m.group(1)), int(m.group(2))
        res = f"{w}×{h}"
        ratio = round(w / h, 3)
        if abs(ratio - 16 / 9) < 0.02:
            aspect = "16:9"
        elif abs(ratio - 17 / 9) < 0.02:
            aspect = "17:9"
        elif abs(ratio - 3 / 2) < 0.02:
            aspect = "3:2"
        else:
            aspect = f"{ratio:.2f}:1"
        by_model[(d["brand"], d["model"])][res] = (w * h, aspect)

    out = []
    for (brand, model), resmap in by_model.items():
        ranked = sorted(resmap.items(), key=lambda x: -x[1][0])
        for i, (res, (px, aspect)) in enumerate(ranked, 1):
            out.append({
                "brand": brand, "model": model, "rank": i, "resolution": res,
                "pixels": px, "aspect": aspect,
                "prefer_16_9": "Y" if aspect == "16:9" else "",
            })
    fields = ["brand", "model", "rank", "resolution", "pixels", "aspect", "prefer_16_9"]
    with open(os.path.join(BASE, "resolution_ladders.csv"), "w",
              encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    return out


# ---------------------------------------------------------------- 4. AI_PACK §3 数据区
def official_sections(official):
    brands = OrderedDict()
    for d in official:
        brands.setdefault(d["brand"], []).append(d)
    lines = []
    for brand, rows in brands.items():
        lines.append(f"### {brand}（{len(rows)} 条）")
        lines.append("")
        lines.append("| 机型 | 编码 | 分辨率 | 帧率 | GB/h |")
        lines.append("|---|:---:|:---:|:---:|---:|")
        for d in rows:
            res = d["resolution"].replace("x", "×") if re.search(r"\d+x\d+", d["resolution"]) else d["resolution"]
            lines.append(f"| {d['model']} | {d['codec']} | {res} | {d['fps']} | "
                         f"{d['gbh_binary']} |")
        lines.append("")
    return lines


def rewrite_pack(head_lines, tbl25, aliases, official):
    path = PACK
    with open(path, encoding="utf-8") as f:
        text = f.read()
    i = text.find(SEP25)
    j = text.find(SEP4)
    if i < 0 or j < 0 or j <= i:
        raise RuntimeError("AI_PACK.md 找不到 §3 / §4 分隔标记，拒绝改写")
    block = [SEP25, ""] + head_lines + ["", "### 3.1 25p 基准速查（客户没说帧率就用这张）", ""] \
        + tbl25 + ["", "### 3.2 别名对照（客户报的机型先过这张表，命中就直接出表）", ""] \
        + alias_table(aliases) + ["", "### 3.3 官方规格全集（按品牌，帧率为库内原始标注）", ""] \
        + official_sections(official) + ["---", ""]
    new = text[:i] + "\n".join(block) + text[j:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    return len(block)


def main():
    official = read_csv(OFFICIAL)
    anchors = read_csv(ANCHORS)
    rows25 = build_25p(official)
    aliases = build_aliases(official, anchors)
    ladders = build_ladders(official)

    head = [
        "**单位（对外）**：1 TB = 10¹² B ≈ 1000 GB，**取约数**；库内 GB/h 沿用二进制计算口径，"
        "两者差几个百分点属允许误差，不抠 1024。",
        "**帧率**：客户没说帧率一律按 **25p** 出表（用 §3.1 25p 基准表）；"
        "50p = 25p × 2；24p = 25p × 24/25；**库内已有对应帧率行优先取库内值**。",
        "**精度口径**：允许误差，直接按比例换算即可，不要因为换算值对不上就反复核对或向客户解释。"
        "现场多拍一分钟、少拍一分钟带来的偏差，比这点换算误差更大。",
        "**取数顺序**：客户说的机型名 → §3.2 别名表换成规范机型 → §3.1 取 25p 基准 → 出表。"
        "查到就答，禁止答「本库暂无」。",
    ]
    n = rewrite_pack(head, key_25p_table(rows25), aliases, official)
    print(f"specs_25p.csv      : {len(rows25)} 行")
    print(f"aliases.csv        : {len(aliases)} 行  "
          f"(model {sum(1 for x in aliases if x[2] == 'model')} / "
          f"brand {sum(1 for x in aliases if x[2] == 'brand')} / "
          f"family {sum(1 for x in aliases if x[2] == 'family')})")
    print(f"resolution_ladders : {len(ladders)} 行，"
          f"{len({(x['brand'], x['model']) for x in ladders})} 个机型")
    print(f"AI_PACK §3 重生成  : {n} 行")


if __name__ == "__main__":
    main()
