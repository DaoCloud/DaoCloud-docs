# 聚焦 Kubernetes 指导委员会

> 英文原博客位于 [k8s.dev](https://www.kubernetes.dev/blog/2025/09/22/k8s-steering-spotlight-2025/)

**本次采访于 2024 年 8 月进行，由于指导委员会成员和选举过程的动态特性，内容可能未能准确反映实际构成。
然而，所涵盖的主题对于理解其工作范围仍具有高度相关性。随着指导委员会选举的临近，这些内容为理解委员会运作提供了有价值的见解。**

[Kubernetes 指导委员会](https://github.com/kubernetes/steering) 是 Kubernetes 项目的支柱，
确保其充满活力的社区和治理结构顺畅高效地运行。尽管 Kubernetes 的技术卓越性常常通过其
[特别兴趣小组（SIG）和工作组（WG）](https://github.com/kubernetes/community) 被聚焦，
但真正默默掌舵的英雄是指导委员会的成员。他们应对复杂的组织挑战，赋能贡献者，并培育 Kubernetes 所闻名的繁荣开源生态。

但要领导世界上最大的开源社区之一，究竟需要什么？有哪些隐性挑战？是什么驱动这些人投入时间和精力担任如此有影响力的角色？
在这次独家对话中，我们与现任指导委员会（SC）成员——Ben、Nabarun、Paco、Patrick 和 Maciej——一起探讨掌舵
Kubernetes 的收获与挑战。从他们的个人历程和动力，到委员会的重要职责与未来展望，
这篇专题文章为我们提供了难得的幕后视角，走近那些让 Kubernetes 保持航向的人。

## 自我介绍

**Sandipan: 能介绍一下你自己吗？**

**Ben:** 大家好，我是 [Benjamin Elder](https://www.linkedin.com/in/bentheelder/)，也叫 BenTheElder。
我在 2015 年以 Google Summer of Code 学生身份开始接触 Kubernetes，并自 2017 年起在 Google 从事相关工作。
我在多个领域做出贡献，尤其是构建、CI、测试工具等。我最喜欢的项目是构建 [KIND](https://kind.sigs.k8s.io/)。
我曾在发布团队工作，担任过 [SIG Testing](https://github.com/kubernetes/community/blob/master/sig-testing/README.md) 的主席，目前是 SIG Testing 和
[SIG K8s Infra](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md) 的技术负责人。

**Nabarun:** 大家好，我是来自印度的 [Nabarun](https://www.linkedin.com/in/palnabarun/)。自 2019
年起开始参与 Kubernetes。我在多个领域做出贡献：
[SIG ContribEx](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md)（同时担任主席）、
[API Machinery](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md)、[Architecture](https://github.com/kubernetes/community/blob/master/sig-architecture/README.md) 和
[SIG Release](https://github.com/kubernetes/community/blob/master/sig-release/README.md)。
我参与了多个版本的发布，并担任过
[Kubernetes 1.21](https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement/)
的发布团队负责人。

**Paco:** 我是来自中国的 [Paco](https://www.linkedin.com/in/pacoxu2020/)，曾在上海 DaoCloud
担任开源团队负责人。在社区中，我主要参与
[kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)、
[SIG Node](https://github.com/kubernetes/community/blob/master/sig-node/README.md) 和
[SIG Testing](https://github.com/kubernetes/community/blob/master/sig-testing/README.md)。
此外，我协助组织了 KCD China，并担任近期在香港举办的
[KubeCon+CloudNativeCon China 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-open-source-summit-ai-dev-china/) 的共同主席。

**Patrick:** 大家好！我是 [Patrick](https://www.linkedin.com/in/patrickohly/)。自 2018 年以来，
我一直为 Kubernetes 做出贡献。我从
[SIG Storage](https://github.com/kubernetes/community/blob/master/sig-storage/README.md) 开始，
后来逐渐参与更多领域。目前，我是 SIG Testing 的技术负责人、日志基础设施维护者，
[Structured Logging](https://github.com/kubernetes/community/tree/master/wg-structured-logging) 和
[Device Management](https://github.com/kubernetes/community/tree/master/wg-device-management)
工作组的组织者，[SIG Scheduling](https://github.com/kubernetes/community/blob/master/sig-scheduling/README.md) 的贡献者，以及指导委员会成员。当前我的主要关注领域是 [动态资源分配（DRA）](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)，这是一个用于加速器的新 API。

**Maciej:** 大家好，我是 [Maciej](https://www.linkedin.com/in/maciejszulik/)，自 2014 年末开始参与 Kubernetes，涉及控制器、apiserver 和 kubectl 等多个领域。除了身为指导委员会的一员，我还帮助指导 [SIG CLI](https://github.com/kubernetes/community/blob/master/sig-cli/README.md)、[SIG Apps](https://github.com/kubernetes/community/blob/master/sig-apps/README.md) 和 [WG Batch](https://github.com/kubernetes/community/blob/master/wg-batch/README.md)。

## 关于指导委员会

**Sandipan: 指导委员会主要做什么？**

**Ben:** 章程是权威答案，但我认为指导委员会主要是帮助解决 Kubernetes 组织层面的“人员问题”（而非技术问题），比如澄清项目治理，协调云原生计算基金会（CNCF）（例如申请额外资源和支持），以及与其他 CNCF 项目沟通。

**Maciej:** 我们的[章程](https://github.com/kubernetes/steering/blob/main/charter.md#direct-responsibilities-of-the-steering-committee)很好地描述了所有职责。简而言之，我们通过支持维护者和贡献者的日常工作，确保项目顺利运行。

**Patrick:** 理想情况下，我们什么都不做 😀 日常事务都已委托给 SIG 和 WG。只有当遇到不清楚谁来负责或需要解决冲突时，指导委员会才会介入。

**Sandipan: 指导委员会与 SIG 有何不同？**

**Ben:** 从治理角度看：指导委员会将所有子项目的所有权委托给 SIG 和/或委员会（如 _安全响应_、_行为准则_ 等）。它们非常不同。SIG 负责项目的具体部分，而指导委员会处理一些宏观的人员和政策问题。软件开发、发布、沟通和文档工作都发生在 SIG 和委员会中。

**Maciej:** SIG 或 WG 主要关注 Kubernetes 某一领域的技术方向。指导委员会则主要确保所有 SIG、WG，尤其是维护者拥有顺利开展工作的所需条件。这包括从确保 CI 系统的资金，到治理结构和政策，再到支持维护者个人的各种需求。

**Sandipan: 你们提到项目，可以举个近期指导委员会做过的例子吗？**

**Ben:** 我们一直在讨论如何更好地将项目的正式维护者定义同步到 CNCF。例如，这个名单会用于投票 [技术监督委员会](https://www.cncf.io/people/technical-oversight-committee/)（TOC）。目前，这个名单是指导委员会，以及 SIG 贡献者体验、Infra 和 Release 负责人可以访问 CNCF 服务台。这在 CNCF 项目中还没有统一标准，但我认为很重要。

**Maciej:** 过去一年里，我在指导委员会的主要任务大多是提供签证申请支持信。此外，每年我们都会协助所有 SIG 和 WG 撰写年度报告。

**Patrick:** 自从我和 Maciej 在 2023 年底加入指导委员会以来，显然这是比较安静的一年。这正是理想状态。

**Sandipan: 有没有一些项目提交到指导委员会，最后你们转交给 SIG 的？**

**Ben:** 我们经常收到关于测试/构建资源的请求，会转交给 SIG K8s Infra + SIG Testing；或者关于子项目发布的请求，会转交给 SIG K8s Infra / SIG Release。

## 通往指导委员会之路

**Sandipan: 是什么驱动你们加入指导委员会？你们的经历如何？**

**Ben:** 有几个人联系我并鼓励我参选，但我的动力主要来自于我对社区和项目的热情。我认为我们正在做的事情很特别，我非常关心它的持续成功。我整个职业生涯都在这个领域，虽然总会有棘手的问题，但这个社区一直非常支持，我希望能保持下去。

**Paco:** 在我参加 [Kubernetes 贡献者峰会 EU 2023](https://www.kubernetes.dev/events/2023/kcseu/) 后，我结识并与许多维护者和成员交流，并首次参加了 Steering 的 AMA。由于自 2019 年起中国没有举办过贡献者峰会，我开始与中国的贡献者建立联系，并推动在当年晚些时候举办。通过在 KCS EU 和本地的交流，我意识到为亚太区贡献者降低参与门槛、吸引更多人加入社区非常重要。之后，我在 [KCS CN 2023](https://www.kubernetes.dev/events/2023/kcscn/) 之后当选。

**Patrick:** 我之前做了很多技术工作，其中一些影响并（希望）惠及了所有 Kubernetes 贡献者（如 lint 和测试）以及用户（更好的日志输出）。我把加入指导委员会视为帮助运行大型开源项目的组织事务的机会。

**Maciej:** 我考虑参选指导委员会已经有一段时间了。最大的推动力来自与社区成员的交流。最终在去年，我决定听取他们的建议，并顺利当选 :-)

**Sandipan: 你最喜欢身为指导委员会成员的哪一部分？**

**Ben:** 当我们能直接帮助贡献者时。例如，有时长期贡献者会联系委员会索取正式信函，用于签证申请，解释他们的贡献和价值。能够纯粹地帮助 Kubernetes 贡献者，是我最喜欢的部分。

**Patrick:** 这是一个直接从其他优秀成员那里学习项目实际运行方式的好机会。

**Maciej:** 和项目一样，最棒的始终是身边的人——他们给了我们合作的机会，共同创造有趣和令人兴奋的东西。

**Sandipan: 你觉得作为指导委员会成员最具挑战性的部分是什么？**

**Ben:** 我认为我们都花了很多时间在可持续性问题上，却没有一个完美的答案。很多人都在努力解决这些问题，但我们时间和资源有限。我们已将大部分事务正式委托（如 SIG ContribEx 和 K8s Infra），但我们仍然认为它们很重要，值得投入更多精力。然而，答案并不明显，平衡非常困难。

**Paco:** 对我而言，贡献者和维护者的可持续性是最大挑战之一。我一直在倡导 OSS 用户和雇主加入社区。社区是开发者互相学习、讨论问题、分享经验和解决方案的地方。确保社区中的每个人都感到被支持和重视，对于项目的长期健康至关重要。

**Patrick:** 关于项目运作的文档虽然存在，但并不全面。有些部分故意未记录，可能是因为不能公开、变化太快，或需要个案处理。幸运的是，我们有任期交叠，可以向有经验的成员学习。我们还有一份前成员名单，他们也乐意回答问题。

**Maciej:** 未知的未知 :-) 在我当选后，我尝试和现任及往届成员交流。最大的挑战是，无论你准备多么充分，总会遇到前人未曾面对的新问题。

**Sandipan: 对未来想竞选指导委员会的人，你们认为最重要的建议是什么？**

**Ben:** 指导委员会的大部分工作是“突发驱动”的……总会有突发问题需要解决——请确保你有承诺并准备好腾出时间。同时，希望你能冷静思考问题，并以同理心倾听社区声音。

**Paco:** 这是前任成员调查中的一句话：我们要确保“每个人的声音都被听到和尊重”（来自 Clayton）。对社区而言，最重要的部分就是人。

**Maciej:** 一旦决定参选并当选，请确保每周固定安排时间处理指导委员会事务。有时可能没什么事情，有时又可能事务堆积。预留时间能保证你作为成员的工作一致性。

## 结语

每一个成功的开源项目背后，都有一群确保其顺利运行的 dedicated 人，而 Kubernetes 指导委员会正是这样做的。他们默默而高效地工作，应对挑战，支持贡献者，确保社区保持开放与活力。

他们的特别之处在于专注于“人”——赋能贡献者、解决治理问题，并营造一个创新可以蓬勃发展的环境。这并不容易，但正如他们所分享的那样，这是极具回报的。

无论你是长期贡献者还是正在考虑参与，Kubernetes 社区都欢迎你。Kubernetes 的核心不仅仅是技术——更是让一切发生的人。永远有空间为多一个声音，共同塑造未来。
