---
hide:
  - toc
---

# 仪表盘

Grafana 是一种开源的数据可视化和监控平台，它提供了丰富的图表和面板，用于实时监控、分析和可视化各种数据源的指标和日志。可观测性 Insight 使用开源 Grafana 提供监控服务，支持从集群、节点、命名空间等多维度查看资源消耗情况，

关于开源 Grafana 的详细信息，请参见 [Grafana 官方文档](https://grafana.com/docs/grafana/latest/getting-started/?spm=a2c4g.11186623.0.0.1f34de53ksAH9a)。

## 操作步骤

1. 在左侧导航栏选择 __仪表盘__ 。

    - 在 __Insight /概览__ 仪表盘中，可查看多选集群的资源使用情况，并以命名空间、容器组等多个维度分析了资源使用、网络、存储等情况。

    - 点击仪表盘左上侧的下拉框可切换集群。

    - 点击仪表盘右下侧可切换查询的时间范围。

    ![dashboard](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/dashboard00.png){ width="1000"}

2. Insight 精选多个社区推荐仪表盘，可从节点、命名空间、工作负载等多个维度进行监控。点击 __insight-system / Insight /概览__ 区域切换仪表盘。

    ![dashboard](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/dashboard01.png){ width="1000"}

!!! note

    1. 访问 Grafana UI 请参考[以管理员身份登录 Grafana](../../user-guide/dashboard/login-grafana.md)。
    
    2. 导入自定义仪表盘请参考[导入自定义仪表盘](./import-dashboard.md)。
