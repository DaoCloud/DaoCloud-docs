---
hide:
  - toc
---

# 什么是可观测模块

可观测模块 (Insight) 是以应用为中心、开箱即用的新一代云原生可观测性平台。
能够实时监控应用及资源，采集各项指标、日志及事件等数据用来分析应用健康状态，不仅提供告警能力以及全面、清晰、多维度数据可视化能力，兼容主流开源组件，而且提供快捷故障定位及一键监控诊断的能力。

可观测模块实现了指标、日志、链路的统一采集，支持对指标、日志进行多维度的告警并提供简洁明了的可视化管理界面。

## 模块指引

<div class="grid cards" markdown>

- :material-server:{ .lg .middle } __安装与升级__

    ---

    可观测性模块包含 Insight 和 Insight Agent，后者需要部署在被观测的 Kubernetes 上。

    - 部署[资源规划](../quickstart/res-plan/index.md)
    - Insight Agent [安装](../quickstart/install/install-agent.md) 与[升级](../quickstart/install/offline-install.md)
    - Insihgt Agent 安装在 [DCE 4](../quickstart/other/install-agentindce.md) 或 [OpenShift](../quickstart/other/install-agent-on-ocp.md)
    - [大规模日志部署调整](../best-practice/insight-kafka.md)
    - 升级[注意事项](../quickstart/install/upgrade-note.md)

- ::material-auto-fix:{ .lg .middle } __开始观测__

    ---

    使用 OpenTelemetry 技术对您的应用程序进行观测。

    - 了解 [OpenTelemetry](../quickstart/otel/otel.md)，向 Insight [发送观测数据](../quickstart/otel/send_tracing_to_insight.md)
    - 使用[无侵入](../quickstart/otel/operator.md)方式增强应用
    - 针对 [Java 应用观测](../quickstart/otel/java/index.md)
    - 针对 [Golang 应用观测](../quickstart/otel/golang/golang.md)
    - [其他观测技术集成](../best-practice/sw-to-otel.md)

</div>

## 基本概念

可观测性 (Insight) 有关的基本概念如下。

| #    | 术语       | 英文              | 定义                                                         |
| :--- | :--------- | ----------------- | :----------------------------------------------------------- |
| 1    | 监控目标   | Target            | 被监控的对象；系统会定时向监控点发起抓取任务，从中获取指标   |
| 2    | 指标       | Metric            | 使用 [open-metric](https://openmetrics.io/) 格式描述，衡量软件或硬件系统中某种属性的程度的标准 |
| 3    | 自定义指标 | Recording Rule    | 一个被命名的 PromQL 表达式，这是将多个指标通过计算而得到的新指标，用来描述更加完整和复杂的系统状态 |
| 4    | 仪表盘     | Dashboard         | 仪表盘是可视化管理的一种表现形式，即对数据、情报等状况一目了然的表现，它通过形象直观而又色彩适宜的各种视觉感知来展示信息。通过可视化图形展示平台的实时情况和 DCE 中所有的性能指标。 |
| 6    | 服务发现   | Service Discovery | 一个用于 Kubernetes 环境的服务发现配置，用于批量且自动地接入 Kubernetes 上的监控点 |
| 7    | Exporter   | Exporter          | 一个能够提供指标的服务，往往被理解为监控对象                 |
| 8    | 告警规则   | Rule              | 一个返回值是布尔值的 PromQL 表达式，它描述了指标或自定义指标是否处于阈值范围中，如果不满足将产生一条告警事件 |
| 9    | 告警消息   | Alert             | 告警规则被触发时的记录信息，记录了告警规则、触发时间、当前系统状态；同时将触发相应的动作，例如发送邮件 |
| 10   | 通知       | Notification      | 由系统通过邮件等渠道发送给用户的告警事件信息                 |
| 11   | PromQL     | PromQL            | Prometheus 系统所支持的查询语句                              |

[下载 DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../../dce/license0.md){ .md-button .md-button--primary }
