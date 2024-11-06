---
MTPE: windsonsea
date: 2024-05-11
hide:
  - toc
---

# Cluster Resources for Installing DCE Community

You can install DCE 5.0 on a standard Kubernetes cluster (production env) or on a kind cluster (test and development env).

## Install in a standard Kubernetes cluster

| Resource | Requirements |
| :------- | :----------- |
| Node Hardware | **3 Master + 2 Worker** <br />Master Nodes: 4 Cores, 8 GB RAM; 100 GB system disk <br />Worker Nodes: 4 Cores, 8 GB RAM; 100 GB system disk |
| K8s Version | Recommended [highest stable version from K8s community](https://kubernetes.io/releases/), currently recommended v1.29.5, minimum support v1.22 |
| Supported CRI | Docker and containerd |
| CPU Architecture | x86_64 and ARM64 |

## Install in a kind cluster

| Resources  | Requirements |
| :--------- | :---------- |
| Node | CPU > 10 cores, memory > 12 GB, disk > 100 GB |
| K8s Version | Recommended [highest stable version from K8s community](https://kubernetes.io/releases/), currently recommended v1.29.5, minimum support v1.22 |
| Supported CRIs | Docker and containerd |
| CPU | x86_64 and ARM64 |
