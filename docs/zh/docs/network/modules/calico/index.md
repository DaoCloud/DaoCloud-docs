# 什么是 Calico

Calico 创建和管理一个扁平的三层网络（不需要 overlay），每个容器会分配一个可路由的 IP。
由于通信时不需要解包和封包，网络性能损耗小，易于排查，且易于水平扩展。

小规模部署时可以通过 BGP client 直接互联，大规模下可通过指定的 BGP Route Reflector 来完成，这样保证所有的数据流量都是通过 IP 路由的方式完成互联的。

Calico 基于 iptables 提供了丰富而灵活的网络 Policy，保证通过各个节点上的 ACL 来提供 Workload 的多租户隔离、安全组以及其他可达性限制等功能。

!!! info

    Calico 原意为”有斑点的“花猫，也叫三色猫，所以 Calico 的 logo 是一只三色猫。

    ![calico](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/cat.jpeg)

## Calico 组件

Calico 由以下组件组成，在部署 Calico 的时候部分组件是可选的。

- [什么是 Calico](#什么是-calico)
  - [Calico 组件](#calico-组件)
    - [Calico API Server](#calico-api-server)
    - [Felix](#felix)
    - [BIRD](#bird)
    - [confd](#confd)
    - [Dikastes](#dikastes)
    - [CNI](#cni)
    - [数据存储插件](#数据存储插件)
      - [Kubernetes API datastore](#kubernetes-api-datastore)
      - [etcd](#etcd)
    - [IPAM](#ipam)
    - [kube-controller](#kube-controller)
    - [Typha](#typha)
    - [calicoctl](#calicoctl)
    - [云编排器插件](#云编排器插件)

### Calico API Server

可以使用 kubectl 直接管理 Calico。

### Felix

Felix 以 agent 代理的形式在每台机器端点上运行。对路由和 ACL 以及主机进行编程，为该主机上的端点提供所需的连接。

根据具体的编排器环境，Felix 负责：

- 接口管理

    将有关接口的信息编入内核，以便内核能够正确处理来自该端点的流量。
    特别是，确保主机响应来自每个工作负载的 ARP 请求，提供主机的 MAC，并为它所管理的接口启用 IP 转发。
    它还监控接口，以确保编程在适当的时候应用。

- 路由编程

    将其主机上的端点的路由编程到 Linux 内核的 FIB（转发信息库）。
    这可以确保到达主机上的以这些端点为目的地的数据包被相应地转发。

- ACL 编程

    在 Linux 内核中编程 ACL，以确保只有有效的流量可以在端点之间发送，并且端点不能规避 Calico 的安全措施。

- 状态报告

    提供网络健康数据。特别是在配置其主机时报告错误和问题。这些数据被写入数据存储，以便对网络的其他组件和运营商可见。

### BIRD

BGP Internet Routing Daemon，简称 BIRD。从 Felix 获取路由，并分发到网络上的 BGP peer，用于主机间的路由。在每个 Felix 代理的节点上运行。

BGP 客户端负责：

- 路由分配

    当 Felix 将路由插入 Linux 内核的 FIB 时，BGP 客户端将它们分配给部署中的其他节点。这确保了部署中的有效流量路由。

- BGP 路由反射器的配置

    BGP 路由反射器通常是为大型部署而配置的，而不是一个标准的 BGP 客户端。BGP 路由反射器作为连接 BGP 客户端的一个中心点。
    (标准 BGP 要求每个 BGP 客户端在网格拓扑结构中与其他每个 BGP 客户端连接，这很难维护。)

    为了实现冗余，可以无缝部署多个 BGP 路由反射器。BGP 路由反射器只参与网络的控制，没有终端数据通过它们。
    当 Calico BGP 客户端将其 FIB 中的路由通告给路由反射器时，路由反射器将这些路由通告给部署中的其他节点。

### confd

开源的、轻量级的配置管理工具。监控 Calico 数据存储对 BGP 配置和全局默认的日志变更，如 AS 号、日志级别和 IPAM 信息。

confd 根据存储中的数据更新，动态生成 BIRD 配置文件。当配置文件发生变化时，confd 会触发 BIRD 加载新的文件。

### Dikastes

执行 Istio 服务网格的网络策略。作为 Istio Envoy 的一个 Sidecar 代理，在集群上运行。

Dikastes 是可选的。Calico 在 Linux 内核（使用 iptables，在三、四层）和三到七层使用 Envoy 的 Sidecar 代理 Dikastes 为工作负载执行网络策略，对请求进行加密认证。
使用多个执行点建立基于不同标准的远程端点的身份。即使安全威胁绕过 Envoy 代理，影响工作负载 Pod，主机 Linux 内核的执行也能保护工作负载。

### CNI

为 Kubernetes 集群提供 Calico 网络。

将 API 暴露给 Kubernetes 的 Calico 二进制文件为 CNI 插件，该插件必须安装在 Kubernetes 集群的每个节点上。
Calico CNI 插件允许使用符合 CNI 网络规范的编排调度器使用 Calico 网络。

### 数据存储插件

通过减少每个节点对数据存储的影响来扩大规模。

#### Kubernetes API datastore

在 Calico 中使用 Kubernetes API 数据存储（kdd）的优点是：

- 管理简单，不需要额外的数据存储
- 使用 Kubernetes RBAC 来控制对 Calico 资源的访问
- 使用 Kubernetes 审计日志来生成 Calico 资源变化的审计日志

#### etcd

etcd 是一个一致的、高可用的分布式键值存储，为 Calico 网络提供数据存储，并用于组件之间的通信。
etcd 仅支持保护非集群主机（Calico v3.1 及更新版本）。etcd 的优点是：

- 支持在非 Kubernetes 平台上运行 Calico。
- 解耦 Kubernetes 和 Calico 资源，例如允许独立地扩展数据存储。
- 支持 Calico 集群中包含多个 Kubernetes 集群，例如让 Calico 主机保护的裸机服务器与 Kubernetes 集群互通。

### IPAM

使用 Calico 的 IP 池资源将 IP 地址分配给集群中的 Pod。

> 一般情况下，IPAM 为 Calico 的默认安装插件。

### kube-controller

监控 Kubernetes 的 API，并根据集群状态执行行动。

`tigera/kube-controllers` 容器包括以下控制器：

- Policy 控制器
- Namespace 控制器
- ServiceAccount 控制器
- WorkloadEndpoint 控制器
- Node 控制器

### Typha

通过减少每个节点对数据存储的影响来扩大规模。作为数据存储和 Felix 实例之间的一个守护程序运行。Typha 为默认安装的插件，但默认不进行配置。

Typha 代表 Felix 和 confd 等所有客户端维护一个单一的数据存储连接。
可用于缓存数据存储的状态，并复制事件，以便将事件推广到更多的监听器。
一个 Typha 实例支持数百个 Felix 实例，可以大幅降低数据存储的负载。
由于 Typha 可以过滤掉与 Felix 无关的更新，因而减少了 Felix 的 CPU 使用。
在一个大规模（100 多个节点）的 Kubernetes 集群中，这是至关重要的，因为 API 服务器产生的更新数量随着节点数量的增加而增加。

### calicoctl

Calicoctl 命令行作为二进制或容器需要单独安装，支持在任何可以通过网络访问 Calico 数据存储的主机上使用。

### 云编排器插件

将管理网络的编排器 API 转换成 Calico 的数据模型和数据存储。

对于云供应商，Calico 为每个云编排平台提供了一个单独的插件。
这使得用户可以使用各自的编排器来管理 Calico 网络。
当需要时，编排器插件会将 Calico 网络的反馈信息提供给编排器。
例如，提供关于 Felix liveness 的信息，并在网络设置失败时将特定端点标记为失败。
