# 索引 · 拍摄格式码率资料库

本仓库是给 AI 索引的**公开拍摄格式 / 码率 / 数据量资料库**。**当前版本 v14 · 2026-11-14**。详见 [README.md](README.md)（含使用说明与客户回复口径）。

## 访问方式
- 库地址（raw 直读）：`https://raw.githubusercontent.com/1120575848-commits/camera-specs-db/main/`
- 国内网络常抓不到 raw（时断时续），用镜像：
  - jsDelivr（推荐）：`https://cdn.jsdelivr.net/gh/1120575848-commits/camera-specs-db@main/`
  - 代理：`https://ghproxy.net/https://raw.githubusercontent.com/1120575848-commits/camera-specs-db/main/`

## 文件导航
- `START_HERE.md`：**接入入口（3 KB，优先发这个）**——版本号 + 七条硬规则 + 开场白 + 数据指路。AI 抓不到大文件时先读它。
- `aliases.csv`：**别名单一真源**（口语机型 → 规范机型，品牌词 / 家族词单独标记不映射具体机型）。
- `specs_25p.csv`：**25p 基准换算表**（由 `build_kb.py` 从官方表生成，24p / 25p / 50p 三档预换算 + 对外十进制 TB 约数）。
- `resolution_ladders.csv`：机型 → 官方分辨率档位按像素降序（容量受限降档逐级向下、16:9 优先用）。
- `business_notes.md`：开票 / 存储卡 / 传输带宽 / DIT 劳务拓展口径（问到才给，无数据不编数字）。
- `regression_qa.md`：20 条固定问答回归集，每次改规则后逐条比对。
- `build_kb.py` / `check_rules.py`：派生数据生成 / 规则一致性门禁（**推送前必跑**）。
- `specs_official.csv` / `specs_official.json`：官网公开规格全集（**条数持续更新中**），含 MB/s、GB/h、GB/min、1TB 时长、实测对照、来源。
- `specs_measured.csv`：本项目 26 份报告的**实测格式**（品牌/机型/分辨率/双帧率/编码/码流/GB/h/样本数）。
- `measured_anchors.csv`：客户回复区间锚点（项目级每日数据量中位/平均/P90/最大 + 各机型满格式 GB/h）。
- `specs_devices.csv` / `specs_devices.json`：设备接口库（时码 TC / 麦克风 / 视频 SDI·HDMI 输出，按机型）。
- `AI_PACK.md`：**给不会抓链接的 AI 用的单文件包**（开场白 + 硬规则 + 3 列格式规范 + **25p 基准表 + 别名表 + 官方规格全集（§3 由 `build_kb.py` 自动生成）** + 容量/备份/报价口径 + 示范），一个文件自带全部内容，粘进系统提示或知识库即可。
- `hdd_prices.md` / `hdd_prices.csv`：**硬盘价格档案**（快照 2026-11-13）：我们这边 18/20 TB、企业盘、希捷桌面盘、PSSD、机械移动盘，单价 + ¥/TB + 渠道。渠道只有四个词（我们这边 / 京东自营 / 京东渠道店 / 京东海外购）；标「内部参考」的行只做内部核算、不对外报。客户问价格 / 型号 / 配盘多少钱时从这里取数。
- `README.md`：使用说明 + 客户回复口径（**移动端 3 列表**；合计行「N 天合计」+ 30 分钟·1 小时双口径、多机型混拍求和；**帧率默认 25p、50p ×2、24p ×24/25、1 TB=10¹² B 取约数、允许误差**；**工时 ≠ 机时**；容量建议**两档触发**——只问容量给 TB 和块数，问推荐/去哪买一次给全型号+渠道+价格；容量档**一档一档向上取** 4/5/8/10/12/14/16/18/20 TB、绝不跳档；常规封顶 3 块，**大项目可超 3 块并给两个并列方案+预算**；超时补盘固定句；渠道四词；别名先过表；分辨率按官方档位逐级降、16:9 优先；备份建议客户问到就给）+ 11 个 few-shot 示例。
- `AI_INSTRUCTIONS.md`：给接入 AI 的系统指令（开场白原话、取数路径、输出规范、索尼设置、多机位工作流）。

## 按品牌分片（大文件分拆，便于精准抓取避免截断）
- [ARRI（52 条）](specs_official_arri.md)
- [Apple（67 条）](specs_official_apple.md)
- [Atomos（2 条）](specs_official_atomos.md)
- [Blackmagic（30 条）](specs_official_blackmagic.md)
- [Canon（22 条）](specs_official_canon.md)
- [DJI（24 条）](specs_official_dji.md)
- [GoPro（2 条）](specs_official_gopro.md)
- [Nikon（14 条）](specs_official_nikon.md)
- [Panasonic（6 条）](specs_official_panasonic.md)
- [RED（15 条）](specs_official_red.md)
- [Sony（43 条）](specs_official_sony.md)

## 设备接口库（时码 TC / 麦克风 / 视频输出）
- [ARRI](specs_devices_arri.md) · [Sony](specs_devices_sony.md) · [Canon](specs_devices_canon.md) · [Blackmagic](specs_devices_blackmagic.md) · [DJI](specs_devices_dji.md) · [RED](specs_devices_red.md) · [Nikon](specs_devices_nikon.md) · [Panasonic](specs_devices_panasonic.md) · [Apple](specs_devices_apple.md) · [Atomos](specs_devices_atomos.md) · [GoPro](specs_devices_gopro.md)

## 技术文章归档（逃避梦DIT工作室原创）
- [`articles/`](articles/README.md)：公众号合集《技术分享与工作流》全部 17 篇原文（工作流／RAW 解码／达芬奇／ARRI LOOK／现场监看／DIT 访谈等），保留原标题与配图链接。经验性长文，不进 CSV 校验，仅作背景参考。

## 常见问法 → 去哪查
- 某格式一小时多少 G → `specs_official.csv`（GB/h 列）或对应品牌分片。
- 一天拍多少 / 推荐多大硬盘 → `measured_anchors.csv` + README 客户回复口径。
- 某机型满格式数据量 → `measured_anchors.csv` 的 CAMERA_MAX_GBH，或 `specs_official.csv` 按机型筛。
- 省空间对比（如 HDE）→ `specs_official.csv` 内 ARRIRAW 与 HDE 两行，或 README 示例。
- 某机型时码/麦克风/视频接口 → `specs_devices.csv` 或对应设备品牌分片。
