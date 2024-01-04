---
MTPE: windsonsea
date: 2024-01-04
---

# Known Issues

This page lists some issues related to the installation and uninstallation of Insight Agent and their workarounds.

## v0.23.0

### Insight Agent

#### Uninstallation Failure of Insight Agent

1. When you run the following command to uninstall Insight Agent,

    ```sh
    helm uninstall insight agent
    ```

    The `tls secret` used by `otel-operator` is failed to uninstall.

2. Due to the logic of "reusing tls secret" in the following code of `otel-operator`,
   it checks whether `MutationConfiguration` exists and reuses the CA cert bound in
   MutationConfiguration. However, since `helm uninstall` has uninstalled `MutationConfiguration`,
   it results in a null value.

Therefore, please manually delete the corresponding `secret` using one of the following methods:

1. Log in to the console of the target cluster and run the following command:

    ```sh
    kubectl -n insight-system delete secret insight-agent-opentelemetry-operator-controller-manager-service-cert
    ```

2. Log in to DCE 5.0 Container Management, select the target cluster, navigate to `Secrets`
   in the left navigation menu, enter `insight-agent-opentelemetry-operator-controller-manager-service-cert`,
   and select `Delete`.

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
