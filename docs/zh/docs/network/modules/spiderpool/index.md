---
hide:
  - toc
---

# 什么是 Spiderpool

Spiderpool 是一个 IP 地址管理 (IPAM) 插件，可为容器云平台分配 IP 地址。
大部分的 Overlay CNI 都具备符合功能特性的 IPAM 组件，SpiderPool 的主要设计目标是搭配 Underlay CNI
（例如 [MacVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、
[VLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan)、
[IPVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)等）进行 IP 的精细化管理。

Spiderpool 适用于任何能够对接第三方 IPAM 的 CNI 插件，尤其适合于一些缺失 IPAM 的 CNI，
包括 [SR-IOV](https://github.com/k8snetworkplumbingwg/sriov-cni)、
[MacVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、
[IPVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)、
[OVS-CNI](https://github.com/k8snetworkplumbingwg/ovs-cni) 等。
而一些 overlay CNI 自带了 IPAM 组件，对 Spiderpool 需求相对较低。

目前 SpiderPool 支持的能力如下：

| 功能 | 描述 |
| --- | ---- |
| 多途径的 IP Pool 的使用方式 | 1. IP Pool 可通过 Node Selector 同命名空间、节点和应用进行关联使用。 <br />2. 应用部署时可在 Annotation 中指定 IP Pool，按照优先级依次获取 IP Pool 中的 IP 资源。|
| IP Pool 的节点亲和性 | 同一集群内接入的节点可能属于不同数据中心，或者属于不同子网，因而同一个应用不同副本进行调度时，需要分配不同子网下的 IP 地址。IP Pool 的节点亲和性支持此场景。 |
| IP Pool 的命名空间亲和性 |  基于 IP Pool 的命名空间亲和性，同一 IP Pool 可以同时共享给多个 Namespace 使用。|
| 备用 IP Pool | 当 IP Pool 中 IP 地址分配完毕后，并且对应的子网已无可用 IP，可新建子网和 IP Pool，并指定给应用使用，防止应用扩容失败。|
| 应用固定 IP | 自动化创建应用固定 IP 池并选择固定 IP 范围。 |
| 应用使用默认 IP 池 | 默认 IP 池，供那些没有特定IP需求的工作负载使用。|
| 防止 IP 地址分配冲突的机制  | 1. IP Pool 中 IP 地址错开，IP Pool 间地址不重叠。 <br />2. 严格管控 IP Pool 的增删改查，规避 IP 重叠。 <br />3. 预留 IP 机制，可将已被集群外部节点使用的 IP 冻结，防止 IP 冲突。|
| 防止 IP 地址泄露的回收机制  | 在 Pod 故障、重启、重建等场景下，清理 IP 资源被一些 “僵尸 Pod” 占用的垃圾数据，规避可用 IP 减少问题。 在 overlay IPAM 场景下，因为 CIDR 范围很大，所以该问题并不突出。而在 underlay 场景下，IP 资源有限，且部分应用有固定 IP 地址范围的需求，该问题就会影响应用的健康运行。 |
| 双栈支持 | 支持 ipv4-only、ipv6-only 和 dual-stack。|
| Statefulset 支持 | Statefulset Pod 在重启、重建场景下，持续获取到相同的 IP 地址。|
| Pod 多网卡支持 | 配合 Multus，实现对多网卡场景下的 IP 分配支持。|
| 预留 IP | 预留 IP 机制，可将已被集群外部节点使用的 IP 冻结，防止 IP 冲突。|
| 多层级路由定制 | 支持子网 CIDR、IP Pool、应用级别的自定义路由，路由优先级由低至高。|
| 丰富的 Metrics | 提供丰富的监控指标，保障集群 IP 资源监控。|
