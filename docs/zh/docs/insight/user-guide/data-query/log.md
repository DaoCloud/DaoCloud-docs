# 日志查询

日志查询支持查询节点、事件、工作负载的日志，可快速在大量日志中查询到所需的日志，同时结合日志的来源信息和上下文原始数据辅助定位问题。

!!! note

    由于性能限制，目前一次最多可展示 10000 条日志，当一段时间内日志量过大时，请缩小查询的时间范围分阶段查询日志。

## 前提条件

集群中已[安装 insight-agent](../../quickstart/install/install-agent.md) 且应用处于`运行中`状态。

## 查询日志

1. 在左侧导航栏中，选择`数据查询` -> `日志查询`。

    ![日志查询](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/log01.png)

2. 选择查询条件后，点击`搜索`，将显示图表形式的日志记录。最新的日志显示在最上面。

3. 在`筛选`面板，切换`类型`，选择`节点`，可查到该集群中所有节点的日志。

    ![日志查询](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/log03.png)

4. 在`筛选`面板，切换`类型`，选择`事件`，可查到该集群中所有的 Kubernetes events 产生的日志。

    ![日志查询](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/log04.png)

## 导出日志

点击列表右上角的`下载`，可下载对应筛选条件下的日志内容，目前支持将日志查询结果导出为 .csv 格式的文件。
出于性能考虑，目前下载的日志上限为 2000 条，当导出日志的数量大于 2000 条时，请修改时间范围进行多次下载。

![日志查询](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/log05.png)

## 查看日志上下文

点击单条日志后的图标，可查看该条日志详细信息和上下文的日志。并支持下载查询的日志上下文的内容，目前支持导出 .csv 格式的文件。

![日志查询](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/log02.png)
