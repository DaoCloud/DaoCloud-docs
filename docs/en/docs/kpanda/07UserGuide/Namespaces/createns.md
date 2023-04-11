# Create namespace

A namespace is an abstraction used for resource isolation in Kubernetes. This article will introduce how to create a namespace.

## Prerequisites

- The container management platform [has joined the Kubernetes cluster](../Clusters/JoinACluster.md) or [has created the Kubernetes cluster](../Clusters/CreateCluster.md), and can access the UI interface of the cluster.
- Completed a [Namespace Creation](../Namespaces/createtens.md), [User Creation](../../../ghippo/04UserGuide/01UserandAccess/User.md), and created a Grant [`NS Admin`](../Permissions/PermissionBrief.md#ns-admin) or higher permissions, please refer to [Namespace Authorization](../Permissions/Cluster-NSAuth.md) for details.

## Steps

1. Click the name of the target cluster to enter `Cluster Details`.

    

2. Click `Namespace` on the left navigation bar to enter the namespace management page, and click the `Create` button on the right side of the page.

    

3. Fill in the name of the namespace, configure the workspace and labels (optional settings), and click `OK`.

    !!! info

        Workspaces are primarily used to divide groups of resources and grant users (groups of users) different access rights to that resource. For a detailed description of the workspace, please refer to [Workspace and Hierarchy](../../../ghippo/04UserGuide/02Workspace/Workspaces.md).

    

4. Click `OK` to complete the creation of the namespace. On the right side of the namespace list, click `⋮`, and you can choose to update, delete, and more from the pop-up menu.

    