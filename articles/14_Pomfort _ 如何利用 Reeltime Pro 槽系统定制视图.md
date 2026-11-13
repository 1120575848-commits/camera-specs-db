# Pomfort | 如何利用 Reeltime Pro 槽系统定制视图

> 来源：http://mp.weixin.qq.com/s?__biz=MzU2MDYyNjA1MQ==&mid=2247484476&idx=2&sn=b12bf9ee2692ba81dd813f1f1c73676e&chksm=fc0464d0cb73edc623370784b76ff53beb3f96fe4805e4e6204365540563968fe5154306df3a#rd
> 归档自「逃避梦DIT工作室」微信公众号合集《技术分享与工作流》

---

回放操作员面临的主要挑战是满足片场每个人不同的观看要求。由于一些回放设置的局限性，剧组工作人员有时需要做出妥协，而且显示在他们的监看设备上的信号和图像往往不能完全理想地满足其职位的工作需要。




在一个理想化的世界里，向人们展示他们需要看到的东西很容易，这样他们就可以做出更明智的决定，并专注于他们手头的任务。这能够极大地加速协作过程，而这也就是我们在Reeltime Pro中开发槽系统的原因。本文中，我们将向你介绍什么是槽系统，如何使用它，以及你和你的项目如何能从中受益。










解释槽系统





你可能会问：什么是槽，我如何使用它们？


槽是一种容器，可以容纳一条实时信号、一条回放信号，或有时两者兼而有之。你可以通过连接这些容器来使用槽，以控制传入和传出信号的路由。为了给出更明确的答案，让我们来看两个例子：


例1：一般来说，输入槽代表摄影机，输出槽代表监看设备，比如SDI监看器。




摄影机“A”的信号连接到输入槽“A”。摄影机A通过视频I/O设备的SDI输入端口连接到系统；

导演的SDI监视器连接到输出槽“导演”。导演的SDI监视器通过视频I/O设备的SDI输出端口连接到系统；

现在，你可以通过设置输入槽“A”作为输出槽“导演”的源，在导演的监视器上显示来自摄影机A的信号。




例2：除了输入和输出槽之外，还有可以容纳两条或更多实时和/或回放信号的复合槽。




摄影机“A”和“B”通过视频I/O设备的SDI输入端口连接到输入槽“A”和“B”；

输出槽“导演”通过视频I/O设备的SDI输出端口连接到导演的SDI监视器；

你可以将A机和B机信号合并到一个槽中。将复合槽“Comp 1”的布局设置为“并列”，并选择输入槽“A”和“B”作为源；

通过设置复合槽“Comp 1”作为输出槽“导演”的源，你可以在导演的监视器上并列显示A机和B机的信号。




带有A机和B机并列视图的复合槽路由到导演输出槽


这些例子已指出了最关键的东西是什么：能够单独控制显示在片场监看设备上的每一处最终结果。除了提供这些观看结果，能够快速看到它们也很重要。在下一节中，我们会向你展示槽系统使你能快速交付所需内容的不同方式。那么，我们来深入介绍一下Reeltime Pro的槽类型。












槽类型：工作流程中每一步的特殊工作台





想象一下，一个熙熙攘攘的工匠作坊，充满了专门的工作台，每个工作台都配备了特定工艺方面所需的特定工具。而这个作坊的设计，及其战略布局的工作台、装配区加上仓储区，都和Reeltime Pro槽系统的功能相呼应。


继续沿着这个类比，你可以将每种槽类型视为专门用于流程中特定步骤的工作台。






输入槽：你的主工作台






输入槽的作用是充当你的主工作台。一旦设置好了其他所有内容，你会花大部分时间仅在输入槽上工作。


输入槽与摄影机信号相关联。摄影机信号通过视频I/O设备的SDI输入端口到达输入槽。它们可以让你监看和录制你收到的实时信号，既可以成组也可以是单一摄影机。录制完成后，你可以（自动）将最新一段录制内容加载到相关的一个或多个源槽中，以便进行回放。参考模式还让你能将输入槽的实时信号与加载用于回放的片段作比较。你可以，比方说，混合和覆盖你的实时信号与你最后的录制内容。这将有助于剧组工作人员精确匹配摄影机的构图或演员的起始位置。


