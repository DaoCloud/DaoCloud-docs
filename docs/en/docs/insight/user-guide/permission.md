---
hide:
  - toc
---

# Observability permission description

The observability module uses the following roles:

- Admin / Kpanda Owner
- [Cluster Admin](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#cluster-admin)
- [NS Admin](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#ns-admin) / [NS Edit](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#ns- edit)
- [NS View](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#ns-view)

The permissions of each role are as follows:

<!--
You have permission to use `&check;`, but you don't have permission to use `&cross;`
-->

| Menu | Operation | Admin / Kpanda Owner | Cluster Admin | NS Admin / NS Edit | NS View |
| -------- | --------------------------- | ------------ -------- | ------------- | ------------------ | ------- |
| Overview | View Overview | &check; | &cross; | &cross; | &cross; |
| Dashboard | View Dashboard | &check; | &cross; | &cross; | &cross; |
| Scenario Monitoring | View Cluster Monitoring | &check; | &check; | &cross; | &cross; |
| | View node monitoring | &check; | &check; | &cross; | &cross; |
| | View container monitoring | &check; | &check; | &check; | &check; |
| | View Service Monitoring | &check; | &check; | &check; | &check; |
| | View Topology | &check; | &check; | &check; | &check; |
| Metric Query | Query Node Metrics - Common | &check; | &check; | &cross; | &cross; |
| | Query Workload Metrics - Normal | &check; | &check; | &check; | &check; |
| | Query Metrics - Advanced | &check; | &check; | &check; | &check; |
| Log query | Query cluster event logs | &check; | &check; | &cross; | &cross; |
| | Query node logs | &check; | &check; | &cross; | &cross; |
| | Query container logs | &check; | &check; | &check; | &check; |
| link query | query link | &check; | &check; | &check; | &check; |
| Alarm List | View Alarm Events | &check; | &check; | &check; | &check; |
| Alert Rules | Create Metric Template Rule - Workload | &check; | &check; | &check; | &cross; |
| | Create Indicator Template Rule - Node | &check; | &check; | &cross; | &cross; |
| | Modify Metric Template Rule - Workload | &check; | &check; | &check; | &cross; |
| | Modify Indicator Template Rules - Node | &check; | &check; | &cross; | &cross; |
| | View Metric Template Rules - Workload | &check; | &check; | &check; | &check; |
| | View Indicator Template Rules - Node | &check; | &check; | &cross; | &cross; |
| | Create promQL rules | &check; | &check; | &check; | &cross; |
| | Modify promQL rules | &check; | &check; | &check; | &cross; |
| | Delete custom alert rule | &check; | &check; | &check; | &cross; |
| | View built-in alert rules | &check; | &cross; | &cross; | &cross; |
| | Modify built-in alarm rules | &check; | &cross; | &cross; | &cross; |
| Who to Notify | View Who to Notify | &check; | &check; | &check; | &check; |
| | Add notification object | &check; | &cross; | &cross; | &cross; |
| | Modify notification object | &check; | &cross; | &cross; | &cross; |
| | delete notification object | &check; | &cross; | &cross; | &cross; |
| | View message templates | &check; | &check; | &check; | &check; |
| | Add Message Template | &check; | &cross; | &cross; | &cross; |
| | Modify Message Template | &check; | &cross; | &cross; | &cross; |
| | Delete Message Template | &check; | &cross; | &cross; | &cross; |
| Collection Management | View Agent List | &check; | &check; | &check; | &check; |
| | Install/Uninstall Agent | &check; | &check; | &check; | &check; |
| | View Agent Details | &check; | &check; | &check; | &check; |
| System Configuration | View System Configuration | &check; | &cross; | &cross; | &cross; |

For more information on permissions, see [Container Management Permissions Description](../../kpanda/07UserGuide/Permissions/PermissionBrief.md).

For creating, managing and deleting roles, please refer to [Role and Access Management](../../ghippo/user-guide/access-control/Role.md).