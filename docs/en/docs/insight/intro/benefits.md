---
MTPE: windsonsea
date: 2024-05-13
hide:
  - toc
---

# Advantages of Insight

- Multi-cluster Management

    By using a global service cluster to uniformly store metrics, logs, and trace data, unified monitoring of multiple clusters is achieved. Users can query data across multiple clusters.

- Out-of-the-box

    - Open Source Curated Dashboards: Insight provides a variety of ready-to-use pre-built monitoring dashboards, allowing comprehensive monitoring of clusters, nodes, workloads, and other components through built-in dashboards.
    - Built-in Alert Rules: Insight offers built-in alert rules, enabling out-of-the-box monitoring of basic metrics for cluster resources and system components without any configuration.

- High Availability

    - Lightweight Agent, supports one-click installation via Helm.
    - Data storage components support multiple replicas to ensure high availability of data.

- Open Source Compatibility

    - Compatible with standard open-source Prometheus, supports native PromQL queries for metric data.
    - Compatible with standard open-source __Prometheus.yaml__ collection rule configuration files, suitable for customizing monitoring collection rules within Kubernetes via ServiceMonitor.
    - Adheres to the open-source OpenTelemetry specification, supporting the integration of Jaeger trace data.
