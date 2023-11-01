---
hide:
- toc
---

# Terway CNI 插件介绍

Terway 是阿里云容器服务团队推出的针对阿里云 VPC 网络的 CNI 插件，稳定、高性能，支持Kubernetes network policy、流控等高级特性。

相关术语:

- ECS 实例: 对应 Kubernetes 的节点
- 弹性网卡（Elastic Network Interfaces，简称 ENI）: 是专有网络 VPC 中的虚拟网络接口，用于连接云服务器 ECS 与 专有网络。
- 辅助IP: 弹性网卡（包括主网卡和辅助弹性网卡）支持分配一个或多个辅助私网IP地址
- 虚拟交换机: ECS使用的交换机，用于节点间网络通信
- Pod 虚拟交换机: Pod 地址从该交换机分配，用于 Pod 网络通信。Terway 网络模式下，Pod 分配的 Pod IP 就是从这个交换机网段内获取。

Terway CNI 主要分为两个组件:

- CNI Binary: 一方面与 Kubernetes CRI-Runtime 和 交互，处理来自 API-Server 管理 Pod 的请求，设置 Pod 的网络协议栈。一方面与自身的 daemon 组件交互，
  调用阿里云 OpenAPI 获取阿里云网络资源, 设置和联通网络。

- Daemon 组件: Daemon 组件由 CNI Binary 调用，负责去调用阿里云 OpenAPI, 由其完成操作阿里云 VPC 网络资源。比如弹性网卡 ENI 的创建与删除，或辅助 IP 的添加与删除等等。

为满足不同用户的需求，Terway 插件支持四种不同的通信模式:

- VPC
- ENI
- ENIIP
- ENI-Trunking

下一步:

- [Terway 网络模式介绍](what.md)
- [使用文档](usage.md)
- [阿里云运行 Calico](aliyun-calico.md)
- [阿里云运行 Cilium](aliyun-cilium.md)
- [Q & A + 总结](Q_A.md)
