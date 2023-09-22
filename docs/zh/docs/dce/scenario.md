---
hide:
  - toc
---

# 适用场景

DCE 5.0 集成社区最优秀的众多技术，内置依赖项数以万计，经海量调测后熔于一炉，铸就新一代 PaaS 服务平台，在各类使用场景中都游刃有余。

## DCE 5.0 场景化视频

我们精心制作了 Step-By-Step 场景化视频，以满足具体的场景化业务需求：

=== "多云和混合云"

    - [如何将单云应用一键转换为多云应用？](../videos/use-cases.md#_2)
    - [如何在 DCE 5.0 中部署混合云应用？](../videos/use-cases.md#dce-50)

=== "流量治理"

    - [如何将微服务接入 DCE 5.0 并治理南北向流量？](../videos/use-cases.md#dce-50_1)
    - [如何借助服务网格治理传统微服务东西向流量？](../videos/use-cases.md#_3)

=== "OEM IN 和 OUT"

    - [如何将客户系统集成到 DCE 5.0？](../videos/use-cases.md#dce-50_3)
    - [如何将 DCE 5.0 集成到客户系统？](../videos/use-cases.md#dce-50_2)

=== "网络和通信"

    - [如何让传统应用上云后仍通过固定 IP 对外通信？](../videos/use-cases.md#ip)
    - [如何实现应用加速与跨集群通信？](../videos/use-cases.md#_4)

=== "CICD 和 GitOps"

    - [如何利用 CICD 快速交付应用？](../videos/use-cases.md#cicd)
    - [如何利用 GitOps 持续部署云原生应用？](../videos/use-cases.md#gitops)

=== "ChatGPT、中间件和故障排查"

    - [如何利用可观测性快速定位异常并排障？](../videos/use-cases.md#_5)
    - [如何用中间件和 pgvector 部署 ChatGPT 应用？](../videos/use-cases.md#pgvector-chatgpt)
    - [如何实现 Redis 的跨集群数据同步？](../videos/use-cases.md#redis)

## DCE 5.0 适用场景

DCE 5.0 从总体上看，可以支持以下场景：

=== "生产级容器管理"

用户在运维团队需要承接数十个至上百个集群运行维护任务，且集群网络规划需满足用户传统网络监管要求。

涉及模块：[容器管理](../kpanda/intro/index.md)、[容器网络](../network/intro/index.md)、容器集群生命周期管理

方案优势：提供集群从部署、升级、证书变更、配置变更、回收等全集群生命周期管理管理能力。
尽可能复用当前企业环境中网络基础设施，针对不同的环境，可以实施的最佳方案有：MacVLAN 网络方案、SR-IOV 智能网卡加速方案、[SpiderPool](../network/modules/spiderpool/index.md) 云原生 IPAM 方案、[Clilum](../network/modules/cilium/index.md) eBPF 网络加速方案、Underlay 和 Overlay 协同网络方案。

通过自主开源的 [Clusterpedia](../community/clusterpedia.md) 统一控制平面管理所有集群及负载信息，兼容标准 Kubernetes 集群接入，突破 Kubernetes API 性能瓶颈，支持上千人同时使用。

=== "多云编排"

用户中多集群、多云部署成为常态，希望能完成多云统一发布，并且拥有跨云容灾备份的能力

涉及模块：[容器管理](../kpanda/intro/index.md)、[多云编排](../kairship/intro/index.md)、[容器网络](../network/intro/index.md)、边云协同、信创云

方案优势：创新性技术完成跨云容灾，跨云资源检索并发性能高，结合容器平台的能力适配边缘、信创场景。

=== "融合微服务"

用户应用架构决定采用微服务架构或已经采用微服务，希望得到全方位的微服务框架等技术支持及运维兜底能力，或希望引入服务网格技术，并且在技术更迭的过程中实现平滑过度。

涉及模块：[容器管理](../kpanda/intro/index.md)、[容器网络](../network/intro/index.md)、[微服务引擎](../skoala/intro/index.md)、[服务网格](../mspider/intro/index.md)、[可观测性](../insight/intro/index.md)、[应用工作台](../amamba/intro/index.md)

方案优势：无缝融合以 SpringCloud、Dubbo 为代表的初代微服务与 Istio 服务网格代表的新一代微服务技术，完成从开发、部署、接入、对外、观测、运维全生命周期微服务管理能力。

=== "云边协同"

用户按照云、边、端方案设计边缘协同方案，边缘端为通用算力平台，且边缘端有较强的算力需求。边缘端支持三种部署模式: 边缘节点、边缘集群模式，边缘集群叠加边缘节点四层架构模式。

涉及模块：[容器管理](../kpanda/intro/index.md)、[容器网络](../network/intro/index.md)、容器集群生命周期管理、边缘节点

方案优势：云端统一管控所有边缘节点、集群信息，在传统的云边端三层模式基础上，针对强边缘算力需求，增加边缘集群迭代边缘节点的方案，形成四层云边协同方案。

=== "信创云原生"

用户有信创需求，对底层基础设施及操作系统有特定要求，例如处理器：Loongson 龙芯、海光、飞腾、鲲鹏、intel；操作系统：麒麟、统信 UOS、OpenEuler 等。

涉及模块：[容器管理](../kpanda/intro/index.md)、[容器网络](../network/intro/index.md)、容器集群生命周期管理

方案优势：北向支持国产芯片及服务器，南向支持容器内信创操作系统及信创应用生态体系。

=== "应用交付"

用户大规模采用云原生技术，并且期望规范化、流程化结合 DevOps 理念将云原生技术推广至更广泛的应用项目组。

涉及模块：[容器管理](../kpanda/intro/index.md)、[应用工作台](../amamba/intro/index.md)、[容器网络](../network/intro/index.md)、[镜像仓库](../kangaroo/index.md)、边云协同、信创云

方案优势：支持层级多租户体系，无缝适配用户组织架构规划资源分配。
CI/CD 流水线能力自动化完成应用构建、部署工作。创新性引入 GitOps、渐进式交付的能力体系，帮助应用进行更细致的交付管理能力。

=== "云原生可观测"

用户对运行应用观测能力较弱，希望能轻量级或无改造接入就能完成观测接入，完成全方位的应用运行观测（日志、指标、链路）。

涉及模块：[容器管理](../kpanda/intro/index.md)、[可观测性](../insight/intro/index.md)、[容器网络](../network/intro/index.md)、边云协同、信创云

方案优势：观测数据统一汇总，一个控制面板就能查询到所有集群及负载观测数据，并且深入支持微服务架构、[服务网格](../mspider/intro/index.md)、网络 EBPF 观测能力。

=== "数据服务"

用户应用架构依赖主流中间件能力，希望能统一运行维护中间件，并且得到较为专业的关于中间件规划、运维的支持能力。

涉及模块：[容器管理](../kpanda/intro/index.md)、[容器网络](../network/intro/index.md)、[容器本地存储](../storage/index.md)、[云原生中间件](../middleware/index.md)、边云协同、信创云

方案优势：专为有状态应用设计的云原生本地存储能力，统一平台管理云原生中间件，提供多租户、部署、观测、备份、运维的全生命周期的中间件管理能力，结合容器平台的能力适配边缘、信创场景。

=== "应用商店"

用户希望获得专属场景开箱即用的云原生应用软件能力。

涉及模块：[容器管理](../kpanda/intro/index.md)、应用商店

方案优势：收录来自生态伙伴十大领域的软件产品，面向企业实际业务需求提供完整软件堆栈，可轻松查找、测试、和部署在 DaoCloud Enterprise 上运行的消息中间件、数据中间件、低代码/无代码应用等。

[下载 DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](license0.md){ .md-button .md-button--primary }
[DCE 5.0 场景化视频](../videos/use-cases.md){ .md-button .md-button--primary }
