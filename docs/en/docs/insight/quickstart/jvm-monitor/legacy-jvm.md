---
MTPE: ModetaNiu
DATE: 2024-08-14
---

# Java Application with JVM Metrics to Dock Insight 

If your Java application exposes JVM monitoring metrics through other means (such as Spring Boot Actuator),
We need to allow monitoring data to be collected. You can let Insight collect existing JVM metrics by 
adding Kubernetes Annotations to the workload:

```yaml
annatation:
   insight.opentelemetry.io/metric-scrape: "true" # whether to collect
   insight.opentelemetry.io/metric-path: "/" # path to collect metrics
   insight.opentelemetry.io/metric-port: "9464" # port for collecting metrics
```

YAML Example to add annotations for __my-deployment-app__ workload： 

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
        insight.opentelemetry.io/metric-scrape: "true" # whether to collect
        insight.opentelemetry.io/metric-path: "/" # path to collect metrics
        insight.opentelemetry.io/metric-port: "9464" # port for collecting metrics
```

The following shows the complete YAML: 

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
        insight.opentelemetry.io/metric-scrape: "true" # whether to collect
        insight.opentelemetry.io/metric-path: "/actuator/prometheus"      # path to collect metrics
        insight.opentelemetry.io/metric-port: "8080"   # port for collecting metrics
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

In the above example，Insight will use __:8080//actuator/prometheus__ to get Prometheus metrics exposed through *Spring Boot Actuator* .
