---
date: 2022-11-17
hide:
  - toc
---

# 集群升级

Kubernetes 社区每个季度都会发布一次小版本，每个版本的维护周期大概只有 9 个月。版本停止维护后就不会再更新一些重大漏洞或安全漏洞。手动升级集群操作较为繁琐，给管理人员带来了极大的工作负担。

本节将介绍如何在通过 Web UI 界面一键式在线升级工作集群 Kubernetes 版本，如需离线升级工作集群的 kubernetes 版本，请参阅[工作集群离线升级指南](../../best-practice/update-offline-cluster.md)进行升级。

!!! danger

    版本升级后将无法回退到之前的版本，请谨慎操作。

!!! note

    - Kubernetes 版本以 `x.y.z` 表示，其中 `x` 是主要版本，`y` 是次要版本，`z` 是补丁版本。
    - 不允许跨次要版本对集群进行升级，例如不能从 1.23 直接升级到 1.25。
    - **接入集群不支持版本升级。如果左侧导航栏没有`集群升级`，请查看该集群是否为接入集群。**
    - 全局服务集群只能通过终端进行升级。
    - 升级工作集群时，该工作集群的[管理集群](cluster-role.md#_3)应该已经接入容器管理模块，并且处于正常运行中。
    - 如果需要修改集群参数，可以通过升级相同版本的方式实现，具体操作参考下文。

1. 在集群列表中点击目标集群的名称。

    ![升级集群](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/upgradeclsuter00.png)

2. 然后在左侧导航栏点击`集群运维`->`集群升级`，在页面右上角点击`版本升级`。

    ![升级集群](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/upgradecluster01.png)

3. 选择可升级的版本，输入集群名称进行确认。

      ![可升级版本](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/upgradecluster02.png)

    !!! note

        如果您是想通过升级方式来修改集群参数，请参考以下步骤：

        1. 找到集群对应的 configmap，您可以登录控制节点执行如下命令，找到 varsConfRef 中的 configmap name。

            ```shell
            kubectl get cluster.kubean.io <clustername> -o yaml
            ```
        2. 根据需要，修改 configmap 中的参数信息。

        3. 在此处选择相同版本进行升级操作，升级完成即可成功更新对应的集群参数。

4. 点击`确定`后，可以看到集群的升级进度。

      ![升级进度](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/upgradecluster03.png)

5. 集群升级预计需要 30 分钟，可以点击`实时日志`按钮查看集群升级的详细日志。

    ![实时日志](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/createcluster07.png)
