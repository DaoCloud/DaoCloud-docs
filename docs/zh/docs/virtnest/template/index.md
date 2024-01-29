# 通过模板创建虚拟机

本文将介绍如何通过模板创建虚拟机。

通过内置模板和自定义模板，用户可以轻松创建新的虚拟机。此外，我们还提供将现有虚拟机转换为虚拟机模板的功能，让用户能够更加灵活地管理和使用资源。

## 模板创建

参考以下步骤，使用模板创建一个虚拟机。

1. 点击左侧导航栏上的`容器管理`，然后点击`虚拟机`，进入`虚拟机管理`页面。在虚拟机列表页面，点击创建虚拟机-选择模板创建虚拟机。

    ![虚拟机模板创建](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep01.png)

2. 进入镜像创建页面，依次填写基本信息、模板配置、存储与网络、登录设置后，在页面右下角点击`确定`完成创建。

    系统将自动返回虚拟机列表。点击列表右侧的 `︙`，可以对虚拟机执行关机/开启、重启、克隆、更新、创建快照、配置转换为模板、控制台访问（VNC）、删除等操作。
    克隆和快照能力依赖于存储池的选择。

    ![虚拟机操作](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep02.png)

### 基本信息

在创建虚拟机页面中，根据下表输入信息后，点击`下一步`。

![虚拟机基础信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep03.png)

- 名称：最多包含 63 个字符，只能包含小写字母、数字及分隔符（“-”），且必须以小写字母或数字开头及结尾。
  同一命名空间内名称不得重复，而且名称在虚拟机创建好之后不可更改。
- 别名：允许任何字符，最长60个字符。
- 集群：选择将新建的虚拟机部署在哪个集群内。
- 命名空间：选择将新建的虚拟机部署在哪个命名空间。
  找不到所需的命名空间时可以根据页面提示去[创建新的命名空间](../../kpanda/user-guide/namespaces/createns.md)。

### 模板配置

出现模板列表，按需选择内置模板/自定义模板。

- 选择内置模板：平台内置了2个标准模板，不允许编辑和删除。选择内置模板后，镜像来源、操作系统、镜像地址等将使用模板内的信息，无法修改；资源配额也将使用模板内的信息，允许修改。
  
    ![内置模板](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep04.png)

    ![内置模板](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep05.png)

- 选择自定义模板：由虚拟机配置转化而来的模板，支持编辑和删除。使用自定义模板则根据具体情况支持修改镜像来源等信息。

    ![使用镜像仓库](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep06.png)

    ![使用镜像仓库](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep07.png)

### 存储与网络配置

![存储与网络配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/create-tep08.png)

- 存储：系统默认创建一个 VirtIO 类型的 rootfs 系统盘，用于存放操作系统和数据。
  默认使用块存储。如果需要使用克隆和快照功能，请确保您的存储池支持 VolumeSnapshots 功能，
  并在存储池（SC）中进行创建。请注意，存储池（SC）还有其他一些先决条件需要满足。

    - 先决条件：

        - KubeVirt 利用 Kubernetes CSI 驱动程序的 VolumeSnapshot功能来捕获持久化虚拟机状态。
          因此，您需要确保您的虚拟机使用由支持 VolumeSnapshots 的 StorageClass 并配置了正确的 VolumeSnapshotClass。
        - 查看已创建的 Snapshotclass ，并且确认 provisioner 属性同存储池中的 Driver 属性一致。

    - 支持添加一块系统盘和多块数据盘。

- 网络：若您不做任何配置，系统将默认创建一个 VirtIO 类型的网络。

### 登录设置

- 用户名/密码：可以通过用户名和密码登录至虚拟机。
- SSH：选择 SSH 登录方式时可为虚拟机绑定 SSH 密钥，用于日后登录虚拟机。

![登录设置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/createvm08.png)
