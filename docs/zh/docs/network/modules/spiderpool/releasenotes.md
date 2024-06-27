# Spiderpool Release Notes

本页列出 Spiderpool 的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2024-06-26

### v0.9.4

#### 修复 bug

- **修复** 将 link-local IP 添加到 istio Pod 的 veth0，确保节点上可访问同节点的 Pod 。
- **修复** 使用超大 CIDR 地址范围的子网创建 Pod ，分配 IP 性能缓慢。

#### 功能变更

- **优化** coordinator: 检测网关时使用 arp 而不是 icmp，避免由于路由器禁止 icmp，而导致检查失败，并且 icmp 也需要 arp 来获取目标 mac。

## 2024-06-25

### v0.8.7

#### 修复 bug

- **修复** coordinator：确保 hijickRoute 的 gw 来自 hostIPRouteForPod，而不是 nodelocaldns 中。
- **修复** 将 link-local IP 添加到 istio Pod 的 veth0，确保节点上可访问同节点的 Pod 。
- **修复** 使用超大 CIDR 地址范围的子网创建 Pod ，分配 IP 性能缓慢。

#### 功能变更

- **优化** coordinator: 检测网关时使用 arp 而不是 icmp，避免由于路由器禁止 icmp，而导致检查失败，并且 icmp 也需要 arp 来获取目标 mac。
