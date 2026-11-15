# 回溯 / 回滚说明（v19 · 2026-11-15）

> 本页给维护者看，**不对客户输出**。当前线上版本 **v19**；v18 是最后一次已验证稳定的基线。
> 如果改乱了、规则自相矛盾、或下游 AI 开始回旧口径，按下面任一条路径回到 v18，再慢慢改。

## 基线信息

| 项 | 值 |
|:---|:---|
| 基线版本 | **v18 · 2026-11-15** |
| 远端 tag | `v18-backup-20261115`（指向 v18 时的 `main` HEAD `65a99aae4996`） |
| 本地副本 | `/Users/admin/Desktop/camera-specs-db_v18_backup_20261115`（46 个顶层文件，完整副本） |
| 本地 git tag | `v18-backup-20261115`（本地 commit `8200044`） |
| 基线门禁 | `validate_db.py` HARD 0 / WARN 8；`check_rules.py` HARD 0 / WARN 0；回归集 44 条 |

## 路径 1：让下游 AI 立刻读回旧版（最快，不改任何文件）

把主转发链接里的 `main` 换成 tag 名即可，规则文本逐字节就是 v18：

```
https://ghproxy.net/https://raw.githubusercontent.com/1120575848-commits/camera-specs-db/v18-backup-20261115/START_HERE.md
https://raw.githubusercontent.com/1120575848-commits/camera-specs-db/v18-backup-20261115/README.md
```

`AI_PACK.md` / `AI_INSTRUCTIONS.md` / `hdd_prices.md` 等同理，把路径中的 `main` 换成 `v18-backup-20261115`。**注意缓存**：ghproxy / raw 的 `max-age=300`，切换后最长 5 分钟生效；**不要用 jsDelivr `@main`**（边缘缓存 12 小时）。

## 路径 2：本地整体还原

```bash
cd /Users/admin/Desktop
mv camera-specs-db camera-specs-db_v19_broken
cp -a camera-specs-db_v18_backup_20261115 camera-specs-db
cd camera-specs-db && python3 validate_db.py && python3 check_rules.py
```

或在仓库内用 git（本地 tag 是完整 v18 快照）：

```bash
cd /Users/admin/Desktop/camera-specs-db
git show v18-backup-20261115:README.md          # 查看单文件
git diff v18-backup-20261115 -- README.md       # 对比改动
git checkout v18-backup-20261115 -- README.md   # 单文件还原
```

## 路径 3：把远端 main 整体推回 v18

`python3 /tmp/gh_push_v14.py` 在哪个目录跑就把哪个目录的内容推上去。先 `cp -a` 还原到本地仓库目录，确认两道门禁全绿，再跑推送脚本；脚本会按 blob SHA 只推不同的文件，并用 API 逐字节核验。

> ⚠️ 推送脚本用的是 GitHub Contents API（钥匙串 PAT），**不是 git push**。本地 git 历史与远端 main 不同步属正常现象，不要试图 `git push` 覆盖远端。

## 每次改版的固定动作

1. 改文件前先给当前版本打远端 tag + 本地副本（脚本模板：`/tmp/backup_v18.py`）。
2. 改完跑 `python3 validate_db.py` 与 `python3 check_rules.py`，HARD 必须为 0。
3. 推送后做 `46+ / 46+` 逐字节核验，并复核 ghproxy / raw 文本入口（5 分钟缓存后重查一次）。
4. 更新本页的「基线信息」与工作记忆。

## 已知运维坑

- **jsDelivr `@main` 对规则文本有 12 小时边缘缓存**，purge 后实测仍发旧版；规则文本一律走 ghproxy / raw（`max-age=300`），静态二维码图片才走 `gcore.jsdelivr.net` 直出。
- `?v=` 参数破不了 raw / ghproxy 的缓存，只能等 5 分钟。
- 主转发**只发 ghproxy / raw 的 `START_HERE.md`**，不要发 GitHub 仓库主页。
