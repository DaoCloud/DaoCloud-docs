# 创建蓝绿发布任务

蓝绿部署，通过流量控制，可以将用户流量从旧版本逐渐迁移到新版本，同时旧版本会保持在线运行待机，一旦期间发生任何异常，就可以立马切换流量到旧版本，从而实现快速回滚。

![蓝绿发布](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/blue-green.png)

## 前提条件

- 创建一个[工作空间](../../../ghippo/user-guide/workspace/workspace.md)和一个[用户](../../../ghippo/user-guide/access-control/user.md)，该用户需加入该工作空间并具备 **Workspace Editor** 角色。

- 发布对象所在的集群已经安装了 Argo Rollout 组件。有关具体的安装方式，可参考[管理 Helm 应用](../../../kpanda/user-guide/helm/helm-app.md)。

## 操作步骤

1. 进入**应用工作台**模块，在左侧导航栏点击 **灰度发布**，然后在页面右上角点击**创建发布任务**->**蓝绿发布**。

    ![进入创建页面](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/blue-green01.png)

2. 参考下列要求填写基本信息，然后点击**创建**。

    - 名称：填写发布任务的名称。最长 63 个字符，只能包含小写字母、数字及分隔符("-")，且必须以小写字母或数字开头及结尾
    - 集群：选择发布对象所在的集群。需要确保该集群已经部署了 Istio 和 Argo Rollout。
    - 命名空间：选择发布对象所在的命名空间。
    - 无状态负载：选择具体的发布对象。
    - Service：选择发布对象的服务，该服务必须关联了该发布对象。

        ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/blue-green02.png)

3. 系统自动跳转至灰度发布的任务列表页面，提示**创建成功**，并成功在列表生成一条记录。

    ![返回列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/blue-green03.png)
