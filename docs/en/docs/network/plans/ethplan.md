---
hide:
  - toc
---

# Eth card planning

This page describes how to plan network adapters based on different network solution combinations before creating a workload cluster.
Please complete [Cluster Deployment Plan](../../install/commercial/deploy-requirements.md) and network card planning before cluster deployment.

## Overlay scheme only

When the application Pod in the cluster only needs to use a single CNI and does not need to provide external access, only the component Calico/Cilium needs to be deployed, and the network card planning is also relatively simple. The specific network card planning is as follows:

| Deployment Environment | Infrastructure | Number of NICs | NIC Description | Purpose |
| -------------- | ----------------- | ---------------- - | ----------------------- | ------------- |
| PoC environment<br /> | Physical machine<br />Virtual machine<br />Public cloud| 1 physical network card/Bond network card| Access mode access, the network card where the default route is located ==[^1]== | Bearer K8s management traffic, Calico Pod traffic |
| Production environment<br /> | Physical machine<br />Virtual machine<br />Public cloud| 1 or 2 physical network cards/Bond network cards| **NIC 1**: Access mode access, the network card where the default route is located< br />**NIC 2** ==[^2]== (optional): Access mode access | **NIC 1**: carry K8s management traffic, Calico Pod traffic<br />**NIC 2**: Hwameistor data replicas synchronize traffic across nodes |

## Overlay + Underlay scheme

When the cluster deployment application needs to use a combination of multiple CNIs and Underlay CNI (Macvlan/SR-IOV) IP to provide external communication, the network component combination that can be used is `Calico + SpiderPool + Multus + Macvlan/SR-IOV` (the same cluster can Deploy Macvlan and SR-IOV CNI at the same time). The specific network card planning is as follows:

| Deployment Environment | Infrastructure | Number of NICs | NIC Description | Purpose |
| -------------- | ----------------- | ---------------- - | ----------------------- | ------------- |
| PoC environment| Physical machine<br />Virtual machine<br /> | 1 physical network card / Bond network card | Access mode access, the network card where the default route is ==[^1]== | Carrying K8s management traffic, Calico Pod Traffic, Underlay CNI (Macvlan) Pod Traffic |
| Production environment<br /> | Physical machine<br />Virtual machine<br /> | 2 physical NICs/Bond NICs| **NIC 1**: Access mode access, the network card where the default route is located<br />**NIC 2** ==[^1]==: Trunk mode access | **NIC 1**: carrying K8s management traffic, Calico Pod traffic<br />**NIC 2**: carrying Underlay CNI (Macvlan/SR-IOV) Pod Traffic |
| Production environment<br /> | Physical machine<br />Virtual machine<br /> | 3 physical network cards/Bond network cards| **NIC 1**: Access mode access, the network card where the default route is located<br />**NIC 2** ==[^2]==: Trunk mode access<br />**NIC 3** (optional): Access mode access| **NIC 1**: carrying K8s management traffic, Calico Pod traffic<br />**NIC 2**: carrying Underlay CNI (Macvlan/SR-IOV) Pod traffic<br />**NIC 3**: Hwameistor data copy cross-node synchronization traffic |

[^1]: All network cards shall have a consistent name
[^2]: All network cards shall have a consistent name; if you want to use Hwameistor local storage and enable the high availability function, you can plan additional network cards based on actual situations
