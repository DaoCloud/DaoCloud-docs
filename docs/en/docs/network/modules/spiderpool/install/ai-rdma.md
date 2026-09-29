# AI/RDMA Network Solution Overview

This page describes the overall solution and selection recommendations for using Spiderpool in DCE to
provide RDMA network capabilities for AI workloads. It applies to both RoCE and InfiniBand scenarios.

## Scenarios

- Large model training/inference, distributed storage, real-time computing, and other scenarios
  sensitive to low latency and high throughput
- RDMA devices and network channels need to be provided for Pods in Kubernetes
- Cluster nodes are equipped with RDMA NICs (such as the Mellanox ConnectX series)

## Solution Comparison and Selection Recommendations

| Solution | RDMA Protocol | Resource Isolation | Performance | Resource Utilization | Scenario | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| Shared RDMA (Macvlan/IPvlan) | RoCE | Shared | High | High | Virtual machines/bare metal; rapid deployment | Prefer for lightweight and multi-tenant needs |
| Dedicated RDMA (SR-IOV RoCE) | RoCE | Dedicated | Optimal | Medium | High-performance training/inference | Prefer for performance and isolation |
| Dedicated RDMA (SR-IOV InfiniBand) | InfiniBand | Dedicated | Optimal | Medium | IB Fabric environment | IB-specific scenarios |

Selection recommendations:

- If the environment is mainly Ethernet-based and you want rapid deployment, prefer shared RDMA
  (Macvlan/IPvlan).
- If you need stronger isolation and performance, use SR-IOV (RoCE).
- If the cluster uses an InfiniBand fabric, use SR-IOV (InfiniBand).

## Key Components

- Spiderpool: Provides IPAM, RDMA resource management, and multi-NIC management capabilities
- Multus: Adds a second or more NICs to a Pod
- RDMA device plugin: Reports RDMA resources to Kubernetes in shared or dedicated mode
- SR-IOV Operator (dedicated solution): Configures SR-IOV VFs and the RDMA CNI

## Environment Requirements

- DCE
- Spiderpool v1.0.x
- RDMA NICs and drivers are installed (refer to [Install the NVIDIA OFED Driver](ofed_driver.md))
- For RoCE scenarios, complete lossless network and MTU planning in advance

## Recommended Deployment Path (Offline/Addon First)

1. Download and prepare the offline Addon package (offline packages are recommended for offline environments).
2. In DCE, install Spiderpool through **Helm Apps** -> **Helm Templates**
   (refer to [Install Spiderpool](install.md)).
3. Enable RDMA-related components and parameters as required by the scenario
   (refer to [RDMA Environment Preparation and Installation](rdmapara.md)).

## Monitoring and O&M

- RDMA metrics description: [RDMA Metrics](../rdma-metrics.md)
- RDMA visualization dashboard: [RDMA Dashboard](../rdma-dashboard.md)

## Quick Links

- [Shared RDMA (Macvlan/IPvlan)](rdma-macvlan.md)
- [Dedicated RDMA (SR-IOV RoCE)](rdma-sriov-roce.md)
- [Dedicated RDMA (SR-IOV InfiniBand)](rdma-sriov-ib.md)
