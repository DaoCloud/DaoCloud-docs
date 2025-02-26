# Prometheus 集群标签配置

本文说明如何修改 Prometheus(CR) 为监控指标添加集群标识标签（cluster_name），以提高指标、告警消息的可读性。

## 方式一：通过 Prometheus 修改

1. 在命令行执行以下语句找到 Prometheus(CR)

    ```shell
    kubectl get prometheus -n insight-system
    ```

    预期输出示例：

    ```
    NAME                                    VERSION   DESIRED   READY   RECONCILED   AVAILABLE   AGE
    insight-agent-kube-prometh-prometheus   v2.44.0   1         1       True         True        73d
    ```

1. 编辑 Prometheus CR，在 `spec.externalLabels` 参数中增加 `cluster_name`，作为在容器管理中注册的名字。

    ```diff
    apiVersion: monitoring.coreos.com/v1
    kind: Prometheus
    metadata:
      name: insight-agent-kube-prometh-prometheus
      namespace: insight-system
    spec:
      externalLabels:
        cluster: deb65d24-1090-40cf-b5e6-489fac2f2c1b
    +   cluster_name: kpanda-global-cluster
    ```

## 方式二：通过 Helm 修改（推荐）

1. 建议通过 Helm 来更新 `Prometheus CR`，以避免在升级过程中丢失这些配置。编辑 `values.yaml` 里对应的参数：

    ```diff
    kube-prometheus-stack:
      prometheus:
        prometheusSpec:
          externalLabels:
            cluster: '{{ (lookup "v1" "Namespace" "" "kube-system").metadata.uid }}'
    +       cluster_name: 'kpanda-global-cluster'
    ```

1. 可以通过 `--set` 参数来设置

    ```shell
    --set kube-prometheus-stack.prometheus.prometheusSpec.externalLabels.cluster_name='kpanda-global-cluster'
    ```

## 补充说明

在容器管理 v0.27 版本之后，集群的名字也会标记在 `kpanda-system` 的 `namespace` 中，记录在 `kpanda.io/cluster-name` 的标签中。

```yaml
kubectl get ns kpanda-system -o yaml                                                                    
apiVersion: v1
kind: Namespace
metadata:
  finalizers:
  - kpanda.io/kpanda-system
  labels:
    kpanda.io/cluster-name: kpanda-global-cluster
    kpanda.io/kube-system-id: deb65d24-1090-40cf-b5e6-489fac2f2c1b
    kubernetes.io/metadata.name: kpanda-system
    name: kpanda-system
  name: kpanda-system
spec:
  finalizers:
  - kubernetes
status:
  phase: Active
```
