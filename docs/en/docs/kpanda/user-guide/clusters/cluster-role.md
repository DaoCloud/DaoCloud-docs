# Cluster Roles

DaoCloud Enterprise 5.0 classifies cluster roles based on cluster functions to help users better manage their IT infrastructure.

!!! note

    A cluster can have multiple cluster roles. For example, a cluster can be a global service cluster, a management cluster and a worker cluster at the same time.

## Global Service Cluster

This cluster is used to run DCE 5.0 components, such as Container Management, Global Management, Observability, Container Registry, etc. As a best practice, it's not recommended to run business applications in this cluster.

You can **have only** one Global Service Cluster in a DCE 5.0 platform.

| Items | Support or not |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------------------- ---------------------- |
| K8s version | 1.22+ |
| Operating System | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86;<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86;<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| Cluster Lifecycle Management | Support |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Network | Calico, Cilium, Multus and other CNIs |
| Policy Management | Support network policies, quota policies, resource limits, disaster recovery policies, and security policies |

## Management Clusters

This cluster is used to manage worker clusters. As a best practice, it's not recommended to run business applications in this kind of clusters.

You can have one or more management clusters in a DCE 5.0 platform.

- [Classic Mode](../../../install/commercial/deploy-requirements.md): deploy the Global Service Cluster and management clusters as different clusters, designed for enterprises with multiple data centers and architectures.
- [Simple Mode](../../../install/commercial/deploy-requirements.md): deploy the Global Service Cluster and management cluster as the same **one** cluster.

| Items | Support or not |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------------------- ---------------------- |
| K8s version | 1.22+ |
| Operating System | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86;<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86;<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| Cluster Lifecycle Management | Support |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Network | Calico, Cilium, Multus and other CNIs |
| Policy management | Support network policies, quota policies, resource limits, disaster recovery policies, and security policies |

## Worker Clusters

This cluster is created from scratch in [Container Management](../../intro/index.md). Worker clusters are designed for running business applications.

You should select a management cluster when creating a worker cluster. The selected management cluster will be responsible for the lifecycle management of all worker clusters under its control.

| Items | Support or not |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------------------- ---------------------- |
| K8s version | Support K8s 1.22+ |
| Operating System | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86;<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86;<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| Cluster Lifecycle Management | Support |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Network | Calico, Cilium, Multus and other CNIs |
| Policy management | Support network policies, quota policies, resource limits, disaster recovery policies, and security policies |

## Integrated Clusters

This cluster is designed to allow you to use your existing clusters in DCE 5.0. To achieve this, you should first integrate the existing cluster into DCE 5.0. You may integrate on-premise clusters, public/private cloud clusters , edge clusters, and other provides.

It is recommended to run business applications in this kind of clusters.

| Items | Support or not |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------- |
| K8s version | 1.18+ |
| Providers | Vmware Tanzu, Amazon EKS, Redhat Openshift, SUSE Rancher, Ali ACK, Huawei CCE, Tencent TKE, Standard K8s Cluster, DaoCloud DCE |
| Cluster Lifecycle Management | Not support |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Network | subject to the network mode of integrated clusters |
| Policy Management | Support network policies, quota policies, resource limits, disaster recovery policies, and security policies |
