# 什么是 Spiderpool

Spiderpool 是一个 IP 地址管理 (IPAM) 插件，可为容器云平台分配 IP 地址。
大部分的 Overlay CNI 都具备符合功能特性的 IPAM 组件，SpiderPool 的主要是设计目标是搭配 Underlay CNI
（例如 [MacVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、
[VLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan)、
[IPVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)等）进行 IP 的精细化管理。

Spiderpool 适用于任何能够对接第三方 IPAM 的 CNI 插件，尤其适合于一些缺失 IPAM 的 CNI，
包括 [SRI-OV](https://github.com/k8snetworkplumbingwg/sriov-cni)、
[MacVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、
[IPVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)、
[OVS-CNI](https://github.com/k8snetworkplumbingwg/ovs-cni) 等。
而一些 overlay CNI 自带了 IPAM 组件，对 Spiderpool 需求相对较低。

spiderpool 具备以下特点：
* CRD 设计，全面的状态和事件展示
* 应用绑定 ippool 具备多种渠道，包括 annotaiton静态指定、annotaiton智能分配、租户默认池、集群默认池、CNI配置文件等
* ippool 的节点亲和性设置，帮助同一应用解决跨子网分配 IP 地址等特殊需求。
* “应用固定 IP 地址范围” 场景的智能管理，包括智能创建ippool、弹性扩缩容IP数量、智能回收ippool等
* 防止 IP 地址泄露的回收机制，避免IP浪费
* ipv4-only、ipv6-only 和 dual-stack 集群的支持
* statefulset 支持
* 配合multus，在对多网卡场景下，支持不同网卡的进行独立指定 ippool
* 预留集群外部的IP地址，使得IPAM永不分配给 pod 使用
* 路由定制
* 丰富的metrics
