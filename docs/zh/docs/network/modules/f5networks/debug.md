---
hide:
  - toc
---

# F5network 安装问题汇总

本页介绍安装 F5network 组件时遇到的一些问题及其解决办法。
有关 F5network 组件的安装步骤，请参考[安装](./install.md)文档。

安装常见的一些问题汇总如下。

1. 安装 F5network 组件后 `f5 ipam controller` 服务无法拉起。

    如果本组件使用 4 层负载均衡模式，会安装 `f5 ipam controller`，而 `f5 ipam controller` 要求集群具备 storage 组件且提供 PVC 服务。
    当没有 storage 组件时，会出现这个问题。可参考相关的存储组件安装手册进行安装。

1. Service 中指定了 `cis.f5.com/ipamLabel: LabelName`，但却无法分配到 IP。

    请检查集群中是否有其它 loadbalancer 组件。如果有，会导致 F5 IPAM 组件无法给 Service 分配 IP 地址，请卸载其它 loadbalancer 组件。

1. F5 端没有 Pool Member

    请检查 Service 是否具有 Endpoint。如果没有，将会导致 F5 端没有 Pool Member。

1. F5 流量无法转发到集群节点的 nodePort 上。

    请执行 `kubectl describe pod <f5Name>-f5-bigip-ctlr-<xxx> -n <namespace>`，检查是否设置了 --node-label-selector。
    如果设置了，但是相关 node 却没有对应的 label，会导致 F5 不知道如何转发。
