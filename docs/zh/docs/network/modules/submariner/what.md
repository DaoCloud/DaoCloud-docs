---
hide:
- toc
---

# 什么是 Submariner

随着 Kubernetes 不断的发展, 多集群也逐渐变得流行起来。多集群提高应用的冗余、规模和故障隔离等能力，但多集群连通是一个比较大的问题。
Submariner 是一款开源的多集群网络解决方案，它以一种安全的方式实现了跨集群间 Pod 与 Service 连通性，并且通过 Lighthouse 组件实现
[KMCS](https://github.com/kubernetes/enhancements/tree/master/keps/sig-multicluster/1645-multi-cluster-services-api) 以提供跨集群的服务发现能力。

**架构图**:

![submariner](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner.png)

它包括下面几个 **重要组件** :

- Broker：没有实际的 Pod 和 Service，只提供子集群访问 Broker 集群 API-Server 的凭证。基于此，使子集群之间可以交换 Metadata 信息，用于发现对方。
- Gateway Engine：建立和维护集群间的隧道，打通跨集群的网络通讯。
- Route Agent：在 Gateway 节点和工作节点之间建立 Vxlan 隧道，使工作节点上的跨集群流量先转发到 Gateway 节点，再通过跨集群的隧道从 Gateway 节点发送至对端。
- Service Discover：包括 Lighthouse-agent 和 Lighthouse-dns-server 组件，实现 KMCS API，提供跨集群的服务发现。

**可选组件**：

- Globalnet Controller：支持重叠子网的集群间互连。

**重要 CRD** 列表：

```shell
[root@master1]# kubectl get crd | grep -iE 'submariner|.multicluster'
brokers.submariner.io                                 2023-02-22T13:56:30Z
clusterglobalegressips.submariner.io                  2023-02-22T13:56:37Z
clusters.submariner.io                                2023-02-22T13:56:37Z
endpoints.submariner.io                               2023-02-22T13:56:37Z
gateways.submariner.io                                2023-02-22T13:56:37Z
globalegressips.submariner.io                         2023-02-22T13:56:37Z
globalingressips.submariner.io                        2023-02-22T13:56:37Z
servicediscoveries.submariner.io                      2023-02-22T13:56:30Z
serviceexports.multicluster.x-k8s.io                  2023-02-22T11:32:29Z
serviceimports.multicluster.x-k8s.io                  2023-02-22T11:32:29Z
submariners.submariner.io                             2023-02-22T13:56:30Z
```

- submariners.submariner.io：用于 submariner-operator 组件创建所有 Submariner 组件
- clusters.submariner.io：存储每个子集群的信息，包括其 Pod、Service 的子网信息
- endpoints.submariner.io：每个子集群网关节点的基本信息，包括私有/公有 IP/隧道模式/状态等
- serviceexports.multicluster.x-k8s.io：导出每一个 Service，对应一个 serviceexports 对象，用于服务发现
- serviceimports.multicluster.x-k8s.io：对于每一个 serviceexports 对象，Lighthouse-agent 创建对应的 serviceimports 对象，供其他集群消费
- clusterglobalegressips.submariner.io：全局的 CIDR，用于启用 Globalnet 时解决子集群子网重叠的问题

下一步：

- [安装 Submariner](install.md)
- [使用和 debug](usage.md)
