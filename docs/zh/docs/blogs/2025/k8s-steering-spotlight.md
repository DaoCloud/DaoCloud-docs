# 聚焦 Kubernetes 指导委员会

> 英文原博客位于 [k8s.dev](https://www.kubernetes.dev/blog/2025/09/22/k8s-steering-spotlight-2025/)

**本次采访于 2024 年 8 月进行。由于指导委员会成员和选举过程具有动态变化的特点，本文内容可能未能完全准确地反映实际成员情况。
但文中探讨的主题依然高度相关，有助于理解委员会的职责与运作。随着指导委员会选举临近，这些分享为我们了解其工作方式提供了宝贵的视角。**

[Kubernetes 指导委员会](https://github.com/kubernetes/steering)是整个项目的中流砥柱，
它不仅确保社区充满活力，还保障治理结构高效顺畅地运转。虽然 Kubernetes 的技术卓越性常通过
[特别兴趣小组（SIG）和工作组（WG）](https://github.com/kubernetes/community)为人所熟知，
但真正默默掌舵的幕后力量正是指导委员会成员。他们应对复杂的组织挑战，支持贡献者成长，并培育出 Kubernetes 引以为傲的繁荣生态。

要领导世界上最大的开源社区之一，需要具备哪些素质？背后有哪些鲜为人知的挑战？又是什么动力驱使这些人投入时间与精力担任如此关键的角色？
在这次专访中，我们与现任委员会成员 Ben、Nabarun、Paco、Patrick 和 Maciej 深入交流，
探讨他们在 Kubernetes 中的收获与挑战。本文不仅涵盖了他们的个人经历与参与动机，还展现了委员会的重要职责与未来展望，
为我们揭开了 Kubernetes 背后的故事，让大家更接近那些守护项目健康发展的贡献者们。

## 自我介绍

**Sandipan: 能介绍一下你自己吗？**

**Ben:** 大家好，我是 [Benjamin Elder](https://www.linkedin.com/in/bentheelder/)，大家也叫我 BenTheElder。
我在 2015 年以 Google Summer of Code 学生身份第一次接触 Kubernetes，并自 2017 年起在 Google 工作。
我在多个领域有过贡献，尤其是构建、CI 和测试工具。我最喜欢的项目是 [kind](https://kind.sigs.k8s.io/)。
我曾在发版团队工作，也担任过 [SIG Testing](https://github.com/kubernetes/community/blob/master/sig-testing/README.md) 主席，目前是 SIG Testing 和
[SIG K8s Infra](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md) 的技术负责人。

**Nabarun:** 大家好，我是来自印度的 [Nabarun](https://www.linkedin.com/in/palnabarun/)。自 2019
年起开始参与 Kubernetes。我在多个领域有过贡献：
[SIG ContribEx](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md)（现任主席）、
[API Machinery](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md)、
[Architecture](https://github.com/kubernetes/community/blob/master/sig-architecture/README.md) 和
[SIG Release](https://github.com/kubernetes/community/blob/master/sig-release/README.md)。
我也参与过多个版本的发布，并曾担任
[Kubernetes 1.21](https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement/)
的发版团队负责人。

**Paco:** 我是来自中国的 [Paco](https://www.linkedin.com/in/pacoxu2020/)，现任上海 DaoCloud
开源团队负责人。在 Kubernetes 社区中，我主要参与
[kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)、
[SIG Node](https://github.com/kubernetes/community/blob/master/sig-node/README.md) 和
[SIG Testing](https://github.com/kubernetes/community/blob/master/sig-testing/README.md)。
此外，我还协助组织了 KCD China，并担任了近期在香港举办的
[KubeCon+CloudNativeCon China 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-open-source-summit-ai-dev-china/) 联席主席。

**Patrick:** 大家好！我是 [Patrick](https://www.linkedin.com/in/patrickohly/)。自 2018 年起，
我一直活跃在 Kubernetes 社区。我从
[SIG Storage](https://github.com/kubernetes/community/blob/master/sig-storage/README.md)
开始贡献，之后逐渐涉足更多领域。目前我是 SIG Testing 技术负责人、日志基础设施维护者，
也是 [Structured Logging](https://github.com/kubernetes/community/tree/master/wg-structured-logging) 和
[Device Management](https://github.com/kubernetes/community/tree/master/wg-device-management)
工作组的组织者，同时参与 [SIG Scheduling](https://github.com/kubernetes/community/blob/master/sig-scheduling/README.md) 的工作，并担任指导委员会成员。
当前我的重点是[动态资源分配（DRA）](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)，这是面向加速器的一项全新 API。

**Maciej:** 大家好，我是 [Maciej](https://www.linkedin.com/in/maciejszulik/)。自 2014 年底起，我一直参与 Kubernetes，涉及控制器、apiserver 和 kubectl 等多个领域。除了担任指导委员会成员外，我还为
[SIG CLI](https://github.com/kubernetes/community/blob/master/sig-cli/README.md)、
[SIG Apps](https://github.com/kubernetes/community/blob/master/sig-apps/README.md) 和
[WG Batch](https://github.com/kubernetes/community/blob/master/wg-batch/README.md) 提供支持。

## 关于指导委员会

**Sandipan: 指导委员会的主要职责是什么？**

**Ben:** [章程](https://github.com/kubernetes/steering/blob/main/charter.md#direct-responsibilities-of-the-steering-committee)中写得很清楚。
我个人认为，指导委员会主要是帮助解决 Kubernetes 组织层面的“人”的问题（而非技术问题），
比如澄清项目治理规则，协调云原生计算基金会（CNCF）（例如申请额外资源和支持），以及与其他 CNCF 项目沟通。

**Maciej:** 我们的[章程](https://github.com/kubernetes/steering/blob/main/charter.md#direct-responsibilities-of-the-steering-committee)很好地总结了职责。
简单来说，我们通过支持维护者和贡献者的日常工作，确保整个项目顺利运转。

**Patrick:** 理想情况下，我们最好什么都不用做 😀 日常事务已经交给各个 SIG 和 WG 处理。
只有在遇到职责不清或出现冲突时，指导委员会才会出面介入。

**Sandipan: 指导委员会与 SIG 有什么不同？**

**Ben:** 从治理角度看，指导委员会会将子项目的所有权委托给 SIG 或委员会（如 **安全响应**、
**行为准则** 等）。两者的职责完全不同。SIG 负责具体的技术领域，而指导委员会处理宏观层面的人事与政策问题。
软件开发、发布、沟通和文档工作都在 SIG 和相关委员会中进行。

**Maciej:** SIG 或 WG 专注于 Kubernetes 某一特定领域的技术方向，而指导委员会则确保所有
SIG、WG，尤其是维护者具备顺利开展工作的条件。这涵盖了从 CI 系统的资金支持，到治理结构与政策，再到对维护者个人的支持。

**Sandipan: 能举个近期指导委员会处理过的项目例子吗？**

**Ben:** 我们最近一直在讨论如何更好地把 Kubernetes 项目的正式维护者名单与 CNCF 保持一致。
例如，这个名单会用于 [技术监督委员会](https://www.cncf.io/people/technical-oversight-committee/)（TOC）的投票。
目前，这份名单存放在 CNCF 服务台，仅指导委员会和 SIG ContribEx、Infra、Release 等负责人能访问。
虽然 CNCF 各项目尚无统一标准，但我觉得这是非常重要的工作。

**Maciej:** 过去一年里，我在指导委员会的主要工作之一是为社区成员的签证申请提供支持信函。
此外，我们每年还会协助各 SIG 和 WG 完成年度报告。

**Patrick:** 自从我和 Maciej 在 2023 年底加入以来，这一年相对比较安静。事实上，这正是理想状态。

**Sandipan: 有没有一些提交给指导委员会的事务，最后被转交给 SIG？**

**Ben:** 经常有这种情况。比如关于测试/构建资源的请求，我们会转交给 SIG K8s Infra 和 SIG Testing；
涉及子项目发布的请求，则交给 SIG K8s Infra 或 SIG Release 处理。

## 通往指导委员会之路

**Sandipan: 是什么促使你们加入指导委员会？经历如何？**

**Ben:** 一些人联系我并鼓励我参选，但真正的动力来自于我对社区和项目的热情。
我觉得我们正在做的事情非常特别，也希望它能持续成功。我整个职业生涯都在这里，
虽然常常面临棘手的问题，但社区一直非常支持，我也希望能让这种氛围延续下去。

**Paco:** 我是在参加 [Kubernetes 贡献者峰会 EU 2023](https://www.kubernetes.dev/events/2023/kcseu/)
后，对 Steering 有了更深入的了解。当时我与许多维护者交流，并首次参加了 Steering 的 AMA。
由于中国自 2019 年后就没有再举办过贡献者峰会，我开始推动与国内贡献者建立联系，
并促成了当年在中国举办的峰会。通过这些交流，我意识到降低亚太区贡献者的参与门槛、吸引更多人加入社区非常重要。
之后，在 [KCS CN 2023](https://www.kubernetes.dev/events/2023/kcscn/) 之后我顺利当选。

**Patrick:** 在此之前，我更多专注于技术工作，比如 lint、测试框架，这些成果既帮助了贡献者，也提升了用户体验（例如更好的日志）。
我把加入指导委员会看作是进一步支持大型开源项目运作的机会。

**Maciej:** 我其实早就考虑过参选指导委员会。推动力来自与社区成员的交流。
最终在去年，我决定听取大家的建议，并顺利当选 :-)

**Sandipan: 你最喜欢担任指导委员会成员的哪一部分？**

**Ben:** 当我们能直接帮助贡献者的时候。比如，一些长期贡献者会联系委员会，希望获得正式信函，
用于签证申请，说明他们的贡献和价值。能以这种方式直接支持社区成员，是我最喜欢的部分。

**Patrick:** 我最喜欢的是能直接向其他优秀的成员学习，了解项目是如何运作的。

**Maciej:** 和项目一样，最棒的始终是身边的人。正是他们，让我们有机会合作并创造出有趣且令人兴奋的成果。

**Sandipan: 你觉得作为指导委员会成员最具挑战性的地方是什么？**

**Ben:** 我们在可持续性问题上投入了大量时间，但始终没有一个完美答案。很多人都在努力，
但时间和资源有限。虽然我们已把大部分事务委托出去（比如交给 SIG ContribEx 和 K8s Infra），
但我们仍然觉得这些很重要，需要更多关注。平衡这些问题非常困难。

**Paco:** 对我而言，贡献者和维护者的可持续性是最大挑战之一。我一直在呼吁 OSS 用户和雇主参与进来。
社区是开发者互相学习、交流经验和解决问题的场所。
确保每个人都感到被支持和重视，对项目的长期健康发展至关重要。

**Patrick:** 有关项目运作的文档虽然存在，但并不完整。有些部分可能因无法公开、变化太快或需要个案处理而未记录。
幸运的是，我们有任期交叠，可以向有经验的成员学习。同时还有前成员名单，他们也乐于回答问题。

**Maciej:** 最大的挑战是“未知的未知”。即使你做了充分准备，当选后仍会遇到前人没有经历过的新问题。

**Sandipan: 对未来想参选指导委员会的人，你们有什么建议？**

**Ben:** 指导委员会的工作大多是“突发驱动”的……总会突然出现问题需要解决。参选之前请确保自己能投入时间。
同时，也要保持冷静思考，并以同理心倾听社区的声音。

**Paco:** 我很认同前任成员 Clayton 的一句话：我们要确保“每个人的声音都被听到并受到尊重”。
对社区来说，最重要的始终是人。

**Maciej:** 一旦决定参选并当选，请确保每周留出固定时间处理委员会事务。
有时候可能很清闲，有时候又会事务堆积。预留时间能保证你工作的连续性和稳定性。

## 结语

每一个成功的开源项目背后，都有一群默默守护的人，确保项目稳定发展。
Kubernetes 指导委员会正是这样的角色。他们低调高效地工作，面对挑战，支持贡献者，让社区始终保持开放与活力。

他们的特别之处在于专注于“人”——赋能贡献者、解决治理难题，并营造一个创新能够蓬勃发展的环境。
这并不容易，但正如他们所分享的，这是极具价值和回报的。

无论你是长期贡献者，还是正考虑加入的新成员，Kubernetes 社区都欢迎你。
Kubernetes 的核心不仅是技术，更是背后那些推动一切前行的人。
不同的声音与观点始终受到欢迎，共同塑造更加美好的未来。
