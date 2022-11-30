---
hide:
  - toc
---

# 什么是 Cilium

Cilium 为基于 Kubernetes 的 Linux 容器管理平台上部署的服务，透明地提供服务间的网络和 API 连接及安全。

Cilium 底层基于 Linux 内核的新技术 eBPF，可以在 Linux 系统中动态注入强大的安全性、可见性和网络控制逻辑。
Cilium 基于 eBPF 提供了多集群路由、替代 kube-proxy 实现负载均衡、透明加密以及网络和服务安全等诸多功能。
除了提供传统的网络安全之外，eBPF 的灵活性还支持应用协议和 DNS 请求/响应安全。
同时，Cilium 与 Envoy 紧密集成，提供了基于 Go 的扩展框架。
因为 eBPF 运行在 Linux 内核中，所以应用所有 Cilium 功能，无需对应用程序代码或容器配置进行任何更改。

基于微服务的应用程序分为小型独立服务，这些服务使用 HTTP、gRPC、Kafka 等轻量级协议通过 API 相互通信。
但是，现有的 Linux 网络安全机制（例如 iptables）仅在网络和传输层（即 IP 地址和端口）上运行，并且缺乏对微服务层的可见性。

Cilium 为 Linux 容器框架（如 Docker 和 Kubernetes）带来了 API 感知网络安全过滤。
使用名为 eBPF 的新 Linux 内核技术，Cilium 提供了一种基于容器 / 容器标识定义和实施网络层和应用层安全策略的简单而有效的方法。

> 注：Cilium 中文意思是 “纤毛 “，它十分细小而又无处不在。
