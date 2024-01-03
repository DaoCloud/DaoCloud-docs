# Known Issues

## v0.21.0

### Insight Agent

#### Multiple JVM Metric Collections by PodMonitor

1. The current implementation of __PodMonitor/insight-kubernetes-pod__ has a defect:
   it incorrectly creates a Job to collect metrics from all containers in Pods marked with
   `insight.opentelemetry.io/metric-scrape=true`. It should only collect metrics from
   containers on the specified `insight.opentelemetry.io/metric-port`.

2. Due to the predefined service discovery configurations set by __PrometheusOperator__ 
   after declaring PodMonitors, and considering the compatibility of CRDs, the mechanism
   of creating collection tasks through __annotation__ is abandoned.

3. Service discovery rules are configured in secrets using Prometheus' additional
   scrape config mechanism and introduced into Prometheus.

Therefore:

1. Remove the current __PodMonitor__ __insight-kubernetes-pod__ .
2. Use the new rules.

In the new rules, the __action: keepequal__ is used to compare the consistency of __source_labels__ 
and __target_label__ to determine whether to create a collection task for a container's port.
Please note that this functionality is available starting from Prometheus 2.41.0 (2022-12-20) and later versions.

```diff
+    - source_labels: [__meta_kubernetes_pod_annotation_insight_opentelemetry_io_metric_port]
+      separator: ;
+      target_label: __meta_kubernetes_pod_container_port_number
+      action: keepequal
```
