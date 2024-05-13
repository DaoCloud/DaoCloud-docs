---
MTPE: FanLin
Date: 2024-01-22
---

# Insight Permissions Description

The Insight uses the following roles:

- Admin / Kpanda Owner
- [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)
- [NS Admin](../../kpanda/user-guide/permissions/permission-brief.md#ns-admin) / [NS Edit](../../kpanda/user-guide/permissions/permission-brief.md#ns-editor)
- [NS View](../../kpanda/user-guide/permissions/permission-brief.md#ns-viewer)

The permissions of each role are as follows:

<!--
You have permission to use `&check;`, but you don't have permission to use `&cross;`
-->

| Menu | Operation | Admin / Kpanda Owner | Cluster Admin | NS Admin / NS Edit | NS View |
| -------- | --------------------------- | -------------------- | ------------- | ------------------ | ------- |
| Overview | View Overview | &check; | &cross; | &cross; | &cross; |
| Dashboard | View Dashboard | &check; | &cross; | &cross; | &cross; |
| Infrastructure | View Cluster Insight | &check; | &check; | &cross; | &cross; |
| | View Node Insight | &check; | &check; | &cross; | &cross; |
| | View Namespace Insight | &check; | &check; | &check; | &check; |
| | View Workload Insight | &check; | &check; | &check; | &check; |
| | View Events | &check; | &check; | &check; | &check; |
| | View Probe| &check; | &check; | &check; | &check; |
| | Create Probe Job | &check; | &check; | &check; | &cross; |
| | Edit Probe Job | &check; | &check; | &check; | &cross; |
| | Delete Probe Job | &check; | &check; | &check; | &cross; |
| Metrics | Query Node Metrics | &check; | &check; | &cross; | &cross; |
| | Query Workload Metrics | &check; | &check; | &check; | &check; |
| | Advanced Query | &check; | &check; | &check; | &check; |
| Logs | Query Node Logs | &check; | &check; | &cross; | &cross; |
| | Query Container Logs | &check; | &check; | &check; | &check; |
| | Lucene Syntax Query Node Logs | &check; | &check; | &cross; | &cross; |
| | Lucene Syntax Query Container Logs | &check; | &check; | &check; | &check; |
| Trace Tracking | View Service Map | &check; | &check; | &check; | &check; |
| | View Services | &check; | &check; | &check; | &check; |
| | View Traces | &check; | &check; | &check; | &check; |
| | TraceID Query Link | &check; | &check; | &check; | &check; |
| Alert List | View Alert Events | &check; | &check; | &check; | &check; |
| Alert Rules | Create Metric Template Rule - Workload | &check; | &check; | &check; | &cross; |
| | Create Metric Template Rule - Node | &check; | &check; | &cross; | &cross; |
| | Modify Metric Template Rule - Workload | &check; | &check; | &check; | &cross; |
| | Modify Metric Template Rule - Node | &check; | &check; | &cross; | &cross; |
| | View Metric Template Rule - Workload | &check; | &check; | &check; | &check; |
| | View Metric Template Rule - Node | &check; | &check; | &cross; | &cross; |
| | Create promQL Rule | &check; | &check; | &check; | &cross; |
| | Modify promQL Rule | &check; | &check; | &check; | &cross; |
| | Create Log Rule | &check; | &check; | &check; | &cross; |
| | Create Time Rule | &check; | &check; | &check; | &cross; |
| | Delete Custom Alert Rule | &check; | &check; | &check; | &cross; |
| | View Built-in Alert Rule | &check; | &cross; | &cross; | &cross; |
| | Modify Built-in Alert Rule | &check; | &cross; | &cross; | &cross; |
| | YAML Import Alert Rule | &check; | &check; | &check; | &cross; |
| Notification Objects | View Notification Objects | &check; | &check; | &check; | &check; |
| | Add Notification Objects | &check; | &cross; | &cross; | &cross; |
| | Modify Notification Objects | &check; | &cross; | &cross; | &cross; |
| | Delete Notification Objects | &check; | &cross; | &cross; | &cross; |
| | View Message Template | &check; | &check; | &check; | &check; |
| | Add Message Template | &check; | &cross; | &cross; | &cross; |
| | Modify Message Template | &check; | &cross; | &cross; | &cross; |
| | Delete Message Template | &check; | &cross; | &cross; | &cross; |
| Alert Silence | View Silence Rules List | &check; | &check; | &check; | &check; |
| | Create Silence Rule | &check; | &check; | &check; | &cross; |
| | Edit Silence Rule | &check; | &check; | &check; | &cross; |
| | Delete Silence Rule | &check; | &check; | &check; | &cross; |
| Collection Management | View Agent List | &check; | &check; | &check; | &check; |
| | Install/Uninstall Agent | &check; | &check; | &check; | &check; |
| | View Agent Details | &check; | &check; | &check; | &check; |
| System Settings | View System Settings | &check; | &cross; | &cross; | &cross; |
| | Modify System Settings | &check; | &cross; | &cross; | &cross; |

For more information on permissions, please refer to the [Container Management Permissions Description](../../kpanda/user-guide/permissions/permission-brief.md).

For information on role creation, management, and deletion, please refer to [Role and Permission Management](../../ghippo/user-guide/access-control/role.md).
