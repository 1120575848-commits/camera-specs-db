#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_rules.py — 规则一致性门禁（v14）
=====================================
推送前必跑：python3 check_rules.py

检查（HARD，任一失败退出码 1，阻断推送）：
  1. 版本号一致：五份规则文件都声明 README 顶部版本戳所定的当前版本，
     且没有把上一版当当前版本（版本号动态读取，--bump 后门禁自动跟随）
  2. 开场白逐字一致：README(§0 + 示范0) / AI_INSTRUCTIONS / AI_PACK / START_HERE
  3. 关键口径同步矩阵：一档一档 / 两档触发 / 工时≠机时 / 帧率换算 / 别名 /
     大项目双方案 / 超时补盘 / 允许误差，四份规则都要有
  4. 旧口径残留：误用移动机械硬盘、10.8 TB → 18 TB、2 块 8 TB、三件一起给…
  5. 容量档九档单价在 README / AI_INSTRUCTIONS / AI_PACK / hdd_prices.md 一致
  6. AI_PACK §3.3 官方规格全集与 specs_official.csv 逐行 0 差异
  7. 别名表：canonical 都能在官方表找到（ILME-FX5 为已知存疑白名单）；
     常见口语别名都出现在 AI_PACK §3.2 内嵌表
  8. 派生文件新鲜度：25p / 别名 / 档位表不早于 specs_official.csv
  9. 对外二维码链接一律走 jsDelivr，不留 raw 直链
 10. index.md 导航覆盖全部新文件；回归集存在且 ≥ 20 条

