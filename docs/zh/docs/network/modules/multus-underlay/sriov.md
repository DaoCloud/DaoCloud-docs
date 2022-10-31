# SRIOV-CNI 配置

## 环境要求

使用 SRIOV-CNI 需要先确认节点是否为物理主机并且节点拥有支持 SRIOV 的物理网卡。如果节点为 VM 虚拟机或者没有支持 SRIOV 的网卡，那么 SRIOV 将无法工作。可通过下面的方式检查节点是否存在支持 SRIOV 功能的网卡:

- 检查是否支持 SRIOV

通过`ip link show`获取所有网卡:

```shell
root@172-17-8-120:~# ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:fc brd ff:ff:ff:ff:ff:ff
    altname enp1s0f0
3: eno2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:fd brd ff:ff:ff:ff:ff:ff
    altname enp1s0f1
4: eno3: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:fe brd ff:ff:ff:ff:ff:ff
    altname enp1s0f2
5: eno4: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:ff brd ff:ff:ff:ff:ff:ff
    altname enp1s0f3
6: enp4s0f0np0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 04:3f:72:d0:d2:86 brd ff:ff:ff:ff:ff:ff
7: enp4s0f1np1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 04:3f:72:d0:d2:87 brd ff:ff:ff:ff:ff:ff
8: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
    link/ether 02:42:60:cb:04:10 brd ff:ff:ff:ff:ff:ff
```

过滤常见的虚拟网卡(如docker0、cali*、vlan子接口等), 以 `enp4s0f0np0` 为例, 确认其是否支持 SRIOV :

```shell
root@172-17-8-120:~# ethtool -i enp4s0f0np0
driver: mlx5_core    # 网卡驱动
version: 5.15.0-52-generic
firmware-version: 16.27.6008 (LNV0000000033)
expansion-rom-version:
bus-info: 0000:04:00.0  # PCI 设备号
supports-statistics: yes
supports-test: yes
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: yes
```

通过 `bus-info` 查询其 pci 设备详细信息:

```shell
root@172-17-8-120:~# lspci -s 0000:04:00.0 -v | grep SR-IOV
	Capabilities: [180] Single Root I/O Virtualization (SR-IOV)
```

如果输出有上面此行, 说明此网卡支持 SRIOV 。 获取此网卡的 vendor 和 device :

```shell
root@172-17-8-120:~# lspci -s 0000:04:00.0 -n
04:00.0 0200: 15b3:1017
```

- `15b3`: 表示此 PCI 设备的厂商号, 如`15b3`表示 Mellanox.
- `1017`: 表示此 PCI 设备的设备型号, 如`1017`表示 Mellanox  MT27800 Family [ConnectX-5] 系列网卡.

> 可通过`https://devicehunt.com/all-pci-vendors`查询所有PCI设备信息

- 配置 VFs

通过下面的方式为 支持SRIOV 网卡配置 VFs:

```shell
root@172-17-8-120:~# echo 8 > /sys/class/net/enp4s0f0np0/device/sriov_numvfs
```

确认 VFs 配置成功:

```shell
root@172-17-8-120:~# cat /sys/class/net/enp4s0f0np0/device/sriov_numvfs
8
root@172-17-8-120:~# ip l show enp4s0f0np0
6: enp4s0f0np0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 04:3f:72:d0:d2:86 brd ff:ff:ff:ff:ff:ff
    vf 0     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 1     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 2     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 3     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 4     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 5     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 6     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 7     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
```

输出上图内容, 表示配置成功.

## 安装 SRIOV-CNI

通过安装 Multus-underlay 来安装 SRIOV-CNI ,具体安装流程参考 [安装](install.md). 注意, 安装时需正确配置 `sriov-device-plugin` resource资源, 包括vendor、device等信息。否则 SRIOV-Device-Plugin
无法找到正确的 VFs .

## 配置 SRIOV-Device-Plugin

安装完 SRIOV-CNI 之后, 通过下面的方式查看 SRIOV-CNI 是否发现了主机上的 VFs :

```shell
root@172-17-8-110:~# kubectl describe nodes 172-17-8-110
...
Allocatable:
  cpu:                           24
  ephemeral-storage:             881675818368
  hugepages-1Gi:                 0
  hugepages-2Mi:                 0
  intel.com/sriov-netdevice:     8      # 此行表示 SRIOV-CNI 成功的发现了该主机上的 VFs 
  memory:                        16250260Ki
  pods:                          110
```

## 使用

使用 SRIOV-CNI 创建工作负载需要注意下面三个方面:

- 确认 SRIOV multus network-attachment-definition对象中存在 `sriov-device-plugin` resource:

```shell
root@172-17-8-110:~# kubectl get network-attachment-definitions.k8s.cni.cncf.io -n kube-system sriov-vlan0 -o yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.v1.cni.cncf.io/resourceName: intel.com/sriov_netdevice
  name: sriov-vlan0
  namespace: kube-system
```

`resourceName`必须与注册到 `kubelet` 中的资源名称保持一致(即和 Node 对象中的名称保持一致)。

> 创建 network-attachment-definition 对象后, 再更新 annotations: `k8s.v1.cni.cncf.io/resourceName` 不会生效！

- 创建工作负载时, 需要在 Pod 的 annotations 字段中通过 multus 的注解绑定指定的 network-attachment-definition 对象:

    - 如果 type 为 sriov-overlay，那么需要在 Pod 的 Annotations 中插入以下的注解：

        ```yaml
          annotations:
            k8s.v1.cni.cncf.io/networks: kube-system/sriov-overlay-vlan0
        ```

        `k8s.v1.cni.cncf.io/networks`：表示会在 Pod 中除默认 CNI 之外再插入一张 SRIOV-CNI 网卡。

    - 如果 type 为 sriov-standalone，那么需要在 Pod 的 Annotations 中插入以下的注解：

        ```yaml
          annotations:
            v1.multus-cni.io/default-network: kube-system/sriov-standalone-vlan0
        ```

        `v1.multus-cni.io/default-network`：修改 Pod 的默认网卡。如果不指定，将通过集群默认 CNI 为 Pod 分配第一张网卡。

- 在 Pod 的 Resource 字段中给予容器 SRIOV 资源配额:

```yaml
...
    containers:
        resources:
          requests:
            intel.com/sriov-netdevice: '1'
          limits:
            intel.com/sriov-netdevice: '1'
...
```

名称需要保持一致, 否则 Pod 会因为请求不到 VF 而创建失败。