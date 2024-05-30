# 使用 OpenTelemetry Java Agent 暴露 JVM 监控指标

在 Opentelemetry Agent v1.20.0 及以上版本中，Opentelemetry Agent 新增了 JMX Metric Insight 模块，如果你的应用已经集成了 Opentelemetry Agent 去采集应用链路，那么你不再需要另外引入其他 Agent 去为我们的应用暴露 JMX 指标。Opentelemetry Agent 也是通过检测应用程序中本地可用的 MBean 公开的指标，对其进行收集并暴露指标。

Opentelemetry Agent 也针对常见的 Java Server 或框架内置了一些监控的样例，请参考[预定义的指标](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/semantic-conventions.md)。

使用 OpenTelemetry Java Agent 同样需要考虑如何将 JAR 挂载进容器，除了可以参考上面 JMX Exporter 挂载 JAR 文件的方式外，我们还可以借助 Opentelemetry 提供的 Operator 的能力来实现自动为我们的应用开启 JVM 指标暴露：

如果你的应用已经集成了 Opentelemetry Agent 去采集应用链路，那么你不再需要另外引入其他 Agent 去为我们的应用暴露 JMX 指标。Opentelemetry Agent 通过检测应用程序中本地可用的 MBean 公开的指标，现在可以本地收集并暴露指标接口。

但是，截至目前版本，你仍然需要手动为应用加上相应注解之后，JVM 数据才会被 Insight 采集到，具体注解内容请参考 [已有 JVM 指标的 Java 应用对接可观测性](./legacy-jvm.md)。

## 为 Java 中间件暴露指标

Opentelemetry Agent 也内置了一些中间件监控的样例，请参考 [预定义指标](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/jmx-metrics/javaagent/README.md#predefined-metrics)。

默认没有指定任何类型，需要通过 __-Dotel.jmx.target.system__ JVM Options 指定,比如 __-Dotel.jmx.target.system=jetty,kafka-broker__ 。

## 参考

- [Gaining JMX Metric Insights with the OpenTelemetry Java Agent](https://opentelemetry.io/blog/2023/jmx-metric-insight/)

- [Otel jmx metrics](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/jmx-metrics)
