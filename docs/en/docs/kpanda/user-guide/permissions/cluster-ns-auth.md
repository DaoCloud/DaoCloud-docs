# Cluster and Namespace Authorization

Container management implements authorization based on global authority management and global user/group management. If you need to grant users the highest authority for container management (can create, manage, and delete all clusters), refer to [What are Access Control](../../../ghippo/user-guide/access-control/iam.md).

## Prerequisites

Before authorizing users/groups, complete the following preparations:

- The user/group to be authorized has been created in the global management, refer to [User](../../../ghippo/user-guide/access-control/user.md).

- Only [ __Kpanda Owner__ ](../../../ghippo/user-guide/access-control/global.md) and [`Cluster Admin`](permission-brief.md) of the current cluster have Cluster authorization capability. For details, refer to [Permission Description](permission-brief.md).

- only [ __Kpanda Owner__ ](../../../ghippo/user-guide/access-control/global.md), [`Cluster Admin`](permission-brief.md) for the current cluster, [`NS Admin`](permission-brief.md) of the current namespace has namespace authorization capability.

## Cluster Authorization

1. After the user logs in to the platform, click __Privilege Management__ under __Container Management__ on the left menu bar, which is located on the __Cluster Permissions__ tab by default.

    

2. Click the __Add Authorization__ button.

    

3. On the __Add Cluster Permission__ page, select the target cluster, the user/group to be authorized, and click __OK__ .

    Currently, the only cluster role supported is __Cluster Admin__ . For details about permissions, refer to [Permission Description](permission-brief.md). If you need to authorize multiple users/groups at the same time, you can click __Add User Permissions__ to add multiple times.

    

4. Return to the cluster permission management page, and a message appears on the screen: __Cluster permission added successfully__ .

    

## Namespace Authorization

1. After the user logs in to the platform, click __Privilege Management__ under __Container Management__ on the left menu bar, and click the __Namespace Permissions__ tab.

    

2. Click the __Add Authorization__ button. On the __Add Namespace Permission__ page, select the target cluster, target namespace, and user/group to be authorized, and click __OK__ .

    The currently supported namespace roles are NS Admin, NS Edit, and NS View. For details about permissions, refer to [Permission Description](permission-brief.md). If you need to authorize multiple users/groups at the same time, you can click __Add User Permission__ to add multiple times. Click __OK__ to complete the permission authorization.

    

3. Return to the namespace permission management page, and a message appears on the screen: __Cluster permission added successfully__ .

    

    !!! tip

        If you need to delete or edit permissions later, you can click __⋮__ on the right side of the list and select __Edit__ or __Delete__ .

        