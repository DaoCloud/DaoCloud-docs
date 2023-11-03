# Known Issues

## v0.21.0

### Insight Agent

#### Multiple JVM Metric Collections by PodMonitor

1. The current implementation of `PodMonitor/insight-kubernetes-pod` has a defect:
   it incorrectly creates a Job to collect metrics from all containers in Pods marked with
   `insight.opentelemetry.io/metric-scrape=true`. It should only collect metrics from
   containers on the specified `insight.opentelemetry.io/metric-port`.

2. Due to the predefined service discovery configurations set by `PrometheusOperator`
   after declaring PodMonitors, and considering the compatibility of CRDs, the mechanism
   of creating collection tasks through `annotation` is abandoned.

3. Service discovery rules are configured in secrets using Prometheus' additional
   scrape config mechanism and introduced into Prometheus.

Therefore:

1. Remove the current `PodMonitor` `insight-kubernetes-pod`.
2. Use the new rules.

In the new rules, the `action: keepequal` is used to compare the consistency of `source_labels`
and `target_label` to determine whether to create a collection task for a container's port.
Please note that this functionality is available starting from Prometheus 2.41.0 (2022-12-20) and later versions.

```diff
+    - source_labels: [__meta_kubernetes_pod_annotation_insight_opentelemetry_io_metric_port]
+      separator: ;
+      target_label: __meta_kubernetes_pod_container_port_number
+      action: keepequal
```
