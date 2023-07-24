# 工具推荐

本页列出一些云原生社区常用的工具，以期提高 K8s 的用户体验。

- [Kubernetes 解决“近邻干扰”（Noisy Neighbor）场景的探索](https://mp.weixin.qq.com/s/g28ett0Z5LR0sHTyOljCRg)

    当一个租户的性能由于另一个租户的活动而下降时，就会出现 noisy neighbor 问题。
    虽然 Kubernetes 提供了 CPU 管理器、设备插件管理器以及拓扑管理器，协调资源分配和保证关键工作负载的最佳性能，但是没有根本上解决该问题。
    对此，Intel 资源调配技术 RDT 支持通过为三种 Kubernetes QoS 级别配置相应的 RDT 类来限制非关键工作负载对共享资源的访问。

- [FinOps 时代如何玩转应用资源配置](https://mp.weixin.qq.com/s/2ulduH_zKKcCsB64sVI0bg)

    Kubernetes 会按照应用程序申请的资源配额进行调度，因此如何合理的配置应用资源规格就成为提升集群利用率的关键。
    文章分享如何基于 FinOps 开源项目 Crane 正确的配置应用资源，以及如何在企业内推进资源优化的实践。

- [帮助 Go 团队使用 OpenTelemetry 的新方法](https://gethelios.dev/blog/helping-go-teams-implement-opentelemetry-a-new-approach/)

    用 Go 实现 OTel 来向观测平台发送数据并不简单，Go instrumentation 需要大量的手动操作。
    Helios 团队开发了一种[新的 OTel Go instrumentation 方法](https://app.gethelios.dev/get-started)，这种方法将 Go AST 和代理库的结合，易于实现和维护。
    同时，对于最终用户而言，这种方法是非侵入性的，易于理解。

- [为什么在 Kubernetes 中调试应用的体验如此糟糕？](https://mp.weixin.qq.com/s/maI6Nu6r431LtGzrgq_6rg)

    对于开发者而言，想要的是：快速的内部开发循环，可以利用熟悉 IDE 工具来做本地调试；提前发现 bug，避免过早进入 Outer Loop；在内部环境，团队之间的协作可以互不干扰。
    为解决上述痛点，文章介绍了三款工具：Kubernetes 本地开发工具 [Telepresence](https://github.com/telepresenceio/telepresence)、云原生协同开发测试解决方案 [KT-Connect](https://github.com/alibaba/kt-connect) 以及基于 IDE 的云原生应用开发工具 [Nocalhost](https://github.com/nocalhost/nocalhost)。

- [在 K8s 上构建端到端的无侵入开源可观测解决方案](https://mp.weixin.qq.com/s/HUFawiyv55Hi0aEoEPl6rA)

    [Odigos](https://github.com/keyval-dev/odigos) 是一个开源的可观测性控制平面，允许企业在几分钟内创建可观测性管道，集成众多第三方项目、开放标准，降低多个可观测性软件平台和开源软件解决方案的复杂性。
    此外，还允许应用程序在几分钟内提供追踪、指标和日志，重要的是无需修改任何代码，完全无任何侵入性。
    Odigos 能够自动检测集群中每个应用的编程语言，并进行自动检测。

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

- [5 个实用工具，提升 Kubernetes 生产力](https://mp.weixin.qq.com/s/KAg48nzlsL2jxm0sUDo3mw)

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

    Kubernetes 的复杂性使得标准化应用零信任原则成为挑战。默认情况下，kubectl 不启用 RBAC，执行的命令不会被用户账号记录。通过防火墙访问资源很困难，监督多个集群也变得繁杂易错。
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
    与谷歌的 Bazel 和基于 Debian 的系统不同的是，Chainguard 工具链以 [apk](https://github.com/alpinelinux/apk-tools)（Alpine 软件包管理器）、[apko](https://github.com/chainguard-dev/apko)（用来构建基于 Alpine 的 distroless 镜像）和 [melange](https://github.com/chainguard-dev/melange)（使用声明式 pipeline 构建 apk 包）为核心，减少 distroless 镜像的复杂性。

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

    [OPAL](https://github.com/permitio/opal) 是开放策略代理（OPA）的一个管理层，它能够保持授权层的实时更新。
    OPAL 对策略和策略数据的变化进行检测，并将实时更新推送给 agent。当应用状态发生变化时，OPAL 将确保服务始终与所需的授权数据和策略保持同步。

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