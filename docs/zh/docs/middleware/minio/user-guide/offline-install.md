# 离线升级中间件 - MinIO 模块

本页说明从[下载中心](../../../download/index.md)下载中间件 - MinIO 模块后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `mcamel` 字样是中间件模块的内部开发代号。

## 从安装包中加载镜像

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 chart-syncer 同步镜像到镜像仓库，该方法更加高效便捷。

### chart-syncer 同步镜像到镜像仓库

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并修改相关配置。

    === "已安装 chart repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/mcamel # (3)
          repo:
            kind: HARBOR # (4)
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (5)
            auth:
            username: "admin" # (6)
            password: "Harbor12345" # (7)
          containers:
            auth:
              username: "admin" # (8)
              password: "Harbor12345" # (9)
        ```

        1. 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        2. 需更改为你的镜像仓库 url
        3. 需更改为你的镜像仓库
        4. 也可以是任何其他支持的 Helm Chart 仓库类别
        5. 需更改为 chart repo url
        6. 你的镜像仓库用户名
        7. 你的镜像仓库密码
        8. 你的镜像仓库用户名
        9. 你的镜像仓库密码

    === "未安装 chart repo"

        若当前环境未安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件，并存放在指定路径。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/mcamel # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        2. 需更改为你的镜像仓库 url
        3. 需更改为你的镜像仓库
        4. chart 本地路径
        5. 你的镜像仓库用户名
        6. 你的镜像仓库密码

1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Docker 或 containerd 直接加载

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf minio_0.8.1_amd64.tar
    ```

    解压成功后会得到 3 个文件：

    - hints.yaml
    - images.tar
    - original-chart

2. 从本地加载镜像到 Docker 或 containerd。

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr image import images.tar
        ```

!!! note

    每个 node 都需要做 Docker 或 containerd 加载镜像操作。
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 升级

有两种升级方式。您可以根据前置操作，选择对应的升级方案：

=== "通过 helm repo 升级"

    1. 检查 helm 仓库是否存在。

        ```shell
        helm repo list | grep minio
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加 helm 仓库。

        ```shell
        helm repo add mcamel-minio http://{harbor url}/chartrepo/{project}
        ```

    1. 更新 helm 仓库。

        ```shell
        helm repo update mcamel/mcamel-minio # (1)
        ```

        1. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    1. 选择您想安装的版本（建议安装最新版本）。

        ```shell
        helm search repo mcamel/mcamel-minio --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-minio --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-minio     0.8.1           0.8.1           A Helm chart for Kubernetes
        ...
        ```

    1. 备份 `--set` 参数。

        在升级版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values mcamel-minio -n mcamel-system -o yaml > mcamel-minio.yaml
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 mcamel-minio.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade mcamel-minio mcamel/mcamel-minio \
          -n mcamel-system \
          -f ./mcamel-minio.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.8.1
        ```


=== "通过 chart 包升级"

    1. 备份 `--set` 参数。

        在升级版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values mcamel-minio -n mcamel-system -o yaml > mcamel-minio.yaml
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade mcamel-minio . \
          -n mcamel-system \
          -f ./mcamel-minio.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
