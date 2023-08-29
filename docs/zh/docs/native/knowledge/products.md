# 产品选型

本页列出一些基于云原生社区构建的商业化产品。

- [Kubernetes 策略引擎：OPA vs. Kyverno vs. jsPolicy](https://mp.weixin.qq.com/s/bMPraw5Q8-DZqCoJLJe2jQ)

    文章讨论了 Kubernetes 策略引擎的概念，并比较了三种不同的 Kubernetes 策略引擎：OPA、Kyverno 和 jsPolicy。
    结论是：如果想要更直接和简单的方法，或者精通 JavaScript 和 TypeScript，推荐使用 jsPolicy。
    如果更喜欢 YAML，并且希望继续直接使用 Kubernetes 资源，Kyverno 是一个不错的选择。

- [过去二十年里开源的 12 个开源监控工具大对比](https://mp.weixin.qq.com/s/ByQ3skUrcf1c_DPD4dCbRg)

    文章对 12 款典型的开源监控工具做了简要的介绍和分析，指出各自的优势和不足。
    其中提到的工具包括分布式监控系统 Zabbix、时序数据库 VictoriaMetrics、Prometheus、云原生监控分析系统夜莺监控等。

- [云原生存储工具的选型和应用探讨](https://mp.weixin.qq.com/s/QoVlOe01hGWSYEKS8wfsKw)

    文章逐步梳理了云原生存储的概念，并对 Longhorn、OpenEBS、Rook+Ceph 进行简要介绍和横向对比，最后选择了具有代表性的 Longhorn 演示其安装和使用。

- [K8s CNI 插件选型和应用场景探讨](https://mp.weixin.qq.com/s/GG7GX_E1oyZf-cmjk80OYg)

    文章介绍容器环境常见七个网络应用场景及对应场景的 Kubernetes CNI 插件功能实现。

- [云原生时代的 DevOps 平台设计之道（Rancher vs KubeSphere vs Rainbond）](https://mp.weixin.qq.com/s/oxeNq4GHE85NUBIDcgixcg)

    文章重点介绍了 Rancher 、KubeSphere、Rainbond 三款云原生平台级产品各自不同的 DevOps 实现。
    作者认为，DevOps 团队可以选择 Rancher + KubeSphere 或 Rancher + Rainbond 的组合。
    Rancher 最擅长向下对接基础设施，管理集群的安全性与合规性，而向上为开发人员提供易用的云原生平台则交给 KubeSphere 或 Rainbond。

- [到底谁强？Grafana Mimir 和 VictoriaMetrics 性能测试](https://mp.weixin.qq.com/s/TVJZ5k5U7bs8WEyE4rikSQ)

    文章比较 VictoriaMetrics 和 Grafana Mimir 集群在相同硬件上运行的工作负载的性能和资源使用情况。
    在基准测试中，与 Mimir 相比，VictoriaMetrics 表现出更高的资源效率和性能。从操作上讲，VictoriaMetrics 扩展更为复杂，Mimir 可以很容易实现组件扩展。

- [一文读懂 Prometheus 长期存储主流方案](https://mp.weixin.qq.com/s/1BF83kIF_AGVD9J2qLnlSA)

    由于 Prometheus 存在跨集群聚合、长时间存储等局限性，社区给出了多种扩展方案。
    文章对包括 M3、VictoriaMetrics、Thanos、Cortex、Grafana Mimir 在内的 5 种主流 Prometheus 长期存储方案进行了多维度对比分析。

- [eBPF 基础设施库的技术选型](https://mp.weixin.qq.com/s/4WNyNwkRW2lZ82nMOP6rMA)

    文章对几个 eBPF 基础设施库进行比较，如 libbcc、dropbox 的 goebpf、Cilium 的 ebpf 库、Calico 的底层库、falco 的 lib 库，
    并说明开源可观测性工具 Kindling 选择 falco-libs 的原因。

- [在生产环境如何选择靠谱的 APM 系统](https://mp.weixin.qq.com/s/3dD0hIuqpXdepLVC6V7aoA)

    文章从主流 APM 产品介绍出发（对比 Pinpoint、Jaeger、Skywalking、听云、腾讯云+阿里云 Arms 和 Datadog），通过生产环境中关注的几个重要维度，如产品体验、Agent 能力、报警+ DB 支持、云原生的支持能力、数据大屏等，给予 APM 选型方案建议。
