# 管理 Helm 应用

容器管理模块支持对 Helm 进行界面化管理，包括使用 Helm 模板创建 Helm 实例、自定义 Helm 实例参数、对 Helm 实例进行全生命周期管理等功能。

本节将以 [cert-manager](https://cert-manager.io/docs/) 为例，介绍如何通过容器管理界面创建并管理 Helm 应用。

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](../Clusters/JoinACluster.md)或者[已创建 Kubernetes 集群](../Clusters/CreateCluster.md)，且能够访问集群的 UI 界面。

- 已完成一个[命名空间的创建](../Namespaces/createns.md)、[用户的创建](../../../ghippo/04UserGuide/01UserandAccess/User.md)，并为用户授予 [`NS Admin`](../Permissions/PermissionBrief.md#ns-admin) 或更高权限，详情可参考[命名空间授权](../Permissions/Cluster-NSAuth.md)。

## 安装 Helm 应用

参照以下步骤安装 Helm 应用。

1. 点击一个集群名称，进入`集群详情`。

    ![集群详情](../../images/crd01.png)

2. 在左侧导航栏，依次点击 `Helm 应用` -> `Helm 模板`，进入 Helm 模板页面。

    在 Helm 模板页面选择名为 `addon` 的 [Helm 仓库](helm-repo.md)，此时界面上将呈现 `addon` 仓库下所有的 Helm chart 模板。
    点击名称为 `cert-manager` 的 Chart。

    ![找到 chart](../../images/helm01.png)

3. 在安装页面，能够看到 Chart 的相关详细信息，在界面右上角选择需要安装的版本，点击`安装`按钮。此处选择 v1.9.1 版本进行安装。

    ![点击安装](../../images/helm02.png)

4. 配置`名称`、`命名空间`及`版本信息`，也可以在下方的 **参数配置** 区域通过修改 YAML 来自定义参数。点击`确定`。

    ![填写参数](../../images/helm03.png)

5. 系统将自动返回 Helm 应用列表，新创建的 Helm 应用状态为`安装中`，等待一段时间后状态变为`运行中`。

    ![查看状态](../../images/helm04.png)

## 更新 Helm 应用

当我们通过界面完成一个 Helm 应用的安装后，我们可以对 Helm 应用执行更新操作。注意：只有通过界面安装的 Helm 应用才支持使用界面进行更新操作。

参照以下步骤更新 Helm 应用。

1. 点击一个集群名称，进入`集群详情`。

    ![集群详情](../../images/crd01.png)

2. 在左侧导航栏，点击 `Helm 应用`，进入 Helm 应用列表页面。

    在 Helm 应用列表页选择需要更新的 Helm 应用，点击列表右侧的 `...` 操作按钮，在下拉选择中选择`更新`操作。

    ![点击更新](../../images/helm08.png)

3. 点击`更新`按钮后，系统将跳转至更新界面，您可以根据需要对 Helm 应用进行更新，此处我们以更新 `dao-2048` 这个应用的 http 端口为例。

    ![更新页面](../../images/helm09.png)

4. 修改完相应参数后。您可以在参数配置下点击`变化`按钮，对比修改前后的文件，确定无误后，点击底部`确定`按钮，完成 Helm 应用的更新。

    ![对比变化](../../images/helm10.png)

5. 系统将自动返回 Helm 应用列表，右上角弹窗提示`更新成功`。

    ![更新成功](../../images/helm11.png)

## 查看 Helm 操作记录

Helm 应用的每次安装、更新、删除都有详细的操作记录和日志可供查看。

1. 在左侧导航栏，依次点击`集群运维` -> `最近操作`，然后在页面上方选择 `Helm 操作`标签页。每一条记录对应一次安装/更新/删除操作。

    ![helm 操作](../../images/helm05.png)

2. 如需查看每一次操作的详细日志：在列表右侧点击 `⋮`，在弹出菜单中选择`日志`。

    ![选择日志](../../images/helm06.png)

3. 此时页面下方将以控制台的形式展示详细的运行日志。

    ![查看运行日志](../../images/helm07.png)

## 删除 Helm 应用

参照以下步骤删除 Helm 应用。

1. 找到待删除的 Helm 应用所在的集群，点击集群名称，进入`集群详情`。

    ![集群详情](../../images/crd01.png)

2. 在左侧导航栏，点击 `Helm 应用`，进入 Helm 应用列表页面。

    在 Helm 应用列表页选择您需要删除的 Helm 应用，点击列表右侧的 `...` 操作按钮，在下拉选择中选择`删除`。

    ![点击删除](../../images/helm12.png)

3. 在弹窗内输入 Helm 应用的名称进行确认，然后点击`删除`按钮。

    ![确认删除](../../images/helm13.png)
