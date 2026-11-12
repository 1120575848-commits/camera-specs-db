# DJI · 官网公开拍摄格式规格（附录 B）

> 数据来源：厂商官网（Apple/ARRI/Sony/RED/Blackmagic/Canon/DJI/Nikon/Panasonic/GoPro/Atomos）｜核对 2026-11-12。
> 单位：MB/s 为二进制(1024²B)；GB/h = MB/s × 3600 ÷ 1024；1TB 按 10¹² B。

| 机型 | 别名 | 编码 | 分辨率 | 帧率 | 官方码率 | MB/s | GB/h | GB/min | 1TB时长 | 覆盖 | 实测对照 | 来源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ronin 4D | 大疆如影4D / R4D | ProRes RAW 8K Full Frame | 8192x4320 | 24p | 405 MB/s（官方摄录规格表 @ 24p） | 386.24 | 1357.9 | 22.63 | 41 min | ✓ 有实测 | 1,278.2（-5.9%） | N24 |
| Ronin 4D | 大疆如影4D / R4D | ProRes RAW 8K Full Frame | 8192x4320 | 60p | 修正：ProRes RAW 8K FF 单帧恒为 16.09 MiB，60p = 386.24×60/24 = 965.60 MB/s（原 482.56 实为 30p 误标 60p） | 965.60 | 3394.7 | 56.58 | 16 min（1TB @60fps） | ○ 机型有 · 此档未覆盖 | — | N24 |
| Ronin 4D X9-8K | 大疆如影4D / R4D | ProRes 422 HQ 8K Full Frame | 8192x4320 | 25p | 375 MB/s（官方摄录规格表 @ 25p） | 357.63 | 1257.3 | 20.95 | 44 min | ○ 机型有 · 此档未覆盖 | — | N24 |
| Ronin 4D X9-8K | 大疆如影4D / R4D | ProRes 422 HQ 4K Full Frame | 3840x2160 | 25p | 90 MB/s（官方摄录规格表 @ 25p） | 85.83 | 301.7 | 5.03 | 3h 05m | ✓ 有实测 | 298.6（-1.0%） | N24 |
| Ronin 4D X9-8K | 大疆如影4D / R4D | H.264 4K Full Frame | 3840x2160 | 25p | 18 MB/s（官方摄录规格表 @ 25p） | 17.17 | 60.3 | 1.01 | 15h 25m | ○ 机型有 · 此档未覆盖 | — | N24 |
| Ronin 4D X9-6K | 大疆如影4D 6K / R4D-6K | ProRes RAW 6K Full Frame | 6008x3168 | 25p | 227 MB/s（官方摄录规格表 @ 25p） | 216.48 | 761.1 | 12.68 | 1h 13m | ★ 训练数据未覆盖（新增） | — | N24 |
| Ronin 4D X9-6K | 大疆如影4D 6K / R4D-6K | ProRes 4444 XQ 6K Full Frame | 6008x3168 | 25p | 453 MB/s（官方摄录规格表 @ 25p） | 432.01 | 1518.8 | 25.31 | 37 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Ronin 4D X9-6K | 大疆如影4D 6K / R4D-6K | ProRes 422 HQ 6K Full Frame | 6008x3168 | 25p | 202 MB/s（官方摄录规格表 @ 25p） | 192.64 | 677.3 | 11.29 | 1h 22m | ★ 训练数据未覆盖（新增） | — | N24 |
| Ronin 4D X9-6K | 大疆如影4D 6K / R4D-6K | ProRes 422 LT 6K Full Frame | 6008x3168 | 25p | 94 MB/s（官方摄录规格表 @ 25p） | 89.65 | 315.2 | 5.25 | 2h 57m | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | CinemaDNG 8.1K Full Frame | 8192x4320 | 25p | 844 MB/s（官方摄录规格表 @ 25p） | 804.9 | 2829.7 | 47.16 | 20 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | ProRes RAW 8.1K Full Frame | 8192x4320 | 25p | 422 MB/s（官方摄录规格表 @ 25p） | 402.45 | 1414.9 | 23.58 | 39 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | ProRes 422 HQ 8.1K Full Frame | 8192x4320 | 25p | 375 MB/s（官方摄录规格表 @ 25p） | 357.63 | 1257.3 | 20.95 | 44 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | H.264 4.1K Full Frame | 4096x2160 | 25p | 18 MB/s（官方摄录规格表 @ 25p） | 17.17 | 60.3 | 1.01 | 15h 25m | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | CinemaDNG 8K Full Frame | 8192x4324 | 25p | 791 MB/s（官方摄录规格表 @ 25p） | 754.36 | 2652.0 | 44.2 | 23 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | ProRes RAW 8K Full Frame | 8192x4324 | 25p | 396 MB/s（官方摄录规格表 @ 25p） | 377.65 | 1327.7 | 22.13 | 45 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | ProRes 422 HQ 8K Full Frame | 8192x4324 | 25p | 336 MB/s（官方摄录规格表 @ 25p） | 320.43 | 1126.5 | 18.77 | 53 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | CinemaDNG 5.5K S35 | 5568x2952 | 25p | 392 MB/s（官方摄录规格表 @ 25p） | 373.84 | 1314.3 | 21.9 | 46 min | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | ProRes RAW 5.5K S35 | 5568x2952 | 25p | 196 MB/s（官方摄录规格表 @ 25p） | 186.92 | 657.1 | 10.95 | 1h 31m | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | CinemaDNG 4K Full Frame | 4096x2160 | 25p | 197 MB/s（官方摄录规格表 @ 25p） | 187.87 | 660.5 | 11.01 | 1h 31m | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | ProRes RAW 4K Full Frame | 4096x2160 | 25p | 99 MB/s（官方摄录规格表 @ 25p） | 94.41 | 331.9 | 5.53 | 3h 01m | ★ 训练数据未覆盖（新增） | — | N24 |
| Inspire 3 / X9-8K Air | 悟3 / 大疆 Inspire 3 | ProRes 422 HQ 4K Full Frame | 4096x2160 | 25p | 88 MB/s（官方摄录规格表 @ 25p） | 83.92 | 295.0 | 4.92 | 3h 23m | ★ 训练数据未覆盖（新增） | — | N24 |
| Ronin 4D | 如影 4D / Ronin 4D | ProRes RAW 8K FF | 8192x4320 | 24p | DJI 官方 Ronin 4D X9-8K ProRes RAW 8K @24p 码率 405 MB/s（十进制） | 386.24 | 1357.9 | 22.63 | 41 min（1TB @对应帧率） | ○ 机型有 · 此档未覆盖 | — | N28 |
| Ronin 4D | 如影 4D / Ronin 4D | ProRes 422 HQ 8K FF | 8192x4320 | 24p | DJI 官方 Ronin 4D X9-8K ProRes 422 HQ 8K @24p 码率 360 MB/s（十进制） | 343.32 | 1207.0 | 20.12 | 46 min（1TB @对应帧率） | ○ 机型有 · 此档未覆盖 | — | N28 |
| Ronin 4D | 如影 4D / Ronin 4D | ProRes RAW 4K FF | 4096x2160 | 24p | DJI 官方 Ronin 4D X9-8K ProRes RAW 4K @24p 码率 101 MB/s（十进制） | 96.32 | 338.6 | 5.64 | 2h45m（1TB @对应帧率） | ○ 机型有 · 此档未覆盖 | — | N28 |
