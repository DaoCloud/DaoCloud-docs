---
MTPE: WANG0608GitHub
Date: 2024-09-24
---

# Upgrade Notes

This page provides some considerations for upgrading insight-server and insight-agent.

## insight-agent

### Upgrade from v0.28.x (or lower) to v0.29.x

Due to the upgrade of the Opentelemetry community operator chart version in v0.29.0, the supported values for `featureGates` in the values file have changed. Therefore, before upgrading, you need to set the value of `featureGates` to empty, as follows:

```diff
-  --set opentelemetry-operator.manager.featureGates="+operator.autoinstrumentation.go,+operator.autoinstrumentation.multi-instrumentation,+operator.autoinstrumentation.nginx" \
+  --set opentelemetry-operator.manager.featureGates=""
```

## insight-server

### Upgrade from v0.26.x (or lower) to v0.27.x or higher

In v0.27.x, the switch for the vector component has been separated. If the existing environment has vector enabled, you need to specify `--set vector.enabled=true` when upgrading the insight-server.

### Upgrade from v0.19.x (or lower) to 0.20.x

Before upgrading __Insight__ , you need to manually delete the __jaeger-collector__ and
__jaeger-query__ deployments by running the following command:

```bash
kubectl -n insight-system delete deployment insight-jaeger-collector
kubectl -n insight-system delete deployment insight-jaeger-query
```

### Upgrade from v0.17.x (or lower) to v0.18.x

In v0.18.x, there have been updates to the Jaeger-related deployment files,
so you need to manually run the following commands before upgrading insight-server:

```bash
kubectl -n insight-system delete deployment insight-jaeger-collector
kubectl -n insight-system delete deployment insight-jaeger-query
```

There have been changes to metric names in v0.18.x, so after upgrading insight-server,
insight-agent should also be upgraded.

In addition, the parameters for enabling the tracing module and adjusting the ElasticSearch connection
have been modified. Refer to the following parameters:

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

### Upgrade from v0.15.x (or lower) to v0.16.x

In v0.16.x, a new feature parameter `disableRouteContinueEnforce` in the `vmalertmanagers CRD`
is used. Therefore, you need to manually run the following command before upgrading insight-server:

```shell
kubectl apply --server-side -f https://raw.githubusercontent.com/VictoriaMetrics/operator/v0.33.0/config/crd/bases/operator.victoriametrics.com_vmalertmanagers.yaml --force-conflicts
```

!!! note

    If you are performing an offline installation, after extracting the insight offline package,
    please run the following command to update CRDs.
    
    ```shell
    kubectl apply --server-side -f insight/dependency-crds --force-conflicts 
    ```

## insight-agent

### Upgrade from v0.23.x (or lower) to v0.24.x

In v0.24.x, CRDs have been added to the `OTEL operator chart`. However,
helm upgrade does not update CRDs, so you need to manually run the following command:

```shell
kubectl apply -f https://raw.githubusercontent.com/open-telemetry/opentelemetry-helm-charts/main/charts/opentelemetry-operator/crds/crd-opentelemetry.io_opampbridges.yaml
```

If you are performing an offline installation, you can find the above CRD yaml file after extracting the
insight-agent offline package. After extracting the insight-agent Chart, manually run the following command:

```shell
kubectl apply -f charts/agent/crds/crd-opentelemetry.io_opampbridges.yaml
```

### Upgrade from v0.19.x (or lower) to v0.20.x

In v0.20.x, Kafka log export configuration has been added, and there have been some adjustments
to the log export configuration. Before upgrading __insight-agent__ , please note the parameter changes.
The previous logging configuration has been moved to the logging.elasticsearch configuration:

```diff
-  --set global.exporters.logging.host \
-  --set global.exporters.logging.port \
+  --set global.exporters.logging.elasticsearch.host \
+  --set global.exporters.logging.elasticsearch.port \
```

### Upgrade from v0.17.x (or lower) to v0.18.x

Due to the updated deployment files for Jaeger In v0.18.x, it is important to
note the changes in parameters before upgrading the insight-agent.

```diff
+  --set global.exporters.trace.enable=true \
-  --set opentelemetry-collector.enabled=true \
-  --set opentelemetry-operator.enabled=true \
```

### Upgrade from v0.16.x (or lower) to v0.17.x

In v0.17.x, the kube-prometheus-stack chart version was upgraded from 41.9.1 to 45.28.1, and
there were also some field upgrades in the CRD used, such as the __attachMetadata__ field of
servicemonitor. Therefore, the following command needs to be rund before upgrading the insight-agent:

```bash
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.65.1/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml --force-conflicts
```

If you are performing an offline installation, you can find the yaml for the above CRD in
insight-agent/dependency-crds after extracting the insight-agent offline package.

### Upgrade from v0.11.x (or earlier) to v0.12.x

v0.12.x upgrades kube-prometheus-stack chart from 39.6.0 to 41.9.1, including prometheus-operator to v0.60.1, prometheus-node-exporter chart to v4.3.0.
Prometheus-node-exporter uses [Kubernetes recommended label](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/) after upgrading, so you need to delete __node-exporter__ daemonset.
prometheus-operator has updated the CRD, so you need to run the following command before upgrading the insight-agent:

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
