# 安装依赖项

[部署好 k8s 集群](install-k8s.md)后，若想安装 DCE 5.0，还需要安装一些依赖项。

## 一条命令安装所有依赖项

在 k8s 集群的  Control Plane 上，执行以下一条命令安装依赖项：

```shell
curl -s https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh | bash
```

!!! note

    目前此脚本安装的依赖项包括：

    - helm 3.9.4
    - skopeo 1.9.2
    - kubectl 1.25.0
    - yq 4.27.5

## 离线安装依赖项

离线安装意味着目标主机的网络处于离线状态，无法下载上述工具的文件及压缩包，所以需要先在一个在线环境中制作好所需的离线包。

1. 制作离线包的命令如下:

    ```bash
    bash install_prerequisite.sh export
    ```

2. 当上述命令执行完成后, 会在当前目录生成名为 `pre_pkgs.tar.gz` 的压缩包, 该压缩包中会包含安装所需的所有文件。

    然后上传脚本及压缩包到离线环境中，并执行离线安装：

    ``` bash
    # 脚本与离线包都位于同一目录层级
    $ tree .
    .
    ├── install_prerequisite.sh
    └── pre_pkgs.tar.gz

    # 执行离线安装
    $ bash install_prerequisite.sh offline
    ```
