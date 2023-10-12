# GPU Operator 离线安装

本文介绍如何基于火种节点的离线源来部署 GPU Operator 。本文使用的 AMD 架构的 Centos 7.9 （3.10.0-1160） 进行演示。本章节覆盖 NVIDIA GPU 的多种使用模式的参数配置。

- GPU 整卡模式
- GPU vGPU 模式
- GPU MIG 模式

详情请参考：[NVIDIA GPU 卡使用模式](overvie_nvidia_gpu.md)

!!! note

    Daocloud 内置了 Centos 7.9 3.10.0-1160 的 GPU Operator 离线包，如需使用其它操作系统和内核版本，请参考构建 GPU Operator 离线包进行构建。

### 前提条件

- 待安装 GPU 驱动节点系统要求请参考 [GPU 支持矩阵](../gpu_matrix.md)，本章节使用  AMD 架构的 Centos 7.9 （3.10.0-1160）
- 确认集群节点上具有对应型号的 GPU 卡（[NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/)、 [A100](https://www.nvidia.com/en-us/data-center/a100/) 和 [A30](https://www.nvidia.com/en-us/data-center/products/a30-gpu/) Tensor Core GPU），详情参考 [GPU 支持矩阵](../gpu_matrix.md)

### 操作步骤

参考如下步骤为集群安装 GPU Operator 插件。

1. 登录平台，进入`容器管理`-->`待安装 GPU Operator 的集群`-->进入集群详情。

2. 在 `Helm 模版` 页面，选择 `全部仓库`，搜索 `gpu-operator` 。

3. 选择 `gpu-operator` ，点击`安装`。

4. **基本参数** 配置如下：

    - `名称`：输入插件名称。
    - `命名空间`：选择将插件安装的命名空间。
    - `版本`：插件的版本，此处以 `23.6.10` 版本为例。
    - `就绪等待`：启用后，所有关联资源都处于就绪状态，才会标记应用安装成功。
    - `失败删除`：安装失败，则删除已经安装的关联资源。开启后，将默认同步开启`就绪等待`。
    - `详情日志`：开启后，将记录安装过程的详细日志。

5. **高级参数** 配置如下：

    - `DevicePlugin.enable` ：是否启用 Device Plugin。

        - 使用 **独占 GPU** 请 **启用**。
        - 使用  **vGPU** 时请 **关闭**。
        - 使用 **GPU MIG** 请 **启用**。

    - `Driver.enable` ：是否部署 NVIDIA 驱动，默认开启。

    - `Driver.image` ： GPU 驱动的镜像版本，推荐默认镜像：`nvidia/driver`。

    - `RepoConfig.ConfigMapName` ：GPU Operator 的离线源配置文件名称，参考如下步骤创建名为 `local-repo-config` 的配置文件。

        - 使用 ssh 或其它方式进入火种节点，获取火种节点离线源配置文件 `extension.repo`，执行如下命令查看：

            ```yaml
            cat /etc/yum.repos.d/extension.repo #查看 extension.repo 中的内容。
            
            # 一般输出如下：
            [root@g-master1 yum.repos.d]# cat /etc/yum.repos.d/extension.repo
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
            
            复制上述` extension.repo` 中内容，在集群中新建名为`local-repo-config` 的配置文件，可参考[创建配置项](../../configmaps-secrets/create-configmap.md)进行创建。
            **注意：配置 `key` 值必须为 `CentOS-Base.repo`,`value` 值点离线源配置文件 `extension.repo` 中的内容**

    - `RepoConfig.repository` ：  驱动离线源仓库。默认为：`nvcr.io`。

    - `RepoConfig.version` ： GPU 驱动的镜像版本，仅在线安装时需配置，不同操作系统 Driver 镜像的名称存在差异：

         - Ubuntu 系统，命名规则为：<driver-branch>-<linux-kernel-version>-<os-tag>。
           如 `525-5.15.0-69-ubuntu22.04`，`525` 用于指定 CUDA 的版本，`5.15.0-69` 指定内核的版本，`ubuntu22.04` 指定 OS 版本。
           注意：对于 Ubuntu ，NVIDIA 的 driver 镜像版本需要和节点内核版本强一致，包括小版本号，可前往  NVIDIA GPU Driver 检查该版本驱动是否存在。

         - RedHat/CentOS 系统， 命名规则通常为 CUDA 的版本和 OS 版本组成，如 `535.104.05-centos7`。

    - `Driver.image` ：GPU 驱动的镜像版本，推荐使用默认镜像：`nvidia/driver`。

    - `Node-Feature-Discovery.enableNodeFeatureAPI` ：启用或禁用节点特性 API（Node Feature Discovery API）。

         - 当设置为 `true` 时，启用了节点特性 API。
         - 当设置为 `false` 或`未设置`时，禁用节点特性 API。

6.  **MIG 配置参数**

    详细配置方式请参考[开启 MIG 功能](../create_mig.md)

    - `Mig.enabled` ：是否启用 MIG 能力特性。
    - `Mig.strategy` ：节点上 GPU 卡的 MIG 设备的公开策略。NVIDIA 提供了两种公开 MIG 设备的策略（`single` 、`mixed`策略，详情参考：[NVIDIA GPU 卡模式说明](overvie_nvidia_gpu.md)
    - `MigManager.Config` : 用于配置 MIG 切分配置参数和默认值。
        - `default`: 节点使用的切分配置默认值，默认为 `all-disbled`。
        - `name` ：MIG 的切分配置文件名，用于定义 MIG 的（GI ,CI）切分策略。默认为`default-mig-parted-config`。自定义参数参考[开启 MIG 功能](../create_mig.md)


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
