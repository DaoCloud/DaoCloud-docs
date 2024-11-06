---
hide:
   - toc
---

# Dashboard

Grafana is a cross-platform open source visual analysis tool. Insight uses open source Grafana
to provide monitoring services, and supports viewing resource consumption from multiple dimensions
such as clusters, nodes, and namespaces.

For more information on open source Grafana, see
[Grafana Official Documentation](https://grafana.com/docs/grafana/latest/getting-started/?spm=a2c4g.11186623.0.0.1f34de53ksAH9a).

## Steps

1. Select __Dashboard__ from the left navigation bar .

    - In the __Insight / Overview__ dashboard, you can view the resource usage of multiple clusters and analyze resource usage, network, storage, and more based on dimensions such as namespaces and Pods.

    - Click the dropdown menu in the upper-left corner of the dashboard to switch between clusters.

    - Click the lower-right corner of the dashboard to switch the time range for queries.

    ![Dashboard](../images/dashboard00.png)

2. Insight provides several recommended dashboards that allow monitoring from different dimensions
   such as nodes, namespaces, and workloads. Switch between dashboards by clicking the
   __insight-system / Insight / Overview__ section.

    ![Overview](../images/dashboard01.png)

!!! note

    1. For accessing Grafana UI, refer to [Access Native Grafana](../../user-guide/dashboard/login-grafana.md).

    2. For importing custom dashboards, refer to [Importing Custom Dashboards](./import-dashboard.md).
