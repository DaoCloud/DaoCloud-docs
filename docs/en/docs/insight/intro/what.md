# What is Insight？

The application Insight is a new generation cloud native Insight platform that focuses on applications analyzing. It provides the out-of-the-box real-time resources monitoring, metrics, logs, events and other data to help you analyzing  application status. In additionally, it is compatible with popular open source components, and provides alerting, multi-dimensions data visualization, fault locating,one-click monitoring and diagnosing capabilities.

The insight implements the unified collection of metrics, logs and traces, which supports multi-dimensions alerting on metrics, logs, and provides you a web UI.

The main functions as following:

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

## Basic concepts

The basic concepts related to observability (Insight) are as follows.

| # | Terms | Definitions |
| :--- | ----------------- | :------------- ------------------------------------------------ |
| 1 | Target | The monitored object; the system will regularly initiate capture tasks to the monitoring point to obtain indicators |
| 2 | Metric | Use the [open-metric](https://openmetrics.io/) format description to measure the degree of a certain attribute in a software or hardware system |
| 3 | Recording Rule | A named PromQL expression, which is a new indicator obtained by calculating multiple indicators to describe a more complete and complex system state |
| 4 | Dashboard | Dashboard is a form of visual management, that is, the performance of data, intelligence and other conditions at a glance. It displays information through various visual perceptions with intuitive images and appropriate colors. Display the real-time situation of the platform and all performance indicators in DCE through visual graphics. |
| 6 | Service Discovery | A service discovery configuration for Kubernetes environment, used to batch and automatically access monitoring points on Kubernetes |
| 7 | Exporter | A service that can provide indicators, often understood as a monitoring object |
| 8 | Rule | A PromQL expression whose return value is a Boolean value, which describes whether the indicator or custom indicator is within the threshold range, and if not, an alarm event will be generated |
| 9 | Event | The record information when the alarm rule is triggered, which records the alarm rule, trigger time, and current system status; at the same time, it will trigger the corresponding action, such as sending an email |
| 10 | Notification | The alarm event information sent by the system to the user through e-mail or other channels |
| 11 | PromQL | Query statements supported by the Prometheus system |

[Download DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }

