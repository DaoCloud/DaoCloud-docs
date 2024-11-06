---
MTPE: windsonsea
Date: 2024-10-16
---

# Exposing JVM Metrics Using OpenTelemetry Java Agent

Starting from OpenTelemetry Agent v1.20.0 and later, the OpenTelemetry Agent has introduced the JMX Metric Insight module. If your application is already integrated with the OpenTelemetry Agent for tracing, you no longer need to introduce another agent to expose JMX metrics for your application. The OpenTelemetry Agent collects and exposes metrics by detecting the locally available MBeans in the application.

The OpenTelemetry Agent also provides built-in monitoring examples for common Java servers or frameworks. Please refer to the [Predefined Metrics](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/semantic-conventions.md).

When using the OpenTelemetry Java Agent, you also need to consider how to mount the JAR into the container. In addition to the methods for mounting the JAR file as described with the JMX Exporter, you can leverage the capabilities provided by the OpenTelemetry Operator to automatically enable JVM metrics exposure for your application.

If your application is already integrated with the OpenTelemetry Agent for tracing, you do not need to introduce another agent to expose JMX metrics. The OpenTelemetry Agent can now locally collect and expose metrics interfaces by detecting the locally available MBeans in the application.

However, as of the current version, you still need to manually add the appropriate annotations to your application for the JVM data to be collected by Insight. For specific annotation content, please refer to [Integrating Existing JVM Metrics of Java Applications with Observability](./legacy-jvm.md).

## Exposing Metrics for Java Middleware

The OpenTelemetry Agent also includes built-in examples for monitoring middleware. Please refer to the [Predefined Metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#predefined-metrics).

By default, no specific types are designated; you need to specify them using the `-Dotel.jmx.target.system` JVM options, for example, `-Dotel.jmx.target.system=jetty,kafka-broker`.

## References

- [Gaining JMX Metric Insights with the OpenTelemetry Java Agent](https://opentelemetry.io/blog/2023/jmx-metric-insight/)

- [Otel JMX Metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics)
