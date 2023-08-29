# 如何实现 Ceph Dashboard 仪表盘

本页演示如何在 DCE 5.0 中导入并成功使用 Ceph 监控面板。

## 在 DCE 5.0 中部署 Rook-ceph

先[部署 Rook-ceph](./dce-rook-ceph.md)，再部署 rook-ceph-cluster。

- 由于目前 Ceph 还没离线化支持，所以需要在工作集群的所在节点上增加代理（测试中是在 demo-dev 环境以及内网搭建的工作集群）

    ```shell
    ip r add default via 10.6.102.1 dev ens192
    ```

- 部署 rook-ceph-cluster 时由于工作节点数量有限，还需要设置：`allowMultiplePerNode: true`

## 在工作集群中部署 Insight Agent

采集 rook-ceph-cluster 的监控指标需要先[安装 Insight Agent](../../insight/quickstart/install/install-agent.md)，
然后创建 CR ServiceMonitor 来采集 rook-ceph-cluster 的监控信息。

1. rook-ceph-cluster 的监控指标通过 9283 端口暴露。

    ![port 9283](https://docs.daocloud.io/daocloud-docs-images/docs/storage/solutions/images/agen01.png)

1. 在工作集群中为 rook-ceph-mgr [创建 ServiceMonitor](../../insight/user-guide/collection-manag/service-monitor.md#_3)。

    ```yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
    labels:
      operator.insight.io/managed-by: insight
    name: rook-ceph-sm
    namespace: rook-ceph
    spec:
    endpoints:
      - honorLabels: true
      port: http-metrics
    namespaceSelector:
      any: true
    selector:
      matchLabels:
      app: rook-ceph-mgr
      rook_cluster: rook-ceph
    ```

## 在 Global 集群中部署 GrafanaDashboard

参考 [Dashboard 模板](https://grafana.com/grafana/dashboards/2842-ceph-cluster/)部署 GrafanaDashboard。

导入模板时请参阅 [Insight 导入仪表盘](../../insight/user-guide/dashboard/import-dashboard.md)。

```yaml
apiVersion: integreatly.org/v1alpha1
kind: GrafanaDashboard
metadata:
  labels:
    app: insight-grafana-operator
    operator.insight.io/managed-by: insight
  name: ceph-dashboard
  namespace: insight-system
spec:
  json: >
    {
        "__inputs": [],
        "__elements": {},
        "__requires": [
        {
            "type": "panel",
            "id": "gauge",
            "name": "Gauge",
            "version": ""
        },
        {
            "type": "grafana",
            "id": "grafana",
            "name": "Grafana",
            "version": "9.0.5"
        },
....
```

## 查看 Ceph 监控面板

目前的面板还未区分集群，后续将陆续优化增加 cluster 标识选项。

![监控面板](https://docs.daocloud.io/daocloud-docs-images/docs/storage/solutions/images/dashboard01.png)
