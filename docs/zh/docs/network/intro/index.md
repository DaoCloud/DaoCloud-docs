# 什么是云原生网络？

DCE 5.0 云原生网络基于多个开源技术构建，不仅提供单个 CNI 网络支持，也提供多个 CNI 网络的组合方案。具体方案如下：

## 方案一：Cilium + MacVLAN/SR-IOV/IPVLAN + SpiderPool + Multus

此方案适用于高内核版本（4.19.57+）的 Linux 操作系统。
方案以 Multus 为调度核心，搭配多 CNI，满足不同的网络场景需求，实现跨云跨集群的网络连通性。
同时还具备灵活的 IPAM 管理能力，基于 SpiderPool 加强 Underlay 网络的 IP 管理分配及 IP 回收能力。
不同 IP 池的使用满足了不同应用通信场景的需求。
此网络组合的主要功能如下：

1. 以 Multus 为调度核心，实现 Pod 多 CNI 的 IP 分配，支持应用的多态网络通信场景。基于开源方案实现本集群内跨 CNI 的 Pod 间通信。

    > 如果应用没有 Pod 多网卡以及不同网络形态需求，可以不安装 Multus。

2. 以 Spiderpool 作为 Underlay CNI 的 IPAM 管理组件，实现 IP 精细化管理、灵活的 IP 规划及分配。

    > 如果在应用落地场景中未安装 Underlay CNI，可以不安装 SpiderPool。

3. Cilium 作为高性能 Overlay CNI，提供 eBPF 内核加速，实现跨集群 Pod 通信和跨集群 Service 通信，以及支持灵活的细粒度网络策略下发和丰富的流量观测能力。

    > 在此方案组合中，Cilium 为必备的网络 CNI。

4. 通过 MacVLAN / SRIOV / IPVLAN CNI 提供对外访问 IP，实现 Pod 二层对外通信能力。
搭配 Cilium 动态虚拟网络，降低网络运维难度，并节省 IP 资源。

    > 如果在应用落地场景中没有对外访问需求，可以不安装 Underlay CNI。

![solution01](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/solution01.png)

## 方案二：Calico + MacVLAN/SR-IOV/IPVLAN + SpiderPool + Multus

此方案适用于低内核版本的 Linux 操作系统，在用户有跨集群连通以及多 CNI 等需求时，可以采用此方案。

1. 以 Multus 为调度核心，实现多 CNI 的 IP 分配，支持应用的多态网络通信场景。基于开源方案实现本集群内跨 CNI 的 Pod 间通信。

    > 如果应用没有 Pod 多网卡以及不同网络形态需求，可以不安装 Multus。

2. 以 Spiderpool 作为 Underlay CNI 的 IPAM 管理组件，实现 IP 精细化管理、灵活的 IP 规划及分配。

    > 如果在应用落地场景中，未安装 Underlay CNI，可以不安装 SpiderPool。

3. 通过  MacVLAN / SRIOV / IPVLAN CNI 提供对外访问 IP，实现 Pod 二层对外通信能力。
   搭配 Calico 动态虚拟网络，降低网络运维难度，节省 IP 资源。

    > 在此方案组合中，Calico 为必备的网络 CNI。如果在应用落地场景中，没有对外访问需求，可以不安装 Underlay CNI。

4. 通过 Submariner 组件打通跨集群 Pod 间的通信，结合 Submariner 及 Core DNS 服务发现，实现集群间的服务发现能力。

    > Submariner 可根据需求选择安装。

![solution02](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/solution02.png)

[下载 DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../../dce/license0.md){ .md-button .md-button--primary }
