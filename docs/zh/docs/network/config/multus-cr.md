# 创建 Multus CR

Multus CR 管理，是 Spiderpool 对 Multus CNI 中配置实例的二次封装。旨在为容器提供更灵活的网络连接和配置选项，以满足不同的网络需求，
为用户提供更简单和经济高效的使用体验。本页介绍在创建工作负载使用多网卡配置之前，如何创建 Multus CR。
如需创建新的 **Multus CR 实例**，可参考此文档。

## 前提条件

[SpiderPool 已成功部署](https://docs.daocloud.io/network/modules/spiderpool/install.html), SpiderPool [v0.8.7](https://github.com/spidernet-io/spiderpool/releases/tag/v0.8.7) 已包含 Multus-underlay 的全部功能。

## 界面操作

1. 登录 DCE UI 后，在左侧导航栏点击 __容器管理__ —> __集群列表__，找到对应集群。然后在左侧导航栏点击 __容器网络__ —> __网络配置__。

    ![网络配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/networkconfig01.png)

2. 进入 __网络配置__ —> __Multus CR 管理__ ，点击创建 __Multus CR__ 。

    ![Multus CR 管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/networkconfig02.png)
  
    !!! note

        注意：创建 Multus CR 时，CNI 类型只能为 macvlan、ipvlan、sriov 和自定义四种类型四选一，可分成三种场景，参考以下三种参数方式进行配置。

### 创建 macvlan 或 ipvlan 类型的 Multus CR

请输入如下参数：

![创建 Multus CR](../images/multus01.png)

参数说明:

- __名称__ ：Multus CNI 配置的实例名称，即 Multus CR 名称。
- __描述__ ：实例的描述信息。
- __CNI 类型__ ：CNI 的类型，目前界面可选择 macvlan，ipvlan。
- __VLAN ID__ ：当 CNI 类型为 macvlan，ipvlan，sriov 时被允许配置， "0" 和 ""的效果一样。
- __网卡配置__：网卡配置中包含接口配置信息。
    - 请确保主网卡存在于主机上。
    - 如果使用基于 MacVlan/IPVlan 的共享 RDMA 功能，请确保该网卡具备 RDMA 能力。
    - 当网卡接口数量为一个时，则默认网卡配置中只有一个网卡接口。当添加接口数量大于等于两个时，可以做 Bond 相关配置。
- __网卡接口__ ：只用于 CNI 类型 为 macvlan，ipvlan ，至少有一个元素。如果有两个及其以上的元素, bond 必须不能为空。
- __Bond 信息__：名称不能为空，模式必须在范围 [0,6] 内, 分别对应七种模式：
    - balance-rr
    - active-backup
    - balance-xor
    - broadcast
    - 802.3ad
    - balance-tlb
    - balance-alb

- `IPv4 默认池`：CNI 配置文件 IPv4 默认池。
- `IPv6 默认池`：CNI 配置文件 IPv6 默认池。
参数是可选的, 输入格式为 `k1=v1;k2=v2;k3=v3`，用 `;` 隔开。

#### VLAN 配置说明

- Underlay 网络是指底层物理网络，通常涉及 VLAN 网络。如果 Underlay 网络不涉及到 VLAN 网络，不需要配置 VLAN ID (默认值为 0 即可)。
- **对于 VLAN 子接口**:
    - 如果网络管理员已经创建好 **VLAN 子接口**，那么不需要填写 VLAN ID (默认值为 0 即可)，只需要将创建好的 **VLAN 子接口** 填入到网卡接口(Master) 字段。
    - 如果需要自动创建 **VLAN 子接口** ，那么需要配置 VLAN ID，并将主网卡接口(Master)设置为对应的 **父接口**
    Spiderpool 在创建 Pod 时，在主机上动态创建一个名为: `<master>.<vlanID>` 的 **子接口**，以将 Pod 连接到 VLAN 网络。
- **对于 Bond 网卡**:
    - 如果网络管理员已经创建好 **Bond 网卡**，并且使用 **Bond 网卡** 连接 Pod 的 Underlay 网络，那么不需要填写 VLAN ID (默认值为 0 即可)
      只需要将创建好的 **Bond 网卡名称** 填入到网卡接口(Master) 字段。
    - 如果网络管理员已经创建好 **Bond 网卡**，并且使用 **Bond 网卡** 连接 Pod 的 Underlay 网络，
      那么不需要填写 VLAN ID (默认值为 0 即可)，只需要将创建好的 **Bond 网卡名称** 填入到网卡接口(Master) 字段。
    Spiderpool 在创建 Pod 时，在主机上动态创建一张 **Bond 网卡**，以用于连接 Pod 的 Underlay 网络。
- **对于 RDMA 网卡**：
    - 如果基于 Macvlan/IPVLAN/SRIOV 暴露主机上的 RoCE 网卡给到 Pod 使用时， VLAN ID 无需填写，默认为 0 即可。

- **使用 Bond 网卡创建 VLAN 子接口**：
    - 如果需要在创建 **Bond 网卡** 的同时，需要创建VLAN 子接口来承接 Pod 网络， 需要配置 VLAN ID
      Spiderpool 在创建 Pod 时，在主机上动态创建一个名为: `<bondName>.<vlanID>` 的 **VLAN 子接口** ，以用于连接 Pod 的 VLAN 网络。
    - 所有通过 Spiderpool 创建的接口，都不会配置 IP，并且这些接口不是持久化的。如果被意外删除或节点重启，这些接口将会被删除，重启 Pod 后会自动重新创建这些接口,
      如果需要持久化这些接口或者配置 IP 地址，可以考虑使用 [nmcli](https://networkmanager.dev/docs/api/latest/nmcli.html) 工具。

### 创建 SR-IOV 类型的 Multus CR

请输入如下参数：

![创建multus cr](../images/multus02.png)

- __CNI 类型__ ：选择 SR-IOV
- __Vlan ID__ : 必需填入 `0`
- __RDMA__ ：默认关闭。如果需要开启，请满足 [RDMA 资源使用条件](../modules/spiderpool/install/rdmapara.md)
- __SR-IOV 资源__ ：只用于`sriov`类型, 选择资源名称。如何查看 SR-IOV 资源 请参考：[SR-IOV CNI 配置](../modules/multus-underlay/sriov.md)

**SR-IOV 资源配置说明：**

`SR-IOV resourceName` 为部署`sriovnetworknodepolicies` 时自定义名称。

如果 **基于 SR-IOV 搭配 RDMA** 使用，SR-IOV 资源配置查询如下：

**命令查询：**
   
如下的 `spidernet.io/sriov_netdevice_enp4s0f0np0` 为查询的资源名称。

```sh
   kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
   [
     {
       "name": "10-20-1-220",
       "allocable": {
         "cpu": "56",
         "ephemeral-storage": "3971227249029",
         "hugepages-1Gi": "0",
         "hugepages-2Mi": "0",
         "memory": "131779740Ki",
         "pods": "110",
         "spidernet.io/hca_shared_devices": "0",
         "spidernet.io/mellanoxrdma": "0",
         "spidernet.io/sriov_netdevice": "0",
         "spidernet.io/sriov_netdevice_enp4s0f0np0": "8", # 查询的 RDMA 设备资源名称及数量
         ...
       }
     }
```

**界面查询：**

查询的`resourceName`需要加上 `spidernet.io/`前缀。

![networkconfig08.png](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/networkconfig08.jpg)

![networkconfig09](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/networkconfig09.jpg)

### 创建自定义类型的 Multus CR

请输入如下参数：

![创建 Multus CR](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/networkconfig05.png)

- __JSON__ ：自定义类型时，需判断输入一个合法格式的 Json 文件。

创建完成后[工作负载](use-ippool/usage.md)即可使用 Multus CR 管理。
