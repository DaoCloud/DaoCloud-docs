---
hide:
  - toc
---

# 本地存储解决方案

Hwameistor 是针对云原生有状态负载构建的高可用本地存储系统，隶属于 [CNCF 全景图 -> 云原生存储 -> 运行时](https://landscape.cncf.io/?selected=hwamei-stor)。

![cncf gophers](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/community/images/cncf-gophers.png)

**HwameiStor 是一个 [CNCF](https://cncf.io/) Sandbox 项目。**

HwameiStor 是一款 Kubernetes 原生的容器附加存储 (CAS) 解决方案，将 HDD、SSD 和 NVMe 磁盘形成本地存储资源池进行统一管理，使用 CSI 架构提供分布式的本地数据卷服务，为有状态的云原生应用或组件提供数据持久化能力。

![系统架构](https://docs.daocloud.io/daocloud-docs-images/docs/community/images/hwa.png)

HwameiStor 有 5 个组件：

- 本地磁盘管理器 (Local Disk Manager, LDM)：简化管理节点上的磁盘，将磁盘抽象成一种可以被管理和监控的资源。这是一种 DaemonSet 对象，集群中每一个节点都会运行该服务，通过该服务检测存在的磁盘并将其转换成相应的 LocalDisk 资源。
- 本地存储 (Local Storage, LS) 旨在为应用提供高性能的本地持久化 LVM 存储卷。
- 调度器（scheduler）自动将 Pod 调度到配有 HwameiStor 存储卷的正确节点。使用调度器后，Pod 不必再使用 NodeAffinity 或 NodeSelector 字段来选择节点。调度器能处理 LVM 和 Disk 存储卷。
- 准入控制器（admission-controller）是一个 Webhook，可以自动验证哪个 Pod 使用 HwameiStor 卷，并将 schedulerName 修改为 hwameistor-scheduler。
- DRBD 安装器：通过 Linux 内核模块和相关脚本构成，用以构建高可用性的集群。其实现方式是通过网络来镜像整个设备，可以把它看作是一种网络 RAID。

[了解 HwameiStor 社区](https://github.com/hwameistor/hwameistor){ .md-button }

[查阅 HwameiStor 官网](https://hwameistor.io/){ .md-button }

![cncf logo](./images/cncf.png)

<p align="center">
HwameiStor 是一个 <a href="https://landscape.cncf.io/?selected=hwamei-stor">CNCF Sandbox 项目</a>。
</p>
