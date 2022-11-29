# 知识分享

本页分享一些云原生相关的知识，愿大家携手共进。

## 排障方案

- [K8s：彻底解决节点本地存储被撑爆的问题](https://mp.weixin.qq.com/s/pKTA6O3bdko_eHaw5mU3gQ)

    K8s 节点本地存储保存了镜像、可写层、日志、emptyDir 等内容。除了容器镜像是系统机制控制的，其它都跟应用程序有关。完全依赖开发者对应用使用的存储空间进行限制并不可靠，因此，K8s 提供了垃圾回收、日志总量限制、emptyDir 卷限制、临时数据总量限制来避免本地存储不够用的问题。

- [K8s 有损发布问题探究](https://mp.weixin.qq.com/s/jKVw0m5Ho2AtFRScnKEMKw)

    应用发布过程其实是新 Pod 上线和旧 Pod 下线的过程，当流量路由规则的更新与应用 Pod 上下线配合出现问题时，就会出现流量损失。总的来说，为了保证流量无损，需要从网关参数和 Pod 生命周期探针和钩子来保证流量路径和 Pod 上下线的默契配合。文章从 K8s 的流量路径入手，分析有损发布产生的原因，并给出解决方案。

- [K8s：Pod 的 13 种异常](https://mp.weixin.qq.com/s/cEEdH7npkSHmVHSXLbH6uQ)

    文章总结了 K8s Pod 的 13 种常见异常场景，给出各个场景的常见错误状态，分析其原因和排查思路。

- [K8s: 你需要知道的一切](https://enterprisersproject.com/sites/default/files/2022-11/tep_white-paper_kubernetes-what-you-need-to-know%2Brev2.pdf)

    电子书囊括了了解 Kubernetes 所需的所有定义，同时也包含了与 Kubernetes 相关的其他电子书、文章、教学视频等资源的介绍，以及 7 个最佳实践。

- [Docker Volume 引发 K8s Terminating Pod 的问题](https://mp.weixin.qq.com/s/SMynKYP4obMSl6GQdwDlEw)

    Terminating Pod 是业务容器化后遇到的一个典型问题，诱因不一。文章记录了网易数帆-轻舟 Kubernetes 增强技术团队如何一步步排查，发现 Docker Volume 目录过多导致 Terminating Pod 问题的经历，并给出了解决方案。

- [安装 Kubernetes 或升级主机操作系统后出现网络问题？这可能是你的 iptables 版本有问题](https://www.mirantis.com/blog/networking-problems-after-installing-kubernetes-1-25-or-after-upgrading-your-host-os-this-might-be-your-problem)

    安装新版本的 Kubernetes 后，你的工作节点连接不上网络，突然间无法 ssh 访问甚至无法 ping 它们？这可能是因为 kube-router 1.25 的 iptables 版本和你安装的版本之间出现冲突。归根结底是因为 iptables 1.8.8 和旧版本的规则格式不兼容。对此，有三个解决方案：将 iptables 版本降到 1.8.7、清理 IPTables 链所有权（alpha）或是借助轻量级的 Kubernetes 发行版 [k0s](https://github.com/k0sproject/k0s) 解决。

- [**利用 eBPF 进行 Kubernetes 集群磁盘 I/O 性能问题排查**](https://mp.weixin.qq.com/s/RrTjhSJOviiINsy-DURV2A)

    问题始于 eBay 工程师发现他们的 Kafka 服务在有些时候 follower 追不上 leader 的数据。为解决问题，利用了一些 eBPF 工具，例如，[biopattern](https://github.com/iovisor/bcc/blob/master/tools/biopattern.py) 用于展示 disk I/O pattern，[ebpf_exporter](https://github.com/cloudflare/ebpf_exporter) 用于数据收集和可视化。

## 最佳实践

- [K8s：利用 Mutating Admission Controller 简化应用的环境迁移](https://blog.getambassador.io/using-mutating-admission-controllers-to-ease-kubernetes-migrations-5699c1901015)
  
    Kubernetes 的 Mutating Admission Webhook 通常用于执行安全实践，确保资源遵循特定的策略或配置管理。文章介绍了一个新的用例：简化应用的迁移，实现快速更新新环境的清单，同时保持旧环境正常运行。

- [阿里云容器攻防矩阵 & API 安全生命周期，如何构建金融安全云原生平台](https://mp.weixin.qq.com/s/ZKsIn0UzrrSGWWMv8Sk4Nw)

    文章从攻击者视角介绍了容器平台（容器攻防矩阵）和 API 在金融科技领域的应用所带来的威胁面，分析威胁，并给出容器平台和 API 全生命周期的安全防护实践建议。

- [**全球顶级开源公司是如何找到前 1000 名社区用户的？**](https://mp.weixin.qq.com/s/edy6FsD1d_9fp-U60H_dug)

    文章分享了 4 个顶级开源商业公司（HashiCorp、Confluent、Databricks 和 CockroachDB）的开源项目和开源社区的运作方式，如何找到前 1000 名社区用户及花了多长时间，以及增长衡量指标等。

- [**容器云多集群环境下如何实践 DevOps**](https://mp.weixin.qq.com/s/MW67DhLzUWXm0xHd5LH0Tw)

    文章介绍了如何通过 GitOps 来实现多集群 DevOps，并推荐了一种多集群 GitOps 工作流作为落地参考，最后介绍了在持续集成和持续交付中具体实践 GitOps 的主流方式。

- [**Kubernetes HPA 的三个误区与避坑指南**](https://mp.weixin.qq.com/s/3eSm0BZSrPUAZQQhG_L_5A)

    Kubernetes 提供了水平弹性扩容能力（HPA），让应用可以随着实时指标进行扩/缩。然而 HPA 的实际工作情况可能和我们预想的不一样，这里存在一些认知误区，例如，HPA 存在扩容死区、扩容与预期使用量不符、弹性行为总是滞后等。对此，文章总结了一些注意事项，帮助在使用 HPA 时“有效避坑。

- [**是时候思考 K8s 出向流量安全了（上）**](https://mp.weixin.qq.com/s/Lj3sl-Ukday9WP4U-8-vqA)[**&（下）**](https://mp.weixin.qq.com/s/NMh1XbBXeyfGuJJ8kZ6J2Q)

    我们往往重视 Ingress 的能力，而忽视了 Egress 流量的安全管控。但无论从安全还是合规的角度，Egress 流量都应加强管控。文章分析了进行 Egress 流量策略管控的原因、存在的挑战以及业界方案分析。方案包括六大类：基于 K8s Network Policy、CNI、Service Mesh、微分段技术以及 DNS interception。

- [**如何保障云原生集群安全**](https://mp.weixin.qq.com/s/sv40SzD7Ic1eMeElvccs7A)

    文章为容器集群安全交流论坛的内容汇总。内容包括：云集群安全的分类以及预防及解决方案、容器云上集群划分原则、集群审计、节点安全保障、etcd 集群安全、设计网络策略保障集群资源的安全、网络隔离问题、按照安全等保级别针对 k8s 集群的标准化策略或配置等。

- [**Kubernetes 控制平面应该有多少个节点**](https://thenewstack.io/how-many-nodes-for-your-kubernetes-control-plane/)

    文章为确定 Kubernetes 控制平面的大小提供了参考。对于大多数用例，3 个节点足以。5 个节点将提供更好的可用性，但在所需节点数量和硬件资源消耗方面成本更高。此外，监控、备份 etcd 和控制平面节点配置是解决节点故障、预防意外的最佳实践方案。

- [**利用 Istio 减少跨可用区流量开销**](https://www.tetrate.io/blog/minimizing-cross-zone-traffic-charges-with-istio/)

    跨可用区部署 Kubernetes 集群具备显著的可靠性优势，但需要一些额外的配置在本地保持流量。Istio 的本地感知路由可以帮助减少延迟，并将云供应商对应用流量的跨区数据收费降到最低。

- [**2 分钟测试 Kubernetes Pod 的安全**](https://dzone.com/articles/the-2-minute-test-for-kubernetes-pod-security)

    从集群外部运行 [Kyverno CLI](https://github.com/kyverno/kyverno)，审计集群是否符合最新的 [Kubernetes Pod 安全标准](https://kubernetes.io/docs/concepts/security/pod-security-standards/)的要求，并为 pod 安全标准中定义的每个控制执行策略。执行审计不需要在集群中安装任何东西。

- [**Proxyless Mesh 在 Dubbo 中的实践**](https://mp.weixin.qq.com/s/TH8waHN00y6q26NUDY9wzg)

    [Dubbo Proxyless Mesh](https://github.com/apache/dubbo-awesome/blob/master/proposals/D3.2-proxyless-mesh.md) 直接实现 xDS 协议解析，实现 Dubbo 与 Control Plane 的直接通信，进而实现控制面对流量管控、服务治理、可观测性、安全等的统一管控，规避 Sidecar 模式带来的性能损耗与部署架构复杂性。

- [**零信任策略下 K8s 安全监控最佳实践**](https://mp.weixin.qq.com/s/wYUNsGaWEnQZ0BVxsQORbA)

    文章介绍如何在分布式容器化环境中借助 K8s 相关的安全数据源及采集技术，监控 K8s 集群，及时发现异常 API 访问事件、异常流量、异常配置、异常日志等行为，并且结合合理的告警策略建立更主动的安全防御体系。

## 工具推荐

- [ChaosBlade：大规模 Kubernetes 集群故障注入的利器](https://mp.weixin.qq.com/s/gh4GVnOY_QVU2D2VeyWCeA)

    [ChaosBlade](https://github.com/chaosblade-io/chaosblade) 是一款遵循混沌工程原理和混沌实验模型的实验注入工具，帮助企业提升分布式系统的容错能力，并且为企业在上云或往云原生迁移过程中提供业务连续性保障。文章主要介绍 ChaosBlade 在 Kubernetes 中故障注入的底层实现原理、版本优化过程以及大规模应用演练测试。

- [OpenFeature 和 Feature Flag 标准化如何造就高质量的持续交付](https://www.dynatrace.com/news/blog/openfeature-and-feature-flag-standardization/)

    Feature Flag 即功能开关或功能发布控制，是一种通过配置开关功能特性的技术，无需重新部署代码。而 [OpenFeature](https://github.com/open-feature)，是一个关于 Feature Flag 的开放标准，旨在使用云原生技术构建一个强大的 Feature Flag 生态系统，允许团队灵活地选择符合当前需求的 feature flag 方法，并在需求发生变化时切换到其他方法。

- [Traffic Director: 在 GKE 上 使用 Envoy gateway 代理实现 TLS 路由](https://cloud.google.com/blog/products/networking/tls-routing-using-envoy-gateway-proxy-on-gke)

    Traffic Director 是谷歌托管的服务网格控制平面，用于解决微服务流量的治理问题。文章分享了一个架构样本，在 GKE 集群上，使用 Traffic Director 配置 Envoy gateway 代理，使用 TLS 路由规则，将集群外的客户端流量路由到部署在集群上的工作负载。此外，演示了如何利用 Envoy 代理作为入口网关，使南北流量进入服务网格，以及使用[服务路由 API](https://cloud.google.com/traffic-director/docs/service-routing-overview#:~:text=The%20service%20routing%20APIs%20let,two%20HTTPRoute%20resources%20configure%20routing.) 来路由这些流量，最后还分享了一些故障排除技巧。

- [Quarkus 的 Java 框架如何用于 serverless function 开发？](https://mp.weixin.qq.com/s/oeJjQtqK8h2JSGy4wOlQ6w)

    [Quarkus](https://github.com/quarkusio/quarkus) 解决了传统框架内存消耗大和容器环境的扩展问题。通过 Quarkus，开发人员可以使用熟悉的技术构建云原生微服务和 serverless function。文章介绍如何开始使用 Quarkus 进行 serverless function 开发、如何优化 function 并实现持续测试，以及制作跨 serverless 平台的可移植 function 等。

- [K8s CNI 插件选型和应用场景探讨](https://mp.weixin.qq.com/s/GG7GX_E1oyZf-cmjk80OYg)

    文章介绍容器环境常见七个网络应用场景及对应场景的 Kubernetes CNI 插件功能实现。

- [**云原生时代的 DevOps 平台设计之道（Rancher vs KubeSphere vs Rainbond）**](https://mp.weixin.qq.com/s/oxeNq4GHE85NUBIDcgixcg)

    文章重点介绍了 Rancher 、KubeSphere、Rainbond 三款云原生平台级产品各自不同的 DevOps 实现。作者认为，DevOps 团队可以选择 Rancher + KubeSphere 或 Rancher + Rainbond 的组合。Rancher 最擅长向下对接基础设施，管理集群的安全性与合规性，而向上为开发人员提供易用的云原生平台则交给 KubeSphere 或 Rainbond。

- [**GitLab + Jenkins + Harbor 工具链快速落地指南**](https://mp.weixin.qq.com/s/fA38H5up9VqZ3zEBy1eXnA)

    文章介绍了如何利用 DevOps 工具链管理器 [DevStream](https://github.com/devstream-io/devstream) 快速部署 DevOps 工具链（GitLab + Jenkins + Harbor）。

- [**Helm 部署高可用 Harbor 镜像仓库**](https://mp.weixin.qq.com/s/ev_QE9NhwiCcLHpapbAU7A)

    文章介绍如何使用 Helm 包管理工具将 harbor 部署在 kubernetes 集群中并且实现高可用。

- [**微软 Azure 在容器供应链安全的开源实践**](https://mp.weixin.qq.com/s/bXt-pPID4CyDyp0XEmDyZQ)

    文章主要介绍 Azure 在容器供应链安全领域的开源实践，例如：[Microsoft/SBOM Tool](https://github.com/microsoft/sbom-tool) 生成 SBOM 文件，[Notary v2](https://github.com/notaryproject/notation) 对容器镜像等软件制品进行签名和验证，[ORAS](https://github.com/oras-project/oras) 扩展 OCI 赋能供应链安全，[Ratify](https://github.com/deislabs/ratify) 帮助 Kubernetes 验证应用的部署安全。

- [**vcluster -- 基于虚拟集群的多租户方案**](https://mp.weixin.qq.com/s/831cv8ONpzcJ3FJeyQ3sxQ)

    虚拟集群即 vcluster 是在常规的 Kubernetes 集群之上运行的一个功能齐全、轻量级、隔离性良好的 Kubernetes 集群。其核心思想是提供运行在“真实”集群之上隔离的 Kubernetes 控制平面（例如 API Server）。与完全独立的“真实“集群相比，虚拟集群没有自己的工作节点或者网络，工作负载实际上还是在底层宿主集群上调度。

- [**5个实用工具，提升 Kubernetes 生产力**](https://mp.weixin.qq.com/s/KAg48nzlsL2jxm0sUDo3mw)

    文章列出了五种与 Kubernetes 一起工作的强大工具，分别是终端 UI [K9s](https://github.com/derailed/k9s)、清理 Kubernetes 集群的工具 [Popeye](https://github.com/derailed/popeye)、Kubernetes 集群部署检查工具  [Kube-bench](https://github.com/aquasecurity/kube-bench)、上下文和命名空间快速切换工具 [Kubectx](https://github.com/ahmetb/kubectx)、[Kubens](https://github.com/ahmetb/kubectx) 和 [fzf](https://github.com/junegunn/fzf)、日志聚合器 [Stern](https://github.com/stern/stern)、从 shell 快速检查文件 [Bat](https://github.com/sharkdp/bat)。

- [**利用 Open Cluster Management（OCM） 的 Placement 扩展多集群调度能力**](https://cloud.redhat.com/blog/extending-the-multicluster-scheduling-capabilities-with-open-cluster-management-placement)

    在 K8s 多集群管理项目 OCM 中，多集群调度能力由 [Placement](https://github.com/open-cluster-management-io/placement) 控制器提供。Placement 提供了一些默认的优先级排序器，用于分类和选择最合适的集群。在某些情况下，排序器需要更多的数据来计算集群的得分。因而，我们需要一种可扩展的方式来支持基于自定义得分的调度。

- [**开源云原生安全治理平台 HummerRisk**](https://mp.weixin.qq.com/s/00cER0lVP2u40GROPP_ZbA)

    [HummerRisk](https://github.com/HummerRisk/HummerRisk) 是一个开源的云安全治理平台，以非侵入的方式对云原生环境进行全面安全检测，核心解决三个方面的问题，底层的混合云安全合规，中层的 K8s 容器云安全和上层的软件安全。

- [**使用 Config Sync 以 GitOps 的方式部署 OCI 工件和 Helm charts**](https://cloud.google.com/blog/products/containers-kubernetes/gitops-with-oci-artifacts-and-config-sync)

    [Config Sync](https://github.com/GoogleContainerTools/kpt-config-sync) 是一个开源工具，为 Kubernetes 集群提供 GitOps 持续交付。它能够通过 GitOps 的方式来存储和部署 Kubernetes 清单，把 Kubernetes 清单打包成一个容器镜像，并且使用与容器镜像相同的认证和授权机制。

- [**突破 Kubernetes 对自定义资源数量的限制**](https://mp.weixin.qq.com/s/LV83vuMZ641HzL7bKUE05g)

    Crossplane 社区发现了 Kubernetes 能够处理的 CRD 上限，并且帮助解决了这些问题。其中，限制原因包括：限制性的客户端速率限制器、缓慢的客户端缓存、低效的 OpenAPI 模式计算、冗余高昂的成本、etcd 客户端。

- [**K8s DevOps 平台 TAP 基于 Knative 的云原生运行时**](https://mp.weixin.qq.com/s/kvUDvEVaNC3qordCtaMosw)

    TAP 的云原生应用运行时抽象层（CNR）的核心是 Knative。TAP 提供了一个 Runtime 运行时层，既支持用户使用 K8S Deployment 和 Service,也可以使用 Knative Serving, Scale From/To Zero,Eventing 和 Streaming 等。

- [**到底谁强？Grafana Mimir 和 VictoriaMetrics 性能测试**](https://mp.weixin.qq.com/s/TVJZ5k5U7bs8WEyE4rikSQ)

    文章比较 VictoriaMetrics 和 Grafana Mimir 集群在相同硬件上运行的工作负载的性能和资源使用情况。在基准测试中，与 Mimir 相比，VictoriaMetrics 表现出更高的资源效率和性能。从操作上讲，VictoriaMetrics 扩展更为复杂，Mimir 可以很容易实现组件扩展。

- [**使用 Tekton 和 Kyverno 的基于策略的方法来保障 CI/CD 管道的安全**](https://www.cncf.io/blog/2022/09/14/protect-the-pipe-secure-ci-cd-pipelines-with-a-policy-based-approach-using-tekton-and-kyverno/)

    [Tekton](https://github.com/tektoncd/pipeline) 提供了一个强大的 CI/CD 框架，并且通过 Tekton Chains 等扩展确保构建工件的安全。[Kyverno](https://github.com/kyverno/kyverno) 可用于管理策略，实现基于命名空间的隔离，并为 Tekton 管道生成安全资源。此外，还可以签署 OCI 工件，如 Tekton 捆绑物。Tekton 和 Kyverno 的强大组合使软件构建和交付系统的安全和自动化达到了新的水平。

- [**K8S 运维开发调试神器 Telepresence 实践指南**](https://mp.weixin.qq.com/s/Yu5z9w26rqgVHkEYhg1t2g)

    [Telepresence](https://github.com/telepresenceio/telepresence) 可用于在本地运行单个服务，同时将该服务连接到远程 Kubernetes 集群。Telepresence 提供了 3 个非常重要的功能：cluster 域名解析、cluster 流量代理和 cluster 流量拦截。

## 前沿热点

- [eBPF 程序摄像头——力争解决可观测性领域未来最有价值且最有挑战的难题](https://mp.weixin.qq.com/s/FYNe1H5dmBpbKFOrIpjuzQ)
  
    当前可观测性用户很容易迷失在指标迷阵当中，不知该在什么时间查看何种指标，如何理解大规模细粒度的指标。为解决此问题，Kindling 社区选择了基于 eBPF 的可观测性摄像头，按照 eBPF 粒度去获取程序执行过程当中的细粒度指标，帮助用户理解程序执行的真实过程，同时理解细粒度的指标是如何影响程序执行的。

- [GitOps 是皇帝的新衣吗](https://mp.weixin.qq.com/s/CpLvQM2rTI4InIN1Vk5ZKg)

    在采用 GitOps 前，我们需要了解清楚“什么是 GitOps？”，并问自己“我们使用这些工具为谁提供服务？我们试图解决什么问题？”文章针对 GitOps 的一些主要“卖点”（包括安全性、版本控制和环境历史、回滚、飘逸处理、单一真相来源等）提出了质疑，并介绍了 GitOps 带来的一些挑战。

- [**蚂蚁规模化平台工程实践两年多，我们学到了什么**](https://mp.weixin.qq.com/s/X8AWh43qp4fb4eJSkx50hw)

    平台工程是一门设计与构建工具链和工作流程的学科，可以为云原生时代的软件工程组织提供自助式服务功能。文章基于可编程云原生协议栈 [KusionStack](https://github.com/KusionStack) 在蚂蚁平台工程及自动化中的实践，从平台工程、专用语言、分治、建模、自动化和协同文化等几个角度，阐述规模化平台工程实践中的收益和挑战。

- [**可观测可回溯 | 持续性能分析 Continuous Profiling 实践解析**](https://mp.weixin.qq.com/s/yiwq81ZHB0nSTcYSjOeyZg)

    持续性能分析（简称 CP）对于开发者的意义在于，在生产环节，永远知道代码的所有执行细节。文章在介绍 CP 发展历史的基础上，分析了性能分析 profiling 的 2 个关键点：获取堆栈数据和生成火焰图，以及常见的 profiling tool。

## 安全漏洞

- [Istio 高风险漏洞：拥有 localhost 访问权限的用户可以冒充任何工作负载的身份](https://github.com/istio/istio/security/advisories/GHSA-6c6p-h79f-g6p4)

    如果用户拥有 Istiod 控制平面的 localhost 访问权，他们可以冒充服务网格内的任何工作负载身份。受影响的版本为 1.15.2。目前，已发布补丁版本 [1.15.3](https://github.com/istio/istio/releases/tag/1.15.3)。

- [**Istio 高风险漏洞：Golang Regex 库导致 DoS 攻击**](https://github.com/istio/istio/security/advisories/GHSA-86vr-4wcv-mm9w)

    Istiod 存在请求处理错误漏洞，攻击者会在 Kubernetes validating 或 mutating webhook 服务曝光时，发送自定义或超大消息，导致控制平面崩溃。目前，[Istio](https://github.com/istio/istio/releases) 已发布补丁版本 1.15.2、1.14.5 和 1.13.9。低于 1.14.4、1.13.8 或 1.12.9 的版本会受此影响。

- [**CrowdStrike 发现针对 Docker 和Kubernetes 基础设施的新型挖矿攻击**](https://www.crowdstrike.com/blog/new-kiss-a-dog-cryptojacking-campaign-targets-docker-and-kubernetes/)

    该攻击通过容器逃逸技术和匿名矿池，使用一个模糊的域名来传递其有效负载，以对 Docker 和 Kubernetes 基础设施开展加密货币挖掘活动。采用云安全保护平台能够有效保护云环境免受类似的挖矿活动的影响，防止错误配置和控制平面攻击。

- [**Kube-apiserver CVE 漏洞: 聚合 API server 可能导致服务器请求伪造问题（SSRF）**](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#cve-2022-3172-aggregated-api-server-can-cause-clients-to-be-redirected-ssrf)

    攻击者可能控制聚合 API Server，将客户端流量重定向到任何 URL。这可能导致客户端执行意外操作，或将客户端证书泄露给第三方。此问题没有缓解措施。集群管理员应注意保护聚合 API Server，不允许不受信任方访问 mutate API Services。受影响版本：kube-apiserver 1.25.0、1.24.0 - 1.24.4、1.23.0 - 1.23.10、1.22.0 - 1.22.14。已修复版本：1.25.1、1.24.5、1.23.11、1.22.14。

## 电子书

- [**白皮书《云原生成熟度矩阵评估》中文版**](https://mp.weixin.qq.com/s/xLuAOXwCVif7KrrpZIcUow)

    白皮书为正处于云原生转型的企业总结了一套云原生成熟度矩阵评估流程。从文化、产品、团队、流程、架构、维护、交付、配置、基础设施 9 个领域评估组织当前所处的状态。同时，阐明 4 种经典的云原生转型误区，并总结出典型的云原生转型方案。  
    点击阅读[白皮书](https://pan.baidu.com/s/1qfEqtL-LCbBo9GhnZBcyyg)，提取码：kvrv

- [**电子书《零信任的基石：使用 SPIFFE 为基础设施创建通用身份》**](https://mp.weixin.qq.com/s/3qwVW8AeyRvUVxYAq22XKg)

    这本书介绍了服务身份的 SPIFFE 标准，以及 SPIFFE 的参考实现 SPIRE。深入阐述了如何设计一个 SPIRE 部署、与其他系统集成的方法、如何使用 SPIFFE 身份通知授权、与其他安全技术对比等。

## 其他

- [2022 年容器生态系统的 9 大趋势洞察](https://mp.weixin.qq.com/s/WNanrbCsdWEuyWP8WvO8UQ)
  
    Datadog 对客户运行的超 15 亿个容器进行了分析，总结出容器生态系统的主要趋势：无服务器容器技术在公共云中的使用率持续上升、多云使用率和组织的容器数量正相关、Kubernetes Ingress 使用率正在上升、大多数主机使用超过 18 个月的 Kubernetes 版本、超过 30% 的运行 containerd 的主机使用不受支持的版本、NGINX、Redis 和 Postgres 是最受欢迎的容器镜像。

- [Karmada 大规模测试报告发布，突破 100 集群和 50 万节点](https://karmada.io/zh/blog/2022/10/26/test-report/)

    近日，Karmada 社区对 Karmada 开展了大规模测试工作。根据测试结果分析，以 Karmada 为核心的集群联邦可以稳定支持 100 个集群和 50 万个节点同时在线，管理超过 200 万个Pod。在使用场景方面，Push 模式适用于管理公有云上的 Kubernetes 集群，而 Pull 模式相对于 Push 模式涵盖了私有云和边缘相关的场景。在性能和安全性方面，Pull 模式的整体性能要优于 Push 模式。

- [toB 应用私有化交付技术发展历程和对比](https://mp.weixin.qq.com/s/JcDZxabHImljPCEus_inlg)

    在传统应用交付中，管理运行环境和操作系统差异是一个痛点。当前云原生应用交付使用容器和 kubernetes 相关技术解决了这个问题，但是这些技术的学习和使用门槛太高。因而，抽象的应用模型成为下一代解决方案，例如，基于 OAM 的 KubeVela 应用交付和基于 RAM 的 Rainbond 应用交付。

- [**国内外云厂商容器服务备份恢复方案调研**](https://mp.weixin.qq.com/s/P71vBPiID8o1GI6pqbaO6w)

    文章对四家厂商的容器服务备份恢复方案（阿里云容器服务 ACK、腾讯云容器服务 TKE、华为云备份产品 CBR、谷歌云 Backup for GKE）进行了调研分析，比较各自的优缺点。

- [**云原生网关 Apache APISIX 3.0 与 Kong 3.0 功能背后的趋势**](https://mp.weixin.qq.com/s/hyqqDojuzEU-LvfR5deBZw)

    文章详细分析了两个 API 网关项目 APISIX 和 Kong 的最新版本，试图从更新细节洞察有价值的技术趋势。Kong 3.0 开始逐渐倾向于企业版，侧重政府、金融业以及对安全合规更关注的大型企业。而 APISIX 3.0 版本推出的所有功能都是开源的，在保证性能的同时，也在积极扩展周边生态。

- [**Kubernetes Node 组件指标梳理**](https://mp.weixin.qq.com/s/nrKk7tuARnvfnH0VOF7q9Q)

    文章对 kubelet 自身指标、kube-proxy 指标、kube-state-metrics 指标以及 cadvisor 指标进行了完整梳理。
