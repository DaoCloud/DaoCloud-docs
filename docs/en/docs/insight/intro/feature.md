---
hide:
  - toc
---

# Features list

This page lists the features supported by Observability Insight.

## Community Release - Observability

DCE 5.0 Community Release provides the following observable features.

| Category | Subcategory | Description |
| -------- | ----------------------------------------- --------- | ---------------------------------------- --------- |
| Resource monitoring | Multi-cluster monitoring | Provide multi-cluster business centralized observability<br />The administrator manages multi-cluster alarms in a unified manner, and satisfies cluster and tenant administrator data isolation<br />Supports persistent cluster indicators and log data. |
| | Scenario monitoring | Provides a monitoring overview of a single cluster, allowing you to view the running status of the cluster, understand the resource usage of the cluster, and the current alarms that are occurring in the cluster |
| | Node monitoring | Support to view the running status of the node, etc., and understand the changes in the CPU, memory, network and other resources of the node |
| | Container Monitoring | Supports monitoring of resources such as stateless loads, daemon processes, container groups, etc., can monitor the running status of the workload, and can view the number of alarms and the trend chart of resource consumption such as CPU and memory |
| Dashboard | Platform Component Monitoring | Provide open-source selected dashboards through native Grafana, and provide built-in dashboards to support monitoring etcd, APIServer and other components |
| | Cluster Resource Monitoring | Provides multi-dimensional monitoring of clusters, nodes, and namespaces. The data source used by Grafana supports viewing data from multiple clusters. |
| Data Query | Index Query | Common Query pre-orders basic indicators, and after selecting query conditions such as cluster, type, node, and indicator name, you can query the change trend of resources<br />Support querying indicator charts and data details through native PromQL statements |
| | Log query| You can query the logs of Node, Pod, Depoyment, Statefulset, etc., and you can query the context content of a single log<br />Support searching by keyword<br />Sort by time by default, and you can query the number of logs through the histogram <br />Support querying detailed information and context of a single log |
| | Log Download | Support to download logs within a period of time according to search criteria<br />Support exporting the content of a single log context |
| Alarm Center | Active Alarm | Provide a histogram to view the change trend of the alarm time<br />Support to view all the rules and details that are alarming |
| | Historical alarms | You can query all alarms after automatic recovery or manual resolution |
| | Alert rules| Built-in 100+ alert rules, providing predefined alert rules for cluster components, container resources, etc.<br />Administrators can create global alert rules to provide unified alerts for clusters that have installed insight-agent<br / >Support creating alarm rules through predefined indicators<br />Support creating alarm rules by writing PromQL statements<br />Support custom thresholds, durations and notification methods<br />You can customize the level of alarms, support emergency, warning , Prompt three levels |
| | Notification configuration | On the notification configuration page, you can configure to send messages to users through email groups, corporate WeChat, DingTalk, Webhook, etc.<br />Support simultaneous notification to multiple alarm objects |
| | Message template | The message template function supports customizing the content of the message template, and can notify the specified object in the form of email, corporate WeChat, DingTalk, and Webhook |
| Log collection and query | Unified log collection | Unified collection of log data of nodes, containers, containers, and k8s events<br />Collect the audit operation of the global management platform, and the collection of k8s audit logs is not enabled by default |
| | Log persistent storage | Logs can be marked and output to middleware such as Elasticsearch for persistence |
| Metric collection | Metric data collection | Support to use ServiceMonitor to define the namespace scope of Pod discovery and select the listening Service through matchLabel |
| System configuration | System configuration | System configuration displays the default storage time of indicators, logs, and links and the default Apdex threshold<br />Support custom modification of the storage time of indicators, logs, and link data |

## Commercial Release - Observability

On the basis of the community release, the commercial release of DCE 5.0 provides more abundant and customizable observable features.

