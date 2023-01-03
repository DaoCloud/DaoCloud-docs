# Description of workspace permissions

The workspace has permission mapping and resource isolation capabilities, and can map the permissions of users/groups in the workspace to the resources under it.
If the user/group has the Workspace Admin role in the workspace and the resource Namespace is bound to the workspace-resource group, the user/group will become Namespace Admin after mapping.

!!! note

    The permission mapping capability of the workspace will not be applied to shared resources, because sharing is to share the cluster usage permissions to multiple workspaces, rather than assigning management permissions to the workspaces, so permission inheritance and role mapping will not be implemented.

## Application scenarios

Resource isolation is achieved by binding resources to different workspaces. Therefore, resources can be flexibly allocated to each workspace (tenant) with the help of permission mapping, resource isolation, and resource sharing capabilities.

Generally applicable to the following 2 scenarios:

1. To operate and maintain two common clusters, namely cluster 01 and cluster 02, you want to assign cluster 01 to department A (workspace A) for management and use, and assign cluster 02 to department B (workspace B) for management and use.

    At this point you can bind clusters 01 and 02 to the resource groups of workspaces A and B respectively.

2. O&M a high-availability cluster 03, and hope to assign it to department A (workspace A) and department B (workspace B) at the same time, and limit department A to only use 100-core CPU, and department B to only use 50-core CPU .

    At this point, cluster 03 can be shared to workspaces A and B respectively, and resource quotas can be set separately.

| Feature Name | Object | Action | Workspace Admin | Workspace Editor | Workspace Viewer |
| :----------------------------------------- | :-------- ----- | :--- | :------------- | :--------------- | :----- ---------- |
| workspace | on the workspace itself | view | &check; | &check; | &check; |
| Authorization | &check; | &cross; | &cross; | | |
| Modify Alias ​​| &check; | &check; | &cross; | | |
| Workspace - Resource Group | View | &check; | &check; | &check; | |
| resource binding | &check; | &cross; | &cross; | | |
| Unbind | &check; | &cross; | &cross; | | |
| Workspace - Shared Resources | View | &check; | &check; | &check; | |
| Add Share | &check; | &cross; | &cross; | | |
| Unshare | &check; | &cross; | &cross; | | |
| Resource Quota | &check; | &cross; | &cross; | | |
| Use shared resources (Create Namespace in [Application Workbench](../../../amamba/03UserGuide/Namespace/namespace.md)) | &check; | &cross; | &cross; | | |