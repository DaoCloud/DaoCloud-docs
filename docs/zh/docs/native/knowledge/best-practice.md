# 最佳实践

本页列出云原生社区推崇的最佳实践，供产品和交付参考学习。

- [跨集群运行 StatefulSet](https://mp.weixin.qq.com/s/y1dEO8Fb3SxqQUW9WrEsHQ)

    跨集群可靠地运行 StatefulSet 可能需要解决网络和存储两个方面的问题。
    文章基于一个示例，介绍了配置和管理跨集群的有状态应用服务的一个方法。

- [我们如何基于云原生项目发展开源社区？](https://thenewstack.io/how-do-we-cultivate-community-within-cloud-native-projects/)

    基于云原生项目发展开源社区，首先要知道哪些人会关心你的项目、谁是终端用户、利益相关者和贡献者？
    他们做什么工作、在哪工作以及使用目标是什么？
    发现更多的潜在利益相关者，为他们提供贡献途径，对提高项目的采用率来说至关重要。

- [Dapr 集成 Flomesh 实现跨集群服务调用](https://mp.weixin.qq.com/s/Y-MewxHVMULKDi4_cbl6Yw)

    [Flomesh 服务网格](https://github.com/flomesh-io/fsm)使用可编程代理 Pipy 为核心提供东西、南北向的流量管理。
    通过基于 L7 的流量管理能力，突破计算环境间的网络隔离，建立一个虚拟的平面网络，使不同计算环境中应用可以互相通信。
    文章介绍通过 Dapr 与 Flomesh 服务网格的集成进行跨集群的服务调用，实现“真正的”多集群互联互通。

- [云原生场景下，如何缓减容器隔离漏洞，监控内核关键路径？](https://mp.weixin.qq.com/s/qlmm2h8RpQnKOnEjlK0pMA)

    文章介绍了 OpenCloudOS 社区自研的两个方案：CgroupFS 和 SLI，用于缓减容器隔离漏洞，监控内核关键路径。
    CgroupFS 方案提供一个内核态容器视角的虚拟机文件系统(/proc、/sys)，增强了容器资源视图隔离。
    SLI 是容器级别的性能跟踪机制，从容器的角度对 CPU、内存资源的竞争情况进行跟踪、观测，从而为容器性能问题的定位、分析提供可靠的指标。

- [基于 Kubernetes 和 Istio 轻松完成 gRPC 到 REST 的转码](https://cloud.redhat.com/blog/grpc-to-rest-transcoding-with-openshift-and-service-mesh)

    文章介绍如何在无需修改大量代码的情况下使得 gRPC 服务与 REST 兼容。
    该方案利用 Envoy 过滤器，建立一个转码器，让 RESTful JSON API 客户端通过 HTTP 发送请求，并被代理到一个 gRPC 服务。
    转码器将 gRPC 服务方法的消息输出编码为 JSON，并将 HTTP 响应的 Content-Type 头设置为 application/json。

- [kube-state-metrics 在大规模集群下的优化](https://mp.weixin.qq.com/s/8R55Holzrf0wNVD8DLJnAg)

    在小规模集群中，只需要保证 kube-state-metrics 高可用就可以在生产环境使用。
    但是对于大规模的集群，只通过一个 KSM 实例来提供 metrics 指标是非常吃力的，还需要做很多优化：
    例如，过滤不需要的指标和标签，通过分片降低 KSM 实例压力，使用 DaemonSet 方式单独针对 pod 指标进行部署。

- [vivo 自研 Jenkins 资源调度系统设计与实践](https://mp.weixin.qq.com/s/wEmheHwTA8m8LHr_5LVSyg)

    文章从目前业界实现 Jenkins 的高可用的实现方案入手，分析各方案的优缺点，引入 vivo 目前使用的 Jenkins 高可用方案——jenkins scheduler 系统。
    该系统不采用原生的 Jenkins 部署方案，而是采用全 master 的方式，master 之间的关系、任务分配、离线、插件安装等由调度系统进行管理。
    目前该系统已经投入生产环境运行。

- [K8s 迁移 cgroup v2 之前要做的三件事](https://mp.weixin.qq.com/s/BV-y82MalhG-A--hvUFMcg)

    随着 Kubernetes 1.25 关于cgroup v2 特性的正式发布（GA），kubelet 容器资源管理能力得到加强。
    文章在 cgroup v2 概念的基础上，介绍了采用 cgroup v2 之前在 Linux OS、K8s 生态、应用变更三方面要做的事。

- [阿里云云原生实战指南](https://developer.aliyun.com/ebook/7879?spm=a2c6h.26392470.ebook-read.13.3e855bc8YpIdco)

    该指南涵盖了全球云原生应用洞察与趋势、阿里云在云原生领域的最新产品与技术布局、阿里云 All in Serverless 的全新思考与投入、传音、新东方、小红书等企业的上云实战经验。

- [服务网格安全性和高可用性部署最佳实践](https://mp.weixin.qq.com/s/hFCshQpmF7Vr0jrpugArjA)

    文章介绍在多集群的基础设施中部署服务网格时的安全性和高可用性最佳实践，包括：控制平面应该如何部署在应用程序附近；
    入口应该如何部署以促进安全性和敏捷性；如何使用 Envoy 促进跨集群负载均衡，以及网格内部如何使用证书。

- [大中型科技企业开源战略制定与落地](https://mp.weixin.qq.com/s/9Z4zFPU0uHk6RhrpUDD-tw)

    目前，很多企业对于开源是什么，怎么用开源，如何参与开源，企业在开源方面如何做决策，如何进行开源治理，如何利用开源强化竞争力等方面的问题，仍存在着一些难点。
    对此，文章介绍了什么是企业开源战略；企业为什么需要开源战略；企业开源战略包含的内容，以及企业开源战略制定和落地的实践经验。

- [ServiceAccount Token 在不同 K8s 版本中的使用](https://mp.weixin.qq.com/s/F0V8nyo3LtATFmS7pHuxXw)

    文章介绍了在不同 K8s 版本下，ServiceAccount Token 令牌的不同使用方式，
    主要包括自动创建 Secret 和 Kubelet 通过 TokenRequest API 去申请 API 两种方式。

- [腾讯百万级别容器云平台实践揭秘](https://mp.weixin.qq.com/s/Gusp1ah_qIoMMOg7FhX6Vg)

    文章介绍了腾讯容器云平台在线业务资源容器化部署遇到的问题、容器化对动态路由同步的挑战及各自的解决方案，
    以及为解决 K8s 已有自愈机制存在容器销毁阶段卡住的问题，探索出的一种全新的容器销毁失败自愈机制。

- [在生产中大规模自动化 Istio CA 轮换](https://mp.weixin.qq.com/s/75paqvd507_ExHHGszB_-Q)

    文章展示如何配置 Istio 以自动重新加载其 CA，以及如何配置 cert-manager 在 Istio 的中间 CA 到期前定期自动轮换，以提高在多个集群上管理 CA 的操作效率。

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