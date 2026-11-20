---
hide:
  - toc
---

# 功能和优势

DaoCloud Enterprise 融海量特性于一体，提供一站式 PaaS 服务，目前支持的典型功能如下。

## 功能特性

| 分类 | 功能特性 | 说明 |
| :--- | :--- | :--- |
| [多集群管理](../kpanda/intro/index.md) | [多集群统一纳管](../kpanda/user-guide/clusters/integrate-cluster.md) | 支持特定版本范围内任意 Kubernetes 集群纳入容器管理范围，实现云上云下多云&混合云容器云平台的统一管理 |
| | [集群快速部署](../kpanda/user-guide/clusters/create-cluster.md) | 通过 Web 界面快速部署企业级的 Kubernetes 集群，适配物理机和虚拟机底层环境 |
| | [一键式集群升级](../kpanda/user-guide/clusters/upgrade-cluster.md) | 一键升级 Kubernetes 版本，统一管理系统组件升级 |
| | 集群高可用 | 内置集群容灾、备份能力，保障业务系统在主机故障、机房中断、自然灾害等情况下可恢复，降低业务中断风险 |
| | 全生命周期管理 | 实现自建云原生集群的全生命周期管理 |
| | [开放式 API](https://docs.daocloud.io/openapi/) | 提供原生的 Kubernetes OpenAPI 能力 |
| [集群运维与安全](../kpanda/user-guide/clusterops/latest-operations.md) | [集群巡检](../kpanda/user-guide/inspect/index.md) | 一键巡检集群与节点健康状态，生成巡检报告，快速发现与定位风险 |
| | [应用备份恢复](../kpanda/user-guide/backup/index.md) | 基于 Velero 备份与恢复应用及其持久化数据，支持集群迁移与灾难恢复 |
| | [GPU 资源管理](../kpanda/user-guide/gpu/index.md) | 支持 GPU 手动/动态调度与共享，适配 NVIDIA、昇腾、天数、MetaX 等异构算力 |
| | [安全扫描](../kpanda/user-guide/security/index.md) | 内置合规性扫描、权限扫描、漏洞扫描三类扫描，保障集群与应用安全 |
| [云原生应用管理](../amamba/intro/index.md) | 多形态应用管理 | 实现不同类型云原生应用的部署及全生命周期管理，支持云原生应用、Helm 应用、OAM 等，开放式多云应用兼容 |
| | 一站式部署 | 解耦底层 Kubernetes 平台，一站式部署和运维业务应用 |
| | 应用负载扩缩容 | 通过界面实现应用负载的手动/自动扩缩容，自定义扩缩容策略，应对流量高峰 |
| | 应用全生命周期 | 支持应用查看、更新、删除、回滚、事件查看以及升级等全生命周期管理 |
| | 跨集群负载统一管理 | 跨集群负载统一管理能力 |
| | [GitOps 持续部署](../amamba/user-guide/gitops/create-argo-cd.md) | 基于 Argo CD 实现声明式持续部署，应用配置以 Git 为唯一可信源 |
| | [渐进式应用发布](../amamba/user-guide/release/canary.md) | 支持[金丝雀发布](../amamba/user-guide/release/canary.md)与[蓝绿发布](../amamba/user-guide/release/blue-green.md) |
| [持续性业务交付](../amamba/intro/index.md) | [企业级云原生 CI/CD](../amamba/user-guide/pipeline/create/custom.md) | 标准化的持续集成和交付能力，实现应用的敏捷迭代，快速满足业务新需求，提高应用的集成和发布效率 |
| | 交付云原生化 | 应用构建环境的容器化管理，自定义构建机器等资源，流水线级资源隔离，支持多种类型的应用部署 |
| | 提升研发效能 | 可视化流水线构建环境中预先封装声明性步骤，无需脚本即可创建复杂流水线；根据资源大小自动创建/销毁环境，避免资源浪费 |
| | 流水线即代码 | 基于声明性语法的流水线易于学习，配置具有版本可控、模块化、可重用等特点 |
| | DevOps 工具集成 | 单个流水线中的步骤可在多操作系统、多体系结构节点上运行，支持集成 Kubernetes、GitLab、SonarQube、Harbor 等主流软件 |
| | [代码仓库管理](../amamba/user-guide/repo.md) | 集中托管代码仓库，与流水线联动实现从代码到应用的持续交付 |
| [多云应用分发](../kairship/intro/index.md) | 统一多云编排控制面 | 统一管理多个多云实例，统一请求入口 |
| | [多云集群一键导入](../kairship/cluster.md) | 多云集群一键导入 |
| | [丰富的分发与覆盖策略](../kairship/policy/propagation.md) | 提供丰富的多云应用[分发策略](../kairship/policy/propagation.md)、[覆盖策略](../kairship/policy/override.md) |
| | [故障切换](../kairship/failover/failover.md) | 多云应用故障切换（Failover）功能 |
| | [多云工作负载](../kairship/workload/deployment.md) | 创建与管理多云工作负载，支持[一键转换](../kairship/workload/promote.md)普通工作负载为多云工作负载 |
| | [多云资源管理](../kairship/resource/ns.md) | 统一管理多云命名空间、服务、Ingress、ConfigMap、Secret 等资源 |
| [镜像仓库](../kangaroo/intro/index.md) | [托管 Harbor](../kangaroo/managed/harbor.md) | 一键创建与托管 Harbor 实例，实现镜像与 Helm Chart 的安全托管 |
| | [镜像空间](../kangaroo/space/index.md) | 基于工作空间的镜像空间管理，支持镜像扫描、回收与清单管理 |
| | [仓库集成](../kangaroo/integrate/integrate-ws.md) | 集成外部镜像仓库（Harbor、Docker Registry 等），统一管理凭据与仓库列表 |
| [容器化虚拟机](../virtnest/intro/index.md) | [虚拟机全生命周期管理](../virtnest/vm/index.md) | 创建、克隆、快照与调度虚拟机，支持 GPU 直通 |
| | [热迁移与快照](../virtnest/vm/live-migration.md) | 支持虚拟机[实时迁移](../virtnest/vm/live-migration.md)与[定时快照](../virtnest/vm/scheduled-snapshot.md)，保障业务连续性 |
| | 虚拟机模板 | 提供开箱即用的虚拟机模板，快速批量创建虚拟机 |
| [云原生网络](../network/intro/index.md) | 多 CNI 组合方案 | 支持 Cilium、Calico 等多种 CNI 及其组合方案（eBPF 加速 Overlay + Underlay），覆盖跨云跨集群连通场景 |
| | [子网与 IP 池管理](../network/config/ippool/createpool.md) | 面向 Underlay 网络提供子网与 IP 池的创建与分配管理 |
| | 网络策略与可观测 | 提供网络连通性检测、网络策略配置与链路质量分析 |
| [云原生存储](../storage/hwameistor/intro/index.md) | 本地存储 | 基于 HwameiStor 提供本地盘、LVM 等云原生存储方案，低时延、高吞吐 |
| | 存储高可用 | 提供 DRBD 数据卷复制，实现存储级容灾 |
| | 存储应用场景 | 提供[高可用卷](../storage/hwameistor/application/ha.md)等持久化方案，适配 TiDB、MinIO 等常见应用 |
| [云边协同](../kant/intro/index.md) | [边缘单元管理](../kant/user-guide/edge-unit/manage-unit.md) | 支持内部/外部边缘单元的创建与管理，按单元批量下发应用 |
| | [边缘应用](../kant/user-guide/edge-app/index.md) | 创建与批量创建边缘应用，部署至指定的边缘单元 |
| | [终端设备管理](../kant/user-guide/device/index.md) | 注册与管理终端设备，支持设备与边缘节点绑定及设备数据上报 |
| [一站式微服务治理](../skoala/intro/index.md) | 注册中心集中纳管 | 集中纳管集群所有动态微服务 |
| | [微服务流量治理](../skoala/cloud-ms/traffic-control.md) | 可快速与主流微服务框架集成 |
| | 注册配置中心 | 集中管理和配置微服务相关资源 |
| | [微服务网关](../skoala/gateway/index.md) | 管理微服务南北流量管控 |
| | [传统微服务托管](../skoala/trad-ms/hosted/index.md) | 提供托管与集成两类注册中心，Spring Cloud、Dubbo 等传统微服务无需改造即可接入 |
| | [插件中心](../skoala/plugins/index.md) | 提供认证、限流、缓存等丰富的网关插件生态 |
| [服务网格](../mspider/intro/index.md) | [托管/专享网格](../mspider/user-guide/service-mesh/index.md) | 一键创建托管网格与专享网格，统一纳管多集群服务治理能力 |
| | [网格多云部署](../mspider/user-guide/multicluster/multicluster-install.md) | 支持网格多云部署与多集群网络互联，跨集群服务互通 |
| | [东西流量治理](../mspider/user-guide/traffic-governance/virtual-service.md) | 基于 VirtualService、DestinationRule 实现精细化的东西流量治理与故障恢复 |
| | [流量泳道](../mspider/user-guide/traffic-lane/index.md) | 支持灰度发布场景的全链路流量泳道 |
| [可观测](../insight/intro/index.md) | 开箱即用 | 以应用为中心的新一代云原生可观测性运维平台，指标、日志、链路三合一采集，实现快速的故障定位和快捷的故障排查 |
| | 实时监控告警 | 采集各项指标、日志及事件等数据分析应用健康状态，提供告警能力和多维度数据可视化 |
| | 开放兼容 | 兼容主流开源组件，提供快捷故障定位及一键监控诊断能力 |
| | [统一告警中心](../insight/user-guide/alert-center/index.md) | 告警策略、消息模板、静默与抑制一站式管理 |
| | [仪表盘](../insight/user-guide/dashboard/index.md) | 提供开箱即用的内置仪表盘，支持导入自定义 Grafana 面板 |
| [统一的用户权限体系](../ghippo/intro/index.md) | [用户/用户组集中管理](../ghippo/user-guide/access-control/user.md) | 多功能模块统一用户/用户组管理，打通用户体系，降低管理运维成本 |
| | 多模型授权 | 满足不同企业规模、组织结构用户及授权模型，实现最短链路授权 |
| | [企业级访问控制](../ghippo/user-guide/access-control/oidc.md) | 统一认证登录系统，通过联合认证接入登录容器管理平台，实现单点登录 |
| | [工作空间/层级管理](../ghippo/user-guide/workspace/index.md) | 高度契合企业业务层级，满足部门层级间的资源隔离及管理需求 |
| | 灵活的资源划分 | 基于资源粒度（命名空间、集群、注册中心等）进行资源划分及绑定，统一分配容器平台资源 |
| | [审计日志](../ghippo/user-guide/audit/index.md) | 记录平台用户与 API 操作，支持按操作类型、时间等维度检索与导出 |
| | [运营管理](../ghippo/user-guide/report-billing/index.md) | 对接计量计费体系，提供部门/租户维度的报表与账单管理 |
| [精选中间件](../middleware/index.md) | 主流中间件 | 支持 [MySQL](../middleware/mysql/intro/index.md)、[Redis](../middleware/redis/intro/index.md)、[PostgreSQL](../middleware/postgresql/intro/index.md)、[Elasticsearch](../middleware/elasticsearch/intro/index.md)、[Kafka](../middleware/kafka/intro/index.md)、[RocketMQ](../middleware/rocketmq/intro/index.md)、[RabbitMQ](../middleware/rabbitmq/intro/index.md)、[MongoDB](../middleware/mongodb/intro/index.md)、[MinIO](../middleware/minio/intro/index.md)、[SeaweedFS](../middleware/seaweedfs/intro/index.md) 等 |
| | 全生命周期管理 | 支持实例全生命周期管理，满足多种高可用集群模式，可根据场景需求自定义副本和配置 |
| | 在线扩容 | 支持在线的资源和存储的扩容 |
| | 统一监控 | 支持实例资源和业务维度的统一监控 |
| | 多租户权限 | 可基于工作空间实现多租户需求的权限管理 |

## 产品优势

| 产品优势 | 说明 |
| :--- | :--- |
| 简单易用 | 一键式创建/接入容器集群，实现大规模集群跨云/跨集群的统一管理；图形化创建流水线，满足多场景需求；一站式应用分发，兼容多形态应用 |
| | 无需感知底层 Kubernetes 平台差异性，简化应用部署流程，降低应用上云难度，让用户聚焦业务开发，无需关心底层基础设施 |
| | 为 **让用户像使用单集群一样来使用多集群** 奠定基础 |
| 生产就绪 | 应用高可用，支持应用的分布式部署，支持单点故障流量的自动切换 |
| | 兼容传统微服务框架及云原生框架，传统微服务框架无需改造、无感接入，高度兼容 Zookeeper 等传统注册中心以及云原生的 Kubernetes 和 Mesh 注册中心，同时支持 Spring Cloud、Dubbo 等主流开源微服务框架以及 Envoy、Sentinel、Contour 等开源网关组件 |
| | 丰富的监控指标，实现应用的全方位监控，提前预警应用流量高峰与应用故障 |
| 持续交付 | 应用构建容器化，自定义流水线创建，简化交付流程 |
| | 基于容器技术，实现应用在不同环境中快速部署、验证和流转 |
| | 多形态应用兼容，包容多样性的部署及管理 |
| 安全可靠 | 自建集群默认为高可用部署模式，保障业务高可用；当节点出现故障或发生自然灾害时，应用可持续运行，业务应用系统不中断 |
| | 跨地域应用高可用，支持将业务部署在不同地域的多个云容器集群上；当某个集群发生故障、机房宕机或自然灾害时，通过统一流量分发机制自动将业务流量切换到其他云容器平台 |
| | 提供平台备份与容灾方案，保障平台数据及业务安全 |
| | 三合一监控系统，基于集中式的集群管理，实现集群、节点、组件、应用的多层面多维度监控，快速定位故障、排查故障 |
| | 完善的用户权限体系，整合 Kubernetes RBAC 权限体系，支持为不同用户设置细粒度权限，实现资源隔离，保证业务数据安全性 |
| 混合异构 | 多云异构，实现云上云下、不同厂商容器云平台的异构管理能力 |
| | 提供高度自动化和具备弹性的异构多云支撑能力，适配 x86 以及信创云体系架构 |
| | 支持 x86、ARM 架构混合集群统一部署、统一管理，稳定支撑应用运行，保障应用间网络互通 |
| 开放兼容 | 基于原生的 Kubernetes 和 Docker 技术，全面兼容 Kubernetes API 和 Kubectl 命令 |
| | 提供了丰富的插件体系扩充云容器集群功能，例如 Multus、Cilium、Contour 等[网络插件](../network/intro/index.md) |

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
