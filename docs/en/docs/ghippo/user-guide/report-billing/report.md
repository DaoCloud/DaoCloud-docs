---
hide:
  - toc
---

# Report Management

The report management module integrates the administrator's job execution status and the cluster's hardware resource configuration, and provides statistics from the dimensions of the cluster, node, Pod, workspace, and namespace. It intuitively presents the utilization of computing resources to users, helping them better partition and schedule computing resources.

After enabling a certain type of report, the cluster report data will start collecting and displaying within 20 minutes. After disabling, data collection for the report will stop within the same time frame. The data that has been collected before will still be displayed normally.

Currently, the following types of reports are provided:

- Cluster report: shows all cluster names, including the number of nodes (clicking on the number can jump to the node report) and resource utilization rates. Searchable by cluster name.
- Node report: shows the IP address, type, and the cluster it belongs to, as well as the resource utilization rate. Customizable time range for the report, searchable by node name, cluster, and IP address.
- Pod report: shows the name, namespace, cluster, workspace, and resource utilization rate of each Pod. Customizable time range for the report, searchable by Pod name, namespace, cluster, and workspace.
- Workspace report: shows the workspace name, number of namespaces contained (clicking on the number can jump to the namespace report), container group quantity (clicking on the number can jump to the Pod report), and resource utilization rate. Customizable time range for the report, searchable by workspace.
- Namespace report: shows the namespace name, number of Pods (clicking on the number can jump to the Pod report), the cluster and workspace it belongs to, and the resource utilization rate. Customizable time range for the report, searchable by namespace, cluster, and workspace.
- Audit report: provides statistics on user operations and operations performed on resources to help administrators control resource usage and track user operation traces. Searchable by username, resource type/event name, workspace, namespace, and cluster.
- Alert report: suitable for generating cluster inspection reports. Customizable time range for the report, searchable by node name and cluster.

The statistical information for each report is shown in the table below:

| Report Type  | Display Content                                            | Searchable Items                                     | Export/Download | Enable/Disable | Customizable Time Range | Gear Icon Setting |
| ------------ | ---------------------------------------------------------- | ---------------------------------------------------- | --------------- | -------------- | ---------------------- | ----------------- |
| Cluster      | Cluster Name, Number of Nodes, Resource Utilization Rate    | Cluster Name                                         | Yes             | Yes            | Yes                    | Yes               |
| Node         | Node IP, Type, Cluster, Resource Utilization Rate          | Node Name, Cluster, IP Address                       | Yes             | Yes            | Yes                    | Yes               |
| Pod          | Pod Name, Namespace, Cluster, Workspace, Resource Utilization Rate | Pod Name, Namespace, Cluster, Workspace | Yes             | Yes            | Yes                    | Yes               |
| Workspace    | Workspace Name, Number of Namespaces, Container Group Quantity, Resource Utilization Rate | Workspace | Yes             | Yes            | Yes                    | Yes               |
| Namespace    | Namespace Name, Number of Pods, Cluster, Workspace, Resource Utilization Rate | Namespace, Cluster, Workspace | Yes             | Yes            | Yes                    | Yes               |
| Audit        | User and resource operation statistics                     | Username, Resource Type/Event Name, Workspace, Namespace, Cluster | Yes             | Yes            | Yes                    | No                |
| Alert        | Cluster inspection report                                   | Node Name, Cluster                                   | Yes             | Yes            | Yes                    | No                |

From the table above, it can be seen that each report has its specific display content and searchable items. In addition, each report can be exported or downloaded for administrators to view. The enable/disable feature and customizable time range are available for all reports. Except for the audit report and alert report, all other reports provide a gear ⚙️ icon setting function so that administrators can customize the columns to display according to their actual needs.