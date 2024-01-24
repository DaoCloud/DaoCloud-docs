---
hide:
  - toc
---

# Merbridge

[Merbridge](https://merbridge.io/)：使用 eBPF 加速您的服务网格，就像利用虫洞在网络世界中穿梭

只需要在 Istio 集群执行一条命令，即可直接使用 eBPF 代替 iptables 实现网络加速！

Merbridge 专为服务网格设计，使用 eBPF 代替传统的 iptables 劫持流量，能够让服务网格的流量拦截和转发能力更加高效。

eBPF (extended Berkeley Packet Filter) 技术可以在 Linux 内核中运行用户编写的程序，而且不需要修改内核代码或加载内核模块，目前广泛应用于网络、安全、监控等领域。相比传统的 iptables 流量劫持技术，基于 eBPF 的 Merbridge 可以绕过很多内核模块，缩短边车和服务间的数据路径，从而加速网络。Merbridge 没有对现有的 Istio 作出任何修改，原有的逻辑依然畅通。这意味着，如果您不想继续使用 eBPF，直接删除相关的 DaemonSet 就能恢复为传统的 iptables 方式，不会出现任何问题。

## 特性

Merbridge 的核心特性包括：

- 出口流量处理

    Merbridge 使用 eBPF 的 connect 程序，修改 user_ip 和 user_port 以改变连接发起时的目的地址，从而让流量能够发送到新的接口。为了让 Envoy 识别出原始目的地址，应用程序（包括 Envoy）会在收到连接之后调用 get_sockopts 函数，获取 ORIGINAL_DST。

- 入口流量处理

    入口流量处理与出口流量处理基本类似。需要注意的是，eBPF 是全局性的，不能在指定的命名空间生效。因此，如果对原本不是由 Istio 管理的 Pod 或者对外部的 IP 地址执行此操作，就会导致请求无法建立连接。为了解决此问题，Merbridge 设计了一个小的控制平面（以 DaemonSet 方式部署），通过 Watch 所有的 Pod，用类似于 kubelet 的方式获取当前节点的 Pod 列表，然后将已经注入 Sidecar 的 Pod IP 地址写入 local_pod_ips map。如果流量的目的地址不在该列表中，Merbridge 就不做处理，转而使用原来的逻辑。这样就可以灵活且便捷地处理入口流量。

- 同节点加速

    在 Istio 中，Envoy 使用当前 PodIP 加服务端口来访问应用程序。由于 PodIP 肯定也存在于 local_pod_ips ，所以请求就会被转发到 PodIP + 15006 端口。这样会造成无限递归，不能在 eBPF 获取当前命名空间的 IP 地址信息。因此，需要一套反馈机制：在 Envoy 尝试建立连接时仍然重定向到 15006 端口，在 sockops 阶段判断源 IP 和目的 IP 是否一致。如果一致，说明发送了错误的请求，需要在 sockops 丢弃该连接，并将当前的 ProcessID 和 IP 地址信息写入 process_ip map，让 eBPF 支持进程和 IP 的对应关系。下次发送请求时直接从 process_ip 表检查目的地址是否与当前 IP 地址一致。Envoy 会在请求失败时重试，且这个错误只会发生一次，后续的连接会非常快。

[了解 Merbridge 社区](https://github.com/merbridge/merbridge){ .md-button }

[查阅 Merbridge 官网](https://merbridge.io/){ .md-button }

![cncf logo](./images/cncf.png)

<p align="center">
Merbridge 已入选 <a href="https://landscape.cncf.io/?selected=merbridge">CNCF 云原生全景图</a>。
</p>