| Category | Subcategory | Description |
| -------------- | -------------- | ---------------- -------------------------------------------- |
| Resource monitoring | Multi-cluster monitoring | Provide multi-cluster business centralized observability<br />The administrator manages multi-cluster alarms in a unified manner, and satisfies cluster and tenant administrator data isolation<br />Supports persistent cluster indicators and log data. |
| | Cluster Monitoring | Provides an overview of the monitoring of a single cluster, allowing you to view the running status of the cluster, understand the resource usage of the cluster, and the alarms that are currently occurring in the cluster |
| | Node monitoring | Support to view the running status of the node, etc., and understand the changes in the CPU, memory, network and other resources of the node |
| | Container Monitoring | Supports monitoring of resources such as stateless loads, daemon processes, container groups, etc., can monitor the running status of the workload, and can view the number of alarms and the trend chart of resource consumption such as CPU and memory |
| Scenario Monitoring| Service Monitoring[^1] | You can view key indicators such as real-time throughput, number of requests, request delay and error rate of the service, as well as the trend of change over a period of time<br />You can view the service's real-time performance over a period of time Requests, as well as the trend of real-time throughput, number of requests, request delay and error rate of a single request |
| | Topology map[^1] | The administrator can view the call relationship and health status between services connected to the observation platform and link collection, and quickly locate faults<br />You can view the traffic direction and key indicators requested between services <br />You can quickly view the real-time throughput, number of requests, request latency and error rate of a single service |
| Dashboard | Platform Component Monitoring | Provide open-source selected dashboards through native Grafana, and provide built-in dashboards to support monitoring etcd, APIServer and other components |
| | Cluster Resource Monitoring | Provides multi-dimensional monitoring of clusters, nodes, and namespaces. The data source used by Grafana supports viewing data from multiple clusters. |
| Data Query | Index Query | Common Query pre-orders basic indicators, and after selecting query conditions such as cluster, type, node, and indicator name, you can query the change trend of resources<br />Support querying indicator charts and data details through native PromQL statements |
| | Log query| You can query the logs of Node, Pod, Depoyment, Statefulset, etc., and you can query the context content of a single log<br />Support searching by keyword<br />Sort by time by default, and you can query the number of logs through the histogram <br />Support querying detailed information and context of a single log |
| | Log Download | Support to download logs within a period of time according to search criteria<br />Support exporting the content of a single log context |
| | Link query[^1] | Through link query, you can view all the requests of the service within a certain period of time, support configuring clusters, namespaces, services, operations, tags, and then click Search for precise search<br />Supports viewing a single Requested aggregated link graph for fast fault location |
| Alarm Center | Active Alarm | Provide a histogram to view the change trend of the alarm time<br />Support to view all the rules and details that are alarming |
| | Historical alarms | You can query all alarms after automatic recovery or manual resolution |
| | Alert rules| Built-in 100+ alert rules, providing predefined alert rules for cluster components, container resources, etc.<br />Administrators can create global alert rules to provide unified alerts for clusters that have installed insight-agent<br />Support creating alarm rules through predefined indicators<br />Support creating alarm rules by writing PromQL statements<br />Support custom thresholds, durations and notification methods<br />You can customize the level of alarms, support emergency, warning , Prompt three levels |
| | Notification configuration | On the notification configuration page, you can configure to send messages to users through email groups, corporate WeChat, DingTalk, Webhook, etc.<br />Support simultaneous notification to multiple alarm objects |
| | Message template | The message template function supports customizing the content of the message template, and can notify the specified object in the form of email, corporate WeChat, DingTalk, and Webhook |
| Log collection and query | Unified log collection | Unified collection of log data of nodes, containers, containers, and k8s events<br />Collect the audit operation of the global management platform, and the collection of k8s audit logs is not enabled by default |
| | Persistent storage of logs | Logs can be marked and output to middleware such as Elasticsearch for persistence |
| Metric collection | Metric data collection | Support to use ServiceMonitor to define the namespace scope of Pod discovery and select the monitored Service through matchLabel |
| | Component status[^1] | Support to view the status of the container group of the collection component, and jump to the corresponding container group details |
| Link Collection[^1] | Link Data Collection| Support link data collection by using OTEL SDK in a non-intrusive or less intrusive way<br />Support link collection by injecting Sidecar into grid applications data |
| System configuration | System configuration | System configuration displays the default storage time of indicators, logs, and links and the default Apdex threshold<br />Support custom modification of the storage time of indicators, logs, and link data |

[^1]: This is a feature only available in the commercial release.