输入槽具有独特的作用。它们可以录制、回放，还有最重要的：允许你比较实时信号和回放信号。因此，输入槽有不同的模式：






实时：用于实时监看和录制
回放：用于查看回放
参考：用于比较实时信号和回放信号






请记住，多个输出槽可以接收来自同一个输入槽的信号，因此你在“输入槽工作台”上所做的操作可能会被许多观看者看到（比如：通过不同的输出槽）。


但如果你不想把你看到的展示给所有人呢？其中一种解决方案是使用媒体库槽。那么，我们来看看我们案例里的另一个“工作台”。






媒体库槽：你的个人工作台






你可以将库槽视为你的个人工作台——在其他人实际看到它们之前，你可以先准备需要的操作或参考材料以供审片。媒体库槽直接链接到你的素材存储——即片段库。此外，每个媒体库槽在媒体库大纲中都有自己的选择。所以你可以用在片段库中选择的任何项填充任何媒体库槽。由此，你也可以很轻松地从不同的场景或地点准备镜头。比方说，你可以使用键盘的向上和向下箭头键浏览媒体夹、文件夹或智能群组的所有片段。你可以在一个媒体库槽浏览场景5，在第二个媒体库槽浏览场景7。


只要媒体库槽没有路由到任何输出槽，你就可以搜索需要的操作并准备参考材料以供审片，而不会分散片场其他人的注意力，然后通过输出槽为单独的观看者开始回放。


很不错的一点是：我们可以随意在输入槽工作台和媒体库槽工作台之间切换，但如果我们可将不同工作台上的各种信号组合起来会如何呢？比如你想要比较一条媒体库槽信号和一台监视器上的输入槽信号。或者你想用两条输入槽信号和两个媒体库槽开网格视图。将任何信号与各种复合选项结合起来显然是理想做法。因此，我们有一种专门的工作台来实现这一点：复合槽。






复合槽：你的组装区域






复合槽可用作组装区域——在这里你可以用输入槽和媒体库槽创建复合视图。与媒体库槽类似，你可以先自行准备复合视图，然后将视图分发到输出槽。四种不同的复合布局选项可以应用于许多不同的用例：






并列：创建2个槽的并列视图。

2×2网格：创建最多4个槽的网格视图。

划像：用水平划像或垂直划像比较两个槽的内容。

叠加：混合并叠加两个槽的内容（比如：比较和匹配两个镜头的构图）。






最后但也很重要的一部分：我们来聊一聊输出槽。






输出槽：你的“展厅”






输出槽好比展厅，用于展示最终成片给你的“客户”。每个输出槽都与一台监看设备相关联，而监看设备可以是下列任何一种：






一台通过视频I/O设备的SDI输出端口连接的监视器

通过Reeltime Viewer应用程序以本地串流连接的iPhone或iPad

通过Reeltime Cinema配套应用程序连接的Apple Vision Pro






你不仅可以选择输出槽的源信号，还可以选择传输技术（SDI或本地串流）。


此外，应用筛选器可让你进一步自定义每个视图。我们将在下一节中介绍筛选器。但首先，我们想强调输出槽的另一个值得一提的功能——快速路由选项：






设置槽跟随选择：你可以使用此选项将输出槽固定到UI中的当前选择项，以便输出槽检视器始终查看你所选择的内容。你可以暂时让输出槽跟随你的选择。比方说，假设你为媒体库槽中的审片准备了一种操作，并想立即将其展示给导演。在这种情况下，你可以将导演的输出槽设置为跟随你的选择，进行操作，然后禁用跟随选择选项。一旦禁用，导演的输出槽就会切换回原来的路由，比如一条实时摄影机信号。

强制槽实时：你可以使用此选项将输出槽固定到其源输入槽的实时信号上。比方说，如果想确保导演在与演员排练时总能看到实时画面，你就可以用这个方法。同时，场记仍然可以在同一个输入槽中查看上一个镜次的回放。






总的来说，通过分拆输入、输出和快速路由选项，将所有信号路由到观看者的监看设备会变得很容易。如果你可以接受轻微的延迟，这就能消除对外接视频路由器的需要。由此，你可以保持你的设置精简。


