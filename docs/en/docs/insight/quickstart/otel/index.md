---
MTPE: windsonsea
date: 2026-11-06
hide:
  - toc
---

# OTel Application Observability

Grant observability capabilities to applications through OpenTelemetry (OTel):
achieve non-intrusive enhancement via Operator annotations, manually instrument
with the OTel SDK, and send trace data to Insight.

## Core Workflow

<div class="grid cards" markdown>

- :material-application-brackets-outline:{ .lg .middle } __Non-Intrusive Enhancement with Operator__

    ---

    Automatically inject probes through annotations without modifying application code.

    [:arrow_forward: View details](operator.md)

- :material-chart-line:{ .lg .middle } __Manual Instrumentation with OTel SDK__

    ---

    Customized metrics, logs, and trace data through OTel SDK coding.

    [:arrow_forward: View details](otel.md)

- :material-connection:{ .lg .middle } __Send Trace Data to Insight__

    ---

    Report application trace data to the OTel Collector built into insight-agent.

    [:arrow_forward: View details](send_tracing_to_insight.md)

</div>

## Language and Scenario Guides

<div class="grid cards" markdown>

- :material-cube-outline:{ .lg .middle } __Observability for Go Applications__

    ---

    Enhance Go applications with OTel SDK, expose metrics, and write TraceId into logs.

    [:arrow_forward: View details](golang/)

- :material-chart-box-outline:{ .lg .middle } __Java Application Monitoring__

    ---

    Java Agent auto-instrumentation, JMX Exporter, and other ways to expose JVM metrics.

    [:arrow_forward: View details](java/)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
