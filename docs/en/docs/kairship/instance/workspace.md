---
hide:
  - toc
---

# Workspace

Workspace is a hierarchical mapping designed for global resource management in DCE 5.0. A workspace can be used to provide resources for each project under a department. Administrators map the relationships between departments and projects in the enterprise to folders and workspace. For more information about workspace, see [Workspace and Folder](../../ghippo/user-guide/workspace/workspace.md).

## Bind/Unbind Workspace

In the Multicloud Management module, admin of the DCE 5.0 platform can bind multicloud instances or multicloud namespaces to a workspace.

After the binding, users of that workspace can operate instances or namespaces within their permission scope.

1. Click `Workspace` in the upper-right corner of the homepage of the Multicloud Management module.

    ![Management entrance.png](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/ws01.png)

2. Check the binding status of multicloud instances/namespaces, then click the `ⵗ` action button and select `Bind Workspace` or `Unbind Workspace` as needed.

    ![Management interface](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/ws02.png)

3. Select which workspace to bind when binding, or just confirm your action when unbinding.

    ![Binding/Unbinding](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/ws03.png)
    ![Binding/Unbinding](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/ws04.png)

!!! note

    - After multicloud instances/namespaces are bound to a workspace, all working clusters under the multicloud instance will automatically synchronize this binding relationship, allowing users in that workspace to operate the corresponding resources in the cluster.
    - After the binding, you can enter the `Workspace and Folder` -> `Resource Group` section of the DCE 5.0 Global Management module to view the resources. For more details, see [Resource Quotas](../../ghippo/user-guide/workspace/quota.md#_1).
    - Currently, one multicloud instance/namespace can be bound to ONLY ONE workspace. The mapping relationship is one-to-one.

        - This ensures stable matching of resources and permissions, preventing resource and permission conflicts.
        - In the future, the multicloud instance or namespace can be bound to multiple workspaces as shared resources. This feature is currently under development, stay tuned.
