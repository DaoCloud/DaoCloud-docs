# Metallb

在 Kubernetes 中, 对于 `LoadBancer` 类型，需要使用云提供商的负载均衡器向外部暴露服务，外部负载均衡器可以将流量路由到自动创建的 `NodePort` 服务和 `ClusterIP` 服务上。
所以对于 `LoadBancer` 类型的 Service，必须要有 `Cloud Provider` 加持才能实现。
也就是说在裸机的 K8s 集群无法使用 `LoadBancer` 类型的服务。否则，您会发现 `LoadBancer` 的服务一直处于 Pending 状态。

![`metallb`](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/lbservice.png)

`Metallb` 是一款开源软件，它采用标准的路由协议（ARP 或 BGP）实现了裸机 K8s 集群的负载均衡功能。

## L2 模式 (ARP)

L2 模式下，`Metallb` 会通过 `memberlist` 选举出一个 Leader 节点，此节点负责向本地网络宣告 `LoadBalancerIP`。
从网络的角度来看，这台机器似乎有多个 IP 地址，它会响应来自 `LoadBancerIP` 的 `ARP` 请求。
L2 模式最大的优势是它不需要依赖譬如路由器等硬件的依赖便可工作。

- 优势：通用型，不需要额外的硬件支持
- 缺点：单节点的带宽限制、稍缓慢的故障转移（10s 左右）

## L3 模式 (BGP)

在 BGP 模式下，集群中的每个节点都会与路由器建立 BGP Peer，并使用该会话向集群外部通告集群服务的 `LoadBalanceIP`。
BGP Router 基于每个不同的连接选择一个下一跳（即集群某个节点，这不同于 L2 模式下所有流量先到达某个 Leader 节点）。

- 优势：负载均衡性更好
- 缺点：
  - 当某个节点故障，所有 BGP 会话将会中断
  - Calico BGP 模式无法和 MetaLB L3 模式并存，会存在冲突，详情请参考：https://metallb.universe.tf/configuration/calico/
