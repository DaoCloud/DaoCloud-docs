---
hide:
  - toc
---

# Cluster Resources for Installing Community Package

You can install DCE 5.0 on a standard Kubernetes cluster (production env) or on a kind cluster (test and development env).

## Install in Standard Kubernetes Cluster

| Resource Item | Requirements                                                                                                    |
| :------------ | :-------------------------------------------------------------------------------------------------------------- |
| Node | **3 Controller + 2 Worker nodes** <br />Controller node: 4 Core, 8 G, system disk 100G <br />Worker node: 4 Core, 8 G, system disk 100G |
| Kubernetes Version   | Recommended to use the latest stable version. Mminimum supported version: v1.20                                                       |
| Supported CRIs | Docker and containerd                                                                                            |
| CPU  | x86_64 and ARM64                                                                                     |

## Install in kind Cluster

| Resource Item | Requirements                                                      |
| :------------ | :---------------------------------------------------------------- |
| Node | CPU > 10 cores, memory > 12 GB, disk > 100 GB                |
| Kubernetes Version   | Recommended to use the latest stable version。 Minimum supported version v1.20 |
| Supported CRIs | Docker and containerd                                              |
| CPU   | x86_64 and ARM64                                    |
