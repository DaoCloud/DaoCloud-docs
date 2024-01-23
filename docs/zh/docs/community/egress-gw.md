# egressgateway

![background](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/community/images/egress01.png)

从 2021 年开始，我们收到了以下反馈。

假设你有两个集群 A 和 B。集群 A 基于 VMWare，主要运行数据库工作负载，而集群 B 是一个 Kubernetes 集群。
集群 B 中的一些应用程序需要访问集群 A 中的数据库，网络管理员希望通过 Egress 网关来管理集群 Pod。

## 概述

该网关为 Kubernetes 集群提供网络 Egress 功能。

### 特点

- 解决 IPv4 IPv6 双栈连接问题
- 解决 Egress 节点的高可用性
- 允许过滤 Pods Egress 策略（_Destination CIDR_）
- 允许过滤 Egress 应用程序（_Pods_）
- 可在低内核版本中使用
- 支持多个 Egress 网关实例
- 支持命名空间 Egress IP
- 支持对 Egress 网关策略进行自动检测以获取集群流量
- 支持命名空间默认 Egress 实例

### 兼容性

- Calico

### CRD

定义了一下 CRD：

- EgressNode
- EgressGateway
- EgressPolicy
- EgressClusterPolicy
- EgressEndpointSlice
- EgressClusterEndpointSlice
- EgressClusterInfo

你可以参考[入门指南](https://spidernet-io.github.io/egressgateway/usage/install)来搭建你的测试环境。

## 开发

![develop](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/community/images/egress02.png)

请参阅[开发指南](https://github.com/spidernet-io/egressgateway/blob/main/docs/develop/dev.md).

## 许可证

EgressGateway 在 Apache 许可证第 2 版下获得许可。有关完整的许可证文本，
请参见 [LICENSE](https://github.com/spidernet-io/spiderpool/blob/main/LICENSE)。

[了解 egressgateway 社区](https://github.com/spidernet-io/egressgateway){ .md-button }
