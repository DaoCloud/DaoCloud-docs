# 双机房部署 Elasticsearch

## 背景

假设 es 按照下面的拓扑结构部署，可能存在一个问题：索引分片的（2 个）副本可能全部落在 zone-1，当 zone-1 发生灾难，则该分片的数据全部丢失。需要利用 es 自身的配置让分片的副本分布在 zone-1 与 zone-2。

## 操作步骤

1. 登录控制台，给集群中位于不同机房的 节点 打 label。假设 work1 work2 在一个机房，work3 在另一个机房：

    ![00](../../elasticsearch/images/es2-01.png)

2. es 的配置主要分为 2 部分，一部分是需要对 es 节点调度进行相应配置；二是需要对 es 的配置文件进行相关配置

### 节点调度配置

- 在 es 的 yaml 中，我们需要配置 2 个 nodeSets（一个 nodeSet 对应一个 statefulset）

    ![00](../../elasticsearch/images/es2-02.png)

- 利用亲和性与反亲和配置，将其中两个 es 节点分布在 zone1，另一个 es 节点分布在 zone2：

    ![00](../../elasticsearch/images/es2-03.png)

### 配置文件配置

将 zone-1 与 zone-2 分为两个 nodeSet 后，就可以对他们的配置文件分开配置，相关的配置有：

- cluster.routing.allocation.awareness.attributes
- node.attr.zone
- cluster.routing.allocation.awareness.force.zone.values

1. 对于 zone-1 的节点配置为：

    ```shell
    node.attr.zone: zone-1
    cluster.routing.allocation.awareness.attributes: zone
    cluster.routing.allocation.awareness.force.zone.values: zone-1,zone-2
    ```

2. 对于 zone-2 的节点配置为：

    ```shell
    node.attr.zone: zone-2
    cluster.routing.allocation.awareness.attributes: zone
    cluster.routing.allocation.awareness.force.zone.values: zone-1,zone-2
    ```
