# 集成其他观测技术
Insight 底层采用标准 OTel 技术以及标准 OTLP 协议，可以兼容任意符合 OTLP 协议的观测数据，包括但不限于如下集成能力：

- 使用 OpenTelemetry 零代码接收 SkyWalking 链路数据：[接收 Skywalking Agent链路数据](./sw-to-otel.md)
- 实现 Nginx Ingress 的链路追踪：[接入 Nginx Ingress 的链路追踪](./ingress-otel.md)

[下载中心](https://docs.daocloud.io/download/){ .md-button .md-button--primary }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button .md-button--primary }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button .md-button--primary }
