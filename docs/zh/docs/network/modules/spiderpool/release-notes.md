# Spiderpool Release Notes

本页列出 Spiderpool 的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2025-04-30

### v1.0.2

### 新功能

- **新增** SpiderMultusConfig 支持为 Macvlan/IPVlan/Sriov CNI 配置 MTU。
- **新增** 为 RDMA 指标添加 Pause 和 Discards 统计信息，并优化 Grafana 仪表盘。
- **新增** 支持通过设置 spiderpool-conf ConfigMap:  enableValidatingResourcesDeletedWebhook=true, 当 IPPool 和 Subnet 被删除时，Webhook 检查是否仍有 IP 分配。如果有，则不允许被删除。

#### 修复 bug

- **修复** 修复节点的 RDMA 多播指标不正确问题。
- **修复** 修复 SpiderMultusConfig 中 sriov 带宽限制不生效的问题（min/maxTxRateMbps）
- **修复** 修复 当无状态应用未经历正常的 CNI Del 流程时，IP 被 GC 但 SpiderEndpoint 残留导致该 IP 无法被正常分配，Pod 无法启动。
- **修复** 修复 Spiderpool-agent ENV(EnableGCStatelessTerminatingPod(Not)ReadyNode=false) 不工作问题。对于为正常运行的无状态应用，Spiderpool 支持通过环境变量控制是否回收其 IP，这样避免当 Pod 对象存在但其 IP 已经被回收场景。

## 2025-02-13

### v1.0.1

#### 修复 bug

- **修复** IPAM: 在做完 IP 冲突检测之后，主动发送免费 arp 更新 arp 缓存表，避免 Pod 刚创建后无法访问。
- **修复** 确保内核发送 GARP 以避免通信故障
- **修复** 更新 ippool/subnet ValidatingWebhook 所用的 Chart

## 2025-01-26

### v1.0.0

### 新功能

- **新增** 支持为 SpiderMultusConfig 和 Pod 注入相同注解: `cni.spidernet.io/network-resource-inject`, Webhook 能够将相关的 SpiderMultusConfig 中网卡以及网络硬件资源注入到 Pod 中。
- **新增** 升级 Multus 版本到 V4.0
- **新增** 支持为 AI 应用提供 Pod 与 节点级别的 RDMA 监控能力
- **新增** Spidermultusconfig 增加 chain CNI 支持，支持 tuning 等插件
- **新增** 支持 IPPool 的通配符筛选
- **新增** 支持卸载 Spiderpool 时清理各种资源
- **新增** 支持从 Kube-controller-manager Pod 中获取集群的子网，避免 kubeadm-config 未提供时无法获取

#### 修复 bug

- **修复** IPAM: 修复 StatefulSet 无法运行在多网卡模式。
- **修复** 修复当 spiderpool-agent 的 container 重启但 Pod 未重启时，节点上的 00-multus.conf 被删除，导致 Pod 无法使用多网卡。
- **修复** 修复在 Statefulset Pod 扩大/缩小期间，Spiderpool 无法正确的 GC  IP 地址，导致 IP 冲突
- **修复** 修复 Coordinator 在多网卡时，策略路由表异常导致通信失败
- **修复** 修复 RBAC 权限过高导致潜在的 CVE 风险
- **修复** 修复在子网过大时，IP 分配缓慢的问题
- **修复** 修复 Pod 多网卡时，访问 NodePort 失败

## 2025-01-26

### v0.9.9

### 新功能

- **新增** 在 IPAM 中做 IP 冲突和网关可达性检测，而不是在 Coordinator 插件中。否则当 IP 冲突时错误的 arp 缓存表可能被更新，在使用固定 IP 的应用迁移场景，导致应用短暂不可通信。

## 2025-01-03

### v0.9.8

### 新功能

- **新增** 添加一个开关，决定是否 istio 的 veth0 配置链路本地地址，避免 istio 无法劫持流量

#### 修复 bug

