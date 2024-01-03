# Use OpenTelemetry Java Agent to expose JVM monitoring metrics

In Opentelemetry Agent v1.20.0 and above, Opentelemetry Agent has added the JMX Metric Insight module. If your application has integrated Opentelemetry Agent to collect application traces, then you no longer need to introduce other Agents for our application Expose JMX metrics. The Opentelemetry Agent also collects and exposes metrics by instrumenting the metrics exposed by MBeans locally available in the application.

Opentelemetry Agent also has some built-in monitoring samples for common Java Servers or frameworks, please refer to [predefined metrics](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics /semantic_conventions/runtime-environment-metrics.md#jvm-metrics).

Using the OpenTelemetry Java Agent also needs to consider how to mount the JAR into the container. In addition to referring to the JMX Exporter above to mount the JAR file, we can also use the Operator capabilities provided by OpenTelemetry to automatically enable JVM metric exposure for our applications. :

If your application has integrated Opentelemetry Agent to collect application traces, then you no longer need to introduce other Agents to expose JMX metrics for our application. The Opentelemetry Agent can now natively collect and expose metrics interfaces by instrumenting metrics exposed by MBeans available locally in the application.

However, for current version, you still need to manually add the [corresponding annotations](./legacy-jvm.md) to workload before the JVM data will be collected by Insight.

## Expose metrics for Java middleware

Opentelemetry Agent also has some built-in middleware monitoring samples, please refer to [Predefined Metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent /README.md#predefined-metrics).

By default, no type is specified, and it needs to be specified through __-Dotel.jmx.target.system__ JVM Options, such as __-Dotel.jmx.target.system=jetty,kafka-broker__ .

## Reference

- [Gaining JMX Metric Insights with the OpenTelemetry Java Agent](https://opentelemetry.io/blog/2023/jmx-metric-insight/)

- [Otel jmx metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics)