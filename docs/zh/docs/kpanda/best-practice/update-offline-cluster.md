# 工作集群离线部署/升级指南

!!! note

    本文仅针对离线模式下，使用 DCE 5.0 平台所创建的工作集群的 kubernetes 的版本进行部署或升级，
    不包括其它 kubeneters 组件的部署或升级。

本文适用以下离线场景：

- 用户可以通过以下操作指南，部署 DCE 5.0 平台所创建的非界面中推荐的 Kubernetes 版本。
- 用户可以通过制作增量离线包的方式对使用 DCE 5.0 平台所创建的工作集群的 kubernetes 的版本进行升级。

整体的思路为：

1. 在联网节点构建离线包
2. 将离线包导入火种节点
3. 更新[全局服务集群](../user-guide/clusters/cluster-role.md#_2)的 Kubernetes 版本清单
4. 使用平台 UI 创建工作集群或升级工作集群的 kubernetes 版本

!!! note

    目前支持构建的离线 kubernetes 版本，请参考 [kubean 支持的 kubernetes 版本列表](../../community/kubean.md#kubernetes)。

## 在联网节点构建离线包

由于离线环境无法联网，用户需要事先准备一台能够 **联网的节点** 来进行增量离线包的构建，并且在这个节点上启动 Docker 或者 podman 服务。
参阅[如何安装 Docker？](../../blogs/2023/230315-install-on-linux.md)

1. 检查联网节点的 Docker 服务运行状态

    ```bash
    ps aux|grep docker
    ```

    预期输出如下：

    ```console
    root     12341  0.5  0.2 654372 26736 ?        Ssl  23:45   0:00 /usr/bin/docked
    root     12351  0.2  0.1 625080 13740 ?        Ssl  23:45   0:00 docker-containerd --config /var/run/docker/containerd/containerd.toml
    root     13024  0.0  0.0 112824   980 pts/0    S+   23:45   0:00 grep --color=auto docker
    ```

2. 在联网节点的 __/root__ 目录下创建一个名为 __manifest.yaml__ 的文件，命令如下：

    ```bash
    vi manifest.yaml
    ```

    __manifest.yaml__ 内容如下：

    ```yaml title="manifest.yaml"
    image_arch:
    - "amd64"
    kube_version: # 填写待升级的集群版本
    - "v1.28.0"
    ```

    - __image_arch__ 用于指定 CPU 的架构类型，可填入的参数为 __amd64__ 和 __arm64__ 。
    - __kube_version__ 用于指定需要构建的 kubernetes 离线包版本，可参考上文的支持构建的离线 kubernetes 版本。

3. 在 __/root__ 目录下新建一个名为 __/data__ 的文件夹来存储增量离线包。

    ```bash
    mkdir data
    ```

    执行如下命令，使用 kubean `airgap-patch` 镜像生成离线包。
    `airgap-patch` 镜像 tag 与 Kubean 版本一致，需确保 Kubean 版本覆盖需要升级的 Kubernetes 版本。

    ```bash
    # 假设 kubean 版本为 v0.13.9
    docker run \
        -v $(pwd)/data:/data \
        -v $(pwd)/manifest.yml:/manifest.yml \
        -e ZONE=CN \
        -e MODE=FULL \
        ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.13.9
    ```

    | 环境变量 | 可选值描述 | 默认值 |
    | ------ | --------- | ----- |
    | ZONE | - `DEFAULT`：采用默认原始地址下载离线资源<br/> -`CN`：采用国内 DaoCloud 加速器地址下载离线资源 | `DEFAULT` |
    | MODE | - `INCR`：仅构建配置中指定组件的离线资源（即：增量包）<br/> - `FULL`：将构建配置中指定的组件以及集群部署必要其他组件的离线资源（即：全量包）| `INCR` |

    等待 Docker 服务运行完成后，检查 __/data__ 文件夹下的文件，文件目录如下：

    ```console
    data
    ├── amd64
    │   ├── files
    │   │   ├── import_files.sh
    │   │   └── offline-files.tar.gz
    │   ├── images
    │   │   ├── import_images.sh
    │   │   └── offline-images.tar.gz
    │   └── os-pkgs
    │       └── import_ospkgs.sh
    └── localartifactset.cr.yaml
    ```

## 将离线包导入火种节点

1. 将联网节点的 __/data__ 文件拷贝至火种节点的 __/root__ 目录下，在 **联网节点** 执行如下命令：

    ```bash
    scp -r data root@x.x.x.x:/root
    ```

    `x.x.x.x` 为火种节点 IP 地址

2. 在火种节点上将 __/data__ 文件内的镜像文件拷贝至火种节点内置的 docker resgitry 仓库。登录火种节点后执行如下命令：

    1. 进入镜像文件所在的目录
    
        ```bash
        cd data/amd64/images
        ```

    2. 执行 __import_images.sh__ 脚本将镜像导入火种节点内置的 Docker Resgitry 仓库。
   
        ```bash
        REGISTRY_ADDR="127.0.0.1"  ./import_images.sh
        ```

    !!! note

        上述命令仅仅适用于火种节点内置的 Docker Resgitry 仓库，如果使用外部仓库请使用如下命令：
        
        ```shell
        REGISTRY_SCHEME=https REGISTRY_ADDR=${registry_address} REGISTRY_USER=${username} REGISTRY_PASS=${password} ./import_images.sh
        ```

        - REGISTRY_ADDR 是镜像仓库的地址，比如1.2.3.4:5000
        - 当镜像仓库存在用户名密码验证时，需要设置 REGISTRY_USER 和 REGISTRY_PASS

3. 在火种节点上将 __/data__ 文件内的二进制文件拷贝至火种节点内置的 Minio 服务上。

    1. 进入二进制文件所在的目录
    
        ```bash
        cd data/amd64/files/
        ```

    2. 执行 import_files.sh 脚本将二进制文件导入火种节点内置的 Minio 服务上。
    
        ```bash
        MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_files.sh http://127.0.0.1:9000
        ```

!!! note

    上述命令仅仅适用于火种节点内置的 Minio 服务，如果使用外部 Minio 请将 `http://127.0.0.1:9000` 替换为外部 Minio 的访问地址。
    “rootuser” 和 “rootpass123”是火种节点内置的 Minio 服务的默认账户和密码。

## 更新全局服务集群的 kubernetes 版本清单

火种节点上执行如下命令，将 `manifest`、`localartifactset` 资源部署到全局服务集群：

```bash
# 部署 data 文件目录下的 localArtifactSet 资源
cd ./data
kubectl apply -f localartifactset.cr.yaml

# 下载 release-2.21 版本的 manifest 资源
wget https://raw.githubusercontent.com/kubean-io/kubean-manifest/main/manifests/manifest-2.21-d6f688f.yaml

# 部署 release-2.21 对应的 manifest 资源
kubectl apply -f manifest-2.21-d6f688f.yaml
```

## 下一步

登录 DCE 5.0 的 UI 管理界面，您可以继续执行以下操作：

1. 参照[创建集群的文档](../user-guide/clusters/create-cluster.md)进行工作集群创建，此时可以选择 Kubernetes 增量版本。

2. 参照[升级集群的文档](../user-guide/clusters/upgrade-cluster.md)对自建的工作集群进行升级。
