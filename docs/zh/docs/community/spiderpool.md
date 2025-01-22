---
hide:
  - toc
---

# Spiderpool

Spiderpool 是 [CNCF](https://www.cncf.io) 的一个 [Sandbox 项目](https://landscape.cncf.io/card-mode?category=cloud-native-network&grouping=category)。

Spiderpool 提供了一个 Kubernetes 的 underlay 和 RDMA 网络解决方案，兼容裸金属、虚拟机和公有云等运行环境。

Spiderpool 是为 Kubernetes 定制的 Underlay 和 RDMA 网络方案，它增强了
[Macvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、
[ipvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan) 和
[SR-IOV CNI](https://github.com/k8snetworkplumbingwg/sriov-cni) 的功能，满足了各种网络需求，
使得 underlay 网络方案可应用在 **裸金属、虚拟机和公有云环境** 中，可为网络 I/O 密集性、低延时应用带来优秀的网络性能，
包括 **存储、中间件、AI 等应用** 。

Spiderpool 的核心功能如下：

![key features](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/community/images/spider-arch.png)

参阅 [Spiderpool 固定 IP 场景视频](../videos/use-cases.md#underlay-ip)和[入选 CNCF Sandbox 的博文](../blogs/2023/231220-spiderpool.md)。

[了解 Spiderpool 社区](https://github.com/spidernet-io){ .md-button }
[查阅 Spiderpool 官网](https://spidernet-io.github.io/spiderpool/){ .md-button }

![cncf logo](./images/cncf.png)

<p align="center">
Spiderpool 是一个 <a href="https://landscape.cncf.io/?selected=spiderpool">CNCF Sandbox 项目</a>。
</p>
