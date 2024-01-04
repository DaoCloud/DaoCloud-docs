# 工作空间

工作空间是 DCE 5.0 为管理全局资源而设计的一种资源层级映射。工作空间可以理解为部门下的项目，管理员通过文件夹和工作空间映射企业中的部门和项目关系。有关工作空间的详细说明，可参考[工作空间与层级](../ghippo/user-guide/workspace/workspace.md)。

## 注意事项

- 当前操作用户应具有 Admin 或 Workspace Admin 权限。有关权限的更多说明，可参考[角色和权限管理](../ghippo/user-guide/access-control/role.md)和[工作空间权限](../ghippo/user-guide/workspace/ws-permission.md)。
- 多云实例/命名空间与工作空间绑定之后，多云实例下的所有工作集群会自动同步这种绑定关系，允许对应工作空间的用户在集群中操作对应资源。
- 绑定之后，可以进入全局管理模块的 __工作空间与层级__ -> __资源组__ 查看该资源，详情可参考[资源配额](../ghippo/user-guide/workspace/quota.md#_1)
- 目前一个多云实例/命名空间只能绑定到一个工作空间，映射关系为一对一。

    - 这样可以确保资源与权限的稳定匹配，防止资源冲突和权限冲突。
    - 后续会支持将多云实例或命名空间作为共享资源绑定到多个工作空间。此项功能正在开发中，敬请期待。

## 绑定/解绑工作空间

在多云编排模块中，DCE 5.0 平台的 admin 管理员可以将多云实例或多云命名空间以资源的形式绑定到某个工作空间。

多云实例或命名空间被绑定到工作空间之后，工作空间内的用户就能直接获得该实例或命名空间的相应权限。

1. 在多云编排模块的首页右上角点击 __工作空间__ 。

    ![管理入口.png](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/20221128014958.png)

2. 点击 __多云实例__ 或 __多云命名空间__ 页签，查看所有多云实例和命名空间当前的绑定状态。
3. 在目标实例/命名空间的最右侧点击更多操作按钮，选择 __绑定工作空间__ / __解绑工作空间__ 。

    ![管理界面](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/workspace01.png)

4. 绑定时选择需要将该实例/命名空间和哪个工作空间绑定。解绑时确认操作即可。

    ![绑定/解绑](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/workspace02.png)
    ![绑定/解绑](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/ws04.png)
