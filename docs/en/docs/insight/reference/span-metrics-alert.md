# Enable Span Metrics Alert Rules and Custom Span Alert Rules

Since v0.33.0, Insight has built in core monitoring alert policies for service traces (SpanMetrics). When installing Insight with Helm, you can enable them with the parameter
`--set victoria-metrics-k8s-stack.defaultRules.spanmetrics=true`. Once enabled, you do not need to configure the basic rules manually.
Automated monitoring and anomaly alerts for the two key dimensions of service or API call error rate and request latency are then available, which further lowers the barrier to adopting observability and improves the efficiency of issue discovery in microservice architectures.

This document describes in detail the SpanMetrics alert rules (of type VMRule) built into the Insight observability platform, helping you understand the meaning of the metrics and the PromQL logic behind each alert rule, so that you can correctly configure or customize the related alert rules in the Alert Center.

This group of rules supports anomaly detection at both the service level (the whole service dimension) and the Span level (the specific API/method dimension), covering overall service health and fine-grained issue localization.

## Built-in Alert Rules

The built-in rules contain 4 core alerts in total, divided into the two categories of error rate and latency and covering the two granularities of service and Span. The specific configuration is shown in the following table:

| Alert Name | Monitoring Dimension | Monitoring Metric | Trigger Condition | Severity | Duration |
| :--- | :----: | ---: | ---: | ---: | ---: |
| ServiceErrorRate | Service-level error rate | calls_total | Error rate of server-side spans ≥ 15% (statistical window: 10 minutes) | critical | 10 minutes |
| SpanErrorRate | Span-level error rate | calls_total | Error rate of server-side spans of a specific API ≥ 15% (statistical window: 10 minutes) | critical | 10 minutes |
| ServiceLatency  | Service-level average latency | duration_milliseconds_bucket | Average server-side span latency ≥ 1000 ms (1 second, statistical window: 10 minutes) | critical | 10 minutes |
| SpanLatency | Span-level average latency | duration_milliseconds_bucket | Average server-side span latency of a specific API ≥ 1000 ms (1 second, statistical window: 10 minutes) | critical | 10 minutes |

The following is the specific content of the built-in alert rules:

```yaml
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMRule
metadata:
  name: spanmetrics
  namespace: insight-system
  labels:
    # Rules are deployed in the insight-system namespace by default; alert rules with this label are built-in rules
    "operator.insight.io/builtin-rule": "true" 
spec:
  groups:
  - name: spanmetrics
    rules:
    - alert: ServiceErrorRate
      annotations:
        description: Error rate of Service {{ $labels.service_name }} in cluster/namespace {{ $labels.cluster }}/{{ $labels.k8s_namespace_name }} is greater than {{ printf "%.2f" $value }}%.'
      expr: 100 * (sum(rate(calls_total{status_code="STATUS_CODE_ERROR",span_kind =~"SPAN_KIND_SERVER"}[10m])) by (cluster,namespace,k8s_namespace_name,k8s,service_name) / sum(rate(calls_total{span_kind =~"SPAN_KIND_SERVER"}[10m])) by (cluster,namespace,k8s_namespace_name,service_name)) >= 15
      for: 10m
      labels:
        severity: critical
        # namespace from k8s_namespace_name: backward Backwards-compatible scenarios where the agent is not upgraded
        namespace: '{{ $labels.k8s_namespace_name }}'
    - alert: SpanErrorRate
      annotations:
        description: Error rate of SpanName {{ $labels.span_name }} of {{ $labels.pod }} Service {{ $labels.service_name }} in cluster/namespace {{ $labels.cluster }}/{{ $labels.k8s_namespace_name }} is greater than {{ printf "%.2f" $value }}%.
      expr: 100 * (sum(rate(calls_total{status_code="STATUS_CODE_ERROR",span_kind =~"SPAN_KIND_SERVER"}[10m])) by (cluster,namespace,k8s_namespace_name,service_name,span_name) / sum(rate(calls_total{span_kind =~"SPAN_KIND_SERVER"}[10m])) by (cluster,namespace,k8s_namespace_name,service_name,span_name)) >= 15
      for: 10m
      labels:
        severity: critical
        namespace: '{{ $labels.k8s_namespace_name }}'
    - alert: ServiceLatency
      annotations:
        description: Latency of Service {{ $labels.service_name }} in cluster/namespace {{ $labels.cluster }}/{{ $labels.k8s_namespace_name }} is greater than {{ printf "%.2f" $value }}.
      expr: (sum(rate(duration_milliseconds_bucket{span_kind =~"SPAN_KIND_SERVER"}[10m])) by (cluster,namespace,k8s_namespace_name,service_name,le)) >= 1000
      for: 10m
      labels:
        severity: critical
        namespace: '{{ $labels.k8s_namespace_name }}'
    - alert: SpanLatency
      annotations:
        description: Latency of SpanName {{ $labels.span_name }} of {{ $labels.pod }} Service {{ $labels.service_name }} in cluster/namespace {{ $labels.cluster }}/{{ $labels.k8s_namespace_name }} is greater than {{ printf "%.2f" $value }}.
      expr: (sum(rate(duration_milliseconds_bucket{span_kind =~"SPAN_KIND_SERVER"}[10m])) by (cluster,namespace,k8s_namespace_name,service_name,span_name,le)) >= 1000
      for: 10m
      labels:
        severity: critical
        namespace: '{{ $labels.k8s_namespace_name }}'
```

