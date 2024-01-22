---
MTPE: FanLin
Date: 2024-01-22
---

# Features

This page lists the features supported by Insight.

## DCE 5.0 Community - Insight

DCE 5.0 Community provides the following Insight features.

| Category | Subcategory  | Description |
| -------- | ------------ | ----------- |
| Infrastructure | Multicluster Insight | Provides centralized insight of multi-cluster business<br />Admins manage multicluster alerts uniformly, and meet the data isolation of cluster and tenant administrators<br />Supports persistent metrics and log data of clusters. |
| | Cluster Insight | Provides an overview of a single cluster's insight, allowing to view the running status of the cluster, understand the resource usage of the cluster, and the current alerts occurring in the cluster |
| | Node Insight | Supports viewing the running status of nodes, and understanding the changes in CPU, memory, network and other resources of the node |
| | Namespace Insight | Supports viewing the number of resources running in the namespace, and the total amount of CPU and memory used by the Pods in the namespace. |
| | Container Insight | Supports monitoring resources such as stateless loads, daemonsets, Pods, etc. You can monitor the running status of this workload, view the number of alerts in progress, and the trend chart of changes in CPU, memory and other resource consumption |
| Dashboard | Platform Component Insight | Provides open source selected dashboards through native Grafana, provides built-in dashboards to support monitoring of etcd, APIServer and other components |
| | Cluster Resource Insight | Provides monitoring for multiple dimensions such as clusters, nodes, namespaces, etc. The data source used by Grafana supports viewing data from multiple clusters. |
| Data Query | Metric Query | The normal query has reserved basic metrics, and the resource change trend can be queried after selecting the cluster, type, node, metric name and other query conditions<br />Supports querying metric charts and data details through native PromQL statements |
| | Log Query | Can query logs of Node, Pod, Depoyment, Statefulset, etc. and can query the context content of a single log<br />Supports searching by keywords<br />Default sorted by time, the log quantity change trend can be queried through histogram<br />Supports querying detailed information and context of a single log |
| | Log Download | Supports downloading logs within a period of time according to search conditions<br />Supports exporting the context content of a single log |
| Alert Center | Active Alerts | Provides histogram to view the change trend of alert time<br />Supports viewing all rules and details that are currently alerting |
| | Historical Alerts | Can query all alerts that have been automatically recovered or manually resolved |
| | Alert Rules | Built-in 100+ alert rules, provides predefined alert rules for cluster components, container resources, etc.<br />Administrators can create global alert rules and uniformly alert clusters that have installed Insight-agent<br />Supports creating alert rules through predefined metrics<br />Supports creating alert rules by writing PromQL statements<br />Supports customizing threshold, duration and notification method<br />Can customize the level of alerts, supports three levels: emergency, warning, prompt |
| | Notification Settings | On the notification settings page, you can configure to send messages to users through email group, WeChat Work, DingTalk, Webhook, etc.<br />Supports notifying multiple alert objects at the same time |
| | Message Template | The message template function supports customizing the content of the message template, and can notify the specified object in the form of email, WeChat Work, DingTalk, Webhook |
| Log Collection and Query | Unified Log Collection | Collects log data of nodes, containers, inside containers, k8s events uniformly<br />Collects audit operations of the global management platform, by default, does not collect k8s audit logs |
| | Log Persistent Storage | Logs can be tagged and output to middleware such as Elasticsearch for persistence |
| Metric Collection | Metric Data Collection | Supports defining the Namespace range of Pod discovery and selecting the Service to monitor by using ServiceMonitor |
| System Management | System Settings | System settings shows the default storage duration of metrics, logs, links and the default Apdex threshold<br />Supports custom modification of storage time of metrics, logs, link data |
| | System Components | Provides unified monitoring of Insight components, and real-time detection of the health status of system components |

## DCE 5.0 Enterprise - Insight

On the basis of the DCE Community, the DCE 5.0 Enterprise provides more abundant and customizable insight features.