- **修复** SpiderMultusConfig 检查 multus.spidernet.io/cr-name 指定的 Name 是否冲突
- **修复** IPAM: 修复多网卡下，一个网卡 IP 短缺造成其他网卡 IP 池被耗尽的问题
- **修复** 修复 Cilium 运行在 Multi-pool IPAM 模式时，Spiderpool-controller Panic 问题
- **修复** 确保在检测网关之前检测 IP 冲突，避免潜在的通信失败问题

## 2024-09-26

### v0.9.7

#### 修复 bug

- **修复** 修复 Panic 错误当 Webhook 验证创建 SpiderMultusConfig 的 podRPFilter 字段
- **修复** Webhook 验证创建 SpiderMultusConfig 时，检查 podMACPrefix 是否是单播的 Mac 地址

## 2024-09-04

### v0.9.6

#### 修复 bug

- **修复** chart 中 tuneSysctlConfig 值未正确工作。
- **修复** 能正确更新 GOMAXPROCS 配置

## 2024-08-25

### v0.9.5

#### 修复 bug

- **修复** 修改 StatefulSet Pod 注释中所使用的池，能够在重新创建时使用新池的 IP 地址
- **修复** 当 Pod 拥有多个网卡时无法访问 NodePort。
- **修复** 当 spiderpool-agent 的健康检查失败，导致 00-multus.conf 丢失时，Pod 无法使用期望的 CNI 启动。
- **修复** spiderpool-init pod 安装阻塞的问题。
- **修复** 在 StatefulSet Pod 快速扩展/缩小期间，Spiderpool GC 的 IP 地址不正确，导致 IP 冲突。
- **修复** coordinator 应仅为 Pod 设置 rp_filter，而不是节点。
- **修复** coordinator：修复 Pod 有多个网卡时的错误的策略路由表。

#### 功能变更

- **新增** spiderpool-agent：支持配置 sysctl 配置
- **新增** spiderpool-agent 可以将每个节点 rp_filter 设置为 0
- **新增** 为 spidermultusconfig 添加 chainCNI 支持

## 2024-06-26

### v0.9.4

#### 修复 bug

- **修复** 将 link-local IP 添加到 istio Pod 的 veth0，确保节点上可访问同节点的 Pod 。
- **修复** 使用超大 CIDR 地址范围的子网创建 Pod ，分配 IP 性能缓慢。

#### 功能变更

- **优化** coordinator: 检测网关时使用 arp 而不是 icmp，避免由于路由器禁止 icmp，而导致检查失败，并且 icmp 也需要 arp 来获取目标 mac。

## 2024-08-25

### v0.8.8

#### 修复 bug

- **修复** 修改 StatefulSet Pod 注释中所使用的池，能够在重新创建时使用新池的 IP 地址
- **修复** 当 Pod 拥有多个网卡时无法访问 NodePort。
- **修复** 当 spiderpool-agent 的健康检查失败，导致 00-multus.conf 丢失时，Pod 无法使用期望的 CNI 启动。
- **修复** spiderpool-init pod 安装阻塞的问题。
- **修复** 在 StatefulSet Pod 快速扩展/缩小期间，Spiderpool GC 的 IP 地址不正确，导致 IP 冲突。
- **修复** coordinator 应仅为 Pod 设置 rp_filter，而不是节点。
- **修复** coordinator：修复 Pod 有多个网卡时的错误的策略路由表。
- **修复** chart 中 tuneSysctlConfig 值未正确工作。

#### 功能变更

- **新增** spiderpool-agent：支持配置 sysctl 配置
- **新增** spiderpool-agent 可以将每个节点 rp_filter 设置为 0
- **新增** 为 spidermultusconfig 添加 chainCNI 支持

## 2024-06-25

### v0.8.7

#### 修复 bug

- **修复** coordinator：确保 hijickRoute 的 gw 来自 hostIPRouteForPod，而不是 nodelocaldns 中。
- **修复** 将 link-local IP 添加到 istio Pod 的 veth0，确保节点上可访问同节点的 Pod 。
- **修复** 使用超大 CIDR 地址范围的子网创建 Pod ，分配 IP 性能缓慢。

#### 功能变更

- **优化** coordinator: 检测网关时使用 arp 而不是 icmp，避免由于路由器禁止 icmp，而导致检查失败，并且 icmp 也需要 arp 来获取目标 mac。
