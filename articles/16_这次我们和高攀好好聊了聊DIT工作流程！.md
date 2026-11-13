# 这次我们和高攀好好聊了聊DIT工作流程！

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247483917&idx=1&sn=2ba80b44819685d4a06a90eab051e7d0&chksm=fc0462e1cb73ebf797776661899e656bd12d4c9147c42006823a85775fef67559e7f5af03e09#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---




写在前面




「高山流水遇知音」是各行各业的用户与Blackmagic Design的故事，它是关于自我学习、持续成长的故事，是保持好奇、勇于创造的故事，是关于学业、兴趣、理想与事业的故事。我们希望通过这个专栏把这些故事广而告之，让各地的朋友们能增进了解，彼此借鉴。




「高山流水遇知音」专栏第五期——













▂▂▂







DIT、调色师：高攀







快闪工作坊在山城重庆举办的时候，我们认识了主做DIT、调色业务的高攀，他除了使用DaVinci Resolve进行剪辑、调色和交付，也会把DaVinci Resolve应用到DIT工作流程中，比如使用DaVinci Resolve更新音频时间码、基于时间码同步视频和音频，使用DaVinci Resolve做代理等等。




在DaVinci Resolve认证导师分享完DaVinci Resolve 18的新功能后，他坐下来和我们聊了聊他的团队、近期的工作状态，也为我们分享他在使用中比较趁手的功能，正是这样面对面的交流，让我们对彼此有了更深的了解。




他的团队成员来自北京、重庆，主要做院线电影、综艺、纪录片、TVC项目、剧情短片的数据管理、云监看、前后期流程设计以及技术支持工作。团队成员参与的院线电影有《欢迎再次登录》，综艺《边走边唱2》、《边走边唱3》；为第17届First青年影展训练营提供DIT和视频技术支持；还参与中国银行、雀巢、美的、VIVO、大众、金典、京东、比亚迪、腾讯游戏的广告片的DIT数据管理和云监看工作。




   

和高攀一起聊聊DIT







“DIT”的误区







因为虽然这个“职位”越来越为大家所熟知，但很多人可能对DIT不了解或者存在认知上的误区，认为DIT就只是负责拷卡，其实DIT部门可大可小，DIT的职责也不只局限于“拷卡”。







那么，什么是DIT呢？







DIT的全称是Digital Imaging Technician，意思是数字影像工程师，“拷卡”属于DMT（Data Management Technician，数据管理员），是DIT部门一个非常重要的组成部分。







DIT的具体职责是什么呢？







DIT的职责一般涉及到整个前后期流程的设计和测试，原始素材的备份管理、视频信号的分发管理、现场色彩管理。







这些职责能不能细化到更具体的工作流程中？







不同的组不同的部门对DIT的需求都各不相同。在前期筹备阶段，DIT需要向各个部门了解需求，制定属于这个组的专属工作流程。在这个过程中，DIT也能不断优化自己的流程，这样更好的服务剧组的各个部门。




摄影部门主要沟通了解DP的需求，例如show LUT、画框线的制作和导入，沟通拍摄参数，确认存储方案能满足拍摄需要。




制片部门主要沟通的是根据了解的拍摄规格等情况，根据预算和需求，确定存储方案，在拍摄结束之后，交接硬盘和DIT日志。




剪辑部门需要沟通的一般诸如代理规格，画面烧录信息，以及剪辑习惯，合板方式，剪辑作为后期部门最开端，代理阶段流程的正确性非常重要。




录音部门的沟通也非常重要，在整个制作环节中，声音部门处于整个制作的尾端，如果前期部门出现了错误，比如时间码的偏移、元数据的丢失，都对声音部门的工作效率影响很大。通常在剪辑部门做代理期间，会在画面上烧录录音的文件名给声音部门做参考；同时在合板之后，导出元数据表，在元数据表上，能够看到视频素材对应的同步音频文件名，能够看到每条录音的轨道备注信息，方便声音后期作参考。




我在做代理的时候，通常是根据项目需求，确认是否合板、数据烧录、还原Rec.709，从DaVinci Resolve中导出，交付给其他部门。也有DIT习惯直接在DIT软件里生成，我比较习惯在DaVinci Resolve里做 ，方便预览素材和检查素材。







再讲讲DMT日常的工作内容吧







