# 集群监控

集群监控可查看集群的基本信息，该集群中的资源消耗以及一段时间的资源消耗变化趋势。

## 前提条件

集群中已[安装 insight-agent](../../quickstart/install/install-agent.md) 且应用处于`运行中`状态。

## 查看集群详情

1. 在左侧导航栏选择 `场景监控 -> 集群监控`，默认展示选中的第一个集群的信息。

    ![容器监控](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/cluster01.png)

2. 在集群列表中选择目标集群，可查看该集群的详细信息。

    ![容器监控](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/cluster02.png)

    - CPU 使用率：该指标是指集群中所有 Pod 资源的实际 CPU 用量与所有节点的 CPU 总量的比率。
    - CPU 分配率：该指标是指集群中所有 Pod 的 CPU 请求量的总和与所有节点的 CPU 总量的比率。
    - 内存使用率：该指标是指集群中所有 Pod 资源的实际内存用量与所有节点的内存总量的比率。
    - 内存分配率：该指标是指集群中所有 Pod 的内存请求量的总和与所有节点的内存总量的比率。
