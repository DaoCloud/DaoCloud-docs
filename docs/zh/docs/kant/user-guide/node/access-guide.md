# 接入边缘节点

根据节点接入配置，获取安装文件和接入命令，在节点上安装边缘核心软件 EdgeCore，这样边缘节点就能与 DCE 5.0 云边协同建立连接，纳入平台管理。

边缘节点初次接入时，自动安装最新版本的边缘核心软件 EdgeCore。

!!! note

    - 接入配置与实际的边缘节点机器是一对一的关系，一个接入配置的安装文件和接入命令只能在单台实际的边缘节点上使用。
    - 本文接入指南仅适用于云边协同模块 v0.20 及以上版本，如果低于 v0.20 版本，请参考历史版本[边缘节点接入指南](./access-guide-v0.19.md) 

本文主要介绍单节点接入流程，如果您想快速批量接入节点，请参考 [批量接入边缘节点](./batch-access-guide.md)。

## 前提条件

- 已经按要求准备好节点，并配置好节点环境，具体请参见[边缘节点接入要求](./join-rqmt.md)
- 已经创建好边缘节点接入配置，具体请参见[创建接入配置](./create-access-guide.md)

!!! note

    如果您是离线环境下接入异构节点，请先进行 Helm 应用多架构融合操作，操作流程参考[Helm 应用多架构和升级导入步骤](../../../kpanda/user-guide/helm/multi-archi-helm.md)。

## 操作步骤

1. 边缘节点列表 页面，点击 **接入节点** 按钮，进入接入节点页面。

    ![节点列表](../../images/access-guide-06.png)

1. 根据节点环境配置，选择对应的接入配置，同时输入节点名称，然后点击 **获取接入步骤**。

    ![接入节点](../../images/access-guide-07.png)

1. 通过在线或离线接入方式，执行操作，接入节点。

    === "在线接入"

        如果您的环境可以访问外网，建议选择在线接入方式。

        1. 在接入步骤抽屉弹框界面，点击 __在线接入__ 页签，显示在线接入安装步骤。

            ![在线接入](../../images/access-guide-08.png)    

        1. 使用脚本准备 keadm 工具，执行界面中展示的命令。

            !!! note

                建议先创建一个空的工作目录，在该目录下执行脚本。

            ```shell
            curl -sfL https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/keadm_init.sh | sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -s --
            ```

        1. 执行界面中展示的接入命令，接入节点。

            !!! note

                请注意接入命令中的 token 有效期，如果 token 失效，请刷新页面重新获取。

            命令示例：

            ```shell
            keadm join \
              --cgroupdriver=cgroupfs \
              --cloudcore-ipport=10.64.24.29:30000 \
              --hub-protocol=websocket \
              --certport=30002 \
              --image-repository=docker.m.daocloud.io/kubeedge \
              --labels=batch-node.kant.io/protocol-type=websocket,kant.io/batch=test \
              --kubeedge-version=v1.20.0 \
              --remote-runtime-endpoint=unix:///run/containerd/containerd.sock \
              --set \
                modules.edgeStream.server=10.64.24.29:30004,\
                modules.edgeStream.enable=true,\
                modules.metaManager.enable=true,\
                modules.metaManager.metaServer.enable=true,\
                modules.serviceBus.enable=true,\
                modules.edgeHub.websocket.server=10.64.24.29:30000 \
              --token=f06150c1f9469047fd459187f6c1eb539b2778373ff874e55786c1c721ff8a29.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTEwNzY3ODd9.ATFgzWCHJhGGTYDwCk7E6SrbXh0STv40JuZwCUgX2H0
            ```

    === "离线接入"

        如果您的环境不可以访问外网，请选择离线接入方式。

        1. 在接入步骤抽屉弹框界面，点击 __离线接入__ 页签，显示离线线接入安装步骤。

            ![在线接入](../../images/access-guide-09.png)    

        1. 点击 **下载文件** 按钮，跳转到下载中心，在下载列表中选择对应架构的边端安装包和初始化脚本。

        1. 将安装包文件和脚本文件拷贝到要接入的边缘节点的同一个目录下，并在该目录下执行初始化脚本。

            !!! note

                建议创建一个空的工作目录，来存放相关文件。

            ```shell
            sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -c keadm_init.sh
            ```

        1. 接入节点，执行如下命令。

            ```shell
            keadm join \
              --cgroupdriver=cgroupfs \
              --cloudcore-ipport=10.64.24.29:30000 \
              --hub-protocol=websocket \
              --certport=30002 \
              --image-repository=docker.m.daocloud.io/kubeedge \
              --labels=batch-node.kant.io/protocol-type=websocket,kant.io/batch=test \
              --kubeedge-version=v1.20.0 \
              --remote-runtime-endpoint=unix:///run/containerd/containerd.sock \
              --set \
                modules.edgeStream.server=10.64.24.29:30004,\
                modules.edgeStream.enable=true,\
                modules.metaManager.enable=true,\
                modules.metaManager.metaServer.enable=true,\
                modules.serviceBus.enable=true,\
                modules.edgeHub.websocket.server=10.64.24.29:30000 \
              --token=f06150c1f9469047fd459187f6c1eb539b2778373ff874e55786c1c721ff8a29.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTEwNzY3ODd9.ATFgzWCHJhGGTYDwCk7E6SrbXh0STv40JuZwCUgX2H0
            ```

1. 验证边缘节点是否纳管成功。

    1. 选择左侧导航栏的 __边缘计算__ -> __云边协同__ ，进入边缘单元列表页面。

    1. 点击边缘单元名称，进入边缘单元详情页。

    1. 选择左侧导航栏的 __边缘资源__ -> __边缘节点__ ，进入边缘节点列表页面。

    1. 查看边缘节点的状态，当前状态为 __健康__ 表示纳管成功。

    ![边缘节点纳管成功](../../images/access-guide-05.png)
