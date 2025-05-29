# 批量接入边缘节点

本文档介绍如何通过批量任务方式将多个边缘节点接入到系统中。通过批量接入功能，您可以：

- 实现批量节点接入，显著提升运维效率
- 降低运维成本，简化操作流程

## 前提条件

在开始批量接入边缘节点之前，请确保：

- 已准备一台控制节点，该节点需要能够访问所有待接入的边缘节点
- 云边协同模块版本已升级至 v0.19.0 或更高版本

## keadm 初始化脚本说明

为了简化 keadm 工具的初始化过程，我们提供了便捷的初始化脚本 'keadm_init.sh'，您可前往[下载中心](https://docs.daocloud.io/download/modules/kant)下载脚本文件。

该脚本支持以下两个重要参数：

- `MULTI_ARCH`：控制是否支持多架构节点接入
    - `false`：仅支持与控制节点相同架构的节点接入
    - `true`：支持同时接入 amd64 和 arm64 架构的节点
- `WITH_CONTAINERD`：控制是否自动安装 containerd
    - `false`：不自动安装 containerd
    - `true`：自动为节点安装默认版本的 containerd

## 批量节点接入步骤

### 在线模式

1. 创建工作目录

    ```bash
    mkdir keadm-join-node && cd keadm-join-node
    ```

2. 运行 keadm 初始化脚本

    ```bash
    # 根据实际需求设置 MULTI_ARCH 和 WITH_CONTAINERD 参数
    curl -sfL https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/keadm_init.sh | sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -s --
    ```

3. 准备批量配置文件并放置到工作目录中

    ```yaml
    # batch_join_config.yaml
    # 请根据实际情况修改 <xxx> 中的参数值
    # 注意：如果 keadm 初始化脚本中的 WITH_CONTAINERD=true，请保留 --pre-run=./containerd.sh 参数，否则请移除
    keadm:
      download:
        enable: false
      keadmVersion: v1.20.0
      archGroup:
        - amd64
      offlinePackageDir: .
      cmdTplArgs:
        cmd: join <--pre-run=./containerd.sh> --cgroupdriver=cgroupfs --cloudcore-ipport=<master-ip>:30000 --hub-protocol=websocket --certport=30002 --image-repository=docker.m.daocloud.io/kubeedge --kubeedge-version=v1.17.0 --set modules.edgeHub.quic.server=<master-ip>:30001,modules.edgeStream.server=<master-ip>:30004,modules.edgeHub.websocket.server=<master-ip>:30000,modules.edgeStream.enable=true
        token: <token>
      nodes:
        - nodeName: ubuntu1
          copyFrom: ./manifests
          keadmCmd: '{{.cmd}} --edgenode-name=<接入节点名称1> --token={{.token}}'
          ssh:
            ip: <node-ip>
            username: root   # 使用 root 用户登录
            auth:
              type: password
              passwordAuth:
                password: <****>
        - nodeName: ubuntu2
          copyFrom: ./manifests
          keadmCmd: '{{.cmd}} --edgenode-name=<接入节点名称2> --token={{.token}}'
          ssh:
            ip: <node-ip>
            username: root     # 使用 root 用户登录
            auth:
              type: password
              passwordAuth:
                password: <****>
      maxRunNum: 5
    ```

4. 使用 keadm 批量接入节点

    ```bash
    # 在工作目录下执行以下命令
    keadm batch --config=./batch-join-config.yaml
    ```

### 离线模式

1. 创建工作目录

    ```bash
    mkdir keadm-join-node && cd keadm-join-node
    ```

2. 准备离线安装包和初始化脚本

    根据您的安装场景，准备相应的安装包和初始化脚本文件：

    ```bash
    # 单架构不安装 containerd 
    ├── keadm-join-node
        └── keadm_{arch}.tar.gz
        └── keadm_init.sh

    # 单架构安装 containerd 
    ├── keadm-join-node
        └── keadm-containerd-{arch}.tar.gz
        └── keadm_init.sh
        
    # 多架构不安装 containerd 
    ├── keadm-join-node
        └── keadm_amd64.tar.gz
        └── keadm_arm64.tar.gz
        └── keadm_init.sh
        
    # 多架构安装 containerd 
    ├── keadm-join-node
        └── keadm-containerd-amd64.tar.gz
        └── keadm-containerd-arm64.tar.gz
        └── keadm_init.sh
    ```

3. 运行初始化脚本

    ```bash
    # 根据实际需求设置 MULTI_ARCH 和 WITH_CONTAINERD 参数
    sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -c keadm_init.sh
    ```

4. 准备配置文件

    参考在线模式的配置说明，创建 `batch-join-config.yaml` 文件。确保目录结构如下：

    ```bash
    # 以单架构不安装 containerd 模式为例
    ├── keadm-join-node
        └── keadm_{arch}.tar.gz
        └── {arch}
            └── keadm-{version}-linux-{arch}.tar.gz
        └── keadm_init.sh
        └── batch-join-config.yaml
    ```

5. 执行批量接入命令

    ```bash
    # 在工作目录下执行以下命令
    keadm batch --config=./batch-join-config.yaml
    ```