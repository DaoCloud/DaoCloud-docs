# Monitoring metrics

This page explains how to enable `calico_prometheus_metrics` in Calico to access Prometheus monitoring metrics.

## Enable component metrics

When deploying through `kubespray`, you can decide whether to enable it according to the `calico_felix_prometheusmetricsenabled` parameter, which is false by default, or manually enable it in the following ways:

1. Enable `calico_felix_prometheusmetricsenabled`:

    ```shell
    calicoctl patch felixconfiguration default --patch '{"spec":{"prometheusMetricsEnabled": true}}'
    ```

    or

    ```shell
    kubectl patch felixconfiguration default --type merge --patch '{"spec":{"prometheusMetricsEnabled": true}}'
    ```

2. Enable `calico_kube_controller_metrics`:

    ```shell
    calicoctl patch kubecontrollersconfiguration default --patch '{"spec":{"prometheusMetricsPort": 9095}}'
    ```

    or

    ```shell
    kubectl patch kubecontrollersconfiguration default --type=merge --patch '{"spec":{"prometheusMetricsPort": 9095}}'
    ```

## Create the metrics service of the respective components

`calico_felix_svc`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: calico-node-metrics
  namespace: kube-system
  labels:
    app: calico-node
    role: metrics
spec:
  clusterIP: None
  selector:
    k8s-app: calico-node
  ports:
  - port: 9091
    name: metrics
    targetPort: 9091
```

`calico_`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: calico-kube-controllers-metrics
  namespace: kube-system
  labels:
    app: calico-kube-controllers
    role: metrics
spec:
  clusterIP: None
  selector:
    k8s-app: calico-kube-controllers
  ports:
  - port: 9095
    name: metrics
    targetPort: 9095
```

## Create `ServiceMonitor` object

`calico_felix_svc`:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: calico-node
  namespace: kube-system
  labels:
    app: calico-node
spec:
  endpoints:
  - interval: 30s
    port: metrics
  selector:
    matchLabels:
      app: calico-node
      role: metrics
```

`calico-kube-controllers-metrics`:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: calico-kube-controller
  namespace: kube-system
  labels:
    app: calico-kube-controller
spec:
  endpoints:
  - interval: 30s
    port: metrics
  selector:
    matchLabels:
      app: calico-kube-controllers
      role: metrics
```

## List of important metrics

| No. | Index | Explanation | Value Index | Other Explanations | Associated Issues |
|---------|-------------|------------------------- ----------------|----------|--------|------|
| 1 | `felix_ipset_errors`| Execution `ipset-restore` failed times | ** | Consider collection | Times +1 does not necessarily cause problems
| 2 | `felix_iptables_restore_calls` | Number of iptables-restore executions | ***** | Collection | NA
| 3 | `felix_iptables_restore_errors` | Number of iptables-restore failures | *****| Collection | Restore failure may cause Pod access failure. The restore failure may be due to the failure of `xtables_lock` competition, please check whether the number of iptables on the host is too large
| 4 | `felix_iptables_save_calls` | Number of times to execute iptables-save | **** | Can consider collecting | NA
| 5 | `felix_iptables_save_errors`| Number of failed iptables-save operations | ***** | Collection |
| 6 | `felix_log_errors` | The number of times the log reports an error | ***** | Recommended collection
| 7 | `ipam_allocations_per_node` | Number of IP allocations on each node | **** | Suggested collection
| 8 | `ipam_blocks_per_node` | Number of Blocks allocated on each node | ***** | Collection |