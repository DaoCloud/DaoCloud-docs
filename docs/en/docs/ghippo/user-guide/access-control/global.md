# System Roles

## Use cases

DCE 5.0 provides predefined system roles to help users simplify the process of role permission usage.

!!! note

    DCE 5.0 provides three types of system roles: platform role, workspace role, and folder role.

    - Platform role: has proper permissions for all related resources on the platform. Please go to user/group page for authorization.
    - Workspace role: has proper permissions for a specific workspace. Please go to the specific workspace page for authorization.
    - Folder role: has proper permissions for a specific folder, subfolder, and resources under its workspace. Please go to the specific folder page for authorization.

## Platform Roles

Five system roles are predefined in Access Control: Admin, IAM Owner, Audit Owner, Kpanda Owner, and Workspace and Folder Owner. These five roles are created by the system and cannot be modified by users. The proper permissions of each role are as follows:

| Role Name | Role Type | Module | Role Permissions |
| --- | --- | --- | --- |
| Admin | System role | All | Platform administrator, manages all platform resources, represents the highest authority of the platform. |
| IAM Owner | System role | Access Control | Administrator of Access Control, has all permissions under this service, such as managing users/groups and authorization. |
| Audit Owner | System role | Audit Log | Administrator of Audit Log, has all permissions under this service, such as setting audit log policies and exporting audit logs. |
| Kpanda Owner | System role | Container Management | Administrator of Container Management, has all permissions under this service, such as creating/accessing clusters, deploying applications, granting cluster/namespace-related permissions to users/groups. |
| Workspace and Folder Owner | System role | Workspace and Folder | Administrator of Workspace and Folder, has all permissions under this service, such as creating folders/workspaces, authorizing folder/workspace-related permissions to users/groups, using features such as Workbench and microservice engine under the workspace. |

## Workspace Roles

Three system roles are predefined in Access Control: Workspace Admin, Workspace Editor, and Workspace Viewer. These three roles are created by the system and cannot be modified by users. The proper permissions of each role are as follows:

| Role Name | Role Type | Module | Role Permissions |
| --- | --- | --- | --- |
| Workspace Admin | System role | Workspace | Administrator of a workspace, with management permission of the workspace. |
| Workspace Editor | System role | Workspace | Editor of a workspace, with editing permission of the workspace. |
| Workspace Viewer | System role | Workspace | Viewer of a workspace, with readonly permission of the workspace. |

## Folder Roles

Three system roles are predefined in Access Control: Folder Admin, Folder Editor, and Folder Viewer. These three roles are created by the system and cannot be modified by users. The proper permissions of each role are as follows:

| Role Name | Role Type | Module | Role Permissions |
| --- | --- | --- | --- |
| Folder Admin | System role | Workspace | Administrator of a folder and its subfolders/workspaces, with management permission. |
| Folder Editor | System role | Workspace | Editor of a folder and its subfolders/workspaces, with editing permission. |
| Folder Viewer | System role | Workspace | Viewer of a folder and its subfolders/workspaces, with readonly permission. |
