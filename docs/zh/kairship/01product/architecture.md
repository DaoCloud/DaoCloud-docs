# 产品架构

## 整体架构

![整体架构](../images/arch_summary.png)

`Kairship` 管理面主要负责以下功能:

* 多云实例（基于 Karmada）的 LCM
* 作为多云产品统一的流量入口（OpenAPI、Kairship UI、内部模块 GRPC 调用）
* 代理多云实例的 API 请求（Karmada 原生风格）
* 多云实例内的集群信息（监控、管理、控制）等的聚合
* 多云工作负载等资源的管理和监控
* 后续可能的权限操作

## 核心组件

`Kairship` 主要包括两个核心组件:

* Kairship apiserver

    Kairship 数据流入口，所有 API 的入口（protobuf 优先，通过 proto 定义所有的 API 接口，并以此生成对应的前后端代码，使用 grpw-gateway 实现同时支持 http restful 和 grpc）。

* Kairship controller-manager

    Kairship 控制器，主要负责一些实例状态同步、资源搜集、Karmada 实例注册、全局资源注册等。

!!! note
    
    目前 Kairship 鉴权功能 只鉴权 Karmada 实例的权限。Kairship apiserver 校验来自阿猫的接口是否有权限操作、访问 Karmada 实例。

### Kairship apiserver

Kairship apiserver 主要担负着 `Kairship` 所有流量的入口（openapi、grpc 等），启动的时候会从 Ghippo 获取操作人的身份信息，用于后续AuthZ的安全性校验。

无状态服务，具体接口待补充（目前比较简单）

### Kairship controller-manager

!!! note

    多副本部署，通过 leader 机制选举，保持同一个时刻只有一个工作的 Pod（参考 Kubernetes 的 controller-manager 选举机制）。

该组件主要负责 `Kairship` 一系列控制逻辑的处理（每个逻辑单独成 controller），通过 list-watch 机制监听特定对象的变更，然后处理对应事件。主要包括:

* virtual-cluster-sync-controller

    Kairship 实例 CRD 的 CRUD 事件监听，一旦创建 kariship 实例，则同步创建对应的 Kpanda cluster（virtual 类型，Kpanda 界面无须展示）。
    Kairship 实例所有资源的检索（多云工作负载、pp、op）都将通过 Kpanda 内部的加速机制完成（by clusterpedia），实现读写分离，进而提高性能。
    实例删除，则同步删除注册在 Kpanda 中的 virtual cluster。

* resource statistics controller

    主要搜集 Kairship 实例中加入的所有 cluster 的统计信息，并将其回写到 Kairship 实例 crd 中（例如该实例所管理的集群中总共包含多少CPU、内存、节点数）。

* status sync controller

    Kairship 实例本身的状态同步、统计。

* instance registry controller

    `Kairship` 需要注册平台内所有 `Karmada` 实例到 Ghippo（通过 CRD）。
    完成权限资源的注册，这样才能在 Ghippo 中完成人与 Karmada 实例的绑定关系。
    最终这些绑定关系会同步回 Kairship。

* Ghippo webhook controller

    Ghippo 完成人与 Karmada 实例的绑定关系之后会通过 sdk 通知到 Kairship，Kairship 据此完成鉴权动作。

上图 `Kairship` management 中有一个 instance proxy 的组件（内部组件），主要负责 `Kairship` 管理面同各个 `Karmada` 实例间的通信。
可以理解成是一个Kubernetes clients 的集合，根据 Cluster Name 获取对应的 client，然后访问真正的 Karmada 实例。

## 数据流图

!!! note

    多云实例之间互不感知、相互隔离。

Kairship 管理面需要操作每个 Kairship instance，主要分为以下几种场景：

* 获取 Karmada 相关的分发策略以及应用的状态信息。
* 获取 Kairship 实例内的集群、节点的统计、监控信息。
* 编辑、更新、删除相关 Karmada 实例中的多云应用相关的信息（主要围绕 Karmada 工作负载 和 pp、op 两个 CRD）。

所有的请求数据流都直接传递到位于 global 集群的 Kairship 实例中。这样在大规模请求的时候，性能可能会受影响，如图所示:

![数据流图](../images/arch_kairship_instance.png)

如上图所示，所有访问多云模块的请求经过 Kairship 之后将会被分流，所有 get/list 之类的读请求将会访问 Kpanda，写请求会访问 Karmada 实例。那么问题来了？

通过 Kairship 创建一个多云应用之后，通过 Kpanda 怎么能获取的相关资源信息?

了解 Karmada 的小伙伴都知道，Karmada control-plane 其本质也就是一个完整 KKubernetes 控制面，只是没有任何承载 workload 的节点。
因此 Kairship 在创建 Kairship 实例的时候，采用了一个取巧的动作，会把实例本身作为一个隐藏的 cluster 加入到 Kpanda 中（不在容器管理中显示）。
这样就可以完全借助 Kpanda 的能力（搜集加速检索各个 K8s 集群的资源、CRD 等），当在界面中查询某个 Kairship 实例的资源（deployment、pp、op 等）就可以直接通过 Kpanda 进行检索，做到读写分离，加快响应时间。

## Kairship 实例 LCM

### 部署拓扑

![部署拓扑](../images/deploy_topology.png)

如图所示，整个 Kairship 有三个组件组成，Kairship apiserver、Kairship controller manager，Karmada operator 都部署在 global cluster 集群。
其中 Karmada operator 完全 follow 开源社区的部署架构；Kairship apiserver 无状态服务支持水平扩展；Kairship controller manager 高可用架构，内部有选举机制，同时刻单一 Pod 工作。

### 集群导入

![集群导入](../images/cluster_sync.png)

如图所示，Karmada 实例中纳管的所有 K8s 集群都来自于 `Kpanda` 集群，Karmada 实例加入某个集群之后，会自动进行 CR 的同步工作（Kpanda Cluster --> Karmada Cluster）。
同时 Kairship 管理面有控制循环逻辑会实时监听 Kpanda Cluster 变更，第一时间同步到控制面，进一步反馈到对应 `Karmada` 实例的 Karmada Cluster 中，目前主要监听 Kpanda cluster 访问凭证的变更。

### Karmada 实例 CR

Karmada 社区最近在做 Karmada operator，此处我们不做单独的设计，follow 社区最新进展即可。
因此此文没有对 `Karmada` 示例的 LCM 做设计，假设现阶段社区的Operator 仍不完善，我们可以先进行 CR 转换的对接。