| Category | Subcategory  | Description |
| -------- | ------------ | ----------- |
| Infrastructure | Multicluster Insight | Provides centralized Insight of multicluster business<br />Admins manage multicluster alerts uniformly, and meet the data isolation of cluster and tenant administrators<br />Supports persistent metrics and log data of clusters. |
| | Cluster Insight | Provides an overview of a single cluster's monitoring, allowing you to view the running status of the cluster, understand the resource usage of the cluster, and the current alerts occurring in the cluster |
| | Node Insight | Supports viewing the running status of nodes, and understanding the changes in CPU, memory, network and other resources of the node |
| | Namespace Insight | Supports viewing the number of resources running in the namespace, and the total amount of CPU and memory used by the Pods in the namespace. |
| | Container Insight | Supports monitoring resources such as stateless loads, daemonsets, Pods, etc. You can monitor the running status of this workload, view the number of alerts in progress, and the trend chart of changes in CPU, memory and other resource consumption |
| Dashboard | Platform Component Insight | Provides open source selected dashboards through native Grafana, provides built-in dashboards to support monitoring of etcd, APIServer and other components |
| | Cluster Resource Insight | Provides monitoring for multiple dimensions such as clusters, nodes, namespaces, etc. The data source used by Grafana supports viewing data from multiple clusters. |
| Metric | Metric Query | The normal query has reserved basic metrics, and the resource change trend can be queried after selecting the cluster, type, node, metric name and other query conditions<br />Supports querying metric charts and data details through native PromQL statements |
| Log | Log Query | Can query logs, can query the context content of a single log<br />Supports searching by keywords<br />Default sorted by time, the log quantity change trend can be queried through histogram<br />Supports using Lucene syntax to query logs |
| | Log Context | Supports querying the context of multiple selected logs, default query up and down 100, can be adjusted according to needs. |
| | Log Download | Supports configuring export log fields<br />Supports downloading logs within a period of time according to search conditions<br />Supports exporting the context content of a single log |
| Trace Tracking[^1] | Service Map | Administrators can view the call relationship and health status of services that have accessed the Insight platform and link collection, quickly locate faults<br />Can view the flow direction and key indicators of requests between services<br />Can quickly view the real-time throughput, number of requests, request delay and error rate of a single service |
| | Services | Can view the service list of the current link data access, and the throughput, error rate, and request delay of the service in the last 15 minutes<br /> Click the service to view the traffic trend of the selected service in the last 15 minutes and the aggregated indicators of the service operation |
| | Traces | Default query all requests of the selected service in the last 15 minutes and the request status, delay, Span number, etc.<br /> Click the icon on the side of the list to query the related container logs and link logs of the link. |
| Alert Center | Active Alerts | Provides histogram to view the change trend of alert time<br />Supports viewing all rules and details that are currently alerting |
| | Historical Alerts | Can query all alerts that have been automatically recovered or manually resolved |
| |  Alert Rules | Built-in 100+ alert rules, provides predefined alert rules for cluster components, container resources, etc.<br />Administrators can create global alert rules and uniformly alert clusters that have installed Insight-agent<br />Supports creating alert rules through predefined metrics<br />Supports creating alert rules by writing PromQL statements<br />Supports customizing threshold, duration and notification method<br />Can customize the level of alerts, supports three levels: emergency, warning, prompt |
| | Notification Settings | On the notification settings page, you can configure to send messages to users through email group, WeChat Work, DingTalk, Webhook, etc.<br />Supports notifying multiple alert objects at the same time |
| | Message Template | The message template function supports customizing the content of the message template, and can notify the specified object in the form of email, WeChat Work, DingTalk, Webhook |
| | Alert Silence | Supports not sending messages for alerts that match conditions through rule tags or alert event tags during a fixed time |
| Log Collection and Query | Unified Log Collection | Collects log data of nodes, containers, inside containers, k8s events uniformly<br />Collects audit operations of the global management platform, by default, does not collect k8s audit logs |
| | Log Persistent Storage | Logs can be tagged and output to middleware such as Elasticsearch for persistence |
| Metric Collection | Metric Data Collection | Supports defining the Namespace range of Pod discovery and selecting the Service to monitor by using ServiceMonitor |
| System Management | System Settings | System namagement shows the default storage duration of metrics, logs, links and the default Apdex threshold<br />Supports custom modification of storage time of metrics, logs, link data |
| | System Components | Provides unified monitoring of Insight components, and real-time detection of the health status of system components |

[^1]: This is a feature only available in the DCE 5.0 Enterprise.
