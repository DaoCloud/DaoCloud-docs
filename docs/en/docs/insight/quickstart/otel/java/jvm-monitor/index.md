---
MTPE: windsonsea
date: 2026-11-06
hide:
  - toc
---

# Exposing JVM Monitoring Metrics

Multiple ways to expose JVM monitoring metrics: collect non-intrusively with
JMX Exporter or the OpenTelemetry Java Agent, or integrate applications that
already expose JVM metrics with the observability platform.

## Approaches

<div class="grid cards" markdown>

- :material-chart-box-outline:{ .lg .middle } __Expose JVM Metrics Using JMX Exporter__

    ---

    Start as a Java agent and expose JVM monitoring metrics through an HTTP endpoint.

    [:arrow_forward: View details](jmx-exporter.md)

- :material-chart-line:{ .lg .middle } __Expose JVM Metrics Using OTel Java Agent__

    ---

    Automatically collect JVM and application metrics in a non-intrusive way.

    [:arrow_forward: View details](otel-java-agent.md)

- :material-database-outline:{ .lg .middle } __Integrate Existing JVM Metrics__

    ---

    Connect Java applications that already expose JVM metrics to the observability platform.

    [:arrow_forward: View details](legacy-jvm.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
