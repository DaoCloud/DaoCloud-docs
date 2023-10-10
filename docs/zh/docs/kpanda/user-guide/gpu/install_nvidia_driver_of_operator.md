# GPU Operator 离线安装

本文介绍如何基于火种节点的离线源来部署 GPU Operator 。本文使用的 AMD 架构的 Centos 7.9 （3.10.0-1160） 进行演示。本章节覆盖 NVIDIA GPU 的多种使用模式的参数配置。

- GPU 整卡模式

- GPU vGPU 模式

- GPU MIG 模式

  使用模式详情请参考：[NVIDIA GPU 卡使用模式](overvie_nvidia_gpu.md)

!!!note

    Daocloud 内置了 Centos 7.9 3.10.0-1160 的 GPU Operator 离线包，如需使用其它操作系统和内核版本，请参考构建 GPU Operator 离线包 进行构建。

### 前提条件

- 待安装 GPU 驱动节点系统要求请参考：[GPU 支持矩阵](gpu_matrix.md)，本章节使用  AMD 架构的 Centos 7.9 （3.10.0-1160）
- 确认集群节点上具有对应型号的 GPU 卡（[NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/)、 [A100](https://www.nvidia.com/en-us/data-center/a100/) 和 [A30](https://www.nvidia.com/en-us/data-center/products/a30-gpu/) Tensor Core GPU），详情参考：[GPU 支持矩阵](gpu_matrix.md)

### 操作步骤

参考如下步骤为集群安装 GPU Operator 插件。

1. 登录 DCE 5 容器管理平台，进入容器管理界面，在待安装 GPU Operator 的集群详情中进入 `Helm 模版` 页面。

2. 在 `Helm 模版` 页面选择 `全部仓库`，并在右侧搜索栏输入 `gpu-operator` 进行搜索。

3. 点击进入 `gpu-operator` 模版的详情页面，点击`安装`按钮进入安装配置页面。

4. **基本参数** 配置如下：

    - 名称：输入插件名称，请注意名称最长 63 个字符，只能包含小写字母、数字及分隔符（“-”），且必须以小写字母或数字开头及结尾，例如 gpu-operator。
    - 命名空间：选择将插件安装的命名空间。
    - 版本：插件的版本，此处以 `23.6.10` 版本为例。
    - 就绪等待：启用后，将等待应用下的所有关联资源都处于就绪状态，才会标记应用安装成功。
    - 失败删除：如果插件安装失败，则删除已经安装的关联资源。开启后，将默认同步开启`就绪等待`。
    - 详情日志：开启后，将记录安装过程的详细日志。

5. **高级参数** 配置如下：

    - DivicePlugin.enable 参数：用于配置安装 GPU Operator 时，是否启用 Device Plugin，这取决于您对 GPU 的使用规划，请根据以下使用场景选择开启或关闭：

    - 使用应用独占**整张 GPU** 卡时请**启用**。

    - 使用  **vGPU** 时请 **关闭**。

    - 使用 **GPU MIG  **时请 **启用**。启用前请确认卡型号符合要求：[GPU 支持矩阵](gpu_matrix.md)

    - Driver.enable 参数：开启后自动部署 NVIDIA 驱动。

    - Driver.image 参数：用于指定 GPU 驱动的镜像版本，推荐使用默认镜像：`nvidia/driver`。

    - RepoConfig.ConfigMapName 参数：部署  GPU Operator 的离线源配置文件名称，参考如下步骤创建名为 `local-repo-config` 的配置文件。

    - 在 DCE 5 平台部署完成后，使用 ssh 或其它方式进入火种节点，获取火种节点离线源配置文件 `extension.repo`，可执行如下命令查看：

        ```yaml
        cat /etc/yum.repos.d/extension.repo #查看 extension.repo 中的内容。
        
        # 一般输出如下：
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

        复制配置文件 extension.repo 中的内容，在需要安装 GPU-Operator 的集群中使用界面新建一个名为`local-repo-config` 的配置文件，可参考[创建配置项](../configmaps-secrets/create-configmap.md)进行创建。
        **注意：配置数据的 key 值必须为 "CentOS-Base.repo",value 值为火种节点离线源配置文件 extension.repo 中的内容**

    - RepoConfig.repository 参数：用于指定 GPU 驱动离线源仓库。推荐使用默认参数：`nvcr.io`。

    - RepoConfig.version 参数：用于指定 GPU 驱动的镜像版本，仅使用在线安装 GPU Operator 时需要配置，NVDIA 为常用的操作系统和内核提供了相关的驱动镜像，
        详情查阅 NVIDIA GPU Driver 。对于不同的操作系统 Driver 镜像的名称会存在显著的差异：

         - 对于 Ubuntu 系统， Driver 镜像的命名规则为：<driver-branch>-<linux-kernel-version>-<os-tag>。
           如 "525-5.15.0-69-ubuntu22.04"，525 用于指定 CUDA 的版本，5.15.0-69 指定内核的版本，ubuntu22.04 指定 OS 版本。
           注意：对于 Ubuntu ，NVIDIA 的 driver 镜像版本需要和节点内核版本强一致，包括小版本号)，可前往  NVIDIA GPU Driver 检查该版本驱动是否存在。

         - 对于 RedHat/CentOS 系列的系统， Driver 镜像的命名规则通常为 CUDA 的版本和 OS 版本组成，如 "535.104.05-centos7"。

    - Driver.image 参数：用于指定 GPU 驱动的镜像版本，推荐使用默认镜像：`nvidia/driver`。

    

    **MIG 配置参数**

    - Mig.enabled 参数：是否启用 MIG 能力特性。需要注意：

        - 启用 MIG 需要您的 GPU 卡支持 MIG 特性，才能使用 MIG 切分 GPU 资源，参考[GPU 支持矩阵](gpu_matrix.md)查看您的 GPU 卡是否支持开启 MIG 特性。
        - 启用 MIG 需要开启 DivicePlugin 参数。

    - Mig.strategy 参数：用于配置节点上 GPU 卡的 MIG 设备的公开策略。NVIDIA 提供了两种在 Kubernetes 节点上公开 MIG 设备的策略（`single` 、`mixed`策略，策略详情参考：[GNVIDIA GPU 卡使用模式](overvie_nvidia_gpu.md)）:

        **single 模式 **：节点仅在其所有 GPU 上公开单一类型的 MIG 设备。节点上的所有 GPU 必须：

        - 属于同一个型号（例如 A100-SXM-40GB），只有同一型号 GPU 的 MIG Profile 才是一样的。
        - 启用 MIG 配置，需要重启机器才能生效。
        - 为在所有产品中公开“完全相同”的 MIG 设备类型，创建相同的GI和CI。

        **mixed 模式**：节点在其所有 GPU 上公开混合 MIG 设备类型。请求特定的 MIG 设备类型需要设备类型提供的计算切片数量和内存总量。节点上的所有 GPU 必须：

        - 属于同一产品线（例如 A100-SXM-40GB）。同时允许单个 GPU 启用或不启用 MIG，并且可以自由配置任何可用 MIG 设备类型的混合搭配。

    - MigManager.Config : 用于配置 MIG 切分配置参数，请提前按照如下 YAML 配置，创建对应 配置文件,如：`custome-mig-parted-config`

        - Config.default: 节点默认使用的切分配置参数，默认为 `all-disbled`，可填入配置文件中对应的规格（如：`all-1g.10gb`等），输入值说明如下：

            -  `all-disbled` ： 所有节点设备默认禁用 MIG
            - `配置规格（如：all-1g.10gb）`：所有节点默认使用输入规格切分

            若需要给个别GPU 节点按照某种切分规格进行使用，请给对应节点打上 Label：

            - **single** 模式请给对应节点打上如下 Label：

              ```
              kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
              ```

            - **mixed** 模式请给对应节点打上如下 Label：

              ```
              kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
              ```

            - Config.name 参数：MIG 的切分配置参数文件名，参考如下 YAML 创建名为 `custom-mig-parted-config`的配置文件，用来配置 MIG 的（GI ,CI）切分策略。MIG 切分逻辑可参考 [NVIDIA 多实例 GPU(MIG) 概述](./mig_index.md)。

            注意： 创建的配置文件（`custom-mig-parted-config`）名称不能同默认配置文件（`default-mig-parted-config`) 相同。

            A800 80G 卡配置的切分规则，默认如下，用户可基于自身卡的特性进行调整：

        ```yaml
        # 自定义切分 GI 实例配置
          all-disabled:
          - devices: all
              mig-enabled: false
              # 所有设备禁用 MIG
          all-enabled:
          - devices: all
              mig-enabled: true
              mig-devices: {}
              # 所有设备启用 MIG，但没有指定任何 MIG 设备
          all-1g.10gb:
          - devices: all
              mig-enabled: true
              mig-devices:
              1g.5gb: 7
              # 所有设备启用 MIG，使用 1G.5GB 的 MIG 设备，数量为 7
          all-1g.10gb.me:
          - devices: all
              mig-enabled: true
              mig-devices:
              1g.10gb+me: 1
              # 所有设备启用 MIG，使用 1G.10GB+ME 的 MIG 设备，数量为 1
          all-1g.20gb:
          - devices: all
              mig-enabled: true
              mig-devices:
              1g.20gb: 4
              # 所有设备启用 MIG，使用 1G.20GB 的 MIG 设备，数量为 4
          all-2g.20gb:
          - devices: all
              mig-enabled: true
              mig-devices:
              2g.20gb: 3
              # 所有设备启用 MIG，使用 2G.20GB 的 MIG 设备，数量为 3
          all-3g.40gb:
          - devices: all
              mig-enabled: true
              mig-devices:
              3g.40gb: 2
              # 所有设备启用 MIG，使用 3G.40GB 的 MIG 设备，数量为 2
          all-4g.40gb:
          - devices: all
              mig-enabled: true
              mig-devices:
              4g.40gb: 1
              # 所有设备启用 MIG，使用 4G.40GB 的 MIG 设备，数量为 1
          all-7g.80gb:
          - devices: all
              mig-enabled: true
              mig-devices:
              7g.80gb: 1
              # 所有设备启用 MIG，使用 7G.80GB 的 MIG 设备，数量为 1
          all-balanced:
          - device-filter: ["0x233110DE", "0x232210DE", "0x20B210DE", "0x20B510DE", "0x20F310DE", "0x20F510DE"]
              devices: all
              mig-enabled: true
              mig-devices:
              1g.10gb: 2
              2g.20gb: 1
              3g.40gb: 1
              # 所有设备启用 MIG，使用不同规格的 MIG 设备进行平衡切分
          # 自定义切分 CI 实例配置
          custom-config: # 设置后会按照设置规格切分 CI 实例
          - devices: all
              mig-enabled: true
              mig-devices:
              3g.40gb: 2
              # 所有设备启用 MIG，使用 3G.40GB 的 MIG 设备，数量为 2
        ```

        复制上述内容，作为配置数据中的 vaule 值，前往界面创建名为 `custom-mig-parted-config` 的配置文件。注意：配置数据的 key 必须为 `config.yaml`。

    - Node-Feature-Discovery.enableNodeFeatureAPI 参数：用于启用或禁用节点特性API（Node Feature Discovery API）。
        当 enableNodeFeatureApi 参数设置为 true 时，表示启用了节点特性 API，Kubernetes 集群会收集节点的特性信息并将其提供给其他组件和工具使用。
        当参数设置为 false 或未设置时，则禁用节点特性 API，节点的特性信息将不会被收集和公开。

    -  点击`确定`按钮，完成 `gpu-operator` 插件的安装。

    - 若开启了 **MIG 模式**，并且需要给个别GPU 节点按照某种切分规格进行使用，否则按照 MigManager.Config 中的 default 值进行切分

        - **single** 模式请给对应节点打上如下 Label：

            ```
            kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
            ```

        - **mixed** 模式请给对应节点打上如下 Label：

            ```
            kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
            ```

            

    
