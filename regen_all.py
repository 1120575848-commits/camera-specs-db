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

# === 设备接口库：JSON + 品牌分片 ===
DEV_CSV = os.path.join(BASE, "specs_devices.csv")
DEV_JSON = os.path.join(BASE, "specs_devices.json")
if os.path.exists(DEV_CSV):
    DK = ["no", "brand", "model", "alias", "tc_connector", "tc_io", "mic_input",
          "mic_phantom", "sdi_count", "sdi_spec", "sdi_maxfmt", "hdmi", "genlock",
          "source", "note"]
    with open(DEV_CSV, newline="", encoding="utf-8") as f:
        devs = list(csv.DictReader(f))
    with open(DEV_JSON, "w", encoding="utf-8") as f:
        json.dump([{k: d.get(k, "") for k in DK} for d in devs], f, ensure_ascii=False, indent=2)
    print("设备库 JSON 重生成完成，条数:", len(devs))

    dgroups = OrderedDict()
    for d in devs:
        dgroups.setdefault(d["brand"], []).append(d)
    for brand, rows_d in dgroups.items():
        fn = os.path.join(BASE, f"specs_devices_{brand.lower()}.md")
        lines = [
            f"# {brand} · 设备接口库（时码/麦克风/视频输出）", "",
            "> 数据来源：各厂商官网规格页（核对 2026-11-13）。单位口径见主库 README。", "",
            "| 机型 | 别名 | 时码 TC 接口 | TC 输入/输出 | 麦克风/音频输入 | 幻象供电 | SDI 数量 | SDI 规格 | SDI 最高格式 | HDMI | Genlock | 备注 |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|",
        ]
        for d in rows_d:
            lines.append(
                f"| {d['model']} | {d['alias']} | {d['tc_connector']} | {d['tc_io']} | "
                f"{d['mic_input']} | {d['mic_phantom']} | {d['sdi_count']} | {d['sdi_spec']} | "
                f"{d['sdi_maxfmt']} | {d['hdmi']} | {d['genlock']} | {d.get('note','')} |")
        with open(fn, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    print("设备品牌分片重生成完成，品牌数:", len(dgroups),
          "| 各品牌:", {b: len(v) for b, v in dgroups.items()})
