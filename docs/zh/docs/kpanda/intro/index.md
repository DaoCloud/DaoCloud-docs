---
hide:
  - toc
---

# 容器管理

容器管理是基于 Kubernetes 构建的面向云原生应用的容器化管理模块。它是 DCE 5.0 的核心，
基于原生多集群架构，解耦底层基础设施，实现多云与多集群统一化管理，大幅简化企业的应用上云流程，
有效降低运维管理和人力成本。通过容器管理，您可以便捷创建 Kubernetes 集群，快速搭建企业级的容器云管理平台。

!!! tip

    容器化是数据中心发展的不可或缺的趋势，它是应用封装、部署和托管的自然延伸。

<div class="grid cards" markdown>

- :material-server:{ .lg .middle } __集群管理__

    ---

    DCE 5.0 容器管理目前支持四种集群：全局服务集群、管理集群、工作集群、接入集群。

    - [创建集群](../user-guide/clusters/create-cluster.md)或[接入集群](../user-guide/clusters/integrate-cluster.md)
    - [升级集群](../user-guide/clusters/upgrade-cluster.md)
    - [集群角色](../user-guide/clusters/cluster-role.md)和[集群状态](../user-guide/clusters/cluster-status.md)
    - [选择运行时](../user-guide/clusters/runtime.md)

- :fontawesome-brands-node:{ .lg .middle } __节点管理__

    ---

    节点上运行了 kubelet、容器运行时以及 kube-proxy 等组件。

    - [节点调度](../user-guide/nodes/schedule.md)
    - [标签与注解](../user-guide/nodes/labels-annotations.md)，[污点管理](../user-guide/nodes/taints.md)
    - 节点[扩容](../user-guide/nodes/add-node.md)/[缩容](../user-guide/nodes/delete-node.md)
    - [节点认证](../user-guide/nodes/node-authentication.md)、[节点可用性检查](../user-guide/nodes/node-check.md)

</div>

<div class="grid cards" markdown>

- :simple-myspace:{ .lg .middle } __命名空间__

    ---

    命名空间是构建虚拟空间隔离物理资源的一种方式，仅作用于带有命名空间的对象。

    - [创建/删除命名空间](../user-guide/namespaces/createns.md)
    - [命名空间独享节点](../user-guide/namespaces/exclusive.md)
    - [为命名空间配置 Pod 安全策略](../user-guide/namespaces/podsecurity.md)

- :octicons-tasklist-16:{ .lg .middle } __工作负载__

    ---

    工作负载是在 DCE 5.0 上所运行的各类应用程序。

    - 创建 [Deployment](../user-guide/workloads/create-deployment.md) 和 [StatefulSet](../user-guide/workloads/create-statefulset.md)
    - 创建 [DaemonSet](../user-guide/workloads/create-daemonset.md)
    - 创建 [Job](../user-guide/workloads/create-job.md) 和 [CronJob](../user-guide/workloads/create-cronjob.md)

</div>

<div class="grid cards" markdown>

- :material-expand-all:{ .lg .middle } __弹性伸缩__

    ---

    通过配置 HPA、VPA 策略实现工作负载的弹性伸缩。

    - 安装 [metrics-server](../user-guide/scale/install-metrics-server.md)、[kubernetes-cronhpa-controller](../user-guide/scale/install-cronhpa.md) 和 [VPA](../user-guide/scale/install-vpa.md) 插件
    - [创建 HPA 策略](../user-guide/scale/create-hpa.md)
    - [创建 VPA 策略](../user-guide/scale/create-vpa.md)

- :simple-helm:{ .lg .middle } __Helm 应用__

    ---

    Helm 是 DCE 5.0 的包管理工具，提供了数百个 Helm 模板，方便用户快速部署应用。

    - [Helm 模板](../user-guide/helm/README.md)
    - [Helm 应用](../user-guide/helm/helm-app.md)
    - [Helm 仓库](../user-guide/helm/helm-repo.md)

</div>

<div class="grid cards" markdown>

- :material-dot-net:{ .lg .middle } __容器网络__

    ---

    DCE 5.0 自带的容器网络便于对外提供服务，通过 Ingress 定义路由规则，根据网络策略控制流量。

    - [服务 Service](../user-guide/network/create-services.md)：ClusterIP、NodePort、LoadBalancer
    - [路由 Ingress](../user-guide/network/create-ingress.md)
    - [网络策略 NetworkPolicy](../user-guide/network/network-policy.md)

- :material-harddisk:{ .lg .middle } __容器存储__

    ---

    DCE 5.0 容器管理奉行 Kubernetes 的容器化存储理念，支持原生 CSI，能够制备动态卷、卷快照、克隆等。

    - [数据卷声明 PVC](../user-guide/storage/pvc.md)
    - [数据卷 Volume](../user-guide/storage/pv.md)
    - [存储池 StorageClass](../user-guide/storage/sc.md)

</div>

<div class="grid cards" markdown>

- :material-security:{ .lg .middle } __安全管理__

    ---

    DCE 5.0 容器管理支持对节点、集群执行三种扫描：

    - [合规性扫描](../user-guide/security/cis/config.md)
    - [权限扫描](../user-guide/security/audit.md)
    - [漏洞扫描](../user-guide/security/hunter.md)

- :material-key:{ .lg .middle } __配置与密钥__

    ---

    DCE 5.0 容器管理支持以键值对的形式管理 ConfigMap 和 Secret：

    - [配置项 ConfigMap](../user-guide/configmaps-secrets/create-configmap.md)
    - [密钥 Secret](../user-guide/configmaps-secrets/create-secret.md)

</div>

<div class="grid cards" markdown>

- :material-card-search:{ .lg .middle } __集群巡检__

    ---

    集群巡检可以自动/手动定期或随时检查集群的整体健康状态，让管理员获得保障集群安全的主动权。

    - [创建巡检配置](../user-guide/inspect/config.md)
    - [执行巡检](../user-guide/inspect/inspect.md)
    - [查看巡检模块](../user-guide/inspect/report.md)

- :material-auto-fix:{ .lg .middle } __集群运维__
    
    ---

    集群运维指的是查看集群的操作、升级集群以及集群配置等。

    - [查看最近操作记录](../user-guide/clusterops/latest-operations.md)
    - [集群设置](../user-guide/clusterops/cluster-settings.md)
    - [集群升级](../user-guide/clusters/upgrade-cluster.md)

</div>

!!! success

    通过容器化，您可以更快速、简单地开发和部署应用程序，比构建虚拟设备更加高效。
    容器化架构带来了令人瞩目的运维和经济效益，包括更低的许可成本、更高的物理资源利用率、更好的可扩展性以及更高的服务可靠性。

    展望未来，容器虚拟化将帮助企业更好地利用混合云和多云环境，实现更优化的资源管理和应用部署。

**DCE 5.0 容器管理的逻辑架构**

![逻辑架构图](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/kpanda_architect.png)

[下载 DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../../dce/license0.md){ .md-button .md-button--primary }
