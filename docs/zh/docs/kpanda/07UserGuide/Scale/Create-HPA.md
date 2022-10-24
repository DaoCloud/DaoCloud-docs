# 指标弹性伸缩（HPA）

DaoCloud Enterprise 5.0 支持 Pod 资源基于指标进行弹性伸缩（Horizontal Pod Autoscaling, HPA）。
用户可以通过设置 CPU 利用率、内存用量两项指标来动态调整 Pod 资源的副本数量。
例如，为工作负载设置指标弹性伸缩后，当 Pod 的 CPU 利用率超过/低于您设置的指标阀值，工作负载控制器将会自动减少/增加 Pod 副本数。

本文将介绍如何为工作负载配置基于指标的弹性伸缩。

!!! note

    1. HPA 仅适用于 Deployment 和 StatefulSet，每个工作负载只能创建一个 HPA。
    2. 如果基于 CPU 利用率创建 HPA 策略，必须事先限制工作负载能使用的 CPU 最大配额，否则无法计算 CPU 利用率。
    3. 如果同时使用 CPU 和内存指标，HPA 策略会根据两项指标分别计算目标副本数，取较大值（但不得超过设置 HPA 策略时配置的最大副本数）。

## 前提条件

在为工作负载配置指标弹性伸缩策略之前，需要满足以下前提条件：

- 容器管理平台[已接入 Kubernetes 集群](../Clusters/JoinACluster.md)或者[已创建 Kubernetes 集群](../Clusters/CreateCluster.md)，且能够访问集群的 UI 界面。

- 已完成一个[命名空间的创建](../Namespaces/createns.md)、[无状态工作负载的创建](../Workloads/CreateDeploymentByImage.md)或[有状态工作负载的创建](../Workloads/CreateStatefulSetByImage.md)。

- 当前操作用户应具有 [`NS Edit`](../Permissions/PermissionBrief.md#ns-edit) 或更高权限，详情可参考[命名空间授权](../Namespaces/createns.md)。

- 已完成[`metrics-server 插件安装`](Install-metrics-server.md)。

## 操作步骤

参考以下步骤，为工作负载配置指标弹性伸缩策略。

1. 点击左侧导航栏上的`集群列表`进入集群列表页面。点击一个集群名称，进入`集群详情`页面。

    ![集群详情](../../images/deploy01.png)

2. 在集群详情页面，点击左侧导航栏的`工作负载`进入工作负载列表后，点击一个负载名称，进入`工作负载详情`页面。

    ![工作负载](../../images/createScale.png)

3. 点击`弹性伸缩`页签，查看当前集群的弹性伸缩配置情况。

    ![弹性伸缩](../../images/createScale02.png)

4. 确认集群已[安装了 `metrics-server` 插件](Install-metrics-server.md)，且插件运行状态为正常后，即可点击`新建伸缩`按钮。

    ![新建伸缩](../../images/createScale07.png)

5. 配置弹性伸缩的参数。

    ![工作负载](../../images/createScale08.png)

    - 策略名称：输入弹性伸缩策略的名称，请注意名称最长 63 个字符，只能包含小写字母、数字及分隔符（“-”），且必须以小写字母或数字开头及结尾，例如 hpa-my-dep。
    - 命名空间：负载所在的命名空间。
    - 工作负载：执行弹性伸缩的工作负载对象。
    - 目标 CPU 利用率：工作负载资源下 Pod 的 CPU 使用率。计算方式为：工作负载下所有的 Pod 资源 / 工作负载的请求（request）值。当实际 CPU 用量大于/小于目标值时，系统自动减少/增加 Pod 副本数量。
    - 目标内存用量：工作负载资源下的 Pod 的内存用量。当实际内存用量大于/小于目标值时，系统自动减少/增加 Pod 副本数量。
    - 副本范围：Pod 副本数的弹性伸缩范围。默认区间为为 1 - 10。

6. 完成参数配置后，点击`确定`按钮，自动返回弹性伸缩详情页面。点击列表右侧的 `⋮`，可以执行编辑、删除操作，还可以查看相关事件。

    ![工作负载](../../images/createScale09.png)
