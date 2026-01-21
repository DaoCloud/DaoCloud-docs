# AI/RDMA 网络方案总览

本页介绍在 DCE 5.0 中使用 Spiderpool 为 AI 工作负载提供 RDMA 网络能力的整体方案与选型建议，适用于 RoCE 与 Infiniband 场景。

## 适用场景

- 大模型训练/推理、分布式存储、实时计算等对低延迟与高吞吐敏感的场景
- 需要在 Kubernetes 中为 Pod 提供 RDMA 设备与网络通道
- 集群节点具备 RDMA 网卡（如 Mellanox ConnectX 系列）

## 方案对比与选型建议

| 方案 | RDMA 协议 | 资源隔离 | 性能 | 资源利用率 | 适用场景 | 推荐 |
| --- | --- | --- | --- | --- | --- | --- |
| 共享 RDMA（Macvlan/IPvlan） | RoCE | 共享 | 高 | 高 | 虚拟机/裸金属；快速落地 | 轻量与多租户优先 |
| 独享 RDMA（SR-IOV RoCE） | RoCE | 独享 | 最优 | 中 | 高性能训练/推理 | 性能与隔离优先 |
| 独享 RDMA（SR-IOV Infiniband） | Infiniband | 独享 | 最优 | 中 | IB Fabric 环境 | IB 专用场景 |

选型建议：

- 若环境以以太网为主且希望快速落地，优先使用共享 RDMA（Macvlan/IPvlan）。
- 若需要更强隔离与性能，使用 SR-IOV（RoCE）。
- 若集群为 Infiniband Fabric，则使用 SR-IOV（Infiniband）。

## 关键组件

- Spiderpool：提供 IPAM、RDMA 资源管理与多网卡管理能力
- Multus：为 Pod 增加第二张/多张网卡
- RDMA 设备插件：在共享或独享模式下向 K8s 汇报 RDMA 资源
- SR-IOV Operator（独享方案）：配置 SR-IOV VF 与 RDMA CNI

## 环境要求

- DCE 5.0
- Spiderpool v1.0.x
- RDMA 网卡与驱动已安装（建议参考 [安装 Nvidia OFED 驱动](ofed_driver.md)）
- RoCE 场景建议提前完成无损网络与 MTU 规划

## 推荐部署路径（离线/Addon 优先）

1. 下载并准备离线 Addon 包（离线环境建议优先采用离线包部署）。
2. 在 DCE 中通过 **Helm 应用** -> **Helm 模板** 安装 Spiderpool（参考 [安装 Spiderpool](install.md)）。
3. 按场景启用 RDMA 相关组件与参数（参考 [RDMA 环境准备及安装](rdmapara.md)）。

## 监控与运维

- RDMA 指标说明：[RDMA 指标](../../../config/rdma-metrics.md)
- RDMA 可视化看板：[RDMA 看板](../rdma-dashboard.md)

## 快速入口

- [共享 RDMA（Macvlan/IPvlan）](rdma-macvlan.md)
- [独享 RDMA（SR-IOV RoCE）](rdma-sriov-roce.md)
- [独享 RDMA（SR-IOV Infiniband）](rdma-sriov-ib.md)
