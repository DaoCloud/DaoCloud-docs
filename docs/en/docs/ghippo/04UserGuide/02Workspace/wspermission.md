# Description of workspace permissions

The workspace has permission mapping and resource isolation capabilities, and can map the permissions of users/groups in the workspace to the resources under it.
If the user/group has the Workspace Admin role in the workspace and the resource Namespace is bound to the workspace-resource group, the user/group will become Namespace Admin after mapping.

!!! note

    The permission mapping capability of the workspace will not be applied to shared resources, because sharing is to share the cluster usage permissions to multiple workspaces, rather than assigning management permissions to the workspaces, so permission inheritance and role mapping will not be implemented.

## Application scenarios

Resource isolation is achieved by binding resources to different workspaces. Therefore, resources can be flexibly allocated to each workspace (tenant) with the help of permission mapping, resource isolation, and resource sharing capabilities.

Generally applicable to the following two scenarios:

- Cluster one-to-one

     | Ordinary Cluster | Department/Tenant (Workspace) | Purpose |
     | -------- | ---------------- | -------- |
     | Cluster 01 | A | Administration and Usage |
     | Cluster 02 | B | Administration and Usage |

- Cluster one-to-many

     | Cluster | Department/Tenant (Workspace) | Resource Quota |
     | ------- | ---------------- | ---------- |
     | Cluster 01 | A | 100 core CPU |
     | | B | 50-core CPU |

## Permission description

| Action Objects | Operations | Workspace Admin | Workspace Editor | Workspace Viewer |
| :------- | :---------------- | :-------------- | :----- ---------- | :--------------- |
| itself | view | &check; | &check; | &check; |
| - | Authorization | &check; | &cross; | &cross; |
| - | Modify Alias | &check; | &check; | &cross; |
| Resource Group | View | &check; | &check; | &check; |
| - | resource binding | &check; | &cross; | &cross; |
| - | unbind | &check; | &cross; | &cross; |
| Shared Resources | View | &check; | &check; | &check; |
| - | Add Share | &check; | &cross; | &cross; |
| - | Unshare | &check; | &cross; | &cross; |
| - | Resource Quota | &check; | &cross; | &cross; |
| - | Using Shared Resources [^1] | &check; | &cross; | &cross; |

[^1]:
     Authorized users can go to modules such as workbench, microservice engine, middleware, multicloud orchestration, and service mesh to use resources in the workspace.
     For the operation scope of the roles of Workspace Admin, Workspace Editor, and Workspace Viewer in each module, please refer to the permission description:

     - [Workbench Permissions](../../permissions/amamba.md)
     - [Service Mesh Permissions](../../permissions/mspider.md)
     - [Middleware permissions](../../permissions/mcamel.md)
     - [Microservice Engine Permissions](../../permissions/skoala.md)
     - [Container Management Permissions](../../../kpanda/07UserGuide/Permissions/PermissionBrief.md)