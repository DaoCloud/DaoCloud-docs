# 前沿热点

本页列出云原生社区的一些前沿热点，便于大家了解潮流和方向。更多请参阅 [OSS Insight](https://ossinsight.io/)。

- [国内首例社区双栈 Istio 方案落地经验，实现代码已开源](https://mp.weixin.qq.com/s/E9HZIkSbZ3BLetDL0ZhzvA)

    在业界广泛应用的服务网格项目（以 Istio 和 Linkerd 为例）中，双栈技术的支持依然是缺失的。
    为更好的实现服务网格与 Kubernetes 在双栈支持上的协同工作，
    文章主要介绍了 Istio 在双栈技术中的实现方案以及该方案在移动云的落地实现场景。
    但是，此方案只是[实验性的分支](https://github.com/istio/istio/tree/experimental-dual-stack)，并没有完善单元测试和集成测试。

- [微服务进入深水区后该何去何从](https://mp.weixin.qq.com/s/yBY-E-tndUJCmA4KYRfrDw)

    微服务进入深水区后，开发者和架构师更关心的是微服务安全、稳定性、成本优化、微服务治理标准化，以及促使云原生微服务架构逐步演进到多运行时微服务架构。
    而对于多运行时架构存在的局限性，需要实现更加标准化与平台化的服务网格开发与运维能力，规范化 Sidecar 与运行时的定义，同时将运维平台变得更加标准易用。

- [2023 年云原生发展趋势的预测](https://mp.weixin.qq.com/s/QePkownt0_Ex9RWWeGtaag)

    文章是 CNCF CTO Chris Aniszczyk 关于 2023 年云原生和技术领域的热点话题的预测，
    包括：云原生 IDE 成为常态、FinOps 成为主流并左移、开源 SBOM 无处不在、GitOps 走向成熟并进入实质生产高峰期、OpenTelemetry 日益成熟、Backstage 开发者门户继续完善、WebAssembly 进入稳步爬升期等等。

- [探索基于隧道的 Kubernetes 跨集群通讯](https://mp.weixin.qq.com/s/uuWCr1d7V_aFdCAJCJS_XQ)

    文章介绍了基于 ssh 隧道的跨集群访问访问。
    集群 A 中服务要访问集群 B 中的不同服务，即单隧道多服务的实现是通过在隧道两头增加一个隧道的代理，隧道左端监听多个端口，用来区分集群 A 中服务要访问的集群 B 中的不同服务。
    并且将此信息告知隧道右端的代理，右端代理根据此信息来转发给对应的集群 B 中的服务。
    目前该方案只是在 demo 的程度。

- [2023 年 eBPF 的六个发展趋势](https://www.solo.io/blog/ebpf-trends-2023/)

    2023 年 eBPF 的六个发展趋势包括：
    利用 eBPF 网络追踪建立高性能的 HTTP 监控、更深入的网络功能和 sidecar 优化、安全和恶意软件检测、云平台的大规模应用、电信领域的应用、更多基于 eBPF 的项目涌现。

- [Kubernetes 之痛，平台工程可以解决](https://thenewstack.io/kubernetes-pains-platform-engineering-can-help/)

    构建平台工程所需的产品方法有助于组织了解尚未提供支持的 Kubernetes 领域。
    开发者自助服务允许工程师自行调配和使用测试、保护和部署应用所需的技术，而无需等待运维提供资源或启动环境。
    内部开发平台使开发和运维专注于各自的核心职责和优势，开发人员专注于编写代码，运维向上游转移到更关键的任务，如管理网络或物理硬件。

- [信创如何为业务带来价值？](https://mp.weixin.qq.com/s/uDe1wb0cVsqrz7oXjYOXXg)

    提到信创，大家第一反应就是自主可控。但要做好信创，需要从埋头于自主可控中抽出一部分精力，思考如何从信创中获取价值。
    文章介绍了国内外技术替代的成功案例，技术替换在什么情况下能为业务带来价值，以及如何做能够让信创更好地为业务服务。

- [从 PingCAP 的 TiDB 数据库产品看国产技术出海模式](https://mp.weixin.qq.com/s/3y9pafdEy8rD5H2OtgPwEw)

    文章介绍了 PingCAP 为实现技术出海，对 TiDB 在技术上、合规性、商业化方面所做的优化。
    技术上，要实现降本增效、运维自动化、多租户管理、满足特定地区的场景需求；
    合规性上，考虑数据安全、监管规则；
    商业上，考虑计价模式、商业化策略等。
    此外，TiDB 能够吸引海外客户还有几个因素：TiDB 是开源的，有着活跃的开源社区；
    客户数据存放在 AWS、GCP 等公有云上；
    远程支持，不依赖当地技术团队，可以有效解决部分地区人力资源贵的问题。

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