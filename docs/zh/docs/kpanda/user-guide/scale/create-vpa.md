# 创建 VPA

容器垂直扩缩容策略（Vertical Pod Autoscaler, VPA）通过监控 Pod 在一段时间内的资源申请和用量，计算出对该 Pod 而言最适合的 CPU 和内存请求值。使用 VPA 可以更加合理地为集群下每个 Pod 分配资源，提高集群的整体资源利用率，避免集群资源浪费。

DCE 5.0 支持通过容器垂直扩缩容策略（Vertical Pod Autoscaler, VPA），基于此功能可以根据容器资源的使用情况动态调整 Pod 请求值。DCE 5.0 支持通过手动和自动两种方式来修改资源请求值，您可以根据实际需要进行配置。

本文将介绍如何为工作负载配置 Pod 垂直伸缩。

!!! warning

    使用 VPA 修改 Pod 资源请求会触发 Pod 重启。由于 Kubernetes 本身的限制， Pod 重启后可能会被调度到其它节点上。

## 前提条件

为工作负载配置垂直伸缩策略之前，需要满足以下前提条件：

- 在[容器管理](../../intro/index.md)模块中[接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。

- 创建一个[命名空间](../namespaces/createns.md)、[用户](../../../ghippo/user-guide/access-control/user.md)、[无状态工作负载](../workloads/create-deployment.md)或[有状态工作负载](../workloads/create-statefulset.md)。

- 当前操作用户应具有 [NS Edit](../permissions/permission-brief.md#ns-edit) 或更高权限，详情可参考[命名空间授权](../namespaces/createns.md)。

- 当前集群已经安装 [ __metrics-server__ ](install-metrics-server.md) 和 [ __VPA__ ](install-vpa.md) 插件。

## 操作步骤

参考以下步骤，为工作负载配置内置指标弹性伸缩策略。

1. 在 __集群列表__ 中找到目前集群，点击目标集群的名称。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy01.png)

2. 在左侧导航栏点击 __工作负载__ ，找到需要创建 VPA 的负载，点击该负载的名称。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/createScale.png)

3. 点击 __弹性伸缩__ 页签，查看当前集群的弹性伸缩配置，确认已经安装了相关插件并且插件是否运行正常。

    ![垂直伸缩](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/createVpaScale.png)

4. 点击 __新建伸缩__ 按钮，并配置 VPA 垂直伸缩策略参数。

    ![新建伸缩](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/createVpaScale01.png)

    - 策略名称：输入垂直伸缩策略的名称，请注意名称最长 63 个字符，只能包含小写字母、数字及分隔符（“-”），且必须以小写字母或数字开头及结尾，例如 vpa-my-dep。
    - 伸缩模式：执行修改 CPU 和内存请求值的方式，目前垂直伸缩支持手动和自动两种伸缩模式。
        - 手动伸缩：垂直伸缩策略计算出推荐的资源配置值后，需用户手动修改应用的资源配额。
        - 自动伸缩：垂直伸缩策略自动计算和修改应用的资源配额。
    - 目标容器：选择需要进行垂直伸缩的容器。

5. 完成参数配置后，点击 __确定__ 按钮，自动返回弹性伸缩详情页面。点击列表右侧的 __⋮__ ，可以执行编辑、删除操作。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/createVpaScale02.png)
