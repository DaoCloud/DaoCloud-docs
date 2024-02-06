# GPU Operator 离线安装

DCE 5 预置了 CentOS 7.9，内核为 3.10.0-1160 的 GPU operator 离线包。本文介绍如何离线部署 GPU Operator。本章节覆盖 NVIDIA GPU 的多种使用模式的参数配置。

- GPU 整卡模式
- GPU vGPU 模式
- GPU MIG 模式

详情请参考：[NVIDIA GPU 卡使用模式](index.md)，本文使用的 AMD 架构的 Centos 7.9 （3.10.0-1160） 进行演示。如需使用 redhat8.4 部署，请参考[向火种节点仓库上传 RedHat GPU Opreator 离线镜像](./push_image_to_repo.md)和[构建 RedHat 8.4 离线 yum 源](./upgrade_yum_source_redhat8_4.md)。

## 前提条件

1. 用户已经在平台上安装了 v0.12.0 及以上版本的 addon 离线包。
2. 待部署 GPU Operator 的集群节点内核版本必须完全一致。节点 发行版和 GPU 卡型号在 [GPU 支持矩阵](../gpu_matrix.md) 范围内。

## 操作步骤

参考如下步骤为集群安装 GPU Operator 插件。

1. 登录平台，进入 __容器管理__ --> __待安装 GPU Operator 的集群__ -->进入集群详情。

2. 在 __Helm 模板__ 页面，选择 __全部仓库__ ，搜索 __gpu-operator__ 。

3. 选择 __gpu-operator__ ，点击 __安装__ 。

4. 参考下文参数配置，配置 __gpu-operator__ 安装参数，完成 __gpu-operator__ 的安装。

## 参数配置

### 基本参数配置

- __名称__ ：输入插件名称。
- __命名空间__ ：选择将插件安装的命名空间。
- __版本__ ：插件的版本，此处以 __23.6.10__ 版本为例。
- __就绪等待__ ：启用后，所有关联资源都处于就绪状态，才会标记应用安装成功。
- __失败删除__ ：安装失败，则删除已经安装的关联资源。开启后，将默认同步开启 __就绪等待__ 。
- __详情日志__ ：开启后，将记录安装过程的详细日志。

### 高级参数配置

#### DevicePlugin 参数配置

1. __DevicePlugin.enable__ ：配置是否启用 kubernentes [DevicePlugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) 特性。默认为 **开启** 状态，**关闭** 后 GPU 整卡/MIG 功能将无法使用。


#### Operator 参数配置

1. __InitContainer.image__ ：配置 CUDA 镜像，推荐默认镜像： __nvidia/cuda__ 。
2. __InitContainer.repository__ ：CUDA 镜像所在的镜像仓库，默认为 __nvcr.m.daocloud.io__ 仓库。
3. __InitContainer.version__ : CUDA 镜像的版本，请使用默认参数。

#### Driver 参数配置

1. __Driver.enable__ ：配置是否在节点上部署 NVIDIA 驱动，默认开启，如果您在使用 GPU Operator 部署前，已经在节点上部署了 NVIDIA 驱动程序，请关闭。

2. __Driver.image__ ：配置 GPU 驱动镜像，推荐默认镜像： __nvidia/driver__ 。

3. __Driver.repository__ ：GPU 驱动镜像所在的镜像仓库，默认为 nvidia 的 __nvcr.io__ 仓库。
4. __Driver.version__ ：GPU 驱动镜像的版本，离线部署请使用默认参数，仅在线安装时需配置，不同类型操作系统的 Driver 镜像的版本存在如下差异，详情可参考：[Nvidia GPU Driver 版本](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/driver/tags)，如下不同操作系统的 `Driver Version` 示例：

??? note

 系统默认提供 525.147.05-centos7 的镜像，其他镜像需要参考 [向火种节点仓库上传镜像](./push_image_to_repo.md) 

    - RedHat 系统 ，示例：`525.105.17-rhel8.4`
    - Ubuntu 系统，示例：`535-5.15.0-1043-nvidia-ubuntu22.04`
    - CentOS 系统，示例： `525.147.05-centos7`

    
