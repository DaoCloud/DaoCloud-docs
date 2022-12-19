# 监控指标

本页说明如何在 Calico 中开启 `calico_prometheus_metrics`，接入 Prometheus 监控指标。

## 开启组件 metrics

通过 `kubespray` 部署时可根据 `calico_felix_prometheusmetricsenabled` 参数决定是否打开，默认为 false，或者通过以下方式手动开启：

1. 开启 `calico_felix_prometheusmetricsenabled`：

    ```shell
    calicoctl patch felixconfiguration default  --patch '{"spec":{"prometheusMetricsEnabled": true}}'
    ```

    或者

    ```shell
    kubectl patch felixconfiguration default --type merge --patch '{"spec":{"prometheusMetricsEnabled": true}}'
    ```

2. 开启 `calico_kube_controller_metrics`：

    ```shell
    calicoctl patch kubecontrollersconfiguration default  --patch '{"spec":{"prometheusMetricsPort": 9095}}'
    ```

    或者

    ```shell
    kubectl patch kubecontrollersconfiguration default --type=merge  --patch '{"spec":{"prometheusMetricsPort": 9095}}'
    ```

## 创建各自组件的 metrics service

`calico_felix_svc`：

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

`calico_`：

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

## 创建 `ServiceMonitor` 对象

`calico_felix_svc`：

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

`calico-kube-controllers-metrics`：

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

## 重要指标列表

| 序号 | 指标   | 说明   | 价值指数 | 其他说明 | 关联问题 |
|---------|-------------|-----------------------------------------|----------|--------|------|
| 1 | `felix_ipset_errors`| 执行 `ipset-restore` 失败次数 | ** | 可考虑采集 | 次数 +1 不一定造成问题
| 2 | `felix_iptables_restore_calls` | 执行 iptables-restore 次数 | ***** | 采集 | NA
| 3 | `felix_iptables_restore_errors` | 执行 iptables-restore 失败次数 | *****| 采集 | restore 失败可能造成 Pod 访问失败。出现 restore 失败的原因可能是`xtables_lock` 竞争失败，请检查主机上 iptables 数量是否过多
| 4 | `felix_iptables_save_calls` | 执行 iptables-save 的次数 | **** | 可考虑采集 | NA
| 5 | `felix_iptables_save_errors`| 执行 iptables-save 失败的次数 | ***** | 采集 |
| 6 | `felix_log_errors` | 日志报告 error 的次数 | ***** | 建议采集
| 7 | `ipam_allocations_per_node` | 每个节点上 IP 分配的数量 | **** | 建议采集
| 8 | `ipam_blocks_per_node` | 每个节点上分配的 Block 数量 | ***** | 采集 |
