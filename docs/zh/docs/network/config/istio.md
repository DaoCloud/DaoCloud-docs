# Istio 服务网格适配（Underlay）

当 Istio 与 Spiderpool 的 Underlay 网络一起使用时，可能出现 sidecar 无法劫持流量的问题。本页介绍推荐的适配配置。

## 问题背景

Underlay Pod 的流量通过 veth0 转发，Istio 使用 iptables 规则劫持流量，但 veth0 如果没有 IP 地址，数据包可能被内核丢弃。Spiderpool 提供 `vethLinkAddress` 为 veth0 配置一个 link-local 地址，以解决该问题。

## 配置方式

### 方式一：集群级开启（推荐）

在安装 Spiderpool 时设置：

- `coordinator.vethLinkAddress=169.254.100.1`

安装入口参考 [安装 Spiderpool](../modules/spiderpool/install/install.md)。

### 方式二：运行中修改

通过修改默认 SpiderCoordinator 生效：

```shell
kubectl patch spidercoordinators default --type='merge' -p '{"spec": {"vethLinkAddress": "169.254.100.1"}}'
```

### 方式三：仅针对特定网卡

为单个 Multus 配置开启：

```yaml
spec:
  coordinator:
    vethLinkAddress: 169.254.100.1
```

## 验证

在 Pod 内查看 veth0：

```shell
kubectl exec -it <pod-name> -n <namespace> -- ip addr show veth0
```

确认 veth0 具备配置的 link-local 地址。

## 注意事项

- `vethLinkAddress` 必须是合法的 IP 地址
- 建议全局统一配置，避免不同网卡行为不一致
