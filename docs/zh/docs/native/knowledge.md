# 知识分享

本页分享一些云原生相关的技术文章，愿大家携手共进。

### 排障方案

- [K8s：彻底解决节点本地存储被撑爆的问题](https://mp.weixin.qq.com/s/pKTA6O3bdko_eHaw5mU3gQ)

    K8s 节点本地存储保存了镜像、可写层、日志、emptyDir 等内容。
    除了容器镜像是系统机制控制的，其它都跟应用程序有关。
    完全依赖开发者对应用使用的存储空间进行限制并不可靠，因此，K8s 提供了垃圾回收、日志总量限制、emptyDir 卷限制、临时数据总量限制来避免本地存储不够用的问题。

- [K8s 有损发布问题探究](https://mp.weixin.qq.com/s/jKVw0m5Ho2AtFRScnKEMKw)

    应用发布过程其实是新 Pod 上线和旧 Pod 下线的过程，当流量路由规则的更新与应用 Pod 上下线配合出现问题时，就会出现流量损失。
    总的来说，为了保证流量无损，需要从网关参数和 Pod 生命周期探针和钩子来保证流量路径和 Pod 上下线的默契配合。
    文章从 K8s 的流量路径入手，分析有损发布产生的原因，并给出解决方案。

- [K8s：Pod 的 13 种异常](https://mp.weixin.qq.com/s/cEEdH7npkSHmVHSXLbH6uQ)

    文章总结了 K8s Pod 的 13 种常见异常场景，给出各个场景的常见错误状态，分析其原因和排查思路。

- [K8s: 你需要知道的一切](https://enterprisersproject.com/sites/default/files/2022-11/tep_white-paper_kubernetes-what-you-need-to-know%2Brev2.pdf)

    电子书囊括了了解 Kubernetes 所需的所有定义，同时也包含了与 Kubernetes 相关的其他电子书、文章、教学视频等资源的介绍，以及 7 个最佳实践。

- [Docker Volume 引发 K8s Terminating Pod 的问题](https://mp.weixin.qq.com/s/SMynKYP4obMSl6GQdwDlEw)

    Terminating Pod 是业务容器化后遇到的一个典型问题，诱因不一。
    文章记录了网易数帆-轻舟 Kubernetes 增强技术团队如何一步步排查，发现 Docker Volume 目录过多导致 Terminating Pod 问题的经历，并给出了解决方案。

- [安装 Kubernetes 或升级主机操作系统后出现网络问题？这可能是你的 iptables 版本有问题](https://www.mirantis.com/blog/networking-problems-after-installing-kubernetes-1-25-or-after-upgrading-your-host-os-this-might-be-your-problem)

    安装新版本的 Kubernetes 后，你的工作节点连接不上网络，突然间无法 ssh 访问甚至无法 ping 它们？
    这可能是因为 kube-router 1.25 的 iptables 版本和你安装的版本之间出现冲突。
    归根结底是因为 iptables 1.8.8 和旧版本的规则格式不兼容。
    对此，有三个解决方案：将 iptables 版本降到 1.8.7、清理 IPTables 链所有权（alpha）或是借助轻量级的 Kubernetes 发行版 [k0s](https://github.com/k0sproject/k0s) 解决。

- [利用 eBPF 进行 Kubernetes 集群磁盘 I/O 性能问题排查](https://mp.weixin.qq.com/s/RrTjhSJOviiINsy-DURV2A)

    问题始于 eBay 工程师发现他们的 Kafka 服务在有些时候 follower 追不上 leader 的数据。
    为解决问题，利用了一些 eBPF 工具，例如，[biopattern](https://github.com/iovisor/bcc/blob/master/tools/biopattern.py) 用于展示 disk I/O pattern，[ebpf_exporter](https://github.com/cloudflare/ebpf_exporter) 用于数据收集和可视化。

- [Kubernetes 网络排错骨灰级指南](https://mp.weixin.qq.com/s/mp5coRHPAdx5nIfcCnPFhw)

    文章介绍 Kubernetes 集群中网络排查的思路，包括 Pod 常见网络异常分类、排查工具、排查思路及流程模型、CNI 网络异常排查步骤以及案例学习。

- [Redis 缓存异常及处理方案总结](https://mp.weixin.qq.com/s/P38ETBZJO2lNlE-i7g6HhA)

    Redis在实际应用过程中，会存在缓存雪崩、缓存击穿和缓存穿透等异常情况，如果忽视这些情况可能会带来灾难性的后果，文章对这些缓存异常问题和相应处理方案进行了分析和总结。

- [K8S Internals 系列：存储卷指标消失之谜](https://mp.weixin.qq.com/s/Sd1TY9ml65MQYVSupmvpbw)

    这篇文章的创作灵感因 Grafana 不展示使用存储驱动创建的存储卷的容量指标而起，展示了该问题的排查思路及手段，进而勾勒出 Kubelet 对于存储卷指标收集的实现流程。

### 最佳实践

- [Kubernetes 零信任安全的 mTLS 最佳实践](https://mp.weixin.qq.com/s/QYeP6WZKG0gjJ2u6k1fXxQ)

    文章介绍在 Kubernetes 中实现双向 TLS（mTLS）的三大最佳实践，
    包括不要使用自签名证书、将 Istio 的信任根植于现有的公钥基础设施 (PKI) 中、使用中间证书。

- [微服务应用视角解读如何选择 K8s 的弹性策略](https://mp.weixin.qq.com/s/jfpF3WUs4YvtlJ8Q4zsuxg)

    对于集群资源弹性，K8s 社区给出了 Cluster Autoscaler（CA）和Virtual Kubelet（VK）两种解决方案。
    文章围绕微服务应用的形态与特点，剖析了 CA 与 VK 各自适用的场景，并总结了微服务架构下应用该如何选择集群资源弹性。

- [GitOps 软件交付 pipeline 的组件介绍](https://www.weave.works/blog/infographic-gitops-pipeline)

    文章总结了开始使用 GitOps 所需的组件，包括容器平台、Git 仓库、容器镜像仓库、GitOps 代理和构建服务器。
    以及在扩大规模时可以增加的一些组件，如容器配置自动化、策略引擎、服务网格、渐进式交付工具、事件监控等。

- [万字解读，如何从 0 到 1 构建 K8s 容器平台的 Nginx 负载均衡体系](https://mp.weixin.qq.com/s/Q1DXAEL4ceUcUCQjHAIU5Q)

    文章介绍了从 0 到 1 来构建大规模 Kubernetes 容器平台的 Nginx 负载均衡体系的实战经验，
    包括体系的业务需求和运维需求、对 Nginx-Controller 组件的要求、架构设计、体验优化、核心考量点。

- [如何管理云原生应用程序的依赖关系](https://mp.weixin.qq.com/s/SipnQhbaa7WlpwORTVLCRw)

    文章介绍了一些云原生应用依赖关系管理的最佳实践，例如，使用 depcheck 来检查未使用的依赖关系，使用依赖关系检查脚本检测过期的依赖关系，
    以及利用自动化依赖关系管理开源工具 [Mend Renovate](https://github.com/marketplace/renovate) 为所有类型的依赖关系更新自动创建拉取请求。

- [K8s：利用 Mutating Admission Controller 简化应用的环境迁移](https://blog.getambassador.io/using-mutating-admission-controllers-to-ease-kubernetes-migrations-5699c1901015)
  
    Kubernetes 的 Mutating Admission Webhook 通常用于执行安全实践，确保资源遵循特定的策略或配置管理。
    文章介绍了一个新的用例：简化应用的迁移，实现快速更新新环境的清单，同时保持旧环境正常运行。

- [阿里云容器攻防矩阵 & API 安全生命周期，如何构建金融安全云原生平台](https://mp.weixin.qq.com/s/ZKsIn0UzrrSGWWMv8Sk4Nw)

    文章从攻击者视角介绍了容器平台（容器攻防矩阵）和 API 在金融科技领域的应用所带来的威胁面，分析威胁，并给出容器平台和 API 全生命周期的安全防护实践建议。

- [全球顶级开源公司是如何找到前 1000 名社区用户的？](https://mp.weixin.qq.com/s/edy6FsD1d_9fp-U60H_dug)

    文章分享了 4 个顶级开源商业公司（HashiCorp、Confluent、Databricks 和 CockroachDB）的开源项目和开源社区的运作方式，如何找到前 1000 名社区用户及花了多长时间，以及增长衡量指标等。

- [容器云多集群环境下如何实践 DevOps](https://mp.weixin.qq.com/s/MW67DhLzUWXm0xHd5LH0Tw)

    文章介绍了如何通过 GitOps 来实现多集群 DevOps，并推荐了一种多集群 GitOps 工作流作为落地参考，最后介绍了在持续集成和持续交付中具体实践 GitOps 的主流方式。

- [Kubernetes HPA 的三个误区与避坑指南](https://mp.weixin.qq.com/s/3eSm0BZSrPUAZQQhG_L_5A)

    Kubernetes 提供了水平弹性扩容能力（HPA），让应用可以随着实时指标进行扩/缩。
    然而 HPA 的实际工作情况可能和我们预想的不一样，这里存在一些认知误区，例如，HPA 存在扩容死区、扩容与预期使用量不符、弹性行为总是滞后等。
    对此，文章总结了一些注意事项，帮助在使用 HPA 时“有效避坑。

- [是时候思考 K8s 出向流量安全了（上）](https://mp.weixin.qq.com/s/Lj3sl-Ukday9WP4U-8-vqA)[&（下）](https://mp.weixin.qq.com/s/NMh1XbBXeyfGuJJ8kZ6J2Q)

    我们往往重视 Ingress 的能力，而忽视了 Egress 流量的安全管控。但无论从安全还是合规的角度，Egress 流量都应加强管控。
    文章分析了进行 Egress 流量策略管控的原因、存在的挑战以及业界方案分析。方案包括六大类：基于 K8s Network Policy、CNI、Service Mesh、微分段技术以及 DNS interception。

- [如何保障云原生集群安全](https://mp.weixin.qq.com/s/sv40SzD7Ic1eMeElvccs7A)

    文章为容器集群安全交流论坛的内容汇总。
    内容包括：云集群安全的分类以及预防及解决方案、容器云上集群划分原则、集群审计、节点安全保障、etcd 集群安全、设计网络策略保障集群资源的安全、网络隔离问题、按照安全等保级别针对 k8s 集群的标准化策略或配置等。

- [Kubernetes 控制平面应该有多少个节点](https://thenewstack.io/how-many-nodes-for-your-kubernetes-control-plane/)

    文章为确定 Kubernetes 控制平面的大小提供了参考。对于大多数用例，3 个节点足以。
    5 个节点将提供更好的可用性，但在所需节点数量和硬件资源消耗方面成本更高。
    此外，监控、备份 etcd 和控制平面节点配置是解决节点故障、预防意外的最佳实践方案。

- [利用 Istio 减少跨可用区流量开销](https://www.tetrate.io/blog/minimizing-cross-zone-traffic-charges-with-istio/)

    跨可用区部署 Kubernetes 集群具备显著的可靠性优势，但需要一些额外的配置在本地保持流量。
    Istio 的本地感知路由可以帮助减少延迟，并将云供应商对应用流量的跨区数据收费降到最低。

- [2 分钟测试 Kubernetes Pod 的安全](https://dzone.com/articles/the-2-minute-test-for-kubernetes-pod-security)

    从集群外部运行 [Kyverno CLI](https://github.com/kyverno/kyverno)，审计集群是否符合最新的 [Kubernetes Pod 安全标准](https://kubernetes.io/docs/concepts/security/pod-security-standards/)的要求，并为 pod 安全标准中定义的每个控制执行策略。执行审计不需要在集群中安装任何东西。

- [Proxyless Mesh 在 Dubbo 中的实践](https://mp.weixin.qq.com/s/TH8waHN00y6q26NUDY9wzg)

    [Dubbo Proxyless Mesh](https://github.com/apache/dubbo-awesome/blob/master/proposals/D3.2-proxyless-mesh.md) 直接实现 xDS 协议解析，实现 Dubbo 与 Control Plane 的直接通信，进而实现控制面对流量管控、服务治理、可观测性、安全等的统一管控，规避 Sidecar 模式带来的性能损耗与部署架构复杂性。

- [零信任策略下 K8s 安全监控最佳实践](https://mp.weixin.qq.com/s/wYUNsGaWEnQZ0BVxsQORbA)

    文章介绍如何在分布式容器化环境中借助 K8s 相关的安全数据源及采集技术，监控 K8s 集群，及时发现异常 API 访问事件、异常流量、异常配置、异常日志等行为，并且结合合理的告警策略建立更主动的安全防御体系。

- [基于 DevOps 流程的容器安全最佳实践](https://mp.weixin.qq.com/s/y42BgaosyIQnA1uDEgqTPA)

    文章分享了青藤云安全总结得出的适用于 DevOps 工作流程的 14 个容器安全实践，包括防御阶段的 6 个安全左移步骤、保护阶段的安全运行容器、检测阶段的异常行为告警以及响应阶段的事件响应与取证。

- [如何设计内部开发平台的 “Golden Path”](https://cloud.redhat.com/blog/designing-golden-paths)

    “Golden Path”是指构建和部署某个软件的预架构方法。
    这种方法基于最佳实践的沉淀，能够加速典型应用的开发效率，是成功搭建内部开发平台（IDP）的先决条件。
    文章介绍了“Golden Path”应该具备的特点以及一个简单相关成熟度模型，并展示了一个如何实施“Golden Path”的例子。

- [通过云原生的方式管理 GPU 资源](https://mp.weixin.qq.com/s/W-Ntu2xdjypFgs5EPMVjkg)

    文章介绍了如何使用云原生的方式管理GPU资源，包括统一 GPU 资源和框架，以及通过 qGPU 共享方式提高 GPU 使用率，降低了集群层面 GPU 资源的管理难度。

- [微服务全链路灰度新能力](https://mp.weixin.qq.com/s/JL7Ru4nIiP2XuXwNiw2TtA)

    文章主要介绍阿里云 MSE 服务治理基于全链路灰度能力的应用场景与痛点延伸出来的两个新能力：运行时白屏化和配置灰度。
    运行时白屏化用于洞察全链路灰度的流量匹配以及运行的行为；配置灰度是指微服务应用中的配置项应该具备的灰度能力，以应对灰度应用对特殊配置值的诉求。

- [Kubernetes 集群利用率提升实践](https://mp.weixin.qq.com/s/IAo41AZ0aAkIxY-JzonXMQ)

    文章分享了 Kubernetes 集群利用率提升的思路和实现方式，包括两级扩容机制、两级动态超卖、动态调度、动态驱逐。

- [NGINX 现代应用参考架构（MARA）的 OpenTelemetry 集成进展报告](https://mp.weixin.qq.com/s/j1dknNrFz0XqXSB2-Cwc3g)

    [MARA](https://github.com/nginxinc/kic-reference-architectures) 是可用于在 Kubernetes 环境中构建和部署现代应用的生产就绪代码。
    文章描述了 MARA 对多功能开源可观测性工具的需求，然后介绍了选择 OpenTelemetry 过程中的利弊权衡和设计决策，
    以及采用了哪些技术将 OpenTelemetry 与使用 Python、Java 和 NGINX 构建的微服务应用相集成。

- [Istio 外部控制面部署实践](https://mp.weixin.qq.com/s/TaQWryqD5AwWMJOXbejaqg)

    通过对外部 Istiod 部署模型进行调研与部署，作者对其架构进行了剖析并对其使用的部署 yaml 文件部分进行了解析，总结了在部署过程中可能会遇到一些问题。

- [监控 Cilium 的关键指标](https://www.datadoghq.com/blog/cilium-metrics-and-architecture/)

    文章介绍了监控 Cilium 的关键指标：端点的健康状况、Kubernetes 网络状态、网络策略的有效性、Cilium 的 API 处理和速率限制的性能。

- [基于服务网格的云原生安全分层方法](https://www.tetrate.io/blog/lateral-movement-and-the-service-mesh/)

    文章主要探讨如何利用服务网格优化 OSI 模型各层的现有安全工具和实践。
    服务网格很适合作为最接近应用的一层，位于（并隐藏）底层安全层之上，为服务提供传输加密、应用身份和应用层访问控制。

- [Observability：采样 Sampling 场景和落地案例（上篇）](https://mp.weixin.qq.com/s/tnYUOHJT0TOh4iYBHlP4aA)

    文章先后介绍了采样的使用场景、采样在调用链系统架构的位置、主要方案（头部连贯采样、单元采样和尾部连贯采样）、主流开源和商业系统的采样实现、落地案例等。

- [Observability 之采样 sampling 场景和落地案例（下篇）](https://mp.weixin.qq.com/s/nxnz37VJydNHFMaEywu9KA)

    作者围绕一些落地案例，分享了一些关于可观测系统采样设计的思考。
    先分析全量采样的必要性、适合全量采样的链路，然后分享了阿里鹰眼和字节跳动等业内完整采样方案以及 OpenTelemetry 生产环境采样案例。

- [如何扩展 K8s Descheduler 策略](https://mp.weixin.qq.com/s/pkDxexvrzmtuLMWwzi0p_g)

    社区 Descheduler 的功能远不能满足公司内部生产环境的需要。
    文章介绍了 LowNodeUtilization 和 HighNodeUtilization 策略的扩展。
    在使用 Descheduler 迁移 Pod 时还需要对业务的稳定性做一些保障措施，完善组件功能后还需要对服务自身进行效果评估。

- [Kubernetes 资源拓扑感知调度优化](https://mp.weixin.qq.com/s/CgW1zqfQBdUQo8qDtV-57Q)

    文章首先介绍了腾讯星辰算力的业务场景与精细化调度相关的知识，然后对 K8s 和 Volcano 社区进行调研，发现目前已有的方案都存在局限性。
    最后通过痛点问题分析给出相应的解决方案。
    优化后，原有测试任务的训练速度提升至原来的 3 倍，CPU 抢占的驱逐率大大降低至物理机水平。

- [如何正确配置 RBAC 防止容器逃逸](https://mp.weixin.qq.com/s/tV3HOaE3TzJ6EbuEmYYfdA)

    文章介绍了在集群内利用危险的 RBAC 配置进行权限提升的思路，以此说明在容器逃逸后权限配置不当的影响。

- [如何优化 Prometheus 查询性能](https://thenewstack.io/query-optimization-in-the-prometheus-world/)

    使用 Prometheus 时常会遇到的一个问题是：随着收集的指标数据量的增加，查询性能下降。
    文章介绍了影响 Prometheus 查询性能的因素、Prometheus 提供的可识别缓慢/低效查询的选项以及优化查询性能的方法（如缩短查询时间范围、降低指标分辨率等）。

- [vivo 容器集群监控系统架构与实践](https://mp.weixin.qq.com/s/SBZO48fWcEojlDlBROdogQ)

    文章以 vivo 容器集群监控实践经验为基础，探讨了云原生监控体系架构如何构建，从监控高可用和数据转发层组件高可用两个方面介绍 vivo 容器集群监控架构的设计思路，最后总结了在实践过程中遇到的挑战和对策。

- [混合云的多活架构指南](https://mp.weixin.qq.com/s/NXXwjxUAGXDD3krKXyJbaQ)

    文章介绍了作业帮公司在混合云环境下的多活架构：多云间的网络是介于单云多可用区和中心-边缘之间的一种状态；
    常态的应用间调用闭环在单云内部，仅需要单云内部独立注册发现；
    某些场景下的跨云调用只需要集群间发现即可；
    多云部署了全量服务，南北向流量就可以优先通过 DNS 进行调度。

- [2022 年，如何安全加固 Kubernetes?](https://elastisys.com/nsa-cisa-kubernetes-security-hardening-guide-and-beyond-for-2022/)

    文章作者认为，美国国家安全局去年发布的[《Kubernetes 加固指南》](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)的摘要和后面主体内容存在很大差距。
    为此，作者在总结该报告的基础上，提出了一些配置、应用任意许可、镜像扫描、安全测试等相关的额外见解。

- [混沌工程在微服务场景下的应用](https://mp.weixin.qq.com/s/dEA3g3JnAKloW6K7cUskYQ)

    杭州每刻科技引入云原生混沌工程测试平台 Chaos Mesh ，以解决云财务场景下微服务健壮性测试过程中遇到的痛点。

- [百度云原生混部大规模落地实践之路](https://mp.weixin.qq.com/s/OgU2uRGhIy7r6WucvdrPzg)

    混部技术，即将在线业务和离线任务混合部署到相同物理资源上，通过资源隔离、调度等控制手段，充分使用资源，同时保证服务的稳定性。
    百度云原生混部系统主要分为三个部分：单机管理层、调度层、运营层。
    单机层提供提供资源质量管理、内核级别的 QoS 隔离、资源视图上报和策略执行、eBPF 细粒度指标采集能力；
    调度层负责资动态源视图的感知和提供最佳调度策略；
    运营层提供资源画像、资源运营、水位设置、热点治理等功能。

- [确保 Kubernetes 安全合规的 6 个最佳实践](https://mp.weixin.qq.com/s/MQh16-PQYsjaGCjwyxIk_A)

    文章介绍了，确保在容器化环境中持续合规而不影响生产力，应遵循的 6 个实践：
    实现自动化、对 Kubernetes 本身进行保护、事先发现攻击、专注于零信任、利用 Kubernetes 内置安全措施验证云主机的安全性。

- [如何使用 Istio 授权策略执行 egress 流量](https://www.tetrate.io/blog/istio-how-to-enforce-egress-traffic-using-istios-authorization-policies/)

    文章以“服务网格内两个独立命名空间中的睡眠服务访问谷歌和雅虎的外部服务”为例，介绍了在执行 ingress 策略时，如何使用 Istio 的 Egress 网关以相似策略执行 egress 授权策略。

- [解决微服务架构下流量有损问题的实践和探索](https://mp.weixin.qq.com/s/eQzy3zvvEokNXYL637LNCg)

    尽管可灰度、可观测和可滚回的安全生产三板斧可以最大限度的规避发布过程中由于应用自身代码问题对用户造成的影响，但对于高并发大流量情况下的短时间流量有损问题却仍然无法解决。
    因此，文章围绕发布过程中如何解决流量有损问题、实现应用发布过程中的无损上下线效果相关内容展开方案介绍。

- [阿里巴巴的 Envoy Gateway 实践](https://mp.weixin.qq.com/s/t1ppAQfm0cPmqhxEARB03Q)

    文章简单介绍了阿里巴巴探索下一代网关的历程：Envoy Gateway 1.0（孵化期）主要应用于东西向流量的 RPC 互通；
    2.0（成长期）采用 Tengine + Envoy 两层网关，承担南北向网关流量；
    3.0（成熟期）通过 Envoy 将流量网关 + 微服务网关合二为一，辅以硬件加速、内核调优等手段。

- [阿里云发布《云原生实战案例集》](https://developer.aliyun.com/ebook/read/7575?spm=a2c6h.26392459.ebook-detail.4.17f14848W6TyWT)

    阿里云发布《云原生实战案例集》，通过技术瞭望、行业分析、实战案例解读为企业实践和落地云原生提供一定参考和借鉴。

- [阿里云发布企业云原生 IT 成本治理方案：五大能力加速企业 FinOps 进程](https://mp.weixin.qq.com/s/hAHNlAi8c0OAO7zSq31J1w)

    企业云原生 IT 成本治理存在业务单元与计费单元生命周期不匹配、动态资源交付与静态容量规划矛盾、企业 IT 成本治理模型与云原生架构适配等问题。
    由此，阿里云容器服务推出了企业云原生 IT 成本治理方案，提供企业 IT 成本管理、成本可视化、成本优化等功能。

- [2022 年值得关注的 DevOps 趋势和最佳实践](https://technostacks.com/blog/devops-trends)

    这篇文章介绍了 2022 年值得关注的 DevOps 趋势，其中包括微服务架构、DevSecOps 的应用、朝着完全无服务器的方向发展、弹性测试成为主流、GitOps 成为新常态以及发展混沌工程等。

- [分布式定时任务调度框架实践](https://mp.weixin.qq.com/s/9gBY_QHyBrzSoMlBG83zug)

    这篇文章介绍了任务调度框架使用的需求背景和痛点，对业界普遍使用的开源调度框架进行了探究实践，并分析了各自的优劣势。

- [拆分单独应用三问: What, When, How](https://dzone.com/articles/split-the-monolith-what-when-how)

    在微服务架构设计中，如何拆分单体是一件非常重要但令架构师十分头疼的事。这篇文章介绍了一些关于如何准备和执行单体应用程序拆分的思路和操作步骤。

- [K8s 安全策略最佳实践](https://mp.weixin.qq.com/s/ZDqchROixZT4enVYH6UIfw)

    文章开篇对K8s环境面临的安全风险及K8s提供的安全机制进行了介绍。此外，作者根据社区和自身团队的生产实践，总结了改善K8s安全状况的最佳实践。

- [Prometheus 监控 Harbor 实战](https://blog.51cto.com/u_15331726/5177735)

    Harbor v2.2及其更高版本支持对相关指标的采集和使用，这篇文章介绍了如何使用 Prometheus 轻松抓取 Harbor 实例的一些关键指标。

### 工具推荐

- [为什么我们提倡以工作负载为中心而非基础设施为中心的开发模式？](https://score.dev/blog/workload-centric-over-infrastructure-centric-development)

    云原生开发人员经常被环境间的配置不一致所困扰。
    [Score](https://github.com/score-spec/spec) 是一个开源项目，提供了一个以开发者为中心、与平台无关的工作负载规范，
    能够声明式地描述其运行时的要求，消除了本地和远程环境之间的配置不一致性，提高开发者的生产力。

- [用 Bindle 轻松存储和分发云原生应用](https://mp.weixin.qq.com/s/gGp_CneC8BzU3GKOKIfbWA)

    [Bindle](https://github.com/deislabs/bindle) 是一个开源的包管理器，通常用于存储和分发 WebAssembly 应用和二进制文件。
    Bindle 可以将多个不同的微服务打包在一个大应用程序中，并将其部署在任何需要的地方，也可以存储包含数十个不同二进制文件的应用程序。

- [Kubernetes 跨集群流量调度实战](https://mp.weixin.qq.com/s/RF--gLZtJlT0ijaPp1ZP7A)

    文章演示了 Kubernetes 南北向流量管理方案 [FSM](https://github.com/flomesh-io/fsm) 是如何实现服务的跨集群流量调度和负载均衡的，以及三种不同的全局流量策略的实现：仅本集群调度、故障转移、全局负载均衡。

- [ChaosBlade：大规模 Kubernetes 集群故障注入的利器](https://mp.weixin.qq.com/s/gh4GVnOY_QVU2D2VeyWCeA)

    [ChaosBlade](https://github.com/chaosblade-io/chaosblade) 是一款遵循混沌工程原理和混沌实验模型的实验注入工具，帮助企业提升分布式系统的容错能力，并且为企业在上云或往云原生迁移过程中提供业务连续性保障。
    文章主要介绍 ChaosBlade 在 Kubernetes 中故障注入的底层实现原理、版本优化过程以及大规模应用演练测试。

- [OpenFeature 和 Feature Flag 标准化如何造就高质量的持续交付](https://www.dynatrace.com/news/blog/openfeature-and-feature-flag-standardization/)

    Feature Flag 即功能开关或功能发布控制，是一种通过配置开关功能特性的技术，无需重新部署代码。
    而 [OpenFeature](https://github.com/open-feature)，是一个关于 Feature Flag 的开放标准，旨在使用云原生技术构建一个强大的 Feature Flag 生态系统，允许团队灵活地选择符合当前需求的 feature flag 方法，并在需求发生变化时切换到其他方法。

- [Traffic Director: 在 GKE 上 使用 Envoy gateway 代理实现 TLS 路由](https://cloud.google.com/blog/products/networking/tls-routing-using-envoy-gateway-proxy-on-gke)

    Traffic Director 是谷歌托管的服务网格控制平面，用于解决微服务流量的治理问题。
    文章分享了一个架构样本，在 GKE 集群上，使用 Traffic Director 配置 Envoy gateway 代理，使用 TLS 路由规则，将集群外的客户端流量路由到部署在集群上的工作负载。
    此外，演示了如何利用 Envoy 代理作为入口网关，使南北流量进入服务网格，以及使用[服务路由 API](https://cloud.google.com/traffic-director/docs/service-routing-overview#:~:text=The%20service%20routing%20APIs%20let,two%20HTTPRoute%20resources%20configure%20routing.) 来路由这些流量，最后还分享了一些故障排除技巧。

- [Quarkus 的 Java 框架如何用于 serverless function 开发？](https://mp.weixin.qq.com/s/oeJjQtqK8h2JSGy4wOlQ6w)

    [Quarkus](https://github.com/quarkusio/quarkus) 解决了传统框架内存消耗大和容器环境的扩展问题。
    通过 Quarkus，开发人员可以使用熟悉的技术构建云原生微服务和 serverless function。
    文章介绍如何开始使用 Quarkus 进行 serverless function 开发、如何优化 function 并实现持续测试，以及制作跨 serverless 平台的可移植 function 等。

- [GitLab + Jenkins + Harbor 工具链快速落地指南](https://mp.weixin.qq.com/s/fA38H5up9VqZ3zEBy1eXnA)

    文章介绍了如何利用 DevOps 工具链管理器 [DevStream](https://github.com/devstream-io/devstream) 快速部署 DevOps 工具链（GitLab + Jenkins + Harbor）。

- [Helm 部署高可用 Harbor 镜像仓库](https://mp.weixin.qq.com/s/ev_QE9NhwiCcLHpapbAU7A)

    文章介绍如何使用 Helm 包管理工具将 harbor 部署在 kubernetes 集群中并且实现高可用。

- [微软 Azure 在容器供应链安全的开源实践](https://mp.weixin.qq.com/s/bXt-pPID4CyDyp0XEmDyZQ)

    文章主要介绍 Azure 在容器供应链安全领域的开源实践，
    例如：[Microsoft/SBOM Tool](https://github.com/microsoft/sbom-tool) 生成 SBOM 文件，[Notary v2](https://github.com/notaryproject/notation) 对容器镜像等软件制品进行签名和验证，[ORAS](https://github.com/oras-project/oras) 扩展 OCI 赋能供应链安全，[Ratify](https://github.com/deislabs/ratify) 帮助 Kubernetes 验证应用的部署安全。

- [vcluster -- 基于虚拟集群的多租户方案](https://mp.weixin.qq.com/s/831cv8ONpzcJ3FJeyQ3sxQ)

    虚拟集群即 vcluster 是在常规的 Kubernetes 集群之上运行的一个功能齐全、轻量级、隔离性良好的 Kubernetes 集群。
    其核心思想是提供运行在“真实”集群之上隔离的 Kubernetes 控制平面（例如 API Server）。
    与完全独立的“真实“集群相比，虚拟集群没有自己的工作节点或者网络，工作负载实际上还是在底层宿主集群上调度。

- [5个实用工具，提升 Kubernetes 生产力](https://mp.weixin.qq.com/s/KAg48nzlsL2jxm0sUDo3mw)

    文章列出了五种与 Kubernetes 一起工作的强大工具，
    分别是终端 UI [K9s](https://github.com/derailed/k9s)、清理 Kubernetes 集群的工具 [Popeye](https://github.com/derailed/popeye)、Kubernetes 集群部署检查工具  [Kube-bench](https://github.com/aquasecurity/kube-bench)、上下文和命名空间快速切换工具 [Kubectx](https://github.com/ahmetb/kubectx)、[Kubens](https://github.com/ahmetb/kubectx) 和 [fzf](https://github.com/junegunn/fzf)、日志聚合器 [Stern](https://github.com/stern/stern)、从 shell 快速检查文件 [Bat](https://github.com/sharkdp/bat)。

- [利用 Open Cluster Management（OCM） 的 Placement 扩展多集群调度能力](https://cloud.redhat.com/blog/extending-the-multicluster-scheduling-capabilities-with-open-cluster-management-placement)

    在 K8s 多集群管理项目 OCM 中，多集群调度能力由 [Placement](https://github.com/open-cluster-management-io/placement) 控制器提供。
    Placement 提供了一些默认的优先级排序器，用于分类和选择最合适的集群。在某些情况下，排序器需要更多的数据来计算集群的得分。
    因而，我们需要一种可扩展的方式来支持基于自定义得分的调度。

- [开源云原生安全治理平台 HummerRisk](https://mp.weixin.qq.com/s/00cER0lVP2u40GROPP_ZbA)

    [HummerRisk](https://github.com/HummerRisk/HummerRisk) 是一个开源的云安全治理平台，以非侵入的方式对云原生环境进行全面安全检测，核心解决三个方面的问题，底层的混合云安全合规，中层的 K8s 容器云安全和上层的软件安全。

- [使用 Config Sync 以 GitOps 的方式部署 OCI 工件和 Helm charts](https://cloud.google.com/blog/products/containers-kubernetes/gitops-with-oci-artifacts-and-config-sync)

    [Config Sync](https://github.com/GoogleContainerTools/kpt-config-sync) 是一个开源工具，为 Kubernetes 集群提供 GitOps 持续交付。
    它能够通过 GitOps 的方式来存储和部署 Kubernetes 清单，把 Kubernetes 清单打包成一个容器镜像，并且使用与容器镜像相同的认证和授权机制。

- [突破 Kubernetes 对自定义资源数量的限制](https://mp.weixin.qq.com/s/LV83vuMZ641HzL7bKUE05g)

    Crossplane 社区发现了 Kubernetes 能够处理的 CRD 上限，并且帮助解决了这些问题。
    其中，限制原因包括：限制性的客户端速率限制器、缓慢的客户端缓存、低效的 OpenAPI 模式计算、冗余高昂的成本、etcd 客户端。

- [K8s DevOps 平台 TAP 基于 Knative 的云原生运行时](https://mp.weixin.qq.com/s/kvUDvEVaNC3qordCtaMosw)

    TAP 的云原生应用运行时抽象层（CNR）的核心是 Knative。
    TAP 提供了一个 Runtime 运行时层，既支持用户使用 K8S Deployment 和 Service,也可以使用 Knative Serving, Scale From/To Zero,Eventing 和 Streaming 等。

- [使用 Tekton 和 Kyverno 的基于策略的方法来保障 CI/CD 管道的安全](https://www.cncf.io/blog/2022/09/14/protect-the-pipe-secure-ci-cd-pipelines-with-a-policy-based-approach-using-tekton-and-kyverno/)

    [Tekton](https://github.com/tektoncd/pipeline) 提供了一个强大的 CI/CD 框架，并且通过 Tekton Chains 等扩展确保构建工件的安全。
    [Kyverno](https://github.com/kyverno/kyverno) 可用于管理策略，实现基于命名空间的隔离，并为 Tekton 管道生成安全资源。
    此外，还可以签署 OCI 工件，如 Tekton 捆绑物。Tekton 和 Kyverno 的强大组合使软件构建和交付系统的安全和自动化达到了新的水平。

- [K8S 运维开发调试神器 Telepresence 实践指南](https://mp.weixin.qq.com/s/Yu5z9w26rqgVHkEYhg1t2g)

    [Telepresence](https://github.com/telepresenceio/telepresence) 可用于在本地运行单个服务，同时将该服务连接到远程 Kubernetes 集群。
    Telepresence 提供了 3 个非常重要的功能：cluster 域名解析、cluster 流量代理和 cluster 流量拦截。

- [使用 Containerlab + kind 快速部署 Cilium BGP 环境](https://mp.weixin.qq.com/s/FBkln02REVMByhdzaZhj7w)

    kind 提供快速部署 K8s 能力，[Containerlab](https://github.com/srl-labs/containerlab) 提供快速部署网络资源能力，二者结合可达到秒速部署跨网络 K8s 集群，可用于快速部署和销毁 Cilium BGP 环境。

- [可观测下一站：基于 Trace 的测试](https://thenewstack.io/trace-based-testing-the-next-step-in-observability/)

    可观测性工具收集的分布式追踪数据是集成测试的理想选择。
    基于 trace 的测试能够准确地指定要测试的事务，观测系统行为的结果，验证组件之间的依赖关系，主动测试潜在的问题。
    [Tracetest](https://github.com/kubeshop/tracetest) 是一个基于 trace 的测试工具，它利用 Opentelemetry 分布式追踪所捕获的数据，来生成强大的集成测试。

- [RunD：高密高并发的轻量级 Serverless 安全容器运行时](https://mp.weixin.qq.com/s/fgBKqIeuGt2tLcQaYuuyfg)

    RunD 通过全栈的 host-to-guest 解决方案，解决了跨容器的重复数据、每个虚拟机的高内存占用和 host 端 cgroup 的高开销问题，提供高密度部署和高并发能力的支持。
    使用 RunD 运行时，可以做到在一秒内启动超过 200 个安全容器，并且可以在一个 384GB 内存的节点上部署超过 2500 个安全容器。

- [在 Kubernetes 中实施零信任的难点及相关开源解决方案](https://thenewstack.io/introducing-open-source-zero-trust-to-kubernetes/)

    Kubernetes 的复杂性使得标准化应用零信任原则成为挑战。默认情况下，kubectl 不启用 RBAC，执行的命令不会被用户账户记录。通过防火墙访问资源很困难，监督多个集群也变得繁杂易错。
    [Paralus](https://github.com/paralus/paralus) 是为多集群环境设计的资源访问管理、威胁识别响应方案，支持自定义角色、身份提供商（IdP）等，允许管理员创建具有不同权限的自定义规则。

- [Kubernetes Gateway API 及其用例介绍](https://www.armosec.io/blog/kubernetes-gateway-api/)

    文章介绍了 Gateway API 与 Ingress 的区别及其用例。Gateway API 是 Ingress 的演变，它通过扩展 API 定义来提供一些高级的功能，如 HTTP 和 TCP 路由、流量拆分、跨命名空间路由以及集成渐进式交付工具等。

- [如何进行 K8s 集群基准测试——Kube-burner 对 KubeVirt CRD 的扩展支持介绍](https://cloud.redhat.com/blog/introducing-kubevirts-crd-support-for-kube-burner-to-benchmark-kubernetes-and-openshift-creation-of-vms)

    [Kube-burner](https://github.com/cloud-bulldozer/kube-burner)一个通过创建或删除大量对象进行 Kubernetes 集群压测的工具。
    kube-burner 在默认情况下不支持第三方插件，如 KubeVirt CRD。
    因此，Openshift 对 kube-burner 进行扩展以支持 KubeVirt CRD，通过创建/删除虚拟机实现集群基准测试。

- [在 Argo CD 中使用 Sops 增强 GitOps 安全性](https://mp.weixin.qq.com/s/GboGFpdAfF1SL150VSRn8Q)

    [Sops](https://github.com/mozilla/sops) 是一款加密文件的编辑器，支持 YAML、JSON、ENV 等格式，同时可以用 AWS KMS、GCP KMS、age 和 PGP 等进行加密。
    Argo CD 可以与 Sops 集成，对私密信息进行加解密。

- [如何使用 KubeClarity 检测和管理软件物料清单以及容器镜像和文件系统漏洞](https://mp.weixin.qq.com/s/mw948wYKmTWt-Mxv4nxHRA)

    [KubeClarity](https://github.com/openclarity/kubeclarity) 是一款专门用于检测和管理软件物料清单以及容器镜像和文件系统漏洞的工具，可以扫描运行时 K8s 集群和 CI/CD 管道，以增强软件供应链的安全性。

- [如何针对 Helm 做金丝雀发布？](https://mp.weixin.qq.com/s/frOOSffcCknS_YAjQChuNg)

    Helm 本身在设计时并不考虑灰度发布、也不针对工作负载做管理。
    通过 [KubeVela 的插件机制](https://github.com/kubevela/catalog/tree/master/addons)联合 fluxcd addon 和 kruise-rollout addon，无需对 Helm Chart 做任何改动，就可轻松完成 Helm 应用的金丝雀发布。

- [使用 Nocalhost 开发 Rainbond 上的微服务应用](https://mp.weixin.qq.com/s/kC9P7fvMtJvKK7_TM2LbTw)

    [Nocalhost](https://github.com/nocalhost/nocalhost) 是基于 IDE 的云原生应用开发工具，[Rainbond](https://github.com/goodrain/rainbond) 是一款云原生多云应用管理平台。
    Nocalhost 可以直接在 Kubernetes 中开发应用，Rainbond 可以快速部署微服务项目，无需编写 Yaml，Nocalhost 结合 Rainbond 加速微服务开发效率。

- [两个 OCI 镜像构建工具介绍 builders—— melange 和 apko](https://blog.chainguard.dev/secure-your-software-factory-with-melange-and-apko/)

    [apk](https://github.com/alpinelinux/apk-tools) 直接使用 Alpine 的包管理工具 APK 来构建镜像，不需要使用 Dockerfile，只需要提供声明式 YAML 清单。
    [melange](https://github.com/chainguard-dev/melange) 使用声明式 YAML 管道来构建 APK。

- [多集群场景下基于 Flux v2 的应用持续交付实践](https://mp.weixin.qq.com/s/a9lRoa36tFl1_1-ESvXJpA)

    [Flux v2](https://github.com/fluxcd/flux2) 提供了一组可支持实现 GitOps 的工具，面向云原生应用持续交付提供了通用的解决方案。
    文章主要从多集群场景下部署差异化配置的云原生应用出发，介绍了基于 Flux v2 的应用持续交付实践。

- [使用 Chain-bench 审计你的软件供应链是否符合 CIS 的要求](https://blog.aquasec.com/cis-software-supply-chain-compliance)

    互联网安全中心（CIS）最近发布了[《软件供应链安全指南》](https://github.com/aquasecurity/chain-bench/blob/main/docs/CIS-Software-Supply-Chain-Security-Guide-v1.0.pdf)，提供保护软件交付管道的最佳实践。
    作为指南的发起者和主要贡献者，Aqua 团队开发了首个软件供应链审计开源工具—— [Chain-bench](https://github.com/aquasecurity/chain-bench)，用以审计软件供应链是否符合 CIS 的基准，并实现审计过程自动化。

- [Chainguard 版本的 下一代 Distroless 镜像](https://blog.chainguard.dev/minimal-container-images-towards-a-more-secure-future/)

    Chainguard 正在构建下一代 [distroless](https://github.com/distroless) 镜像，使用一个工具链即可轻松地从现有的软件包中组成 distroless 镜像，并创建自定义软件包。
    与谷歌的 Bazel 和基于 Debian 的系统不同的是，Chainguard 工具链以 [apk](https://github.com/alpinelinux/apk-tools)（Alpine 软件包管理器）、[apko](https://github.com/chainguard-dev/apko)（用来构建基于 Alpine 的 distroless 镜像） 和 [melange](https://github.com/chainguard-dev/melange)（使用声明式 pipeline 构建 apk 包）为核心，减少 distroless 镜像的复杂性。

- [通过 MetalLB 在 OpenYurt 边缘侧实现对 LoadBalancer类型 service 的支持](https://openyurt.io/zh/blog/Enable-MetalLB-in-OpenYurt/)

    在云边协同场景下，由于边缘侧并不具备云端 SLB 服务的能力，边缘 Ingress 或边缘应用无法暴露 LoadBalancer 类型的服务供集群外访问。
    文章对此场景，探讨如何通过 MetalLB 在OpenYurt 边缘侧实现对 LoadBalancer 类型 service 的支持。

- [在 Kubernetes 中实施热重载应用](https://loft.sh/blog/implementing-hot-reloading-in-kubernetes/?utm_medium=reader&utm_source=rss&utm_campaign=blog_implementing-hot-reloading-in-kubernetes?utm_source=thenewstack&utm_medium=website)

    如果想在开发 Kubernetes 应用时直接在集群内测试应用，需要执行相当多的步骤。
    文章介绍了在 Kubernetes 内部进行热重载的意义，以及如何使用[DevSpace](https://github.com/loft-sh/devspace) 高效完成热重载——DevSpace 负责自动重建和重新部署应用，用户只需要保存应用文件。

- [使用 Tracetest 检测和修复性能问题](https://kubeshop.io/blog/detect-fix-performance-issues-using-tracetest?utm_source=thenewstack&utm_medium=website)

    [Tracetest](https://github.com/kubeshop/tracetest) 是基于 OpenTelemetry Traces 的端到端测试工具。
    Tracetest 可以在用户或开发人员遇到 bug 之前发现代码中的异常情况。

- [OPAL 介绍：实时动态授权](https://www.cncf.io/blog/2022/06/27/real-time-dynamic-authorization-an-introduction-to-opal/)

    [OPAL](https://github.com/permitio/opal) 是开放策略代理（OPA）的一个管理层，它能够保持授权层的实时更新。OPAL 对策略和策略数据的变化进行检测，并将实时更新推送给 agent。当应用状态发生变化时，OPAL 将确保服务始终与所需的授权数据和策略保持同步。

- [夜莺（Nightingale）—— Prometheus 的企业级版本](https://mp.weixin.qq.com/s/OXmnH9KsygpB70-NmwxM1w)

    [夜莺](https://github.com/ccfos/nightingale)是一款开源云原生监控分析系统，采用All-In-One 的设计，集数据采集、可视化、监控告警、数据分析于一体，集成云原生生态，提供开箱即用的企业级监控分析和告警能力。
    文章主要介绍了夜莺如何关联可观测性三指标、运维量化、告警噪音处理、产品定位以及 AIOps 应用等。

- [移植 eBPF 应用到 BumbleBee —— 开发 BPF CO-RE 程序最简单的方法](https://www.solo.io/blog/porting-ebpf-applications-to-bumblebee/)

    BPF CO-RE（Compile Once - Run Everywhere）旨在解决 eBPF 程序可移植性的问题。
    文章举例详细说明了如何将一个 BPF CO-RE libbpf 脚本移植到 [Bumblebee](https://github.com/solo-io/bumblebee) 中，以解决 user space、distribution 和集成方面的挑战。

- [一键开启 Kubernetes 可观察性 —— 如何自动生成和存储 OpenTelemetry 追踪](https://mp.weixin.qq.com/s/98tqrwgXviUIe0nRAMgzPw)

    [Tobs](https://github.com/timescale/tobs) 是 Kubernetes 的可观测性技术栈，它可以在几分钟内在 Kubernetes 集群中部署一个完整的可观测性技术栈。
    该栈包括 OpenTelemetry Operator、OpenTelemetry Collector、Promscale 和 Grafana。它还部署了其他几个工具，如 Prometheus，用于收集 Kubernetes 集群的指标，并将其发送到 Promscale。
    Tobs 支持通过 OpenTelemetry Operator 用 OpenTelemetry trace 自动检测的 Python、Java 和 Node.js 服务。

- [Categraf：夜莺监控默认数据采集 Agent 介绍](https://mp.weixin.qq.com/s/Qt0YbhPE6WSvoZZmuCLjyw)

    Categraf 是夜莺监控的默认数据采集 Agent，主打开箱即用和 all-in-one，同时支持对 metrics、log、trace 的收集。
    文章首先对比 categraf 和 telegraf、exporters、grafana-agent、datadog-agent 的异同，然后介绍了 catagraf 的安全、测试和配置。

- [Crane-scheduler：基于真实负载进行调度](https://mp.weixin.qq.com/s/s0usEAA3pFemER97HS5G-Q)

    原生 Kubernetes 调度器只能基于资源的 resource request 进行调度，然而 Pod 的真实资源使用率，往往与其所申请资源的 request / limit 差异很大。
    Crane-scheduler 是成本优化开源项目 Crane 的调度插件，实现了基于真实负载的调度功能，作用于调度过程中的 Filter 与 Score 阶段，并提供了一种灵活的调度策略配置方式，从而有效缓解 kubernetes 集群中各种资源的负载不均问题。

- [如何利用 Multus CNI 在二级网络上使用 Kubernetes 服务](https://cloud.redhat.com/blog/how-to-use-kubernetes-services-on-secondary-networks-with-multus-cni)

    文章介绍了 OpenShift 4.10 开发者预览版如何利用 Multus CNI 在二级网络上使用 Kubernetes 服务，实现 Kubernetes 二级网络在功能上的平等。

- [使用 vmagent 代替 Prometheus 采集监控指标](https://mp.weixin.qq.com/s/jGf1L-8c8id8umB72b3AsQ)

    vmagent 是开源时序数据库 VictoriaMetrics（VM） 中的一个组件，它可以帮助我们从各种来源收集指标并将它们存储在 VM 或者任何其他支持 remote write 协议的 Prometheus 兼容的存储系统中。
    vmagent 可以实现 Prometheus 的诸多功能，但指标抓取更灵活，支持拉取和推送指标，使用更少的内存、CPU、磁盘 I/O 以及网络带宽等。

- [深度解读：分布式系统韧性架构压舱石 OpenChaos](https://mp.weixin.qq.com/s/x-aRajL_ThKgVpOwV5GgXA)

    [OpenChaos](https://github.com/openmessaging/openchaos) 是 RocketMQ 团队针对分布式系统韧性能力而打造的新兴混沌工程工具。
    OpenChaos 针对一些分布式系统特有属性，如 Pub/Sub 系统的投递语义与推送效率，调度编排系统的精准调度、弹性伸缩与冷启效率，streaming 系统的流批实时性等，设置专用的检测模型。
    同时，内置可扩展的模型支持，以便验证在大规模数据请求以及各种故障冲击下的韧性表现，并为架构演进提供优化建议。

- [Kubernetes 将大量采用 Sigstore 来保护开源生态系统](https://www.infoq.cn/article/pXTp33YPCH2LYkQw3HRv)

    去年推出的 Sigstore 是一项面向软件开发人员的免费签名服务，它通过由透明日志技术支持的加密软件签名，提高了软件供应链的安全性。
    Kubernetes 1.24 以及所有未来的版本采用 Sigstore 来签署工件和验证签名。

- [Kubernetes 节点弹性伸缩开源组件 Amazon Karpenter 实践：部署 GPU 推理应用](https://mp.weixin.qq.com/s/DcP9vQGGldCFRNs9odpFJg)

    Karpenter 是亚马逊发布的针对 Kubernetes 集群节点弹性伸缩的开源组件。
    该组件可以针对 Unscheduleable Pods 的需求，自动创建合适的新节点并加入集群中。
    Karpenter 彻底抛弃了节点组的概念，利用 EC2 Fleet API 直接对节点进行管理。
    文章以 GPU 推理的场景为例，详细阐述 Karpenter 的工作原理、配置过程以及测试效果。

- [Kruise Rollout: 让所有应用负载都能使用渐进式交付](https://mp.weixin.qq.com/s/m-r3AQMbv2IPoAAJMhReZg)

    [Kruise Rollout](https://github.com/openkruise/rollouts) 是 OpenKruise（阿里云开源的云原生应用自动化管理套件）针对渐进式交付抽象的定义模型，旨在解决应用交付领域的流量调度以及分批部署问题。
    其能够配合应用流量和实际部署实例的金丝雀发布、蓝绿发布等，以及发布过程能够基于 Prometheus Metrics 自动化分批与暂停，兼容多种工作负载等。

- [Prometheus 长期远程存储方案 VictoriaMetrics 入门实践](https://mp.weixin.qq.com/s/C3fzohygl5_tey70Qnz3og)

    VictoriaMetrics（简称 VM ）是一个支持高可用、经济高效且可扩展的开源监控解决方案和时间序列数据库，可用于 Prometheus 监控数据做长期远程存储。
     除此之外，VM 的主要特点包括：对外支持 Prometheus 相关的 API、指标数据摄取和查询具备高性能和良好的可扩展性、高性能的数据压缩方式等。

- [声明式管理 Helm 版本的工具](https://helm.sh/blog/tools-to-manage-helm-declaratively/)

这篇文章介绍了 Kubernetes 生态中一些可用于声明式管理 Helm 版本的工具（如 CNCF 项目 Flux 和 Argo），并对这些工具进行了比较。

- [使用 Kubecost 和 Kyverno 进行云原生工作负载成本治理](https://dzone.com/articles/cost-governance-of-cloud-native-workloads-using-kubecost-and-kyverno)

    这篇文章介绍了如何使用策略引擎 Kyverno 和 成本管理工具 Kubecost 对云原生工作负载进行成本治理，当 Kubecost 统计的某个 Kubernetes 工作负载的成本高于分配的值时，Kyverno 会创建违规/失败。

- [Dubbo-go-Mesh 开启新一代 Go 微服务形态](https://mp.weixin.qq.com/s/cSsnne_kGfUjm1lKZWLiOw)

    Dubbo-go-Mesh 是分布式 RPC 框架 Dubbo-go 在无代理服务网格场景下的跨生态服务框架实现方案。目前已支持兼容 Istio 的服务治理能力。支持接口级服务发现能力，兼容 Istio 生态的流量控制和管理能力，并且提供了脚手架和应用模板以提高 Go 应用开发效率。

- [如何通过二级调度器在 OpenShift 中引入自定义的调度器](https://cloud.redhat.com/blog/how-to-bring-your-own-scheduler-into-openshift-with-the-secondary-scheduler-operator)

    Kubernetes Scheduler 无法满足一些应用对调度器的特殊需求：如共同调度、拓扑感知调度、负载感知调度等。
    由此，OpenShift 允许用户通过应用市场 Operator Hub 的[二级调度器](https://github.com/openshift/secondary-scheduler-operator)引入各自定制的调度器，并使用该调度器运行他们选择的工作负载。
    而控制面组件仍使用 OpenShift 提供的默认调度器。

- [利用eBPF技术带来的可观测性的上帝视角：Kindling开源项目介绍](https://mp.weixin.qq.com/s/nIqFnIbjrPsrjtxSLQp3gg)

    分布式追踪技术在实际落地过程中常会面临探针自动化覆盖依赖人工、难以覆盖多语言服务、APM trace 缺少内核可观测数据等痛点，
    而 Kindling 基于 eBPF 技术构建的上帝视角带来了解决方案——关联内核可观测数据的 trace。

- [虚拟 Kubernetes 集群: 多租户新模式](https://opensource.com/article/22/3/virtual-kubernetes-clusters-new-model-multitenancy)

    一直以来，基于命名空间和集群的两种多租户模式都存在诸多弊端。
    这篇文章引出一个较新的概念——虚拟集群。它结合了上述两种多租户方法的优点：多租户只使用一个命名空间，租户在虚拟集群内拥有完全控制权。

### 产品选型

- [过去二十年里开源的 12 个开源监控工具大对比](https://mp.weixin.qq.com/s/ByQ3skUrcf1c_DPD4dCbRg)

    文章对 12 款典型的开源监控工具做了简要的介绍和分析，指出各自的优势和不足。
    其中提到的工具包括分布式监控系统 Zabbix、时序数据库 VictoriaMetrics、Prometheus、云原生监控分析系统夜莺监控等。

- [云原生存储工具的选型和应用探讨](https://mp.weixin.qq.com/s/QoVlOe01hGWSYEKS8wfsKw)

    文章逐步梳理了云原生存储的概念，并对 Longhorn、OpenEBS、Rook+Ceph 进行简要介绍和横向对比，最后选择了具有代表性的 Longhorn 演示其安装和使用。

- [K8s CNI 插件选型和应用场景探讨](https://mp.weixin.qq.com/s/GG7GX_E1oyZf-cmjk80OYg)

    文章介绍容器环境常见七个网络应用场景及对应场景的 Kubernetes CNI 插件功能实现。

- [云原生时代的 DevOps 平台设计之道（Rancher vs KubeSphere vs Rainbond）](https://mp.weixin.qq.com/s/oxeNq4GHE85NUBIDcgixcg)

    文章重点介绍了 Rancher 、KubeSphere、Rainbond 三款云原生平台级产品各自不同的 DevOps 实现。
    作者认为，DevOps 团队可以选择 Rancher + KubeSphere 或 Rancher + Rainbond 的组合。
    Rancher 最擅长向下对接基础设施，管理集群的安全性与合规性，而向上为开发人员提供易用的云原生平台则交给 KubeSphere 或 Rainbond。

- [到底谁强？Grafana Mimir 和 VictoriaMetrics 性能测试](https://mp.weixin.qq.com/s/TVJZ5k5U7bs8WEyE4rikSQ)

    文章比较 VictoriaMetrics 和 Grafana Mimir 集群在相同硬件上运行的工作负载的性能和资源使用情况。
    在基准测试中，与 Mimir 相比，VictoriaMetrics 表现出更高的资源效率和性能。从操作上讲，VictoriaMetrics 扩展更为复杂，Mimir 可以很容易实现组件扩展。

- [一文读懂 Prometheus 长期存储主流方案](https://mp.weixin.qq.com/s/1BF83kIF_AGVD9J2qLnlSA)

    由于 Prometheus 存在跨集群聚合、长时间存储等局限性，社区给出了多种扩展方案。
    文章对包括 M3、VictoriaMetrics、Thanos、Cortex、Grafana Mimir 在内的 5 种主流 Prometheus 长期存储方案进行了多维度对比分析。

- [eBPF 基础设施库的技术选型](https://mp.weixin.qq.com/s/4WNyNwkRW2lZ82nMOP6rMA)

    文章对几个 eBPF 基础设施库进行比较，如 libbcc、dropbox 的 goebpf、Cilium 的 ebpf 库、Calico 的底层库、falco 的 lib 库，
    并说明开源可观测性工具 Kindling 选择 falco-libs 的原因。

- [在生产环境如何选择靠谱的 APM 系统](https://mp.weixin.qq.com/s/3dD0hIuqpXdepLVC6V7aoA)

    文章从主流 APM 产品介绍出发（对比 Pinpoint、Jaeger、Skywalking、听云、腾讯云+阿里云 Arms 和 Datadog），通过生产环境中关注的几个重要维度，如产品体验、Agent 能力、报警+ DB 支持、云原生的支持能力、数据大屏等，给予 APM 选型方案建议。

### 前沿热点

- [探索 K8s 新功能 Container Checkpointing](https://sysdig.com/blog/forensic-container-checkpointing-dfir-kubernetes/)

    容器检查点功能（K8s 1.25 alpha）为某个正在运行的容器创建一个状态点的快照，并将其保存到磁盘中。
    之后可以使用此检查点启动容器，恢复状态，或者将容器迁移到其他的机器上。
    文章介绍了这个功能的工作原理、Podman 的检查点功能、CRIU 以及取证分析等应用场景。

- [OCI 容器与 Wasm 初体验](https://mp.weixin.qq.com/s/4oFErzG65b-0FfpHQB941A)

    文章介绍如何通过配置，让 OCI 运行时运行 Linux 容器和与 WASI 兼容的工作负载。

- [Service Mesh 的下一站是 Sidecarless 吗？](https://mp.weixin.qq.com/s/SF5uN8VHwrqji4xdME4hCg)

    尽管 Cilium、Linkerd、Istio 等几大开源社区都在 Sidecarless 领域进行了各自的探索和实践，但是各家在安全性，稳定性，管理成本，资源占用上是各有侧重点的，适应不同的业务场景。

- [eBPF 程序摄像头——力争解决可观测性领域未来最有价值且最有挑战的难题](https://mp.weixin.qq.com/s/FYNe1H5dmBpbKFOrIpjuzQ)
  
    当前可观测性用户很容易迷失在指标迷阵当中，不知该在什么时间查看何种指标，如何理解大规模细粒度的指标。
    为解决此问题，Kindling 社区选择了基于 eBPF 的可观测性摄像头，按照 eBPF 粒度去获取程序执行过程当中的细粒度指标，帮助用户理解程序执行的真实过程，同时理解细粒度的指标是如何影响程序执行的。

- [GitOps 是皇帝的新衣吗](https://mp.weixin.qq.com/s/CpLvQM2rTI4InIN1Vk5ZKg)

    在采用 GitOps 前，我们需要了解清楚“什么是 GitOps？”，并问自己“我们使用这些工具为谁提供服务？我们试图解决什么问题？”
    文章针对 GitOps 的一些主要“卖点”（包括安全性、版本控制和环境历史、回滚、飘逸处理、单一真相来源等）提出了质疑，并介绍了 GitOps 带来的一些挑战。

- [蚂蚁规模化平台工程实践两年多，我们学到了什么](https://mp.weixin.qq.com/s/X8AWh43qp4fb4eJSkx50hw)

    平台工程是一门设计与构建工具链和工作流程的学科，可以为云原生时代的软件工程组织提供自助式服务功能。
    文章基于可编程云原生协议栈 [KusionStack](https://github.com/KusionStack) 在蚂蚁平台工程及自动化中的实践，从平台工程、专用语言、分治、建模、自动化和协同文化等几个角度，阐述规模化平台工程实践中的收益和挑战。

- [可观测可回溯 | 持续性能分析 Continuous Profiling 实践解析](https://mp.weixin.qq.com/s/yiwq81ZHB0nSTcYSjOeyZg)

    持续性能分析（简称 CP）对于开发者的意义在于，在生产环节，永远知道代码的所有执行细节。
    文章在介绍 CP 发展历史的基础上，分析了性能分析 profiling 的 2 个关键点：获取堆栈数据和生成火焰图，以及常见的 profiling tool。

- [下一代云原生边缘设备管理标准 DMI 的设计与实现](https://mp.weixin.qq.com/s/T3TnKXhBefqavP4rni59Sg)

    DMI 整合设备管理接口，优化边缘计算场景下的设备管理能力；
    同时定义了 EdgeCore 与 Mapper 之间统一的连接入口，并分别由 EdgeCore 和 Mapper 实现上行数据流和下行数据流的服务端和客户端，承载 DMI 具体功能。

- [使用 eBPF LSM 热修复 Linux 内核漏洞](https://mp.weixin.qq.com/s/UJEC8nmfQbdsWdJMfju0ig)

    Linux Security Modules（LSM）是一个基于 hook 的框架，用于在 Linux 内核中实现安全策略和强制访问控制。
    文章介绍了 eBPF LSM 的实现思路（核心内容是确定 hook 点），如何使用 unshare 将 user 映射到 root，以及如何通过在 eBPF 中实现程序来解决真实场景问题。
    最后，对比了这个 LSM 程序的性能影响。

- [关于 Cilium Service Mesh，你需要知道的一切](https://isovalent.com/blog/post/cilium-service-mesh/)

    Cilium 在最新发布 [v1.12](https://github.com/cilium/cilium/releases/tag/v1.12.0) 中正式推出 Cilium Service Mesh。
    在 Cilium Service Mesh 中，除有多种不同的控制平面可供选择外，用户还能够灵活地选择运行有/无 sidecar 模型的服务网格。

- [使用 eBPF 准确定位服务网格的关键性能问题](https://www.tetrate.io/blog/pinpoint-service-mesh-critical-performance-impact-by-using-ebpf/)

    [SkyWalking Rover](https://github.com/apache/skywalking-rover) 是 SkyWalking 生态系统中引入的 eBPF profiling 功能，可实现 CPU profiling、off-CPU profiling 等。
    文章讨论了如何使用 eBPF 技术来改进 SkyWalking 中的剖析功能，并用于分析服务网格中的性能影响。

- [coolbpf 技术实践，将 BPF 程序开发效率提升百倍](https://www.infoq.cn/article/IielSpCwjf6Owd6jMBef)

    [coolbpf](https://github.com/aliyun/coolbpf) 是由龙蜥社区开源的一站式 BPF 开发编译平台，旨在解决 BPF 在不同系统平台的运行和生产效率提升问题。
    coolbpf 的六大功能：本地编译服务，基础库封装；远程编译服务；高版本特性通过 kernel module 方式补齐到低版本；自动生成 BTF；各内核版本功能测试自动化；Python、Rust、Go、C 等高级语言支持。

- [阿里云容器服务负责人对云原生与软件供应链安全的思考](https://mp.weixin.qq.com/s/jz8sBMeHTSFm8sndHakddw)

    文章作者介绍了目前容器化软件供应链安全的最新实践和工具链，包括容器镜像的 SBOM 支持，以及新一代镜像签名技术—— Sigstore 的无密钥签名 Keyless Signatures 模式。

- [eBPF、Sidecar 和服务网格的未来](https://buoyant.io/2022/06/07/ebpf-sidecars-and-the-future-of-the-service-mesh/)

    Linkerd 团队认为，至少在可预见的未来，eBPF 服务网格仍然需要 sidecar 代理。
    一方面，eBPF 的局限性意味着 L7 流量代理仍然需要用户空间网络代理来完成工作；
    另一方面，同 sidecar 相比，基于主机的代理在操作、维护和安全性方面都更差。
    而 Linkerd 未来将继续利用 eBPF 技术让 sidecar 代理变得更小更轻快。

- [通过模糊测试提高 CNCF 项目的安全性](https://mp.weixin.qq.com/s/B63juDzcifj_UOCxc8Xo_g)

    模糊测试是一种测试软件的技术，将“随机数据”传递到目标应用中，观察目标应用是否崩溃。
    [OSS-Fuzz](https://github.com/google/oss-fuzz) 是一个开源项目，为持续模糊测试提供了一个自动化平台。截止目前，共有 18 个 CNCF 项目通过 OSS-Fuzz 进行持续模糊测试。  
    点击了解 [CNCF 模糊测试的更多细节](https://github.com/cncf/cncf-fuzzing)

- [什么是持续分析?](https://www.cncf.io/blog/2022/05/31/what-is-continuous-profiling/)

    持续分析（continuous profiling）是一种分析程序复杂性的动态方法，通过了解系统在一段时间内的资源，定位、调试和修复与性能有关的问题。
    CNCF 的 CTO 认为，持续分析是可观测性堆栈不可或缺的一部分。
    文章介绍了与此相关的概念、行业动态以及开源持续性能分析平台。  
    点击访问 Pyroscope [项目地址](https://github.com/pyroscope-io/pyroscope)

- [Envoy Gateway 计划提供一个标准化 Kubernetes 入口](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/)

    Envoy Gateway 计划使 Envoy 反向代理成为一个网络网关，不仅可以引导内部微服务流量，还可以管理进入网络的外部流量。
    其根本目的是为 Kubernetes 建立一套标准化、简化的 API。

- [使用 WebAssembly 验证请求负载](https://www.tetrate.io/blog/validating-a-request-payload-with-wasm/)

    这篇文章介绍了如何使用 Wasm 插件来扩展 Istio——验证一个请求的有效负载。
    当你需要添加 Envoy 或 Istio 不支持的自定义功能时，可以使用 Wasm 插件，如使用 Wasm 插件来添加自定义验证、认证、日志或管理配额。

- [OPLG：新一代云原生可观测最佳实践](https://mp.weixin.qq.com/s/Bf6nmOymcG9bk91VxLL_Kw)

    OPLG 是指将 OpenTelemetry Traces、Prometheus Metrics、Loki Logs 通过 Grafana Dashboards 进行统一展示，满足企业级监控与分析的大部分场景。
    基于 OPLG 体系可以快速构建一套覆盖云原生应用全栈的统一可观测平台，全面监测基础设施、容器、中间件、应用及终端用户体验。

- [Kubernetes 软件供应链安全必备四要素](https://www.cncf.io/blog/2022/04/12/a-map-for-kubernetes-supply-chain-security/)

    这篇文章介绍了Kubernetes DevOps 团队理解软件供应链安全所需的四个要素：Artifacts、Metadata、Attestations和 Policies（A-MAP）。
    软件构建系统产生工件和元数据，验证构建完整性和软件组件安全属性需要证明和策略。

### 安全漏洞

- [Istio 高风险漏洞：拥有 localhost 访问权限的用户可以冒充任何工作负载的身份](https://github.com/istio/istio/security/advisories/GHSA-6c6p-h79f-g6p4)

    如果用户拥有 Istiod 控制平面的 localhost 访问权，他们可以冒充服务网格内的任何工作负载身份。
    受影响的版本为 1.15.2。目前，已发布补丁版本 [1.15.3](https://github.com/istio/istio/releases/tag/1.15.3)。

- [Istio 高风险漏洞：Golang Regex 库导致 DoS 攻击](https://github.com/istio/istio/security/advisories/GHSA-86vr-4wcv-mm9w)

    Istiod 存在请求处理错误漏洞，攻击者会在 Kubernetes validating 或 mutating webhook 服务曝光时，发送自定义或超大消息，导致控制平面崩溃。
    目前，[Istio](https://github.com/istio/istio/releases) 已发布补丁版本 1.15.2、1.14.5 和 1.13.9。低于 1.14.4、1.13.8 或 1.12.9 的版本会受此影响。

- [CrowdStrike 发现针对 Docker 和Kubernetes 基础设施的新型挖矿攻击](https://www.crowdstrike.com/blog/new-kiss-a-dog-cryptojacking-campaign-targets-docker-and-kubernetes/)

    该攻击通过容器逃逸技术和匿名矿池，使用一个模糊的域名来传递其有效负载，以对 Docker 和 Kubernetes 基础设施开展加密货币挖掘活动。
    采用云安全保护平台能够有效保护云环境免受类似的挖矿活动的影响，防止错误配置和控制平面攻击。

- [Kube-apiserver CVE 漏洞: 聚合 API server 可能导致服务器请求伪造问题（SSRF）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#cve-2022-3172-aggregated-api-server-can-cause-clients-to-be-redirected-ssrf)

    攻击者可能控制聚合 API Server，将客户端流量重定向到任何 URL。这可能导致客户端执行意外操作，或将客户端证书泄露给第三方。
    此问题没有缓解措施。集群管理员应注意保护聚合 API Server，不允许不受信任方访问 mutate API Services。
    受影响版本：kube-apiserver 1.25.0、1.24.0 - 1.24.4、1.23.0 - 1.23.10、1.22.0 - 1.22.14。已修复版本：1.25.1、1.24.5、1.23.11、1.22.14。

- [Aqua 发现新型非法加密挖矿方式，能够利用容器消耗网络带宽](https://blog.aquasec.com/cryptojacking-cloud-network-bandwidth)

    近日，Aqua Security 发布了一则关于新型挖矿攻击的警报。较传统的挖矿攻击会造成 CPU 消耗的急剧增加，新型攻击利用容器消耗网络带宽，而 CPU 消耗增加并不显著。
    因此，依靠 CPU 利用率来识别攻击的安全工具可能无法发现该威胁。
    Aqua 建议，运行能够静态和动态分析容器的安全工具是最有效的抵御攻击的方式。

- [Istio 漏洞：向 Envoy 发送格式不正确的头信息可能导致未知内存访问](https://istio.io/latest/news/security/istio-security-2022-006/)

    在受影响的版本（1.14.2 和 1.13.6）中，在某些配置中向 Envoy 发送的格式错误头信息可能导致未知行为或崩溃。该漏洞已在 1.12.8、1.13.5 和 1.14.1 版本中得到解决。此外，Istio 官方建议不要在生产环境中安装 1.14.2 或 1.13.6。

- [CRI-O 漏洞：Kube API 访问可能会导致节点上的内存耗尽](https://access.redhat.com/security/cve/cve-2022-1708)

    CRI-O 会读取 ExecSync 请求的输出结果。如果输出的数据量很大，有可能耗尽节点的内存或磁盘空间，对系统可用性造成威胁。目前，该文章尚未给出解决方案。

- [Istio 控制平面存在请求处理漏洞](https://istio.io/latest/news/security/istio-security-2022-004/)

    Istiod 存在请求处理漏洞，发送定制信息或超大信息的攻击者可能会导致控制平面进程崩溃。
    当Kubernetes 验证或变更 webhook 服务公开暴露时，受攻击的风险最大。此漏洞为 0day 漏洞。

### 电子书

- [白皮书《云原生成熟度矩阵评估》中文版](https://mp.weixin.qq.com/s/xLuAOXwCVif7KrrpZIcUow)

    白皮书为正处于云原生转型的企业总结了一套云原生成熟度矩阵评估流程。从文化、产品、团队、流程、架构、维护、交付、配置、基础设施 9 个领域评估组织当前所处的状态。
    同时，阐明 4 种经典的云原生转型误区，并总结出典型的云原生转型方案。  
    点击阅读[白皮书](https://pan.baidu.com/s/1qfEqtL-LCbBo9GhnZBcyyg)，提取码：kvrv

- [电子书《零信任的基石：使用 SPIFFE 为基础设施创建通用身份》](https://mp.weixin.qq.com/s/3qwVW8AeyRvUVxYAq22XKg)

    这本书介绍了服务身份的 SPIFFE 标准，以及 SPIFFE 的参考实现 SPIRE。
    深入阐述了如何设计一个 SPIRE 部署、与其他系统集成的方法、如何使用 SPIFFE 身份通知授权、与其他安全技术对比等。

- [Kube-OVN v1.10 系列中文文档，99.9% 的问题都能在这里找到答案](https://mp.weixin.qq.com/s/OI996gGQasWaFLy2Matghw)

    文档分为五个部分：Kube-OVN 快速入门、使用指南、运维指南、高级功能和技术参考。  
    点击查阅[文档](https://kubeovn.github.io/docs/)

- [从构建到治理，业内首本微服务治理技术白皮书正式发布](https://mp.weixin.qq.com/s/mG0jX66BLOHY0TWTqYO50A)

    阿里云云原生微服务团队近日发布[《微服务治理技术白皮书》](https://developer.aliyun.com/ebook/read/7565?spm=a2c6h.26392459.ebook-detail.4.12d9775enBrpOH)。
    该白皮书聚焦微服务治理业务领域，囊括了技术原理、业务场景、解决方案、最佳实践等微服务落地的全流程。

### 其他

- [Containerd 深度剖析-NRI 篇](https://mp.weixin.qq.com/s/2LrWqOtqIfbIzWG9fv5ANA)

    NRI 是 containerd 中的 CRI 插件，提供一个容器运行时级别的插件框架来管理节点资源。
    NRI 可用来解决批量计算、延迟敏感性服务的性能问题，以及满足服务 SLA/SLO、优先级等用户需求，
    比如通过将容器的 CPU 分配同一个 numa node，来保证 numa 内的内存调用。
    当然除了 numa，还有 CPU、L3 cache 等资源拓扑亲和性。

- [Kubernetes 证书管理系列](https://mp.weixin.qq.com/s/6VC_15V0MlvN-vCN-GwRLQ)

    文章介绍了 Kubernetes 中的证书以及 Kubernetes 证书管理器在实际生产中的作用。然后以证书管理项目 cert-manager 为例，阐释其架构、组件、生态兼容等。

- [2022 年容器生态系统的 9 大趋势洞察](https://mp.weixin.qq.com/s/WNanrbCsdWEuyWP8WvO8UQ)
  
    Datadog 对客户运行的超 15 亿个容器进行了分析，总结出容器生态系统的主要趋势：
    无服务器容器技术在公共云中的使用率持续上升、多云使用率和组织的容器数量正相关、Kubernetes Ingress 使用率正在上升、大多数主机使用超过 18 个月的 Kubernetes 版本、超过 30% 的运行 containerd 的主机使用不受支持的版本、NGINX、Redis 和 Postgres 是最受欢迎的容器镜像。

- [Karmada 大规模测试报告发布，突破 100 集群和 50 万节点](https://karmada.io/zh/blog/2022/10/26/test-report/)

    近日，Karmada 社区对 Karmada 开展了大规模测试工作。根据测试结果分析，以 Karmada 为核心的集群联邦可以稳定支持 100 个集群和 50 万个节点同时在线，管理超过 200 万个Pod。
    在使用场景方面，Push 模式适用于管理公有云上的 Kubernetes 集群，而 Pull 模式相对于 Push 模式涵盖了私有云和边缘相关的场景。
    在性能和安全性方面，Pull 模式的整体性能要优于 Push 模式。

- [toB 应用私有化交付技术发展历程和对比](https://mp.weixin.qq.com/s/JcDZxabHImljPCEus_inlg)

    在传统应用交付中，管理运行环境和操作系统差异是一个痛点。当前云原生应用交付使用容器和 kubernetes 相关技术解决了这个问题，但是这些技术的学习和使用门槛太高。
    因而，抽象的应用模型成为下一代解决方案，例如，基于 OAM 的 KubeVela 应用交付和基于 RAM 的 Rainbond 应用交付。

- [国内外云厂商容器服务备份恢复方案调研](https://mp.weixin.qq.com/s/P71vBPiID8o1GI6pqbaO6w)

    文章对四家厂商的容器服务备份恢复方案（阿里云容器服务 ACK、腾讯云容器服务 TKE、华为云备份产品 CBR、谷歌云 Backup for GKE）进行了调研分析，比较各自的优缺点。

- [云原生网关 Apache APISIX 3.0 与 Kong 3.0 功能背后的趋势](https://mp.weixin.qq.com/s/hyqqDojuzEU-LvfR5deBZw)

    文章详细分析了两个 API 网关项目 APISIX 和 Kong 的最新版本，试图从更新细节洞察有价值的技术趋势。
    Kong 3.0 开始逐渐倾向于企业版，侧重政府、金融业以及对安全合规更关注的大型企业。
    而 APISIX 3.0 版本推出的所有功能都是开源的，在保证性能的同时，也在积极扩展周边生态。

- [Kubernetes Node 组件指标梳理](https://mp.weixin.qq.com/s/nrKk7tuARnvfnH0VOF7q9Q)

    文章对 kubelet 自身指标、kube-proxy 指标、kube-state-metrics 指标以及 cadvisor 指标进行了完整梳理。

- [Kubernetes 1.25 中的删除和主要变化](https://kubernetes.io/blog/2022/08/04/upcoming-changes-in-kubernetes-1-25/)

    v1.25 的删除和主要变化：删除 PodSecurityPolicy、核心 CSI 迁移功能升级为 GA、弃用 GlusterFS、Kubernetes 发布工件签名升级为 Beta、cgroup v2 支持升级为 GA、清理 IPTables 链所有权。

- [解读 Curve 资源占用之内存管理](https://mp.weixin.qq.com/s/3gupHWlcRRY-lCsV9nZhDA)

    文章结合分布式存储系统 [Curve](https://github.com/opencurve/curve) 说明内存布局，以及内存分配器的必要性和需要解决的问题，
    并通过举例说明内存分配器的内存管理方法，最后介绍当前 Curve 内存分配器的选择及原因。

- [Kubernetes 单机侧的驱逐策略总结](https://mp.weixin.qq.com/s/ehECtQiXSHLpCrH5vuBX_w)

    文章总结用户空间和内核空间的驱逐流程和进程选择策略。
    用户态中 Kubelet 通过驱逐来限制节点资源、pod 资源。
    用户空间通过监控系统资源来触发驱逐流程，内核空间通过分配内存时触发驱逐流程。

- [GitOps 成熟度检查清单](https://www.weave.works/blog/the-16-point-checklist-for-gitops-success)

    文章介绍了一份 [GitOps 检查清单](https://go.weave.works/rs/249-YDT-025/images/The%2016-point%20Checklist%20for%20GitOps%20Success.pdf)，可用于评估团队 GitOps 的成熟度。
    清单共 16 项，包括六个维度：团队文化、git 管理、GitOps pipeline、Kubernetes、安全&策略。

- [为什么 Istio 要使用 SPIRE 做身份认证？](https://mp.weixin.qq.com/s/043yz1etTkJ1l4Eo6DG7WA)

    Istio 1.14 中最值得关注的特性是新增对 [SPIRE](https://github.com/spiffe/spire) 的支持。
    SPIFFE 统一了异构环境下的身份标准。Istio 利用 SPIRE 为每个工作负载提供一个唯一标识，服务网格中的工作负载在进行对等身份认证、请求身份认证和授权策略都会使用到服务标识，用于验证访问是否被允许。

- [弃用 Pod Security Policies 后，如何确保 Pod 安全](https://www.cncf.io/blog/2022/06/30/how-to-secure-kubernetes-pods-post-psps-deprecation/)

    Pod Security Policies（PSP） 已被弃用，未来将在 Kubernetes 1.25 中删除。
    Pod Security Admission（PSA） 将取代 PSP 来实现 Pod 的安全特性，它为 pod 定义了三种隔离级别：privileged、baseline 和 restricted。此外，也可以采用外部准入控制器，如 OPA 和 Kyverno。

- [CryptoMB - 加速 Istio TLS 握手](https://istio.io/latest/blog/2022/cryptomb-privatekeyprovider/)

    文章介绍了 Envoy 1.20 和 Istio 1.14 中引入的一个新功能：通过 CryptoMB Private Key Provider 来加速 Istio TLS 握手。
    CryptoMB 是一个Envoy 扩展，它利用 Intel multi-buffer 技术，使得服务网格可以卸载 TLS 握手，以处理更多连接，降低延迟并节省 CPU。

- [如何看待 Dapr、Layotto 这种多运行时架构](https://mp.weixin.qq.com/s/sKaKzlOXsLSmqBwv9uI5Cw)

    文章分享了蚂蚁在落地多运行时架构 Layotto 之后的思考：
    Dapr API 的 “可移植性” 的必要性、多运行时架构的价值、与 Service Mesh、Event Mesh 的区别以及部署形态等。

- [Kubernetes 1.24: 避免为 Services 分配 IP 地址时发生冲突](https://kubernetes.io/blog/2022/05/23/service-ip-dynamic-and-static-allocation/)

    Kubernetes 1.24 允许启用一个新的特性门控 ``ServiceIPStaticSubrange``。 
    启用此特性后，可以为 Service 使用不同的 IP 分配策略，减少冲突的风险。

- [Harbor v2.5 远程复制：制品的签名如影随形](https://mp.weixin.qq.com/s/erH1iCbNn9yM1Bl5UlgGMg)

    Harbor v2.5 于上周发布，其中Cosign制品签名和验证解决方案是重要功能，解决了镜像等制品在远程复制中，其签名信息无法被复制到目标端的问题。
    这篇文章对该功能进行了详细介绍。