### Rule Characteristics

- Statistical scope: Only span_kind=~"SPAN_KIND_SERVER" (server-side spans) is covered, focusing on the APIs that a service exposes to the outside and excluding non-core scenarios such as clients and internal traces;
- Metric calculation: The error rate is calculated with the rate function to obtain the per-second call rate, and the latency is calculated with the increase function to obtain the counter increment, which avoids loss of precision and follows the best practices for Prometheus counter metrics;
- Label pass-through: Alert messages include key labels such as cluster, service_name, k8s_namespace_name, and span_name, which makes it easy to quickly locate the environment and business module to which an issue belongs.

## Custom Rules

This section mainly illustrates how to write PromQL statements to meet business requirements when creating rules. For UI operations, see [Alert Policies](../user-guide/alert-center/alert-policy.md).

For example:

- First create an alert policy for the `Cluster` object:

    ![Example alert group for the payment service](../images/spanmetrics-alert-policy.png)

- Then add an alert rule with PromQL:

    ![Example alert rule for the payment service](../images/spanmetrics-error_rate.png)

The following are PromQL examples for different scenarios:

### Example 1

Adjust the error rate threshold for a specific service (strict monitoring for a core service): for the payment service (service_name: "pay-service"), you need to lower the error rate threshold from the built-in 15% to 5%, and an alert is triggered only after the condition persists for 5 minutes.

```promql
100 * (sum(rate(calls_total{status_code="STATUS_CODE_ERROR",span_kind=~"SPAN_KIND_SERVER",service_name="pay-service"}[5m])) by (cluster,service_name,k8s_namespace_name) / sum(rate(calls_total{span_kind=~"SPAN_KIND_SERVER",service_name="pay-service"}[5m])) by (cluster,service_name,k8s_namespace_name)) >= 5
```

### Example 2

Monitor the P95 latency of a specific service (fine-grained performance monitoring): for the "createOrder" API (span_name: "createOrder") of the order service, you need to monitor its P95 latency and trigger an alert once it exceeds 800 ms.

```promql
histogram_quantile(0.95, sum(rate(duration_milliseconds_bucket{span_kind=~"SPAN_KIND_SERVER",service_name="order-service",span_name="createOrder"}[10m])) by (cluster,k8s_namespace_name,service_name,span_name,le)) >= 800
```

!!! note

    The built-in rules only monitor the average latency. The P95/P99 percentile latency must be calculated based on duration_milliseconds_bucket (a histogram metric), which better matches the real user experience.

### Example 3

Monitor a sudden drop in service call volume (availability fallback monitoring): the call volume of the user service (service_name: "user-service") suddenly drops by more than 50%, which may mean that the service is unavailable or the traffic is abnormal, and an alert needs to be sent in time.

```promql
rate(calls_total{span_kind=~"SPAN_KIND_SERVER",service_name="user-service"}[5m]) / rate(calls_total{span_kind=~"SPAN_KIND_SERVER",service_name="user-service"}[5m] offset 5m) <= 0.5
```
