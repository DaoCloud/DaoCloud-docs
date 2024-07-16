# 资源绑定权限说明

假如用户小明（“小明”代表任何有资源绑定需求的用户）已经具备了
[Workspace Admin 角色](../access-control/role.md#_4)或已通过[自定义角色](../access-control/custom-role.md)授权，
同时自定义角色中包含[工作空间的“资源绑定”权限](./ws-permission.md#_3)，希望将某个集群或者某个命名空间绑定到其所在的工作空间中。

要将集群/命名空间资源绑定到工作空间，不仅需要该[工作空间的“资源绑定”权限](./ws-permission.md#_3)，还需要
[Cluster Admin](../../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin) 的资源权限。

## 给小明授权

1. 使用[平台 Admin 角色](../access-control/role.md#_2)，
   在 **工作空间** -> **授权** 页面给小明授予 Workspace Admin 角色。

    ![资源绑定](../../images/wsbind1.png)

1. 然后在 **容器管理** -> **权限管理** 页面，通过 **添加授权** 将小明授权为 Cluster Admin。

    ![集群授权1](../../images/wsbind2.png)

    ![集群授权2](../../images/wsbind3.png)

## 绑定到工作空间

使用小明的账号登录 DCE 5.0，在 **容器管理** -> **集群列表** 页面，通过 **绑定工作空间** 功能，
小明可以将指定集群绑定到自己的工作空间中。

!!! note

    小明能且只能在[容器管理模块](../../../kpanda/intro/index.md)将集群或者该集群下的命名空间绑定到某个工作空间，无法在全局管理模块完成此操作。

![cluster绑定](../../images/wsbind4.png)

绑定命名空间到工作空间也至少需要 Workspace Admin + Cluster Admin 权限。

![ns绑定](../../images/wsbind5.png)
