---
hide:
  - toc
---

# 网络规划

本页主要描述基于[网卡规划](./ethplan.md)中的 Overlay + Underlay CNI 网络方案中的的最佳实践，主要覆盖场景为：

1. Calico 搭配 Macvlan CNI
2. Calico 搭配 Macvlan 及 SR-IOV CNI

在如下场景中，最佳实践均为 2 张网卡，不同网卡承载流量如下：

1. **网卡 1（eth0）**：主要负责 Kubernetes 内部管理流量，Calico 流量，节点间通信流量
2. **网卡 2（eth1）**：主要负责 Underlay（Macvlan/SR-IOV） 网络流量

## Calico 搭配 Macvlan CNI

![calico-macvlan](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/calico-macvlan.jpg)

**规划说明**：

- 在此规划中默认 CNI 为 Calico/Cilium，需要配合安装 Multus-underlay、Spiderpool 等组件。
- 建议所有节点都具备多张物理网卡且网卡名称一致。
- eth0 为主机默认路由所在网卡，网关指向 Gateway 主机，由该主机转发到外部网络。
  主要用途为：节点间的通讯、K8s 管理网卡、Calico Pod 通信。
- eth1 为 Underlay 业务网卡，无需设置 IP 地址。
  基于 eth1 创建 VLAN 子接口 (eth1.1, eth1.2)，对应网段如 172.16.15.0/24 和 172.16.16.0/24。
  创建的业务应用 Pod 使用对应网段地址，可满足多 VLAN 多子网场景。
- eth1.1，eth1.2 VLAN 子接口可不设置 IP 地址。

## Calico 搭配 Macvlan 及 SR-IOV CNI

![macvlan-sriov](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/macvlan-sriov.jpg)

**规划说明**：

- 在此规划中默认 CNI 为 Calico/Cilium，需要配合安装 Multus-underlay、Spiderpool 等组件。
- 建议所有节点都具备多张物理网卡且网卡名称一致。
- eth0 为主机默认路由所在网卡，网关指向 Gateway 主机，由该主机转发到外部网络。
  主要用途为：节点间的通讯、K8s 管理网卡、Calico Pod 通信。
- `Worker01`、`Worker02` 中的 eth1 为 VLAN 业务网卡，无需设置 IP 地址。
  基于 eth1 创建 VLAN 子接口 (eth1.1, eth1.2)，对应网段如 172.16.15.0/24 和 172.16.16.0/24。
  创建的业务应用 Pod 使用对应网段地址，可满足多 VLAN 多子网场景。
- eth1.1，eth1.2 VLAN 子接口可不设置 IP 地址。
- `Worker03`、`Worker04` 中的 eth1 为 SR-IOV 业务网卡，无需设置 IP 地址。eth1 对应网段为 172.16.17.0/24，eth1 网段可与 eth1.1、eth1.2 属于相同网段，可根据规划需要自行决定。本示例中网段均错开。创建的业务应用 Pod 使用对应网段，并基于扩展出来的 VF（Virtual Functions）可被容器直接调用，从而实现加速。
