---
MTPE: windsonsea
Date: 2024-10-16
---

# Integrating Existing JVM Metrics of Java Applications with Observability

If your Java application exposes JVM monitoring metrics through other means (such as Spring Boot Actuator), you will need to ensure that the monitoring data is collected. You can achieve this by adding annotations (Kubernetes Annotations) to your workload to allow Insight to scrape the existing JVM metrics:

```yaml
annotations: 
  insight.opentelemetry.io/metric-scrape: "true"  # Whether to scrape
  insight.opentelemetry.io/metric-path: "/"         # Path to scrape metrics
  insight.opentelemetry.io/metric-port: "9464"      # Port to scrape metrics
```

For example, to add annotations to the **my-deployment-app**:

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
        insight.opentelemetry.io/metric-scrape: "true"  # Whether to scrape
        insight.opentelemetry.io/metric-path: "/"         # Path to scrape metrics
        insight.opentelemetry.io/metric-port: "9464"      # Port to scrape metrics
```

Here is a complete example:

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: spring-boot-actuator-prometheus-metrics-demo
spec:
  type: NodePort
  selector:
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
      app.kubernetes.io/name: spring-boot-actuator-prometheus-metrics-demo
  replicas: 1
  template:
    metadata:
      labels:
        app.kubernetes.io/name: spring-boot-actuator-prometheus-metrics-demo
      annotations:
        insight.opentelemetry.io/metric-scrape: "true"  # Whether to scrape
        insight.opentelemetry.io/metric-path: "/actuator/prometheus"  # Path to scrape metrics
        insight.opentelemetry.io/metric-port: "8080"      # Port to scrape metrics
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

In the above example, Insight will scrape the Prometheus metrics exposed through **Spring Boot Actuator** via `http://<service-ip>:8080/actuator/prometheus`.
