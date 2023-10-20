# 离线升级运营管理模块

本页说明[下载运营管理模块](../../../download/modules/gmagpie.md)后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `gmagpie` 字样是运营管理模块的内部开发代号。

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
          intermediateBundlesPath: gmagpie-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/gmagpie # (3)
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
          intermediateBundlesPath: gmagpie-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/gmagpie # (3)
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
    tar xvf gmagpie.bundle.tar
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

    每个节点都需要执行 Docker 或 containerd 加载镜像操作，
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 升级

有两种升级方式。您可以根据前置操作，选择对应的升级方案：

!!! note

    当从 v0.1.x（或更低版本）升级到 v0.2.0（或更高版本）时，需要修改数据库连接参数。

    数据库连接参数的修改示例：

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      database:
        host: 127.0.0.1
        port: 3306
        dbname: gmagpie
        password: passowrd
        user: gmagpie

    ```

    修改为：

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      storage:
        gmagpie:
        - driver: mysql
          accessType: readwrite
          dsn: {global.database.apiserver.user}:{global.database.apiserver.password}@tcp({global.database.host}:{global.database.port})/{global.database.apiserver.dbname}?charset=utf8mb4&multiStatements=true&parseTime=true
    ```

=== "通过 helm repo 升级"

    1. 检查运营管理 Helm 仓库是否存在。

        ```shell
        helm repo list | grep gmagpie
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加运营管理的 Helm 仓库。

        ```shell
        heml repo add gmagpie http://{harbor url}/chartrepo/{project}
        ```

    1. 更新运营管理的 Helm 仓库。

        ```shell
        helm repo update gmagpie # (1)
        ```

        1. Helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    1. 选择您想安装的运营管理版本（建议安装最新版本）。

        ```shell
        helm search repo gmagpie/gmagpie --versions
        ```

        ```none
        [root@master ~]# helm search repo gmagpie/gmagpie --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        gmagpie/gmagpie  0.3.0          v0.3.0       A Helm chart for GHippo
        ...
        ```

    1. 备份 `--set` 参数。

        在升级运营管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values gmagpie -n gmagpie-system -o yaml > bak.yaml
        ```

    1. 更新 Gmagpie CRD。

        ```shell
        helm pull gmagpie/gmagpie --version 0.3.0 && tar -zxf gmagpie-0.3.0.tgz
        kubectl apply -f gmagpie/crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade gmagpie gmagpie/gmagpie \
          -n gmagpie-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.3.0
        ```

=== "通过 Chart 包升级"

    1. 备份 `--set` 参数。

        在升级运营管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values gmagpie -n gmagpie-system -o yaml > bak.yaml
        ```

    1. 更新 Gmagpie CRD。

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade gmagpie . \
          -n gmagpie-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
