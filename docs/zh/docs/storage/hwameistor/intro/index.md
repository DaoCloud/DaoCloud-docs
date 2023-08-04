---
hide:
  - toc
---

# 什么是 HwameiStor

HwameiStor 是一款 Kubernetes 原生的容器附加存储 (CAS) 解决方案，将 HDD、SSD 和 NVMe 磁盘形成本地存储资源池进行统一管理，
使用 CSI 架构提供分布式的本地数据卷服务，为有状态的云原生应用或组件提供数据持久化能力。

![System architecture](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/img/architecture.png)

具体的功能特性如下：

1. 自动化运维管理

    可以自动发现、识别、管理、分配磁盘。根据亲和性，智能调度应用和数据。自动监测磁盘状态，并及时预警。

2. 高可用的数据

    使用跨节点副本同步数据， 实现高可用。发生问题时，会自动将应用调度到高可用数据节点上，保证应用的连续性。

3. 丰富的数据卷类型

    聚合 HDD、SSD、NVMe 类型的磁盘，提供非低延时，高吞吐的数据服务。

4. 灵活动态的线性扩展

    可以根据集群规模大小进行动态的扩容，灵活满足应用的数据持久化需求。

[HwameiStor 发行版本](https://github.com/hwameistor/hwameistor/releases){ .md-button .md-button--primary }
[下载 DCE 5.0](../../../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../../../dce/license0.md){ .md-button .md-button--primary }
