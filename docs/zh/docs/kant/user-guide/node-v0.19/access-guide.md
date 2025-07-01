# 接入边缘节点

根据节点接入配置，获取安装文件和接入命令，在节点上安装边缘核心软件 EdgeCore，这样边缘节点就能与 DCE 5.0 云边协同建立连接，纳入平台管理。

边缘节点初次接入时，自动安装最新版本的边缘核心软件 EdgeCore。

!!! note

    接入配置与实际的边缘节点机器是一对多的关系，一个接入配置的安装文件和接入命令可以在多台实际的边缘节点上使用。

## 前提条件

- 已经按要求准备好节点，并配置好节点环境，具体请参见[边缘节点接入要求](./join-rqmt.md)
- 已经创建好边缘节点接入指南，具体请参见[创建接入配置](./create-access-guide.md)

!!! note

    如果您是离线环境下接入异构节点，请先进行 Helm 应用多架构融合操作，操作流程参考[Helm 应用多架构和升级导入步骤](../../../kpanda/user-guide/helm/multi-archi-helm.md)。

![接入节点](../../images/access-guide-03.png)

## 操作步骤

1. 边缘节点列表 页面，点击 **接入节点** 按钮，右侧会弹出接入节点弹框。

1. 根据节点环境配置，选择对应的接入配置。

1. 点击 **下载文件** 按钮，跳转到下载中心，在下载列表中选择对应版本和架构的边端安装包：`kantadm_{版本}_{架构}.tar.gz`。建议选择最新版本。

    ![下载边端安装包](../../images/access-guide-04.png)

1. 将边端安装包拷贝到要接入的边缘节点，并解压。

    解压命令：

    ```shell
    tar -zxf kantadm_{version}_{tarch}.tar.gz
    ```

    !!! note

        将解压后的 kantadm 二进制文件放到 `/usr/local/bin` 目录下。

1. 通过 token 或证书方式，执行命令，接入节点。

    **token 安装**

    1. 接入指南界面，第三步点击 __token 安装__ 页签，显示 token 安装步骤。

        !!! note

            安装命令的 token 24小时内有效，如需长期有效的安装方式，请使用证书安装。

    1. 接入节点，执行如下命令。

        ```shell
        kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --token=b2d6bb5d9312c39ffac08ecfd5030bed006b8b67d0799d632d381f19fca9e765.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2NTk3NDV9.0sdaWbYSTURmAYmQwDn_zF7P9TwcRTSMhwPw6l87U7E --cgroup-driver=cgroupfs --remote-runtime-endpoint= --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003  --tunnel-port=30004 --labels=test=1,test1=1
        ```

    **证书安装**

    1. 接入节点界面，第三步点击 __证书安装__ 页签，显示证书安装步骤。

    1. 点击 __下载证书__ 按钮，将证书下载到本地。

    1. 保存证书，执行如下命令。

        ```shell
        mkdir -p /etc/kant && mv ./cert.tar /etc/kant/cert.tar
        ```

    1. 接入节点，执行如下命令。

        ```shell
        kantadm join --cloudcore-host=10.2.129.13 --websocket-port=30000 --node-prefix=sh --remote-runtime-endpoint=unix:///run/containerd/containerd.sock --cgroup-driver=cgroupfs --version=v1.12.6 --batch-name=guide-test --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003 --tunnel-port=30004
        ```

1. 验证边缘节点是否纳管成功。

    1. 选择左侧导航栏的 __边缘计算__ -> __云边协同__ ，进入边缘单元列表页面。

    1. 点击边缘单元名称，进入边缘单元详情页。

    1. 选择左侧导航栏的 __边缘资源__ -> __边缘节点__ ，进入边缘节点列表页面。

    1. 查看边缘节点的状态，当前状态为 __健康__ 表示纳管成功。

        ![边缘节点纳管成果](../../images/access-guide-05.png)
