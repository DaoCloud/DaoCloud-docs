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

## Spiderpool

**建议：**

如果您遇到了如下的问题，请尝试更新 Spiderpool 到更高的版本来解决。

### 0.9 版本已知问题

#### spidercoordinator 同步 status 时发生错误，但是其状态仍为 running

如果获取集群的CIDR信息失败，我们应该将其状态更新为 NotReady，这会阻止 Pod 的正常创建。否则，Pod 将使用不正确的 CIDR 运行，将造成网络连通问题。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2929

#### Values.multus.multusCNI.uninstall 设置后，不生效，导致 multus 资源没有正确删除

Values.multus.multusCNI.uninstall 设置为 true 后，卸载 Spiderpool 后，发现仍存在 multus 相关资源，它们并没有如预期的一样被删除。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2974

#### 缺失 kubeadm-config 时，无法从 kubeControllerManager Pod 获取 serviceCIDR

有些场景没有使用 kubeadm 创建集群，可能没有 kubeadm-config configMap，将会尝试从 kubeControllerManager 中获取，由于 bug 却无法从 kubeControllerManager Pod 获取 serviceCIDR，导致 Spidercoordinator 的 status 更新失败。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/3020

#### v0.9.0 的 SpiderCoordinator CRD 添加一个新属性 TxQueueLen，从 0.7.0 版本升级到该版本时，将导致 panic

Spiderpool v0.9.0 为 SpiderCoordinator CRD 添加一个新属性 `TxQueueLen` ，但在升级操作。没有默认值，将导致 panic 。需使用它并将其视为默认值 0 。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/3118

#### 由于集群部署方式不同，导致 spidercoordinator 返回空的 serviceCIDR，从而无法创建Pod

由于集群部署方式的不同，集群 kube-controller-manager Pod 中记录 CIDR 的有两种类型：`Spec.Containers[0].Command` 和 `Spec.Containers[0].Args` 。比如 RKE2 集群是 `Spec.Containers[0].Args` 而不是 `Spec.Containers[0].Command`，而在原本逻辑中 hardcode `Spec.Containers[0].Command` ，导致判断异常，返回空 serviceCIDR，而无法创建 Pod。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/3211

### 0.8 版本已知问题

#### ifacer 无法使用 vlan 0 创建 bond

使用 vlan 0 时，通过 ifacer 创建 bond 将失败。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2639

#### 禁用 multus 功能，仍创建了 multus CR 资源

当安装时，禁用了 multus 功能，仍创建了 multus CR 资源，不符合预期。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2756

#### spidercoordinator 无法检测 Pod 的 netns 中的网关连接

当前 spidercoordinator 使用插件使用 errgroup 来并发检查网关可达性和 IP 冲突，提高检测速度。由于每个操作系统线程可以有不同的网络命名空间，并且 Go 的线程调度是高度可变的，因此调用者不能保证设置任何特定的命名空间，但是在 netns.Do 中启动 goroutine 时，Go 运行时无法保证代码一定会在指定的网络命名空间中执行，因此需要修改了 Go 的 errgroup 方法：在启动 goroutine 时手动切换到目标网络命名空间，执行完毕后返回原网络命名空间，从而保证能够检查网关可达性和 IP 冲突。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2738

#### 当 kubevirt 固定 IP 功能关闭时，spiderpool-agent Pod crash

当将 kubevirt 固定 IP 功能关闭时，spiderpool-agent Pod 将 crash，无法运行，影响整体 IPAM 功能。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2971

#### SpiderIPPool 资源未继承 SpiderSubnet 的 gateway 和 route 属性

如果先创建 SpiderSubnet 资源，然后再创建对应子网的 SpiderIPPool 资源，则 SpiderIPPool 会继承 SpiderSubnet 的 gateway, routes 。但是，如果您首先创建一个孤立的 SpiderIPPool，再创建对应的 SpiderSubnet 资源；那么 SpiderIPPool 资源将不会继承 SpiderSubnet 属性。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/3011

### 0.7 版本已知问题

#### statefulset 类型的 Pod 重启后，获取 IP 分配时，提示 IP 冲突

由于 StatefulSet pod 重新启动，此时 GC scanAll 会释放之前的 IP 地址，因为系统认为 Pod UID 与 IPPool 记录的 IP 地址不同，从而提示冲突。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2538

#### 第三方控制器，如：RedisCluster 。Spiderpool 将无法识别他们，它们控制的 StatefulSet 其 Pod 无法固定 IP

RedisCluster -> StatefulSet -> Pod, 如果 Spiderpool 为其设置 SpiderSubnet 自动池注释，Pod 将无法成功启动。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2370

#### 空的 spidermultusconfig.spec, 将导致 spiderpool-controller Pod crash

使用空的 spidermultusconfig.spec 创建 CR，webhook 校验成功，但没有相关的 network-attachment-definitions 生成，并且查看到 spiderpool-controller 出现了 panic。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2444

#### cilium 模式获取到错误的 overlayPodCIDR

spidercoordinator auto 模式获取 `podCIDRType` 类型错误，更新 spidercoordinator status 状态不符合预期；创建 Pod 可能导致出现网络问题。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2434

#### Pod 与 IP 数 1:1 的场景，出现 IPAM 分配阻塞，导致一些 Pod 无法运行，对分配 IP 性能产生影响

具有 1000 个 IP 地址的 IPPool，并创建具有 1000 个副本的 Deployment，分配到一定数量的 IP 地址后，观察到分配性能下降明显，甚至无法继续分配 IP 地址，而一个 Pod 在没有 IP 地址的情况下无法正常启动。实际 IPPool 资源中已经记录了 Pod 并分配了其 IP，但 SpiderEndpoint 对应的 Pod 却不存在。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2518

#### 禁用 IP GC 功能，spiderpool-controller 组件将由于 readiness 健康检查失败而无法正确启动

禁用 IP GC 功能，spiderpool-controller 组件将由于 readiness 健康检查失败而无法正确启动

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2532

#### IPPool.Spec.MultusName 指定了 namespace ，与预期的 multusName 将亲和失败

指定了 pod Annotation: `v1.multus-cni.io/default-network: kube-system/ipvlan-eth0` 它与 multusName 亲和失败了。但如果你指定 pod Annotation `v1.multus-cni.io/default-network: ipvlan-eth0` 它可以工作，但这并不符合预期。

**参考：**

https://github.com/spidernet-io/spiderpool/pull/2514