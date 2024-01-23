# 用户

用户指的是由平台管理员 admin 或者用户与访问控制管理员 IAM Owner 在 __全局管理__ -> __用户与访问控制__ -> __用户__ 页面创建的用户，或者通过 LDAP / OIDC 对接过来的用户。
用户名代表账号，用户通过用户名和密码登录 DaoCloud Enterprise 平台。

拥有一个用户账号是用户访问平台的前提。新建的用户默认没有任何权限，例如您需要给用户赋予相应的角色权限，比如在 __用户列表__ 或 __用户详情__ 授予子模块的管理员权限。
子模块管理员拥有该子模块的最高权限，能够创建、管理、删除该模块的所有资源。
如果用户需要被授予具体资源的权限，比如某个资源的使用权限，请查看[资源授权说明](#为用户授予子模块管理员权限)。

本页介绍用户的创建、授权、禁用、启用、删除等操作。

## 创建用户

前提：拥有平台管理员 Admin 权限或者用户与访问控制管理员 IAM Owner 权限。

1. 管理员进入 __用户与访问控制__ ，选择 __用户__ ，进入用户列表，点击右上方的 __创建用户__ 。

    ![创建用户按钮](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/createuser01.png)

2. 在 __创建用户__ 页面填写用户名和登录密码。如需一次性创建多个用户，可以点击 __创建用户__ 后进行批量创建，一次性最多创建 5 个用户。根据您的实际情况确定是否设置用户在首次登录时重置密码。

    ![设置用户名和密码](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/createuser02.png)

3. 点击 __确定__ ，创建用户成功，返回用户列表页。

!!! note

    此处设置的用户名和密码将用于登录平台。

## 为用户授予子模块管理员权限

前提：该用户已存在。

1. 管理员进入 __用户与访问控制__ ，选择 __用户__ ，进入用户列表，点击 __⋮__ -> __授权__ 。

    ![授权菜单](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/authorize01.png)

2. 在 __授权__ 页面勾选需要的角色权限（可多选）。

    ![授权界面](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/authorize02.png)

3. 点击 __确定__ 完成为用户的授权。

!!! note

    在用户列表中，点击某个用户，可以进入用户详情页面。

## 将用户加入用户组

1. 管理员进入 __用户与访问控制__ ，选择 __用户__ ，进入用户列表，点击 __⋮__ -> __加入用户组__ 。

    ![加入用户组菜单](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/joingroup01.png)

2. 在 __加入用户组__ 页面勾选需要加入的用户组（可多选）。若没有可选的用户组，点击 __创建用户组__ 创建用户组，再返回该页面点击 __刷新__ 按钮，显示刚创建的用户组。

    ![加入用户组界面](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/joingroup02.png)

3. 点击 __确定__ 将用户加入用户组。

!!! note

    用户会继承用户组的权限，可以在 __用户详情__ 中查看该用户已加入的用户组。

## 启用/禁用用户

禁用用户后，该用户将无法再访问平台。与删除用户不同，禁用的用户可以根据需要再次启用，建议删除用户前先禁用，以确保没有关键服务在使用该用户创建的密钥。

1. 管理员进入 __用户与访问控制__ ，选择 __用户__ ，进入用户列表，点击一个用户名进入用户详情。

    ![用户详情](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/createuser03.png)

2. 点击右上方的 __编辑__ ，关闭状态按钮，使按钮置灰且处于未启用状态。

    ![编辑](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/enableuser.png)

3. 点击 __确定__ 完成禁用用户的操作。

## 忘记密码

前提：需要设置用户邮箱，有两种方式可以设置用户邮箱。

- 管理员在该用户详情页面，点击 __编辑__ ，在弹出框输入用户邮箱地址，点击 __确定__ 完成邮箱设置。

    ![编辑](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/enableuser.png)

- 用户还可以进入 __个人中心__ ，在 __安全设置__ 页面设置邮箱地址。

    ![个人中心](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/mailbox.png)

如果用户登录时忘记密码，请参考[重置密码](../password.md)。

## 删除用户

!!! warning

    删除用户后，该用户将无法再通过任何方式访问平台资源，请谨慎删除。
    在删除用户之前，请确保您的关键程序不再使用该用户创建的密钥。
    如果您不确定，建议在删除前先禁用该用户。
    如果您删除了一个用户，然后再创建一个同名的新用户，则新用户将被视为一个新的独立身份，它不会继承已删除用户的角色。

1. 管理员进入 __用户与访问控制__ ，选择 __用户__ ，进入用户列表，点击 __⋮__ -> __删除__ 。

    ![删除用户菜单](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/deleteuser01.png)

2. 点击 __移除__ 完成删除用户的操作。

    ![删除用户确认](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/deleteuser02.png)
