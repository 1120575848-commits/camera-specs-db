# Pomfort | 如何以 Reeltime Pro 搭建一套视频回放系统

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247484476&idx=1&sn=0962fe6537d8cbfe00e3288c872f0ea9&chksm=fc0464d0cb73edc6c6325f6ad55dedd600ba3eaf101586f1d58347e12e608bb831609d669083#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---

视频回放之必要



数字电影制作中，创作过程的基础功能之一就是即时回看每一个镜次。因此，在片场进行快速可靠的视频回放是非常重要的。每个人都能从视频回放系统中受益，但不同部门的需求可能有所不同。满足所有不同需要，需要一位有经验的视频回放操作员和一套便捷实用的工具箱，以高效执行所有必要的步骤。


根据拍摄需求的不同，你的工具箱在不同的项目中可能会有所不同。你的工作从评估每个创意部门除了视频串流之外还需要看到什么信息开始。比方说，导演可能只对低延迟的实时信号感兴趣，而剧本部门可能对元数据覆盖更感兴趣。同时，场记可能会要求合成视图，而服化道那边可能会希望无线视频串流到他们的移动设备。所有部门的综合需求将决定你该为你的特定视频回放系统考虑采用哪些设备。


本文中，我们将为你提供有关如何搭建自己自定义的Reeltime Pro视频回放系统的所有信息，包括在现实中的用例——以帮助你更好地理解不同的情况。此外，我们还会向你展示如何从多个方面评估你的设置，包括性能、灵活性和易用性。本文末尾的检查清单将确保你拥有搭建自己完美视频回放系统所需的一切。






收集我们的工具






开始评估电影制作的不同用例之前，让我们简要地看一下涉及到的硬件组件：






摄影机/麦克风（音视频来源）
视频I/O设备（由AJA和BMD提供）
声音I/O设备（与MacOS兼容）
监视器/头戴式耳机（音视频输出）
基于Mac的，带Pomfort Reeltime Pro软件的工作站
视频路由（由AJA和BMD设计，可选）
iPhone或iPad（无线串流时可选）
Elgato Stream Deck控制面板（可选）
LUT盒子（可选是否与Livegrade Pro/Studio一起安装）






Reeltime Pro使用连接的I/O设备（也被称为采集设备）能接收音频和视频信号，这些设备会转换信号以便应用程序能够读取它们。


Reeltime Pro处理信号并通过I/O设备将它们返回给专用的输出设备（例如，视频监视器和耳机）。应用程序对组合视频I/O设备没有任何限制。多次使用同一款设备（例如两台AJA Kona 5设备）或将BMD与AJA采集设备结合使用是可行的。可选择的视频路由就像十字路口，在你想传输的目的地和如何快速到达你的目的地方面能给你更高的灵活性。


信号链是这样的：


视频和音频信号链






视频信号细节






SDI是种常规信号，在电影片场连接所有摄影机，往往通过线缆以BNC连接器连接。SDI能够传输未压缩的视频、音频、时间码和其他元数据，比如片段名称。视频信号通过1.5 G/3G/6G/12G-SDI（取决于分辨率和帧率）传输，因此确保设备支持所需的数据速率（注：我们推荐目前以HD分辨率工作，因为UHD/4K仍在测试阶段）。


每台采用SDI信号的摄影机或设备都可以通过一个AJA或BMD视频I/O设备连接到Reeltime Pro。


AJA 采集设备还传输嵌入在SDI信号中的水平辅助数据（HANC）。此数据包含一个录制旗标，为所支持的ARRI、RED或Sony的摄影机启用Reeltime Pro中的自动录制功能。针对该功能，录制旗标用以触发Reeltime Pro中的并行录制，这样每次摄影机录制，软件中就会开始一次新的录制。


Reeltime Pro允许在同一个项目中混合不同的帧率和分辨率。在多机环境下工作，这是非常有帮助的，因为某台摄影机可能以较高帧率进行慢动作拍摄，或者项目可能有大量无人机航拍镜头——有时会导致出现混合帧率，等等。






接收音频信号






音频连接的工作原理与视频类似：外部声音通过以Thunderbolt/USB连接的声音设备录制。同时，通过摄影机的SDI接口接收音频信号也是可行的。因此你可以接收多个音频信号，并将所有信号录制为双单声道混音。这些音频通道的音量可以在设置中为每个通道单独设置。Reeltime Pro额外的音频延迟设置让你可以将音频信号从视频信号中偏移，因为音频通常比视频信号早接收一点。