“拷卡”属于DMT，DMT是对原始素材进行备份管理。通常我们会用到DIT备份软件来对现场素材进行备份和校验。




备份原则。在数据的备份中通常会遵循“三-二-一备份原则”，即至少三份原始素材备份，至少两种存储介质，一个异地存放。





存储介质的选择。通常我们会在项目筹备阶段，了解拍摄规格、拍摄习惯以及供电情况，然后再根据预算，制定存储方案。同时，还会准备固态硬盘、阵列作为中转盘，在拍摄现场应对各种突发情况，以保证拍摄顺利、安全进行，避免出现全剧组等卡的情况。




数据备份及校验。每次下卡备份我们还需要对素材卡做好标记和区分。比如，用不同颜色的胶带做好素材卡卷名和备份状态的标记，素材卡放在两个颜色的盒子来做区分，并使用带有校验功能的软件进行备份，备份完成后，我还会使用将素材导入到DaVinci Resolve中对素材进行质检，检查素材是否能够识别，参数是否正确，画面是否异常。




DaVinci Resolve中的自动同步音频功能





生成代理文件。在素材备份完成后，就可以开始进行代理的制作。使用时码器的剧组现在越来越多了，将时码器连接摄影机和录音机，在DaVinci Resolve里可通过时间码进行同步，也就是合板。合板完成后，会导出剪辑部门需要的格式来生成对应的代理文件，便于达到流畅剪辑的目的，需要的时候也会在代理文件中烧录对应的文件名和时间码等信息。






对想要从事DIT的朋友们有什么建议？







在素材备份管理阶段，一定要做好文件名的规范命名。对于专业摄影机来说，有卷名系统可以更方便进行素材管理，但对于一些消费级的微单、无人机、运动相机不具备卷名系统就更需要DIT做好文件名的管理，必要时需要手动进行文件批量重命名，文件的重名在后期回套简直就是灾难。同时在进行转代理的时候，强烈建议在项目设置里勾选「协助使用卷名」。通常情况下，如果是内嵌卷号的素材，可以勾选「内嵌在源片段中」；如果是民用级别的微单、无人机、运动相机，我们通常使用文件名作为卷名。



0
1
0
2



拍摄的原始素材是我们一切的基础。所以如何保证数据的安全，工作流程非常重要，一个规范安全的工作流才能保证安全生产。一次错误操作，格式化错了一张卡，会让整个剧组的辛苦付之一炬。

DIT最核心的就是不断的学习和工作经验的积累，具备在剧组中快速高效地解决问题的能力。所以一定不要小看每次遇到的问题，必要的时候把遇到的问题以及解决办法记录下来，以后遇到相同的问题，能够快速的回溯之前的情况。



0
3










   

使用DaVinci Resolve生成代理文件







高攀说，在DIT项目中，也会使用DaVinci Resolve来生成代理文件，那么，使用DaVinci Resolve生成代理文件的一般步骤和注意事项有哪些呢？




○ 了解素材




首先进入「媒体池」页面。我们将一张卡或一台机器拍的素材导入DaVinci Resolve 媒体池，选择「列表」模式，可查看片段详细信息。







如列表所示，导入的所有素材都是Blackmagic RAW文件，3840*2160(4K)分辨率，帧数24帧。默认情况下，「片段名」和「文件名」是相同的，当我们双击单个素材的「片段名」，可以根据需要进行修改，而「文件名」是无法修改的。而卷名是在制作代理过程中，最容易被忽略的一个重要的参数，如果卷名管理得当，基本就是一次套片，基本上不怎么手动。




○ 根据项目要求提取或自定义「卷名」

「卷名」通常是摄影机自带的，有时候也需要自定义。

点击「媒体池」右下角「项目设置」按钮，选择「常规选项」>「套底选项」。







当我们勾选「协助使用的卷名来自」>「内嵌在源片段文件中」进行测试时，「卷名」仍未显示；







当我们勾选「协助使用的卷名来自」>「源片段文件路径名称」进行测试时，「卷名」显示“01 视频”，符合实际。







我们也可以自定义「卷名」。首先，全选片段，右键单击选择「片段属性」，会弹出「片段属性」选项卡；







在「片段属性」中选择「名称」，勾选「设置卷名使用」>「用户定义」，输入“DaVinci Resolve”（仅做示意），「卷名」就被修改了。







