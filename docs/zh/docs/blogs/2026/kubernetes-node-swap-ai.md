# Kubernetes 上的 cgroup v1 已死：接下来会发生什么

> 英文原稿为 [Kubernetes on cgroup v1 is dead. Here’s what comes next.](https://thenewstack.io/kubernetes-node-swap-ai/)
>
> 作者 [Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)，发表于 2026 年 10 月 9 日。本文为 The New Stack《Road to KubeCon》系列译稿。

边缘 AI 正在重塑 Kubernetes：节点交换内存最高可将密度提升约 3 倍，cgroup v2 全面接管，Edge Day 与 CiliumCon 也将在 KubeCon NA 前再度回归。

欢迎回到新一期的 Road to KubeCon。我们将跟踪云原生生态的最新动向，为 2026 年 11 月 9–12 日在犹他州盐湖城举行的 [KubeCon + CloudNativeCon North America 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 做准备。

本期关注的是：当计算工作负载需要在边缘跑 AI 时会发生什么。底层的 Kubernetes 机制在变，可观测实践与安全决策也在变。我们会梳理正在涌现的应对思路，以及几个关键项目如何回应这些变化。

下文涵盖：如何打开 Kubernetes 的容量空间、HPE 在 AI 专用算力上的进展、一次关于已废弃 Linux 内核接口的迁移提醒，以及今年 Kubernetes on Edge Day 与 Cilium 同场活动的看点。

## HPE：为什么边缘需要专用算力

把 AI 推理放到边缘有很多理由——减少不必要的服务器往返、降低数据出站费用，以及出于合规把数据留在云外。因此，许多企业正基于这些原因转向边缘 AI。

Hewlett Packard Enterprise（HPE）是 Road to KubeCon 的呈现赞助商。HPE Software 帮助 IT 组织在混合、多厂商环境中完成基础设施现代化、简化运维，并加速 AI 相关举措。

不过，正如 HPE 的 Aaron Lamond 在近期 [HPE 博文](https://www.hpe.com/us/en/newsroom/)中指出的那样，组织往往在用未针对场景优化的服务器硬套需求，相当于方枘圆凿。“随着智能日益分布式部署，专用算力对运营成功变得越来越关键，”他写道。

对 Lamond 而言，“专用算力”应同时考虑硬件、软件、安全与运维如何协同。他认为 ProLiant 边缘服务器适合这一任务：它们面向资源受限环境做了边缘优化，同时具备高规格安全能力。

## Kubernetes on Edge Day：边缘知识再度集结

Kubernetes 上的边缘部署已经升温多年，CNCF 项目如 [KubeEdge](https://kubeedge.io/) 以及众多厂商平台都在支撑边缘侧 Kubernetes。今年的 KubeCon + CloudNativeCon 将举办专门的同场活动 [Kubernetes on Edge Day](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/kubernetes-on-edge-day/)，探讨云原生与边缘计算的交汇。

正如 Mars Toktonaliev 与 Katerina Arzhayev 在 [CNCF 博客](https://www.cncf.io/blog/)中所写：“这一活动的设立，是为了弥合以数据中心为中心的传统云原生方法，与边缘计算真实运维之间的鸿沟。”他们特别提到可观测性与安全是相关主题。

Kubernetes on Edge Day 的日程将呈现大量案例与运维指引——对在分布式、资源受限环境中运行 Kubernetes 的工程师很有帮助。

## 节点交换内存：Kubernetes 密度最高可提升约 3 倍

突发性的智能体 AI 工作负载，往往会在启动时突然吃掉大量内存；之后内存又长期闲置。但闲置的 RAM 很贵，这种分配方式也直接卡住了 Kubernetes 集群密度。

Ocean Xie 与 Yuan Wang 在 [Kubernetes 博客](https://kubernetes.io/blog/2026/10/05/scaling-kubernetes-workloads-with-node-swap/)上深入讨论了这一问题。“内存往往是 Kubernetes 集群最先撞上的硬性上限，”他们写道，“节点耗尽 RAM 的时间远早于耗尽 CPU，而新一波智能体 AI 工作负载让这件事更糟。”

他们提出在 Kubernetes 节点上启用节点交换内存（node swap）。该能力已在 Kubernetes v1.34 正式发布（GA），可在流量高峰时充当“减震器”。

在他们的基准测试中，当节点交换内存由高速 NVMe SSD 承载时，某些场景下密度最高可提升约三倍。这一分析补充了缓解智能体 AI 高算力开销与成本的实践方法。

本站已有该文的中文译稿：[Kubernetes 节点交换内存：AI 工作负载的 Pod 密度最多可提升 3 倍](./k8s-node-swap.md)。

## 自托管平台部署：安装前就要先准备好

本周，托管云原生基础设施服务商 Fairwinds 分享了面向销售自托管 AI 平台团队的实用建议。工程总监 Munib Ali 指出：安装只是开始。

Ali 认为，有一个能跑通的安装器还不够。平台厂商往往只管交付，却忽略客户侧需要提前理顺的周边机制——例如事先划清团队职责、配置 IAM、持续维护、与客户私有云的兼容性、支持的 DNS 配置等。

“面向 AI 平台的自托管 Kubernetes 部署，常常因为客户前置条件、环境限制和跨团队交接不完整而卡住，”Ali 说。没有这些准备，上线日期会一拖再拖，项目甚至可能根本启动不了。

部分云原生厂商出于隐私、主权或可控性，提供客户侧托管交付。但要让流程顺畅、避免卡点，团队需要在“上线日”之前就把大量事项想清楚——这理应是双方共同的责任。

随着 Kubernetes 演进，运维团队面临的要求也在提高。呈现赞助商 HPE 通过覆盖虚拟化、云管理、可观测性与自动化的软件，帮助团队应对这种复杂性。

## Kubernetes 转向 Linux cgroup v2

道客（DaoCloud）开源团队负责人徐俊杰（Paco Xu）分享了关于 [cgroup v2](https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift/) 的思考——这是内核用于管理 CPU、内存等资源的特性。在他看来，cgroup v1 有诸多局限。

“与 cgroup v1 相比，cgroup v2 提供了单一统一层级、更一致的接口，以及更强的资源隔离基础和现代资源管理能力，”徐俊杰写道。视 Kubernetes 版本与配置而定，cgroup v2 还支持内存服务质量（Memory QoS）更新、容器感知的 OOM 处理、rootless 支持等能力。

自 v1.35 起，kubelet 默认会拒绝在 cgroup v1 节点上启动。若你仍在较旧版本上，他建议在升级前把每一台 Linux 节点都迁移到 v2。运维人员应及时响应，既享受收益，也避免架构继续老化。

这也是节点交换内存能落地的前提之一：节点交换依赖 cgroup v2 的独立交换内存核算。详见本站译稿 [Kubernetes 节点交换内存](./k8s-node-swap.md) 中的落地提示。

## Cilium 社区近况

Cilium 是基于 eBPF 的网络、可观测与安全项目，已从 CNCF 毕业。今年 11 月 9 日，它将在盐湖城再次举办同场活动。与会者可以期待聚焦云原生 AI 与安全的议题。

正如 Joe Stringer（Isovalent at Cisco）与 Google 的 Jordan Rife 在 [CNCF 博客](https://www.cncf.io/blog/)中所写：“今年的议程直指当 AI 与 GPU 工作负载把 Kubernetes 网络推到其原有设计边界之外时出现的问题。”

社区持续回应新的 GPU 需求、AI 驱动的可观测要求，以及新出现的漏洞。近期也涌现出不少有意思的案例，展示 Cilium 以及 eBPF 如何被更广泛地用于生产。

“Cilium 最近与 Splunk、Celonis、Preferred Networks 的案例，谈到了 eBPF 如何用于安全与 AI 场景，我认为这很好地预示了方向，”Cilium 与 eBPF 社区的 Bill Mulligan 告诉 The New Stack。

他还提到 Meta 开源的 eBPF 安全工具 [BpfJailer](https://github.com/facebook/bpfjailer)——这是 Meta 内部闭源 eBPF 安全工具的实验性开源重写。

关注 Cilium、Tetragon 或 eBPF 的朋友还需留意：Isovalent 也会在盐湖城举办 Hive Mind Mingle……名额有限，请尽早报名。

## 继续跟随 Road to KubeCon

Road to KubeCon 是由 HPE 呈现的八篇系列，面向盐湖城的 KubeCon + CloudNativeCon North America。出发前，不妨了解 HPE Software 如何帮助 IT 团队用更少复杂度做更多事。

与此同时，你也可以回看往期内容：Kubernetes v1.37、推理成本、OpenTelemetry 更新，以及云原生 AI harness 等，或浏览完整存档。

本系列作者 Bill Doerrfeld 欢迎投稿。可通过其个人联系页发送 PR、动态、项目、引言或观点。
