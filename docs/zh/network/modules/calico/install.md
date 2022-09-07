# 安装

本页说明如何用 Kubespray 安装 Calico 的配置说明。

### `enable_dual_stack_networks`

是否启用双栈：`false`

建议根据实际情况开启，可作为安装配置项。

### `ipv4_pools`

这是默认 IPv4 地址池。由 `calico_pool_cidr` 指定（默认未设置，由全局变量 `kube_pods_subnet` 指定）。

建议与 `kube_pods_subnet` 保持一致，可在安装时暴露配置项。

### `ipv6_pools`

这是默认 IPv6 地址池。由 `calico_pool_cidr_ipv6` 指定（默认未设置，由全局变量 `kube_pods_subnet_ipv6` 指定）。

建议与 `kube_pods_subnet_ipv6` 保持一致，可在安装时暴露配置项。

### `calico_pool_blocksize`

默认的 ippool(ipv4) 的 blockSize。

默认该字段未定义，由全局变量 `kube_pods_subnet` 控制，默认为 24。

默认即可，但必须根据集群规模来设定，至少每个节点拥有一个 block，可在安装时暴露配置项。

### `calico_pool_blocksize_ipv6`

默认的 ippool(ipv6) 的 blockSize。

由 `calico_pool_blocksize_ipv6` 定义，默认为 116。

默认即可，但必须根据集群规模来设定，至少每个节点拥有一个 block，可在安装时暴露配置项。

### `calico_vxlan_mode`

表示是否启用 vxlan 隧道模式。

默认启用。如没特殊要求，默认启用 vxlan 模式。

可在安装时暴露配置项，默认 always。

### `calico_ipip_mode`

表示是否启用 ipip 隧道模式。

默认关闭。如没特殊要求，默认启用 vxlan 模式。

可在安装时暴露配置项，默认 Never。

### `calico_felix_prometheusmetricsenabled`

是否暴露 felix metrics。

默认关闭，可根据需求决定是否打开。

可在安装时暴露配置项，默认 false。

### `nat_outgoing`

跨 ippool 池访问，是否需要 snat。

默认开启，推荐开启。

可在安装时暴露配置项，默认 true。

### `calico_allow_ip_forwarding`

是否在容器命名空间内开启 `ip_forwarding`。

默认 false，推荐 false。

不建议作为基础配置项，可作为高级配置项。

### `calico_datastore`

Calico 数据存储引擎、kdd 或 etcd。

默认 kdd，推荐 kdd。

### `calico_iptables_backend`

CentOS 8.0 下的 `calico iptables backend mode` 需要和主机的 iptables 模式保持一致。

由 `calico_iptables_backend` 配置，默认为 "Auto"。

需要和主机的 iptables 模式保持一致。

只针对于 CentOS 8.0。

