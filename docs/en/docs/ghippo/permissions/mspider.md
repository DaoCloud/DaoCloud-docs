---
hide:
  - toc
---

# Service Mesh Permissions Explanation

[Service Mesh](../../mspider/intro/what.md) supports several user roles:

- Admin
- Workspace Admin
- Workspace Editor
- Workspace Viewer

!!! info

    Starting from installer [v0.6.0](../../download/dce5.md) of DCE 5.0, the [global management](../../ghippo/intro/what.md) module supports custom roles configuration for Service Mesh, meaning that in addition to using default system roles, custom roles can be defined and granted different permissions within Service Mesh.

<!--
Permissions are indicated with `✅` for granted access and `❌` for denied access.
-->

The specific permissions for each role are shown in the following table.

| Menu Object     | Action    | Admin | Workspace Admin | Workspace Editor | Workspace Viewer |
| ------------------------ | -------------------------- | ----- | ---------- | --------- | ------------- |
| Service Mesh List   | [Create Mesh](../../mspider/user-guide/service-mesh/README.md)| ✅    | ❌   | ❌    | ❌    |
|      | Edit Mesh | ✅    | ✅   | ✅    | ❌    |
|      | [Delete Mesh](../../mspider/user-guide/service-mesh/delete.md)| ✅    | ✅   | ❌    | ❌    |
|      | [View Mesh](../../mspider/user-guide/service-mesh/README.md)  | ✅    | ✅   | ✅    | ✅    |
| Mesh Overview   | View      | ✅    | ✅   | ✅    | ✅    |
| Service List    | [Go to Governance Page](../../mspider/user-guide/service-list/README.md) | ✅    | ✅   | ✅    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Service Entry   | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Virtual Service | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Destination Rule| Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Gateway Rule    | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Peer Identity Auth  | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Request Identity Auth          | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Authorization Policy| Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Namespace Sidecar Management   | Enable Injection     | ✅    | ✅   | ✅    | ❌    |
|      | Disable Injection    | ✅    | ✅   | ✅    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Workload Sidecar Management    | Enable Injection     | ✅    | ✅   | ✅    | ❌    |
|      | Disable Injection    | ✅    | ✅   | ✅    | ❌    |
|      | Configure Sidecar Resources         | ✅    | ✅   | ✅    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Global Sidecar Injection       | Enable Injection     | ✅    | ✅   | ✅    | ❌    |
|      | Disable Injection    | ✅    | ✅   | ✅    | ❌    |
|      | Configure Sidecar Resources         | ✅    | ✅   | ✅    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Cluster Management (for Hosted Mesh only) | Join Cluster         | ✅    | ✅   | ❌    | ❌    |
|      | Leave Cluster        | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Mesh Gateway Management        | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Istio Resource Management      | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| TLS Certificate Management     | Create    | ✅    | ✅   | ❌    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Multi-cloud Network Interconnection       | Enable    | ✅    | ✅   | ✅    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ❌    |
|      | Edit      | ✅    | ✅   | ✅    | ❌    |
|      | Delete    | ✅    | ✅   | ❌    | ❌    |
|      | Disable   | ✅    | ✅   | ❌    | ❌    |
| System Upgrade  | Istio Upgrade        | ✅    | ✅   | ✅    | ❌    |
|      | Sidecar Upgrade      | ✅    | ✅   | ✅    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
| Workspace Management| Bind      | ✅    | ❌   | ❌    | ❌    |
|      | Unbind    | ✅    | ❌   | ❌    | ❌    |
|      | View      | ✅    | ✅   | ✅    | ✅    |
