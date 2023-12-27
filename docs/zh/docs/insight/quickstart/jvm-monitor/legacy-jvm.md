# 已有 JVM 指标的 Java 应用对接可观测性

如果您的 Java 应用通过其他方式（比如 Spring Boot Actuator）暴露了 JVM 的监控指标，
我们需要让监控数据被采集到。您可以通过在工作负载种添加注解（Kubernetes Annotations）的方式让 Insight 来采集已有的 JVM 指标：

```yaml
annatation: 
  insight.opentelemetry.io/metric-scrape: "true" # 是否采集
  insight.opentelemetry.io/metric-path: "/"      # 采集指标的路径
  insight.opentelemetry.io/metric-port: "9464"   # 采集指标的端口
```

例如为 `my-deployment-app` 添加注解： 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment-app
spec:
  selector:
    matchLabels:
      app: my-deployment-app
      app.kubernetes.io/name: my-deployment-app
  replicas: 1
  template:
    metadata:
      labels:
        app: my-deployment-app
        app.kubernetes.io/name: my-deployment-app
      annotations:
        insight.opentelemetry.io/metric-scrape: "true" # 是否采集
        insight.opentelemetry.io/metric-path: "/"      # 采集指标的路径
        insight.opentelemetry.io/metric-port: "9464"   # 采集指标的端口
```

以下是完整示例：

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: spring-boot-actuator-prometheus-metrics-demo
spec:
  type: NodePort
  selector:
    #app: my-deployment-with-aotu-instrumentation-app
    app.kubernetes.io/name: spring-boot-actuator-prometheus-metrics-demo
  ports:
    - name: http
      port: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-boot-actuator-prometheus-metrics-demo
spec:
  selector:
    matchLabels:
      #app: my-deployment-with-aotu-instrumentation-app
      app.kubernetes.io/name: spring-boot-actuator-prometheus-metrics-demo
  replicas: 1
  template:
    metadata:
      labels:
        app.kubernetes.io/name: spring-boot-actuator-prometheus-metrics-demo
      annotations:
        insight.opentelemetry.io/metric-scrape: "true" # 是否采集
        insight.opentelemetry.io/metric-path: "/actuator/prometheus"      # 采集指标的路径
        insight.opentelemetry.io/metric-port: "8080"   # 采集指标的端口
    spec:
      containers:
        - name: myapp
          image: docker.m.daocloud.io/wutang/spring-boot-actuator-prometheus-metrics-demo
          ports:
            - name: http
              containerPort: 8080
          resources:
            limits:
              cpu: 500m
              memory: 800Mi
            requests:
              cpu: 200m
              memory: 400Mi
```

以上示例中，Insight 会通过 `:8080//actuator/prometheus` 抓取通过 *Spring Boot Actuator* 暴露出来的 Prometheus 指标。
