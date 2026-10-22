# Unifabric Overview

Unifabric discovers RDMA network topology in Kubernetes clusters, publishes the results as Kubernetes custom resources, and applies topology labels to nodes. Schedulers can use this information to understand node placement, such as whether nodes are in the same acceleration zone or connected to the same leaf or spine switch, and make more informed workload placement decisions. Unifabric also provides node-level RDMA metrics for dashboard monitoring and analysis.

## Key Capabilities

- **RDMA topology discovery**: Supports hybrid RoCE and InfiniBand topology discovery. InfiniBand deployments can integrate with [NVIDIA Topograph](https://github.com/NVIDIA/topograph).
- **Topology resources and labels**: Records node RDMA information and network neighbors in Kubernetes custom resources, and writes topology information to node labels.
- **RDMA metrics**: Exposes node-level RDMA metrics with optional Pod attribution for monitoring devices, ports, and workload traffic.
- **eBPF Flow attribution (optional)**: Uses `libibverbs` uprobes to attribute RDMA send traffic to Pod-to-Pod flows and record RDMA Pod addresses and queue pairs.

## Installation

Install Spiderfabric on the global cluster to provide the Grafana data source backend for cluster topology discovery. Install Unifabric on each worker cluster from which RDMA network information must be collected.

- [Install Spiderfabric on the global cluster](install-spiderfabric.md)
- [Install Unifabric on a worker cluster](install-unifabric.md)