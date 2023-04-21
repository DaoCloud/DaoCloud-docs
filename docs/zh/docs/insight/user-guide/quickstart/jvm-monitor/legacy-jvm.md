# 已有 JVM 指标的 Java 应用对接可观测性

如果您的 Java 应用通过其他方式（比如 Spring Boot Actuator）暴露了 JVM 的监控指标，
我们需要让监控数据被采集到。您可以通过在工作负载种添加注解（Kubernetes Annotations）的方式让 Insight 来采集已有的 JVM 指标：

```yaml
annatation: 
  insight.opentelemetry.io/metric-scrape: "true" # 是否采集
  insight.opentelemetry.io/metric-path: "/"      # 采集指标的路径
  insight.opentelemetry.io/metric-port: "9464"   # 采集指标的端口
```