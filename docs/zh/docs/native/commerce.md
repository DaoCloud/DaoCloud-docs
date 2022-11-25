# 商业产品

- [**Aqua 云原生安全平台引入基于 eBPF 技术的零日漏洞检测工具 Lightning Enforcer**](https://blog.aquasec.com/combat-zero-day-threats-with-aquas-ebpf-lightning-enforcer)

    Aqua Lightning Enforcer 利用漂移和基于行为的自动化检测方法，检测零日漏洞等未知威胁，并提供事件管理、可疑行为告警以及开箱即用的 CNDR（云本地检测和响应）。此外，eBPF 技术的应用避免了传统代理对工作负载的影响，降低了系统的资源开销。

- [**D2iQ Kubernetes 平台 DKP v2.4.0 发布**](https://docs.d2iq.com/dkp/2.4/dkp-2-4-0-features-and-enhancements)

    该版本主要新特性：支持在本地和物理隔离环境中运行 GPU 节点、支持红帽企业 Linux 系统、Rook Ceph 替代 MinIO 成为平台的默认存储、集成 Trivy 等第三方扫描工具。

- [**F5 发布中国版容器 Ingress 服务 CIS-C**](https://mp.weixin.qq.com/s/4BuiZC8AEnRt-lwT7dNyxg)

    CIS-C 是一款将 Kubernetes 集群内服务通过 F5 BIG-IP 进行自动化发布的控制器软件。帮助用户打通 Kubernetes 集群与外部入口，将 BIG-IP 应用交付能力集成到 kubernetes 技术栈的云环境中。它实现了多团队合作，用户可以灵活地、自动化地创建、变更应用或者服务入口策略。

- [**GitLab 15.5 发布**](https://mp.weixin.qq.com/s/AiRU9pQUxTex0F_XvuHiHg)

    该版本主要新特性：在合并请求流水线中运行安全扫描工具、支持 Kubernetes 容器扫描、支持从 GitHub 导入项目时导入更多的关系、新增预定义 DORA（评估 DevOps 效能水平的指标）可视化比较报告。

- [**Google 发布云原生文件存储服务 Filestore Multishares for GKE**](https://cloud.google.com/filestore/docs/multishares)

    Filestore 是一个文件存储托管服务，Filestore 实例是一个网络附属存储（NAS）托管系统。Filestore Multishares for GKE 为 GKE 实例提供了文件存储服务，其主要功能包括：支持区域性存储，防止区域故障；一个Filestore Enterprise 实例上可分配多达 10 个 share,每个 share 映射到 GKE 中唯一的持久卷；支持动态卷配置，可根据需要增加或减少 share 和实例的容量。

- [**Google 发布 Kubernetes Gateway API 的企业级实现 GKE Gateway Controller**](https://cloud.google.com/blog/products/containers-kubernetes/google-kubernetes-engine-gateway-controller-is-now-ga)

    GKE Gateway Controller GKE 提供了一个可扩展的 API 来管理内外部的 HTTP(S) 负载均衡。其主要功能包括：提供了一个多路由/租户共享的网关、默认提供两个 GatewayClass 即 Global external 和 Regional Internal 负载均衡、支持大规模的端到端加密、支持定制后端服务属性、提供高级流量管理等。

- [**Grafana Cloud 观测平台集成 Cilium Enterprise，加强 Kubernetes 网络监控**](https://grafana.com/blog/2022/11/17/introducing-the-cilium-enterprise-integration-in-grafana-cloud-for-kubernetes-network-monitoring/)

    集成后，可以将 Cilium Enterprise 中部署的数据输送到 Grafana Cloud。Grafana Cloud 提供四个预制的仪表盘：Cilium 总览、Hubble 总览、Cilium operator 和 Cilium Agent。还提供了 17 条告警规则，用于监测与 Cilium Agent 和 Kubernetes 集群状态相关的 Cilium 核心组件。

- [**Grafana Cloud 推出业内首个性能测试和分布式追踪的集成**](https://grafana.com/blog/2022/11/03/how-to-correlate-performance-testing-and-distributed-tracing-to-proactively-improve-reliability/)

    Grafana Cloud 引入负载测试项目 [k6](https://github.com/grafana/k6) 和分布式追踪后端 [Tempo](https://github.com/grafana/tempo)（k6 x Tempo）的集成，缩小性能测试的黑盒数据和系统内部白盒数据之间的差距。该集成允许关联 k6 的测试运行数据和服务器端的追踪数据，从而进行根本原因分析；汇总收集的追踪数据以生成实时指标，帮助用户缩小搜索空间并快速发现异常行为。

- [**Lacework Platform 云安全平台十一月更新**](https://docs.lacework.com/releases/2022-11-platform-releases)

    更新内容：平台扫描器支持多架构的容器镜像、提供攻击路径分析功能、无代理工作负载扫描功能普遍可用、在不活动的主机内核上发现的漏洞会自动被标记为例外、CIS GCP 1.3.0 基准报告和策略普遍可用、新增主机策略用于检测反向 shell 连接和加密劫持工件。

- [**NetApp Kubernetes 应用数据管理方案 Astra Control 更新**](https://www.netapp.com/blog/astra-kubernetes-data-protection/)

    更新内容：支持为多个命名空间设置一个应用数据保护策略；扩大集群范围内资源的检测和保护范围；基于标签和标签选择器允许每个命名空间有多个应用程序；K8s 应用现在可以在不同的项目、订阅或账户托管的集群间进行故障转移；集成轻量目录访问协议 LDAP；支持更多 Self-managed K8s 平台。

- [**Ondat v2.9 云原生块存储平台发布**](https://www.ondat.io/blog/ondat-launches-version-2.9)

    该版本主要新特性：支持在零停机的情况下调整卷的大小、通过存储池可以控制工作负载所使用的存储类型、允许定义卷的拓扑结构。

- [**OpenShift Service Mesh 2.3 发布**](https://cloud.redhat.com/blog/introducing-openshift-service-mesh-2.3)

    该版本主要新特性：支持 Istio v1.14、支持通过注入 deployment 实例来创建和管理网关、新增集群范围的拓扑结构、增加 OpenShift 服务网格控制台 operator、支持 Istio 可视化工具 Kiali 1.57。

- [**Openshift 日志管理服务 Logging 5.5 发布**](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.11/html/logging/release-notes#cluster-logging-release-notes-5-5-0)

    该版本主要新特性：支持把同一 pod 内不同容器的结构化日志转发给不同的索引、使用 Kubernetes 通用标签过滤带有 Elasticsearch 输出的日志、日志聚合 Loki Operator 和 观测数据收集Vector collector 正式可用。

- [**Portworx Enterprise 2.12 云原生数据管理平台发布**](https://docs.portworx.com/release-notes/portworx/#2-12-0)

    该版本主要新特性：本地用户可以启用 PX-Fast 功能，使用高性能存储作为 Kubernetes 的持久化存储；允许存储管理员使用自定义的 Kubernetes 对象为对象存储桶提供各种支持服务；自动生成 Vault 令牌，在 Vault 中存储加密 secret 和云证书；允许 Kubernetes 资源迁移到目标集群之前对其进行修改。

- [**Rafay Systems 推出 Service Mesh Manager and Network Policy Manager，提供企业级的 K8s 流量管理和通信安全保障**](https://rafay.co/press-release/rafay-launches-service-mesh-manager-and-network-policy-manager-for-enterprise-grade-traffic-management-and-transport-security-for-kubernetes/)

    Service Mesh Manager 基于 Istio 构建，为微服务团队提供集中的安全控制和流量管理策略配置。Network Policy Manager 基于 Cilium 构建，提供集中管理以及 pod 和命名空间通信的可见性，以隔离边界并减少集群的横向攻击面。

- [**Traefik Labs 发布云原生网络平台 Traefik Hub 1.0**](https://traefik.io/blog/announcing-the-general-availability-of-traefik-hub-1-0/)

    Traefik Hub 1.0 允许用户可以使用 Traefik 或 Nginx 快速、安全地发布 Kubernetes 或 Docker 容器。Traefik Hub 提供了为 Kubernetes 集群联网所需的集中控制平面，而无需部署容器 sidecar 来运行网络软件。其支持通过安全加密隧道和直接私有连接进行容器联网，通过 JWT 或 OIDC 为服务添加访问控制，通过 GitOps 实现规模化的自动化等，并配有工作空间促进跨团队协作等。

- [**Veeam 发布 Kubernetes 数据管理平台 Kasten K10 v5.5**](https://www.kasten.io/kubernetes/resources/blog/scaling-simplicity-with-kasten-k10-v5.5)

    该版本主要新特性：新增备份窗口允许用户选择策略运行的时间间隔、支持自动安排底层备份工作的顺序、支持定义多个保护策略以设置备份频率和位置等参数、提供可视化 Helm 向导程序、支持 IPv6、集成 GitOps 流水线、新增存储类型、通过 OpenSSF 和 Azure Managed Identity 增强备份安全性。

- [**VMware Tanzu Kubernetes Grid 2.1 发布**](https://tanzu.vmware.com/content/blog/tanzu-kubernetes-grid-2-1)

    该版本主要新特性：引入新的 Cluster API 功能 ClusterClass 以及 Carvel 工具，使用统一的、声明式的 API 创建和管理集群；支持公有云 Oracle Cloud 基础设施。

- [**VMware Tanzu 发布 Application Service Adapter for Tanzu Application Platform v1.0，旨在弥补 Cloud Foundry 和 Kubernetes 间的开发体验差距**](https://tanzu.vmware.com/content/blog/application-service-adapter-for-vmware-tanzu-application-platform-1-0)

    该版本主要新特性：支持在 Kubernetes 和 TAP 上提供一个无缝的 Cloud Foundry 推送工作流、使用 Contour 复制 Cloud Foundry 部署中的 goRouter 入口模式、使用本地 Kubernetes RBAC、重建了由本地 Kubernetes 命名空间支持的 Cloud Foundry 组织和空间结构、集成 Tanzu Build Service、集成 TAP 的端到端流水线供应链 Supply chain choreographer（实验性）。

- [**VMware Tanzu v2.0 应用容器化工具发布**](https://docs.vmware.com/en/Application-Transformer-for-VMware-Tanzu/2.0/rn/application-transformer-for-vmware-tanzu-20-release-notes/index.html)

    该版本主要新特性：集成自动化扫描工具 Cloud Suitability Analyzer（CSA）、支持 Windows 容器化、支持虚拟机容器化、支持 Linux 和  Windows 平台的 200 多个组件签名、提供命令行界面。

- [**阿里云容器服务 ACK 更新**](https://mp.weixin.qq.com/s/cOObDVvnTGkX_hiAWv8mVA)

    更新内容：提供对 eRDMA 高性能容器网络的支持、基于新一代容器网络文件系统 CNFS 2.0 更好支持有状态应用的容器化、内建云原生混部系统 Koordinator 的产品化支持、发布 AIOps 套件和 FinOps 套件。

- [**阿里云发布云原生技术中台 CNStack 2.0**](https://mp.weixin.qq.com/s/5q8i_BSL8DbdwOUHmBkQ8Q)

    CNStack 2.0 支持不同厂商、不同架构、不同地域和 CPU/GPU 算力混合管理。提供应用开发、测试、运维全生命周期的一站式管理，场景覆盖容器服务、分布式应用、云边、DevOps。此外，平台还提供了完整的技术栈支持，包括内置的、开箱即用的产品组件和中间件以及原厂和合作伙伴提供的产品及组件。

- [**阿里云微服务引擎 MSE 10 月更新**](https://mp.weixin.qq.com/s/Puud_MYgCMezqKESaAiG-w)

    更新内容：注册配置中心提供迁移工具及方案、云原生网关服务来源支持 Serverless 应用引擎、认证鉴权支持多个规则并存、路由及服务详情页面新增QPS、错误、延迟等指标监控、全链路灰度及标签路由等能力支持 Consul 注册中心。

- [**时速云微服务治理平台 TMF v5.6.0 发布**](https://mp.weixin.qq.com/s/8J0uJIKBwR9RIRwn299Acw)

    该版本主要新特性：支持独立部署，实现与底层平台的解耦；解耦微服务框架和性能监控能力两个模块；新增链路组件拓扑图；增加对无损流量上下线功能的支持；新增主备拓扑能力，拓扑图可视化展示主备关系。
