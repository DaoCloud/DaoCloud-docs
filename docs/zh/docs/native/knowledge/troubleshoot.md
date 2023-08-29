# 排障方案

本页列出云原生社区的一些故障排查方案，供运维人员参考。

- [如何解决 Prometheus 的存储容量问题？](https://mp.weixin.qq.com/s/TMApz8FxT91qBvS1fzuTVw)

    单机存储不好扩展是 Prometheus 一个广受诟病的问题。对此问题，文章给出了 3 种集群解决方案：Prometheus 联邦集群、远程存储方案、Prometheus 自身搭建集群，这这三种方案能够很好地解决 Prometheus 的存储问题。

- [云原生场景下，nettrace 怎么快速进行网络故障诊断？](https://mp.weixin.qq.com/s/0n7kbOhHr6m5JClTrSIysA)

    [nettrace](https://github.com/OpenCloudOS/nettrace) 是一款基于 eBPF 的集网络报文跟踪（故障定位）、网络故障诊断、网络异常监控于一体的网络工具集，
    提供一种更加高效、易用的方法来解决复杂场景下的网络问题。

- [Istio 运维实战：如何规避 503 UC 错误](https://mp.weixin.qq.com/s/4YIYPIszyKyWVMKXnXtHbg)

    503 UC 是在 Istio/Envoy 使用过程中经常遇到的一个问题。
    文章分析了由于 TCP 服务器 keepalive Timeout 导致的 503 UC 的原理及规避方法。

- [K8s CNI Cilium 网络故障排查指南](https://mp.weixin.qq.com/s/jBuNPOKbL-keXmzq1gq-mQ)

    文章介绍了作者从 kubenet 升级到  cilium 时遇到的一个问题及排障过程。
    问题是，在 kubenet 网络的节点上的 pod 无法访问 cilium 网络的节点上的 pod。
    通过抓包测试，以及分析 cilium 的相关信息，
    发现问题所在：cilium 如果没有管理所有 k8s 节点，剩余的节点就按照外部服务器的方式来处理。

- [如何高效地对 Kubernetes Service 进行排障](https://blog.getambassador.io/how-to-debug-a-kubernetes-service-effectively-3d4eff0b221a)

    文章简要介绍了 service 的工作方式，在运行 service 时可能出现的各种 bug 以及如何解决这些 bug。
    最后，还介绍了一个高效排障工具 [Telepresence](https://github.com/telepresenceio/telepresence)。
    Telepresence 能够为 Kubernetes 建立一个远程开发环境，用户仍然可以使用自己的本地工具，如 IDE 和调试器，
    并针对远程 K8 集群的微服务测试本地服务。

- [K8s：彻底解决节点本地存储被撑爆的问题](https://mp.weixin.qq.com/s/pKTA6O3bdko_eHaw5mU3gQ)

    K8s 节点本地存储保存了镜像、可写层、日志、emptyDir 等内容。
    除了容器镜像是系统机制控制的，其它都跟应用程序有关。
    完全依赖开发者对应用使用的存储空间进行限制并不可靠，因此，K8s 提供了垃圾回收、日志总量限制、emptyDir 卷限制、临时数据总量限制来避免本地存储不够用的问题。

- [K8s 有损发布问题探究](https://mp.weixin.qq.com/s/jKVw0m5Ho2AtFRScnKEMKw)

    应用发布过程其实是新 Pod 上线和旧 Pod 下线的过程，当流量路由规则的更新与应用 Pod 上下线配合出现问题时，就会出现流量损失。
    总的来说，为了保证流量无损，需要从网关参数和 Pod 生命周期探针和钩子来保证流量路径和 Pod 上下线的默契配合。
    文章从 K8s 的流量路径入手，分析有损发布产生的原因，并给出解决方案。

- [K8s：Pod 的 13 种异常](https://mp.weixin.qq.com/s/cEEdH7npkSHmVHSXLbH6uQ)

    文章总结了 K8s Pod 的 13 种常见异常场景，给出各个场景的常见错误状态，分析其原因和排查思路。

- [K8s: 你需要知道的一切](https://enterprisersproject.com/sites/default/files/2022-11/tep_white-paper_kubernetes-what-you-need-to-know%2Brev2.pdf)

    电子书囊括了了解 Kubernetes 所需的所有定义，同时也包含了与 Kubernetes 相关的其他电子书、文章、教学视频等资源的介绍，以及 7 个最佳实践。

- [Docker Volume 引发 K8s Terminating Pod 的问题](https://mp.weixin.qq.com/s/SMynKYP4obMSl6GQdwDlEw)

    Terminating Pod 是业务容器化后遇到的一个典型问题，诱因不一。
    文章记录了网易数帆-轻舟 Kubernetes 增强技术团队如何一步步排查，发现 Docker Volume 目录过多导致 Terminating Pod 问题的经历，并给出了解决方案。

- [安装 Kubernetes 或升级主机操作系统后出现网络问题？这可能是你的 iptables 版本有问题](https://www.mirantis.com/blog/networking-problems-after-installing-kubernetes-1-25-or-after-upgrading-your-host-os-this-might-be-your-problem)

    安装新版本的 Kubernetes 后，你的工作节点连接不上网络，突然间无法 ssh 访问甚至无法 ping 它们？
    这可能是因为 kube-router 1.25 的 iptables 版本和你安装的版本之间出现冲突。
    归根结底是因为 iptables 1.8.8 和旧版本的规则格式不兼容。
    对此，有三个解决方案：将 iptables 版本降到 1.8.7、清理 IPTables 链所有权（alpha）或是借助轻量级的 Kubernetes 发行版 [k0s](https://github.com/k0sproject/k0s) 解决。

- [利用 eBPF 进行 Kubernetes 集群磁盘 I/O 性能问题排查](https://mp.weixin.qq.com/s/RrTjhSJOviiINsy-DURV2A)

    问题始于 eBay 工程师发现他们的 Kafka 服务在有些时候 follower 追不上 leader 的数据。
    为解决问题，利用了一些 eBPF 工具，例如，[biopattern](https://github.com/iovisor/bcc/blob/master/tools/biopattern.py) 用于展示 disk I/O pattern，[ebpf_exporter](https://github.com/cloudflare/ebpf_exporter) 用于数据收集和可视化。

- [Kubernetes 网络排错骨灰级指南](https://mp.weixin.qq.com/s/mp5coRHPAdx5nIfcCnPFhw)

    文章介绍 Kubernetes 集群中网络排查的思路，包括 Pod 常见网络异常分类、排查工具、排查思路及流程模型、CNI 网络异常排查步骤以及案例学习。

- [Redis 缓存异常及处理方案总结](https://mp.weixin.qq.com/s/P38ETBZJO2lNlE-i7g6HhA)

    Redis在实际应用过程中，会存在缓存雪崩、缓存击穿和缓存穿透等异常情况，如果忽视这些情况可能会带来灾难性的后果，文章对这些缓存异常问题和相应处理方案进行了分析和总结。

- [K8S Internals 系列：存储卷指标消失之谜](https://mp.weixin.qq.com/s/Sd1TY9ml65MQYVSupmvpbw)

    这篇文章的创作灵感因 Grafana 不展示使用存储驱动创建的存储卷的容量指标而起，展示了该问题的排查思路及手段，进而勾勒出 Kubelet 对于存储卷指标收集的实现流程。