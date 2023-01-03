# resource limit

Sharing resources does not mean that the sharers can use the shared resources without restriction.
Admin, Kpanda Owner and Workspace Admin can limit the maximum usage of a user through the `Resource Quota` function in shared resources.
Unrestricted means unlimited use.

- CPU request (Core)
- CPU limit (Core)
- memory request (MB)
- Memory limit (MB)
- Total storage requests (GB)
- volume claim(s)

A resource (cluster) can be shared by multiple workspaces, and a workspace can also use resources in multiple shared clusters at the same time.

## Resource groups and shared resources

Both shared resources and cluster resources in resource groups come from [Container Management](../../../kpanda/03ProductBrief/WhatisKPanda.md), but cluster binding and sharing to the same workspace will produce two very different effect.

1. Binding resources

    Make the users/groups in the workspace have full management and usage rights of the cluster, and Workspace Admin will be mapped to Cluster Admin.
    Workspace Admin can enter [Container Management Module](../../../kpanda/07UserGuide/Permissions/PermissionBrief.md) to manage the cluster.

    ![Resource Group](../../images/quota01.png)

    !!! note

        Currently, the container management module does not have the roles of Cluster Editor and Cluster Viewer, so Workspace Editor and Workspace Viewer cannot be mapped yet.

2. Add shared resources

    Make the user/group in the workspace have the permission to use the cluster resources, and can use the resource quota to go to [Create a namespace (Namespace) in the application workbench](#_2).

    ![Shares](../../images/quota02.png)

    Unlike resource groups, when a cluster is shared to a workspace, the user's role in the workspace will not be mapped to the resources, so Workspace Admin will not be mapped to Cluster admin.

This section presents 3 scenarios related to resource quotas.

## Create namespace

Resource quotas are involved when creating a namespace.

1. Add a shared cluster in workspace ws01.

    ![New shared cluster](../../images/quota03.png)

1. Select the workspace ws01 and the shared cluster in the application workbench, and create a namespace ns01.

    ![Create Namespace](../../images/quota04.png)

    - If no resource quota is set in the shared cluster, no resource quota can be set when creating a namespace.
    - If the resource quota has been set in the shared cluster (for example, CPU request = 100 core), then `CPU request ≤ 100 core` when creating the namespace.

## Namespaces are bound to workspaces

Prerequisite: Workspace ws01 has added a shared cluster, and the operator is Workspace Admin + Kpanda Owner or Admin role.

The following two binding methods have the same effect.

- Bind the created namespace ns01 to ws01 in container management

    ![Bind to workspace](../../images/quota05.png)

    - If the resource quota is not set in the shared cluster, the namespace ns01 can be successfully bound regardless of whether the resource quota is set.
    - If the resource quota `CPU request = 100 core` has been set in the shared cluster, the namespace ns01 must satisfy `CPU request ≤ 100 core` to bind successfully.

- In Global Admin, bind namespace ns01 to ws01

    ![Bind to workspace](../../images/quota06.png)

    - If the resource quota is not set in the shared cluster, the namespace ns01 can be successfully bound regardless of whether the resource quota is set.
    - If the resource quota `CPU request = 100 core` has been set in the shared cluster, the namespace ns01 must satisfy `CPU request ≤ 100 core` to bind successfully.

## Unbind the namespace from the workspace

The following two unbinding methods have the same effect.

- unbind namespace ns01 from workspace ws01 in container management

    ![Bind to workspace](../../images/quota07.png)

    - If no resource quota is set in the shared cluster, no matter whether the namespace ns01 has resource quota set or not, unbinding will not affect the resource quota.
    - If the resource quota `CPU request = 100 core` has been set in the shared cluster, and the resource quota has also been set in the namespace ns01, the corresponding resource quota will be released after unbinding.

- unbind namespace ns01 from workspace ws01 in global admin

    ![Bind to workspace](../../images/quota08.png)

    - If no resource quota is set in the shared cluster, no matter whether the namespace ns01 has resource quota set or not, it will not affect the resource quota after being unbound.
    - If the resource quota `CPU request = 100 core` has been set in the shared cluster, and the resource quota has also been set in the namespace ns01, the corresponding resource quota will be released after unbinding.