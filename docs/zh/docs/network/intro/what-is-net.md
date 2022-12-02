# 网络组合方案

DCE 5.0 云原生网络基于开源技术，不仅提供单 CNI 网络支持，同时提供了多个 CNI 组合方案。

## 方案一：Cilium + MacVLAN/SpiderFlat + SpiderPool + Multus

此方案适用于高内核版本（4.19.57+）的 Linux 操作系统，以 Multus 为调度核心，搭配多 CNI，满足不同的网络场景，打造跨云跨集群的网络连通性。
同时基于 SpiderFlat 及 SpiderPool 加强 Underlay 网络的 IP 管理分配及 IP 回收能力，具备灵活的 IPAM 管理能力。
不同 IP 池的多样化使用方式能满足应用通信的不同场景，此网络组合中主要的特色功能如下：

1. 以 Multus 为调度核心，实现 Pod 多 CNI IP 分配，实现应用的多态网络通信场景。基于开源的方案实现本集群内跨 CNI 的 Pod 通信。
   如果应用没有 Pod 多网卡以及不同网络形态需求，可以不安装 Multus。
2. 以 Spiderpool 作为 Underlay CNI 的 IPAM 管理组件，实现 IP 精细化管理、灵活的 IP 规划及分配。
   如果在应用落地场景中未安装 Underlay CNI，可以不安装 SpiderPool。
3. Cillium 作为高性能 Overlay CNI，实现 eBPF 内核加速，连通跨集群 Pod 通信，跨集群 Service 通信，以及灵活的细粒度网络策略下发和丰富的流量观测能力。
   在此方案组合中，Cillium 为必备的网络 CNI。
4. 通过 SpiderFlat / MacVLAN CNI / SRI-OV CNI 提供对外访问 IP，实现 Pod 二层对外通信能力，搭配 Calico 动态虚拟网络，降低网络运维难度，并节省 IP 资源。
   如果在应用落地场景中没有对外访问需求，可以不安装 Underlay CNI。

![solution01](../images/solution01.png)

## 方案二：Calico + MacVLAN/SpiderFlat + SpiderPool + Multus

此方案适用于低内核版本的 Linux 操作系统，在用户有跨集群连通以及多 CNI 等多样化需求时，可以采用此组合方案。

1. 同样以 Multus 为调度核心，实现多 CNI IP 分配，实现应用的多态网络通信场景，基于开源的方案实现本集群内跨 CNI Pod 通信。
   如果应用没有 Pod 多网卡以及不同网络形态需求，可以不安装 Multus。
2. 以 Spiderpool 作为 Underlay CNI 的 IPAM 管理组件，实现 IP 精细化管理、灵活的 IP 规划及分配。
   如果在应用落地场景中，未安装 Underlay CNI，可以不安装 SpiderPool。
3. 通过 SpiderFlat / MacVLAN CNI / SRI-OV CNI 提供对外访问 IP，实现 Pod 二层对外通信能力，搭配 Calico 动态虚拟网络，降低网络运维难度，节省 IP 资源。
   在此方案组合中，Calico 为必备的网络 CNI。如果在应用落地场景中，没有对外访问需求，可以不安装 Underlay CNI。
4. 通过 Submariner 组件打通跨集群 Pod 间的通信，结合 Submariner 及 Core DNS 服务发现，实现集群间的服务发现能力。Submariner 可根据需求选择安装。

![solution02](../images/solution02.png)

## 网络组件

按照上述两种方案，DCE 5.0 可以安装的网络组件包括：

- [Calico](../modules/calico/what.md)：基于 Linux kernel 技术实现的 Virtual Router,完成数据平面的转发。
- [Cilium](../modules/cilium/what.md)：基于 eBPF 内核构建的网络方案
- [Contour](../modules/contour/what.md)：一个开源的 Kubernetes Ingress 控制器，使用 Envoy 作为数据面。
- [f5networks](../modules/f5networks/what.md)：全面控制 F5 设备，将集群中 service 和 ingress 配置同步到 F5 硬件设备上，实现集群北向入口的负载均衡。
- [Ingress-nginx](../modules/metallb/what.md)：是 Kubernetes 官方社区托管的 Ingress 控制器，使用 nginx 作为反向代理和负载均衡
- [MetalLB](../modules/metallb/what.md)：裸金属版的 Kubernetes 负载均衡器实现
- [Multus-underlay](../modules/multus-underlay/what.md)：基于 Multus、搭配 Macvlan + SRIOV-CNI 的多网卡实现
- [Spiderpool](../modules/spiderpool/what.md)：自动化管理 IP 资源

以上所有 CNI 和 Ingress 等组件可以按需安装。我们的愿景是：牵线搭桥赋能万物互联，融合多 CNI 君臣佐使一应俱全。

[下载 DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
[申请社区免费体验](../../dce/license0.md){ .md-button .md-button--primary }
