# GPU Operator 离线安装

DCE 5.0 预置了 Ubuntu22.04、Ubuntu20.04、CentOS 7.9 这三个操作系统的 Driver 镜像，驱动版本是 535.104.12；
并且内置了各操作系统所需的 Toolkit 镜像，用户不再需要手动离线 Toolkit 镜像。

本文使用 AMD 架构的 CentOS 7.9（3.10.0-1160）进行演示。如需使用 Red Hat 8.4 部署，
请参考[向火种节点仓库上传 Red Hat GPU Opreator 离线镜像](./push_image_to_repo.md)和[构建 Red Hat 8.4 离线 yum 源](./upgrade_yum_source_redhat8_4.md)。

## 前提条件

- 待部署 gpu-operator 的集群节点内核版本必须完全一致。节点所在的发行版和 GPU 卡型号在 [GPU 支持矩阵](../gpu_matrix.md)的范围内。
- 用户已经在平台上安装了 v0.12.0 及以上版本的 [addon 离线包](../../../../download/addon/history.md)
  （Addon v0.20 及以上版本内置 Ubuntu22.04、Ubuntu20.04、CentOS 7.9 三个操作系统）。
- 安装 gpu-operator 时选择 v23.9.0+2 及以上版本

## 操作步骤

参考如下步骤为集群安装 gpu-operator 插件。

1. 登录平台，进入 __容器管理__ -> __待安装 gpu-operator  的集群__ -> 进入集群详情。

2. 在 __Helm 模板__ 页面，选择 __全部仓库__ ，搜索 __gpu-operator__ 。

3. 选择 __gpu-operator__ ，点击 __安装__ 。

4. 参考下文参数配置，配置 __gpu-operator__ 安装参数，完成 __gpu-operator__ 的安装。

## 参数配置

- __systemOS__ ：选择机器的操作系统，当前内置了 `Ubuntu 22.04`、`Ubuntu20.04`、`Centos7.9` 、`other` 四个选项，请正确的选择操作系统。

### 基本参数配置

- __名称__ ：输入插件名称。
- __命名空间__ ：选择将插件安装的命名空间。
- __版本__ ：插件的版本，此处以 __v23.9.0+2__ 版本为例。
- __失败删除__ ：安装失败，则删除已经安装的关联资源。开启后，将默认同步开启 __就绪等待__ 。
- __就绪等待__ ：启用后，所有关联资源都处于就绪状态，才会标记应用安装成功。
- __详情日志__ ：开启后，将记录安装过程的详细日志。

### 高级参数配置

#### Operator 参数配置

- __InitContainer.image__ ：配置 CUDA 镜像，推荐默认镜像： __nvidia/cuda__
- __InitContainer.repository__ ：CUDA 镜像所在的镜像仓库，默认为 __nvcr.m.daocloud.io__ 仓库
- __InitContainer.version__ : CUDA 镜像的版本，请使用默认参数

#### Driver 参数配置

- __Driver.enable__ ：配置是否在节点上部署 NVIDIA 驱动，默认开启，如果您在使用 GPU Operator 部署前，已经在节点上部署了 NVIDIA 驱动程序，请关闭。（若手动部署驱动程序需要关注 CUDA Toolkit 与 Toolkit Driver Version 的[适配关系](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#id5)，通过 GPU operator 安装则无需关注）。
- __Driver.usePrecompiled__ ：启用预编译的GPU驱动
- __Driver.image__ ：配置 GPU 驱动镜像，推荐默认镜像： __nvidia/driver__ 。
- __Driver.repository__ ：GPU 驱动镜像所在的镜像仓库，默认为 nvidia 的 __nvcr.io__ 仓库。
- __Driver.usePrecompiled__ ：开启预编译模式安装驱动。
- __Driver.version__ ：GPU 驱动镜像的版本，离线部署请使用默认参数，仅在线安装时需配置。不同类型操作系统的 Driver 镜像的版本存在如下差异，
   详情可参考：[Nvidia GPU Driver 版本](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/driver/tags)。
   如下不同操作系统的 `Driver Version` 示例：

    !!! note

        使用内置的操作系统版本无需修改镜像版本，其他操作系统版本请参考[向火种节点仓库上传镜像](./push_image_to_repo.md)。
        注意版本号后无需填写 Ubuntu、CentOS、Red Hat 等操作系统名称，若官方镜像含有操作系统后缀，请手动移除。

        - Red Hat 系统，例如 `525.105.17`
        - Ubuntu 系统，例如 `535-5.15.0-1043-nvidia`
        - CentOS 系统，例如 `525.147.05`

- __Driver.RepoConfig.ConfigMapName__ ：用来记录 GPU Operator 的离线 yum 源配置文件名称，
   当使用预置的离线包时，各类型的操作系统请参考如下的文档。

    - [构建 CentOS 7.9 离线 yum 源](./upgrade_yum_source_centos7_9.md)
    - [构建 Red Hat 8.4 离线 yum 源](./upgrade_yum_source_redhat8_4.md)

#### Toolkit 配置参数

__Toolkit.enable__ ：默认开启，该组件让 conatainerd/docker 支持运行需要 GPU 的容器。

#### MIG 配置参数

详细配置方式请参考[开启 MIG 功能](mig/create_mig.md)

**MigManager.Config.name** ：MIG 的切分配置文件名，用于定义 MIG 的（GI, CI）切分策略。
默认为 __default-mig-parted-config__ 。自定义参数参考[开启 MIG 功能](mig/create_mig.md)。

### 下一步操作

完成上述相关参数配置和创建后：

- 如果使用 **整卡模式**，[应用创建时可使用 GPU 资源](full_gpu_userguide.md)

- 如果使用 **vGPU 模式** ，完成上述相关参数配置和创建后，下一步请完成 [vGPU Addon 安装](vgpu/vgpu_addon.md)

- 如果使用 **MIG 模式**，并且需要给个别 GPU 节点按照某种切分规格进行使用，
  否则按照 `MigManager.Config` 中的 __default__ 值进行切分。

    - **single** 模式请给对应节点打上如下 Label：

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
        ```

    - **mixed** 模式请给对应节点打上如下 Label：

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
        ```

​    切分后，应用可[使用 MIG GPU 资源](mig/mig_usage.md)。
