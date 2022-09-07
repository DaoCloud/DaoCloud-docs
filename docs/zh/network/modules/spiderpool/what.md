# 什么是 Spiderpool

Spiderpool 是一个 IP 地址管理 (IPAM) 插件，可为容器云平台分配 IP 地址。
大部分的 Overlay CNI 都具备符合功能特性的 IPAM 组件，SpiderPool 的主要是设计目标是搭配 Underlay CNI（例如 [MacVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、[VLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan)、[IPVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)等）进行 IP 的精细化管理。

Spiderpool 适用于任何能够对接第三方 IPAM 的 CNI 插件，尤其适合于一些缺失 IPAM 的 CNI，包括 [SRI-OV](https://github.com/k8snetworkplumbingwg/sriov-cni)、[MacVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、[IPVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)、[OVS-CNI](https://github.com/k8snetworkplumbingwg/ovs-cni) 等。而一些 overlay CNI 自带了 IPAM 组件，对 Spiderpool 需求相对较低。
