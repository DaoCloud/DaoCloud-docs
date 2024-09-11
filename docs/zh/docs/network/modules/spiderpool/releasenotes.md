# Spiderpool Release Notes

本页列出 Spiderpool 的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2024-09-04

### v0.9.6

#### 修复 bug

- **修复** chart 中 tuneSysctlConfig 值未正确工作。
- **修复** 能正确更新 GOMAXPROCS 配置

## 2024-08-25

### v0.9.5

#### 修复 bug

- **修复** 修改 Statefulset Pod 注释中所使用的池，能够在重新创建时使用新池的 IP 地址
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

- **修复** 修改 Statefulset Pod 注释中所使用的池，能够在重新创建时使用新池的 IP 地址
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
