# KubeVirt 固定 IP 与 Underlay 网络

本页介绍在 DCE 5.0 中使用 Spiderpool 为 KubeVirt 虚拟机提供固定 IP 与 Underlay 网络能力的推荐配置。

## 适用场景

- KubeVirt 虚拟机重启/重建/热迁移后需要保持同一 IP
- 需要让 VM 直接接入 Underlay 网络

## 网络模式与能力差异

| 模式 | 典型 CNI | 网卡数量 | Service Mesh | 热迁移 | 说明 |
| --- | --- | --- | --- | --- | --- |
| passt | macvlan/ipvlan | 单网卡 | 支持 | 不支持 | 适合轻量场景 |
| bridge | ovs-cni | 多网卡 | 不支持 | 不支持 | 适合多网卡场景 |

> 说明：Spiderpool 对 KubeVirt VM 的固定 IP 是基于 VM 维度而不是 Pod 维度记录。

## 前提条件

- 已安装 Spiderpool（参考 [安装 Spiderpool](../modules/spiderpool/install/install.md)）
- 已准备好 Underlay CNI（Macvlan/IPvlan 或 OVS）

## 关键配置

Spiderpool 默认开启 KubeVirt 固定 IP 功能。如需关闭，可在安装 Spiderpool 时设置：

- `ipam.enableKubevirtStaticIP=false`

## 示例流程（passthrough + macvlan）

1. 创建 macvlan 的 Multus 配置（参考 [Multus CR 管理](multus-cr.md)）。
2. 创建 IPPool（参考 [创建子网及 IP 池](ippool/createpool.md)）。
3. 创建 VM，并指定默认网卡配置：

```yaml
metadata:
  annotations:
    v1.multus-cni.io/default-network: kube-system/macvlan-ens192
```

创建后，VM Pod 在重启/重建场景下会持续获得相同 IP。

## 注意事项

- KubeVirt 热迁移场景下，Spiderpool 不进行 IP 冲突检测
- passt 模式只支持单网卡；bridge 模式可多网卡但不支持 Service Mesh
