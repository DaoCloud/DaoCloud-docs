---
hide:
- toc
---

# Terway CNI 插件介绍

Terway 是阿里云容器服务团队推出的针对阿里云 VPC 网络的 CNI 插件，稳定、高性能，支持Kubernetes network policy、流控等高级特性。Terway CNI 主要
分为两个组件:

* CNI Binary: 一方面与 Kubernetes CRI-Runtime 和 交互，处理来自 API-Server 管理 Pod 的请求，设置 Pod 的网络协议栈。一方面与自身的 daemon 组件交互，
  调用阿里云 Openapi 获取阿里云网络资源, 设置和联通网络。

* Daemon 组件: Daemon 组件由 CNI Binary 调用，负责去调用阿里云 Openapi, 由其完成操作阿里云 VPC 网络资源。比如弹性网卡ENI的创建与删除，或辅助IP的添加与删除等等。

为满足不同用户的需求，Terway 插件支持四种不同的通信模式:

* VPC
* ENI
* ENIIP
* ENI-Trunking

下一步:

- [Terway 网络模式介绍](what.md)
- [使用文档](usage.md)
- [Q & A + 总结](Q_A.md)