---
hide:
  - toc
---

# Description of Service Mesh Permissions

[Service Mesh](../../mspider/01Intro/WhatismSpider.md) supports several user roles:

-Admin
-Workspace Admin
- Workspace Editor
- Workspace Viewer

<!--
You have permission to use `&check;`, but you don't have permission to use `&cross;`
-->

The specific permissions of these roles are shown in the table below.

| Menu Objects | Actions | Admin | Workspace Admin | Workspace Editor | Workspace Viewer |
| ---------------- | -------------- | ------- | --------- ------ | ---------------- | ---------------- |
| Service Mesh List | [Create Mesh](../../mspider/03UserGuide/servicemesh/create-mesh.md) | &check; | &cross; | &cross; | &cross; |
| | Edit mesh | &check; | &check; | &check; | &cross; |
| | [Delete Mesh](../../mspider/03UserGuide/servicemesh/delete.md) | &check; | &check; | &cross; | &cross; |
| | [View Mesh](../../mspider/03UserGuide/servicemesh/README.md) | &check; | &check; | &check; | &check; |
| mesh Overview | View | &check; | &check; | &check; | &check; |
| Service List | [Jump to Governance Page](../../mspider/03UserGuide/01ServiceList/README.md) | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Service Entry | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Virtual Service | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| target rule | create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Gateway Rules | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Peer Authentication | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Request Authentication | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Authorization Policies | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Namespace Sidecar Management | Enable Injection | &check; | &check; | &check; | &cross; |
| | disable injection | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Workload Sidecar Management | Enable Injection | &check; | &check; | &check; | &cross; |
| | disable injection | &check; | &check; | &check; | &cross; |
| | Sidecar Resource Setup | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Global Sidecar Injection | Enable Injection | &check; | &check; | &check; | &cross; |
| | disable injection | &check; | &check; | &check; | &cross; |
| | Sidecar Resource Setup | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Cluster Management | Cluster Access | &check; | &check; | &cross; | &cross; |
| | Cluster removal | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Mesh Gateway | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Istio Resource Management | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| TLS Certificate Management | Create | &check; | &check; | &cross; | &cross; |
| | edit | &check; | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| System Upgrade | Istio Upgrade | &check; | &check; | &check; | &cross; |
| | sidecar upgrade | &check; | &check; | &check; | &cross; |
| | View | &check; | &check; | &check; | &check; |
| Workspace Management | Bindings | &check; | &cross; | &cross; | &cross; |
| | Unbind | &check; | &cross; | &cross; | &cross; |
| | View | &check; | &check; | &check; | &check; |