外部控制面板






Reeltime Pro是为电影片场的即时时刻而设计的。有时，用实体按钮触发软件的某个操作更有利于快速反应和增强控制能力。Reeltime Pro支持Elgato Stream Deck，一款常用的实体按钮控制面板，每个按钮上都有一个发光的迷你显示器。该插件可以从应用程序内部安装，并附带预定义的配置文件，其中包含所有重要指令。当然，你也可以创建自定义配置文件，在设计、布局和操作方面几乎没有任何限制。






设置一套视频回放体系






下面的硬件设置是为实际用例设计的，并给出了如何在片场布置Reeltime Pro的示例。Reeltime Pro和设备并不仅限于这些场景。






开始上手






将基于线缆的SDI流与无线连接相结合


让我们从一个简单的设置开始，了解一下各部分是如何协同工作的。眼下，我们用单个音频和视频源，并预期在一台视频监视器上为导演或客户显示串流。摄影机和视频监视器通过线缆与工作站连接，并配有BMD 3G录机/监视器设备，能够实现高清分辨率且最高达到60帧而无需额外电源。外部音频（通常由声音部门提供）将通过附加的音频接口录制。在Reeltime Pro中，我们将输入槽配置为使用BMD 3G录机，输出槽通过BMD 3G监视器进行传输，最后选择合适的视频格式。然后就行了！


这样，我们第一段针对SDI监看、录制和回放的基于线缆的视频流就准备就绪了。现在，我们再来添加一些屏幕。通过使用摄制组的移动设备进行监看，我们可以很轻松地在不离开工作站的情况下扩展我们的视频回放系统。






使用无线串流的灵活性






搭配iOS和iPadOS的免费配套应用程序“Reeltime Viewer”，每台iPhone或iPad都可以用作摄制组的移动监看设备。Reeltime Pro设置中的二维码让你可以从苹果应用商店快速下载应用程序。在Reeltime Pro中，我们通常将无线连接称为“本地串流”。它们能提供与任何其他输出槽相同的功能，且可以在槽管理器中快速配置。


槽管理器还包含单独本地串流的目标比特率设置。当然，你可以用一个Reeltime Pro配置多个本地串流。如果多个Reeltime Pro工作站共享相同的网络，客户可以选择从中接收本地串流的工作站。连接到在Reeltime Pro的本地网络上共享的低延迟信号非常简单。分发的串流使用行业标准加密进行保护，以符合多数拍摄安全准则。


关于整体性能，工作站的硬件要求是轻量级的，因为Reeltime Pro在这个设置中只需处理一些输入和输出信号。请注意，这里不能使用上文提到的BMD采集设备的自动录制功能。






双机设置






带一个视频I/O设备的双机设置


现在，让我们增加一些复杂性，并添加另一台摄影机。这是电影片场很典型的情况，因为它能提供更多电影拍摄过程中的创意控制。这里我们不使用之前的录机/监看设备，而是切换为一台AJA Io 4K Plus或Io X3。AJA Io 4k Plus有四个双向SDI接口，可以同时连接两台摄影机和两台视频监视器。AJA设备需要独立电源，但只需要一个Thunderbolt 3接口。此时我们再次打开槽管理器来快速分配两个输入/输出槽的摄影机。


由于AJA设备的属性，我们不必再手动选择视频格式，因为它会自动检测。有了两台视频监视器，你就可以在单独的屏幕上看到每台摄影机的实时画面，或者为每位观看者配置一台监看设备，这样每位观看者都有自己的屏幕，可以根据自己的需要定制视图。比方说，一台视频监视器可以显示两台摄影机的复合视图，而另一台则可以整个画面显示主摄影机。


使用两台摄影机使得摄影机与时间码的同步成为必要。Reeltime Pro默认使用原始摄影机时间码，因此需要对两个摄影机进行拥塞同步 *。另一种选择是用Reeltime Pro的当前时间来生成时间代码。由于我们此处用的是AJA设备，我们可以利用HANC录制旗标来使用应用程序的自动录制功能。


* 引申阅读：https://zunzheng.com/news/archives/14219


