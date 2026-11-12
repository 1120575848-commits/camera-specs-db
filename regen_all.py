#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""regen_all.py — 由 specs_official.csv 重新生成 JSON + 品牌分片（不含追加）。"""
import csv, json, os
from collections import OrderedDict

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, "specs_official.csv")
JSON = os.path.join(BASE, "specs_official.json")

with open(CSV, newline="", encoding="utf-8") as f:
    allr = list(csv.DictReader(f))

# === JSON (16 键，无 trained) ===
out = [{
    "no": d["no"], "brand": d["brand"], "model": d["model"], "alias": d["alias"],
    "codec": d["codec"], "res": d["resolution"], "fps": d["fps"], "off": d["official_rate"],
    "mbs": d["mbs_binary"], "gbh": d["gbh_binary"], "gbm": d["gbm_binary"],
    "tb": d["tb_record_time"], "covered": d["covered"], "meas": d["measured_cmp"],
    "src": d["source"], "note": d["note"],
} for d in allr]
with open(JSON, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("JSON 重生成完成，条数:", len(out))

# === 品牌分片 ===
brands = OrderedDict()
for d in allr:
    brands.setdefault(d["brand"], []).append(d)
for brand, rows_b in brands.items():
    fn = os.path.join(BASE, f"specs_official_{brand.lower()}.md")
    lines = [
        f"# {brand} · 官网公开拍摄格式规格（附录 B）", "",
        "> 数据来源：厂商官网（Apple/ARRI/Sony/RED/Blackmagic/Canon/DJI/Nikon/Panasonic/GoPro/Atomos）｜核对 2026-11-12。",
        "> 单位：MB/s 为二进制(1024²B)；GB/h = MB/s × 3600 ÷ 1024；1TB 按 10¹² B。", "",
        "| 机型 | 别名 | 编码 | 分辨率 | 帧率 | 官方码率 | MB/s | GB/h | GB/min | 1TB时长 | 覆盖 | 实测对照 | 来源 |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for d in rows_b:
        lines.append(
            f"| {d['model']} | {d['alias']} | {d['codec']} | {d['resolution']} | {d['fps']} | "
            f"{d['official_rate']} | {d['mbs_binary']} | {d['gbh_binary']} | {d['gbm_binary']} | "
            f"{d['tb_record_time']} | {d['covered']} | {d['measured_cmp']} | {d['source']} |")
    with open(fn, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
print("品牌分片重生成完成，品牌数:", len(brands), "| 各品牌:", {b: len(v) for b, v in brands.items()})
