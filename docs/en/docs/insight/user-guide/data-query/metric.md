# Metric query

Metric query supports querying the index data of each container resource, and you can view the trend changes of the monitoring index. At the same time, advanced query supports native PromQL statements for Metric query.

## Prerequisites

- The cluster has [insight-agent installed](../../quickstart/install/install-agent.md) and the application is in __running__ state.

## Common query

1. In the left navigation bar, click __Data Query__ -> __metric Query__ .

2. After selecting query conditions such as cluster, type, node, and metric name, click __Search__ ,
   and the corresponding metric chart and data details will be displayed on the right side of the screen.

    

!!! tip

    Support custom time range. You can manually click the __Refresh__ icon or select a default time interval to refresh.

## Advanced Search

1. In the left navigation bar, click __Data Query__ -> __metric Query__ ,
   click the __Advanced Query__ tab to switch to the advanced query page.

    

2. Enter a PromQL statement
   (see [PromQL Syntax](https://prometheus.io/docs/prometheus/latest/querying/basics/)),
   click __Query__ , and the query metric chart and data details will be displayed.

    