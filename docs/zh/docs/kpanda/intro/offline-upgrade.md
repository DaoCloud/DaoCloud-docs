# 离线升级容器管理模块

本页说明从[下载中心](../../download/index.md)下载容器管理模块后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `kpanda` 字样是容器管理模块的内部开发代号。

## 从下载的安装包中加载镜像

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 chart-syncer 同步镜像到镜像仓库，该方法更加高效便捷。

#### 方式一：使用 chart-syncer 同步镜像

使用 chart-syncer 可以将您下载的安装包中的 chart 及其依赖的镜像包上传至安装器部署 DCE 时使用的镜像仓库和 helm 仓库。

首先找到一台能够连接镜像仓库和 helm 仓库的节点（如火种节点），在节点上创建 load-image.yaml 配置文件，填入镜像仓库和 helm 仓库等配置信息。

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。
    === "已添加 Helm repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kpanda # 节点上执行 load-image.yaml 文件的路径。
        target:
          containerRegistry: 10.16.10.111 # 镜像仓库地址
          containerRepository: release.daocloud.io/kpanda # 镜像仓库路径
          repo:
            kind: HARBOR # Helm Chart 仓库类别
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Helm 仓库地址
            auth:
            username: "admin" # 镜像仓库用户名
            password: "Harbor12345" # 镜像仓库密码
          containers:
            auth:
              username: "admin" # Helm 仓库用户名
              password: "Harbor12345" # Helm 仓库密码
        ```

    === "未添加 Helm repo"

        若当前节点上未添加 helm repo，chart-syncer 也支持将 chart 导出为 tgz 文件，并存放在指定路径。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kpanda # 节点上执行 load-image.yaml 文件的路径。
        target:
          containerRegistry: 10.16.10.111 # 镜像仓库 url
          containerRepository: release.daocloud.io/kpadna # 镜像仓库路径
          repo:
            kind: LOCAL
            path: ./local-repo # chart 本地路径
          containers:
            auth:
              username: "admin" # 镜像仓库用户名
              password: "Harbor12345" # 镜像仓库密码
        ```

1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### 方式二：使用 Docker 或 containerd 加载镜像

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf kpadna.bundle.tar
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

    每个 node 都需要做 Docker 或 containerd 加载镜像操作，
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 升级

有两种升级方式。您可以根据前置操作，选择对应的升级方案：

!!! note  

    当从 v0.11.x (或更低版本) 升级到 v0.12.0 (或更高版本) 时，需要将 `bak.yaml` 中所有 keycloak key 修改为 `keycloakx`。  

    这个 key 的修改示例：  

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    keycloak:
        ...
    ```

    修改为：

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    keycloakx:
        ...
    ```

!!! note  

    当从 v0.15.x (或更低版本) 升级到 v0.16.0 (或更高版本) 时，需要修改数据库连接参数。  

    数据库连接参数的修改示例：

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      database:
        host: 127.0.0.1
        port: 3306
        apiserver:
          dbname: kpanda
          password: passowrd
          user: kpanda
        keycloakx:
          dbname: keycloak
          password: passowrd
          user: keycloak
      auditDatabase:
        auditserver:
          dbname: audit
          password: passowrd
          user: audit
        host: 127.0.0.1
        port: 3306
    ```

    修改为：

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      storage:
        kpanda:
        - driver: mysql
          accessType: readwrite
          dsn: {global.database.apiserver.user}:{global.database.apiserver.password}@tcp({global.database.host}:{global.database.port})/{global.database.apiserver.dbname}?charset=utf8mb4&multiStatements=true&parseTime=true
        audit:
        - driver: mysql
          accessType: readwrite
          dsn: {global.auditDatabase.auditserver.user}:{global.auditDatabase.auditserver.password}@tcp({global.auditDatabase.host}:{global.auditDatabase.port})/{global.auditDatabase.auditserver.dbname}?charset=utf8mb4&multiStatements=true&parseTime=true
        keycloak:
        - driver: mysql
          accessType: readwrite
          dsn: {global.database.keycloakx.user}:{global.database.keycloakx.password}@tcp({global.database.host}:{global.database.port})/{global.database.keycloakx.dbname}?charset=utf8mb4
    ```

=== "通过 helm repo 升级"

    1. 检查容器管理 helm 仓库是否存在。

        ```shell
        helm repo list | grep kpanda
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加容器管理的 helm 仓库。

        ```shell
        heml repo add kpanda http://{harbor url}/chartrepo/{project}
        ```

    1. 更新容器管理的 helm 仓库。

        ```shell
        helm repo update kpadna # (1)
        ```

        1. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    1. 选择您想安装的容器管理版本（建议安装最新版本）。

        ```shell
        helm search repo kpadna/kpadna --versions
        ```

        ```none
        [root@master ~]# helm search repo kpadna/kpadna --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kpadna/kpadna  0.9.0          v0.9.0       A Helm chart for kpadna
        ...
        ```

    1. 备份 `--set` 参数。

        在升级容器管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kpadna -n kpadna-system -o yaml > bak.yaml
        ```

    1. 更新 kpadna crds

        ```shell
        helm pull kpadna/kpadna --version 0.10.0 && tar -zxf kpadna-0.10.0.tgz
        kubectl apply -f kpadna/crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kpadna kpadna/kpadna \
          -n kpadna-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.9.0
        ```

=== "通过 chart 包升级"

    1. 备份 `--set` 参数。

        在升级容器管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kpadna -n kpadna-system -o yaml > bak.yaml
        ```

    1. 更新 kpadna crds

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kpadna . \
          -n kpadna-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
