# 管理边缘单元

## 边缘单元状态查看

**边缘单元有如下状态：**

- 创建中：边缘单元正在创建，此时编辑和删除按钮不可点击。
- 运行中：边缘单元创建成功，正常运行。
- 失败：边缘单元创建失败或运行异常，鼠标悬浮右侧图标可以查看异常信息。
- 更新中：编辑边缘单元，信息更新中，此时编辑和删除按钮不可点击。
- 删除中：删除边缘单元进行中，此时编辑和删除按钮不可点击。

**边缘单元资源统计：**

- 节点正常数/总数：节点状态为健康的节点数量/总数
- 应用实例正常数/总数；工作负载运行正常数量/总数

![边缘单元列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/manage-unit-01.png)

## 编辑边缘单元

在边缘单元列表的右侧，点击 `⋮` 按钮，在弹出菜单中选择`编辑`，可以对边缘单元的基础信息、组件仓库设置、访问设置进行编辑操作。

![编辑边缘单元](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/manage-unit-02.png)

## 删除边缘单元

在边缘单元列表的右侧，点击 `⋮` 按钮，在弹出菜单中选择删除。

!!! note

    - 删除边缘单元，系统会自动删除边缘单元下的终端设备、消息端点和消息路由资源。
    - 如果边缘单元下有创建边缘节点和工作负载资源，需要用户先手动删除。
    - 点击边缘节点和工作负载，用户可以快速跳转到边缘节点列表和工作负载列表页。

![删除边缘单元](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/manage-unit-03.png)

## 边缘单元概览

点击列表中`边缘单元名称`，进入边缘单元概览页面，可以查看基本信息和资源状态信息。更多管理操作点击左侧菜单栏进入对应菜单进行管理操作。

![边缘单元概览](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/manage-unit-04.png)
