# 知识分享

## 排障方案

- [**K8s：彻底解决节点本地存储被撑爆的问题**](https://mp.weixin.qq.com/s/pKTA6O3bdko_eHaw5mU3gQ)

    K8s 节点本地存储保存了镜像、可写层、日志、emptyDir 等内容。除了容器镜像是系统机制控制的，其它都跟应用程序有关。完全依赖开发者对应用使用的存储空间进行限制并不可靠，因此，K8s 提供了垃圾回收、日志总量限制、emptyDir 卷限制、临时数据总量限制来避免本地存储不够用的问题。

- [**K8s 有损发布问题探究**](https://mp.weixin.qq.com/s/jKVw0m5Ho2AtFRScnKEMKw)

    应用发布过程其实是新 Pod 上线和旧 Pod 下线的过程，当流量路由规则的更新与应用 Pod 上下线配合出现问题时，就会出现流量损失。总的来说，为了保证流量无损，需要从网关参数和 Pod 生命周期探针和钩子来保证流量路径和 Pod 上下线的默契配合。文章从 K8s 的流量路径入手，分析有损发布产生的原因，并给出解决方案。

- [**K8s：Pod 的 13 种异常**](https://mp.weixin.qq.com/s/cEEdH7npkSHmVHSXLbH6uQ)

    文章总结了 K8s Pod 的 13 种常见异常场景，给出各个场景的常见错误状态，分析其原因和排查思路。

- [**K8s: 你需要知道的一切**](https://enterprisersproject.com/sites/default/files/2022-11/tep_white-paper_kubernetes-what-you-need-to-know%2Brev2.pdf)

    电子书囊括了了解 Kubernetes 所需的所有定义，同时也包含了与 Kubernetes 相关的其他电子书、文章、教学视频等资源的介绍，以及 7 个最佳实践。

- [**Docker Volume 引发 K8s Terminating Pod 的问题**](https://mp.weixin.qq.com/s/SMynKYP4obMSl6GQdwDlEw)

    Terminating Pod 是业务容器化后遇到的一个典型问题，诱因不一。文章记录了网易数帆-轻舟 Kubernetes 增强技术团队如何一步步排查，发现 Docker Volume 目录过多导致 Terminating Pod 问题的经历，并给出了解决方案。

- [**安装 Kubernetes 或升级主机操作系统后出现网络问题？这可能是你的 iptables 版本有问题**](https://www.mirantis.com/blog/networking-problems-after-installing-kubernetes-1-25-or-after-upgrading-your-host-os-this-might-be-your-problem)

    安装新版本的 Kubernetes 后，你的工作节点连接不上网络，突然间无法 ssh 访问甚至无法 ping 它们？这可能是因为 kube-router 1.25 的 iptables 版本和你安装的版本之间出现冲突。归根结底是因为 iptables 1.8.8 和旧版本的规则格式不兼容。对此，有三个解决方案：将 iptables 版本降到 1.8.7、清理 IPTables 链所有权（alpha）或是借助轻量级的 Kubernetes 发行版 [k0s](https://github.com/k0sproject/k0s) 解决。

## 最佳实践

- [**K8s：利用 Mutating Admission Controller 简化应用的环境迁移**](https://blog.getambassador.io/using-mutating-admission-controllers-to-ease-kubernetes-migrations-5699c1901015)
  
    Kubernetes 的 Mutating Admission Webhook 通常用于执行安全实践，确保资源遵循特定的策略或配置管理。文章介绍了一个新的用例：简化应用的迁移，实现快速更新新环境的清单，同时保持旧环境正常运行。

- [**阿里云容器攻防矩阵 & API 安全生命周期，如何构建金融安全云原生平台**](https://mp.weixin.qq.com/s/ZKsIn0UzrrSGWWMv8Sk4Nw)

    文章从攻击者视角介绍了容器平台（容器攻防矩阵）和 API 在金融科技领域的应用所带来的威胁面，分析威胁，并给出容器平台和 API 全生命周期的安全防护实践建议。

## 工具推荐

- [**ChaosBlade：大规模 Kubernetes 集群故障注入的利器**](https://mp.weixin.qq.com/s/gh4GVnOY_QVU2D2VeyWCeA)

    [ChaosBlade](https://github.com/chaosblade-io/chaosblade) 是一款遵循混沌工程原理和混沌实验模型的实验注入工具，帮助企业提升分布式系统的容错能力，并且为企业在上云或往云原生迁移过程中提供业务连续性保障。文章主要介绍 ChaosBlade 在 Kubernetes 中故障注入的底层实现原理、版本优化过程以及大规模应用演练测试。

- [**OpenFeature 和 Feature Flag 标准化如何造就高质量的持续交付**](https://www.dynatrace.com/news/blog/openfeature-and-feature-flag-standardization/)

    Feature Flag 即功能开关或功能发布控制，是一种通过配置开关功能特性的技术，无需重新部署代码。而 [OpenFeature](https://github.com/open-feature)，是一个关于 Feature Flag 的开放标准，旨在使用云原生技术构建一个强大的 Feature Flag 生态系统，允许团队灵活地选择符合当前需求的 feature flag 方法，并在需求发生变化时切换到其他方法。

- [**Traffic Director: 在 GKE 上 使用 Envoy gateway 代理实现 TLS 路由**](https://cloud.google.com/blog/products/networking/tls-routing-using-envoy-gateway-proxy-on-gke)

    Traffic Director 是谷歌托管的服务网格控制平面，用于解决微服务流量的治理问题。文章分享了一个架构样本，在 GKE 集群上，使用 Traffic Director 配置 Envoy gateway 代理，使用 TLS 路由规则，将集群外的客户端流量路由到部署在集群上的工作负载。此外，演示了如何利用 Envoy 代理作为入口网关，使南北流量进入服务网格，以及使用[服务路由 API](https://cloud.google.com/traffic-director/docs/service-routing-overview#:~:text=The%20service%20routing%20APIs%20let,two%20HTTPRoute%20resources%20configure%20routing.) 来路由这些流量，最后还分享了一些故障排除技巧。

- [**Quarkus 的 Java 框架如何用于 serverless function 开发？**](https://mp.weixin.qq.com/s/oeJjQtqK8h2JSGy4wOlQ6w)

    [Quarkus](https://github.com/quarkusio/quarkus) 解决了传统框架内存消耗大和容器环境的扩展问题。通过 Quarkus，开发人员可以使用熟悉的技术构建云原生微服务和 serverless function。文章介绍如何开始使用 Quarkus 进行 serverless function 开发、如何优化 function 并实现持续测试，以及制作跨 serverless 平台的可移植 function 等。

- [**K8s CNI 插件选型和应用场景探讨**](https://mp.weixin.qq.com/s/GG7GX_E1oyZf-cmjk80OYg)

    文章介绍容器环境常见七个网络应用场景及对应场景的 Kubernetes CNI 插件功能实现。

## 前沿热点

- [**eBPF 程序摄像头——力争解决可观测性领域未来最有价值且最有挑战的难题**](https://mp.weixin.qq.com/s/FYNe1H5dmBpbKFOrIpjuzQ)
  
    当前可观测性用户很容易迷失在指标迷阵当中，不知该在什么时间查看何种指标，如何理解大规模细粒度的指标。为解决此问题，Kindling 社区选择了基于 eBPF 的可观测性摄像头，按照 eBPF 粒度去获取程序执行过程当中的细粒度指标，帮助用户理解程序执行的真实过程，同时理解细粒度的指标是如何影响程序执行的。

- [**GitOps 是皇帝的新衣吗**](https://mp.weixin.qq.com/s/CpLvQM2rTI4InIN1Vk5ZKg)

    在采用 GitOps 前，我们需要了解清楚“什么是 GitOps？”，并问自己“我们使用这些工具为谁提供服务？我们试图解决什么问题？”文章针对 GitOps 的一些主要“卖点”（包括安全性、版本控制和环境历史、回滚、飘逸处理、单一真相来源等）提出了质疑，并介绍了 GitOps 带来的一些挑战。

## 安全漏洞

- [**Istio 高风险漏洞：拥有 localhost 访问权限的用户可以冒充任何工作负载的身份**](https://github.com/istio/istio/security/advisories/GHSA-6c6p-h79f-g6p4)

    如果用户拥有 Istiod 控制平面的 localhost 访问权，他们可以冒充服务网格内的任何工作负载身份。受影响的版本为 1.15.2。目前，已发布补丁版本 [1.15.3](https://github.com/istio/istio/releases/tag/1.15.3)。

## 其他

- [**2022 年容器生态系统的 9 大趋势洞察**](https://mp.weixin.qq.com/s/WNanrbCsdWEuyWP8WvO8UQ)
  
    Datadog 对客户运行的超 15 亿个容器进行了分析，总结出容器生态系统的主要趋势：无服务器容器技术在公共云中的使用率持续上升、多云使用率和组织的容器数量正相关、Kubernetes Ingress 使用率正在上升、大多数主机使用超过 18 个月的 Kubernetes 版本、超过 30% 的运行 containerd 的主机使用不受支持的版本、NGINX、Redis 和 Postgres 是最受欢迎的容器镜像。

- [**Karmada 大规模测试报告发布，突破 100 集群和 50 万节点**](https://karmada.io/zh/blog/2022/10/26/test-report/)

    近日，Karmada 社区对 Karmada 开展了大规模测试工作。根据测试结果分析，以 Karmada 为核心的集群联邦可以稳定支持 100 个集群和 50 万个节点同时在线，管理超过 200 万个Pod。在使用场景方面，Push 模式适用于管理公有云上的 Kubernetes 集群，而 Pull 模式相对于 Push 模式涵盖了私有云和边缘相关的场景。在性能和安全性方面，Pull 模式的整体性能要优于 Push 模式。

- [**toB 应用私有化交付技术发展历程和对比**](https://mp.weixin.qq.com/s/JcDZxabHImljPCEus_inlg)

    在传统应用交付中，管理运行环境和操作系统差异是一个痛点。当前云原生应用交付使用容器和 kubernetes 相关技术解决了这个问题，但是这些技术的学习和使用门槛太高。因而，抽象的应用模型成为下一代解决方案，例如，基于 OAM 的 KubeVela 应用交付和基于 RAM 的 Rainbond 应用交付。