检查（WARN）：raw 直链仍出现在说明性文字里（备用地址允许，仅提醒）。
"""
import csv
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RULES = ["README.md", "AI_INSTRUCTIONS.md", "AI_PACK.md", "START_HERE.md", "index.md"]


def current_version(texts):
    """版本真源 = README 顶部的版本戳；--bump 后门禁自动跟随。"""
    m = re.search(r"本文件版本：(v\d+)", texts.get("README.md", ""))
    return m.group(1) if m else None

EXPECT_PRICES = {
    "¥1229": "4 TB", "¥1349": "5 TB", "¥2489": "8 TB",
    "¥3099": "10 TB", "¥3599": "12 TB", "¥3899": "14 TB",
    "¥3699": "16 TB", "¥5270": "18 TB", "¥6143": "20 TB",
}

KEY_MATRIX = {
    "README.md": ["一档一档", "两档触发", "工时 ≠ 机时", "25p", "aliases.csv",
                  "让客户自己选", "超时补盘", "允许误差", "specs_25p.csv"],
    "AI_INSTRUCTIONS.md": ["一档一档", "工时 ≠ 机时", "25p", "aliases.csv",
                           "让客户自己选", "超时补盘", "允许误差", "specs_25p.csv"],
    "AI_PACK.md": ["一档一档", "工时 ≠ 机时", "25p", "让客户自己选",
                   "超时补盘", "允许误差", "§3.2"],
    "START_HERE.md": ["一档一档", "工时 ≠ 机时", "25p", "aliases.csv",
                      "让客户自己选", "specs_25p.csv", "超时补盘", "七条硬规则"],
    "index.md": ["当前版本", "aliases.csv", "specs_25p.csv", "resolution_ladders.csv",
                 "business_notes.md", "check_rules.py", "regression_qa.md"],
}

BANNED = [
    "误用移动机械硬盘", "平均约 100 MB/s", "通用估算、非库内数据",
    "10.8 TB → 18 TB", "2 块 8 TB", "三份共 6 块",
    "三件一起给，缺一不可", "5 TB 最划算", "自有供货商",
    "只有2个2TB硬盘，能拍什么格式",
]

ALIAS_WHITELIST = ["A7S3", "悟3", "威尼斯2", "猛禽X", "狗13", "科莫多-X", "FX6", "阿莱", "小飞机"]


class Report:
    def __init__(self):
        self.hard = []
        self.warn = []

    def h(self, m):
        self.hard.append(m)

    def w(self, m):
        self.warn.append(m)


def read(fn):
    with open(os.path.join(BASE, fn), encoding="utf-8") as f:
        return f.read()


def norm_block(s):
    lines = [l.rstrip() for l in s.strip().splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def openings(text):
    """抓出文件里所有开场白实例（含示范 0 / 短入口页）。"""
    # 只认含「比如您可以问」的完整开场白，跳过 §0 里那句「不要复读已接到…」的引用
    return [norm_block(m) for m in re.findall(
        r"已接到逃避梦.*?(?=\n```|\n\s*> 之后用户|\n## 3\.|\n---|\Z)", text, re.S)
        if "比如您可以问" in m]


def check_version(rep, texts):
    version = current_version(texts)
    if not version:
        rep.h("[版本] README.md 顶部找不到「本文件版本：vN」版本戳，无法判定当前版本")
        return
    try:
        prev = "v%d" % (int(version[1:]) - 1)
    except ValueError:
        prev = None
    for fn in RULES:
        t = texts[fn]
        if version not in t:
            rep.h(f"[版本] {fn} 没有声明 {version}")
        if prev and re.search(r"版本[^\n]{0,20}" + re.escape(prev), t):
            rep.h(f"[版本] {fn} 仍把 {prev} 写成当前版本")
    idx = texts.get("index.md", "")
    if f"当前版本 {version}" not in idx:
        rep.h(f"[版本] index.md 没有写「当前版本 {version}」")
    print(f"  ✓ 当前版本 {version}（真源 = README 顶部版本戳）")


def check_opening(rep, texts):
    all_blocks = {}
    for fn in ["README.md", "AI_INSTRUCTIONS.md", "AI_PACK.md", "START_HERE.md"]:
        blocks = openings(texts[fn])
        if not blocks:
            rep.h(f"[开场白] {fn} 找不到开场白")
            continue
        all_blocks[fn] = blocks
        if len(blocks) < (2 if fn == "README.md" else 1):
            rep.h(f"[开场白] {fn} 开场白实例数不足：{len(blocks)}")
    if not all_blocks:
        return
    base = all_blocks.get("README.md", [None])[0]
    if not base:
        return
    for fn, blocks in all_blocks.items():
        for i, b in enumerate(blocks, 1):
            if b != base:
                rep.h(f"[开场白] {fn} 第 {i} 处与 README 不一致"
                      f"（{len(b.splitlines())} 行 vs {len(base.splitlines())} 行）")
    if "只有2个2TB硬盘" in base or "能拍什么格式" in base:
        rep.h("[开场白] 仍是旧版引导（含容量反推格式的例子）")
    if "几台、什么型号" not in base:
        rep.h("[开场白] 没有引导客户说清「几台什么型号」")


def check_matrix(rep, texts):
    for fn, keys in KEY_MATRIX.items():
        for k in keys:
            if k not in texts[fn]:
                rep.h(f"[同步] {fn} 缺少关键口径「{k}」")
    for fn in RULES:
        # 版本头的「旧版自检标记」本来就要列出旧句，检查时剥离开头的元信息区
        body = texts[fn].split("\n---\n", 1)[-1]
        for bad in BANNED:
            if bad in body:
                rep.h(f"[残留] {fn} 仍含旧口径「{bad}」")


def check_prices(rep, texts):
    for fn in ["README.md", "AI_INSTRUCTIONS.md", "AI_PACK.md", "hdd_prices.md"]:
        t = texts.get(fn) or read(fn)
        for price, cap in EXPECT_PRICES.items():
            if price not in t:
                rep.h(f"[价格档] {fn} 缺少 {cap} 的单价 {price}")
    # README / AI_INSTRUCTIONS / AI_PACK 三张档位表措辞一致
    for fn in ["README.md", "AI_INSTRUCTIONS.md", "AI_PACK.md"]:
        if "8 TB 的数据就给 8 TB" not in texts[fn] and "不许直接给 18 TB" not in texts[fn]:
            rep.h(f"[容量档] {fn} 缺少「绝不跳档」的判据")


def check_pack_data(rep, pack):
    """AI_PACK §3.3 官方全集必须与 specs_official.csv 逐行一致。"""
    if "### 3.3 官方规格全集" not in pack:
        rep.h("[数据] AI_PACK.md 找不到 §3.3 官方规格全集（请先跑 build_kb.py）")
        return
    sec = pack.split("### 3.3 官方规格全集", 1)[1].split("\n---\n", 1)[0]
    packrows = []
    for line in sec.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) == 5 and c[0] not in ("机型", ""):
            packrows.append(tuple(c))
    with open(os.path.join(BASE, "specs_official.csv"), encoding="utf-8-sig") as f:
        csvrows = []
        for r in csv.DictReader(f):
            res = r["resolution"]
            if re.search(r"\d+x\d+", res):
                res = res.replace("x", "×")
            csvrows.append((r["model"], r["codec"], res, r["fps"], r["gbh_binary"]))
    ps, cs = set(packrows), set(csvrows)
    if len(ps) != len(packrows):
        rep.w(f"[数据] AI_PACK §3.3 有 {len(packrows)-len(ps)} 行重复")
    missing, extra = cs - ps, ps - cs
    if missing:
        rep.h(f"[数据] CSV 有而 AI_PACK §3.3 无：{len(missing)} 行，例 {list(missing)[:2]}")
    if extra:
        rep.h(f"[数据] AI_PACK §3.3 有而 CSV 无：{len(extra)} 行，例 {list(extra)[:2]}")
    if not missing and not extra:
        print(f"  ✓ AI_PACK §3.3 与 CSV 逐行一致（{len(csvrows)} 行）")


def check_aliases(rep, pack):
    path = os.path.join(BASE, "aliases.csv")
    if not os.path.exists(path):
        rep.h("[别名] 找不到 aliases.csv（请先跑 build_kb.py）")
        return
    with open(path, encoding="utf-8-sig") as f:
        aliases = list(csv.DictReader(f))
    with open(os.path.join(BASE, "specs_official.csv"), encoding="utf-8-sig") as f:
        models = {r["model"] for r in csv.DictReader(f)}
    allowed = {"ILME-FX5"}  # 报告代号，库内已标「待人工修正」
    bad = sorted({a["canonical"] for a in aliases
                  if a["kind"] == "model" and a["canonical"]
                  and a["canonical"] not in models and a["canonical"] not in allowed})
    if bad:
        rep.h(f"[别名] canonical 指向库内不存在的机型：{bad}")
    if "### 3.2 别名对照" not in pack:
        rep.h("[别名] AI_PACK §3.2 内嵌别名表缺失")
        return
    sec = pack.split("### 3.2 别名对照", 1)[1].split("### 3.3", 1)[0]
    flat = sec.replace(" ", "")
    for a in ALIAS_WHITELIST:
        if a.replace(" ", "") not in flat:  # 「猛禽X」与「猛禽 X」视为同一称呼
            rep.h(f"[别名] AI_PACK §3.2 内嵌表缺常见口语别名「{a}」")
    print(f"  ✓ 别名表 {len(aliases)} 行，AI_PACK 内嵌表同步")


def check_freshness(rep):
    src = os.path.join(BASE, "specs_official.csv")
    t0 = os.path.getmtime(src)
    for fn in ["specs_25p.csv", "aliases.csv", "resolution_ladders.csv"]:
        p = os.path.join(BASE, fn)
        if not os.path.exists(p):
            rep.h(f"[新鲜度] 缺少 {fn}，请跑 python3 build_kb.py")
        elif os.path.getmtime(p) < t0:
            rep.h(f"[新鲜度] {fn} 早于 specs_official.csv，请跑 python3 build_kb.py")


def check_links_and_nav(rep, texts):
    for fn in ["README.md", "AI_INSTRUCTIONS.md", "AI_PACK.md"]:
        for m in re.finditer(r"https?://[^\s)]*qrcode_wechat\.jpg", texts[fn]):
            if "cdn.jsdelivr.net" not in m.group(0):
                rep.h(f"[链接] {fn} 二维码仍是 raw 直链：{m.group(0)[:70]}")
    idx = texts["index.md"]
    for fn in ["START_HERE.md", "aliases.csv", "specs_25p.csv",
               "resolution_ladders.csv", "business_notes.md",
               "regression_qa.md", "build_kb.py", "check_rules.py", "AI_PACK.md"]:
        if fn not in idx:
            rep.h(f"[导航] index.md 没有列出 {fn}")
    qa = os.path.join(BASE, "regression_qa.md")
    if not os.path.exists(qa):
        rep.h("[回归] 缺少 regression_qa.md")
    else:
        with open(qa, encoding="utf-8") as f:
            n = len(re.findall(r"^\| \d+ \|", f.read(), re.M))
        if n < 20:
            rep.h(f"[回归] regression_qa.md 只有 {n} 条，要求 ≥ 20 条")
        else:
            print(f"  ✓ 回归集 {n} 条")


def main():
    rep = Report()
    texts = {}
    for fn in RULES + ["hdd_prices.md"]:
        p = os.path.join(BASE, fn)
        if not os.path.exists(p):
            rep.h(f"[文件] 缺少 {fn}")
        else:
            texts[fn] = read(fn)
    if rep.hard:
        for m in rep.hard:
            print("  [HARD] " + m)
        return 1

    print("== 1. 版本号 ==")
    check_version(rep, texts)
    print("== 2. 开场白逐字一致 ==")
    check_opening(rep, texts)
    print("== 3. 关键口径同步 / 旧口径残留 ==")
    check_matrix(rep, texts)
    print("== 4. 容量档单价 ==")
    check_prices(rep, texts)
    print("== 5. AI_PACK §3 与 CSV ==")
    check_pack_data(rep, texts["AI_PACK.md"])
    print("== 6. 别名表 ==")
    check_aliases(rep, texts["AI_PACK.md"])
    print("== 7. 派生文件新鲜度 ==")
    check_freshness(rep)
    print("== 8. 链接与导航 ==")
    check_links_and_nav(rep, texts)

    print("\n================= 门禁摘要 =================")
    for m in rep.hard:
        print("  [HARD] " + m)
    for m in rep.warn:
        print("  [WARN] " + m)
    print(f"\n  HARD 错误: {len(rep.hard)} | WARN: {len(rep.warn)}")
    if rep.hard:
        print("  → 规则不一致，禁止推送。修好后重跑。")
        return 1
    print("  → 全绿，可以推送。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
