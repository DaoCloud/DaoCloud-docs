# bind workspace

Multicloud instances and multicloud namespaces can be bound to a [workspace](../ghippo/user-guide/workspace/workspace.md).
After binding to the workspace, users with relevant permissions can manage these resources in the corresponding workspace.

**Precautions**

- The current operating user should have Admin or Workspace Admin privileges.
  For more instructions on permissions, please refer to [Role and Permission Management](../ghippo/user-guide/access-control/role.md) and [Workspace Permissions](../ghippo/user-guide/workspace/ws-permission.md).
- A multicloud instance/namespace can only be bound to one workspace.

## Bind multicloud instance and workspace

1. Enter the Multicloud Management module, click `Workspace` in the upper right corner of the page,

    <!--screenshot-->

2. Enter the workspace page, select the target instance on the multicloud instance list page, click `ⵗ`, and select `Bind to Workspace`.

    <!--screenshot-->

3. Select the workspace you want to bind and click `OK`.

    <!--screenshot-->

4. At this point, the multicloud instance has been bound to `kairship-ws`.
    Click `Global Management` to enter the Workspace and Folder page, select `kairship-ws` resource group, you can see that `k-kairship-test01` has been bound.

    <!--screenshot-->

## Bind multicloud namespace and workspace

1. Enter the Multicloud Management module, click the workspace in the upper right corner of the page, and select the `Multicloud instance` tab.

    <!--screenshot-->

2. In the multicloud namespace tab page, select a multicloud namespace `k-kairship-test01-95fzz` of a multicloud instance `k-kairship-test01`, click `ⵗ` on the right, and select `Bind to Workspace `.

    <!--screenshot-->

3. Select the workspace you want to bind and click `OK`.

    <!--screenshot-->

4. At this point, the multicloud namespace has been bound to `kairship-ws`.
    Click `Global Management` to enter the Workspace and Folder page, select `kairship-ws` resource group, you can see that `k-kairship-test01-95fzz` has been bound.

    <!--screenshot-->