正如前面提到的，Reeltime Pro允许你录制所有已配备槽的信号，于是你可以用一台摄影机的录制旗标来触发所有附加摄影机的录制。如果你只有一台能通过SDI发送录制旗标的摄影机，这就很实用了。你只需在那台特定摄影机上安装一个来自AJA的采集设备，这样你就可以在其他摄影机上使用BMD设备了。这样，一台摄影机就可以启动和停止整个录制组所有摄影机的录制。






使用视频路由






视频路由允许暂时绕过工作站


虽然视频路由不是必要的，但它们能就连接你的设备提供很高的灵活性。此外，它们还可以提高回放系统的总体性能。一般来说，每个通过Reeltime Pro的信号都需要处理，最终会增加一些延迟。而对于实时信号，我们希望尽可能避免延迟。要想实现这点，我们可通过路由将未经处理的信号从摄影机直接发送到监看设备或录机，从而绕过工作站。对于回放，Reeltime Pro可以自动切换回路由，以显示软件的回放输出。这个过程保证了监看期间的最佳性能和低延迟，并且对需要同步看到图像及听到实时演员原始表演声音的导演来说特别有用。


在摄影机信号链和视频I/O设备之间，我们增加了视频路由，以使得所有带SDI信号的设备首先连接到路由，然后再连接到视频I/O设备。Reeltime Pro通过BMD和AJA的视频路由。它们通过以太网连接，并可通过交互式视频路由选项轻松地在Reeltime Pro中进行管理：


Reeltime Pro的视频路由截图


此外，视频路由还可以复制SDI信号，并将它们从源路由到其他目的地（如截图所示）。Reeltime Pro的另一个功能“自动化管理器”，可以很好地与视频路由互补。它将事件与操作关联起来，能帮你自动完成特定任务。事件可以是任何发生的活动，比如录制的开始或从回放模式切换到实时模式。指定的操作将在事件发生后立即执行。你可以配置自动化管理器，使其在激活实时模式后立即将未处理的实时信号通过视频路由从摄影机路由到导演的监视器上。是不是很棒？






高端视频回放
与Livegrade相结合






让我们把之前的设置再推进一点。我们现在讨论的是大规模项目的拍摄，比如电影长片或高端广告。你的回放系统会配有一位摄影部门的DIT，用一个单独的工作站以及Livegrade Pro或Livegrade Studio配LUT盒子，来交互调色未经处理的信号。所有LUT盒子将直接连在摄影机后。如果你此前没用过Livegrade，别担心。简而言之，这款应用程序让DIT能对来自摄影机的视频信号进行实时调色，并通过以太网控制LUT盒子。理论上，你也可以在同一台机器上使用Reeltime Pro和Livegrade——但要注意，应用程序不能同时共享视频I/O设备。这种情况下，我们建议的工作流是用Reeltime Pro来管理完整的信号链，并用Livegrade来远程控制LUT盒子。LUT盒子的处理由硬件执行，几乎不需占用系统上的额外计算能力。有一点需要注意：如果你有一台带输入和输出SDI接口的监视器，那么你可以将来自LUT盒子的已调色信号从视频监视器环出到视频路由。


我们假设你正在拍摄中，并且到目前为止一直在使用双机设置。在此过程中，忽然需要第三台摄影机了。你该怎么办？


由于Reeltime Pro可以同时处理来自不同供应商的各种设备，因此你可以用另一台BMD录机（或任何其他视频I/O设备）扩展你的回放系统。就是这么简单！


LUT盒子给未处理的信号添加调色



现在我们处理的是三台摄影机，所以将槽或摄影机组织成一组可能是必要的。在Reeltime Pro中，我们称这个概念为配备（槽）。当录制所有按钮被按下或群组自动录制功能在设置中被启用时，配备三个输入槽中的两个将得到仅录制那些配备槽的结果。这在片场第三台摄影机只是偶尔需要录制时十分有用。


现在，关于同时处理各种分辨率和帧率，让我们最后再提一次Reeltime Pro在这种使用情景中的优势。在这方面，Reeltime Pro运行非常稳定，能带给你创意自由来制作你构想中的惊艳电影，而不必担心技术限制。Reeltime Pro几乎只受限于所使用的设备和产品许可允许的最高通道配置。






清单：关键步骤






我们已经讨论了Reeltime Pro视频回放系统所需的硬件，评估了不同的使用情景，并研究了几个真实的使用案例。现在，你应对Reeltime Pro在集成任意数量的行业标准设备，以及适应任意规模片场的需求方面的灵活性有了很好的了解。克服最先出现的障碍后，视频回放领域会变得相当令人兴奋。希望我们已经助你辨识出了其中的部分障碍，并启发你搭建自己的定制视频回放系统。下面的清单是对我们上述所讲内容的简要回顾，旨在帮助你用Reeltime Pro设置好第一个项目：






