# 用户组

用户组是用户的集合，用户可以通过加入用户组，继承用户组的角色权限。通过用户组批量地给用户进行授权，可以更好地管理用户及其权限。

## 适用场景

当用户权限发生变化时，只需将其移到相应的用户组下，不会对其他用户产生影响。

当用户组的权限发生变化时，只需修改用户组的角色权限，即可应用到组内的所有用户。

## 创建用户组

前提：拥有平台管理员 Admin 权限或者用户与访问控制管理员 IAM Owner 权限。

1. 管理员进入 __用户与访问控制__ ，选择 __用户组__ ，进入用户组列表，点击右上方的 __创建用户组__ 。

    ![创建用户组](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/group00.png)

2. 在 __创建用户组__ 页面填写用户组信息。

    ![创建用户组](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/group01.png)

3. 点击 __确定__ ，创建用户组成功，返回用户组列表页面。列表中的第一行是新创建的用户组。

## 为用户组授权

前提：该用户组已存在。

1. 管理员进入 __用户与访问控制__ ，选择 __用户组__ ，进入用户组列表，点击 __...__ -> __授权__ 。

    ![创建用户组按钮](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/group02.png)

2. 在 __授权__ 页面勾选需要的角色权限（可多选）。

    ![创建用户组按钮](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/group03.png)

3. 点击 __确定__ 完成为用户组的授权。自动返回用户组列表，点击某个用户组，可以查看用户组被授予的权限。

    ![创建用户组按钮](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/group04.png)

## 给用户组添加用户

1. 管理员进入 __用户与访问控制__ ，选择 __用户组__ 进入用户组列表，在某个用户组右侧，点击 __...__ -> __添加用户__ 。

    ![添加用户](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/group05.png)

2. 在 __添加用户__ 页面点选需要添加的用户（可多选）。若没有可选的用户，点击 __前往创建新用户__ ，先前往创建用户，再返回该页面点击 __刷新__ 按钮，显示刚创建的用户。

    ![选择用户](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/group06.png)

3. 点击 __确定__ 完成给用户组添加用户。

!!! note

    用户组中的用户会继承用户组的权限；可以在用户组详情中查看加入该组的用户。

## 删除用户组

说明：删除用户组，不会删除组内的用户，但组内用户将无法再继承该组的权限

1. 管理员进入 __用户与访问控制__ ，选择 __用户组__ 进入用户组列表，在某个用户组右侧，点击 __...__ -> __删除__ 。

    ![删除按钮](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/deletegroup01.png)

2. 点击 __移除__ 删除用户组。

    ![确认删除](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/deletegroup02.png)

3. 返回用户组列表，屏幕上方将提示删除成功。

    ![删除提示](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/deletegroup03.png)

!!! note

    说明：删除用户组，不会删除组内的用户，但组内用户将无法再继承该组的权限。
