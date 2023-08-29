# How to implement the Ceph Dashboard dashboard

This page demonstrates how to import and successfully use the Ceph Monitoring Plane in DCE 5.0.

## Deploy Rook-ceph in DCE 5.0

[Deploy Rook-ceph](./dce-rook-ceph.md) first, then deploy rook-ceph-cluster.

- Since Ceph has no offline support at present, it is necessary to add an agent on the node where the working cluster is located (in the test, the working cluster is built in the demo-dev environment and the intranet)

     ```shell
     ip r add default via 10.6.102.1 dev ens192
     ```

- Due to the limited number of working nodes when deploying rook-ceph-cluster, you also need to set: `allowMultiplePerNode: true`

## Deploy Insight Agent in a worker cluster

To collect the monitoring metrics of rook-ceph-cluster, you need to [Install Insight Agent](../../insight/quickstart/install/install-agent.md),
Then create CR ServiceMonitor to collect monitoring information of rook-ceph-cluster.

1. The monitoring metrics of rook-ceph-cluster are exposed through port 9283.

     ![port 9283](https://docs.daocloud.io/daocloud-docs-images/docs/storage/solutions/images/agen01.png)

1. Create a ServiceMonitor for rook-ceph-mgr [Create a ServiceMonitor] in the worker cluster (../../insight/user-guide/collection-manag/service-monitor.md#_3).

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

## Deploy GrafanaDashboard in the Global cluster

Refer to [Dashboard Template](https://grafana.com/grafana/dashboards/2842-ceph-cluster/) to deploy GrafanaDashboard.

See [Insight Import Dashboard](../../insight/user-guide/dashboard/import-dashboard.md) when importing templates.

```yaml
apiVersion: integrally.org/v1alpha1
kind: Grafana Dashboard
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

## View Ceph Monitoring Dashboard

The current panel does not distinguish between clusters, and the cluster identification option will be optimized and added in the future.

![Monitoring Panel](https://docs.daocloud.io/daocloud-docs-images/docs/storage/solutions/images/dashboard01.png)