○ 根据片段新建时间线（①色彩管理②是否需要遮幅...）







全选片段，右键选择「使用所选片段新建时间线」；打开新建好的时间线，因为导入的片段都是Blackmagic RAW文件，需要进行色彩还原。




像这里，是同一台Blackmagic Pocket Cinema Camera摄影机在同一场景的不同角度拍摄的RAW文件，我们就可以简单地通过Resolve的色彩管理来完成色彩还原。




点击右下角「项目设置」按钮，在弹出的选项卡中，选择「色彩管理」>「色彩空间&转换」。其中，「色彩科学」可以选择“DaVinci YRGB Color Managed”，勾选「自动色彩管理」，「输出色彩空间」可以选择“SDR Rec.709”，点击「OK」，颜色就自动还原了，还可以在调色面板针对片段做一些微调。







有时候，我们还需要根据项目需求添加遮幅，最简便的办法就是在顶部菜单栏选择「时间线」，滑到底部，选择「输出加遮幅」，例如选择“2.35”，效果如下图。是否添加、比例多少，具体细节还需要和客户确认。




「输出加遮幅」前后对比




○ 数据烧录

到了「数据烧录」环节，常常要求烧录必要的信息。

在顶部菜单栏选择「工作区」，向下滑动，选择「数据烧录」；







在弹出的「片段烧录」选项卡中，可选择针对「项目」还是「片段」进行烧录。左侧是可以添加的选项，右侧是针对选项进行参数调整。







在DaVinci Resolve中进行数据烧录时，可添加的选项非常多。我们可以选择烧录「源片段时间码与帧编号」、「源片段名」、「卷名」，还可以烧录「自定义文本」、「Logo」、「摄影机编号」等等。




数据烧录后的截图




备注：如果想把这一次的设置重复使用，可以考虑将其「另存为新预设」，只需要在完成一次设置后，点击右上角三个小点，就能保存预设了。







○ 根据项目要求完成交付设置

切换到DaVinci Resolve「交付」页面，进行代理文件的渲染设置。







选择「自定义导出」，选择合适的渲染路径，点选渲染「多个单独片段」，然后针对「视频」、「音频」、「文件」，按照项目要求分别进行设置。







上图为导出代理素材「视频」和「音频」时常用的设置，视具体情况而定。特别需要注意的是，在「音频」设置版块，通道需要选择「与源文件相同」，不然剪辑完成以后，没有保留和源文件相同情况，这对声音后期就是灾难。







「文件」这里，「文件名使用」一般情况下选择「源名称」，同时勾选「保留源文件目录层级」，层级可自定义，方便后期套底工作顺利进行。




完成设置后，点击「添加到渲染队列」>「渲染所有」。




○ 检查DaVinci Resolve生成的代理文件




前面将DaVinci Resolve生成的代理文件导出到文件夹「生成代理文件」中；这里，将它重新导入DaVinci Resolve进行检查。




回到「媒体池页面」，在媒体存储中找到该文件夹，右键单击，选择「将文件夹与子文件夹添加到媒体池（创建媒体夹）」。此时，会发现它保留了3个源文件目录层级，与设置相符。




让我们来检查其他设置。







如果想重点检查某些信息，可以在「片段名」这一栏的任意位置右键，调出「创建栏布局」，可以勾选我们想要显示的信息栏。








这里，我们对显示的信息栏进行了筛选，点击空白处，即可回到列表。







如上图所示，我们可以检查片段名、卷名、音频位深、分辨率、格式、音视频编解码器、色彩空间等信息，与设置相符。







选中所有片段，右键选择「使用所选片段新建时间线」。打开新建的时间线，我们可以移动播放头，时间线检视器面板正确显示了烧录信息。




这就是使用DaVinci Resolve生成代理文件的一般步骤。




   

工具分享







和我们遇到的其他用户一样，高攀一直在不断适应DaVinci Resolve的更新频率，在软件中不断去发掘与自身工作适配度更高的工具，帮助解决工作中遇到的问题，这是特别宝贵的经验，所以我们也想要整理出来分享给更多的用户借鉴、使用。







高攀分享了他在使用DaVinci Resolve一键换天时的使用心得，用到了DaVinci Resolve调色特效库中的「天空替换」工具。




