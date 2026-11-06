---
MTPE: windsonsea
date: 2026-11-06
---

# Insight Reference

This page lists reference documentation for the observability module (Insight), covering alert notifications, data collection, query syntax, and security integration.

## Alerts and Notifications

<div class="grid cards" markdown>

- :material-bell-outline:{ .lg .middle } __Alert Notification Process Description__

    ---

    The full path from alert triggering to delivery.

    [:arrow_forward: View details](alertnotification.md)

- :material-email-edit-outline:{ .lg .middle } __Configure Notification Templates__

    ---

    Customize message templates for email, WeChat Work, DingTalk, and more.

    [:arrow_forward: View details](notify-helper.md)

- :material-send-outline:{ .lg .middle } __Alertmanager Sends Alert Notifications Individually__

    ---

    Push alert messages one by one.

    [:arrow_forward: View details](send-alert-notifications-individually.md)

</div>

## Trace and Log Collection

<div class="grid cards" markdown>

- :material-server-network:{ .lg .middle } __Create a Remote Sampling Server__

    ---

    Deploy a remote sampling service for trace data.

    [:arrow_forward: View details](remote-sampling.md)

- :material-chart-areaspline:{ .lg .middle } __Enable Span Metrics Alert Rules__

    ---

    Configure alerts based on span metrics.

    [:arrow_forward: View details](span-metrics-alert.md)

- :material-package-variant:{ .lg .middle } __Collecting Container Logs through Sidecar__

    ---

    Log collection for containers without shared storage volumes.

    [:arrow_forward: View details](tailing-sidecar.md)

</div>

## Query Syntax and Metrics

<div class="grid cards" markdown>

- :material-text-search:{ .lg .middle } __Lucene Syntax Usage__

    ---

    Advanced query syntax for logs.

    [:arrow_forward: View details](lucene.md)

- :material-numeric:{ .lg .middle } __Insight Reference Metrics__

    ---

    Meanings and usage of built-in metrics.

    [:arrow_forward: View details](used-metric-in-insight.md)

</div>

## Security and Integration

<div class="grid cards" markdown>

- :material-lock-outline:{ .lg .middle } __Secure Connection from Insight and insight-agent to Kafka__

    ---

    Authentication for feeding collected data into Kafka.

    [:arrow_forward: View details](security-connect-kafka.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
