# 应用备份

本文介绍如何在 DCE 5.0 中为应用做备份，本教程中使用的演示应用名为 __dao-2048__ ，属于无状态工作负载。

## 前提条件

在对无状态工作负载进行备份前，需要满足以下前提条件：

- 在[容器管理](../../intro/index.md)模块中[接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。

- 创建一个[命名空间](../namespaces/createns.md)和[用户](../../../ghippo/user-guide/access-control/user.md)。

- 当前操作用户应具有 [NS Edit](../permissions/permission-brief.md#ns-edit) 或更高权限，详情可参考[命名空间授权](../namespaces/createns.md)。

- [安装 velero 组件](install-velero.md)，且 velero 组件运行正常。

- [创建一个无状态工作负载](../workloads/create-deployment.md)（本教程中的负载名为 __dao-2048__ ），并为无状态工作负载打上 __app: dao-2048__ 的标签。

## 备份工作负载

参考以下步骤，备份无状态工作负载 __dao-2048__ 。

1. 进入容器管理模块，点击左侧导航栏上的 __备份恢复__ -> __应用备份__ ，进入 __应用备份__ 列表页面。

    ![集群列表](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/backupd20481.png)

2. 在 __应用备份__ 列表页面，选择已经安装了 velero 和 __dao-2048__ 应用的集群。点击右上角的 __备份计划__ ，新建一个备份集群。

    ![应用备份](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/backupd20482.png)

3. 参考下方说明填写备份配置。

    - 名称：新建备份计划的名称。
    - 源集群：计划执行应用备份的集群。
    - 对象存储位置：在源集群安装 velero 时配置的对象存储的访问路径。
    - 命名空间：需要进行备份的命名空间，支持多选。
    - 高级配置：根据资源标签对命名空间内的特定资源进行备份如某个应用，或者备份时根据资源标签对命名空间内的特定资源不进行备份。

        ![操作菜单](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/backupd20483.png)

4. 参考下方说明设置备份执行频率，然后点击 __下一步__ 。

    - 备份频率：基于分钟、小时、天、周、月设置任务执行的时间周期。支持用数字和 `*` 自定义 Cron 表达式，**输入表达式后下方会提示当前表达式的含义**。有关详细的表达式语法规则，可参考 [Cron 时间表语法](https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax)。
    - 留存时长（天）：设置备份资源保存的时间，默认为 30 天，过期后将会被删除。
    - 备份数据卷（PV）：是否备份数据卷（PV）中的数据，支持直接复制和使用 CSI 快照两种方式。
        - 直接复制：直接复制数据卷（PV）中的数据用于备份；
        - 使用 CSI 快照：使用 CSI 快照来备份数据卷（PV）。需要集群中有可用于备份的 CSI 快照类型。

            ![操作菜单](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/backupd20484.png)

5. 点击 __确定__ ，页面会自动返回应用备份计划列表，找到新建的 __dao-2048__ 备份计划，执行 __立即备份__ 操作。

    ![操作菜单](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/backupd20485.png)

6. 此时集群的 __上一次执行状态__ 将转变为 __备份中__ 。等待备份完成后可以点击备份计划的名称，查看备份计划详情。

    ![操作菜单](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/backupd20486.png)