高攀说，在调色工作中，很多时候都需要在项目中使用调色手段来弥补前期拍摄的不足，最常见的就是针对天空所做的调整。




仅供示意：前景和天空有相对清晰的分界线




“我们拍摄的天空常常会因为曝光过度而缺少细节，同时它也极易受天气的影响，碰到不合适的天空会影响画面美感和情绪表达，这时我就会尝试用Resolve FX风格化里的「天空替换」工具来一键换天。”说着，他打开随身携带的笔记本电脑，任意找了一段素材为我们演示。让我们一起来复盘。




使用 “神奇遮罩-物体”直接抠出天空部分




使用“限定器”抠出前景，再用外部节点得到天空部分




“正常的逻辑是这样的，首先需要建立一个天空蒙版，也就是要把天空部分给抠出来，然后给蒙版添加「天空替换」效果，最后再去调整合成的细节。想要抠出干净的天空部分，方法和工具的选择非常多，需要结合具体的素材特点进行分析判断。我们既可以使用「限定器」工具，也可以使用「神奇遮罩」工具，既可以先将天空部分抠出来，也可以先抠出主体，再使用「外部节点」或者「反转遮罩」得到天空部分。




使用「神奇遮罩」工具的抠像效果




做好蒙版以后，在「特效库」里搜索「天空替换」效果，将它拖拽至蒙版节点上，这时设置面板被同步激活了。我们可以在「人造天空」这里轻松地调整天空的颜色、透明度等参数，甚至还可以为我们的人造天空添加云层细节，调整云的颜色、大小和形状等等，使之更加真实细腻，就像下图显示的这样。




使用「天空替换」工具的人造天空效果




“当我们把抠出来的山川河流和人造天空两者合在一起的时候，如果觉得合成效果不够理想，还可以返回「限定器」面板进行「蒙版优化」，或者返回「神奇遮罩」面板进行「细节优化」。这个功能很推荐大家试一试。”




在「限定器」中继续优化蒙版




特别注意：使用神奇遮罩，还需进行跟踪，才能将该片段每一帧画面中的天空部分抠出来。只需点击双向箭头按钮即可，跟踪完成后，进度条会变成蓝色。

在「神奇遮罩」面板做好蒙版跟踪




当然，「天空替换」还有进阶玩法，就是把天空部分换成自己的素材，并且可以进行动态跟踪。




○ 将天空替换为素材




进阶玩法：将天空部分替换为自己的素材




除了人造天空之外，我们还可以使用自己的天空素材，只不过，添加「天空替换」效果的方式不同。之前我们将天空部分抠出来以后，直接把「天空替换」拖拽到蒙版所在的节点上，现在我们把它拖拽到蒙版与输出端的连线上，同时，连接蒙版节点的Alpha输出与天空替换的Alpha输入（一条蓝色的虚线）。




「节点编辑器」节点示意图




接下来，在「媒体池」直接拖拽天空素材到「节点编辑器」，选中该素材节点，使用快捷键option+S或者右键新建串行节点，将输出端连接到「天空替换」节点的输入端，此时，天空部分就被自己的素材替换了。




想要做更精细化的调整，需要在「天空替换」面板选择「源天空外观」、「天空位置」等进行虚实、远近、大小的调整，还可以在「天空位置」>「匹配运动」中选择跟踪模式，进行动态跟踪。






天空替换


源天空




备注：快闪工作坊到达重庆时，「天空替换」效果还未汉化，名字叫「Sky Replacement」，现附上最新版本DaVinci Resolve 18.6.1下载链接，可尽情体验该功能：

https://pan.baidu.com/s/1lk91ceSZR6mpEDywNuiHyg

提取码: bvcc




高攀说，希望更多人能走出对DIT的认识误区，摆脱素材“拷贝”的刻板印象，也希望越来越多的影视从业者能够认识到DIT的重要性，给予DIT及其从业者应有的尊重和理解。




通过在快闪工作坊与用户们面对面地交流，我们更能理解用户的工作和处境，希望更多的人可以认识到DIT的价值，DIT们能更好地发挥自己技术和艺术方面的才华，也希望我们的产品能够陪伴他们成长！







🌟

『 高山流水遇知音 』




故事还在继续，

你是否愿意和我们分享？

我们在快闪工作坊，

等你。

/




 ○ 下一站预告 