5. __Driver.RepoConfig.ConfigMapName__ ：用来记录 GPU Operator 的离线 yum 源配置文件名称，当使用预置的离线包时，global 集群可直接执行如下命令，工作集群 __参考 Global 集群任意节点的 yum 源配置__ 。
    - global 集群配置

        ```sh
        kubectl create configmap local-repo-config  -n gpu-operator --from-file=CentOS-Base.repo=/etc/yum.repos.d/extension.repo
        ```
     - 工作集群配置
       
    ??? note "参考 Global 集群任意节点的 yum 源配置"

        1. 使用 ssh 或其它方式进入 Global 集群的任意节点，获取平台离线源配置文件 __extension.repo__ ：
        
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
        
        2. 复制上述 __extension.repo__ 文件中的内容，在待部署 GPU Operator 的集群的 __gpu-operator__ 命名空间下，新建名为 __local-repo-config__ 的配置文件，可参考[创建配置项](../../configmaps-secrets/create-configmap.md)进行创建。
        **注意：配置 __key__ 值必须为 __CentOS-Base.repo__ , __value__ 值点离线源配置文件 __extension.repo__ 中的内容**。

    其它操作系统或内核可参考如下链接创建 yum 源文件：
    - [构建 CentOS 7.9 离线 yum 源](./upgrade_yum_source_centos7_9.md)

    - [构建 RedHat 8.4 离线 yum 源](./upgrade_yum_source_redhat8_4.md)

#### Toolkit 配置参数

1. __Toolkit.enable__ ：默认开启，主要用于加速并行计算应用程序的开发和优化。

2. __Toolkit.image__ ：配置 Toolkit 镜像，推荐默认镜像： __nvidia/k8s/container-toolkit__ 。

3. __Toolkit.repository__ ：所在的镜像仓库，默认为 __nvcr.m.daocloud.io__ 仓库。

4. __Toolkit.version__ ：Toolkit 镜像的版本。默认使用 centos 的镜像，如果使用ubuntu，需要手动修改 addon 的yaml，将centos，改成ubuntu。具体型号参考:https://catalog.ngc.nvidia.com/orgs/nvidia/teams/k8s/containers/container-toolkit/tags

#### MIG 配置参数

详细配置方式请参考[开启 MIG 功能](mig/create_mig.md)

1. __MigManager.enabled__ ：是否启用 MIG 能力特性。
2. **MigManager.Config.name**: MIG 的切分配置文件名，用于定义 MIG 的（GI ,CI）切分策略。默认为 __default-mig-parted-config__ 。自定义参数参考[开启 MIG 功能](mig/create_mig.md)
3. __Mig.strategy__ ：节点上 GPU 卡的 MIG 设备的公开策略。NVIDIA 提供了两种公开 MIG 设备的策略（ __single__ 、 __mixed__ 策略，详情参考：[NVIDIA GPU 卡模式说明](index.md)

#### Node-Feature-Discovery 配置参数

1. __Node-Feature-Discovery.enableNodeFeatureAPI__ ：启用或禁用节点特性 API（Node Feature Discovery API）。

     - 当设置为 __true__ 时，启用了节点特性 API。
     - 当设置为 __false__ 或 __未设置__ 时，禁用节点特性 API。

### 下一步操作

完成上述相关参数配置和创建后：

1. 如果使用 **整卡模式**，[应用创建时可使用 GPU 资源](full_gpu_userguide.md)

2. 如果使用 **vGPU 模式** ，完成上述相关参数配置和创建后，下一步请完成 [vGPU Addon 安装](vgpu/vgpu_addon.md)

3. 如果使用 **MIG 模式**，并且需要给个别 GPU 节点按照某种切分规格进行使用，否则按照 MigManager.Config 中的 __default__ 值进行切分。

    - **single** 模式请给对应节点打上如下 Label：

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
        ```

    - **mixed** 模式请给对应节点打上如下 Label：

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
        ```

​    切分后，应用可[使用 MIG GPU 资源](mig/mig_usage.md)。
