# 快速制作及相互转换ARRI LOOK文件｜玩转 LogC3(ALF2)、LogC4(ALF4)色彩科学

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247485500&idx=1&sn=5f413d634448498e78d4601c8e90f12c&chksm=fc0468d0cb73e1c65592a3ad66648c3e3d3b28936040145e5a320312e7bb80586bfa44a80369#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---

本文则主要侧重于通过ARRI参考工具 (ARRI Reference Tool) 和DaVinci Resolve Studio软件快速制作基于LogC3色彩科学的ALF2（.aml）文件格式与基于LogC4色彩科学的ALF4（.alf4/.alf4c）文件格式的ARRI摄影机监看Look文件与通用型3D LUT（.cube)相互转换。

ARRI参考工具 (ARRI Reference Tool) 缩写"ART"。伴随ALEXA 35摄影机的推出，ARRI借此机会把过去三个软件 -ARRIRAW转换器 (ARRIRAW Converter)、ARRI色彩工具(ARRI Color Tool)以及ARRI元数据提取器 (ARRI Meta Extractor)整合成为一个新软件，这意味着以上这三个软件中的所有功能，如今都集成在ARRI参考工具 (ART) 里。


ART的界面分为四个窗口，各自承担不同功能：第一个是浏览窗口 (BROWSE)，用来导入片段，创建Bin和片段序列；观看窗口 (VIEW) 用于回放素材，检查画面，同时可调整ARRIRAW素材参数 -如果录制的是ARRIRAW格式，比如调整EI或白平衡；第三个是画面风格窗口(LOOK) 可以用来以多种方式打造自定义风格，例如调整CDL参数或调用ART内建的ARRI画面风格库再或者导入各种第三方调色工具制作的LUT，然后制作ALF-2或ALF-4画面风格文件，再导入ARRI数字摄影机使用；最后是渲染窗口(RENDER) - 将ART里的任何素材输出为各种流行的后期制作文件格式。

技术｜ARRI 参考工具技术分享 第一部分 - 什么是ARRI 参考工具以及观看（VIEW）窗口功能讲解

技术｜ARRI 参考工具技术分享 第二部分 - 关于画面风格以及渲染（RENDER）视窗功能讲解

更多ARRI参考工具 (ARRI Reference Tool) 的内容可以跳转ARRI官方公众号的这两篇文章。




ARRI LOOK文件（.aml/.alf4/.alf4c）转出通用LUT文件(.cube)

打开ARRI参考工具，转到“风格-LOOK”界面。

根据ARRI LOOK文件类型，在检视器顶部居中位置选择LogC3/AWG3或LogC4/AWG4。

在LOOK界面右上角找到“My Looks”再到对应访达位置里的ARRI LOOK文件路径，点击缩略图即可挂载上ARRI LOOK文件。

在检视器顶部右上方可选择导出通用LUT文件(.cube)和调整后的ARRI LOOK文件（.aml/.alf4/.alf4c）

需注意，在ARRI参考工具 (ARRI Reference Tool) 内：
基于LogC3色彩科学的ALF2（.aml）文件只能导出.aml和.cube，无法导出.alf4/.alf4c；

基于LogC4色彩科学的ALF4（.alf4/.alf4c）文件只能导出.alf4/.alf4c和.cube，无法导出.aml。




ALEXA Mini（LogC3）与ALEXA 35（LogC4）的LUT文件互转

ARRI LogC3和LogC4使用的Rec709还原LUT不一样，如果从ALEXA Mini（LogC3）切换到ALEXA 35（LogC4），需要重新创建Look文件。


 

通过ARRI参考工具 (ARRI Reference Tool) ，我们把ARRI LOOK文件（.aml/.alf4/.alf4c）转出通用LUT文件(.cube)，此时我们回到DaVinci Resolve Studio中，将我们LUT文件导入到达芬奇LUT库里，在调色界面-特效库-在该应用LUT之前的串行节点使用【ACES转换】完成输入转换和输出转换设置即可完成，通过生成LUT输出得到调整后的通用LUT文件(.cube)。

 如果是ALEXA Mini（LogC3）转换目标ALEXA 35（LogC4），在ACES2.0版本里输入转换应选择【ARRI LogC4-CSC】和输出转换应选择【ARRI LogC E1800 AWG-CSC】。

如果是ALEXA 35（LogC4）转换目标ALEXA Mini（LogC3），输入转换是【ARRI LogC E1800 AWG-CSC】、输出转换是【ARRI LogC4-CSC】。

