---
MTPE: windsonsea
Date: 2024-10-16
---

# Exposing JVM Metrics Using OpenTelemetry Java Agent

In OpenTelemetry Agent v1.20.0 and later, OpenTelemetry Agent has added the [JMX Metric Insight](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#jmx-metric-insight) module,
which also collects and exposes metrics by detecting the locally available MBeans in the application. It also provides built-in monitoring examples for common Java servers or frameworks, refer to [Predefined Metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#predefined-metrics).
If your application has already had the OpenTelemetry Agent automatically injected through the OpenTelemetry Operator, you no longer need to introduce another Agent to expose JMX metrics for your application. For example, the following demo:

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
        instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation" # required for injecting the otel agent
        # The following are the 3 annotations required for metric collection
        insight.opentelemetry.io/metric-scrape: "true" # whether to collect
        insight.opentelemetry.io/metric-path: "/metrics"      # path to collect metrics
        insight.opentelemetry.io/metric-port: "9464"   # port to collect metrics
    spec:
      containers:
      - name: myapp
        image: jaegertracing/vertx-create-span:operator-e2e-tests
        ports:
          - containerPort: 8080
            protocol: TCP
          - containerPort: 9464 # the container also needs to expose port 9464 accordingly, and the SVC corresponding to the Deployment also needs to declare port 9464
            protocol: TCP
```

In the above Deployment, we added four annotations under __template.metadata.annotations__ , each with its own purpose. Among them, __insight.opentelemetry.io/metric-port__
specifies the default metric exposure port of OpenTelemetry Agent. If the port conflicts, you can specify a new metric port for your application: __-Dotel.exporter.prometheus.port=8464__ ,
and the port values in other places must also be changed accordingly.


## Exposing Metrics for Java Middleware

OpenTelemetry Agent also provides built-in examples for monitoring middleware. Please refer to the [Predefined Metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#predefined-metrics).

By default, no specific types are designated; you need to specify them using the __-Dotel.jmx.target.system__ JVM Options, for example, __-Dotel.jmx.target.system=jetty,kafka-broker__ .

## References

- [Gaining JMX Metric Insights with the OpenTelemetry Java Agent](https://opentelemetry.io/blog/2023/jmx-metric-insight/)

- [Otel JMX Metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics)
