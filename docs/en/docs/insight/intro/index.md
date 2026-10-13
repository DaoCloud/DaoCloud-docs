---
MTPE: windsonsea
date: 2024-05-13
---

# What is Insight

Insight is a next-generation, cloud native observability platform that focuses on application analysis.
Its out-of-the-box real-time resource monitoring, metrics, logs, events, and other data assist enterprises
in analyzing application status. Furthermore, it is compatible with popular open-source components,
providing alerting, multi-dimensional data visualization, fault locating, and one-click monitoring and diagnosis.

Insight implements unified collection of metrics, logs, and traces, supports multi-dimensional alerting
on metrics and logs, and provides a concise and clear visual management interface.

## Module Guide

<div class="grid cards" markdown>

- :material-server:{ .lg .middle } __Installation and Upgrades__

    ---

    The observability module includes Insight and Insight Agent, the latter of which needs to be deployed on the Kubernetes being observed.

    - Deployment [Resource Planning](../quickstart/res-plan/index.md)
    - Insight Agent [Installation](../quickstart/install/install-agent.md) and [Upgrade](../quickstart/install/offline-install.md)
    - Insight Agent installed on [DCE 4](../quickstart/other/install-agentindce.md) or [OpenShift](../quickstart/other/install-agent-on-ocp.md)
    - [Large-scale Log Deployment Adjustments](../best-practice/insight-kafka.md)
    - Upgrade [Considerations](../quickstart/install/upgrade-note.md)

- ::material-auto-fix:{ .lg .middle } __Start Observing__

    ---

    Use OpenTelemetry technology to observe your applications.

    - Understand [OpenTelemetry](../quickstart/otel/otel.md) and [send observability data](../quickstart/otel/send_tracing_to_insight.md) to Insight
    - Enhance applications in a [non-intrusive](../quickstart/otel/operator.md) manner
    - Observability for [Java Applications](../quickstart/otel/java/index.md)
    - Observability for [Golang Applications](../quickstart/otel/golang/golang.md)
    - [Integrating Other Observability Technologies](../best-practice/index.md)

</div>

## Basic concepts

The basic concepts related to observability (Insight) are as follows.

| # | Terms | Definitions |
| - | ----- | ---------- |
| 1 | Target | The monitored object; the system will regularly initiate capture tasks to the monitoring point to obtain metrics |
| 2 | Metric | Use the [open-metric](https://openmetrics.io/) format description to measure the degree of a certain attribute in a software or hardware system |
| 3 | Recording Rule | A named PromQL expression, which is a new metric obtained by calculating multiple metrics to describe a more complete and complex system state |
| 4 | Dashboard | Dashboard is a form of visual management, that is, the performance of data, intelligence and other conditions at a glance. It displays information through various visual perceptions with intuitive images and appropriate colors. Display the real-time situation of the platform and all performance metrics in DCE through visual graphics. |
| 6 | Service Discovery | A service discovery configuration for Kubernetes environment, used to batch and automatically access monitoring points on Kubernetes |
| 7 | Exporter | A service that can provide metrics, often understood as a monitoring object |
| 8 | Rule | A PromQL expression whose return value is a Boolean value, which describes whether the metric or custom metric is within the threshold range, and if not, an alert event will be generated |
| 9 | Alert | The record information when the alert rule is triggered, which records the alert rule, trigger time, and current system status; at the same time, it will trigger the corresponding action, such as sending an email |
| 10 | Notification | The alert event information sent by the system to the user through e-mail or other channels |
| 11 | PromQL | Query statements supported by the Prometheus system |

[Download DCE](../../download/index.md){ .md-button .md-button--primary }
[Install DCE](../../install/index.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }
