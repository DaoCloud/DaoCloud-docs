# Role and permission management

A role corresponds to a set of permissions. Permissions determine the actions that can be performed on a resource. Granting a role to a user grants all the permissions included in the role.

There are the following three modes of rights management, which can flexibly and effectively solve your use problems on rights:

- Global management mode
- Submodule management mode
- Resource-based management model

## Global management mode

The global management mode refers to the way you configure permissions for users (groups) through system roles in the global management module.
The platform predefines an administrator role for each sub-module, which is used to realize the block management of sub-modules.
For example, the IAM Owner of access control, the Kpanda Owner of container management, etc., each sub-module administrator has the highest authority of the module.
The submodule administrator role needs to be configured in the global management module, which can be obtained in the following ways:

- Find the user in the user list of `Global Management` -> `Access Control` -> `User`; click `...`, select `Authorization`, and assign the user a predefined submodule of the system Administrator privileges.

    

- Create a group in the group list of `Global Management` -> `Access Control` -> `group`, add the user to the group, and authorize the group (the specific operation is: in the group list Find the group, click `...`, select `Authorization`, and give the group the pre-defined sub-module administrator rights of the system).

    

- In the role list of `Global Management` -> `Users and Access Control` -> `Roles`, find the corresponding submodule administrator role, click the role name to enter the details, click the `Associate Member` button, select the user or The group to which the user belongs, click `OK`.

    

Submodules that support this mode: Access Control (IAM), Audit Log (Audit), Container Management (Kpanda)
At the same time, the administrator role (Admin) of the platform can also be authorized through the above methods



!!! note

    - Admin platform administrator
    - IAM Owner access control module administrator
    - Kpanda Owner container management module administrator
    - Audit Owner Audit log module administrator

## Submodule management mode

The sub-module management mode means that you can assign different resources to different users on demand through sub-modules, and at the same time, different users can have different usage permissions for the same resource.
The platform predefines three roles for each resource in the submodule, namely Admin, Editor and Viewer.

- The Admin role has administrative rights to the resource and can authorize the resource to be used by others;
- The Editor role has permission to use resources and can edit and view resources;
- The Viewer role has view-only access to resources.

For example, the NS Admin role in Namespace01 under cluster A in container management can manage, edit, and view Namespace01, and can authorize other users to NS Admin, NS Editor, and NS Viewer roles.
The NS Editor role of Namespace01 can edit and view Namespace01, and can deploy applications.
The Viewer role for Namespace01 can only view Namespace01.

Submodules that support this mode: [Container Management](../../../kpanda/intro/what.md)

You can go to `Container Management` -> `Privilege Management`, select `Add Authorization` to grant Cluster or Namespace permissions to users/groups.



!!! note

    In this manual, Cluster refers to cluster; NS is the abbreviation of Namespace, that is, namespace.

## Resource-based management mode

1. The resource-based management mode depends on the workspace. Through the centralized and unified access control strategy, the role authority of the user/group in the workspace is applied to the resources under the workspace, and the cross-submodule authorization user (group) is realized. ) for resource access.
    For example, user A has the role of Workspace Editor in workspace 01, then user A has Editor permission for all resources under workspace 01.
    Workspaces are often used to refer to a project or environment, and the resources in each workspace are physically isolated from those in other workspaces.
    You can grant users (groups) different access rights to the same set of resources through "Authorization" in the workspace.
    At the same time, the workspace contains multiple types of resources in different modules, and different types of resources have different presentation methods in the workspace.

    - Module Name: [App Workbench](../../../amamba/intro/what.md), [Microservice Engine](../../../skoala/intro/features.md ), [middleware](../../../middleware/what.md)

        Because these modules do not support the authorization methods of the global management mode and the sub-module management mode, they only rely on the workspace to obtain authorization.
        Therefore, all resources are created under the workspace, and the resources are automatically bound to the workspace after creation to ensure that these resources can be authorized for use after creation.
        After these resources are created, they will not be automatically displayed in the resource group or shared resources in the workspace, but can only be displayed in the resource list of each module.
        (Any role with Workspace can enter the above modules)

    - [Container Management](../../../kpanda/intro/what.md)

        Container management supports three authorization modes: global management mode, sub-module management mode and resource-based management.
        Therefore, in the container management module, you can choose to grant the user/group the Kpanda Owner role through the access control module, or grant the user/group the corresponding permission for a resource through the permission management function of the container management module itself, or by assigning the resource ( Cluster or Namespace) is bound to the workspace to inherit the role permissions of the user/group in the workspace.
        Since there are two states of bound and unbound workspace for resources in container management, in order to distinguish the two different states, the resources bound to the workspace will be presented in the workspace-resource group, and the workspace - Both the resource group and the resource list managed by the container provide the resource binding/unbinding entry.
        (Admin role or Workspace admin + Kpanda Owner role can perform resource binding)

    - [Service Mesh](../../../mspider/intro/what.md)

        Due to the particularity of its own resources, the service mesh also has two states: bound and unbound.
        Therefore, you can manage the resources in the service mesh through the Admin role, or bind the resources (Mesh or Mesh-Namespace) to the workspace, so that users/groups can obtain the permissions of the resources in the service mesh through the workspace, and are bound The specified resources will be displayed in the resource group of the workspace.
        Currently only the service mesh module provides a resource binding entry. (Admin role can perform resource binding)

2. Sub-modules that support this mode: App Workbench, microservice engine, middleware, container management, and service mesh.

3. You can create a workspace through `Global Management` -> `Workspace and Hierarchy`, and grant users/groups Workspace Admin, Workspace Editor, and Workspace Viewer roles in `Workspace-Authorization`.

    

!!! note

    Resource (Resource) generally refers to the resources created by each sub-module on the DCE platform, which is the specific data to complete the authorization. Usually a resource describes one or more operation objects, and each sub-module has its own resource and corresponding resource definition details.
    Such as cluster, Namespace, gateway, etc. The owner of the resource is the main account Admin. Admin has the authority to create/manage/delete resources in each sub-module. Ordinary users will not automatically have access to resources without authorization, and need to be authorized by the resource owner.
    Usually, the resource owner adds a group of resources to a certain workspace, and then authorizes users (groups) through the workspace, so that the user/group can obtain the operation authority of certain resources.