有时你可能想为监视器提供一条直接来自摄影机的实时信号。在这种情况下，你还可以将内部路由选项与保存好的外接视频路由器配置相结合。你可以通过在自动化管理器中使用视频路由配置作为“操作”来实现。这使你可根据特定事件自动更改路由配置。比方说，你可以应用不同的配置，以确保不管输出槽接收的是哪种类型的信号，你总能在无延迟的情况下收到实时信号。


正如你所看到的，槽系统可以非常灵活地路由你的出入信号。你甚至可以选择在哪台监看设备上观看者可以接收到你为他们创建的视图。但如果同时也能决定素材如何呈现不是会很便利吗？好消息——Reeltime Pro有另一个工具可以让你做到这一点：筛选器。






筛选器：进行最后润色的精密工具






好了，现在把我们的“精密工具”拿出来！使用针对每个槽的独立筛选器，你可以定制视图的风格，以满足观看者职责要求或特定用例的需求。这里的第一步是从一系列筛选器中进行选择：






带偏移、旋转参数和自动检测的裁切：从摄影机中裁切出黑色边框的元数据HUD

翻转：水平/垂直翻转图像

带偏移、比例和不透明度参数的图像覆盖（例如：用于添加logo或水印）

元数据覆盖：带摄影机元数据字段参数、打板信息、槽模式（回放/实时），片段名称和时间码

LUT：以.cube格式加载3D LUT（例如：在你接收到未调色的信号时应用一种风格）






筛选器给了槽系统更高的灵活性。你可以决定添加筛选器到输入槽、输出槽，或者两者的混合。我们来看两个例子：


例1：你直接从摄影机得到一条未调色的log信号。摄影部门提供了一个show LUT，供你应用以使片场预览效果更吸引人。在这种情况下，将LUT筛选器直接添加到输入槽是有意义的，这样所有的输出槽都将接收调色后的图像。


例2：场记希望看到所有的相关元数据，包括摄影机HUD和状态信息，但导演希望看到干净图像。没问题——你可以添加一个裁切筛选器到“导演”输出槽，并添加元数据覆盖筛选器到“场记”输出槽。这样，导演会看到干净的裁切图像，而场记会看到未裁切的摄影机信号与元数据叠加。而且无论如何，他们看到的都是相同的输入信号。好消息是：如果输出槽“场记”显示的是一个复合槽，其中A机和B机并列显示，那么元数据覆盖将自动应用于每个复合源。




带定制视图的输出槽：导演从A机获得干净图像，而场记看到的是带有来自A机和B机元数据的并列视图。


筛选器是另一位好帮手，服务于片场每个人的单独需要。现在，所有的观看者都可以在关注当前任务的同时做出明智的决定。说到这个，作为一个回放操作员，你如何专注于当前的任务？让我们来看看窗口布局吧！






多视图窗口布局：每个工作台都有一个单独的“房间”






有时你可以在一个大的区域里于工作台之间快速切换，这很有帮助。但通常情况下，你可能更希望专注于当前的任务，并且只在一个工作台上花费更长时间。Reeltime Pro的多窗口布局可以让你在每个工作台的不同“房间”之间快速切换。


主视图布局可访问具备每种类型的槽、槽设置、筛选器设置的部分，以及其他基本应用程序组件。这让你可以在不同类型的槽之间快速更改，以此来方便地设置视图。
但是，当一切都设置好之后，你可能会想留在工作台上专注于当前的任务。因此，Reeltime Pro为输入槽、媒体库槽和输出槽提供了专用的多视图。让我们再来看一些多视图提供便利的例子：


例1：你只在一台小型的MacBook Pro上工作，但你得同时监看每台摄影机的信号，以确保素材被正确拍摄、录制，并且有稳定的视频质量。你可以使用输入槽多视图布局，在一个单独的检视器窗口中查看每个活动的输入槽——它们带有所有回放或录制控件。


输入槽的多视图窗口布局


例2：当剧组在准备下一个镜头时，你可以利用这段时间在媒体库槽多视图中准备审片操作。如果你需要为每个媒体库槽预定义一个播放头位置，那么在同个UI布局中查看所有视图是有帮助的。


