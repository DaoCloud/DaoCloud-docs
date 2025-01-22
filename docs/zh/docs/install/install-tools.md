# 安装依赖项

安装 DCE 5.0 之前，需要先安装一些依赖项。

- 对于社区版，请在 K8s Master 节点上安装依赖项。
- 对于商业版，请在[火种节点](./commercial/deploy-arch.md)上安装依赖项。

!!! note

    安装的依赖项大致包括：

    - podman
    - helm
    - skopeo
    - kind
    - kubectl
    - yq
    - minio client
    - charts-syncer
    
    安装过程中如果您的环境存在一些工具且版本低于我们定义的版本，会将对应工具进行强制更新替换。

## 在线安装依赖项

1. 下载脚本。

    ```bash
    export VERSION=v0.20.0   # (1)!
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh
    ```

    1. 安装器版本

    为 `install_prerequisite_${VERSION}.sh` 添加可执行权限：

    ```bash
    chmod +x install_prerequisite_${VERSION}.sh
    ```

2. 开始在线安装前置依赖。

    - 对于社区版

        ```bash
        bash install_prerequisite_${VERSION}.sh online community
        ```

    - 对于商业版

        ```bash
        bash install_prerequisite_${VERSION}.sh online full
        ```

## 离线安装依赖项

离线安装意味着目标主机的网络处于离线状态，无法下载所需依赖项，所以需先在一个在线环境中制作好离线包。

1. 找一台能连通外网的机器，下载安装脚本。

    ```bash
    export VERSION=v0.20.0
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh
    ```

2. 下载前置依赖组件离线包。

    ```bash
    export VERSION=v0.20.0
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_amd64.tar.gz
    ```

    !!! note

        - 如果是 arm 架构，请使用下载地址：
          <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_arm64.tar.gz>
        - 确保离线包与脚本在同一个目录层级

3. 将下载的这些离线包上传到一台 K8s 集群控制平面节点，执行离线安装。

    - 对于社区版

        ```bash
        export BINARY_TAR=prerequisite_${VERSION}_amd64.tar.gz
        chmod +x install_prerequisite_${VERSION}.sh
        ./install_prerequisite_${VERSION}.sh offline community
        ```

    - 对于商业版

        ```bash
        export BINARY_TAR=prerequisite_${VERSION}_amd64.tar.gz
        chmod +x install_prerequisite_${VERSION}.sh
        ./install_prerequisite_${VERSION}.sh offline full
        ```

接下来就可以安装 DCE 5.0 [社区版](community/resources.md)或[商业版](commercial/deploy-requirements.md)了。
