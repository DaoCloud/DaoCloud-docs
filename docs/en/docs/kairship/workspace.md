# bind workspace

Multi-cloud instances and multi-cloud namespaces can be bound to a [workspace](../ghippo/user-guide/workspace/workspace.md).
After binding to the workspace, users with relevant permissions can manage these resources in the corresponding workspace.

**Precautions**

- The current operating user should have Admin or Workspace Admin privileges.
  For more instructions on permissions, please refer to [Role and Permission Management](../ghippo/user-guide/access-control/role.md) and [Workspace Permissions](../ghippo/user-guide/workspace/ws-permission.md).
- A multi-cloud instance/namespace can only be bound to one workspace.

## Bind multi-cloud instance and workspace

1. Enter the multi-cloud orchestration module, click `Workspace` in the upper right corner of the page,

    <!--screenshot-->

2. Enter the workspace page, select the target instance on the multi-cloud instance list page, click `ⵗ`, and select `Bind to Workspace`.

    <!--screenshot-->

3. Select the workspace you want to bind and click `OK`.

    <!--screenshot-->

4. At this point, the multi-cloud instance has been bound to `kairship-ws`.
    Click `Global Management` to enter the workspace and hierarchy page, select `kairship-ws` resource group, you can see that `k-kairship-test01` has been bound.

    <!--screenshot-->

## Bind multi-cloud namespace and workspace

1. Enter the multi-cloud orchestration module, click the workspace in the upper right corner of the page, and select the `Multi-cloud instance` tab.

    <!--screenshot-->

2. In the multi-cloud namespace tab page, select a multi-cloud namespace `k-kairship-test01-95fzz` of a multi-cloud instance `k-kairship-test01`, click `ⵗ` on the right, and select `Bind to Workspace `.

    <!--screenshot-->

3. Select the workspace you want to bind and click `OK`.

    <!--screenshot-->

4. At this point, the multi-cloud namespace has been bound to `kairship-ws`.
    Click `Global Management` to enter the workspace and hierarchy page, select `kairship-ws` resource group, you can see that `k-kairship-test01-95fzz` has been bound.

    <!--screenshot-->