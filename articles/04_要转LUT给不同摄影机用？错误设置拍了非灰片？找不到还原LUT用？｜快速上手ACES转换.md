# 要转LUT给不同摄影机用？错误设置拍了非灰片？找不到还原LUT用？｜快速上手ACES转换

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247485484&idx=1&sn=d12f622c00f61b36a26eb9913f13d937&chksm=fc0468c0cb73e1d6ec6d4322147c8514fbceeda4a12594428e6a900415ef9645c53cd1822218#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---

认识ACES色彩工作流程

ACES 是由美国电影艺术与科学学院（AMPAS）于 2014 年推出的开放式色彩管理和图像交换系统，旨在为电影、电视和商业广告制作提供标准化的色彩工作流程。将不同摄影机（ARRI、RED、Sony、Canon 等）的原始色彩空间转换到 ACES 标准空间之后，在ACES清单的摄影机源素材对应的色彩空间可以任意相互转换，也能将 ACES 色彩空间转换到目标显示设备（影院放映机、HDR 电视、SDR 监视器等），支持多种输出标准：DCI-P3、Rec.709、Rec.2020等。


 在DaVinci Resolve Studio中调色界面-特效库-使用【ACES转换】

一个更全面且持续更新的LUT库

在DaVinci Resolve里也拥有各式各样的官方摄影机Log to Rec709，一般我们直接使用相应的还原LUT制作审阅样片，而在达芬奇LUT库没有的，比如ALEXA 35 LogC4 to Rec709、Apple log、Apple log2的LUT，而这些【ACES转换】就能找得到，目前的DaVinci Resolve Studio20已经升级到ACES2.0，同时加入对DJI D-log的支持。

特定摄影机的风格LUT转换适用其他摄影机

在拍摄过程中，摄影组一般会提前制作准备好监看LUT挂载至摄影机输出给到下游监视器，在不同影片项目里也常常会遇到自带LUT的摄影指导，这些LUT必然是专用于特定单一产品线或单一品牌摄影机，无法适用于其他摄影机品牌或不同年代的色彩科学，如ARRI LogC3和LogC4使用的Rec709还原LUT不一样，如果从ALEXA Mini（LogC3）切换到ALEXA 35（LogC4），需要重新创建Look文件。而通过使用【ACES转换】即可将不同的输入源转换成LUT原先的输入源的色彩空间与之衔接匹配，可导出制作新的LUT。

举例说明：我们使用ALEXA Mini（LogC3）、ALEXA 35（LogC4）2台不同年代的ARRI色彩科学的摄影机，我们已有ALEXA Mini（LogC3）的LUT，此时通过使用【ACES转换】将ALEXA 35（LogC4）转ALEXA Mini（LogC3）即可完成转换。

反之也成立，通过转换使得任意摄影机能给使用专为某类特定摄影机的风格LUT，并与之保证匹配性。

后期调色的实际使用场景

在实际拍摄制作中会混入无法使用Log灰片进行拍摄机位，比如GoPro、高速摄影机、穿越机、延时照片等，后期交换物料会接收到特效DPX等物料，个别情况下会遇到现场某个摄影机错误设置（尤其是Sony的摄影机）导致录制视频为非灰片，进入到后期调色阶段面临剪辑片段的衔接及色彩严重不匹配，此时则需要逆向将这些非灰片视频色彩从Rec709转成相应摄影机的Log灰片，再进行调色。

在DaVinci Resolve Studio中调色界面-FX特效库里，有【色彩空间转换】和【ACES转换】，可以理解成【色彩空间转换】为开发测试版本，看似拥有更多可调设置参数，你必须对各个技术细节都要了如指掌需要反复验证，而【ACES转换】是标准正式版，自动匹配各个厂商预设，更不容易出错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Daacgke2msFKD8lyDGFUhlp1iczMvudkWNsF0vNszQOiaHDklKcGYoygMm4S4muB21yN8eN1sp7cq5mQ6EE7V9pkPkXNRoiamQJIegxWpna14c/640?wx_fmt=png&from=appmsg#imgIndex=0)
![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msGs4aNyI9opicMkEEBOEdfp0MmJaIOAeoobOFFZ0ygq6IShRbTA07oODVFV2r68gYEDwqtZSqknlFkLUUE869IaktUSNMvRmtoM/640?wx_fmt=png&from=appmsg#imgIndex=1)
![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msG8YF01HmNWT9DYnAm7VsQUFPC1vtEjK0h7CGlvicibNgPaibtMWjpMmV9opiarNviaJWxRCibTAex9qHY0lhTGuO52HPpkuLyWyWIcE/640?wx_fmt=png&from=appmsg#imgIndex=2)
![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msFJ2Vwm1nSohMTyIDOGcaCt5wZBRUPC6jbauU6r9uqqsPb9WG035OjEJ5snJ8Vs9SHZ2BtB6FpuZW33LWX9fDrnibD2lP1zDK54/640?wx_fmt=png&from=appmsg#imgIndex=3)
