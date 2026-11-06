---
MTPE: windsonsea
date: 2026-11-06
---

# Best Practices

Insight uses standard OTel technology and the standard OTLP protocol, which is compatible with any observability data conforming to OTLP. This page lists best practices for the observability module, covering observability technology integration, data storage and performance, and troubleshooting.

## Technology Integration

<div class="grid cards" markdown>

- :material-exchange:{ .lg .middle } __Receive SkyWalking Trace Data with Zero-Code OpenTelemetry__

    ---

    Seamlessly integrate SkyWalking Agent trace data.

    [:arrow_forward: View details](sw-to-otel.md)

- :material-gate:{ .lg .middle } __Integrate Nginx Ingress Trace Tracking__

    ---

    Enable full-link observability for gateway traffic.

    [:arrow_forward: View details](ingress-otel.md)

- :material-water:{ .lg .middle } __Integrate DeepFlow__

    ---

    Complement application observability with eBPF-based zero-intrusion collection.

    [:arrow_forward: View details](integration_deepflow.md)

</div>

## Data Storage and Performance

<div class="grid cards" markdown>

- :material-chart-box-outline:{ .lg .middle } __Persisting Insight Grafana Data to a Database__

    ---

    Persistence for custom dashboards.

    [:arrow_forward: View details](grafana-use-db.md)

- :simple-apachekafka:{ .lg .middle } __Kafka + Elasticsearch Stream Architecture for Large-Scale Logs__

    ---

    Architecture adjustment for large-scale log deployment.

    [:arrow_forward: View details](insight-kafka.md)

- :material-gauge:{ .lg .middle } __VictoriaMetrics Resource Planning__

    ---

    Capacity and resource configuration for VM storage components.

    [:arrow_forward: View details](vm-resource-plan.md)

- :material-filter-variant:{ .lg .middle } __About Trace Sampling and Configuration__

    ---

    Tail-based sampling to balance cost and troubleshooting value.

    [:arrow_forward: View details](tail-based-sampling.md)

</div>

## Troubleshooting

<div class="grid cards" markdown>

- :material-bug-outline:{ .lg .middle } __Log Collection Troubleshooting Guide__

    ---

    Diagnostic approach and steps for log collection issues.

    [:arrow_forward: View details](debug-log.md)

- :material-radar:{ .lg .middle } __Trace Collection Troubleshooting Guide__

    ---

    How to troubleshoot missing or abnormal trace data.

    [:arrow_forward: View details](debug-trace.md)

- :material-target:{ .lg .middle } __Troubleshooting Service Issues with Insight__

    ---

    Rapidly locate application issues using metrics, logs, and traces.

    [:arrow_forward: View details](find_root_cause.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
