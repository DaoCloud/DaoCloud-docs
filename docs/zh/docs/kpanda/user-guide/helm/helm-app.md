# 管理 Helm 应用

容器管理模块支持对 Helm 进行界面化管理，包括使用 Helm 模板创建 Helm 实例、自定义 Helm 实例参数、对 Helm 实例进行全生命周期管理等功能。

本节将以 [cert-manager](https://cert-manager.io/docs/) 为例，介绍如何通过容器管理界面创建并管理 Helm 应用。

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。

- 已完成一个[命名空间的创建](../namespaces/createns.md)、[用户的创建](../../../ghippo/user-guide/access-control/user.md)，并为用户授予 [NS Admin](../permissions/permission-brief.md#ns-admin) 或更高权限，详情可参考[命名空间授权](../permissions/cluster-ns-auth.md)。

## 安装 Helm 应用

参照以下步骤安装 Helm 应用。

1. 点击一个集群名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/crd01.png)

2. 在左侧导航栏，依次点击 __Helm 应用__ -> __Helm 模板__ ，进入 Helm 模板页面。

    在 Helm 模板页面选择名为 __addon__ 的 [Helm 仓库](helm-repo.md)，此时界面上将呈现 __addon__ 仓库下所有的 Helm chart 模板。
    点击名称为 __cert-manager__ 的 Chart。

    ![找到 chart](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm01.png)

3. 在安装页面，能够看到 Chart 的相关详细信息，在界面右上角选择需要安装的版本，点击 __安装__ 按钮。此处选择 v1.9.1 版本进行安装。

    ![点击安装](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm02.png)

4. 配置 __名称__ 、 __命名空间__ 及 __版本信息__ ，也可以在下方的 **参数配置** 区域通过修改 YAML 来自定义参数。点击 __确定__ 。

    ![填写参数](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm03.png)

5. 系统将自动返回 Helm 应用列表，新创建的 Helm 应用状态为 __安装中__ ，等待一段时间后状态变为 __运行中__ 。

    ![查看状态](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm04.png)

## 更新 Helm 应用

当我们通过界面完成一个 Helm 应用的安装后，我们可以对 Helm 应用执行更新操作。注意：只有通过界面安装的 Helm 应用才支持使用界面进行更新操作。

参照以下步骤更新 Helm 应用。

1. 点击一个集群名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/crd01.png)

2. 在左侧导航栏，点击 __Helm 应用__ ，进入 Helm 应用列表页面。

    在 Helm 应用列表页选择需要更新的 Helm 应用，点击列表右侧的 __⋮__ 操作按钮，在下拉选择中选择 __更新__ 操作。

    ![点击更新](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm08.png)

3. 点击 __更新__ 按钮后，系统将跳转至更新界面，您可以根据需要对 Helm 应用进行更新，此处我们以更新 __dao-2048__ 这个应用的 http 端口为例。

    ![更新页面](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm09.png)

4. 修改完相应参数后。您可以在参数配置下点击 __变化__ 按钮，对比修改前后的文件，确定无误后，点击底部 __确定__ 按钮，完成 Helm 应用的更新。

    ![对比变化](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm10.png)

5. 系统将自动返回 Helm 应用列表，右上角弹窗提示 __更新成功__ 。

    ![更新成功](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm11.png)

## 查看 Helm 操作记录

Helm 应用的每次安装、更新、删除都有详细的操作记录和日志可供查看。

1. 在左侧导航栏，依次点击 __集群运维__ -> __最近操作__ ，然后在页面上方选择 __Helm 操作__ 标签页。每一条记录对应一次安装/更新/删除操作。

    ![helm 操作](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm05.png)

2. 如需查看每一次操作的详细日志：在列表右侧点击 __⋮__ ，在弹出菜单中选择 __日志__ 。

    ![选择日志](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm06.png)

3. 此时页面下方将以控制台的形式展示详细的运行日志。

    ![查看运行日志](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm07.png)

## 删除 Helm 应用

参照以下步骤删除 Helm 应用。

1. 找到待删除的 Helm 应用所在的集群，点击集群名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/crd01.png)

2. 在左侧导航栏，点击 __Helm 应用__ ，进入 Helm 应用列表页面。

    在 Helm 应用列表页选择您需要删除的 Helm 应用，点击列表右侧的 __⋮__ 操作按钮，在下拉选择中选择 __删除__ 。

    ![点击删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm12.png)

3. 在弹窗内输入 Helm 应用的名称进行确认，然后点击 __删除__ 按钮。

    ![确认删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm13.png)
