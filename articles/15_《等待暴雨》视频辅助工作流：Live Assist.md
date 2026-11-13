# 《等待暴雨》视频辅助工作流：Live Assist

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247484408&idx=1&sn=d58f834108bf733385bb18131a9b2dc2&chksm=fc046314cb73ea027c8ad1e92405174748d3a282035931b72213a5f5340e2c524ff8af44b486#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---

前言：本文权当工作经验分享，欢迎指正交流！

场记老师：侯元惠
流程搭建

   尽管《等待暴雨》剧组使用ARRI ALEXA MINI单机进行拍摄，但是预算方面还是与大部分学生剧组的情况相似：一如既往地捉襟见肘。但是没关系，他们找到的DIT是我。
秉承着用爱发电的理念，作为乞讨拷卡的DIT，我依旧持着“助力中国青年电影”的傻白甜精神，在剧组开机前的一个星期，为导演组设计了一套现场实时回放系统。



Assilmilate Live Assist与 Live Looks现场视频辅助工作流程图
1、监看系统与信号管理。本次带出组的监视器是尊正DM211，用于现场色准参考辅助。由于现场图传数量仅支持一发两收（摄影大助跟焦+监视器接收），所有的色空间输出仅为Rec 709。由于乞讨拷卡，我并没有BMD雷电三的Mini Recorder，所以使用了一个价格仅为30rmb，支持1080p60规格的HDMI to USB3.0的不知名采集卡。HDMI从图传接入采集卡后，经过Live Assist中设置视频IO即可实时抓取图传信号，再通过上屏卡的连接输出至DM211，从DM211走一路环出(Loop out)至导演监视器。



黎明晖现场DIT On-set
2、数字资产管理。三备二介一异地，我使用两块4TB机械硬盘组建Raid 0阵列，保证一份现场完整的备份。固态硬盘方面使用4TB+2TB+1TB的搭配，保证Offload效率的情况下同时兼顾Live Assist的现场信号录制空间。后场驻地的备份使用三块导演提供的西数8TB红盘作为三个单一备份。
3、DIT数据备份软件方面。我使用的是磁带王Yoyotta！Yoyotta最初是为了给LTO磁带备份设计的，同时，这款软件也适合现场DIT的Offload与Verify流程。通常第一现场我使用的是MD5+xxHash的完整校验模式，驻地的备份则使用xxHash的快速校验模式。在校验过程中，Yoyotta会自动生成带有首尾帧缩略图的校验报告，里面包含了各项素材元数据信息与校验和（Checksum），还可以自定义生成ALE、CSV、MHL等元数据信息与校验报告。


Live Assist：回放的实际使用
Live Assist顾名思义就是现场实时视频辅助，负责信号的回放以供导演实时回看画面。可能大多数学生剧组习惯从掌机处 手动回放 读取素材，其本质即是读取储存卡中的数据，通过图传发送到导演监视器上进行回放。
其中可能存在的缺点有
1）增加储存卡的读取次数，减少储存卡寿命。（貌似问题不大但确实是有影响...）
2）手动回放过程相对繁琐，快进帧与倒退帧的控制无法精准停落。
3）导演需要通过三方或对讲发出指令等待掌机回放，指令发出接收有一定的时间差。若是信号状况较差，后场的导演可能会与片场前方失去联系（不要跟我说没有！）
4）在未输出代理之前，导演若想看之前的素材回放，就只能真的傻傻等代理！sorry～

Live Assist工作界面：图为回放状态
Live Assist怎么工作？
设置好视频IO 和 代理录制的路径与格式（推荐422Proxy）后，左侧上方的通道控制器可输入对应的场镜次用作代理的区分。按下“录像”键后，软件将录制图传信号来源并实时编码保存至设定好的路径文件夹下。每当需要回放时，仅需点击区分好的场景次条数即可实时播放录制素材。
注意，这一个过程与机内素材毫无任何关系，仅仅是图传信号的录制素材！
实时视频辅助的好处：
1）其与储存卡素材毫无关联，仅仅为图传信号的录制素材。即使摄影机关机，系统也可以追溯素材进行回放。
2）DIT实时控制回放区间与段落，能够精准停落某一帧以查看 穿帮 或者 关键画面帧。
3）整个过程中，DIT与导演位于后场。导演无需与前方沟通，能够非常有效地提高导演现场工作效率，为掌机老师争取“歇口气”的机会，更进一步压缩“垃圾时间”。
4）无需等待代理的生成，随时查看任何场次任何天数的任何素材。


