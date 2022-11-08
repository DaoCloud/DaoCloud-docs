# DEBUG

本章节介绍安装 F5network 组件遇到的一些问题

## 安装

安装 F5network 组件 请参考文档 [安装](https://docs.daocloud.io/network/modules/f5networks/install/)

## QA

### 安装 F5network 组件后 `f5 ipam controller` 服务无法拉起。
如果本组件使用 4 层负载均衡模式，会安装 `f5 ipam controller` ，而 `f5 ipam controller` 要求集群具备 storage 组件提供 PVC 服务，当没有 storage 组件时，会出现上述问题，可参考相关的存储组件安装手册进行安装。

### service 中指定了` cis.f5.com/ipamLabel: LabelName`，但却无法分配到IP
请检查集群中是否有其它 loadbalancer 组件，如果有，会导致 F5 ipam 组件给 service 分不上 IP 地址，请卸载其它 loadbalancer 组件。

### F5端 没有pool Members
请检查 service 是否具有endpoint，如果没有，将会导致 F5端没有pool Members。

### F5 流量无法转发到集群节点的 nodePort 上。
请执行 `kubectl describe pod <f5Name>-f5-bigip-ctlr-<xxx> -n <namespace>`，检查是否设置了 --node-label-selector，如果设置了，但是相关 node 却没有对应的label，会导致F5不知道如何转发。
