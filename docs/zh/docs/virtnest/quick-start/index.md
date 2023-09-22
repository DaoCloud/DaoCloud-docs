# 创建虚拟机

本文将介绍如何通过镜像和 YAML 文件两种方式创建虚拟机。

虚拟机容器基于 KubeVirt 技术将虚拟机作为云原生应用进行管理，与容器无缝地衔接在一起，
使用户能够轻松地部署虚拟机应用，享受与容器应用一致的丝滑体验。

## 前提条件

创建虚拟机之前，需要满足以下前提条件：

- 在集群内安装 virtnest-agent。
- 创建一个[命名空间](../../kpanda/user-guide/namespaces/createns.md)和[用户](../../ghippo/user-guide/access-control/user.md)。
- 当前操作用户应具有
  [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)
  或更高权限，详情可参考[命名空间授权](../../kpanda/user-guide/namespaces/createns.md)。
- 提前准备好镜像。

## 镜像创建

参考以下步骤，使用镜像创建一个虚拟机。

1. 点击左侧导航栏上的`容器管理`，然后点击`虚拟机容器`，进入`虚拟机管理`页面。

    ![虚拟机容器](../images/createvm01.png)

2. 在虚拟机列表页面，点击创建虚拟机-选择镜像创建虚拟机

    ![镜像创建](../images/createvm02.png)

3. 进入镜像创建页面，依次填写基本信息、镜像配置、存储与网络、登录设置后，在页面右下角点击`确定`完成创建。

    系统将自动返回虚拟机列表。点击列表右侧的 `︙`，可以对虚拟机执行关机/开启、重启、克隆、更新、创建快照、控制台访问（VNC）、删除等操作。
    克隆和快照能力依赖于存储池的选择。

    ![虚拟机操作](../images/createvm03.png)

### 基本信息

在`创建虚拟机`页面中，根据下表输入信息后，点击`下一步`。

![基础信息](../images/createvm04.png)

- 名称：最多包含 63 个字符，只能包含小写字母、数字及分隔符（“-”），且必须以小写字母或数字开头及结尾。
  同一命名空间内名称不得重复，而且名称在虚拟机创建好之后不可更改。
- 别名：允许任何字符，最长60个字符。
- 集群：选择将新建的虚拟机部署在哪个集群内。
- 命名空间：选择将新建的虚拟机部署在哪个命名空间。
  找不到所需的命名空间时可以根据页面提示去[创建新的命名空间](../../kpanda/user-guide/namespaces/createns.md)。
- 标签/注解：选择为虚拟机添加所需的标签/注解信息。

### 容器配置

根据下表填写镜像相关信息后，点击`下一步`

![容器配置](../images/createvm05.png)

![使用镜像仓库](../images/createvm06.png)

- 镜像来源：支持三种类型的来源。

    - 镜像仓库类型：镜像存储与容器镜像仓库中，支持是否开启选择系统内置镜像，若开启，则可以使用平台内置镜像，若关闭，则支持从镜像仓库中按需选择镜像；
    - HTTP类型：镜像存储于 HTTP 协议的文件服务器中，支持HTTPS://和HTTP://前缀；
    - 对象存储（S3）：支持通过对象存储协议(S3)获取的虚拟机镜像，若是无需认证的对象存储文件，请使用 HTTP 来源。

- 目前可以使用以下的操作系统和版本。

    | 操作系统 |   对应版本   | 镜像地址                                                     |
    | :------: | :----------: | ------------------------------------------------------------ |
    |  CentOS  |  CentOS 8.3  | release-ci.daocloud.io/virtnest/system-images/centos-7.9-x86_64:v1 |
    |  Ubuntu  | Ubuntu 22.04 | release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1 |
    |  Debian  |  Debian 12   | release-ci.daocloud.io/virtnest/system-images/debian-12-x86_64:v1 |

- CPU 配额、内存 配额：CPU 建议使用整数，若填写小数则会向上取整。

### 存储与网络配置

![存储与网络配置](../images/createvm07.png)

- 存储：系统默认创建一个 VirtIO 类型的 rootfs 系统盘，用于存放操作系统和数据。
  默认使用块存储。如果需要使用克隆和快照功能，请确保您的存储池支持 VolumeSnapshots 功能，
  并在存储池（SC）中进行创建。请注意，存储池（SC）还有其他一些先决条件需要满足。

    - 先决条件：

        - KubeVirt 利用 Kubernetes CSI 驱动程序的 VolumeSnapshot功能来捕获持久化虚拟机状态。
          因此，您需要确保您的虚拟机使用由支持 VolumeSnapshots 的 StorageClass 并配置了正确的 VolumeSnapshotClass。
        - 查看已创建的 Snapshotclass ，并且确认 provisioner 属性同存储池中的 Driver 属性一致。

        > 后续将支持多块数据盘。

- 网络：若您不做任何配置，系统将默认创建一个 VirtIO 类型的网络。

### 登录设置

- 用户名/密码：可以通过用户名和密码登录至虚拟机。
- SSH：选择 SSH 登录方式时可为虚拟机绑定 SSH 密钥，用于日后登录虚拟机。

![登录设置](../images/createvm08.png)

## YAML 创建

除了通过镜像方式外，还可以通过 YAML 文件更快速地创建创建虚拟机。

1. 进入虚拟机容器列表页，点击 `通过 YAML 创建`按钮

    ![yaml 创建](../images/createvm09.png)

2. 输入或粘贴事先准备好的 YAML 文件，点击`确定`即可完成创建。
