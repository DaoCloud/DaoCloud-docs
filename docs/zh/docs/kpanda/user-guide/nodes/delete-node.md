# 集群节点缩容

当业务高峰期结束之后，为了节省资源成本，可以缩小集群规模，卸载冗余的节点，即节点缩容。节点卸载后，应用无法继续运行在该节点上。

## 前提条件

- 当前操作用户具有 [Cluster Admin](../permissions/permission-brief.md) 角色授权 。
- 只有通过容器管理模块[创建的集群](../clusters/create-cluster.md)才支持节点扩缩容，从外部接入的集群不支持此操作。
- 卸载节点之前，需要[暂停调度该节点](schedule.md)，并且将该节点上的应用都驱逐至其他节点。
- 驱逐方式：登录控制器节点，通过 kubectl drain 命令驱逐节点上所有 Pod。安全驱逐的方式可以允许容器组里面的容器优雅地中止。

## 注意事项

1. 集群节点缩容时，只能逐个进行卸载，无法批量卸载。

2. 如需卸载集群控制器节点，需要确保最终控制器节点数为 **奇数**。

3. 集群节点缩容时不可下线 **第一个控制器** 节点。如果必须执行此操作，请联系售后工程师。

## 操作步骤

1. 在 __集群列表__ 页面点击目标集群的名称。

    若 __集群角色__ 中带有 __接入集群__ 的标签，则说明该集群不支持节点扩缩容。

    ![进入集群列表页面](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/addnode01.png)

2. 在左侧导航栏点击 __节点管理__ ，找到需要卸载的节点，点击 __ⵗ__ 选择 __移除节点__ 。

    ![移除节点](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deletenode01.png)

3. 输入节点名称,并点击 __删除__ 进行确认。

    ![移除节点](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deletenode02.png)