当给其他摄影机品牌转不同LUT也是根据具体摄影机对应使用的色彩空间和LUT输入色彩空间调整输入转换和输出转换设置即可。




通用LUT文件(.cube)转ARRI LOOK文件（.aml/.alf4/.alf4c）



场景举例：我们使用ALEXA Mini（LogC3）、ALEXA 35（LogC4）2种不同的ARRI色彩科学的摄影机，我们需要2台摄影机同时机内同时加载到同一个黑白胶片模拟风格LOOK，我们已有ALEXA Mini（LogC3）的AML。

通过在ARRI参考工具 (ARRI Reference Tool) 软件我们完成了LogC3.aml转换成LogC3.cube，在DaVinci Resolve Studio【ACES转换】将LogC3.cube完成转换获得LogC4.cube黑白胶片模拟风格LUT，此时还需要再将LogC4.cube转成LogC4.alf4c文件即可。

*需要注意.alf4ch含有色彩空间“Rec 709-D65”和色彩空间“Rec 2100/PQ”2种色彩空间映射选项，本次文件正确映射只有正确挂载色彩空间“Rec 709-D65”lut。

ALEXA Mini（LogC3）转ALEXA 35（LogC4）的LOOK文件路径：LogC3.aml【ART】➡LogC3.cube【ACES】➡LogC4.cube【ART】➡LogC4.alf4c

ALEXA 35（LogC4）转ALEXA Mini（LogC3）的LOOK文件路径：LogC4.alf4c【ART】➡LogC4.cube【ACES】➡LogC3.cube【ART】➡LogC3.aml

最终别忘了制作一份转换报告连同转换好的LOOK文件给到摄影组，来确认验证转换无误，工作留痕，也能随时回顾检查步骤操作是否有所错误。



ALEXA 35摄影机导入LOOK文件

内容来自ARRI ALEXA 35 REVEAL Workflow Quick Guide v2 vCN.PDF截图

ARRI还原LUT、ART软件及ALEXA 35色彩科学ALF4工作流中文版PDF

链接: https://pan.baidu.com/s/1pY9XstLSRrydb_rnDtkz4w?pwd=tf4t 提取码: tf4t 

点击阅读原文跳转至百度网盘链接

![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msGEkMaf5e4RxWTnvCrqUnTIeBiaFD3R4fmJ1rP8cvlMX4uc4YQf7ojGEpRuwiavicDnrMIxIziaLN9oL7LYMMFCZ6SzjDZlOQ2YlJc/640?wx_fmt=png&from=appmsg#imgIndex=0)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Daacgke2msEFTV4vY9TNmOomh4SJpKhZnwkicwLqDsbVrOnxl4Q4wI4HJ6421FUZYLibGesac4RkEXA59Pd40FJhibIggS1fAqRibCL8n3yjoic4/640?wx_fmt=png&from=appmsg#imgIndex=1)
![](https://mmbiz.qpic.cn/mmbiz_jpg/Daacgke2msE11senGwWoBXHq5mwXnl0TlLjydnxaFQhqwbwvWOfYicABOUY0H6W0CZ1Hm857kDQ4O1tIDAJCyas3Dn5vk3jCMm3AacsFLE9g/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Daacgke2msEEQ8mnpXVnxvLdrcySMC5GBPqpuj18Psg82icVZqhSicmm4gXS9n06Q0SIbtf3e80PPLKRF9yJyjH9CQpalPwyCQ4XdVIibENNls/640?wx_fmt=png&from=appmsg#imgIndex=3)
![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msGiaFRbDZsYswhd5Jf2HDiaIBCiam4jpY1oNCGiak4oaAaSjxIfe4p1Atr14mBcTBUsNmpsVyWhCFsvLCVxTaqDJArXcZBAFdMJtcA/640?wx_fmt=png&from=appmsg#imgIndex=4)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Daacgke2msHZFrbN7efMOV4icibR397hadQy9z8Sy1BxbUthUXDRvekgv6I5EPdNmNeIsec873J2Oq7X6ZybIE5wib1LxjZowOviaqImVhTXEc8/640?wx_fmt=png&from=appmsg#imgIndex=5)
![](https://mmbiz.qpic.cn/mmbiz_png/Daacgke2msHCiaRX89eYECyLlBdWbvlQhUsdQd7xqh61ibL1I8fialqNRy5VQOuicFpfeKoF9j3QDP9iavIfa7c6hicSMoJ5o8LaVoDicy9uibSzQuM/640?wx_fmt=png&from=appmsg#imgIndex=6)
