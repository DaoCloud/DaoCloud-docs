# GPU Operator 离线安装

DCE 5 预置了 CentOS 7.9，内核为 3.10.0-1160 的 GPU operator 离线包。本文介绍如何离线部署 GPU Operator。本章节覆盖 NVIDIA GPU 的多种使用模式的参数配置。

- GPU 整卡模式
- GPU vGPU 模式
- GPU MIG 模式

详情请参考：[NVIDIA GPU 卡使用模式](index.md)，本文使用的 AMD 架构的 Centos 7.9 （3.10.0-1160） 进行演示。如需使用 redhat8.4 部署，请参考[向火种节点仓库上传 RedHat GPU Opreator 离线镜像](./push_image_to_repo.md)和[构建 RedHat 8.4 离线 yum 源](./upgrade_yum_source_redhat8_4.md)。

## 前提条件

1. 用户已经在平台上安装了 v0.12.0 及以上版本的 addon 离线包。
2. 待部署 GPU Operator 的集群节点内核版本必须完全一致。节点 发行版和 GPU 卡型号在 [GPU 支持矩阵](../gpu_matrix.md)范围内。

## 操作步骤

参考如下步骤为集群安装 GPU Operator 插件。

1. 登录平台，进入`容器管理`-->`待安装 GPU Operator 的集群`-->进入集群详情。

2. 在 `Helm 模版` 页面，选择 `全部仓库`，搜索 `gpu-operator` 。

3. 选择 `gpu-operator`，点击`安装`。

4. 参考下文参数配置，配置 `gpu-operator` 安装参数，完成 `gpu-operator` 的安装。

## 参数配置

### 基本参数配置

- `名称`：输入插件名称。
- `命名空间`：选择将插件安装的命名空间。
- `版本`：插件的版本，此处以 `23.6.10` 版本为例。
- `就绪等待`：启用后，所有关联资源都处于就绪状态，才会标记应用安装成功。
- `失败删除`：安装失败，则删除已经安装的关联资源。开启后，将默认同步开启`就绪等待`。
- `详情日志`：开启后，将记录安装过程的详细日志。

### 高级参数配置

#### DevicePlugin 参数配置

1. `DevicePlugin.enable` ：配置是否启用 kubernentes [DevicePlugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) 特性。请结合使用场景，确定是否启用。

    - 使用 GPU 整卡模式请 **启用**。
    - 使用 GPU vGPU 模式请 **关闭**。
    - 使用 GPU MIG 模式请 **启用**。

    !!! note

        注意：
        1. 一个集群只能使用一种 GPU 卡模式，部署 GPU Operator 前，请确认 GPU 卡的使用模式，以选择是否启用 `DevicePlugin` 特性。
        2. 当使用 vGPU 模式（关闭这个参数）时，守护进程 `nvidia-operator-validator` 将长期处于 “等待中”状态，这属于正常现象，不影响 vGPU 功能的使用。

#### Driver 参数配置

2. `Driver.enable`：配置是否在节点上部署 NVIDIA 驱动，默认开启，如果您在使用 GPU Operator 部署前，已经在节点上部署了 NVIDIA 驱动程序，请关闭。

3. `Driver.image`：配置 GPU 驱动镜像，推荐默认镜像：`nvidia/driver`。

4. `Driver.repository`：GPU 驱动镜像所在的镜像仓库，默认为 nvidia 的 `nvcr.io` 仓库。

5. `Driver.version`：GPU 驱动镜像的版本，离线部署请使用默认参数，仅在线安装时需配置，不同类型操作系统的 Driver 镜像的版本存在如下差异：

    - RedHat 系统， 命名规则通常为 CUDA 的版本和 OS 版本组成，如内核为 `4.18.0-305.el8.x86_64` 的 RedHat 8.4 的 Driver.version 值为 `525.105.17`。
    - Ubuntu 系统，命名规则为：`<driver-branch>-<linux-kernel-version>-<os-tag>`。
    如 `525-5.15.0-69-ubuntu22.04`，`525` 为 CUDA 的版本，`5.15.0-69` 为内核版本，`ubuntu22.04` 为 OS 版本。
    注意：对于 Ubuntu ， Driver 镜像版本需和节点内核版本强一致，包括小版本号。

    - CentOS 系统， 命名规则通常为 CUDA 的版本和 OS 版本组成，如 `535.104.05`。