“扫描上方二维码即可报名活动”







· end ·

「 专业平民化 创意专业化 」







欢迎加入我们的微信群。现有Blackmagic Design摄影机、ATEM切换台、DaVinci Resolve微信群，欢迎大家加入。入群前请先关注BMD用户俱乐部微信公众号，添加管理员微信。




![](https://mmbiz.qpic.cn/mmbiz_jpg/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZs1MHtMq4OrNJ4rLR3bVn4ibE6ibsHkt1LpyB9KmODJ2EcBAumefWapaA/640?wx_fmt=jpeg#imgIndex=0)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZib6hibVj0kW5eONjENaQESvy7ic4pUnSSQ60hoItdBke55rHCUu7iam14w/640?wx_fmt=png#imgIndex=1)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmLB0pfh0n5Epp77megy9SLK7qcobPjIfCZmJPEm6soGewOyw07ZwtScyNgXiasD8cL9mpkusUNdp3A/640?wx_fmt=png#imgIndex=2)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZJPoX9T2TclBUbD0cSKWHPHFN0meKWaO7ymjCibqfLOsSz5KpDZRkL9Q/640?wx_fmt=png#imgIndex=3)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZjMGMoAa3u4oeM13BtXktG9ImkVAUrgQU52U6CWKTLsianyIFC4jFJQA/640?wx_fmt=png#imgIndex=4)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZv7Pn9iabDB4OvpVicmzuhpib8CtticTo6M7HwARnt1Isv3CBHSUjv4FIXA/640?wx_fmt=png#imgIndex=5)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZ6GscW3OEwqEcsHmzm1qbadXZ2DWgGy9Sd81TPvatwFQheLoZdC1Keg/640?wx_fmt=png#imgIndex=6)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZja2bfAKZeuEKtzzGxibArJ4mdpb6PaLkibiamy053omukJ29W6mCC7Hag/640?wx_fmt=png#imgIndex=7)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZ4XFujHf8DmZKo8lZEwubvH6atWHWTtKKEvAh9ozMnP4ALOaVicHRGbQ/640?wx_fmt=png#imgIndex=8)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZXw1FKHrNWucmXBQFvibhMxbLXMEj2xLYSNKjLuCCdkpbndicKrfIEo5Q/640?wx_fmt=png#imgIndex=9)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZBTibb2hHadwKWAbTEbLgDiccnHO6KibZHjicbfc22KaiaWibwRsqXIFJ8wIg/640?wx_fmt=png#imgIndex=10)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZyfjicZVZVzWdgwKfq2KC7hBBBmGxlRfZXcMofItcKYNPmMXAqzBTeMg/640?wx_fmt=png#imgIndex=11)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZHl7PjEQsiaJ8DzLQ0zMqLcDwOQgSwKs2icsEa87W2buVbRwyEhRSn8ibg/640?wx_fmt=png#imgIndex=12)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZmAriaXK0ba8DdweicgzB622qIqgZESb7EZcAcaJiaQzbFqYpw50UicEV2g/640?wx_fmt=png#imgIndex=13)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZYQ162xlZdibso35Jl3SwTCPiaz1XsZPwtsJ5CrOjLm1rwKnglWf6shaQ/640?wx_fmt=png#imgIndex=14)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZv57LtiaMcQKb8UfUlZo5hnQrQYDTceqQusiaXQPjhD5flDmicgzibpSQ6Q/640?wx_fmt=png#imgIndex=15)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZK55cCDuzHWIoHLo2jemePl1L7fs60nOYRQZibqw3AqNp2nR5QjPVibvg/640?wx_fmt=png#imgIndex=16)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZic7Ov391WyQgQmGFW5mxg1YosIgIFhAibib7Uj2JHQ5kdWv12jog3LUicg/640?wx_fmt=png#imgIndex=17)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZWe3NaKdmicSzlnkibKPquHR43snKKX4FtKemKwjOC406fS8bbta59icfw/640?wx_fmt=png#imgIndex=18)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmJpYxxxQlpWrsFL55AzLtMBIrgKibvgrqsoyHNUlw0kmlL2enb6L2OibjCRr4FqOT5tjDHkKwWOevmg/640?wx_fmt=png#imgIndex=19)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZMhAOyNtYdJ3iatibYKWXRuvy3jZYtUOoAFQb2uvCGskicdS6U6icYeDqibA/640?wx_fmt=png#imgIndex=20)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmJpYxxxQlpWrsFL55AzLtMBh614tboCKsmTb5El9msoTYgXcNWVFWJDdpo2jaQViam4JIRYCLPyZRg/640?wx_fmt=png#imgIndex=21)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmJpYxxxQlpWrsFL55AzLtMBIktxKX99rUmNgWia8geMnLztQt9OnVdyVkic7O3SUpPdrASn6UFXVWsA/640?wx_fmt=png#imgIndex=22)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmJpYxxxQlpWrsFL55AzLtMBNXKZf1yicG1bkhLz6LdwlFqd6qY413mH62v41vOiaiaquAEBib28FRRvXw/640?wx_fmt=png#imgIndex=23)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmJpYxxxQlpWrsFL55AzLtMBCPYia2CN9lRTCo0DMyCSBzyTwZDFLyQaTx0uOH5XIicCHTCLOPdJMHQw/640?wx_fmt=png#imgIndex=24)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmJpYxxxQlpWrsFL55AzLtMBq0o7EzASrdaqUcydOEkzndicLlWjE5JUxozItNkEcBibwGPArvhIO1dg/640?wx_fmt=png#imgIndex=25)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmJdYjzcrparoE3PEib0d5Wficom82WdXogLU8SLhicia5XGkvbMfdgAquqLQM1Y6gKk1oQk3jKzs1nFLw/640?wx_fmt=png#imgIndex=26)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZ1qAD0EL7PQr9L6TOrD01ibgTeTzZPnUC6LIibcacjeibvjicic53Nt6n7LQ/640?wx_fmt=png#imgIndex=27)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZuY30qAsesn3UKT2kCE1OKnt7o46GfWgbNZdaf5wm7ahA6icVCWQWbHA/640?wx_fmt=png#imgIndex=28)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZ30aHakBc4MsumwQAp5ia48iaYFATjSzpdkFVw6XK0LUHGCJNTYn4Z1Ag/640?wx_fmt=png#imgIndex=29)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZkvT0x5CzDbWScKJ2pDYGbG5t4aXRMibLZeiaqtJ7Nhh7ibX6d9zwDOJqg/640?wx_fmt=png#imgIndex=30)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZY7DOZynibgU6rMdWcmQp5nuzge1etxqDCBibBeCiaDveA4Yjoia3j75pJw/640?wx_fmt=png#imgIndex=31)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZibttJ9c6Eiby6vhw5ibIF3qAKrUEwtwgK3P505qrS38ot6pCGaJscNXuA/640?wx_fmt=png#imgIndex=32)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZg9e3zuNTB2D8micmRqaHb7ib0Jibd6KgAj3XEYtwK82ia19vlf0b1zeEbw/640?wx_fmt=png#imgIndex=33)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZ35wpFuY7UtNKvy572euic4oddTPeyhVLNn0Sk6Au3EGnYhEHicPsDIicg/640?wx_fmt=png#imgIndex=34)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZFShqkfNZbXX9htThPmqVhzpd2S2icryl7copY8ia95icOKgBDlpGr1mSA/640?wx_fmt=png#imgIndex=35)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZEH9iamD06mBia9KOuap0chSpubFEH3YdxRiadRclV8F5qxzCodZOW7whA/640?wx_fmt=png#imgIndex=36)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmKVVcLWAnTKaRXS47BdCoHZ12UOicXULTYCrFfpsTiaREAudR3FeP7icrIauucYPnNNlQSmUkQISkdqQ/640?wx_fmt=png#imgIndex=37)
![](https://mmbiz.qpic.cn/mmbiz_png/kXn7thBBMmLB0pfh0n5Epp77megy9SLKKMJq9k0uBc8rQicqiaygibArCXiaOvMoUAO4jicjwicPscxibSUW7tJZ0jjkw/640?wx_fmt=png#imgIndex=38)
![](https://mmbiz.qpic.cn/mmbiz_jpg/kXn7thBBMmLB0pfh0n5Epp77megy9SLKjHIeHWEuyzK3RonQll7qicsauRUu78RpwtwNV42KLia2zhcpocPTLxXA/640?wx_fmt=jpeg#imgIndex=39)
