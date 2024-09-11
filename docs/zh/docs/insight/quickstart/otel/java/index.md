# 开始监控 Java 应用

1. Java 应用链路接入与监控请参考 [通过 Operator 实现应用程序无侵入增强](../operator.md) 文档，通过注解实现自动接入链路。

2. Java 应用的 JVM 进行监控：已经暴露 JVM 指标和仍未暴露 JVM 指标的 Java 应用如何与可观测性 Insight 对接。

- 如果您的 Java 应用未开始暴露 JVM 指标，您可以参考如下文档：

    - [使用 JMX Exporter 暴露 JVM 监控指标](./jvm-monitor/jmx-exporter.md)
    - [使用 OpenTelemetry Java Agent 暴露 JVM 监控指标](./jvm-monitor/otel-java-agent.md)

- 如果您的 Java 应用已经暴露 JVM 指标，您可以参考如下文档：
    
    - [已有 JVM 指标的 Java 应用对接可观测性](./jvm-monitor/legacy-jvm.md)

3. [将 TraceId 和 SpanId 写入 Java 应用日志](./mdc.md), 实现链路数据与日志数据关联
