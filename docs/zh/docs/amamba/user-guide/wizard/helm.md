# 基于 Helm 模板部署 Helm 应用

应用工作台支持通过 [Git 仓库](create-app-git.md)、[Jar 包](jar-java-app.md)、容器镜像、Helm 模板等四种方式构建应用。本文介绍如何通过 Helm 模板部署 Helm 应用。

## 前提条件

- 需创建一个工作空间和一个用户，该用户需加入该工作空间并赋予 **workspace edit** 角色。
  参考[创建工作空间](../../../ghippo/user-guide/workspace/workspace.md)、[用户和角色](../../../ghippo/user-guide/access-control/user.md)。

## 操作步骤

1. 进入应用工作台模块后，在左侧导航栏点击**向导**，然后选择**基于 Helm 模板**。

    ![基于helm](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/helm01.png)

2. 在页面上方选择需要将应用部署在哪个集群，然后点击需要部署的 Helm Chart 卡片，例如 “docker-registry”。

    !!! note

        -  点击**仓库**右侧的列表可以筛选 Helm 仓库
        -  点击**类型**右侧的列表可以筛选 Helm Chart 的类型
        -  也可以在在右侧的搜索框直接输入 Chart 名称快速找到需要部署的 Helm 应用

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/helm02.png)

3. 阅读该应用的安装前提、参数配置说明等信息，在右上角选择需要安装版本，然后点击**安装**。

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/helm03.png)

4. 设置应用名称、命名空间等基本信息，然后在下方通过表单或 YAML 配置参数，最后在页面底部点击**确定**。

    - 就绪等待：启用后，将等待应用下的所有关联资源都处于就绪状态，才会标记应用安装成功。
    - 失败删除：如果插件安装失败，则删除已经安装的关联资源。开启后，将默认同步开启就绪等待。
    - 详情日志：开启后，将记录安装过程的详细日志。
    - 点击**参数配置**下方的**变化**页签可使用对比视图查看参数变更情况。

        ![容器配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/helm04.png)

5. 页面自动跳转到概览页面下的 Helm 应用列表，可查看当前集群下已经安装的 Helm 应用。

    > 点击应用名称可以跳转到容器管理模块查看应用详情。
    
    ![高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/helm05.png)

!!! note

    如需更新删除该 Helm 应用，需要点击应用名称跳转到容器管理模块，在应用详情页面进行更新与删除以及更多操作。

    ![高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/helm06.png)