Live Assist：实时调色的实际使用

Assist中的调色特效面板，包含基本的实时调色、合成、CDLs与Luts生成等功能。
在《等待暴雨》拍摄的第一场戏中，我们就碰到了大面积染色的情况。由于办公室的外幕玻璃封贴了一层淡绿色的窗膜，场景出现大面积染色导致人物肤色与白色参照物在监视器中整体偏色，对灯光指导的布光造成一定的难度。
于是，我对整个画面进行基础的校色以给导演参考相对白净透亮的视觉效果。

实时调色前的预览

基本校正后的视觉参考（仅参考，没啥用）


我给学生剧组搭建Assimilate现场视频辅助工作流的意义
   1）从我初出茅庐的工作经验出发，我依旧认为国内剧组普遍对于DIT岗位的认知严重不足、误解尤为严重。可能很多人对于DIT的认知停留在数据管理方面，也就是“拷卡”。当然，我不是说“拷卡”不那么重要，数据管理是DIT最基本的工作内容，也是整个过程中要求最为严谨的环节。但貌似DIT的工作内容不只局限于数据管理，从最基础最重要的数字资产管理，到进阶的信号管理分发、视频辅助回看、实时调色、蓝绿幕抠像、FX合成 到 整体的DIT工作流程设计等都是数字影像工程师们必须不断进化学习的内容。
  2）相较于Qtake流程，对于学生组来说Assimilate Live Assist仅仅是够用、刚好合适用的程度。Qtake高昂的租赁费用不是一般学生组能够承担的，说到底我还是希望学生剧组也能够用得上相对便宜、配套要求相对较低的回放系统。
3）用过都说好........吧。至少拍到最后一两天，很多学生导演对于这套系统的心态变化是从陌生到习惯再到依赖的。



On-set


End.....
最后说一句，DIT隶属摄影组。



![](https://mmbiz.qpic.cn/sz_mmbiz_png/fuZ9aarx42QQ6uetPUe8cnecf8baZ7uWpCEicnpDwAd3czdanpmIlkvlPTUDrBm54tSxVRh2VqNzBT5J4OqkLHA/640?wx_fmt=png#imgIndex=0)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fuZ9aarx42QQ6uetPUe8cnecf8baZ7uWnjkhGbYLvsckxw0NeO1bEMsEdIYmia88XwM4b3DT2d3eC8MNaVOZqOQ/640?wx_fmt=jpeg#imgIndex=1)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fuZ9aarx42SInVGs7rEpgGOTJ2ibGQicRK7BedflBxspSJDETicqwliar4nUy46jYBnZ2otXAFsK5jibIPAZmDE74XA/640?wx_fmt=jpeg#imgIndex=2)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fuZ9aarx42SInVGs7rEpgGOTJ2ibGQicRKV1Waxky3ewxnRDkDwf9hNnJoGMTTLQrJ4zMLgn2V1UbE4iaY9aMWibbQ/640?wx_fmt=jpeg#imgIndex=3)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fuZ9aarx42QQ6uetPUe8cnecf8baZ7uWFlhMvC6NKctZzYEU3U9Cc2Qic6iah9vgPfJiaUYr51a64EWOlyjAR8JCw/640?wx_fmt=png#imgIndex=4)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fuZ9aarx42QQ6uetPUe8cnecf8baZ7uWqR4g8FoyuicibKCHwrtFdpcnXds6nx7AV3VZKiac655HuX3GiaovY25jfw/640?wx_fmt=png#imgIndex=5)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fuZ9aarx42SInVGs7rEpgGOTJ2ibGQicRK68Flm0rX9LQc2Lmp3mkUxd5NpLlO90rTtVicee5EFzw0R7h7yz0ZRmQ/640?wx_fmt=jpeg#imgIndex=6)
