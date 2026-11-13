# 如何在DaVinci批量将PRAW转为Log

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247485309&idx=2&sn=3b35dbc16a72198bb274d81a32dd9f7f&chksm=fc046791cb73ee87c3ade10a5d507fcafcc3e30fbc687aca080745b87f442267295b30b836d6#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---

    众所周知，影视从业者苦DaVinci Resolve适配Apple ProRes RAW(后续都简称为PRAW)久矣，这一个期许在2025年9月10日得以实现。在此之前，PRAW要进入Resolve工作流，都需要借助其它专业软件将PRAW转为Cinema DNG或ProRes 4444XQ。
    而这次，苹果和BMD达成深度合作，不仅新出的iPhone17 Pro能够在Final Cut Camera和Blackmagic Camera拍摄ProRes RAW,BMD的BMPCC摄影机也同样适配。更重磅的是，DaVinci Resolve适配了PRAW，不限相机和品牌，都可以在Resolve里预览和编辑。
    在DIT的日常工作中，我们需要将大体积的视频源文件转码成小巧方便的代理小档，客户那边小档要求保持log灰片也越来越多。目前Resolve（截止到2025年9月25日最新的版本为20.2.1）尚不支持PRAW在项目设置里像主流电影机ARRI或者RED一样修改默认的解码方式，如下图所示。
    要调整对应的色彩空间和伽马，就需要在调色界面的Camera Raw面板调整，将解码方式改为片段，如下图所示。
    以大疆如影4D的PRAW素材举例，通过上述步骤我们可以把素材调整成对应的D-log。
    比较致命的是，一旦素材过多，一个一个打开Camera RAW里调整非常难受，用中键复制的操作会将上一个镜头的ISO和白平衡参数也复制过去，这显然不是我们所期望的。
    可以看到默认的解码方式是HLG，我们可以不在camera raw面板调整，通过色彩空间转换的OFX插件将HLG转换为我们期望的色彩空间和伽马。具体操作如图所示，注意色调映射和色域映射需要改为无，后一个节点匹配下camera raw解码的曝光
以下为两种方式的对比
这样调整之后（该操作不能调整camera raw面板，需要保持默认状态），我们就可以随意进行复制的操作，不用担心会影响到默认的摄影机参数。
    感谢你听完我的碎碎念，为表感谢，我将上述的操作做成了两个对应的LUT可供大家在DIT转码的工作中使用（注意Resolve的版本需要更新到20.2或以上）
下载链接
https://pan.baidu.com/s/1ATXxl1azCj0vhUEKKFxl-A?pwd=4f4d 提取码: 4f4d
本人才疏学浅，如有错误或者不足，欢迎大家在评论区指出，踊跃谈论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFrv789CJTOvnDRFv1srrbibyqFgnmmc1jWibn3WqRWSJCVKUBojlRcjjCzG2M9MS8jFl4VZIs4mc54A/640?wx_fmt=png&from=appmsg#imgIndex=0)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFrv789CJTOvnDRFv1srrbibygnEs8x0ib9azhmW4ebgLR6oMHVCglpearkosN4LxYDSfGF5FNN5LaXA/640?wx_fmt=png&from=appmsg#imgIndex=1)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFrv789CJTOvnDRFv1srrbibylE6pOIclBUDCOSMX8IDGXapqib4ZMOZvA9Ob5icmZ2uLVbBkkBoh1hqg/640?wx_fmt=png&from=appmsg#imgIndex=2)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFoL5UUgY08Cg4XVgAndeEfvkwZhkmovF6ldCRian2kejrj8vl96BkwotKMEQyQA6RzNiaJ0RtEH73vA/640?wx_fmt=png&from=appmsg#imgIndex=3)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFrv789CJTOvnDRFv1srrbibyopueIc15PrVwua9uyzVSn3YDDQlTBP3ULGT5FmibU238akDnSiaFrHNw/640?wx_fmt=png&from=appmsg#imgIndex=4)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFrv789CJTOvnDRFv1srrbibyMeYlIyL8pRQE0mibnf9T5icTKqhgqWosrT5WxYcseht37kOBkRFIWraA/640?wx_fmt=png&from=appmsg#imgIndex=5)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5p3hic3PskFrv789CJTOvnDRFv1srrbibylMIu5ScVJibhlOxZt7UjOSCJoqTKBheiafUeeGZNFQbDxnn6t7GMb2aw/640?wx_fmt=jpeg&from=appmsg#imgIndex=6)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFrv789CJTOvnDRFv1srrbibyiaPYAVra4YibjsaxGNuY99YS1TQWkrofoibsM9BRgibKc1bNrO3F6JoNDQ/640?wx_fmt=png&from=appmsg#imgIndex=7)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/5p3hic3PskFoL5UUgY08Cg4XVgAndeEfvQjAJuPg48ibpGZ9u9XWeUrbgLvVfiaWPvR10unugdKM7SXk0taMhru7g/640?wx_fmt=png&from=appmsg#imgIndex=8)
