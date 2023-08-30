# 工作集群离线升级指南

!!! note

    本文仅针对离线模式下，使用 DCE 5.0 平台所创建的工作集群的 kubernetes 的版本进行升级，不包括其它 kubeneters 组件的升级。

## 概述

在离线场景下，用户可以通过制作增量离线包的方式对使用 DCE 5.0 平台所创建的工作集群的 kubernetes 的版本进行升级。整体的升级思路为：在联网节点构建离线包 → 将离线包导入火种节点 → 更新 Global 集群的 kubernetes 版本清单  →  使用平台 UI 升级工作集群的 kubernetes 版本 。

!!! note

    目前支持构建的离线 kubernetes 版本如下：

    - v1.26.3, v1.26.2, v1.26.1, v1.26.0, v1.25.8
    - v1.25.7, v1.25.6, v1.25.5, v1.25.4, v1.25.3, v1.25.2, v1.25.1, v1.25.0,
    - v1.24.12, v1.24.11, v1.24.10, v1.24.9, v1.24.8, v1.24.7, v1.24.6, v1.24.5, v1.24.4, v1.24.3, v1.24.2, v1.24.1, v1.24.0

## 在联网节点构建离线包

由于离线环境无法联网，用户需要事先准备一台能够**联网的节点**来进行增量离线包的构建，并且在这个节点上启动 Docker 服务。[如何安装 Docker？](../../blogs/230315-install-on-linux.md)

1. 检查联网节点的 Docker 服务运行状态

    ```bash
    # 查看节点下 Docker 进程的运行状态
    ps aux|grep docker 

    # 预期输出如下：
    root     12341  0.5  0.2 654372 26736 ?        Ssl  23:45   0:00 /usr/bin/docked
    root     12351  0.2  0.1 625080 13740 ?        Ssl  23:45   0:00 docker-containerd --config /var/run/docker/containerd/containerd.toml
    root     13024  0.0  0.0 112824   980 pts/0    S+   23:45   0:00 grep --color=auto docker
    ```

2. 在联网节点的 `/root` 目录下创建一个名为 `manifest.yaml` 的文件，命令如下：

    ```bash
    vi manifest.yaml
    ```

    `manifest.yaml` 内容如下：

    ```yaml
    image_arch:
    - "amd64"
    kube_version:
    - "v1.25.5"
    - "v1.25.4"
    - "v1.24.8"
    - "v1.24.5"
    ```

    - `image_arch` 用于指定 CPU 的架构类型，可填入的参数为 `amd64` 和`arm64`。
    - `kube_version` 用于指定需要构建的 kubernetes 离线包版本，可参考上文的支持构建的离线 kubernetes 版本。

3. 在 `/root` 目录下新建一个名为 `/data` 的文件夹来存储增量离线包。

    ```bash
    mkdir data
    ```

    执行如下命令，使用 `ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.4.8` 镜像生成离线包。

    更多关于 `ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.4.8` 镜像的信息，
    请前往 [kubean](https://github.com/orgs/kubean-io/packages)。

    ```bash
    docker run --rm -v $(pwd)/manifest.yml:/manifest.yml -v $(pwd)/data:/data ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.4.8
    ```

    等待 docker 服务运行完成后，检查 `/data` 文件夹下的文件，文件目录如下：

    ```bash
    data
    └── v_offline_patch
        ├── amd64
        │   ├── files
        │   │   ├── import_files.sh
        │   │   └── offline-files.tar.gz #二进制文件
        │   └── images
        │       ├── import_images.sh
        │       └── offline-images.tar.gz #镜像文件
        └── kubeanofflineversion.cr.patch.yaml
    ```

## 将离线包导入火种节点

1. 将联网节点的 `/data` 文件拷贝至火种节点的 `/root` 目录下，在**联网节点**执行如下命令：

    ```bash
    scp -r data root@x.x.x.x:/root
    ```

    !!! note

        “x.x.x.x“ 为火种节点 IP 地址

2. 在**火种节点**上将 `/data` 文件内的镜像文件拷贝至火种节点内置的 docker resgitry 仓库。登录火种节点后执行如下命令：

    1. 进入镜像文件所在的目录
    
        ```bash
        cd data/v_offline_patch/amd64/images
        ```

    2. 执行 import_images.sh 脚本将镜像导入火种节点内置的 docker resgitry 仓库。
   
        ```bash
        DEST_TLS_VERIFY=false ./import_images.sh 127.0.0.1:443
        ```

    !!! note

        上述命令仅仅适用于火种节点内置的 docker resgitry 仓库，如果使用外部仓库请使用如下命令：
        
        ```yaml
        DEST_USER=${username} DEST_PASS=${password} DEST_TLS_VERIFY=false ./import_images.sh https://x.x.x.x:443
        ```
        
        ”https://x.x.x.x:443” 为外部仓库的地址。
        “DEST_USER=${username} DEST_PASS=${password}” 外部仓库的用户名和密码参数。
        如果外部仓库为免密，则可删除此参数。

3. 在火种节点上将`/data` 文件内的二进制文件拷贝至火种节点内置的 Minio 服务上。

    1. 进入二进制文件所在的目录
    
        ```bash
        cd data/v_offline_patch/amd64/files/
        ```

    2. 执行 import_files.sh 脚本将二进制文件导入火种节点内置的 Minio 服务上。
    
        ```bash
        MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_files.sh http://127.0.0.1:9000
        ```

!!! note

    上述命令仅仅适用于火种节点内置的 Minio 服务，如果使用外部 Minio 请将“http://127.0.0.1:9000” 替换为外部 Minio 的访问地址。
    “rootuser” 和 “rootpass123”是火种节点内置的 Minio 服务的默认账户和密码。

## 更新 Global 集群的 kubernetes 版本清单

1. 将联网节点的 `/data` 文件内的 `kubeanofflineversion.cr.patch` 清单配置文件拷贝至 Global 集群内任一 **Master 节点**的 `/root` 目录下，请在**联网节点**执行如下命令：

    ```bash
    scp -r data/v_offline_patch/kubeanofflineversion.cr.patch.yaml root@x.x.x.x:/root
    ```

    !!! note

        “x.x.x.x“ 为 Global 集群内任一 Master 节点 IP 地址


2. 完成上一步后登录 Global 集群内任一 **Master 节点**执行清单配置文件，命令如下：

    ```bash
    kubectl apply -f kubeanofflineversion.cr.patch.yaml
    ```

## 使用平台 UI 升级工作集群的 kubernetes 版本

登录 DCE 5.0 的 UI 管理界面，参照[集群升级文档](../../kpanda/user-guide/clusters/upgrade-cluster.md)对平台自建的工作集群进行升级。
