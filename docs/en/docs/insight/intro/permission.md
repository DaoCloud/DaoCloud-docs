---
hide:
   - toc
---

# Insight permission description

The Insight uses the following roles:

- Admin / Kpanda Owner
- [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)
- [NS Admin](../../kpanda/user-guide/permissions/permission-brief.md#ns-admin) / [NS Edit](../../kpanda/user-guide/permissions/permission-brief.md#ns-edit)
- [NS View](../../kpanda/user-guide/permissions/permission-brief.md#ns-view)

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
| trace query | query trace | &check; | &check; | &check; | &check; |
| alert List | View alert Events | &check; | &check; | &check; | &check; |
| Alert Rules | Create Metric Template Rule - Workload | &check; | &check; | &check; | &cross; |
| | Create metric Template Rule - Node | &check; | &check; | &cross; | &cross; |
| | Modify Metric Template Rule - Workload | &check; | &check; | &check; | &cross; |
| | Modify metric Template Rules - Node | &check; | &check; | &cross; | &cross; |
| | View Metric Template Rules - Workload | &check; | &check; | &check; | &check; |
| | View metric Template Rules - Node | &check; | &check; | &cross; | &cross; |
| | Create promQL rules | &check; | &check; | &check; | &cross; |
| | Modify promQL rules | &check; | &check; | &check; | &cross; |
| | Delete custom alert rule | &check; | &check; | &check; | &cross; |
| | View built-in alert rules | &check; | &cross; | &cross; | &cross; |
| | Modify built-in alert rules | &check; | &cross; | &cross; | &cross; |
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

For more information on permissions, see [Container Management Permissions Description](../../kpanda/user-guide/permissions/permission-brief.md).

For creating, managing, and deleting roles, see [Role and Permission Management](../../ghippo/user-guide/access-control/role.md).
