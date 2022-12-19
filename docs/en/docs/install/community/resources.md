---
hide:
  - toc
---

# Cluster resource planning

You can install DCE 5.0 on a standard Kubernetes cluster, or you can install DCE 5.0 on a kind cluster.

The requirements for standard Kubernetes cluster resources are as follows:

| Resource Items | Requirements |
| :--------- | :------------------------------------- -------------------------------------------------- ----------------------- |
| Node hardware | **3 Master + 2 Worker** <br />Master node: 4 Core, 8 G; system disk 100G <br />Worker node: 4 Core, 8 G; system disk 100G |
| K8s version | The official highest stable version of K8s is recommended, currently v1.24 is recommended, and the minimum support is v1.20 |
| Supported CRIs | Docker and containerd |
| CPU architecture | x86_64, ARM is not supported temporarily |

The requirements for kind cluster resources are as follows, and are only recommended for testing and development.

| Resource Items | Requirements |
| :--------- | :------------------------------------- ------------------- |
| Node Hardware | CPU > 10 Cores, Memory > 12 GB, Disk Space > 100 GB |
| K8s version | The official highest stable version of K8s is recommended, currently v1.24 is recommended, and the minimum support is v1.20 |
| Supported CRIs | Docker and containerd |
| CPU architecture | x86_64, ARM is not supported temporarily |