例3：如果你想知道片场所有观看者眼下都在看着什么图像（或者你想再次检查一遍），那么你可以在输出槽多视图中同时看到所有输出槽。


请记住，窗口布局可以通过快捷键或Stream Deck操作进行更改，让你可在窗口或“房间”之间快速切换。


总之，多窗口布局与槽系统无缝融合在一起，为你要关注的槽类型提供了一个专们的“房间”。












槽Vs.视图：为何少即是多









最后但也很重要的是，你不该将槽和传统回放系统中的“视图”混为一谈。






Reeltime Pro的3通道选项让你能远不止3视图地开展工作。它提供了3个输入槽、6个媒体库槽、2个复合槽和6个输出槽。每个槽实际上是一个单独视图，由你决定谁该看到它的内容。有了Reeltime Pro的6通道选项，你可以得到6个输入槽、9个媒体库槽、4个复合槽和9个输出槽。


因此，槽系统提供了更高的灵活性，因为在槽中创建额外的视图并不需要额外的成本。比方说，通过使用媒体库槽，你可以避免在搜索某个操作时显示给片场的每个人。此外，输入和输出槽之间的差异让你能轻松地从同一条摄影机信号中为多个观看者添加不同的视图。












槽系统的好处





本文中，我们介绍了Reeltime Pro的槽系统及其相关功能集。我们把它想象成一个为回放操作员提供专门布局的工作坊，为片场的所有岗位提供高度定制的监看结果。现在我们来总结一下我们谈到过的好处。



槽系统可以让你……






保持灵活：决定谁看到什么内容，在哪台设备上，以及素材如何呈现。

保持专注：避免冗余内容或不相关信息分散工作人员注意力。

保持所有信号透明概览：（在部分或单独的多视图布局）监看输入和输出信号。

处理多任务：同时为一位观看者提供回放并为另一位提供实时信号。工作人员在观看另一条实时或回放信号时，你可以私下准备回放。

使用小型设置：输入和输出槽搭配灵活路由选项，让你可在没有视频路由器的情况下工作。

优化可缩放性：能够与多个观看者共享一个视图，或者为个人浏览和搜索目的保留更多视图。






总的来说，槽系统能创新地处理视频回放和相关需求。你和所有剧组工作人员都能受益于灵活且透明的路由和观看选项，而且你可以很好地为片场的各位创意人员提供定制视图。因此，现在就采用Reeltime Pro槽系统提供的所有好处，来增强和加速你的协作过程吧。




出处：Pomfort
编译：Charlie | 盖雅翻译小组












您可能还对以下内容感兴趣



Reeltime Pro发布1.1版本！速来探索丰富新功能！




Pomfort | 如何以 Reeltime Pro 搭建一套视频回放系统




Pomfort | Reeltime Pro 推出全新短期许可选项，Silverstack 等多项更新




Pomfort丨Reeltime × Apple Vision Pro 探索新的监看选择，多项更新已上线




Pomfort | Livegrade 发布 6.4.3 更新！








4*BoxIO 如何运作？立陶宛 DIT 亨利卡斯·杰努蒂斯谈《88年劫案》现场调色工作流




