---
hide:
   - toc
---

# Upgrade Notes

## insight server

### Upgrading from v0.17.x (or lower) to v0.18.x

Since there are updated deployment files for Jaeger in version 0.18.x, you need to
manually run the following commands before upgrading the insight server:

```bash
kubectl -n insight-system delete deployment insight-jaeger-collector
kubectl -n insight-system delete deployment insight-jaeger-query
```

Furthermore, there have been changes in metric names in version 0.18.x, so after
upgrading insight server, insight-agent should also be upgraded.

In addition, there have been adjustments in the parameters for enabling the tracing module and the Elasticsearch connection. Please refer to the specific parameters below:

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

### Upgrading from v0.15.x (or lower) to v0.16.x

Since the new feature parameter disableRouteContinueEnforce of vmalertmanagers CRD is used in 0.16.x,
the following commands need to be manually executed before upgrading the insight server.

```shell
kubectl apply --server-side -f https://raw.githubusercontent.com/VictoriaMetrics/operator/v0.33.0/config/crd/bases/operator.victoriametrics.com_vmalertmanagers.yaml --force-conflicts
```

!!! note

     If you are installing offline, you can run the following command to update the
     CRD after decompressing the insight offline package.
    
     ```shell
     kubectl apply --server-side -f insight/dependency-crds --force-conflicts
     ````

## insight-agent

### Upgrading from v0.17.x (or lower) to v0.18.x

Due to the updated deployment files for Jaeger in version 0.18.x, it is important to
note the changes in parameters before upgrading the Insight Agent.

```diff
+  --set global.exporters.trace.enable=true \
-  --set opentelemetry-collector.enabled=true \
-  --set opentelemetry-operator.enabled=true \
```

### Upgrading from v0.16.x (or lower) to v0.17.x

In v0.17.x, the kube-prometheus-stack chart version was upgraded from 41.9.1 to 45.28.1, and
there were also some field upgrades in the CRD used, such as the `attachMetadata` field of
servicemonitor. Therefore, the following command needs to be executed before upgrading the insight agent:

```bash
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.65.1/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml --force-conflicts
```

If you are performing an offline installation, you can find the yaml for the above CRD in
insight-agent/dependency-crds after extracting the insight-agent offline package.

### Upgrade from v0.11.x (or earlier) to v0.12.x

v0.12.x upgrades kube-prometheus-stack chart from 39.6.0 to 41.9.1, including prometheus-operator to v0.60.1, prometheus-node-exporter chart to 4.3.0, etc.
Prometheus-node-exporter uses [Kubernetes recommended label](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/) after upgrading, so you need to delete `node- exporter`s daemonset.
prometheus-operator has updated the CRD, so you need to run the following command before upgrading the insight agent:

```shell linenums="1"
kubectl delete daemonset insight-agent-prometheus-node-exporter -n insight-system
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_alertmanagerconfigs.yaml --force- conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_alertmanagers.yaml --force- conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_podmonitors.yaml --force- conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_probes.yaml --force- conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_prometheuses.yaml --force- conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_prometheusrules.yaml --force- conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml --force- conflicts
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.60.1/example/prometheus-operator-crd/monitoring.coreos.com_thanosrulers.yaml --force- conflicts
```

!!! note

     If you are installing offline, you can run the following command to update the CRD after decompressing the insight-agent offline package.
    
     ```shell
     kubectl apply --server-side -f insight-agent/dependency-crds --force-conflicts
     ```
  