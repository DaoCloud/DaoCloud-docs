# 安装依赖项

部署好 Kubernetes 集群后，还需要安装一些依赖项，才能安装 DCE 5.0 体验新一代云原生操作系统的魅力。

## 一条命令安装所有依赖项

在 Kubernetes 集群的控制平面（Master 节点）上，执行以下一条命令安装依赖项：

```shell
curl -s http://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh | bash
```

!!! note

    这条 curl 命令会调用预先制作的脚本 `install_prerequisite.sh`，目前此脚本安装的依赖项包括：

    - helm 3.9.4
    - skopeo 1.9.2
    - kubectl 1.25.0
    - yq 4.27.5

## 离线安装依赖项

离线安装意味着目标主机的网络处于离线状态，无法下载所需依赖项，所以需要先在一个在线环境中制作好离线包。

1. 制作离线包。

    ```bash
    bash install_prerequisite.sh export
    ```

2. 上传目录中的所有文件到离线环境，执行离线安装。

    ``` bash
    # 脚本与离线包都位于同一目录层级
    $ tree .
    .
    ├── install_prerequisite.sh
    └── pre_pkgs.tar.gz

    # 执行离线安装
    $ bash install_prerequisite.sh offline
    ```
