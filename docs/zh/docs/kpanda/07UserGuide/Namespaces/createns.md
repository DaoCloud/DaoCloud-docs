# 创建命名空间

命名空间是 Kubernetes 中用来进行资源隔离的一种抽象，本文将介绍如何创建命名空间。

## 前提条件

- 容器管理平台[已接入 Kubernetes 集群](../Clusters/JoinACluster.md)或者[已创建 Kubernetes 集群](../Clusters/CreateCluster.md)，且能够访问集群的 UI 界面。
- 已完成一个[命名空间的创建](../Namespaces/createns.md)、[用户的创建](../../../ghippo/04UserGuide/01UserandAccess/User.md)，并为用户授予 [`NS Admin`](../Permissions/PermissionBrief.md#ns-admin) 或更高权限，详情可参考[命名空间授权](../Permissions/Cluster-NSAuth.md)。

## 操作步骤

1. 点击目标集群的名称，进入`集群详情`。

    ![ns](../../images/crd01.png)

2. 在左侧导航栏点击`命名空间`，进入命名空间管理页面，点击页面右侧的`创建`按钮。

    ![ns](../../images/ns01.png)

3. 填写命名空间的名称，配置工作空间和标签（可选设置），然后点击`确定`。

    !!! info

        工作空间主要用于划分资源组并为用户（用户组）授予对该资源的不同访问权限。有关工作空间的详细说明，可参考[工作空间与层级](../../../ghippo/04UserGuide/02Workspace/Workspaces.md)。

    ![ns](../../images/ns02.png)

4. 点击`确定`，完成命名空间的创建。在命名空间列表右侧，点击 `⋮`，可以从弹出菜单中选择更新、删除等更多操作。

    ![ns](../../images/ns03.png)
