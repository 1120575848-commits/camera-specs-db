# 索引 · 拍摄格式码率资料库

本仓库是给 AI 索引的**公开拍摄格式 / 码率 / 数据量资料库**。详见 [README.md](README.md)（含使用说明与客户回复口径）。

## 文件导航
- `specs_official.csv` / `specs_official.json`：官网公开规格全集（202 条），含 MB/s、GB/h、GB/min、1TB 时长、实测对照、来源。
- `specs_measured.csv`：本项目 26 份报告的**实测格式**（品牌/机型/分辨率/双帧率/编码/码流/GB/h/样本数）。
- `measured_anchors.csv`：客户回复区间锚点（项目级每日数据量中位/平均/P90/最大 + 各机型满格式 GB/h）。
- `README.md`：使用说明 + 客户回复口径（单位TB化、三数区间、区间失效反问、默认小时假设、必带2TB换算）+ few-shot 示例。

## 按品牌分片（大文件分拆，便于精准抓取避免截断）
- [ARRI（19 条）](specs_official_arri.md)
- [Apple（67 条）](specs_official_apple.md)
- [Atomos（2 条）](specs_official_atomos.md)
- [Blackmagic（23 条）](specs_official_blackmagic.md)
- [Canon（15 条）](specs_official_canon.md)
- [DJI（13 条）](specs_official_dji.md)
- [GoPro（2 条）](specs_official_gopro.md)
- [Nikon（8 条）](specs_official_nikon.md)
- [Panasonic（6 条）](specs_official_panasonic.md)
- [RED（15 条）](specs_official_red.md)
- [Sony（32 条）](specs_official_sony.md)

## 常见问法 → 去哪查
- 某格式一小时多少 G → `specs_official.csv`（GB/h 列）或对应品牌分片。
- 一天拍多少 / 推荐多大硬盘 → `measured_anchors.csv` + README 客户回复口径。
- 某机型满格式数据量 → `measured_anchors.csv` 的 CAMERA_MAX_GBH，或 `specs_official.csv` 按机型筛。
- 省空间对比（如 HDE）→ `specs_official.csv` 内 ARRIRAW 与 HDE 两行，或 README 示例。
