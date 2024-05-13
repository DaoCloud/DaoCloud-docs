---
MTPE: windsonsea
date: 2024-05-13
---

# What is Insight？

Insight is a next-generation, cloud native observability platform that focuses on application analysis.
Its out-of-the-box real-time resource monitoring, metrics, logs, events, and other data assist enterprises
in analyzing application status. Furthermore, it is compatible with popular open-source components,
providing alerting, multi-dimensional data visualization, fault locating, and one-click monitoring and diagnosis.

Insight implements unified collection of metrics, logs, and traces, which supports multi-dimension alerting
on metrics and logs. The platform offers a web UI for enterprises to easily navigate. It provides several
monitoring components, including multi-dimensional monitoring of containers, services, nodes, and clusters,
and monitors CPU, memory, storage, and network resources. The integration with Grafana enables the creation of
comprehensive dashboards.

The platform allows for collection and search of workload logs, system logs, Kubernetes events,
and context log queries. It supports service topology visualization and transparent tracing,
including real-time service metrics, request per second, error rates, and latency. The platform
supports distributed tracing based on open-source technologies and comes with pre-defined alerting rules,
while also enabling users to define their metrics, logs, and alerts.

Insight provides flexible configuration options for alerting rules, and notifications can be sent
via multiple channels such as email, WeChat, and Webhook. It ensures the persistence of metrics,
logs and tracing data, catering to the data storage needs of enterprises.

The main features as following:

- Provide multi-dimensional monitoring of containers, services, nodes and clusters.
- CPU, memory, storage, network monitoring.
- Integrated with grafana to provide comprehensive dashboards.
- Collect and search workloads logs, system logs and kubernetes events.
- Contextual logs query.
- Services topology.
- Transparence tracing supports, fully supported services real-time RPS, error rates, and latency metrics.
- Open source based distributed tracing.
- Out-of-the-box alerting rules.
- User-defined metics, logs and other alerts.
- Flexible configuration of alerting rules.
- Multiple notification channels, such as email, WeChat, nail and Webhook.
- Persistence of metics, logs, and tracing data.

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

    - Understand [OpenTelemetry](../quickstart/otel/otel.md), send observability data to Insight [Sending Observability Data](../quickstart/otel/send_tracing_to_insight.md)
    - Enhance applications in a [non-intrusive](../quickstart/otel/operator.md) manner
    - Observability for [Java Applications](../quickstart/jvm-monitor/jvm-catelogy.md)
    - Observability for [Golang Applications](../quickstart/otel/golang.md)
    - [Integrating Other Observability Technologies](../best-practice/sw-to-otel.md)

</div>

## Basic concepts

The basic concepts related to observability (Insight) are as follows.

| # | Terms | Definitions |
| :--- | ----------------- | :------------- ------------------------------------------------ |
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

[Download DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }
