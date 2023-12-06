# Macvlan

Macvlan 是 Linux 的一种网卡虚拟化的解决方案，它可以将一张物理网卡虚拟为多张虚拟网卡。
借助 Multus，可以为 Pod 分配一张或者多张 Macvlan 网卡，从而实现 Pod 借助 macvlan 网卡与外部通讯。

## 安装

在 Kubernetes 中，Macvlan 只是存放于每个节点 `/opt/cni/bin` 下的一个二进制文件，不存在单独的安装方式。
默认情况下，安装集群时将包括 macvlan 在内的多个插件复制到每个节点的 `/opt/cni/bin` 下。
如果在节点的 `/opt/cni/bin` 下未发现 macvlan 的二进制文件，
那么需要手动下载 [cni-plugins](https://github.com/containernetworking/plugins/releases/download/v1.1.1/cni-plugins-linux-amd64-v1.1.1.tgz)，
并解压到各个节点上。而安装 multus-underlay 时，仅创建属于 Macvlan 的 Multus network-attachment-definition CRD 对象。

## 说明

Multus + Macvlan 一般会有两种使用场景：

- macvlan-standalone

    类型为 `macvlan-standalone`，意味着 Pod 的第一张网卡 (eth0) 为 macvlan 分配的网卡，通过在 Pod 的 `annotations` 中插入如下字段：

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
    ```

    注意：macvlan-standalone 只与 macvlan-standalone 类型搭配，不能与 macvlan-overlay 搭配。你可以通过下面的方式为 Pod 插入多张 macvlan 网卡：

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
      k8s.v1.cni.cncf.io/networks: kube-system/macvlan-standalone-vlan0
    ```

- macvlan-overlay

    此类型意味着 macvlan 与 overlay 类型的 CNI 搭配（如 calico 或 cilium），macvlan 不作为 Pod 的缺省 CNI，即不会是 Pod 的第一张网卡 (eth0)。
    所以 macvlan-overlay 类型的 Pod 要与 overlay 类型的 Pod 能够正常通讯。你可以通过下面的方式为 Pod 多分配一张网卡：

    ```yaml
    annotations:
      k8s.v1.cni.cncf.io/networks: kube-system/macvlan-overlay-vlan0
    ```

    !!! caution

        `v1.multus-cni.io/default-network` 的值不能为 macvlan-overlay 类型的 CRD，即 macvlan-overlay 不能作为 Pod 的第一张网卡。

## 其他

使用 macvlan 一个比较常见的网络场景：

![](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/vlan.png)

如图所示，将主机上两个物理接口（ens224、ens256）组成一个 bond0，然后根据 bond0 创建两个 VLAN 子接口，分别是 bond0.100 和 bond0.200。
然后将 bond0（也就是 ens224 和 ens256）与交换机 trunk 相连。并且在交换机上配置允许 vlan100 和 vlan200 通过。

然后创建两个不同 vlan 的 macvlan multus 实例，它们的 master 接口分别为 bond0.100 和 bond0.200。
这样使用不同 macvlan multus 实例创建的 Pod 也就属于不同的 vlan 了。但它们都可以通过交换机做到同 vlan 或不同 vlan 之间的通讯。

注意：它们的网关应该指向交换机对应的 vlanif IP 地址。

这是一个比较常见、稍复杂的网络拓扑。总结：

- 在主机上创建 bond 和 vlan 接口
- 配置交换机
- 创建 multus 的 CRD 实例
- 创建不同的 Spiderpool IP 池
- 在 Pod 的 annotations 中指定对应的实例和选择对应的 spiderpool IP 池

在主机上创建 bond 和 vlan 等接口，可以参考 [nmstat 用法](nmstat.md)。
