# 网络组件已知问题与内核兼容性

本页汇总说明各个网络组件的已知问题，这些问题可能会对生产环境产生重大影响，并给出一些建议和方案。

## kube-proxy

### IPVS 模式 - 访问服务有 1s 延迟或者请求失败问题

**现象：**

1. 通过 Service 访问服务有 1s 延迟
2. 滚动更新业务，有部分请求失败

**影响：**

| k8s 版本 | kube-proxy 行为 | 现象 |
| ------ | -------------- | -------- |
| <=1.17 | net.ipv4.vs.conn_reuse_mode=0 | RealServer 无法被移除，当滚动更新业务，有部分请求失败。|
| >=1.19 | net.ipv4.vs.conn_reuse_mode=0 (kernel > 4.1)<br />net.ipv4.vs.conn_reuse_mode=1 (kernel < 4.1) | CentOS 7.6-7.9，默认内核版本低于 4.1，存在通过 Service 访问服务有 1s 延迟问题。<br />CentOS 8 默认内核 4.16 高于 4.1，存在 RealServer 无法被移除，当滚动更新业务，有部分请求失败。|
| >=1.22 | 不修改 net.ipv4.vs.conn_reuse_mode 值（kernel > 5.6）<br />net.ipv4.vs.conn_reuse_mode=0 (kernel > 4.1)<br />net.ipv4.vs.conn_reuse_mode=1 (kernel < 4.1)<br /> | CentOS 7.6-7.9，默认内核版本低于 4.1，存在通过 Service 访问服务有 1s 延迟问题。<br />CentOS 8 默认内核 4.16 高于 4.1，存在 RealServer 无法被移除，当滚动更新业务，有部分请求失败。 <br />Ubuntu 22.04 默认内核版本 5.15，高于 5.9 内核，不存在该问题。|

**建议：** 对于低于 5.9 内核的系统，不推荐使用 IPVS 模式。

**参考：** [Kubernetes Issue #93297](https://github.com/kubernetes/kubernetes/issues/93297)

### iptables 模式 - 源端口 nat 以后不够随机，导致 1s 延时

**影响：**

| 内核 | iptables 版本 | 现象 |
| ------ | ------------- | ----- |
| < 3.13 | 1.6.2 | 源端口 nat 以后不够随机，导致 1s 延时。|

**建议：** 参考系统发行版本，升级内核。


### externalIPs 在 externalTrafficPolicy: Local 下不工作

**影响：**

1.26.0 <= 受影响版本 < 1.30.0

**建议：** 升级到 1.30.0

**参考：**

https://github.com/kubernetes/kubernetes/pull/121919


### Service 的 endpoint 更新时，新 endpoint 的规则等到很久以后才生效

**影响：**

1.27.0 <= 受影响版本 < 1.30.0

**建议：** 升级到 1.30.0

**参考：**

https://github.com/kubernetes/kubernetes/pull/122204

### nftables 模式下 LoadBalancerSourceRanges 无法正常工作的问题


**建议：** 升级到 1.30.0

**参考：**

https://github.com/kubernetes/kubernetes/pull/122614

### Iptables nft 和 legacy 模式选择问题

**影响：**

| 版本    | 行为                       | 影响                      |
| ------- | -------------------------- | ------------------------- |
| <v1.18  | 使用 iptables-legacy       | Kube-proxy 可能不会工作。 |
| >=v1.18 | 自动计算，更优先选择 nft。 |                           |

**参考：**

https://github.com/kubernetes-sigs/iptables-wrappers/tree/master

## Calico

### offload vxlan 导致访问延迟问题

**影响：**

| Calico 版本 | 行为 | 影响 |
| ---------- | ---- | --- |
| <v3.20 | 不处理 | 内核 < 5.7，Pod 与 Service 之间延迟 63s。|
| >=v3.20 | 可以通过 FelixConfiguration 配置，默认自动关闭 vxlan offload。| 导致网卡性能低，只能跑到 1-2 Gbps/s。|
| >= 3.28 | 在 5.7 内核自动打开 vxlan offload， 解决之前的 ClusterIP 访问丢包问题，提高性能。| 内核 < 5.7，导致网卡性能低，只能跑到 1-2 Gbps/s。|

**建议：** 低版本 Calico 存在访问延迟问题时，可以通过 `ethtool --offload vxlan.calico rx off tx off` 规避。
高版本 Calico 默认自动关闭 vxlan offload，对于网络性能有要求的客户可以升级内核到 5.7 解决。

**参考：**

* [Calico Issue #3145](https://github.com/projectcalico/calico/issues/3145)
* [Felix Pull Request #2811](https://github.com/projectcalico/felix/pull/2811)

### vxlan 父设备改了，路由没更新的问题

**影响：**

| Calico 版本 | 行为                                               | 影响                                                         |
| ----------- | -------------------------------------------------- | ------------------------------------------------------------ |
| <v3.28.0    | 不处理                                             | 路由表未更新为使用新的父网卡，即使重新启动 felix 后，也无法清理旧的路由。 |
| >=v3.28.0   | 当父设备发生更改时，VXLAN 管理器会重新创建路由表。 | 无                                                           |

**建议：** 

更新到 v3.28 版本。

**参考：**

https://github.com/projectcalico/calico/pull/8279

### 集群 calico-kube-controllers 的缓存不同步，导致内存泄漏

**建议：** 

更新到 v3.26.0 版本。

### IPIP 模式下 Pod 跨节点网络不通

**影响：**

| Calico 版本 | 行为                     | 影响                                                         |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| <v3.28.0    | 不处理                   | 由于 `iptables --random-fully` 和 checksum 校验和计算不兼容，在内核 < 5.7，Pod 跨节点网络可能不通。 |
| >=v3.28.0   | 默认禁用 checksum 计算。 | 无                                                           |

**建议：** 

更新到 v3.28.0+ 的版本，较低版本可以使用 `ethtool -K tunl0 tx off`  命令手动关闭。

**参考：**

https://github.com/projectcalico/calico/pull/8031

### Iptables nft 和 legacy 模式选择问题

**影响：**

| Calico 版本 | 行为                                           | 影响                                                      |
| ----------- | ---------------------------------------------- | --------------------------------------------------------- |
| <v3.26.0    | 仅支持需要手动指定，自动计算存在一定逻辑问题。 | 由于 iptables 模式选择错误，可能会导致 Service 网络异常。 |
| >=v3.26.0   | 自动计算。                                     | 无                                                        |

**建议：** 

更新到 v3.26.0+ 的版本，较低版本需要手动指定 `FELIX_IPTABLESBACKEND` 变量，可选值 NFT 或者 LEGACY。

**参考：**

https://github.com/projectcalico/calico/pull/7111