6. `Driver.RepoConfig.ConfigMapName`：用来记录 GPU Operator 的离线 yum 源配置文件名称，当使用预置的离线包时，参考`使用 Global 集群任意节点的 yum 源配置`。

    ??? note "使用 Global 集群任意节点的 yum 源配置"

        1. 使用 ssh 或其它方式进入 Global 集群的任意节点，获取平台离线源配置文件 `extension.repo`：

            ```bash
            cat /etc/yum.repos.d/extension.repo #查看 extension.repo 中的内容。
            ```
            # 预期输出如下：

            ```bash
            [extension-0]
            async = 1
            baseurl = http://x.x.x.x:9000/kubean/centos/$releasever/os/$basearch
            gpgcheck = 0
            name = kubean extension 0

            [extension-1]
            async = 1
            baseurl = http://x.x.x.x:9000/kubean/centos-iso/$releasever/os/$basearch
            gpgcheck = 0
            name = kubean extension 1
            ```

        2. 复制上述 `extension.repo` 文件中的内容，在待部署 GPU Operator 的集群的 `gpu-operator` 命名空间下，新建名为`local-repo-config` 的配置文件，可参考[创建配置项](../../configmaps-secrets/create-configmap.md)进行创建。
        **注意：配置 `key` 值必须为 `CentOS-Base.repo`,`value` 值点离线源配置文件 `extension.repo` 中的内容**。

    其它操作系统或内核可参考如下链接创建 yum 源文件：
    - [构建 CentOS 7.9 离线 yum 源](./Upgrade_yum_source_of_preset_offline_package.md)

    - [构建 RedHat 8.4 离线 yum 源](./upgrade_yum_source_redhat_8.4.md)

7. **MIG 配置参数**

    详细配置方式请参考[开启 MIG 功能](mig/create_mig.md)

    - `MigManager.enabled` ：是否启用 MIG 能力特性。
    - `Mig.strategy` ：节点上 GPU 卡的 MIG 设备的公开策略。NVIDIA 提供了两种公开 MIG 设备的策略（`single` 、`mixed`策略，详情参考：[NVIDIA GPU 卡模式说明](index.md)
    - `MigManager.Config` : 用于配置 MIG 切分配置参数和默认值。
        - `default`: 节点使用的切分配置默认值，默认为 `all-disabled`。
        - `name` ：MIG 的切分配置文件名，用于定义 MIG 的（GI ,CI）切分策略。默认为`default-mig-parted-config`。自定义参数参考[开启 MIG 功能](mig/create_mig.md)

8. `Node-Feature-Discovery.enableNodeFeatureAPI`：启用或禁用节点特性 API（Node Feature Discovery API）。

     - 当设置为 `true` 时，启用了节点特性 API。
     - 当设置为 `false` 或`未设置`时，禁用节点特性 API。

### 下一步操作

完成上述相关参数配置和创建后：

1. 如果使用 **整卡模式**，[应用创建时可使用 GPU 资源](full_gpu_userguide.md)

2. 如果使用 **vGPU 模式** ，完成上述相关参数配置和创建后，下一步请完成 [vGPU Addon 安装](vgpu/vgpu_addon.md)

3. 如果使用 **MIG 模式**，并且需要给个别 GPU 节点按照某种切分规格进行使用，否则按照 MigManager.Config 中的 `default` 值进行切分。

    - **single** 模式请给对应节点打上如下 Label：

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
        ```

    - **mixed** 模式请给对应节点打上如下 Label：

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
        ```

​    切分后，应用可[使用 MIG GPU 资源](mig/mig_usage.md)。
