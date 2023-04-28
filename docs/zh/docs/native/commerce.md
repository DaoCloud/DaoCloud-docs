# 商业产品

本页按字母顺序列出一些知名商业化产品的更新动态。

### A

- [Aqua 云原生安全平台引入基于 eBPF 技术的零日漏洞检测工具 Lightning Enforcer](https://blog.aquasec.com/combat-zero-day-threats-with-aquas-ebpf-lightning-enforcer)

    Aqua Lightning Enforcer 利用漂移和基于行为的自动化检测方法，检测零日漏洞等未知威胁，并提供事件管理、可疑行为告警以及开箱即用的 CNDR（云本地检测和响应）。
    此外，eBPF 技术的应用避免了传统代理对工作负载的影响，降低了系统的资源开销。

- [Aqua 推出首个端到端软件供应链安全解决方案，保护云原生应用供应链的安全](https://mp.weixin.qq.com/s/8GHg5onYiuzrDvF5a64GxQ)

    该解决方案是 Aqua 云原生应用保护平台的一部分，提供的功能包括：代码扫描、CI/CD 态势管理、流水线安全管理、优化 SBOM 功能、评估开源代码的健康状况和口碑情况。

- [ARMO Platform Kubernetes 安全平台 推出基于 eBPF 技术的漏洞分析和评估功能](https://www.armosec.io/blog/kubernetes-vulnerability-relevancy-and-prioritization/)

    该功能可以针对 Kubernetes 平台上存在的漏洞进行分析和评估，识别和确定漏洞的相关性和优先级，为用户提供有针对性的修复建议。其中，相关性和优先级允许用户降低未使用的软件包和组件的漏洞的优先级，从而专注于解决对集群构成更大威胁的漏洞。

- [AtomicJar 发布集成测试工具 Testcontainers Cloud](https://containerjournal.com/topics/container-management/atomicjar-unveils-testcontainers-cloud-service/)

    Testcontainers Cloud 基于轻量级开源测试框架 [Testcontainers](https://github.com/testcontainers) 构建，通过 Docker 容器创建更真实的测试环境，
    开发人员可以在将代码通过持续集成（CI）平台转移到生产环境之前自己测试应用程序，这使得云原生应用开发者无需专门应用测试团队的帮助即可测试依赖关系。

- [AWS 应用配置工具 AWS AppConfig 推出一个用于容器运行时的代理，简化 feature flag 和运行时的配置](https://rafay.co/press-release/rafay-launches-cost-management-service-to-deliver-real-time-visibility-and-allocation-of-kubernetes-cloud-costs/)

    AKS 等平台的用户可以使用 AWS AppConfig Agent 管理容器应用配置数据的检索和缓存，以及处理轮询和缓存逻辑等。
    feature flag 和运行配置功能允许用户无需部署新代码即可发布新的功能。
    此外，还具备配置安全功能，包括验证器、警报提醒，自动回滚配置等。

- [AWS 推出本地集群，用于在混合云服务 Outposts 上本地运行 EKS 集群](https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-eks-outposts-local-clusters/)

    本地集群减少了因云端网络中断而导致的应用停机风险。在此期间，应用程序仍然可用，并且可以执行集群操作。当连接到云时，EKS 管理 Outposts 上 K8s 控制平面的可用性。本地集群运行的 Kubernetes 与云上 EKS 功能相同，支持自动部署最新的安全补丁。

- [Azure 推出面向 AKS 的 Kubernetes 应用方案](https://mp.weixin.qq.com/s/Uk8t5pWoRiWmz1VL4nMOaQ)

    Azure Kubernetes 应用方案旨在助力合作方在微软 Azure 市场中创建、发布和管理商业商品化的 Kubernetes 解决方案的“工具箱”。
    Azure Kubernetes 应用方案支持利用现有 Helm Chart 打包，为 Kubernetes 应用方案创建捆绑包；
    仅需 48 小时即可创建和发布方案；自动进行安全扫描；全方位赋能销售增量。

- [Azure 混合云多云解决方案 Azure Arc 集成可观测平台 Datadog](https://mp.weixin.qq.com/s/YVUuFQLKe8DGADenZCKsyw)

    Azure Arc 与 Datadog 的集成提供了以下功能：监控连接状态和代理版本，确保 Azure Arc 启用的服务器、SQL 服务器和 Kubernetes 集群已连接且安全；将混合云和多云服务器、Kubernetes 集群和数据服务集成到一个统一仪表板中，实现跨环境的无缝管理；简化合规性的管理和跟踪，提供丰富的可视化效果和可操作告警。

- [Azure Serverless 容器平台 Azure Container Apps 十一月更新](https://azure.microsoft.com/en-us/updates/?query=azure%20container%20apps)

    更新内容：无需 Dockerfile 即从源代码构建容器镜像、可以使用 Azure pipeline 任务从 Azure DevOps 构建和部署容器应用、支持从GitHub Actions 工作流中构建和部署容器应用、支持按 IP 限制 Azure 容器应用的入站流量。

- [Azure Kubernetes 发行版 AKS 11 月更新](https://azure.microsoft.com/en-us/updates/?query=AKS)

    更新内容：支持基于 Azure Arc 在数据中心和边缘节点上运行轻量级 AKS、集成事件路由服务 Event Grid、最大节点限制增加到 5000 个、
    支持通过 Azure Active Directory 进行工作负载身份管理、推出 Kubernetes 应用市场、新增 CNI 插件 Azure CNI Overlay mode、启用基于 AMD 的机密虚拟机节点池。

- [Azure Container Apps (一款Serverless 容器运行时) 更新](https://azure.microsoft.com/en-us/updates/?query=azure%20container%20apps)

    更新内容：Dapr 组件支持通过托管身份验证后端服务提供者、支持 Dapr secrets API、集成监控服务 Azure Monitor。

- [Azure Kubernetes 发行版 AKS 10 月更新](https://azure.microsoft.com/en-us/updates/?query=AKS)

    更新内容：支持垂直 Pod 自动扩缩容（VPA）、支持下一代 Azure 磁盘存储 Premium SSD v2、新增镜像清理功能、支持开启 IPVS 负载均衡、
    简化数据库创建和身份管理、允许根据工作负载要求启/禁用 CSI 驱动、新增 Linux 发行版 Mariner 作为容器主机、Azure CNI Powered by Cilium 可用、支持 K8s 1.25、支持 Dapr 1.9。

- [Azure Kubernetes 发行版 AKS 9 月更新](https://azure.microsoft.com/en-us/updates/?query=AKS)

    更新内容包括：Azure 容器注册中心新增软删除功能，可恢复误删除的工件；允许中止 AKS 集群或代理池上的任何操作；支持多实例 GPU（MIG）；将 Azure 网络策略管理器（NPM）扩展到 Windows server 2022 的 AKS 集群；集成用于 AKS 私有集群的 API Server VNET。

- [Azure 轻量级 Kubernetes 发行版 AKS Edge Essentials 正式可用](https://azure.microsoft.com/en-us/updates/now-available-azure-kubernetes-service-edge-essentials/)

    AKS Edge Essentials 是 AKS 的本地 Kubernetes 实现，可以在资源有限的边缘设备上运行。它可以用来部署单节点和多节点的 K3s 和 K8s 集群，可以在现有的 Windows 设备上运行 Linux 和 Windows 工作负载。

- [Azure 发布 AKS 舰队管理器（公开预览版）](https://mp.weixin.qq.com/s/YVUuFQLKe8DGADenZCKsyw)

    Azure Kubernetes 舰队管理器将多个群集地视为单个集群来管理。用户可通过创建一个 Fleet 资源来管理多个集群。用户可将现有 AKS 集群当作成员集群，加入到舰队中，然后用这些集群的元数据，编排多个集群场景，如 Kubernetes 资源传播和多集群负载均衡。

- [阿里云服务网格 ASM 2023 年 3 月产品动态](https://mp.weixin.qq.com/s/Yca5J3liIg6oznZDz6fVrA)

    更新内容：网关支持对接 WAF、支持配置 Ingress 资源、支持 Knative 服务的管理、网格拓扑支持 OIDC 方式登录、Sidecar 代理支持超卖模式、新增出口流量策略、支持配置全局默认的 HTTP 请求重试策略。

- [阿里云 ACK 2 月产品更新](https://mp.weixin.qq.com/s/nqW681bqKocpc7AWUV56jg)

    更新内容：节点池支持 Kubelet 参数自定义功能、AIOps 支持 Service 诊断功能、支持变更云盘类型、支持使用 cloud-auto 类型云盘作为动态存储卷。

- [阿里云服务网格 ASM 2023 年 2 月更新](https://mp.weixin.qq.com/s/jNeC_gMQdCk8b8d3QXSeMQ)

    更新内容：支持以 Telemetry CRD 的方式定义管理日志、监控及链路追踪；支持网格全局及命名空间级别的细粒度配置；在 150 Pod 规模以上的集群中，网格拓扑加载速度提升；支持配置 sidecar 代理的环境变量、istio-proxy 线程数等；支持在多集群内配置集群内流量保持功能。

- [阿里云容器镜像服务 ACR 正式推出云原生制品中心](https://mp.weixin.qq.com/s/atQF7WNfeodW3eizw6e1tg)

    云原生制品中心为容器开发者免费提供来源于阿里云官方、龙蜥社区的安全可信容器基础镜像。
    包含应用容器化基础 OS 镜像、基础语言镜像、AI/大数据相关镜像类别，覆盖 ARM、ARM 64、x64、x86-64 多种系统架构。

- [阿里云微服务引擎 MSE 2022 年 12 月更新](https://mp.weixin.qq.com/s/j2si2vqTTcEugAWazpKL2A)

    更新内容：注册配置中心 zookeeper 支持导出快照和事务日志、云原生网关支持 HTTP/3、微服务洞察支持无损上下线过程中的日志采集以及关键节点信息展示。

- [阿里云服务网格 ASM 2022 年 12 月更新](https://mp.weixin.qq.com/s/4lODob6kB7xjYDaKACzmhw)

    更新内容：支持托管式的按需推送 xDS 配置、支持自建 Istio 社区版本迁移到 ASM、ASM 网关支持配置自定义授权服务、启用服务等级目标 SLO。

- [阿里云分布式云容器平台 ACK One 更新](https://mp.weixin.qq.com/s/TC1KA_xWpVAwZMFAgVmNfg)

    更新内容：集成 ArgoCD 实现多集群的 GitOps 持续交付，优化多集群应用分发；统一配置报警规则，支持配置特定集群的差异化报警规则，支持自动同步报警规则到新关联集群。

- [阿里云容器服务 ACK 云栖大会更新](https://mp.weixin.qq.com/s/cOObDVvnTGkX_hiAWv8mVA)

    更新内容：提供对 eRDMA 高性能容器网络的支持、基于新一代容器网络文件系统 CNFS 2.0 更好支持有状态应用的容器化、内建云原生混部系统 Koordinator 的产品化支持、发布 AIOps 套件和 FinOps 套件。

- [阿里云发布云原生技术中台 CNStack 2.0](https://mp.weixin.qq.com/s/5q8i_BSL8DbdwOUHmBkQ8Q)

    CNStack 2.0 支持不同厂商、不同架构、不同地域和 CPU/GPU 算力混合管理。提供应用开发、测试、运维全生命周期的一站式管理，场景覆盖容器服务、分布式应用、云边、DevOps。此外，平台还提供了完整的技术栈支持，包括内置的、开箱即用的产品组件和中间件以及原厂和合作伙伴提供的产品及组件。

- [阿里云微服务引擎 MSE 10 月更新](https://mp.weixin.qq.com/s/Puud_MYgCMezqKESaAiG-w)

    更新内容：注册配置中心提供迁移工具及方案、云原生网关服务来源支持 Serverless 应用引擎、认证鉴权支持多个规则并存、路由及服务详情页面新增QPS、错误、延迟等指标监控、全链路灰度及标签路由等能力支持 Consul 注册中心。

- [阿里云服务网格 ASM 9 月更新](https://mp.weixin.qq.com/s/tx7iHBzoelS-3xB0UWKK2A)

    更新内容：应用服务治理支持预热功能；支持以试运行模式应用安全策路；优化 sidecar 代理配置；“请求认证〞中新增多种 JWT 算法；支持通过外部授权接入 O1DC 协议服务；支持 K8s 1.24；AHPA 弹性预测支持基于 GPU 指标的预测；日志中心支持网络组件的日志和大盘展示；当 Pod 挂载 OSS 存储卷时，支持 I/O 可观测性。

- [阿里云容器服务 ACK 9 月更新](https://mp.weixin.qq.com/s/uI5sw-HwCJf56W9wDcmysw)

    更新内容：新增托管节点池、支持通过 Annotation 为 Service 配置网络配置型负载均衡 NLB 实例、为工作负载提供资源画像功能、支持使用容器网络文件系统对对象存储 OSS Bucket 进行生命周期管理。

- [阿里云服务网格 ASM 八月更新](https://mp.weixin.qq.com/s/BDgNctG90oHpbrRWC0Hxkg)

    更新内容包括：兼容 Istio 1.14 系列版本、支持 Kubernetes 1.21 - 1.24 版本、增强网格诊断功能、支持第三方令牌在 ACK 集群的兼容、支持用户自定义 EnvoyFilter、无需修改代码即可实现同可用区优先路由。

### B

- [Backslash Security 推出同名云原生代码可视化工具](https://www.backslash.security/post/backslash-security-emerges-from-stealth-to-fuse-code-security-with-cloud-native-context)

    Backslash 推出的可视化工具可以识别云原生代码中可能导致安全漏洞的工作流。
    具体功能包括：通过上下文可视化仪表盘，自动发现和映射云原生应用的代码及其依赖关系；根据生产中的应用云状况，自动确定高风险代码的优先次序；通过智能的自动风险识别，简化漏洞和风险的补救。
    该工具目前支持 AWS 环境和 GitHub 代码库。

- [BellSoft 推出 Alpaquita Cloud Native Platform，用于高效运行云原生 Java 应用](https://containerjournal.com/features/bellsoft-optimizes-java-for-cloud-native-platform/)

    [Alpaquita Cloud Native Platform](https://bell-sw.com/cloud-native-platform/) 利用适用于 Java 的 Linux 发行版、JVM 优化、多用途框架和原生镜像技术，提供了一个专为在容器中运行的 Java 应用而优化的运行时环境。该平台特性：云成本降低 20%，使用更小的 Pod，所需节点的数量减少；零迁移成本，不需要重构；效率提升 50%，实现低延迟、低成本、快启动。

- [博云容器云产品 BoCloud Container Platform v3.7 发布](https://mp.weixin.qq.com/s/K68IWq18YWkmMyyRte-OlQ)

    支持 x86 架构和 ARM 架构的混合管理、支持国产化数据库达梦、支持生产级 windows 容器、提供 ACK 和 TKE 公有云容器集群的统一资源纳管服务、支持同时发布多个原生 yaml 文件、支持原生 ingress 能力、将高性能虚拟机作为一种全新的资源类型进行独立管理、提供容器资源超分能力、完成容器云和微服务管理、服务网格、中间件等子产品的深度融合。

### C

- [Calico 云原生安全平台 Calico Enterprise 3.16 发布](https://www.tigera.io/blog/whats-new-in-calico-enterprise-3-16-egress-gateway-on-aks-service-graph-optimizations-and-more/)

    更新内容：egress 网关支持 Azure 和 AKS、支持通过 Tigera operator 部署 egress 网关、新增 Manager UI 用于启用和配置基于工作负载的 Web 应用防火墙、Kubernetes 工作负载的可视化范围扩展至 100 多个命名空间、允许来自不同命名空间的 pod egress 到不同的外部网络。

- [Calico 云原生应用安全平台 Calico Enterprise 3.15 发布](https://www.tigera.io/blog/whats-new-in-calico-enterprise-3-15-fips-140-2-compliance-new-dashboards-egress-gateway-pod-failover-and-more/)

    版本特性：支持将 Calico Enterprise 配置为符合 FIPS 140-2 的模式，FIPS 140-2 规定了应用程序和环境的加密模块需满足的安全标准；提供了一个基于工作负载的 IDS/IPS（入侵检测/入侵防御）系统，根据全球威胁情报源数据库检测并阻止不良工作负载的访问；自动化命名空间的安全策略建议；提供基于命名空间的仪表盘；支持出口网关 pod 的故障检测和故障转移。

- [Canonical K8s 发行版 Charmed Kubernetes 1.26 发布](https://canonical.com/blog/canonical-kubernetes-1-26-is-now-generally-available)

    版本特性：增加 Kube-OVN BGP 支持，实现从外部网络访问 pod IP；支持为 Kube-OVN 配置流量镜像；metallb-controller 和 metallb-speaker 可以部署到更多的架构上（AMD64、ARM、ARM64 等）；集成策略引擎 OPA gatekeeper。

- [CAST AI Kubernetes 成本优化&自动化平台 1 月更新](https://cast.ai/release-notes/#january-2023)

    更新内容：新增 CAST AI kVisor 安全代理，用于评估安全漏洞和和分析集群配置的安全性；改进创建新节点时使用 AKS 镜像的方式；提供每天的 CPU 使用数据以及计费 CPU 数量；改进自动缩放功能。

- [CAST AI Kubernetes 成本优化&自动化平台十一月更新](https://cast.ai/release-notes/#november-2022)

    更新内容：集群再平衡后可以配置最小节点数、为 EKS 用户增加使用存储优化节点进行自动缩放的支持、节点模板支持备选（Fallback）功能、增加对 EKS 和 GKE 集群的 ARM 节点支持。

- [Chainguard 云原生供应链安全平台  Chainguard Enforce 更新](https://www.chainguard.dev/unchained/chainguard-enforce-announces-new-software-signing-capability)

    更新内容：提供基于 Sigstore 的无密钥签名模式、增加一个开箱即用的安全策略库、支持用户通过其 Gitlab 账号登录、支持 CloudEvents、支持细粒度的 Kubernetes 工作负载对象的策略、增强大规模集群用户的稳定性。

- [CloudCasa 基于 Velero 的企业级 Kubernetes 数据保护方案 CloudCasa for Velero](https://www.catalogicsoftware.com/press-releases/introducing-cloudcasa-for-velero-to-manage-and-run-kubernetes-backups-at-enterprise-scale/)

    CloudCasa for Velero 为企业和服务提供商提供了在所有 Kubernetes 发行版以及混合云和公有云环境中对 Velero 备份进行多集群管理的能力。
    开发人员和平台工程师可以通过策略驱动的模板和引导式恢复功能，在控制台管理和监控基于 Velero 的备份。
    Velero 用户可以订阅 CloudCasa 服务，并将其现有设置编入目录，以便在几分钟内进行集中管理。

### D, E

- [D2iQ 推出专为政府部门设计的 Kubernetes 平台 DKP Gov](https://d2iq.com/blog/dkp-gov-kubernetes-management-platform)

    DKP Gov 基于 D2iQ Kubernetes 平台 (DKP)创建，旨在满足政府、军事和民用机构对创新技术的需求。
    DKP Gov 支持物理和逻辑上隔离的节点，支持集中式多云平台、多节点 fleet 管理，符合联邦信息处理标准 (FIPS) 140-2 认证等。

- [D2iQ Kubernetes Platform v2.4.0 发布](https://docs.d2iq.com/dkp/2.4/dkp-2-4-0-features-and-enhancements)

    该版本主要新特性：支持在本地和物理隔离环境中运行 GPU 节点、支持红帽企业 Linux 系统、Rook Ceph 替代 MinIO 成为平台的默认存储、集成 Trivy 等第三方扫描工具。

- [D2iQ Kubernetes Platform v2.3 发布](https://docs.d2iq.com/dkp/2.3/2-3-release-notes)

    该版本主要新特性：支持 Kubernetes 1.23、支持多集群环境下的应用配置和部署、支持 Amazon EKS 和 GCP、支持多可用区、支持为每个集群配置自定义域名和证书、增加自助式故障排除能力。

- [DaoCloud Enterprise 5.0 发布](https://mp.weixin.qq.com/s/7UkIwCp78trO126XQxEL6A)

    DaoCloud Enterprise 5.0 是自主开放、高性能、可扩展的新一代云原生操作系统。围绕云原生底座延伸能力场景，打通云边壁垒，跨越多云环境，解决信创基础设施兼容难题，提升应用交付效能，使能应用敏捷创新，丰富的数据服务赋能业务系统，融合微服务治理和全局可观测应对庞大业务系统运维管理挑战。

- [Databend 发布云原生数据仓库 Databend Cloud](https://mp.weixin.qq.com/s/LzjRQ8_XA-896AZQj2n3hA)

    Databend Cloud 是基于开源云原生数仓项目 [Databend](https://github.com/datafuselabs/databend) 打造的弹性云数仓，由 3 层组成：存储层、计算层和元信息服务。底层基于对象存储，上层计算节点采用不同的规格，最上层是元数据和管理集群，实现多租户的隔离，保证用户的数据安全。

- [Datadog 推出云安全平台 Cloud Security Management](https://www.datadoghq.com/about/latest-news/press-releases/datadog-launches-cloud-security-management-to-provide-cloud-native-application-protection/)

    Cloud Security Management 将云安全态势管理、云工作负载安全、警报、事件管理和报告等功能集中在一个平台上，开发和安全团队能够借此识别错误配置、检测威胁并确保云原生应用的安全。

- [Docker 发布技术预览版 WebAssembly 工具](https://www.docker.com/blog/docker-wasm-technical-preview/)

    现在，Docker 允许用户使用容器和 Wasm 工件构建云原生应用，将 Wasm 视为 Linux 容器的补充性技术。
    此外，Docker Engine 继续使用与整体生态系统相统一的 containerd 容器运行时，只不过把负责容器进程运行的 runC 替换成了 WasmEdge 运行时。

- [Docker Desktop v4.12.0 发布](https://www.docker.com/blog/integrated-terminal-for-running-containers-extended-integration-with-containerd-and-more-in-docker-desktop-4-12/)

    该版本主要新特性：集成 containerd，使用 containerd 来管理和存储镜像；允许直接通过 Docker 仪表盘在运行的容器中执行命令。

- [Dynatrace SaaS v1.250 云监控平台发布](https://www.dynatrace.com/support/help/whats-new/release-notes/saas/sprint-250)

    该版本主要新特性：支持检测 Go 应用中的第三方漏洞、在Kubernetes 命名空间页中新增一个 “Kubernetes services” 列、支持通过 service、service name 或 service type 筛选 pod。

- [Dynatrace 利用人工智能引擎 Davis AI 提供 Kubernetes 根因分析](https://www.dynatrace.com/news/blog/root-cause-analysis-in-kubernetes-with-davis-ai/)

    Davis AI 因果分析引擎为 Kubernetes 性能问题及其对业务连续性的影响提供根因分析。具体功能：自动化根因分析、支持实时跟踪 Kubernetes 的编排流程、将性能问题与 Pod 驱逐联系起来、支持根据工作负载部署清单的变化来识别与错误配置有关的性能下降问题的原因。

- [Ermetic 云原生应用保护平台支持 Kubernetes 安全态势管理](https://ermetic.com/news/ermetic-adds-kubernetes-security-posture-management-to-cloud-native-application-protection-platform/)

    Ermetic 云原生应用保护平台的 Kubernetes 安全姿势管理功能支持自动发现和修复 Kubernetes 集群中的错误配置、合规性违规以及风险或过度特权。
    它提供了所有 Kubernetes 集群内部资源的详细清单，能够持续执行安全态势评估和风险优先级排序，并提供补救方法和工作流集成。

### F

- [F5 发布中国版容器 Ingress 服务 CIS-C](https://mp.weixin.qq.com/s/4BuiZC8AEnRt-lwT7dNyxg)

    CIS-C 是一款将 Kubernetes 集群内服务通过 F5 BIG-IP 进行自动化发布的控制器软件。
    帮助用户打通 Kubernetes 集群与外部入口，将 BIG-IP 应用交付能力集成到 Kubernetes 技术栈的云环境中。
    它实现了多团队合作，用户可以灵活地、自动化地创建、变更应用或者服务入口策略。

- [Fairwinds 的 Kubernetes 治理和安全平台 Fairwinds Insights 十一月更新](https://www.fairwinds.com/blog/fairwinds-insights-release-notes-10.2-10.6-spotlight-on-workload-cost-allocation)

    更新内容：增加工作负载成本分配功能，允许查看一组工作负载的历史成本；优化成本页面，细化 Kubernetes 集群成本的分类；支持查看成本随时间变化的动态。

- [Finout 推出无代理 Kubernetes 成本治理套件](https://www.businesswire.com/news/home/20230413005018/en/Finout-Announces-Agentless-Cost-Governance-Suite-for-Kubernetes)

    该无代理成本治理套件可以在跨各大云平台使用 Kubernetes 时自动检测和管理云浪费，预测支出并保持预算。其提供统一的 MegaBill 仪表盘，管理跨多个云平台的成本，并提供 Kubernetes 支出的上下文信息；支持设置 Kubernetes 部署的预算和未来支出；支持识别跨 Kubernetes 和云服务的支出异常；提供成本优化实时建议。

- [Fortinet 发布云原生防火墙服务 FortiGate CNF](https://www.fortinet.com/blog/business-and-technology/simplify-cloud-security-with-the-fortigate-cloud-native-firewall-on-aws)

    FortiGate CNF 是一个 SaaS 产品，通过与 AWS Gateway Load Balancer、AWS Firewall Manager 等服务的深度云原生集成，支持不同 AWS 环境下的一致安全策略，消除了网络安全的复杂性。此外，还支持下一代防火墙的安全检查功能，提供对应用层的深度可视性，可以保护多个账号、子网、虚拟私有云和可用性区域。

### G

- [GitLab 15.7 发布](https://about.gitlab.com/releases/2022/12/22/gitlab-15-7-released/)

    版本特性：支持将私有化部署的 GitLab 实例部署到 Jira 云、支持 SSH 密钥签署提交文件、支持显示每条流水线的多个代码质量扫描报告、允许在个人命名空间内共享 Kubernetes GitLab 代理的 CI/CD 访问权、支持在默认分支以外的地方进行 GitOps 部署。

- [GitLab 15.5 发布](https://mp.weixin.qq.com/s/AiRU9pQUxTex0F_XvuHiHg)

    该版本主要新特性：在合并请求流水线中运行安全扫描工具、支持 Kubernetes 容器扫描、支持从 GitHub 导入项目时导入更多的关系、新增预定义 DORA（评估 DevOps 效能水平的指标）可视化比较报告。

- [GitLab 15.4 发布](https://about.gitlab.com/releases/2022/09/22/gitlab-15-4-released/)

    该版本主要新特性：改进 VSCode CI/CD 集成功能、支持 Gitee 项目导入、专业版支持测试管理、支持 DORA 指标用于评估企业 DevOps 效能、集成 Harbor 镜像仓库。

- [Gloo Mesh v2.1 服务网格管理平台发布](https://www.solo.io/blog/announcing-gloo-mesh-2-1/)

    该版本主要新特性：增加资源状态和调试页面、优化 Istio 生命周期管理、支持零信任访问策略、东西向流量的 TLS 终端问题修复、支持用同一个 Helm chart 安装代理和管理集群。

- [Gloo Gateway 云原生 API 网关支持 GraphQL](https://www.solo.io/blog/announcing-graphql-for-gloo-gateway/)

    GraphQL for Gloo Gateway 无缝地将 GraphQL API 添加到 Gloo Gateway 中。用户可以借此对 API 进行联合 GraphQL 查询，而不需要为 GraphQL 建立额外的服务器以及解析器和解析器模式库；所有策略和请求都可以在 Envoy Proxy 过滤器中进行管理；同时支持声明式配置，与 CI/CD 和 GitOps 工作流完全兼容。

- [Google Cloud GKE 引入 Network Function Optimizer，助力电信运营商采用云原生网络功能](https://cloud.google.com/blog/topics/telecommunications/network-function-optimizer-for-gke-and-gdc-edge)

    Network Function Optimizer on GKE 主要提供三个方面的能力：
    通过 Kubernetes 原生的多网络实现云网络的现代化，为 Kubernetes 集群定义了一个网络目录，允许 Pod 根据连接性或性能需求，将一个接口附加到一个或多个网络；
    基于软件的高性能数据平面加速，云原生网络功能（CNF）可以在任何 Pod 上进行调度，消除网络功能和底层网卡之间的依赖性；
    流量定向能力，简化流量分类，支持将一组 Pod 定义为下一跳（nexthop）。

- [Google Cloud Kubernetes 发行版 GKE 12 月更新](https://cloud.google.com/kubernetes-engine/docs/release-notes)

    更新内容：允许在 Autopilot 集群中运行基于 GPU 的工作负载；支持双栈集群；支持在多 GPU 工作负载上启用传输层插件 NCCL Fast Socket，提高英伟达集体通信库（NCCL）的性能；GKE 网关控制器支持全局外部 HTTP(S) 负载均衡器。

- [Google Cloud Kubernetes 发行版 GKE 十一月更新](https://cloud.google.com/kubernetes-engine/docs/release-notes)

    更新内容：K8s 控制平面日志正式可用；支持使用弃用 insight 来识别 1.23 及更老版本的集群；Autopilot 集群支持紧凑型放置策略，以及当某个节点有问题时，支持向 GKE 发出信号；单集群 GKE Gateway 正式可用；创建 LoadBalancer 服务时，谷歌云控制器会自动创建防火墙规则并应用到 GKE 节点上。

- [Google 发布云原生文件存储服务 Filestore Multishares for GKE](https://cloud.google.com/filestore/docs/multishares)

    Filestore 是一个文件存储托管服务，Filestore 实例是一个网络附属存储（NAS）托管系统。
    Filestore Multishares for GKE 为 GKE 实例提供了文件存储服务，其主要功能包括：支持区域性存储，防止区域故障；
    一个 Filestore Enterprise 实例上可分配多达 10 个 share，每个 share 映射到 GKE 中唯一的持久卷；支持动态卷配置，可根据需要增加或减少 share 和实例的容量。

- [Google 发布 Kubernetes Gateway API 的企业级实现 GKE Gateway Controller](https://cloud.google.com/blog/products/containers-kubernetes/google-kubernetes-engine-gateway-controller-is-now-ga)

    GKE Gateway Controller GKE 提供了一个可扩展的 API 来管理内外部的 HTTP(S) 负载均衡。
    其主要功能包括：提供了一个多路由/租户共享的网关、默认提供两个 GatewayClass 即 Global external 和 Regional Internal 负载均衡、支持大规模的端到端加密、支持定制后端服务属性、提供高级流量管理等。

- [Google 服务网格 Anthos Service Mesh 更新](https://cloud.google.com/release-notes#September_07_2022)
  
    更新内容包括：支持使用 Fleet Feature API 自动配置 Anthos Service Mesh、支持通过托管数据平面自动升级数据平面代理。

- [Google 混合云自动化配置工具 Anthos Config Management 更新](https://cloud.google.com/release-notes#September_15_2022)

    更新内容包括：配置同步功能可作为 OCI 镜像同步存储在 Google Artifact Registry 或 Container Registry 中、Config Sync 支持从私有 Helm 仓库同步、支持用户提供的 CA 证书用于验证 Git 服务器的 HTTPS 连接、新增约束模板 K8sStorageClass。

- [Grafana Cloud 观测平台集成 Cilium Enterprise，加强 Kubernetes 网络监控](https://grafana.com/blog/2022/11/17/introducing-the-cilium-enterprise-integration-in-grafana-cloud-for-kubernetes-network-monitoring/)

    集成后，可以将 Cilium Enterprise 中部署的数据输送到 Grafana Cloud。
    Grafana Cloud 提供四个预制的仪表盘：Cilium 总览、Hubble 总览、Cilium operator 和 Cilium Agent。还提供了 17 条告警规则，用于监测与 Cilium Agent 和 Kubernetes 集群状态相关的 Cilium 核心组件。

- [Grafana Cloud 推出业内首个性能测试和分布式追踪的集成](https://grafana.com/blog/2022/11/03/how-to-correlate-performance-testing-and-distributed-tracing-to-proactively-improve-reliability/)

    Grafana Cloud 引入负载测试项目 [k6](https://github.com/grafana/k6) 和分布式追踪后端 [Tempo](https://github.com/grafana/tempo)（k6 x Tempo）的集成，
    缩小性能测试的黑盒数据和系统内部白盒数据之间的差距。
    该集成允许关联 k6 的测试运行数据和服务器端的追踪数据，从而进行根本原因分析；汇总收集的追踪数据以生成实时指标，帮助用户缩小搜索空间并快速发现异常行为。

### H, K, L

- [Harness 推出全托管 GitOps-as-a-Service](https://harness.io/blog/generally-available-harness-gitops-as-a-service)

    Harness GitOps-as-a-Service 基于 Argo CD 构建，集成 OPA，支持审计跟踪，提供细粒度的 RBAC，支持不同部署的统一单点登录，支持声明式设置，提供集中的 GitOps 控制中心用于管理和查看多个环境中的部署情况，支持与已有的 Argo CD 实例集成。

- [华为云发布分布式云原生产品——容器 CCE Turbo 和分布式云原生 UCS (Ubiquitous Cloud Native Service)](https://mp.weixin.qq.com/s/Bm_kFuyK3uLaSb4AvcYdmA)

    CCE Turbo 可通过计算、网络、调度全方位加速，实现极致弹性，如帮助客户以 3000 pod/min 的弹性轻松应对业务流量洪峰；UCS 提供跨云、跨地域的云原生应用管理，实现一致体验。

- [火山引擎发布分布式云原生平台 DCP](https://mp.weixin.qq.com/s/Fz7R8R0keKFEryq8zQKFoA)

    [DCP](https://www.volcengine.com/product/dcp) 是面向多云多 Kubernetes 集群场景的企业级云原生统一管理平台，提供多云集群统一管理与运维、应用跨集群分发、统一流量管控等能力。DCP 将火山引擎容器集群、第三方集群、自建集群等统一纳管与运维；基于集群联邦等技术，提供跨集群、跨云的弹性调度能力；提供多集群服务发现、多集群统一入口访问等能力；可基于备份数据进行应用数据恢复及跨集群/云应用迁移。

- [Kong 云原生 API 平台 Kong Enterprise 3.2 发布](https://konghq.com/blog/kong-enterprise-3-2)

    更新内容：当控制平面出现故障时，支持数据平面扩展；新增 Datadog 追踪插件，无需安装 Otel 收集器即可与 Datadog Agent 协同工作；支持基于时延的引导，允许 Kong 负载均衡器在代理上游服务时根据总响应时间选择“最快”的后端。

- [Kong 服务网格产品 Kong Mesh v2.1 发布](https://konghq.com/blog/kong-mesh-kuma-2-1)

    更新内容：完成所有下一代策略的实现，包括增加 MeshHTTPRoute、MeshCircuitBreaker、MeshFaultInjection、MeshOPA 等策略；在用户界面中增加了网关视图；支持在 eBPF 模式下配置端口。

- [Kong Gateway v3.0 云原生 API 网关发布](https://docs.konghq.com/gateway/changelog/#3000)

    该版本主要新特性：提供联邦信息处理标准 FIPS 包以满足安全和合规性要求、支持选择插件的执行顺序、增加对 WebSocket 流量的本地支持、新增 OpenTelemetry 插件、引入新路由引擎用于处理复杂路由要求、吞吐量、延迟及内存消耗等性能显著优化。

- [Kyndryl 推出多云云原生应用迁移和优化方案 Cloud Native Services](https://www.kyndryl.com/gb/en/about-us/news/2022/12/kyndryl-cloud-native-services-digital-modernization)

    Kyndryl Cloud Native Services 提供了一个端到端的生命周期框架，
    这个框架包括云原生应用迁移和优化所需的代码资产、工作流、专业基础知识、咨询管理服务，
    以及与自动备份、补丁、KPI 监测、安全、告警和事件管理相关的综合服务。
    该方案允许企业将其内部应用转移到云服务提供商的环境上，如 AWS、GCP 和 Azure。

- [Lacework Platform 云安全平台十一月更新](https://docs.lacework.com/releases/2022-11-platform-releases)

    更新内容：平台扫描器支持多架构的容器镜像、提供攻击路径分析功能、无代理工作负载扫描功能普遍可用、在不活动的主机内核上发现的漏洞会自动被标记为例外、CIS GCP 1.3.0 基准报告和策略普遍可用、新增主机策略用于检测反向 shell 连接和加密劫持工件。

- [Lacework Platform 云安全平台 9 月更新](https://docs.lacework.com/releases/2022-09_september-platform-releases)
  
    更新内容包括：支持无代理工作负载扫描、支持对 AWS 上的 Linux 主机进行主机漏洞评估、支持容器镜像漏洞评估。

- [Logz.io 发布 K8s 全栈观测平台 Kubernetes360](https://logz.io/blog/unified-observability-kubernetes-360/)

    Kubernetes360 将日志、Prometheus 指标监控和 Jaeger 支持的分布式追踪统一在一个平台中，使 DevOps 团队能够以简单、高效和可操作的方式监控应用 SLO。

### M, N, O

- [Mirantis 容器运行时 Container Runtime 23.0 发布](https://www.mirantis.com/blog/announcing-the-23-0-major-release-for-mirantis-container-runtimeand-moby)

    更新内容：实验性地支持 CSI；增强 OCI运行时支持，支持  Kata Containers 和 gVisor；执行健康检查所需的开销不再计入时间阈值，即使容器负载大，健康检查所需的时间也不会增加；默认使用镜像构建工具 BuildKit。

- [Mirantis 私有云基础设施平台 Mirantis OpenStack for Kubernetes 22.5 发布](https://www.mirantis.com/blog/mirantis-openstack-for-kubernetes-22-5-released)

    版本特性：全面支持 OpenStack Yoga、引入了基于 OpenStack Manila 的共享文件系统、通过 MetalLB 启用 BGP 模式使 OpenStack 云更容易集成到 L3 网络。

- [Mirantis 企业级容器平台 Mirantis Kubernetes Engine v3.6 发布](https://www.mirantis.com/blog/mke-3-6-release)

    该版本主要新特性：支持 Kubernetes 1.24、支持谷歌云平台 GCP、支持 cri-dockerd 取代 Dockershim、安全准入控制更新（提供 OPA gatekeeper 作为 PSP 的可选替代方案）。

- [Spot by NetApp 推出 Kubernetes 应用持续交付产品 Ocean CD](https://www.qualys.com/docs/release-notes/qualys-container-security-1.21-release-notes.pdf)

    Ocean CD 是一个支持多集群的 SaaS 方案，以 Argo rollouts 为引擎，并在上面叠加许多管理功能。
    Ocean CD 允许快速启用智能部署，如金丝雀、蓝绿部署或使用验证和失败策略的简单滚动更新；支持持续验证，根据金丝雀策略定义正确执行回滚和自动行动；提供一个开发者友好型的 UI 界面。

- [NetApp Kubernetes 应用数据管理方案 Astra Control 更新](https://www.netapp.com/blog/astra-kubernetes-data-protection/)

    更新内容：
    支持为多个命名空间设置一个应用数据保护策略；
    扩大集群范围内资源的检测和保护范围；
    基于标签和标签选择器允许每个命名空间有多个应用程序；
    K8s 应用现在可以在不同的项目、订阅或账号托管的集群间进行故障转移；
    集成轻量目录访问协议 LDAP；
    支持更多 Self-managed K8s 平台。

- [Ocean 推出 Kubernetes 网络成本分析解决方案 Network Cost Analysis](https://spot.io/blog/dont-sweat-the-network-costs-ocean-provides-application-cost-visibility-to-your-kubernetes-cluster/)

    Network Cost Analysis（AWS EKS 集群上已提供 beta 支持）不仅支持显示 Kubernetes 应用使用的网络费用和带宽消耗，还支持预测未来支出和使用趋势。

- [Ondat 云原生块存储平台 Ondat v2.10 发布](https://docs.ondat.io/docs/release-notes/#2100---release-2023-04-01)

    更新内容：支持通过 storageoscluster 资源为大部分 Ondat pod 设置容器资源限制、支持实时计算平台 Red Hat Enterprise Linux for Real Time、operator 默认安装 CLI pod、允许在节点之间移动卷。

- [Ondat v2.9 云原生块存储平台发布](https://www.ondat.io/blog/ondat-launches-version-2.9)

    该版本主要新特性：支持在零停机的情况下调整卷的大小、通过存储池可以控制工作负载所使用的存储类型、允许定义卷的拓扑结构。

- [Oracle Kubernetes 发行版 Container Engine for Kubernetes 支持虚拟节点池和虚拟节点](https://docs.oracle.com/en-us/iaas/releasenotes/changes/c3688114-0104-40b0-aece-67169868f990/)

    虚拟节点提供了 serverless Kubernetes 的体验，用户无需管理、扩展、升级和排障节点基础设施，即可规模化运行容器化应用程序。虚拟节点提供了细粒度的 pod 级别弹性和按使用量计费的定价。用户可以通过在增强的集群中创建虚拟节点池以创建虚拟节点。

- [OutSystems 发布云原生低代码开发解决方案 OutSystems Developer Cloud (ODC)](https://mp.weixin.qq.com/s/yx63Um3ju1mC-qNF9_GJkw)

    ODC 是用于构建云原生应用程序的高性能低代码解决方案。
    ODC 将 Kubernetes、Linux 容器、微服务和 AWS 原生云服务与 DORA 高性能级 CI/CD、企业级安全性以及基于模型的可视化开发相结合。
    支持大规模交易量和数据需求，通过高级可视化编程和人工智能提高开发人员生产力，实现高性能 CI/CD 实践。

### P

- [PerfectScale 推出同名 Kubernetes 成本管理 SaaS 平台](https://www.perfectscale.io/blog/perfectscales-saas-platform-is-now-available)

    PerfectScale 是业界首个专门为提高 K8s 环境的持久性和成本效益而建立的持续优化方案。
    通过人工智能算法来评估使用模式和性能和成本指标，该平台提供了多集群、多云的可观测性，支持弹性和性能风险检测、资源浪费检测，
    支持问题优先级排序，提供 GitOps 友好的的补救措施建议，支持预测系统变化对环境的影响等。

- [Portworx Enterprise 2.12 云原生数据管理平台发布](https://docs.portworx.com/release-notes/portworx/#2-12-0)

    该版本主要新特性：本地用户可以启用 PX-Fast 功能，使用高性能存储作为 Kubernetes 的持久化存储；允许存储管理员使用自定义的 Kubernetes 对象为对象存储桶提供各种支持服务；自动生成 Vault 令牌，在 Vault 中存储加密 secret 和云证书；允许 Kubernetes 资源迁移到目标集群之前对其进行修改。

- [Portworx Backup v2.3 数据备份产品发布](https://portworx.com/blog/announcing-portworx-backup-2-3-for-simpler-backup-management-and-flexible-licensing/)

    该版本主要新特性：支持与其他用户和组共享备份、支持根据特定的基础设施定制备份许可证、支持使用用户提供的或默认的密钥为不同类型的备份提供加密支持。

### Q

- [青云发布 KubeSphere 容器平台企业版 3.4.0](https://mp.weixin.qq.com/s/spjVK8jWtXYb53aYjMWFxw)

    更新内容：支持 Prometheus 内部 TLS 认证访问、内置集成 HPA 扩展插件 KEDA、新增企业空间级网关与租户级存储配额、提升资源别名展示权重、支持通过 UI 配置 Whizard 可观测中心。

- [青云企业云平台 v6.1 版本正式发布](https://mp.weixin.qq.com/s/tNx1neUN5B9auBqp_Fpy3A)

    更新内容；新增监控巡检功能；新增企业空间功能，涵盖组织管理、用户管理、配额管理、资源管理、流程审批等空间管理模块；新增对第三方存储的支持；提供 VMware vSphere 纳管工具；QKE 容器引擎支持裸金属服务器作为集群 Worker。

- [青云发布云原生虚拟化平台 KSV 1.6](https://mp.weixin.qq.com/s/XxOWJdLRHS2s_Ev_N9qEgw)

    版本特性：统一管理与展示所有计算、存储和网络资源；支持 KSV 和 KubeSphere 融合部署，实现虚拟机和容器共存共管；基于 KubeVirt，支持以虚拟资源池的方式交付 CPU、存储等物理资源，并实现统一的管理、分配及调度，支持同时创建相互隔离的虚拟机环境；集成 Kube-OVN，实现了 Underlay & Overlay 的网络。

- [青云发布分布式多租户云原生操作系统 KubeSphere 企业版 3.3](https://mp.weixin.qq.com/s/ZuiY-la34DvHW5bQdc9q7Q)

    版本特性：新增可观测中心，汇总同步分散在各个集群的数据；重构集群监控页面，聚焦资源分配；优化租户监控，支持展示租户配额设置情况等；新增对微服务框架 Spring Cloud 的支持；集成 Argo CD 支持 GitOps。

- [Quali 基础设施自动化方案 Torque 更新，简化 Kubernetes 基础设施管理](https://www.quali.com/blog/quali-simplifies-cloud-infrastructure-management/)

    更新内容包括：支持检测 Helm Chart 漂移、支持自动收集 Kubernetes 主机成本、收集的数据可以导入第三方审计工具、提供对环境定义的所有子组件的可见性。

- [Qualys 容器安全工具 Qualys Container Security v1.22 发布](https://www.qualys.com/docs/release-notes/qualys-container-security-1.22-release-notes.pdf)

    更新内容：镜像漏洞报告支持显示与镜像相关的标签、容器漏洞报告支持显示镜像仓库信息和 Kubernetes 对象信息、支持扫描所有注册表中的所有镜像、软件成分分析（SCA）扫描增加对编程语言 PHP、Ruby 和 Rust 的支持。

- [Qualys 容器安全工具 Qualys Container Security v1.21 发布](https://www.qualys.com/docs/release-notes/qualys-container-security-1.21-release-notes.pdf)

    更新内容：支持为普通和 CI/CD 传感器提供传感器配置文件、支持在传感器配置文件中定义传感器配置、在自动注册表扫描时允许扫描所有镜像。

### R

- [Rafay Systems 推出 Environment Manager，优化 Kubernetes 开发者体验](https://rafay.co/press-release/rafay-introduces-environment-manager-to-automate-environment-provisioning-and-accelerate-modern-application-deployment-from-code-to-cloud/)

    Environment Manager 通过为全栈环境提供自助服务功能，改善开发者体验。开发人员能够从平台团队策划、测试和持续管理的环境蓝图中配置现代应用堆栈。通过和 Rafay 的 Kubernetes 运维平台集成，Environment Manager 抽象了底层基础设施的复杂性，减少了配置和访问 Kubernetes 的环境所需的时间。

- [Rafay Systems 发布 Kubernetes 成本管理服务](https://rafay.co/press-release/rafay-launches-cost-management-service-to-deliver-real-time-visibility-and-allocation-of-kubernetes-cloud-costs/)

    成本管理服务是 Rafay Kubernetes 运维平台的一部分，可为位于公有云和内部数据中心的集群提供 Kubernetes 云成本优化。
    其支持实时查看云计算支出；与 RBAC 预集成，提供基于角色的成本指标的可见性和访问权；可集中查看多个公有云账号和内部数据中心的集群；可根据资源消耗优化云预算。

- [Rafay Systems 推出 Service Mesh Manager and Network Policy Manager，提供企业级的 K8s 流量管理和通信安全保障](https://rafay.co/press-release/rafay-launches-service-mesh-manager-and-network-policy-manager-for-enterprise-grade-traffic-management-and-transport-security-for-kubernetes/)

    Service Mesh Manager 基于 Istio 构建，为微服务团队提供集中的安全控制和流量管理策略配置。Network Policy Manager 基于 Cilium 构建，提供集中管理以及 pod 和命名空间通信的可见性，以隔离边界并减少集群的横向攻击面。

- [Red Hat OpenShift 日志管理方案 Logging 5.6 发布](https://docs.openshift.com/container-platform/4.12/logging/cluster-logging-release-notes.html#cluster-logging-release-notes-5-6_cluster-logging-release-notes-v5x)

    更新内容：兼容 OpenShift 容器平台集群范围内的加密策略；支持通过 LokiStack 自定义资源声明租户、流和全局策略保留策略，并按优先级排序；新增日志转发输出选项 Splunk；Vector 取代 Fluentd 作为默认收集器。

- [Red Hat 多集群管理平台 Advanced Cluster Management for Kubernetes 2.7 发布](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.7/html/release_notes/red-hat-advanced-cluster-management-for-kubernetes-release-notes)

    更新内容：支持根据依赖关系进行策略执行排序、策略生成器支持引用本地和远程定制配置、扩大边缘可管理的集群数至 3500 个、支持在 Arm 架构上创建集群、针对大规模环境的搜索组件正式可用、支持使用新的 Submariner LoadBalancer 模式简化集群部署、Submariner 支持无网络环境的集群。

- [Red Hat 云原生 CI/CD 解决方案 OpenShift Pipelines 1.9 发布](https://docs.openshift.com/container-platform/4.11/cicd/pipelines/op-release-notes.html#op-release-notes-1-9_op-release-notes)

    更新内容：Pipelines as Code 正式可用，支持在源代码库中定义 Tekton 模板；支持存储库 CRD 的并发限制；支持对管道中的 URL 进行认证；新增 Resolvers 功能用以“解决”远程任务和管道的请求；新增 CLI 工具 `opc`。

- [Red Hat OpenShift Container Platform 4.12 发布](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.12/html/release_notes/ocp-4-12-release-notes)

    更新内容：使用 OVN-Kubernetes 网络插件作为默认网络插件；新增拓扑感知的生命周期管理器用于管理多个单节点 OpenShift 集群的部署和升级；支持通过 cgroup v2 优化资源分配管理；支持快速、低内存占用的 crun 容器运行时；针对断网环境优化基于代理的安装器；支持管理节点层面的防火墙配置；支持根据集群中的指标动态扩展默认的 Ingress 控制器；支持为 SR-IOV 设备配置多网络策略；支持 Serverless function 功能；新增 OpenShift Network Observability Operator 进行网络排障；新增 Security Profiles Operator 改善安全态势；支持将生产级 Kubernetes 部署到边缘设备上。

- [Red Hat 容器镜像仓库 Red Hat Quay v3.8.0 发布](https://access.redhat.com/documentation/en-us/red_hat_quay/3.8/html/red_hat_quay_release_notes/index)

    该版本新特性：支持 IPv6 单栈和 IPv4/IPv6 双栈、用户必须拥有自签名的证书才能使用 SAN（Subject Alternative Name）、Quay 管理员可以使用存储配额来限制缓存的大小、新用户类型“受限用户”、超级用户经配置可以对系统中的所有内容拥有完全控制权。

- [Red Hat OpenShift Service Mesh 2.3 发布](https://cloud.redhat.com/blog/introducing-openshift-service-mesh-2.3)

    该版本主要新特性：支持 Istio v1.14、支持通过注入 deployment 实例来创建和管理网关、新增集群范围的拓扑结构、增加 OpenShift 服务网格控制台 operator、支持 Istio 可视化工具 Kiali 1.57。

- [Red Hat Openshift 日志管理服务 Logging 5.5 发布](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.11/html/logging/release-notes#cluster-logging-release-notes-5-5-0)

    该版本主要新特性：支持把同一 pod 内不同容器的结构化日志转发给不同的索引、使用 Kubernetes 通用标签过滤带有 Elasticsearch 输出的日志、日志聚合 Loki Operator 和 观测数据收集Vector collector 正式可用。

### S

- [ServiceNow 发布统一查询语言 Lightstep UQL，扩展 Kubernetes 应用的可见性](https://lightstep.com/blog/announcing-the-lightstep-unified-query-language)

    Lightstep UQL 支持统一的“可观测性即代码”，通过单一查询语言简化从多个不同工具迁移到统一 Lightstep 平台的过程，还支持跨多个 Kubernetes 节点、服务器或 serverless 函数查询和关联指标、日志和跟踪。

- [Solo.io 发布云原生应用网络平台 Gloo Platform v2.3](https://www.solo.io/blog/gloo-platform-2-3/)

    更新内容：新增 Gloo Portal，帮助开发者对 API 进行分类、分享和管理；支持在 Istio 服务网格中处理 GraphQL 请求的流量，包括南北向和东西向的流量；支持 Kubernetes 1.25 和 Istio 1.17；商业化支持 Ambient Mesh。

- [Solo.io 推出多云动态资源发现方案 Gloo Fabric](https://www.solo.io/blog/introducing-solo-gloo-fabric/)

    Gloo Fabric 为 Gloo Platform 提供了多云发现、连接、安全和可观测性功能。Gloo Fabric 通过统一的 API 来配置和管理平台的所有功能，通过统一的管理控制平面来管理网络和安全策略，支持动态地发现网络和集群资源，并提供 API 管理和跨集群多租户隔离功能。此外，Gloo Fabric 还提供自动零信任安全和平台集成的可观测功能。

- [Solo.io 发布云原生网关 Gloo Gateway 1.13](https://www.solo.io/blog/gloo-edge-1-13/)

    版本特性：改进对 OpenCensus 和 OpenTelemetry 追踪扩展的支持；提供了一种内置的方法，可以在错误发生前捕获无效的速率限制配置；增加对 RBAC 的支持；增强控制平面的高可用性，支持多个副本的连续运行和零停机升级；集成集群调度工具 HashiCorp Nomad。

- [Solo.io 发布服务网格和 API 平台 Gloo Platform](https://www.solo.io/blog/announcing-gloo-platform/)

    Gloo Platform 是 Solo.io 的集大成之作，集成了三个产品： Gloo Gateway、Gloo Mesh 和 Gloo Network。利用 Kubernetes CR 和 GitOps 提供一个统一的操作模型，并将零信任安全、多租户、高级路由和可观测性等功能扩展到整个第三层到第七层堆栈。

- Solo.io 发布云原生网关 [Gloo Gateway](https://www.solo.io/blog/announcing-gloo-gateway/) 和 CNI 插件 [Gloo Network](https://www.solo.io/blog/announcing-gloo-network/)

    Gloo Gateway 基于 Envoy 构建，利用 Gloo Platform 的多租户和联邦特性，允许用户轻松管理多个开发团队的网关访问和进行多集群流量管理。Gloo Network 基于 Cilium 构建，将 Kubernetes CNI 层整合为 Gloo Platform 的组件。

- [Spectro Cloud 云原生边缘计算平台 Palette Edge Platform v3.3 发布](https://docs.spectrocloud.com/release-notes#edge)

    版本发布：支持从外部 OCI 注册表中加载镜像、安装程序现在可以包含预加载内容包（包括软件包和工件）；支持创建自定义 Edge 安装程序镜像；支持随机生产设备的 UUID 值。

- [Spectro Cloud Kubernetes SaaS 管理平台 Palette v3.1 发布](https://docs.spectrocloud.com/release-notes#december28,2022-release3.1.0)

    更新内容：Palette IaaS 集群支持自动扩缩容、提供符合联邦信息处理标准（FIPS）的 Kubernetes 版本、支持按标签过滤用户访问和查看集群详情视图、支持应用程序配置文件的版本管理、利用 Helm 和OCI 注册表进行自定义包管理、允许暂停和恢复未使用的虚拟集群。

- [Spectro Cloud 发布 Kubernetes SaaS 管理平台 Palette v2.8](https://docs.spectrocloud.com/release-notes#september10,2022-release2.8.0)

    该版本主要新特性：支持利用嵌套集群为应用快速创建安全隔离的环境；利用基于 Web 的 Kubectl 允许用户通过终端部署应用；支持重复使用和共享具有许多附加组件和集成的大型配置文件。

- [Spectro Cloud 云原生边缘计算平台 Palette Edge Platform 更新](https://www.businesswire.com/news/home/20220929005289/en/New-Spectro-Cloud-Palette-Edge-Platform-Brings-World-Class-Security-and-Operational-Efficiencies-to-Kubernetes-at-the-Edge)

    更新内容包括：新增边缘 K8s 集群的防篡改功能、支持边缘优化的 K8s 发行版 Palette eXtended Kubernetes Edge、简化边缘设备部署。

- [StormForge 发布 Kubernetes 生产环境优化方案 Optimize Live v2.0](https://www.stormforge.io/press-releases/stormforge-launches-v2-optimize-live-kubernetes-resource-optimization/)

    更新内容：通过一个 helm deployment 即可调整应用的大小；使用机器学习分析工作负载使用模式，提供 CPU 和内存建议；能够自动检测 HPA 的存在；提供一系列资源使用报告；简化资源建议的部署。

- [StormForge K8s 优化平台与 Datadog 的云应用监控服务集成，简化 Kubernetes 的可观测性](https://www.stormforge.io/press-releases/new-integration-couples-datadog-observability-stormforge-machine-learning-deliver-automatic-actionable-insights-for-kubernetes-application-optimization/?utm_source=thenewstack&utm_medium=website)

    StormForge K8s 优化平台基于机器学习技术分析可观测数据并推荐资源设置（CPU、内存、副本），提高效率、规模和应用性能。平台现在可利用 Datadog 作为一个统一的观测平台，查看和应用优化建议，并确定应重新校准的应用参数，以减少集群规模，回收和重新分配资源。

- [StormForge Kubernetes 集群性能优化方案 Optimize Live 利用机器学习优化 K8 自动扩缩容能力](https://www.stormforge.io/blog/introducing-intelligent-bi-dimensional-autoscaling/)

    最新版本的 Optimize Live 提供了二维自动缩放能力，HPA 和 VPA 能够协同工作，既能调整 pod 的大小，又能水平设置利用率，最大程度优化自动缩放的效率。此外，还利用机器学习分析历史资源使用情况，以找到最佳的 HPA 目标利用率。

- [SUSE 推出企业级容器管理平台 Rancher Prime](https://mp.weixin.qq.com/s/iVFsSGlRd4TdJGcRKLQBuQ)

    Rancher Prime 是 Rancher 的一种分发版，核心功能代码均来自 Rancher 社区版，但更加重视安全方面的建设，并面向企业用户强化了相关功能和服务。
    Rancher Prime 的特色功能在于：综合安全治理能力提升，提供可信的镜像仓库；
    引入 UI 扩展功能；提供对阿里云、腾讯云以及华为云的托管集群的全生命周期支持；
    引入对 openEuler Linux 的支持；对 ARM 体系的支持。

- [SUSE 发布云原生边缘管理平台 SUSE Edge 2.0](https://mp.weixin.qq.com/s/LszXlp9iKT6FudzWY3EmaQ)

    该版本主要新特性：简化边缘设备的添加和更新操作、支持通过统一的操作面板管理 Kubernetes 和底层操作系统、集成专为容器化和虚拟化工作负载打造的轻量级操作系统 SUSE Linux Enterprise Micro 5.3、为所有分布式环境提供安全防护。

- [实时监测平台观测云更新](https://mp.weixin.qq.com/s/RZCpDuNbq0C0SJfWI2E63w)

    更新内容包括：支持查看基础设施容器对应的 YAML 文件、新增日志查看器 DQL 搜索模式、优化应用性能监测、DataKit 支持将 k8s label 作为 tag 同步到 pod 的指标和日志中、支持将 k8s 中各类 yaml 信息采集到对应的对象数据上、Trace 采集支持自动提取一些关键 meta 信息。

- [时速云微服务治理平台 TMF v5.6.0 发布](https://mp.weixin.qq.com/s/8J0uJIKBwR9RIRwn299Acw)

    该版本主要新特性：支持独立部署，实现与底层平台的解耦；解耦微服务框架和性能监控能力两个模块；新增链路组件拓扑图；增加对无损流量上下线功能的支持；新增主备拓扑能力，拓扑图可视化展示主备关系。

- [数澈软件发布 SEAL 0.3：国内首个全链路软件供应链安全管理平台](https://mp.weixin.qq.com/s/H_bjMbH_7DJEVOpvzGEMoQ)

    该版本新特性：支持集成任意 OCI 镜像仓库，扫描其中的容器镜像；支持集成任意 Kubernetes 集群，扫描其中的工作负载配置及镜像；支持扫描第三方软件物料清单文件；支持在任意 CI/CD 流水线中集成 SEAL 的安全扫描功能；能够聚合管理全链路各个阶段的资源提供全链路安全洞察；支持自动生成多策略修复建议、漏洞优先级排序、因时制宜处理安全问题。

### T

- [Tetrate 推出针对 Amazon EKS 设计的服务网格解决方案 TSE](https://mp.weixin.qq.com/s/Q4qTLOv8kNn7lf0flHCOzg)

    TSE 基于 Istio 和 Envoy 等开源服务网格组件构建，并针对 Amazon EKS 对 TSE 进行了简化安装、配置和操作的优化。
    TSE 提供了 Istio 和 Envoy 之上的服务网格自动化。
    它用于在 Amazon EKS 上安装和配置开源组件，与 AWS 服务集成，并为平台运营商提供管理控制台，以快速配置服务网格以实现安全、弹性和可观察性。

- [Tetrate 应用连接平台 Tetrate Service Bridge v1.6.0 发布](https://docs.tetrate.io/service-bridge/1.6.x/en-us/release_notes_announcements)

    更新内容：增加安全域、服务安全设置等安全规则；增加东西向网关改善集群间的服务故障转移；用户界面优化，支持可视化和监控平台和服务活动；新增排障工具，无需集群的访问特权即可排障；支持集群内的多 Istio 环境；支持跨网关和服务代理的 WASM 扩展；Skywalking 的后端服务 OAP 代替 Zipkin，用于收集和查询 trace。

- [Tigera 发布 Kubernetes 网络和容器威胁防御方案 Calico Runtime Threat Defense](https://www.tigera.io/news/tigera-introduces-calico-runtime-threat-defense-the-most-comprehensive-plug-and-play-defense-against-container-and-network-based-threats/)

    Calico Runtime Threat Defense 结合结合基于签名和行为的技术来检测已知威胁和零日威胁，能够检测 MITRE 最常见的容器和网络的攻击。
    与传统的运行时威胁检测平台不同，Calico Runtime Threat Defense 无需编写复杂的规则即可持续监控和分析网络和容器行为，获取攻击指标（IOA）。

- [Traefik Labs 发布云原生 API 网关 Traefik Enterprise 2.10](https://traefik.io/blog/announcing-traefik-enterprise-2-10/)

    更新内容：允许 OIDC 中间件检查访问令牌中的要求、允许从 Kubernetes Secret 中加载敏感数据、支持限制 API 的访问速率。

- [Traefik Labs 发布云原生网络平台 Traefik Hub 1.0](https://traefik.io/blog/announcing-the-general-availability-of-traefik-hub-1-0/)

    Traefik Hub 1.0 允许用户可以使用 Traefik 或 Nginx 快速、安全地发布 Kubernetes 或 Docker 容器。Traefik Hub 提供了为 Kubernetes 集群联网所需的集中控制平面，而无需部署容器 sidecar 来运行网络软件。其支持通过安全加密隧道和直接私有连接进行容器联网，通过 JWT 或 OIDC 为服务添加访问控制，通过 GitOps 实现规模化的自动化等，并配有工作空间促进跨团队协作等。

- [腾讯云容器服务 TKE 2 月更新](https://mp.weixin.qq.com/s/w_rxP8K3C6nccxAsPP3tNw)

    更新内容：集群节点升级入口支持 docker/containerd 组件小版本更新、上线 CFS-Turbo CSI 存储插件、集群日志采集规则支持对元数据的自定义配置、注册节点支持 GPU、支持通过云上控制台一键在用户 IDC 创建、管理和升级 Kubernetes 集群。

- [腾讯云云原生 API 网关更新](https://cloud.tencent.com/product/events)

    更新内容：支持对接云函数 SCF 和微服务平台 TSF、支持定时弹性扩缩容和实例升降配、Kong Ingress 支持使用 Annotation 式配置、灰度能力产品化、支持对接云上 WAF 和云上 SSL、支持 mTLS。

- [腾讯云容器服务 TKE 三项能力升级](https://mp.weixin.qq.com/s/DfxCQM8KzMioSt6rVq5oHw)

    升级内容：节点管理方面，新增 HouseKeeper 运维范式，对原生节点、超级节点、注册节点等云上/云下资源进行纳管；
    集群管理方面，支持一种集群管理任意节点，同时支持原生节点、超级节点、注册节点和边缘节点等多种节点；
    应用管理方面，打造面向多云和边缘场景的应用管理平台，实现多集群统一分发、部署和管理。

- [腾讯云容器服务 TKE 9 月更新](https://mp.weixin.qq.com/s/6_TSSHhU0L8mSbqEMWyu4g)

    更新内容：支持镜像仓库签名镜像的可信验证、kubelet 自定义参数功能全量开放、提供异常 Service/Ingress 事件信息错误码的说明、灰度上线超级节点上运行 Daemonset 能力、新增按照Label 配置和管理 Pod 安全组的功能。

- [腾讯云 K8s 发行版 TKE 8 月更新](https://mp.weixin.qq.com/s/t6yGrxcn4JZdd9877raXhA)
  
    更新内容包括：新增 SecurityGroupPolicy 增强组件，支持为策略匹配的 Pod 绑定安全组；支持业务 Pod 使用 Service Account Token 访问 CVM、VPC 等云资源；支持在不重启 Pod 的情况下修改 CPU、内存的 Request/limit 值；支持节点/工作负载资源洞察能力；新增 Request 智能推荐功能；新增原生节点专用调度器；优化原生节点初始化流程。

- [天翼云发布云原生安全产品——红盾 1.0](https://mp.weixin.qq.com/s/9crAAOde9_spFmk5TZcY2A)

    红盾基于云原生底座将安全能力整合至统一的安全平台，面向云原生业务应用安全、网络安全、数据安全、云原生安全 4 大领域，打造一体化云安全可信运营体系和零信任架构。
    其核心产品包括 Web 应用防火墙、DDoS 高防、网站安全监测、企业安全访问、天翼云数据安全管理平台等。

### U, V

- [Upbound 推出基于 Crossplane 的托管型控制平面管理服务（MCP）](https://blog.upbound.io/upbound-general-availability/)

    用户可以可以通过 MCP 扩展到数千个 CRD，使用控制平面来管理其所需的所有云服务资源，从而允许用户运行数十个甚至数百个控制平面来为不同的环境、团队、业务和客户服务。
    此外，MCP 与 Git 无缝集成，提供用于管理和操作控制平面以及所有资源的控制台，支持安装在任何 Kubernetes 集群中，并支持在 GitOps 流程中管理基础设施和应用程序资源。

- [Veeam 发布 Kubernetes 数据管理平台 Kasten K10 v5.5](https://www.kasten.io/kubernetes/resources/blog/scaling-simplicity-with-kasten-k10-v5.5)

    该版本主要新特性：新增备份窗口允许用户选择策略运行的时间间隔、支持自动安排底层备份工作的顺序、支持定义多个保护策略以设置备份频率和位置等参数、提供可视化 Helm 向导程序、支持 IPv6、集成 GitOps 流水线、新增存储类型、通过 OpenSSF 和 Azure Managed Identity 增强备份安全性。

- [Venafi 推出云原生机器身份管理服务 TLS Protect for Kubernetes](https://venafi.com/blog/simplify-cloud-native-machine-identity-management-with-tls-protect-for-kubernetes/)

    TLS Protect for Kubernetes 是 Venafi 机器身份管理平台 Control Plane for Machine Identities 的一部分，
    帮助安全和平台团队在多云和多集群 Kubernetes 环境中管理云原生机器身份，如 TLS、mTLS 和 SPIFFE，增强机器身份管理的可观测性、控制和自动化。

- [VMware Tanzu 发布 Kubernetes DevOps 平台 VMware Tanzu Application Platform 1.5](https://tanzu.vmware.com/content/blog/tanzu-application-platform-1-5-ga)

    更新内容：完成支持 GitOps 模式的 Namespace Provisioner；平台工程师可以使用私有 Git 仓库来引用模板化的资源；支持基于 GitOps 的安装流程；新增面板用于显示集群中工作负载的详细信息；新增 External Secrets Operator；支持分布式 API 网关 Spring Cloud Gateway for Kubernetes。

- [VMware Tanzu 服务网格方案 Tanzu Service Mesh 3.0.3 发布](https://docs.vmware.com/en/Tanzu/services/rn/vmware-tanzu-service-mesh-global-controller-release-notes/index.html#Past%20Tanzu%20Service%20Mesh%20Releases)

    更新内容：Tanzu Service Mesh CLI 支持 GitOps，可用于自动部署 Tanzu Service Mesh 环境到集群中；支持选择要注入 proxy sidecar 的命名空间；支持客户端集群和 Tanzu Service Mesh SaaS 之间的企业级代理通信。

- [VMware Tanzu 多云多集群 Kubernetes 管理方案 Tanzu Mission Control 更新](https://docs.vmware.com/en/VMware-Tanzu-Mission-Control/services/rn/vmware-tanzu-mission-control-release-notes/index.html)

    更新内容：支持 Pod 安全的 mutation 策略、支持 Tanzu Kubernetes Grid 2.1（包括 ClusterClass）、支持集群组的持续交付、支持从 Git 仓库中安装 Helm chart 到集群中。

- [VMware Tanzu K8s DevOps 平台 Tanzu Application Platform v1.4 发布](https://docs.vmware.com/en/VMware-Tanzu-Application-Platform/1.4/tap/release-notes.html)

    更新内容：支持 shared ingress issuer、新增命名空间配置器实现安全自动化的命名空间配置、新增 TAP 遥测报告以供查看 TAP 的使用情况、新增 Visual Studio 的 IDE 扩展 —— Tanzu Developer Tools for Visual Studio、支持 External Secrets Operator。

- [VMware Tanzu Kubernetes Grid 2.1 发布](https://tanzu.vmware.com/content/blog/tanzu-kubernetes-grid-2-1)

    该版本主要新特性：引入新的 Cluster API 功能 ClusterClass 以及 Carvel 工具，使用统一的、声明式的 API 创建和管理集群；支持公有云 Oracle Cloud 基础设施。

- [VMware Tanzu 发布 Application Service Adapter for Tanzu Application Platform v1.0，旨在弥补 Cloud Foundry 和 Kubernetes 间的开发体验差距](https://tanzu.vmware.com/content/blog/application-service-adapter-for-vmware-tanzu-application-platform-1-0)

    该版本主要新特性：支持在 Kubernetes 和 TAP 上提供一个无缝的 Cloud Foundry 推送工作流、使用 Contour 复制 Cloud Foundry 部署中的 goRouter 入口模式、使用本地 Kubernetes RBAC、重建了由本地 Kubernetes 命名空间支持的 Cloud Foundry 组织和空间结构、集成 Tanzu Build Service、集成 TAP 的端到端流水线供应链 Supply chain choreographer（实验性）。

- [VMware Tanzu v2.0 应用容器化工具发布](https://docs.vmware.com/en/Application-Transformer-for-VMware-Tanzu/2.0/rn/application-transformer-for-vmware-tanzu-20-release-notes/index.html)

    该版本主要新特性：集成自动化扫描工具 Cloud Suitability Analyzer（CSA）、支持 Windows 容器化、支持虚拟机容器化、支持 Linux 和  Windows 平台的 200 多个组件签名、提供命令行界面。

- [VMware Tanzu Application Platform v1.3 (K8s DevOps 平台) 发布](https://tanzu.vmware.com/content/blog/tanzu-application-platform-1-3)

    更新内容：支持在物理隔离环境下运行、集成供应链威胁扫描工具、新增一个统一的威胁监控大盘、支持 SBOM、支持 API 规范动态注册、集成 Jenkins CI/CD、支持自定义证书机构（CA）证书、新增运行时资源监测插件、增加对 Java 和 Python 函数工作负载的支持（beta）、在 OpenShift 上可用。

- [VMware Tanzu Kubernetes Grid v1.6 发布](https://docs.vmware.com/en/VMware-Tanzu-Kubernetes-Grid/1.6/vmware-tanzu-kubernetes-grid-16/GUID-release-notes.html)

    该版本主要新特性：支持在 vSphere 7.0+ 上将工作负载集群部署到支持 GPU 的主机和边缘设备、使用 Multus 和 Whereabouts 实现多个 Pod 网络接口、支持使用 Amazon EBS CSI driver 和 Azure Disk CSI driver for Kubernetes 的 CSI 存储。

- [VMware Spring Cloud Gateway for Kubernetes v1.2.0 发布](https://docs.vmware.com/en/VMware-Spring-Cloud-Gateway-for-Kubernetes/1.2/scg-k8s/GUID-release-notes.html)  

    该版本主要新特性：分离客户端入口和上游应用服务通信的 TLS 配置、扩大自定义扩展云秘密管理的权限、增加熔断器状态指标、新增全局和每个 API 路由的响应缓存配置、增加 JSON 请求转换到 gRPC 上游服务的过滤器、增加 podOverrides 以配置 API 网关实例上的 K8s pod override、API 网关现在可以通过独立的 JAR 部署。

### W, Z

- [Weave GitOps 更新](https://www.weave.works/blog/weave-gitops-2022-09)

    更新内容包括：优化可信交付（Trusted Delivery），增加策略即代码和渐进式交付功能；新增 Team Workspaces，优化多租户的工作方式；用户界面新增 ClickOps 功能，简化微服务部署；新增 GitOps Run 的技术预览功能，提供接近实时的迭代开发，一旦本地清单文件被保存，它就会立即与 Kubernetes 核对。

- [中国联通云原生架构全面升级](https://mp.weixin.qq.com/s/QJIU0UQ48hfl3RPsMVpyCw)

    升级亮点：支持多种国产芯片和国产操作系统；兼容 CNM、CNI 双标准规范；新增 DVR 分布式网关、VPC 互连、VPC 弹性网卡直通网络(基于 IPVLAN)、VPC 路由直通网络(兼容 Flannel/ Calico 插件)、策略路由、VPC 网络多出/入口、IPv4/6、四/七层负载分离等功能；单集群容量支持承载超 10W+ 容器；集成一整套可视化自动运维能力。
