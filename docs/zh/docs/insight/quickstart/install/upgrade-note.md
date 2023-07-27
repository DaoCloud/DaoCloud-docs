---
hide:
  - toc
---

# 升级注意事项

## insight server

### 从 v0.17.x（或更低版本）升级到 v0.18.x

由于 0.18.x 中更新了 Jaeger 相关部署文件，因此需要在升级 insight server 前手动执行如下命令：

```bash
kubectl -n insight-system delete deployment insight-jaeger-collector
kubectl -n insight-system delete deployment insight-jaeger-query
```

由于 0.18.x 中指标名产生了变动，因此，需要在升级 Insight Server 之后，Insight Agent 也应该做升级。

此外，调整了开启链路模块的参数，以及 ElasticSearch 连接调整。具体参考以下参数：

```diff
+  --set global.tracing.enable=true \
-  --set jaeger.collector.enabled=true \
-  --set jaeger.query.enabled=true \
+  --set global.elasticsearch.scheme=${your-external-elasticsearch-scheme} \
+  --set global.elasticsearch.host=${your-external-elasticsearch-host} \
+  --set global.elasticsearch.port=${your-external-elasticsearch-port} \
+  --set global.elasticsearch.user=${your-external-elasticsearch-username} \
+  --set global.elasticsearch.password=${your-external-elasticsearch-password} \
-  --set jaeger.storage.elasticsearch.scheme=${your-external-elasticsearch-scheme} \
-  --set jaeger.storage.elasticsearch.host=${your-external-elasticsearch-host} \
-  --set jaeger.storage.elasticsearch.port=${your-external-elasticsearch-port} \
-  --set jaeger.storage.elasticsearch.user=${your-external-elasticsearch-username} \
-  --set jaeger.storage.elasticsearch.password=${your-external-elasticsearch-password} \
```

### 从 v0.15.x（或更低版本）升级到 v0.16.x

由于 0.16.x 中使用了 vmalertmanagers CRD 的新特性参数 disableRouteContinueEnforce, 因此需要在升级 insight server 前手动执行如下命令。

```shell
kubectl apply --server-side -f https://raw.githubusercontent.com/VictoriaMetrics/operator/v0.33.0/config/crd/bases/operator.victoriametrics.com_vmalertmanagers.yaml --force-conflicts
```

!!! note

    如您是离线安装，可以在解压 insight 离线包后，请执行以下命令更新 CRD。
    
    ```shell
    kubectl apply --server-side -f insight/dependency-crds --force-conflicts 
    ```

## insight-agent

### 从 v0.17.x（或更低版本）升级到 v0.18.x

由于 0.18.x 中更新了 Jaeger 相关部署文件，因此需要在升级 insight agent 前需要注意参数的改动。

```diff
+  --set global.exporters.trace.enable=true \
-  --set opentelemetry-collector.enabled=true \
-  --set opentelemetry-operator.enabled=true \
```

### 从 v0.16.x（或更低版本）升级到 v0.17.x

在 v0.17.x 版本中将 kube-prometheus-stack chart 版本从 41.9.1 升级至 45.28.1, 其中使用的 CRD 也存在一些字段的升级，如 servicemonitor 的 `attachMetadata` 字段，因此需要在升级 insight agent 前执行如下命令：

```bash
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.65.1/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml --force-conflicts
```

如您是离线安装，可以在解压 insight-agent 离线包后，在 insight-agent/dependency-crds 中找到上述 CRD 的 yaml。

### 从 v0.11.x（或更低版本）升级到 v0.12.x

在 v0.12.x 将 kube-prometheus-stack chart 从 39.6.0 升级到 41.9.1，其中包括 prometheus-operator 升级到 v0.60.1, prometheus-node-exporter chart 升级到 4.3.0 等。
prometheus-node-exporter 升级后使用了 [Kubernetes 推荐 label](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/)，因此需要在升级前删除 `node-exporter` 的 daemonset。
prometheus-operator 更新了 CRD，因此需要在升级 insight agent 前执行如下命令：

```shell linenums="1"
kubectl delete daemonset insight-agent-prometheus-node-exporter -n insight-system
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_alertmanagerconfigs.yaml --force-conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_alertmanagers.yaml --force-conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_podmonitors.yaml --force-conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_probes.yaml --force-conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_prometheuses.yaml --force-conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_prometheusrules.yaml --force-conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml --force-conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_thanosrulers.yaml --force-conflicts
```

!!! note

    如您是离线安装，可以在解压 insight-agent 离线包后，执行以下命令更新 CRD。
    
    ```shell
    kubectl apply --server-side -f insight-agent/dependency-crds --force-conflicts
    ```
