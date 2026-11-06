---
hide:
  - toc
MTPE: windsonsea
date: 2026-11-06
---

# Insight FAQs

This page collects common issues and troubleshooting guides for the observability module (Insight). Before installation, it is recommended to read [Resource Planning](../quickstart/res-plan/index.md) and [insight-agent Installation](../quickstart/install/install-agent.md).

## Alerts

<div class="grid cards" markdown>

- :material-bell-ring-outline:{ .lg .middle } __Prometheus Cluster Label Configuration__

    ---

    Mapping between cluster IDs and names in alert information.

    [:arrow_forward: View details](alertinfo-trans-clusterid-to-name.md)

- :material-bell-plus-outline:{ .lg .middle } __Enabling Insight Alert Notifications v1alpha2__

    ---

    Notes on the alert notification API version upgrade.

    [:arrow_forward: View details](alertnotify-enable-v2api.md)

</div>

## Logs

<div class="grid cards" markdown>

- :material-database-outline:{ .lg .middle } __What to Do When ElasticSearch is Full?__

    ---

    Steps to handle a full ES storage.

    [:arrow_forward: View details](expand-once-es-full.md)

- :material-filter-outline:{ .lg .middle } __Container Log Blacklist__

    ---

    Exclude container logs that do not need to be collected.

    [:arrow_forward: View details](ignore-pod-log-collect.md)

- :material-tune-vertical:{ .lg .middle } __Optimizing Logstash Parameters__

    ---

    Tuning Logstash for large-scale log scenarios.

    [:arrow_forward: View details](logstash-optimize.md)

- :simple-apachekafka:{ .lg .middle } __Fluent Bit Routes Logs by Namespace__

    ---

    Split logs into different Kafka topics based on the Kubernetes namespace name.

    [:arrow_forward: View details](fluentbit-dynamic-kafka-topic.md)

- :material-desktop-classic:{ .lg .middle } __Fluent Bit Fails to Start on NeoKylin Linux V10__

    ---

    Compatibility issue on Kylin operating systems.

    [:arrow_forward: View details](kylin-fluentbit.md)

</div>

## Traces

<div class="grid cards" markdown>

- :material-clock-fast:{ .lg .middle } __Clock Offset in Trace Data__

    ---

    Trace data anomalies caused by unsynchronized clocks across clusters.

    [:arrow_forward: View details](traceclockskew.md)

</div>

## Troubleshooting

<div class="grid cards" markdown>

- :material-bug-outline:{ .lg .middle } __Log Collection Troubleshooting Guide__

    ---

    Diagnostic approach and steps for log collection issues.

    [:arrow_forward: View details](../best-practice/debug-log.md)

- :material-radar:{ .lg .middle } __Trace Collection Troubleshooting Guide__

    ---

    How to troubleshoot missing or abnormal trace data.

    [:arrow_forward: View details](../best-practice/debug-trace.md)

- :material-target:{ .lg .middle } __Locating Anomalies with Insight__

    ---

    Rapidly locate application issues using metrics, logs, and traces.

    [:arrow_forward: View details](../best-practice/find_root_cause.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
