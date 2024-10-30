# Macvlan
### Macvlan Standalone
Macvlan Standalone 是一种独立的 Macvlan 配置方式，适用于需要单独管理 Macvlan 网络的场景。


### Macvlan Overlay
Macvlan Overlay 是一种叠加的 Macvlan 配置方式，适用于需要与其他网络插件协同工作的场景。

Macvlan 是 Linux 的一种网卡虚拟化的解决方案，它可以将一张物理网卡虚拟为多张虚拟网卡。
借助 Multus，可以为 Pod 分配一张或者多张 Macvlan 网卡，从而实现 Pod 借助 Macvlan 网卡与外部通讯。
### 使用场景
根据不同的网络需求选择合适的 Macvlan 配置方式，以实现最佳的网络性能和管理灵活性。


## 安装

在 Kubernetes 中，Macvlan 只是存放于每个节点 `/opt/cni/bin` 下的一个二进制文件，不存在单独的安装方式。
默认情况下，安装集群时将包括 Macvlan 在内的多个插件复制到每个节点的 `/opt/cni/bin` 下。
如果在节点的 `/opt/cni/bin` 下未发现 Macvlan 的二进制文件，
那么需要手动下载 [cni-plugins](https://github.com/containernetworking/plugins/releases/download/v1.1.1/cni-plugins-linux-amd64-v1.1.1.tgz)，
并解压到各个节点上。而安装 multus-underlay 时，仅创建属于 Macvlan 的 Multus network-attachment-definition CRD 对象。

## 说明

Multus + Macvlan 一般会有两种使用场景：

- Macvlan-standalone

    类型为 Macvlan-standalone ，意味着 Pod 的第一张网卡 (eth0) 为 Macvlan 分配的网卡，通过在 Pod 的 `annotations` 中插入如下字段：

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
    ```

    注意：Macvlan-standalone 只与 Macvlan-standalone 类型搭配，不能与 Macvlan-overlay 搭配。你可以通过下面的方式为 Pod 插入多张 Macvlan 网卡：

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
      k8s.v1.cni.cncf.io/networks: kube-system/macvlan-standalone-vlan0
    ```

- Macvlan-overlay

    此类型意味着 Macvlan-overlay 类型的 CNI 搭配（如 calico 或 cilium），Macvlan 不作为 Pod 的缺省 CNI，即不会是 Pod 的第一张网卡 (eth0)。
    所以 Macvlan-overlay 类型的 Pod 要与 overlay 类型的 Pod 能够正常通讯。你可以通过下面的方式为 Pod 多分配一张网卡：

    ```yaml
    annotations:
      k8s.v1.cni.cncf.io/networks: kube-system/macvlan-overlay-vlan0
    ```

    !!! caution

        `v1.multus-cni.io/default-network` 的值不能为 Macvlan-overlay 类型的 CRD，即 Macvlan-overlay 不能作为 Pod 的第一张网卡。

## 其他

使用 Macvlan 一个比较常见的网络场景：

![](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/vlan.png)

如图所示，将主机上两个物理接口（ens224、ens256）组成一个 bond0，然后根据 bond0 创建两个 VLAN 子接口，分别是 bond0.100 和 bond0.200。
然后将 bond0（也就是 ens224 和 ens256）与交换机 trunk 相连。并且在交换机上配置允许 VLAN100 和 VLAN200 通过。

然后创建两个不同 VLAN 的 Macvlan-multus 实例，它们的 master 接口分别为 bond0.100 和 bond0.200。
这样使用不同 Macvlan-multus 实例创建的 Pod 也就属于不同的 vlan 了。但它们都可以通过交换机做到同 vlan 或不同 vlan 之间的通讯。

!!! note

    它们的网关应该指向交换机对应的 VLANIF IP 地址。

这是一个比较常见、稍复杂的网络拓扑。总结：

- 在主机上创建 bond 和 VLAN 接口
- 配置交换机
- 创建 multus 的 CRD 实例
- 创建不同的 Spiderpool IP 池
- 在 Pod 的 annotations 中指定对应的实例和选择对应的 spiderpool IP 池

在主机上创建 bond 和 VLAN 等接口，可以参考 [nmstat 用法](nmstat.md)。
