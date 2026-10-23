# Metric query

Metric query supports querying the index data of each container resource, and you can view the trend changes of the monitoring index. At the same time, advanced query supports native PromQL statements for Metric query.

## Prerequisites

- The cluster has [insight-agent installed](../../quickstart/install/install-agent.md) and the application is in __running__ state.

## Steps

1. Click the primary navigation bar to enter __Insight__.

2. In the left navigation bar, select __Metric__.

3. After selecting query conditions such as cluster, type, node, and metric name, click __Search__, and the corresponding metric chart and data details will be displayed on the right side of the screen.

   - Support custom time range. You can manually click the __Refresh__ icon or select a default time interval to refresh.

    ![Query result](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/metrics00.png)

4. Click the __Advanced Query__ tab to query with native PromQL.

    ![Advanced query](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/metics01.png)

!!! NOTE

    See [PromQL Syntax](https://prometheus.io/docs/prometheus/latest/querying/basics/).
