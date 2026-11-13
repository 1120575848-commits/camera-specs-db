# 索引 · 拍摄格式码率资料库

本仓库是给 AI 索引的**公开拍摄格式 / 码率 / 数据量资料库**。详见 [README.md](README.md)（含使用说明与客户回复口径）。

## 访问方式
- 库地址（raw 直读）：`https://raw.githubusercontent.com/1120575848-commits/camera-specs-db/main/`

## 文件导航
- `specs_official.csv` / `specs_official.json`：官网公开规格全集（**条数持续更新中**），含 MB/s、GB/h、GB/min、1TB 时长、实测对照、来源。
- `specs_measured.csv`：本项目 26 份报告的**实测格式**（品牌/机型/分辨率/双帧率/编码/码流/GB/h/样本数）。
- `measured_anchors.csv`：客户回复区间锚点（项目级每日数据量中位/平均/P90/最大 + 各机型满格式 GB/h）。
- `specs_devices.csv` / `specs_devices.json`：设备接口库（时码 TC / 麦克风 / 视频 SDI·HDMI 输出，按机型）。
- `AI_PACK.md`：**给不会抓链接的 AI 用的单文件包**（开场白 + 硬规则 + 3 列格式规范 + 277 条速查数据 + 容量/备份/报价口径 + 示范），一个文件自带全部内容，粘进系统提示或知识库即可。
- `hdd_prices.md` / `hdd_prices.csv`：**硬盘价格档案**（快照 2026-11-13）：企业盘 8–20 TB、希捷桌面盘 8–16 TB、PSSD、机械移动盘，含税单价 + ¥/TB + 渠道；客户问价格 / 型号 / 配盘多少钱时从这里取数。
- `README.md`：使用说明 + 客户回复口径（**移动端 3 列表**：摄影机 / 拍摄格式 / 数据量；格内分段、全列居中、只加粗 TB 数字；合计行「N 天合计」+ 30 分钟·1 小时双口径；HDE 对比小表；容量建议（默认双备份、总量 ≥ 8 TB 转三备份、单组 1–2 块盘装完）；日数据 > 1 TB 才给备份建议（按 100 MB/s 估小时数））+ few-shot 示例。
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
