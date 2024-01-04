# 指标查询

指标查询支持查询容器各资源的指标数据，可查看监控指标的趋势变化。同时，高级查询支持原生 PromQL 语句进行指标查询。

## 前提条件

- 集群中已[安装 insight-agent](../../quickstart/install/install-agent.md) 且应用处于 __运行中__ 状态。

## 操作步骤

1. 点击一级导航栏进入 __可观测性__ 。

2. 左侧导航栏中，选择 __指标__ 。

3. 选择集群、类型、节点、指标名称查询条件后，点击 __搜索__ ，屏幕右侧将显示对应指标图表及数据详情。

   - 支持自定义时间范围。可手动点击 __刷新__ 图标或选择默认时间间隔进行刷新。

    ![查询结果](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/metrics00.png)

4. 点击 __高级查询__ 页签通过原生的 PromQL 查询。

    ![高级查询](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/metics01.png)

!!! NOTE

    参阅 [PromQL 语法](https://prometheus.io/docs/prometheus/latest/querying/basics/)。
