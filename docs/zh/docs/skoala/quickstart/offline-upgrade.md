# 离线升级微服务引擎模块

本页说明从[下载中心](../../download/dce5.md)下载微服务引擎模块后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `skoala` 字样是微服务引擎模块的内部开发代号。

## 从安装包中加载镜像

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 chart-syncer 同步镜像到镜像仓库，该方法更加高效便捷。

### chart-syncer 同步镜像到镜像仓库

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并修改相关配置。

    === "已安装 chart repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerRegistry: 10.16.23.145 # 需更改为你的镜像仓库 url
          containerRepository: release.daocloud.io/skoala # 需更改为你的镜像仓库
          repo:
            kind: HARBOR # 也可以是任何其他支持的 Helm Chart 仓库类别
            url: http://10.16.23.145/chartrepo/release.daocloud.io # 需更改为 chart repo url
            auth:
            username: "admin" # 你的镜像仓库用户名
            password: "Harbor12345" # 你的镜像仓库密码
          containers:
            auth:
              username: "admin" # 你的镜像仓库用户名
              password: "Harbor12345" # 你的镜像仓库密码
        ```

    === "未安装 chart repo"

        若当前环境未安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件，并存放在指定路径。

        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerRegistry: 10.16.23.145 # 需更改为你的镜像仓库 url
          containerRepository: release.daocloud.io/skoala # 需更改为你的镜像仓库
          repo:
            kind: LOCAL
            path: ./local-repo # chart 本地路径
          containers:
            auth:
              username: "admin" # 你的镜像仓库用户名
              password: "Harbor12345" # 你的镜像仓库密码
        ```

1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### docker 或 containerd 直接加载

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf skoala.bundle.tar
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
    每个node都需要做进行docker或containerd加载镜像操作
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 升级

有两种升级方式。您可以根据前置操作，选择对应的升级方案：

=== "通过 helm repo 升级"

    1. 检查微服务引擎 helm 仓库是否存在。

        ```shell
        helm repo list | grep skoala
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    2. 添加微服务引擎的 helm 仓库。

        ```shell
        heml repo add skoala-release http://{harbor url}/chartrepo/{project}
        ```

    3. 更新微服务引擎的 helm 仓库。

        ```shell
        helm repo update skoala-release # helm 版本过低会导致失败，若失败，请尝试执行 helm update repo
        ```

    4. 选择您想安装的微服务引擎版本（建议安装最新版本）。

        ```shell
        helm search repo skoala-release/skoala --versions
        ```

        ```none
        [root@master ~]# helm search repo skoala-release/skoala --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        skoala-release/skoala  0.14.0          v0.14.0       A Helm chart for Skoala
        ...
        ```

    5. 备份 `--set` 参数。

        在升级微服务引擎版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    6. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade skoala skoala-release/skoala \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        --version 0.14.0
        ```

=== "通过 chart 包升级"

    1. 备份 `--set` 参数。

        在升级微服务引擎版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    2. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade skoala . \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```
