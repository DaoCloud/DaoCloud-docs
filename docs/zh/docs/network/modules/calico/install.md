# 安装参数配置

本页说明用 Kubespray 安装 Calico 时各项参数的配置。

## 前提条件

在 DCE 5.0 中安装 Calico，需要在`创建集群`—>`网络配置`页面下，`网络插件`选择 `calico`。关于创建集群，请参阅[创建工作集群](../../../kpanda/user-guide/clusters/create-cluster.md)。

## 参数配置

1. 进入`创建集群`第三步`网络配置`，配置如下参数：![calico-install](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/calico-install.png)
   1. `双栈`：是否开启双栈，默认关闭。`enable_dual_stack_networks`： 开启后，将为 pod 和 service 提供 IPv4 和 IPv6 网络。
   2. `网卡检测模式`： Calico 网卡检测模式，选择后会通过此网卡进行流量通信。
      1. `First Found`：默认模式，枚举所有的节点 IP（忽略一些常见的本地网卡，如 docker0，kube-ipvs0 等)，并选择第一个地址。
      2. `Kubernetes Internal IP`：选择 Node 对象 Status.addresses 字段的第一个内部地址。
      3. `Interface=<INTERFACE-REGEX>`：通过网卡名称或者正则表达式指定网卡。
   3. `IPtables 模式`：Calico 依赖 IPtables 实现 SNAT 以及网络策略，并且需要和主机的 IPtables 模式保持一致，否则可能会造成通讯问题。支持` Legacy`,`NFT`,`Auto`三种模式，默认为 `Legacy`模式。如果您使用的节点系统版本为 CentOS 8 / RHEL 8 / OracleLinux 8 系列，请选择 NFT 模式。
   4. `隧道模式`：Calico 支持两种数据包封装模式: IPIP 和 VXLAN，并都支持 Always 和 CrossSubnet 模式。
      1. ` VXLAN Always` 模式下，无论节点是否处于同一网段，所有跨节点数据包都将使用 VXLAN 被封装，这满足绝大部分的使用场景。
      2. `VXLAN CrossSubnet` 下，只有当节点处于不同网段时，跨节点的数据包才会被封装。
      3. `IPIP CrossSubnet` 下，只有当节点处于不同网段时，跨节点的数据包才会被封装。
      4. ` IPIP Always` 模式下，无论节点是否处于同一网段，所有跨节点数据包都将使用 IPIP 被封装，这满足绝大部分的使用场景。
   5. `IPv4 容器网段`：`kube_pods_subnet`，默认同 `ipv4_pools` 保持一致。集群下容器使用的网段，决定了集群下容器的数量上限。创建后不可修改。默认值为 10.233.64.0/18。
   6. `IPv6 容器网段`：`kube_pods_subnet_ipv6`，默认同 `ipv6_pools` 保持一致。集群下容器使用的网段，决定了集群下容器的数量上限。创建后不可修改。开启双栈后需要输入此网段信息。
   7. `服务网段`：同一集群下容器互相访问时使用的 Service 资源的网段决定了 Service 资源的上限。 创建后不可修改。默认为 10.244.0.0/18 。
2. 如果用户需要为 Calico 配置更多功能，可通过 Kubespray 安装 Calico。关于使用 Kubespray 安装 Calico 时的各项参数配置，请在`高级配置`—>`自定义参数`下根据需要添加并填写。

![calico-install](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/calico-arg.png)

以下介绍使用 Kubespray 安装 Calico 时的各项参数配置：

> 建议根据实际情况开启，可作为安装配置项。

- `calico_pool_blocksize`：默认的 ippool(ipv4) 的 blockSize。

    默认该字段未定义，由全局变量 `kube_pods_subnet` 控制，默认为 24。

    > 使用默认配置即可，但必须根据集群规模来设定，至少每个节点拥有一个 block，可在安装时暴露配置项。

- `calico_pool_blocksize_ipv6`：默认的 ippool(ipv6) 的 blockSize。

    由 `calico_pool_blocksize_ipv6` 定义，默认为 116。

    > 使用默认配置即可，但必须根据集群规模来设定，至少每个节点拥有一个 block，可在安装时暴露配置项。

- `calico_felix_prometheusmetricsenabled`：是否暴露 felix metrics。

    默认关闭，可根据需求决定是否打开。

    > 可在安装时暴露配置项，默认 false。

- `nat_outgoing`：跨 ippool 池访问，是否需要 snat。

    默认开启，推荐开启。

    > 可在安装时暴露配置项，默认 true。

- `calico_allow_ip_forwarding`：是否在容器命名空间内开启 `ip_forwarding`。

    默认 false，推荐 false。

    > 不建议作为基础配置项，可作为高级配置项。

- `calico_datastore`：Calico 数据存储引擎、kdd 或 etcd。

    默认 kdd，推荐 kdd。
