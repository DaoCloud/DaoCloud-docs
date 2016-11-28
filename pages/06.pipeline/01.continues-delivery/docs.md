---
title: 使用流水线持续发布
---

流水线功能提供给用户统一的视图来管理应用自动发布规则，您可通过此功能来自动发布[自有主机](http://docs.daocloud.io/deploy-app-to-own-machine/deploy-to-cluster)或[DCE混合云](http://)环境下的应用

#### 设置自动发布规则

进入构建项目页，选择流水线

![](Screen%20Shot%202016-11-28%20at%2010.44.03%20AM.png)


点击右侧 development 面板中的添加一个新应用，
输入应用的名字，我们可以搜索到使用该项目的应用

![](Screen%20Shot%202016-11-28%20at%2010.45.28%20AM.png)

点击应用的“设置发布规则”来设置自动部署规则。
![](Screen%20Shot%202016-11-28%20at%2010.47.03%20AM.png)

根据此规则，当源码的 master 分支更新时会自动触发CI与构建，并自动发布新版本应用
![](Screen%20Shot%202016-11-28%20at%2010.48.34%20AM.png)

#### 流水线环境

流水线默认提供 development, staging, production 3 个逻辑环境，方便用户组织应用。

建议用户使用对应的环境来管理应用，例如：

在开发中，我们可以把 development 的应用设置为 develop 分支自动发布，staging的设置为 master 分支自动发布。当在 staging 完成最终测试后在生产环境手动进行发布应用。

> 从流水线移除应用或改变应用的环境不会对实际部署造成影响