---
MTPE: WANG0608GitHub
date: 2024-07-16
---

# Resource Binding Permission Instructions

If a user John ("John" represents any user who is required to bind resources) has  
the [Workspace Admin role](../access-control/role.md#workspace-role-authorization-methods) assigned or has been granted proper permissions through a [custom role](../access-control/custom-role.md), 
which includes the [Workspace's "Resource Binding" Permissions](./ws-permission.md#description-of-workspace-permissions), and wants to bind a specific cluster or namespace to the workspace.

To bind cluster/namespace resources to a workspace, not only the [workspace's "Resource Binding" permissions](./ws-permission.md#description-of-workspace-permissions) are required,
but also the permissions of [Cluster Admin](../../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin).

## Granting Authorization to John

1. Using the [Platform Admin Role](../access-control/role.md#workspace-role-authorization-methods),
   grant John the role of Workspace Admin on the **Workspace** -> **Authorization** page.

    ![Resource Binding](../../images/wsbind1.png)

1. Then, on the **Container Management** -> **Permissions** page, authorize John as a Cluster Admin by **Add Permission**.

    ![Cluster Permissions1](../../images/wsbind2.png)

    ![Cluster Permissions2](../../images/wsbind3.png)

## Binding to Workspace

Using John's account to log in to DCE 5.0, on the **Container Management** -> **Clusters** page, 
 John can bind the specified cluster to his own workspace by using the **Bind Workspace** button.

!!! note

    John can only bind clusters or namespaces to a specific workspace in the [Container Management module](../../../kpanda/intro/index.md), and cannot perform this operation in the Global Management module.

![cluster banding](../../images/wsbind4.png)

To bind a namespace to a workspace, you must have at least Workspace Admin and Cluster Admin permissions.

![cluster banding](../../images/wsbind5.png)