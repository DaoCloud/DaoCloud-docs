# 导入仓库

本页展示如何导入仓库。

## 前提条件

- 需创建一个工作空间和一个用户，该用户需加入该工作空间并赋予  __workspace edit__  角色。
  参考[创建工作空间](../../../ghippo/user-guide/workspace/workspace.md)、[用户和角色](../../../ghippo/user-guide/access-control/user.md)。
- 准备一个 Git 仓库。

## 导入仓库

如果持续部署应用的清单文件所在的代码仓库不是公开的，则需要事先将仓库导入至应用工作台。
应用工作台目前支持两种导入方式： __使用 HTTPS 导入仓库__ 和 __使用 SSH 导入仓库__ 。

### 使用 HTTPS 导入仓库

1. 在 __应用工作台__ -> __GitOps__ -> __仓库__ 页面中，点击 __导入仓库__ 按钮，选择 __使用 HTTPS__ 。

    ![导入](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/import01.png)

2. 在 __使用 HTTPS 导入仓库__ 页面中，配置相关参数后点击 __确定__ 。

    ![导入](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/import02.png)

### 使用 SSH 导入仓库

1. 在 __应用工作台__ -> __GitOps__ -> __仓库__ 页面中，点击 __导入仓库__ 按钮，选择 __使用 SSH__ 。

    ![导入](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/import01.png)

2. 在 __使用 SSH 导入仓库__ 页面中，配置相关参数后点击 __确定__ 。

    ![导入](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/import03.png)

## 删除仓库

如果不再使用某个代码仓库，可参照以下步骤删除。

1. 在仓库列表页选择某一个仓库，点击  __︙__  ，在弹出的菜单中点击 __删除__  。

    ![删除](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/import04.png)

2. 在二次确认弹窗中点击 __确定__ 。

    ![删除确认](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/import05.png)