考虑需要你的回放系统的部门。
你是只需要视频还是也需要外部声音？确保你会以最高效的方式接收来自声音部门的音频信号。
会用到多少台摄影机？你需要Reeltime Pro 3通道选项还是6通道选项？
有多少监看设备需要信号？注意，每个目的地都需要一个输出槽。Reeltime Pro的3通道选项支持最多6个输出槽，Reeltime Pro的6通道选项支持最多9个输出槽。此外，你也可以考虑将本地串流作为一种具成本效益的替代方案。
你是否需要一台视频路由来将一个发出信号分发到多台监看设备上？
导演或片场其他人需要看到无延迟的实时信号吗？那你还需要一台视频路由。
你需要自动录制功能吗？你可以考虑使用AJA设备，并检查摄影机是否支持它们。
摄影机的元数据呢？你也用无线图传工作吗？注意，一些图传可能会剥离片段名称和HANC录制旗标。
最后但也很重要的：提前测试设置是必不可少的。






出处：Pomfort
编译：Charlie | 盖雅翻译小组






您可能还对以下内容感兴趣




Pomfort丨全新片场回放产品 Reeltime Pro 许可购买正式上线！




Pomfort丨如何使用 Livegrade 的伪色模式







Pomfort丨Reeltime × Apple Vision Pro 探索新的监看选择，多项更新已上线




Pomfort | QC 科普系列：一切关于质量




![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYgLZKbdkOCTkFSJFZWvxK6qTic3GNpMqfg8Q2wVHDC3icqu1ib2lq27TLUZhUeib4eFUPrRUjFf3rJcA/640?wx_fmt=jpeg&from=appmsg#imgIndex=0)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajeliaa0Q9YA9a7D35xzhV7FaribqRFENicOtt549MoG2JBmJYM2euRIlY8qw/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajelF2rapjZK8bgy8t7vhZGC7ZRzicd8MyicUqcRke1YAa5C4S2qu2BjrTlw/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajelKQFNw0ltibice4lQzGdVl2GcmrmFiafs0xYo9sBCH9TfFFMZ6OZTKfkZA/640?wx_fmt=jpeg&from=appmsg#imgIndex=3)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajelJgTtbf13YBicnpCMs9ZLdBc2gcnq83FQw2fDppYSw2gHPNyfRMSad8A/640?wx_fmt=jpeg&from=appmsg#imgIndex=4)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajelY2rVGdeJIl8GtJMyCBHOrp1D87uicp1fnyQ7ab5bSAeicsG6gm7UXFfA/640?wx_fmt=jpeg&from=appmsg#imgIndex=5)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajelD3KwK1bb0OIAp28nHURRvmAmHrrAo92oRTibNYgP1a59knM2Ajzo8xg/640?wx_fmt=jpeg&from=appmsg#imgIndex=6)
![](https://mmbiz.qpic.cn/mmbiz_png/7VVicaGuObqYVHVFUicydJtHt5vlksunnqvet97Oe5N4MiaAeab3gIY8Bme2GhQqkMKCHNT6oySibAJsLqPQa5H9Jg/640?wx_fmt=png#imgIndex=7)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYs6hZmIhHErmSLrhpFK8wqezM31Jladdib6jYTH6cI82r3BTwdJibk2g8G9y4yXh5U0ib6rdRv3DhQA/640?wx_fmt=jpeg#imgIndex=8)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqbDIEnfgnx73JFAicVHY3WHhuRt9GHgUlWTyt7h4D8fSGH7pEhK9HeBialTXB73NHYqOVCP4hZqP2tA/640?wx_fmt=jpeg#imgIndex=9)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYwYib068npJuz8gCicovfMRA5NyGpejkaDKN4aDDSWLtWAclbGchggXINGodxoTiba5dKLHI8fnTCXw/640?wx_fmt=jpeg#imgIndex=10)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqZxeWhksJnBmQQbUuYv4cjNlvOicOWaGMiarcAnB7tvwJUmibmQdaouR2X1SoQIvPT0dopFsWonW9uHA/640?wx_fmt=jpeg#imgIndex=11)
