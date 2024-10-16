---
MTPE: windsonsea
Date: 2024-10-16
---

# Start Monitoring Java Applications

1. For accessing and monitoring Java application links, please refer to the document [Implementing Non-Intrusive Enhancements for Applications via Operator](../operator.md), which explains how to automatically integrate links through annotations.

2. Monitoring the JVM of Java applications: How Java applications that have already exposed JVM metrics and those that have not yet exposed JVM metrics can connect with observability Insight.

- If your Java application has not yet started exposing JVM metrics, you can refer to the following documents:

    - [Exposing JVM Monitoring Metrics Using JMX Exporter](./jvm-monitor/jmx-exporter.md)
    - [Exposing JVM Monitoring Metrics Using OpenTelemetry Java Agent](./jvm-monitor/otel-java-agent.md)

- If your Java application has already exposed JVM metrics, you can refer to the following document:
    
    - [Connecting Existing JVM Metrics of Java Applications to Observability](./jvm-monitor/legacy-jvm.md)

3. [Writing TraceId and SpanId into Java Application Logs](./mdc.md) to correlate link data with log data.