![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajelIWHwic5Z5ibsXicoXNUhIAfRBKoefgsPyoDEnJpz5gK0xBaN5lL4ewYPA/640?wx_fmt=jpeg&from=appmsg#imgIndex=0)
![](https://mmbiz.qpic.cn/mmbiz_png/sxZZIJpvoVWMlCx4Uo5TzuhnNu3XzUlqJUcKELSyL21o08T2koaCEJHKKdqTTORwDvqlKxIV1c9fcaL4eA6k1g/640?wx_fmt=png#imgIndex=1)
![](https://mmbiz.qpic.cn/mmbiz_png/hVsxLwDqJgNVpDQxAmYBULD7tkAn2cyovmzRpM1oUHh4wV1vtu6reO3SKjHLHIOibKInHACBicJyTcwpB4p1xMww/640?wx_fmt=png#imgIndex=2)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYgLZKbdkOCTkFSJFZWvxK6aX6c9p9dAstltthMKmBX0lqcXRicrBNBzWudcn0w6halzhp0SIqOr8A/640?wx_fmt=jpeg&from=appmsg#imgIndex=3)
![](https://mmbiz.qpic.cn/mmbiz_png/sxZZIJpvoVWMlCx4Uo5TzuhnNu3XzUlqJUcKELSyL21o08T2koaCEJHKKdqTTORwDvqlKxIV1c9fcaL4eA6k1g/640?wx_fmt=png#imgIndex=4)
![](https://mmbiz.qpic.cn/mmbiz_png/hVsxLwDqJgNVpDQxAmYBULD7tkAn2cyovmzRpM1oUHh4wV1vtu6reO3SKjHLHIOibKInHACBicJyTcwpB4p1xMww/640?wx_fmt=png#imgIndex=5)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYgLZKbdkOCTkFSJFZWvxK63kHqdk3zHySypeDnYe0IVSBKhDHzNt9fa4mO1h9spOdvjhZEYib4Sfg/640?wx_fmt=jpeg&from=appmsg#imgIndex=6)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYgLZKbdkOCTkFSJFZWvxK6rJYZnUhqHYic4QuFIxGH2pibfNNibrSe3RmN5iaxFQ8n2BX6r3pyjYZAmA/640?wx_fmt=jpeg&from=appmsg#imgIndex=7)
![](https://mmbiz.qpic.cn/mmbiz_png/sxZZIJpvoVWMlCx4Uo5TzuhnNu3XzUlqJUcKELSyL21o08T2koaCEJHKKdqTTORwDvqlKxIV1c9fcaL4eA6k1g/640?wx_fmt=png#imgIndex=8)
![](https://mmbiz.qpic.cn/mmbiz_png/hVsxLwDqJgNVpDQxAmYBULD7tkAn2cyovmzRpM1oUHh4wV1vtu6reO3SKjHLHIOibKInHACBicJyTcwpB4p1xMww/640?wx_fmt=png#imgIndex=9)
![](https://mmbiz.qpic.cn/mmbiz_png/sxZZIJpvoVWMlCx4Uo5TzuhnNu3XzUlqJUcKELSyL21o08T2koaCEJHKKdqTTORwDvqlKxIV1c9fcaL4eA6k1g/640?wx_fmt=png#imgIndex=10)
![](https://mmbiz.qpic.cn/mmbiz_png/hVsxLwDqJgNVpDQxAmYBULD7tkAn2cyovmzRpM1oUHh4wV1vtu6reO3SKjHLHIOibKInHACBicJyTcwpB4p1xMww/640?wx_fmt=png#imgIndex=11)
![](https://mmbiz.qpic.cn/mmbiz_png/7VVicaGuObqYVHVFUicydJtHt5vlksunnqvet97Oe5N4MiaAeab3gIY8Bme2GhQqkMKCHNT6oySibAJsLqPQa5H9Jg/640?wx_fmt=png#imgIndex=12)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqa7icqUqdIwKHicYwa2CwwHFQYHX6DnRO47rk3OMkFNqYPiaY2EBE90By0Y3YCibE0koXt5AqTfdX8JYA/640?wx_fmt=jpeg#imgIndex=13)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYk17TZrar8RahfheoYajelDED4gQjdjazHIUEPayYlGYnLG15xDjeUTRHhfue3U6qmibPPOYmpVuQ/640?wx_fmt=jpeg#imgIndex=14)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYKZszL6QDTzBibjwtgA2hIDSMwiaz4dkkO5aCb1wOYl8fnCXN17DbYmMVIs3cJcr9cl2c2Ae293HTA/640?wx_fmt=jpeg#imgIndex=15)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqYwYib068npJuz8gCicovfMRA5NyGpejkaDKN4aDDSWLtWAclbGchggXINGodxoTiba5dKLHI8fnTCXw/640?wx_fmt=jpeg#imgIndex=16)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqbN0UZicKAD2hJ5NlOgMCbsMWLHxKPnWiavyOeAicQf33wJ2sHkRt3ic1r9fibSnpfKqcGtlsFk45L91dw/640?wx_fmt=jpeg#imgIndex=17)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7VVicaGuObqY05ucD1ZSzoH9X3748Vl4faJueHkOJq4XPX6h3SAGnc3lFGcibMxylZMeoSXaHfYmlCSxgqHBkd8w/640?wx_fmt=jpeg#imgIndex=18)
