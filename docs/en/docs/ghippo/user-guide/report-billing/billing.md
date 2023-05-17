---
hide:
  - toc
---

# Billing and accounting

First, you can use billing config to set the unit prices for CPU, memory, storage, inbound/outbound traffic, and currency types. Currently, two currencies are supported: CNY and USD.

Currently, billing and accounting are supported for clusters, nodes, Pods, namespaces, and workspaces. After enabling a certain type of billing, the billing data will start collecting and displaying within 20 minutes. After disabling, data collection for the billing will stop within the same time frame. The previous collected data will still be displayed normally.

The table below shows the display content and searchable items for each type of billing. It also provides the function of exporting/downloading data, and supports custom time ranges and gear icon setting functions for administrators to customize the columns to display according to their actual needs.

| Billing and accounting | Display Content                                            | Searchable Items                                     | Export/Download | Enable/Disable | Customizable Time Range | Gear Icon Setting |
| -------------------- | ---------------------------------------------------------- | ---------------------------------------------------- | --------------- | -------------- | ---------------------- | ----------------- |
| Cluster Billing      | Cluster Name, Number of Nodes, Resource Billing Information | Cluster Name                                         | Yes             | Yes            | Yes                    | Yes               |
| Node Billing         | Node IP, Type, Cluster, Resource Billing Information        | Node Name, Cluster, IP Address                       | Yes             | Yes            | Yes                    | Yes               |
| Pod Billing          | Pod Name, Namespace, Cluster, Workspace, Resource Billing Information | Pod Name, Namespace, Cluster, Workspace | Yes             | Yes            | Yes                    | Yes               |
| Workspace Billing    | Workspace Name, Number of Namespaces, Container Group Quantity, Resource Billing Information | Workspace | Yes             | Yes            | Yes                    | Yes               |
| Namespace Billing    | Namespace Name, Number of Pods, Cluster, Workspace, Resource Billing Information | Namespace, Cluster, Workspace | Yes             | Yes            | Yes                    | Yes               |

From the table above, it can be seen that each type of billing has its specific display content and searchable items. In addition, each type of billing can be exported or downloaded for administrators to view. The enable/disable feature and customizable time range are available for all types of billing. All other types of billing except namespace billing provide a gear ⚙️ icon setting function so that administrators can customize the columns to display according to their actual needs.
