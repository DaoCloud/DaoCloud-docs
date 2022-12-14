---
hide:
  - toc
---

# 博客文章

本页汇总 DCE 5.0 相关的博客和公众号文章，默认按字母和拼音排序。

- [20221209 | 保姆式安装 DCE 5.0 社区版](./dce5-install1209.md)

    这是从 0 到 1 安装 DCE 5.0 社区版的真实示例，包含了 K8s 集群、依赖项、网络、存储等细节及更多注意事项。

- [20221130 | Karmada 资源解释器](https://mp.weixin.qq.com/s/DLDmWRmhM_gMVg1qGnj_fA)

    Karmada 已被越来越多的企业，应用到多云和混合云场景中。
    在实际应用过程中，用户经常会遇到，通过 PropagationPolicy 来分发各种资源到成员集群的使用场景。
    这就要求分发的资源类型，不仅仅要包含常见的 Kubernetes 原生或知名扩展资源，同时也需要能支持分发用户的自定义资源。
    因此 Karmada 引入了内置解释器来解析常见的 Kubernetes 原生或知名扩展资源，同时又设计了自定义解释器来解释自定义资源的结构，并且在近期提出了可配置解释器方案。
    对无论是自定义资源，还是常见的 Kubernetes 原生资源，都可以提供更加灵活可配置的自定义方法，来提取资源的指定信息，例如副本数、状态等。

- [20221125 | KubeCon 2022 北美站 | 精彩看点回顾](https://mp.weixin.qq.com/s/HIxBZjCK8ofCN6C5KRY25w)

    2022 年 11 月落幕的云原生顶级会议 2022 KubeCon 北美站上，来自世界各地的云原生技术专家、产品或解决方案供应商和使用者带来了 300 多场精彩纷呈的演讲。
    主题涵盖 Kubernetes、GitOps、可观测性、eBPF 、网络、服务网格和安全等。
    本文精心挑选了此次会议上的几个热点话题演讲，进行简单介绍，感受每一次演讲和讨论背后所蕴藏的云原生趋势。

- [20221123 | 走进车企的数字原生之路 | 论道回顾](https://mp.weixin.qq.com/s/1leu7b8KQw9pcqma8A_cuw)

    11 月 18 日，由「DaoCloud 道客」主办的「论道原生｜云原生数字生态私享会・走进车企」成功举办。
    本次活动从车企的具体案例出发，主要分享了云原生在汽车行业的应用与实践。让我们一起回顾一下本次活动的精彩内容。

- [20221115 | SpiderPool - 云原生容器网络 IPAM 插件](https://mp.weixin.qq.com/s/r6YiuUBGD2KmmMOxl26X6A)

    SpiderPool 来源于容器网络落地实践的经验积累，是「Daocloud 道客」开源的原生容器网络 IPAM 插件（github：https://github.com/spidernet-io/spiderpool），
    主要用于搭配 Underlay CNI 实现容器云平台精细化的管理和分配 IP。

- [20221110 | 源于热爱，始于坚持，不忘初心 — 「DaoCloud 道客」八岁生日快乐！](https://mp.weixin.qq.com/s/4cYUXtZFc3tIjzphVRCSLg)

    时光荏苒，岁月如梭。自 2014 年 11 月成立以来，在 DaoClouders 不懈的耕耘中，「DaoCloud 道客」已经走过了八个年头。
    在 11 月 8 日下午，「DaoCloud 道客」全体船员为 「DaoCloud 道客」举办了生日会。让我们一起来看看「DaoCloud 道客」八岁生日会的盛况吧！

- [20221105 | DaoCloud 是 K8s 资深认证服务商](./kcsp.md)

    DaoCloud 早在 2017 年就首次顺利通过了 Kubernetes 认证，是国内最早涉足并得到 CNCF 官方认可的服务商， 同时也是国内最早获得 Kubernetes Training Partner (KTP) 认证的厂商。
    目前经 CNCF 官方认证可支持的 K8s 版本包括：v1.25, v1.24, v1.23, v1.20, v1.18, v1.15, v1.13, v1.9, v1.7

- [20221105 | 原生思维看金融数字化转型](https://mp.weixin.qq.com/s/9BggFRr0aoEzzmemXplRWg)

    2022 年 11 月 5 日至 6 日，由西南财经大学、成都市地方金融监督管理局和成都市温江区人民政府联合主办的第五届国际金融科技论坛 2022 在蓉成功举办。
    5 日下午以 “数字经济赋能金融科技创新” 为主题的论坛邀请「DaoCloud 道客」创始人兼首席执行官、云原生计算基金会大使陈齐彦先生做主题演讲。本文根据演讲内容整理。

- [20221104 | HwameiStor 入选 CNCF 全景图：生产可运维的云原生本地存储系统](https://mp.weixin.qq.com/s/QqzU_YeUKmegaMiQ9MVbww)

    近日，CNCF（云原生计算基金会）[^1] 发布了最新版的云原生全景图 [^2]。
    「DaoCloud 道客」自主开源的云原生本地存储系统 HwameiStor，被收录在 CNCF 云原生全景图中的 RunTime（运行时）层的 Cloud Native Storage（云原生存储）象限，成为 CNCF 推荐的云原生本地存储项目。

- [20221028 | Kubean 集群生命周期管理](https://mp.weixin.qq.com/s/-NzXmyb-9yQc1ydcsZz0CA)

    Kubean 采用 Kubespray 作为底层技术依赖，一方面简化了集群部署的操作流程，降低了用户的使用门槛。
    另一方面在 Kubespray 能力基础上增加了集群操作记录、离线版本记录等诸多新特性。
    Kubean 还提供了界面化创建集群的能力（需要结合社区版 DCE 5.0 容器管理功能），让新手用户也能一键创建和管理集群。

- [20221028 | 激活医疗、人工智能的数字新动能 | 云原生底座](https://mp.weixin.qq.com/s/VoUCiXaUuEy0wKlHmTqo4w)

    10 月 28 日，由「DaoCloud 道客」主办的「论道原生｜云原生数字生态私享会・上海」成功举办。
    本次活动从云原生思维和技术出发，分享了云原生在医疗和人工智能方面的应用与实践。让我们一起回顾一下本次活动的精彩内容吧。

- [20221026 | DCE 5.0 容器管理能力介绍](./kpanda.md)

    说明 DCE 5.0 容器管理模块提供的能力。

- [20221018 | DCE 5.0 资源管理能力介绍](./resource.md)

    说明 DCE 5.0 全局管理模块提供的能力。

- [20220925 | DCE 5.0 应用工作台能力介绍](./amamba.md)

    说明 DCE 5.0 应用工作台模块提供的能力。

- [20220914 | Merbridge 入选 eBPF 全景图](https://mp.weixin.qq.com/s/Ia9Oi3pKuLcrFJwazmpEjg)

    花开自有期，绽放亦有时。在所有贡献者的共同努力和呵护下，Merbridge 的花苞徐徐绽放开来。
    2022 年 4 月初，Merbridge 顺利入选 CNCF 云原生全景图（Cloud Native Landscape），
    进入 Orchestration & Management (编排与管理) 层的 Service Mesh (服务网格) 象限，成为 CNCF 推荐的云原生服务网格加速器。

- [20220909 | Clusterpedia 使用心得](https://mp.weixin.qq.com/s/GAcBIshuaOXUrDgzIguWHg)

    Kubernetes 带来的云原生技术革命已席卷全球，越来越多的业务应用运行在 Kubernetes 平台上，
    随着业务规模的扩展，集群数量与日俱增，多集群内部资源管理和检索越来越复杂，多云管理面临巨大挑战。
    在多集群时代，我们可以通过 Cluster-api 来批量创建管理集群，使用 Karmada/Clusternet 来分发部署应用。
    不过我们貌似还是缺少了什么功能，我们要如何去统一地查看多个集群中的资源呢？

- [20220908 | 华为与「DaoCloud 道客」推出面向元宇宙的云边协同超融合一体机](https://mp.weixin.qq.com/s/r8vfFofBy7v1VcUMInp_Iw)

    2022 年 9 月 2 日，在世界人工智能大会上，华为与上海道客网络科技有限公司联合推出面向元宇宙创新业务的 “云边协同超融合一体机”，
    将云原生能力下沉至边缘，提供实时的虚拟数字世界体验，实现真正的云边一体化元宇宙。

- [20220905 | 如何打好存储基础，筑就云原生应用基石？| 论道原生](https://mp.weixin.qq.com/s/vrBAjdCkI2BKxG7SsSX2Uw)

    应用的云原生化极大地提升了自身的可用性、稳定性、扩展性、性能等核心能力，同时也深刻改变了应用的方方面面，
    存储作为应用运行的基石，也不可避免地受到了冲击。云原生时代背景下，给存储带来了怎样的挑战，又该如何应对呢？
    第十一期论道原生，「DaoCloud 道客」携华为，分享云原生存储解决方案。

- [20220810 | Cluster API 检索从未如此简单](https://mp.weixin.qq.com/s/8F20pchW6WhbEdlU56qFsg)

    Clusterpedia 是一个 CNCF 沙箱项目，用于跨集群复杂的资源检索。
    名字源于 Wikipedia，寓意是打造多集群的百科全书，可以与多个集群同步资源，
    并在与 Kubernetes OpenAPI 兼容的基础上，提供更强大的搜索功能，以帮助您快速、简便、有效地获取任何多集群资源。

- [20220808 | DCE 5.0 多云编排能力介绍](./kairship.md)

    说明 DCE 5.0 多云编排模块提供的能力。

- [20220708 | DCE 5.0 服务网格能力介绍](./mspider.md)

    说明 DCE 5.0 服务网格模块提供的能力。

- [20220622 | Clusterpedia 作为首个多云检索开源项目正式进入 CNCF 沙箱](https://mp.weixin.qq.com/s/K2jG64msI4j-mWqPF0qkKg)

    2022 年 6 月 15 日，云原生计算基金会 (CNCF) 宣布 Clusterpedia 正式被纳入 CNCF 沙箱（Sandbox）项目。
    Clusterpedia 是由「DaoCloud 道客」于 2021 年年底推出的开源项目，是一个通过加持 kubectl 就能完成多集群资源复杂检索的神器，
    也是目前 CNCF 唯一专注于多云信息检索的项目，正被广泛使用。

- [20220611 | CloudTTY：下一代云原生开源 Cloud Shell](https://mp.weixin.qq.com/s/sFjZmvumQNbP6gnlnpglWQ)

    CloudTTY 是一个云原生开源项目， 基于 kubernetes 之上，解决了一系列集群之上的 “网页命令行” 权限控制下的功能需求。

- [20220609 | KubeCon EU 热门云原生技术分享 | 精彩看点回顾](https://mp.weixin.qq.com/s/2ukrV3M6dGdwzRPnigovkw)

    在刚刚过去的年度最顶级的云原生旗舰会议 KubeCon + CloudNativeCon Europe 2022 上，
    全球的云原生技术专家、产品或解决方案供应商和使用者，对云原生进行广泛充分地交流和讨论。
    本文从云原生的外部融合、自身演进、内部相关功能特性这三个方面，分享一些大会上热门的云原生开源项目，一起走进云原生。

- [20220606 | Merbridge CNI 模式](https://mp.weixin.qq.com/s/3t2FshkQpVHQ44zbBIQDRQ)

    Merbridge CNI 模式的出现，旨在能够更好地适配服务网格的功能。
    之前没有 CNI 模式时，Merbridge 能够做得事情比较有限。
    其中最大的问题是不能适配注入 Istio 的 Sidecar Annotation，这就导致 Merbridge 无法排除某些端口或 IP 段的流量等。
    同时，由于之前 Merbridge 只处理 Pod 内部的连接请求，这就导致，如果是外部发送到 Pod 的流量，Merbridge 将无法处理。

- [20220606 | DCE 5.0 研发背景](./blog00.md)

    简述新一代云原生操作系统 DaoCloud Enterprise 5.0 诞生的背景。

- [20220530 | 云原生布局开始加速，市场前景如何？收好这份指南](https://mp.weixin.qq.com/s/S6CUDwCDZh-I4e5D1SZa4A)

    本文以 Infographic 模式图解说明了当前快速发展的云原生与云计算浪潮。

- [20220520 | 走进可观测性 | 论道原生](https://mp.weixin.qq.com/s/f0oZV5nWfc42b-b0cLkh2g)

    2018 年起可观测性 (Observability) 被引入 IT 领域，CNCF-Landscape 组织创建了 Observability 的分组。
    自此，可观测性逐渐取代传统的系统监控，从被动监控转向主动观测应用关联的各类数据，成为云原生领域的最热门话题之一。

[^1]: CNCF：全称 Cloud Native Computing Foundation (云原生计算基金会)，隶属于 Linux 基金会，成立于 2015 年 12 月，是非营利性组织，致力于培育和维护一个厂商中立的开源生态系统，来推广云原生技术，普及云原生应用。
[^2]: 云原生全景图：由 CNCF 从 2016 年 12 月开始维护，汇总了社区成熟和使用范围较广、具有最佳实践的产品和方案，并加以分类，为企业构建云原生体系提供参考，在云生态研发、运维领域具有广泛影响力。
