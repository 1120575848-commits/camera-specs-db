# 摄影机素材打不开？拖达芬奇只有音频？iPhone、4D、Alexa35、ZR、FX5的RAW解码收藏级达芬奇版本速查指南

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247485635&idx=1&sn=cf7694c5a281e44991894f7a1128926d&chksm=fc04682fcb73e139b83f76b9bba411193d42b36cf84360d9d45507ea47cbb95680e1ed4575ef#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---

先弄懂一个本质问题：RAW 是素材，但不是一个「视频文件」，普通交付片（H.264、ProRes 422）是已经「做熟」的菜，几乎任何软件都能直接播，但 RAW 是「生鲜食材」——它记录的是传感器原始光信号，必须经过专门的解码器才能变成画面。而每家厂商的 RAW 算法都不一样，而且也是在不断迭代更新，达芬奇就得一个个版本去「认」。所以基本遇到「在达芬奇打不开，显示只有音频」，能拖进去却「只有声音、没有画面」，那就是你手上的达芬奇版本，还没学会解这台机器拍的 RAW。

很多时候达芬奇会第一时间去兼容解码最新的RAW，往往第一时间更新软件即可完成对该新摄影机拍摄RAW格式的解码，但达芬奇软件都是需要主动去官方更新，大部分后期工作人员一般不会有事没事就去更新一些小版本的的达芬奇，但在拍摄现场的导演和摄影指导们对于新摄影机和新格式相当热忱，往往非常希望更早去认识和尝试，而这个月发布的Sony FX5 开创行业先河：全球首款机内直接录制 16-bit 场景线性 X-OCN（LT / C1 / C2）的电影机，宽容度与调色空间一步到位，甚至在深圳的摄影器材公司里，FX3会和FX5一起混出，在未来会愈来愈多的人会来问FX5 X-OCN达芬奇什么最低版本可以打开。

Sony FX5的番外注意事项





FX5时间码接口，与FX3或其他摄影机都不一样，用的是 USB-C 转 BNC 适配线（与GoPro也不同），VMC-BNCU1 时间码适配电缆（折合600-650人民币），FX5 的 USB Type-C 端口（PORT1） 输入，用于多机位拍摄和同期录音LTC同步。




ProRes RAW的番外篇知识拓展

在2018年4月苹果就正式发布 ProRes RAW，但直到2025 年 9 月之前长达七年的时间里，达芬奇也没有去兼容解码 ProRes RAW，因此很长时间该格式备受排挤，原因可以理解Apple ProRes RAW和BMD RAW处于定位完全统一的竞争关系，很长一段时间里Apple ProRes RAW是最不受待见的一个格式，因为你的达芬奇调色师没有办法在达芬奇里直接打开ProRes RAW素材。

好在很长一段时间ProRes RAW鲜为人知的转折点发生在2025 年 3 月 31 日。DJI PRO公众号发文官宣全新售价，同步推出 DJI Ronin 4D RAW 授权1元限时优惠， Inspire 3 的 RAW 授权直接 0 元送，而原先使用授权为5999人民币，现在基本等于白送。同批的整机降价，Ronin 4D-6K：¥43888 → ¥32888，Ronin 4D-8K：¥84887 → ¥6799，越来越多的由Ronin 4D和 Inspire 3 产出6K/8K的ProRes RAW生根发芽，野蛮生长。

2025年4月开始仍然Apple ProRes RAW无法在达芬奇等软件正常解码，一般需要转中间格式（DNG RAW、4444、422HQ）再正常跑标准工作流，我们的DIT标准服务也是涵盖转4444或者422HQ的，其中DNG RAW序列帧在后期工作流程会存在时码异常的情况，无法准确回批，其数据量转码之后也是 ProRes RAW源素材的2-3倍，这种高分辨率的RAW转RAW也是DIT的至暗时刻之一。

直到DaVinci Resolve 20.2（2025 年 9 月，IBC 2025 前后）首次加入原生支持，关键节点是iPhone 17 Pro系列全面推出Apple ProRes RAW录制，BMD推出专为iPhone设计的拍摄手柄套件和Blackmagic Cam App。

![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msFjzdOJk7U2UUyTlU3tpRzRL3FWQjhzaEF97OtUw6ia5qcHEFGib22APcTZe27DulD9n9nFicUfCevMvWza1ZticiaC4ZmEQ8siczghU/640?wx_fmt=png&from=appmsg#imgIndex=0)
![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msHKmFjMjJorULp1icxNicu7YdCYP0uqhicYdOWfFSEiamhSfYZ3VY8nsL7JxggSyC9s8udc7pkNIAytDaGoBm9vnVD8vNsQNxHJcXM/640?wx_fmt=png&from=appmsg#imgIndex=1)
