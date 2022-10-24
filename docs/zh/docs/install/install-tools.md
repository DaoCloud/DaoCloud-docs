# 安装依赖项

[部署好 Kubernetes 集群](./install-k8s.md)后，还需要安装一些依赖项，才能安装 DCE 5.0 体验新一代云原生操作系统的魅力。

您可以根据自己的实际情况选择在线或离线安装。

!!! note

    安装的这些工具包括：

    - podman
    - helm
    - skopeo
    - kind
    - kubectl
    - yq
    - minio client

## 在线安装

1. 在 Kubernetes 集群的控制平面（Master 节点）上，下载脚本。

    ```shell
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
    ```

    为 `install_prerequisite.sh` 添加可执行权限：

    ```bash
    chmod +x install_prerequisite.sh
    ```

2. 开始在线安装前置依赖。

    - 社区版本安装

        ```bash
        bash install_prerequisite.sh online community
        ```

    - 全模式安装

        ```bash
        bash install_prerequisite.sh online full
        ```

## 离线安装

离线安装意味着目标主机的网络处于离线状态，无法下载所需依赖项，所以需要先在一个在线环境中制作好离线包。

1. 制作离线包。

    - 社区版制作命令

        ```bash
        bash install_prerequisite.sh export community
        ```

    - 全模式制作命令

        ```bash
        bash install_prerequisite.sh export full
        ```

    !!! note

        当上述命令执行完成后，会在当前目录生成名为 pre_pkgs.tar.gz 的压缩包，该压缩包中会包含我们安装所需的所有文件。

2. 上传目录中的所有文件到离线环境。

    ``` bash
    # 脚本与离线包都位于同一目录层级
    $ tree .
    .
    ├── install_prerequisite.sh
    └── pre_pkgs.tar.gz
    ```

3. 执行离线安装。

    - 社区版制作命令

        ```bash
        bash install_prerequisite.sh offline community
        ```

    - 全模式制作命令

        ```bash
         bash install_prerequisite.sh offline full
        ```

接下来就可以安装 DCE 5.0 了。
