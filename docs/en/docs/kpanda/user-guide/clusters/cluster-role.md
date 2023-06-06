# cluster roles

DaoCloud Enterprise 5.0 classifies the roles of clusters based on their different functional orientations to help users better manage IT infrastructure.

## Global service cluster

This cluster is used to run DCE 5.0 components such as container management, global management, observability, registry, etc.
Generally, no business load is carried.

| Support Item | Description |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------------------- ---------------------- |
| K8s version | 1.22+ |
| Operating System | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86;<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86;<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| Cluster Lifecycle Management | Support |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Networking | Calico, Cillium, Multus and other CNIs |
| Policy management | Support network policy, quota policy, resource limit, disaster recovery policy, security policy |

## Manage Cluster

This cluster is used to manage the working cluster and generally does not carry business load.

- [Classic Mode](../../../install/commercial/deploy-requirements.md) deploys the global service cluster and the management cluster in different clusters, which is suitable for enterprise multi-data center and multi-architecture use cases.
- [Simple mode](../../../install/commercial/deploy-requirements.md) deploys the management cluster and the global service cluster in the same cluster.

| Supported Features | Description |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------------------- ---------------------- |
| K8s version | 1.22+ |
| Operating System | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86;<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86;<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| Cluster Lifecycle Management | Support |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Networking | Calico, Cillium, Multus and other CNIs |
| Policy management | Support network policy, quota policy, resource limit, disaster recovery policy, security policy |

## Working cluster

This is a cluster created using [Container Management](../../intro/what.md), which is mainly used to carry business load. The cluster is managed by the management cluster.

| Supported Features | Description |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------------------- ---------------------- |
| K8s version | Support K8s 1.22 and above |
| Operating System | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86;<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86;<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| Cluster Lifecycle Management | Support |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Networking | Calico, Cillium, Multus and other CNIs |
| Policy management | Support network policy, quota policy, resource limit, disaster recovery policy, security policy |

## access cluster

This cluster is used to access existing standard K8s clusters, including but not limited to self-built clusters in local data centers, clusters provided by public cloud vendors, clusters provided by private cloud vendors, edge clusters, Xinchuang clusters, heterogeneous clusters, Daocloud Different distribution clusters.
It is mainly used to bear business load.

| Supported Features | Description |
| ------------------ | ------------------------------ -------------------------------------------------- -------------------------------------- |
| K8s version | 1.18+ |
| Support Friends | Vmware Tanzu, Amazon EKS, Redhat Openshift, SUSE Rancher, Ali ACK, Huawei CCE, Tencent TKE, Standard K8s Cluster, Daocloud DCE |
| Cluster lifecycle management | Not supported |
| K8s Resource Management | Support |
| Cloud Native Storage | Support |
| Cloud Native Networking | Dependent Access Cluster Distribution Network Mode |
| Policy management | Support network policy, quota policy, resource limit, disaster recovery policy, security policy |

!!! note

    A cluster can have multiple cluster roles. For example, a cluster can be either a global service cluster, a management cluster or a working cluster.