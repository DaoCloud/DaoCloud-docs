---
MTPE: windsonsea
date: 2024-02-26
---

# Known Issues

This page lists some issues related to the installation and uninstallation of Insight Agent and their workarounds.

## v0.23.0

### Insight Agent

#### Uninstallation Failure of Insight Agent

When you run the following command to uninstall Insight Agent,

```sh
helm uninstall insight agent
```

The `tls secret` used by `otel-operator` is failed to uninstall.

Due to the logic of "reusing tls secret" in the following code of `otel-operator`,
it checks whether `MutationConfiguration` exists and reuses the CA cert bound in
MutationConfiguration. However, since `helm uninstall` has uninstalled `MutationConfiguration`,
it results in a null value.

Therefore, please manually delete the corresponding `secret` using one of the following methods:

- **Delete via command line**: Log in to the console of the target cluster and run the following command:

    ```sh
    kubectl -n insight-system delete secret insight-agent-opentelemetry-operator-controller-manager-service-cert
    ```

- **Delete via UI**: Log in to DCE 5.0 container management, select the target cluster, select **Secret**
  from the left menu, input `insight-agent-opentelemetry-operator-controller-manager-service-cert`,
  then select `Delete`.

### Insight Agent

#### Log Collection Endpoint Not Updated When Upgrading Insight Agent

When updating the log configuration of the insight-agent from Elasticsearch to Kafka or from Kafka
to Elasticsearch, the changes do not take effect and the agent continues to use the previous configuration.

**Solution** :

Manually restart Fluent Bit in the cluster.

## v0.21.0

### Insight Agent

#### PodMonitor Collects Multiple Sets of JVM Metrics

1. In this version, there is a defect in **PodMonitor/insight-kubernetes-pod**: it will incorrectly
   create Jobs to collect metrics for all containers in Pods that are marked with
   `insight.opentelemetry.io/metric-scrape=true`, instead of only the containers corresponding
   to `insight.opentelemetry.io/metric-port`.

2. After PodMonitor is declared, **PrometheusOperator** will pre-configure some service discovery configurations.
   Considering the compatibility of CRDs, it is abandoned to configure the collection tasks through **annotations**.

3. Use the additional scrape config mechanism provided by Prometheus to configure the service discovery rules
   in a secret and introduce them into Prometheus.

Therefore:

1. Delete the current **PodMonitor** for **insight-kubernetes-pod**
2. Use a new rule

In the new rule, **action: keepequal** is used to compare the consistency between **source_labels**
and **target_label** to determine whether to create collection tasks for the ports of a container.
Note that this feature is only available in Prometheus v2.41.0 (2022-12-20) and higher.

```diff
+    - source_labels: [__meta_kubernetes_pod_annotation_insight_opentelemetry_io_metric_port]
+      separator: ;
+      target_label: __meta_kubernetes_pod_container_port_number
+      action: keepequal
```
