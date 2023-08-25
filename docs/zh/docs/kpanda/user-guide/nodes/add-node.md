---
hide:
  - toc
---

# 集群节点扩容

随着业务应用不断增长，集群资源日趋紧张，这时可以基于 kubean 对集群节点进行扩容。扩容后，应用可以运行在新增的节点上，缓解资源压力。

只有通过容器管理模块[创建的集群](../clusters/create-cluster.md)才支持节点扩缩容，从外部接入的集群不支持此操作。本文主要介绍同种架构下工作集群的 **工作节点** 扩容，如需为集群增加控制节点或异构工作节点，请参阅：[对工作集群的控制节点扩容](../../best-practice/add-master-node.md)、[为工作集群添加异构节点](../../best-practice/multi-arch.md)、[为全局服务集群的工作节点扩容](../../best-practice/add-worker-node-on-global.md)。

1. 在`集群列表`页面点击目标集群的名称。

    若`集群角色`中带有`接入集群`的标签，则说明该集群不支持节点扩缩容。

    ![进入集群列表页面](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/addnode01.png)

2. 在左侧导航栏点击`节点管理`，然后在页面右上角点击`接入节点`。

    ![节点管理](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/addnode02.png)

3. 输入主机名称和节点 IP 并点击`确定`。

    点击 `➕ 添加工作节点`可以继续接入更多节点。

    ![节点管理](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/addnode03.png)

!!! note

    接入节点大约需要 20 分钟，请您耐心等待。
