# Unifabric 概述

Unifabric 面向 Kubernetes 集群中的 RDMA 网络，能够自动发现网络拓扑，将发现结果发布为 Kubernetes 自定义资源，并为节点添加相应的拓扑标签。调度器可据此识别节点所在的加速域及其与 Leaf、Spine 交换机的连接关系，从而更合理地调度工作负载。Unifabric 还提供节点级 RDMA 指标，支持在仪表盘中监控和分析。

## 主要能力

- **RDMA 拓扑发现**：支持 RoCE 和 InfiniBand 混合网络拓扑发现。InfiniBand 场景可集成 [NVIDIA Topograph](https://github.com/NVIDIA/topograph)。
- **拓扑资源与标签**：将节点 RDMA 信息和网络邻居关系记录为 Kubernetes 自定义资源，并将拓扑信息写入节点标签。
- **RDMA 指标**：提供节点 RDMA 指标，并支持关联 Pod 维度，用于监控设备、端口和工作负载流量。
- **eBPF Flow 归因（可选）**：通过 `libibverbs` uprobe 将 RDMA 发送流量关联到 Pod 间流量，并记录 RDMA Pod 地址和队列对信息。

## 安装

在全局集群安装 Spiderfabric，为集群拓扑发现提供 Grafana 数据源后端。在需要采集 RDMA 网络信息的工作集群安装 Unifabric。

- [在全局集群安装 Spiderfabric](install-spiderfabric.md)
- [在工作集群安装 Unifabric](install-unifabric.md)