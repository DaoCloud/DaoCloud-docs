---
MTPE: FanLin
Date: 2024-01-22
---

# Features

This page lists the features supported by Insight.

| Category | Subcategory  | Description | DCE 5.0 Community | DCE 5.0 Enterprise |
| -------- | ------------ | ----------- | ----------- | ----------- |
| Dashboard | Platform Components | Provides open source selected dashboards through native Grafana, provides built-in dashboards to support monitoring of etcd, APIServer and other components. | ✓ | ✓ |
|  | Cluster Resources | Provides monitoring for multiple dimensions such as clusters, nodes, namespaces, etc. The data source used by Grafana supports viewing data from multiple clusters. | ✓ | ✓ |
| Infrastructure | Multiclusters | Provides centralized insight of multi-cluster business<br />Admins manage multicluster alerts uniformly, and meet the data isolation of cluster and tenant administrators<br />Supports persistent metrics and log data of clusters. | ✓ | ✓ |
|  | Clusters | Provides an overview of a single cluster's insight, allowing to view the running status of the cluster, understand the resource usage of the cluster, and the current alerts occurring in the cluster. | ✓ | ✓ |
|  | Nodes | Supports viewing the running status of nodes, and understanding the changes in CPU, memory, network and other resources of the node. | ✓ | ✓ |
|  | Namespaces | Supports viewing the number of resources running in the namespace, and the total amount of CPU and memory used by the Pods in the namespace. | ✓ | ✓ |
|  | Workloads | Supports monitoring resources such as stateless loads, daemonsets, Pods, etc. You can monitor the running status of this workload, view the number of alerts in progress, and the trend chart of changes in CPU, memory and other resource consumption. | ✓ | ✓ |
|  | Events | Supports viewing the collection of Kubernetes events generated in the cluster, and supports querying by event type, object, reason, etc. | ✓ | ✓ |
|  | Probe | Regularly performs connectivity tests on targets through black box monitoring using methods such as HTTP and TCP, quickly discovering ongoing faults. | ✓ | ✓ |
| Metrics | General Query | Pre-orders basic metrics. After selecting cluster, type, node, metric name, etc., you can query the changing trend of resources. | ✓ | ✓ |
|  | Advanced Query | Supports querying metric charts and data details using native PromQL statements. | ✓ | ✓ |
| Logs | General Query | Can query logs for Node, Pod, Deployment, StatefulSet, etc., and can query the contextual content of a single log<br />Supports searching by keyword<br />Sorted by time by default, log quantity changes can be queried through histograms. | ✓ | ✓ |
|  | Advanced Query | Supports native lucene syntax for quickly querying target logs. | ✓ | ✓ |
|  | Log Context | Clicking the icon on the right side of a single log line can view the contextual information of that log line. | ✓ | ✓ |
|  | Log Download | Supports downloading logs for a period of time<br />Supports exporting the content of a single log context<br />Supports customizing the fields for log download. | ✓ | ✓ |
| Trace Tracking | Service Map | Administrators can view the call relationship and health status of services that have accessed Insight and have enabled distributed tracing, allowing for quick fault location<br />Can view the traffic direction and key metrics of requests between services<br />Can quickly view the real-time throughput, number of requests, request delay, and error rate of a single service. |  | ✓ |
|  | Services | Can view the list of services currently accessing the tracing data, as well as the throughput rate, error rate, and request delay of the services in the last 15 minutes<br />Clicking a service allows you to view the traffic trend of the selected service in the last 15 minutes and the aggregated metrics for the service's operations. |  | ✓ |
|  | Traces | By default, queries all requests, request status, delay, span count, etc. for the selected service in the last 15 minutes<br />Clicking the icon on the right side of the list allows you to query the related container logs and trace logs for that trace. |  | ✓ |
| Alert | Active Alerts | Provides a histogram to view the changing trend of alert time<br />Supports viewing all active rules and details. | ✓ | ✓ |
|  | Historical Alerts | Can query all alerts that have been automatically recovered or manually resolved. | ✓ | ✓ |
|  | Alert Policy | Built-in 100+ alert rules provide predefined alert rules for cluster components, container resources, etc.<br />Administrators can create global alert rules for clusters with installed insight agents for unified alert management<br />Supports creating alert rules using predefined metrics<br />Supports creating alert rules using PromQL statements<br />Supports customizing thresholds, duration, and notification methods<br />Can customize the level of alerts, supporting urgent, warning, and informational levels. | ✓ | ✓ |
|  | Notification Settings | On this page, you can configure sending messages to users through email groups, WeChat Work, DingTalk, Webhook, etc.<br />Supports notifying multiple alert objects simultaneously. | ✓ | ✓ |
|  | Message Templates | The message template feature supports customizing the content of message templates and can notify specified objects through email, WeChat Work, DingTalk, Webhook, etc. | ✓ | ✓ |
|  | Alert Silence | By configuring silence rules, you can stop receiving alert notifications during specified time periods. | ✓ | ✓ |
|  | Alert Suppression | By configuring suppression rules, you can suppress or block other alert notifications related to certain specific alerts. | ✓ | ✓ |
| | Alert Template | Supports alert templates. The platform administrator can create alert templates and rules. The business side can directly use the alert templates to create alert strategies. | ✓ | ✓ |
| Data Collection | Unified Log Collection | Unified collection of log data from nodes, containers, container internals, and k8s events<br />By default, collects audit logs from the global management platform, k8s audit logs are not enabled by default. | ✓ | ✓ |
|  | Log Persistent Storage | Logs can be labeled and output to middleware such as Elasticsearch for persistent storage. | ✓ | ✓ |
| Metric Collection | Metric Data Collection | Supports defining the namespace scope for pod discovery and selecting the services to monitor using matchLabels through ServiceMonitor | ✓ | ✓ |
| System Management | System Settings | System settings display the default storage duration for metrics, logs, and traces, as well as the default Apdex threshold<br />Supports customizing the storage time for metrics, logs, and traces. | ✓ | ✓ |
|  | System Components | Provides unified monitoring of observable components, real-time detection of the health status of system components. | ✓ | ✓ |
