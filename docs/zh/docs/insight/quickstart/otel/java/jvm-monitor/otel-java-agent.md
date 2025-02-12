# 使用 OpenTelemetry Java Agent 暴露 JVM 监控指标

在 Opentelemetry Agent v1.20.0 及以上版本中，Opentelemetry Agent 新增了 [JMX Metric Insight](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#jmx-metric-insight) 模块，
它也是通过检测应用程序中本地可用的 MBean 公开的指标，对其进行收集并暴露指标，它还针对常见的 Java Server 或框架内置了一些监控的样例，请参考[预定义的指标](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#predefined-metrics)。
如果你的应用已经通过 Opentelemetry Operator 将 Opentelemetry Agent 自动注入到了你的应用中了，那么你不再需要另外引入其他 Agent 去为我们的应用暴露 JMX 指标。比如以下 Demo:

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
        instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation" # 注入 otel agent 需要
        # 以下是指标采集需要的 3 个注解
        insight.opentelemetry.io/metric-scrape: "true" # 是否采集
        insight.opentelemetry.io/metric-path: "/metrics"      # 采集指标的路径
        insight.opentelemetry.io/metric-port: "9464"   # 采集指标的端口
    spec:
      containers:
      - name: myapp
        image: jaegertracing/vertx-create-span:operator-e2e-tests
        ports:
          - containerPort: 8080
            protocol: TCP
          - containerPort: 9464 # 容器也需要对应暴露 9464 端口，同时 Deployment 对应的 SVC 也需要申明 9464 端口
            protocol: TCP
```

在以上的 Deployment 中，我们在 __template.metadata.annotations__ 下添加了四个注解，它们各种有自己的作用。其中的 __insight.opentelemetry.io/metric-port__
指定的就是 Opentelemetry Agent 默认的指标暴露端口。如果端口发生了冲突，你可以给你的应用指定一个新的指标端口: __-Dotel.exporter.prometheus.port=8464__，
在改动后其他位置的的端口值也要一并修改。


## 为 Java 中间件暴露指标

Opentelemetry Agent 也内置了一些中间件监控的样例，请参考 [预定义指标](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#predefined-metrics)。

默认没有指定任何类型，需要通过 __-Dotel.jmx.target.system__ JVM Options 指定,比如 __-Dotel.jmx.target.system=jetty,kafka-broker__ 。

## 参考

- [Gaining JMX Metric Insights with the OpenTelemetry Java Agent](https://opentelemetry.io/blog/2023/jmx-metric-insight/)

- [Otel jmx metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics)
