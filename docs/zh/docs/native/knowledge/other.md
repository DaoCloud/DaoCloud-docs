# 其他

本页列出一些云原生社区的其他事项和文章。

- [云原生如何改变电信标准：自上而下与自下而上的对决](https://mp.weixin.qq.com/s/dH_3CAd0PS3EPYKpJA2yNQ)

    文章介绍了云原生自下而上的开发原则、最佳实践和事实标准的逻辑，以及自上而下的、由委员会驱动的标准，如电信行业的标准。
    而自上而下和自下而上的标准相遇会发生什么，当协议的管理者与云原生标准相遇时又会发生什么？

- [接管 K8s 部署运维，基础架构团队是否做好准备？](https://mp.weixin.qq.com/s/7Y5GfShZhFwBQkQfRUPnoA)

    Kubernetes 非常适合作为一种 Infrastructure as a Service（IaaS），既可以在公有云上提供，也可以在企业私有云上作为新一代的基础架构，为现代化应用提供可靠的基础设施。
    因此，Kubernetes 的建设和运维也将更多地交由基础架构团队负责。
    文章探讨了为什么基础架构团队适合负责 Kubernetes 的运维管理，以及这样的转变是否可行。

- [2022 云原生技术盘点与展望](https://mp.weixin.qq.com/s/yRMTS5z15-PERwlameMOIw)

    文章从底层基础技术和场景化的应用技术两方面，对 2022 年云原生的发展情况进行盘点：混部带来了效率的提升；
    Serverless 基于容器完成标准化；Service Mesh 进行新尝试，落地方式还在探索；降本增效大主题下，FinOps 理念快速发展等。

- [K8s 原生支持的准入策略管理](https://mp.weixin.qq.com/s/wDlCQkHTBUQDucT9K7G2mg)

    Kubernetes 1.26 提供了一个 alpha 版本的验证准入策略更新，即在验证准入策略时可以使用一种通用的表达式语言（CEL）来提供声明的、进程内的替代方法来验证 validating admission webhook。将 CEL 表达式嵌入到 Kubernetes 资源中，大大降低了 admission webhook 的复杂性。

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

    Harbor v2.5 于上周发布，其中 Cosign 制品签名和验证解决方案是重要功能，解决了镜像等制品在远程复制中，其签名信息无法被复制到目标端的问题。
    这篇文章对该功能进行了详细介绍。