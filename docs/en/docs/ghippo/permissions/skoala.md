# Description of Microservice Engine Permissions

[Microservice engine](../../skoala/intro/index.md) includes two parts: microservice management center and microservice gateway. The microservice engine supports three user roles:

- Workspace Admin
- Workspace Editor
- Workspace Viewer

Each role has different permissions, which are described below.

<!--
You have permission to use `&check;`, but you don't have permission to use `&cross;`
-->

## Description of Microservice Governance Center Permissions

| Menu Objects | Actions | Workspace Admin | Workspace Editor | Workspace Viewer |
| --------------------- | ------------ | -------------- - | ---------------- | ---------------- |
| Hosted Registry List | View List | &check; | &check; | &check; |
| Hosted Registry | View Basic Information | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | restart | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &cross; | &cross; |
| | On/Off | &check; | &check; | &cross; |
| Microservice Namespace | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Microservice List | View | &check; | &check; | &check; |
| | filter namespace | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | Governance | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Service Governance Rules-Sentinel | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Service Governance Rules-Mesh | Governance | &check; | &check; | &cross; |
| Instance List | View | &check; | &check; | &check; |
| | On/Off | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| Service Governance Policy-Sentinel | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Service Governance Policy-Mesh | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | Create with YAML | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | YAML Editing | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Microservice Configuration List | View | &check; | &check; | &check; |
| | filter namespace | &check; | &check; | &check; |
| | Batch delete | &check; | &check; | &cross; |
| | Export/Import | &check; | &check; | &cross; |
| | Create | &check; | &check; | &cross; |
| | Clone | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | History query | &check; | &check; | &check; |
| | rollback | &check; | &check; | &cross; |
| | listen query | &check; | &check; | &check; |
| Business Monitor | View | &check; | &check; | &check; |
| Resource Monitor | View | &check; | &check; | &check; |
| Request Log | View | &check; | &check; | &check; |
| Instance Log | View | &check; | &check; | &check; |
| Plugin Center | View | &check; | &check; | &check; |
| | Open | &check; | &check; | &cross; |
| | Close | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | View Details | &check; | &check; | &check; |
| access registry list | view | &check; | &check; | &check; |
| | Access | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | Remove | &check; | &cross; | &cross; |
| Microservices | View List | &check; | &check; | &check; |
| | View Details | &check; | &check; | &check; |
| | Governance | &check; | &check; | &cross; |
| Service Governance Policy-Mesh | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | Create with YAML | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | YAML Editing | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |

## Description of Microservice Gateway Permissions

| Objects | Actions | Workspace Admin | Workspace Editor | Workspace Viewer |
| ------------ | ---- | --------------- | --------------- - | ---------------- |
| Gateway List | View | &check; | &check; | &check; |
| Gateway instance | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &cross; | &cross; |
| Diagnostic Mode | View | &check; | &check; | &check; |
| | debug | &check; | &check; | &cross; |
| Service List | View | &check; | &check; | &check; |
| | Add | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Service Details | View | &check; | &check; | &check; |
| Service Source Management | View | &check; | &check; | &check; |
| | Add | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| API List | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Request Log | View | &check; | &check; | &check; |
| Instance Log | View | &check; | &check; | &check; |
| Plugin Center | View | &check; | &check; | &check; |
| | enable | &check; | &check; | &cross; |
| | disabled | &check; | &check; | &cross; |
| Plugin Configuration | View | &check; | &check; | &check; |
| | enable | &check; | &check; | &cross; |
| Domain List | View | &check; | &check; | &check; |
| | Add | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &check; |
| Monitor Alert | View | &check; | &check; | &check; |

!!! note

    For a complete introduction to role and access management, please refer to [Role and Access Management](../user-guide/access-control/role.md).