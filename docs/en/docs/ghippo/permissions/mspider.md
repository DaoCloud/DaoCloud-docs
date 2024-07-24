---
hide:
  - toc
---

# Service Mesh Permissions

[Service Mesh](../../mspider/intro/index.md) supports several user roles:

- Admin
- Workspace Admin
- Workspace Editor
- Workspace Viewer

!!! info

    Starting from installer [v0.6.0](../../download/index.md) of DCE 5.0, the global management module supports custom roles configuration for Service Mesh, meaning that in addition to using default system roles, custom roles can be defined and granted different permissions within Service Mesh.

<!--
Use `&check;`for permissions granted and `&cross;`for permissions not granted.
-->

The specific permissions for each role are shown in the following table.

| Menu Object | Action | Admin | Workspace Admin | Workspace Editor | Workspace Viewer |
| ----------- | ------ | ----- | --------------- | ---------------- | ---------------- |
| Service Mesh List | [Create Mesh](../../mspider/user-guide/service-mesh/README.md) | &check; | &cross; | &cross; | &cross; |
| | Edit Mesh | &check; | &check; | &cross; | &cross; |
| | [Delete Mesh](../../mspider/user-guide/service-mesh/delete.md) | &check; | &cross; | &cross; | &cross; |
| | [View Mesh](../../mspider/user-guide/service-mesh/README.md) | &check; | &check; | &check; | &check; |
| Mesh Overview | View | &check; | &check; | &check; | &check; |
| Service List | View | &check; | &check; | &check; | &check; |
| | Create VM | &check; | &check; | &check; | &cross; |
| | Delete VM | &check; | &check; | &check; | &cross; |
| Service Entry | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Virtual Service | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Destination Rule | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Gateway Rule | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Peer Authentication | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Request Authentication | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Authorization Policy | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Namespace Sidecar Management | Enable Injection | &check; | &check; | &check; | &cross; |
| | Disable Injection | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| | Sidecar Service Discovery Scope | &check; | &check; | &check; | &cross; |
| Workload Sidecar Management | Enable Injection | &check; | &check; | &check; | &cross; |
| | Disable Injection | &check; | &check; | &check; | &cross; |
| | Configure Sidecar Resources | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Global Sidecar Injection | Enable Injection | &check; | &check; | &cross; | &cross; |
| | Disable Injection | &check; | &check; | &cross; | &cross; |
| | Configure Sidecar Resources | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Cluster Management (for Hosted Mesh only) | Join Cluster | &check; | &check; | &cross; | &cross; |
| | Leave Cluster | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Mesh Gateway Management | Create | &check; | &check; | &cross; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Istio Resource Management | Create | &check; | &check; | &cross; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| TLS Certificate Management | Create | &check; | &check; | &check; | &cross; |
| | Edit | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Multicloud Network Interconnection | Enable | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &cross; | &cross; |
| | Edit | &check; | &check; | &cross; | &cross; |
| | Delete | &check; | &check; | &cross; | &cross; |
| | Disable | &check; | &check; | &cross; | &cross; |
| System Upgrade | Istio Upgrade | &check; | &check; | &cross; | &cross; |
| | Sidecar Upgrade | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Workspace Management | Bind | &check; | &cross; | &cross; | &cross; |
| | Unbind | &check; | &cross; | &cross; | &cross; |
| | View | &check; | &cross; | &cross; | &cross; |
