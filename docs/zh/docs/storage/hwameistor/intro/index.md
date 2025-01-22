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

## 产品优势

**I/O 本地化**

100% 本地吞吐，无网络开销，节点故障时 Pod 在副本节点启动，使用副本数据卷进行本地 IO 读写。

**高性能、高可用性**

- 100% IO 本地化，实现高性能本地吞吐
- 2 副本数据卷冗余备份，保障数据高可用

**线性扩展**

- 独立节点单元，最小 1 节点，扩展数量不限
- 控制平面、数据平面分离，节点扩展，不影响业务应用数据 I/O

**CPU、内存开销小**

IO 本地化，相同的 IO 读写，CPU 平稳，无较大波动，内存资源开销小

**生产可运维**

- 支持节点、磁盘、数据卷组（VG）维度迁移
- 支持换盘等运维行为

[HwameiStor 发行版本](https://github.com/hwameistor/hwameistor/releases){ .md-button .md-button--primary }
[下载 DCE 5.0](../../../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../../../dce/license0.md){ .md-button .md-button--primary }
