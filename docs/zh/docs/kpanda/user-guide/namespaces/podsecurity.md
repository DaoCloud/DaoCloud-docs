# 容器组安全策略

容器组安全策略指在 kubernetes 集群中，通过为指定命名空间配置不同的等级和模式，实现在安全的各个方面控制 Pod 的行为，只有满足一定的条件的 Pod 才会被系统接受。它设置三个等级和三种模式，用户可以根据自己的需求选择更加合适的方案来设置限制策略。

!!! note

    一条安全模式仅能配置一条安全策略。同时请谨慎为命名空间配置 enforce 的安全模式，违反后将会导致 Pod 无法创建。

本节将介绍如何通过容器管理界面为命名空间配置容器组安全策略。

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../clusters/create-cluster.md)，集群的版本需要在 v1.22 以上，且能够访问集群的 UI 界面。

- 已完成一个[命名空间的创建](../namespaces/createns.md)、[用户的创建](../../../ghippo/user-guide/access-control/user.md)，并为用户授予 [NS Admin](../permissions/permission-brief.md#ns-admin) 或更高权限，详情可参考[命名空间授权](../permissions/cluster-ns-auth.md)。

## 为命名空间配置容器组安全策略

1. 选择需要配置容器组安全策略的命名空间，进入详情页。在 __容器组安全策略__ 页面点击 __配置策略__ ，进入配置页。

    ![配置策略列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ps01.png)

2. 在配置页点击 __添加策略__ ，则会出现一条策略，包括安全级别和安全模式，以下是对安全级别和安全策略的详细介绍。

    | 安全级别   | 描述                                                         |
    | ---------- | ------------------------------------------------------------ |
    | Privileged | 不受限制的策略，提供最大可能范围的权限许可。此策略允许已知的特权提升。 |
    | Baseline   | 限制性最弱的策略，禁止已知的策略提升。允许使用默认的（规定最少）Pod 配置。 |
    | Restricted | 限制性非常强的策略，遵循当前的保护 Pod 的最佳实践。          |

    | 安全模式 | 描述                                                         |
    | -------- | ------------------------------------------------------------ |
    | Audit    | 违反指定策略会在审计日志中添加新的审计事件，Pod 可以被创建。 |
    | Warn     | 违反指定策略会返回用户可见的告警信息，Pod 可以被创建。       |
    | Enforce  | 违反指定策略会导致 Pod 无法创建。                            |

    ![添加策略](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ps02.png)

3. 不同的安全级别对应不同的检查项，若您不知道该如何为您的命名空间配置，可以点击页面右上角的 __策略配置项说明__ 查看详细信息。

    ![配置项说明01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ps03.png)

    ![配置项说明01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ps04.png)

4. 点击确定，若创建成功，则页面上将出现您配置的安全策略。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ps05.png)

5. 点击 __操作__ 还可以编辑或者删除您配置的安全策略。

    ![操作](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ps06.png)