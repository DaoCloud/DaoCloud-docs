# Start monitoring Java applications

This document mainly describes how to monitor the JVM of the customer's Java application.
It describes how Java applications that have exposed JVM metrics, and those that have not, interface with Insight.

If your Java application does not start exposing JVM metrics, you can refer to the following documents:

- [Expose JVM monitoring metrics with JMX Exporter](./jmx-exporter.md)
- [Expose JVM monitoring metrics using OpenTelemetry Java Agent](./otel-java-agent.md)

If your Java application has exposed JVM metrics, you can refer to the following documents:

- [Java application docking observability with existing JVM metrics](./legacy-jvm.md)