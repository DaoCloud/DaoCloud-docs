# Java application docking observability with existing JVM metrics

If your Java application exposes JVM monitoring indicators through other means (such as Spring Boot Actuator),
We need to allow monitoring data to be collected. You can let Insight collect existing JVM metrics by adding annotations (Kubernetes Annotations) to the workload:

```yaml
annatation:
   insight.opentelemetry.io/metric-scrape: "true" # whether to collect
   insight.opentelemetry.io/metric-path: "/" # path to collect metrics
   insight.opentelemetry.io/metric-port: "9464" # port for collecting metrics
```