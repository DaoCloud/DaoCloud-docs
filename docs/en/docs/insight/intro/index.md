---
MTPE: windsonsea
date: 2026-11-06
---

# What is Insight

Insight is a next-generation, cloud native observability platform that focuses on application analysis.
Its out-of-the-box real-time resource monitoring, metrics, logs, events, and other data assist enterprises
in analyzing application status. Furthermore, it is compatible with popular open-source components,
providing alerting, multi-dimensional data visualization, fault locating, and one-click monitoring and diagnosis.

Insight implements unified collection of metrics, logs, and traces, supports multi-dimensional alerting
on metrics and logs, and provides a concise and clear visual management interface.

![Insight observability architecture](../images/insight-arch.svg)

## Key Capabilities

<div class="grid cards" markdown>

- :material-monitor-dashboard:{ .lg .middle } __Dashboards__

    ---

    Built-in dashboards based on native Grafana covering platform components, cluster resources, and core components, with support for importing custom templates.

    [:arrow_forward: View dashboards](../user-guide/dashboard/dashboard.md)

- :material-server:{ .lg .middle } __Infrastructure Monitoring__

    ---

    Centralized multi-cluster observability across clusters, nodes, namespaces, and containers, with event query and black-box probing.

    [:arrow_forward: Cluster monitoring](../user-guide/infra/cluster.md)

- :material-chart-line:{ .lg .middle } __Metric & Log Query__

    ---

    Metrics support basic and advanced PromQL queries; logs support keyword search, Lucene syntax, context viewing, and download.

    [:arrow_forward: Metric query](../user-guide/data-query/metric.md)

- :material-transit-connection-variant:{ .lg .middle } __Distributed Tracing__

    ---

    Traces are collected through OpenTelemetry, providing service topology, service lists, and trace analysis for rapid fault locating.

    [:arrow_forward: View traces](../user-guide/trace/trace.md)

- :material-bell-outline:{ .lg .middle } __Alert Center__

    ---

    Over 100 built-in alert rules, custom PromQL rules, message templates, silence and inhibition, with notifications via email, WeChat Work, DingTalk, and more.

    [:arrow_forward: Alert center](../user-guide/alert-center/index.md)

- :material-cog-outline:{ .lg .middle } __Collection & System Config__

    ---

    Manage insight-agent and metric/log collection tasks, and customize the retention duration of metrics, logs, and traces.

    [:arrow_forward: Log collection and query](../user-guide/collection-manag/collection-manag.md)

</div>

## Workflow

Using Insight usually involves two stages: **deployment and integration** followed by **observation and alerting**. Administrators plan resources and install insight-agent; business users then integrate application observability, view dashboards and query data, and configure alerts to detect anomalies in time.

```mermaid
flowchart LR
    A["① Resource planning<br/>Insight · insight-agent"] --> B["② Install insight-agent<br/>Online · offline"]
    B --> C["③ Integrate observability<br/>OpenTelemetry"]
    C --> D["④ Dashboards & queries<br/>Dashboards · metrics · logs"]
    D --> E["⑤ Configure alerts<br/>Rules · notifications"]

    click A href "../quickstart/res-plan/"
    click B href "../quickstart/install/install-agent/"
    click C href "../quickstart/otel/otel/"
    click D href "../user-guide/dashboard/dashboard/"
    click E href "../user-guide/alert-center/alert-policy/"
```

| Step | Role | Description |
| ---- | ---- | ----------- |
| ① [Resource planning](../quickstart/res-plan/index.md) | Platform Administrator | Evaluate the node and storage resources required by Insight and insight-agent |
| ② [Install insight-agent](../quickstart/install/install-agent.md) | Platform Administrator | Install the collection components online or offline on observed clusters, and upgrade as needed |
| ③ [Integrate observability](../quickstart/otel/otel.md) | Business User | Collect traces and metrics through OpenTelemetry (non-intrusive Operator or SDK) |
| ④ [Dashboards & queries](../user-guide/dashboard/dashboard.md) | Business User | Understand application and cluster status through dashboards, metric and log queries |
| ⑤ [Configure alerts](../user-guide/alert-center/alert-policy.md) | Platform Administrator | Create alert rules and notification configs to detect anomalies in time |

## Quick Start

<style>
.insight-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.insight-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.insight-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.insight-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.insight-path-step:last-child::after{display:none}
.insight-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.insight-path-title{font-weight:700;font-size:0.95rem}
.insight-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.insight-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.insight-path-step::after{display:none}}
</style>

<div class="insight-path">
  <a class="insight-path-step" style="--path-c:#2196f3" href="../quickstart/res-plan/">
    <span class="insight-path-num">1</span>
    <span class="insight-path-title">Resource planning</span>
    <span class="insight-path-desc">Evaluate node and storage resources</span>
    <span class="insight-path-go">Go →</span>
  </a>
  <a class="insight-path-step" style="--path-c:#00acc1" href="../quickstart/install/install-agent/">
    <span class="insight-path-num">2</span>
    <span class="insight-path-title">Install insight-agent</span>
    <span class="insight-path-desc">Online · offline installation</span>
    <span class="insight-path-go">Go →</span>
  </a>
  <a class="insight-path-step" style="--path-c:#43a047" href="../quickstart/otel/otel/">
    <span class="insight-path-num">3</span>
    <span class="insight-path-title">Integrate observability</span>
    <span class="insight-path-desc">Non-intrusive OpenTelemetry</span>
    <span class="insight-path-go">Go →</span>
  </a>
  <a class="insight-path-step" style="--path-c:#fb8c00" href="../user-guide/dashboard/dashboard/">
    <span class="insight-path-num">4</span>
    <span class="insight-path-title">View dashboards</span>
    <span class="insight-path-desc">Metrics · logs · traces</span>
    <span class="insight-path-go">Go →</span>
  </a>
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

## More Resources

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __Feature List__

    ---

    A complete list of Insight features across dashboards, infrastructure, metrics and logs, tracing, and the alert center.

    [:arrow_forward: View the feature list](features.md)

- :material-map-outline:{ .lg .middle } __Use Cases__

    ---

    Learn about unified multi-cluster data collection and observability, rapid fault locating and troubleshooting, and other typical use cases.

    [:arrow_forward: View use cases](scenarios.md)

- :material-star-outline:{ .lg .middle } __Benefits__

    ---

    Learn about the advantages of Insight in unified collection, out-of-the-box experience, and ecosystem compatibility.

    [:arrow_forward: View benefits](benefits.md)

- :material-shield-account-outline:{ .lg .middle } __Permissions__

    ---

    Learn about the user roles and permissions required for each Insight feature.

    [:arrow_forward: View permissions](permission.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
[View the Insight User Manual (PDF)](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/insight.pdf){ .md-button .md-button--primary }
