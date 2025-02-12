# Use OpenTelemetry Java Agent to expose JVM monitoring metrics

In Opentelemetry Agent v1.20.0 and above, Opentelemetry Agent has added the [JMX Metric Insight](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#jmx-metric-insight) module.

It collects and exposes metrics by instrumenting the metrics exposed by MBeans locally available in the application.

It also has some built-in monitoring samples for common Java Servers or frameworks, please refer to [predefined metrics](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics /semantic_conventions/runtime-environment-metrics.md#jvm-metrics).

If your application has integrated Opentelemetry Agent to collect application traces, then you no longer need to introduce other Agents to expose JMX metrics for our application. 

Following the below example to start collect your application JVM metrics:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  selector:
    matchLabels:
      app: my-app
  replicas: 1
  template:
    metadata:
      labels:
        app: my-app
      annotations:
        instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation" # marking this pod will automatically integrate Opentelemetry Agent
        # the below key-values tell prometheus operator how to scrape metrics
        insight.opentelemetry.io/metric-scrape: "true" # whether to collect
        insight.opentelemetry.io/metric-path: "/" # path to collect metrics
        insight.opentelemetry.io/metric-port: "9464" # port for collecting metrics
    spec:
      containers:
      - name: myapp
        image: jaegertracing/vertx-create-span:operator-e2e-tests
        ports:
          - containerPort: 8080
            protocol: TCP
          - containerPort: 9464 # the pod need expose 9464 port and the relate SVC also need it
            protocol: TCP
```

If there is a port conflict, you can specify a new metric port for your application:__- Dotel.exporter.prometheus.port=8464__，
After the modification, the port values at other locations should also be modified.

## Expose metrics for Java middleware

Opentelemetry Agent also has some built-in middleware monitoring samples, please refer to [Predefined Metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent /README.md#predefined-metrics).

By default, no type is specified, and it needs to be specified through __-Dotel.jmx.target.system__ JVM Options, such as __-Dotel.jmx.target.system=jetty,kafka-broker__ .

## Reference

- [Gaining JMX Metric Insights with the OpenTelemetry Java Agent](https://opentelemetry.io/blog/2023/jmx-metric-insight/)

- [Otel jmx metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics)