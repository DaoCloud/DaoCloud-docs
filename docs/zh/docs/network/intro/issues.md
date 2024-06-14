# 网络组件已知问题与内核兼容性相关汇总

## kube-proxy

### ipvs 模式

#### 问题 1：访问服务有 1s 延迟或者请求失败问题

现象：

1. 通过 Service 访问服务有 1s 延迟
2. 滚动更新业务，有部分请求失败

影响：

| k8s版本 | kube-proxy 行为                                              | 对应现象                                                                                                                                                                         |
| ------- | ------------------------------------------------------------ |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <=1.17  | net.ipv4.vs.conn_reuse_mode=0                                | RealServer 无法被移除，当滚动更新业务，有部分请求失败。                                                                                                                                            |
| >=1.19  | net.ipv4.vs.conn_reuse_mode=0 (kernel > 4.1)<br />net.ipv4.vs.conn_reuse_mode=1 (kernel < 4.1) | CentOS 7.6-7.9，默认内核版本低于 4.1，存在通过 Service 访问服务有 1s 延迟问题。<br />CentOS 8 默认内核 4.16 高于 4.1，存在 RealServer 无法被移除，当滚动更新业务，有部分请求失败。                                                  |
| >=1.22  | 不修改 net.ipv4.vs.conn_reuse_mode 值（kernel > 5.6）<br />net.ipv4.vs.conn_reuse_mode=0 (kernel > 4.1)<br />net.ipv4.vs.conn_reuse_mode=1 (kernel < 4.1)<br /> | CentOS 7.6-7.9，默认内核版本低于 4.1，存在通过 Service 访问服务有 1s 延迟问题。<br />CentOS 8 默认内核 4.16 高于 4.1，存在 RealServer 无法被移除，当滚动更新业务，有部分请求失败。 <br />Ubuntu 22.04 默认内核版本 5.15，高于 5.9 内核，不存在该问题。 |

建议：

对于低于 5.9 内核的系统，不推荐使用 ipvs 模式。

参考：
* https://github.com/kubernetes/kubernetes/issues/93297

### iptables 模式

#### 问题 1：源端口 nat 以后不够随机，导致 1s 延时

影响：

| 内核   | iptables 版本 | 对应现象                                |
| ------ | ------------- | --------------------------------------- |
| < 3.13 | 1.6.2         | 源端口 nat 以后不够随机，导致 1s 延时。 |

建议：

参考系统发行版本，升级内核。


## calico

#### 问题 1：offload vxlan 导致访问延迟问题

影响：

| calico 版本 | 行为                                                         | 影响                                              |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------- |
| <v3.20     | 不处理                                                       | 内核 < 5.7，Pod 与 Service 之间延迟 63s。         |
| >=v3.20    | 可以通过 FelixConfiguration 配置，默认自动关闭 vxlan offload。 | 导致网卡性能低，只能跑到 1-2 Gbps/s。             |
| >= 3.28    | 在 5.7 内核自动打开 vxlan offload， 解决之前的 ClusterIP 访问丢包问题，提高性能。 | 内核 < 5.7，导致网卡性能低，只能跑到 1-2 Gbps/s。 |

建议：

低版本 calico 存在访问延迟问题时，可以通过 `ethtool --offload vxlan.calico rx off tx off` 规避。高版本 calico 默认自动关闭 vxlan offload，对于网络性能有要求的客户可以升级内核到 5.7 解决。

参考：

* https://github.com/projectcalico/calico/issues/3145
* https://github.com/projectcalico/felix/pull/2811