# 离线升级全局管理模块

本页说明[下载全局管理模块](../../download/modules/ghippo.md)后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `ghippo` 字样是全局管理模块的内部开发代号。

## 从安装包中加载镜像

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择chart-syncer同步镜像到镜像仓库，该方法更加高效便捷。

### chart-syncer 同步镜像到镜像仓库

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并修改相关配置。

    === "已安装 chart repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: ghippo-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerRegistry: 10.16.10.111 # 需更改为你的镜像仓库 url
          containerRepository: release.daocloud.io/ghippo # 需更改为你的镜像仓库
          repo:
            kind: HARBOR # 也可以是任何其他支持的 Helm Chart 仓库类别
            url: http://10.16.10.111/chartrepo/release.daocloud.io # 需更改为 chart repo url
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

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: ghippo-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/ghippo # (3)
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
    tar xvf ghippo.bundle.tar
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
        ctr -n k8s.io image import images.tar
        ```

!!! note

    每个 node 都需要做 Docker 或 containerd 加载镜像操作，
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 升级

有两种升级方式。您可以根据前置操作，选择对应的升级方案：

!!! note  

    当从 v0.11.x (或更低版本) 升级到 v0.12.0 (或更高版本) 时，需要将 __bak.yaml__ 中所有 keycloak key 修改为 __keycloakx__ 。  

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
          dbname: ghippo
          password: passowrd
          user: ghippo
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
        ghippo:
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

    1. 检查全局管理 helm 仓库是否存在。

        ```shell
        helm repo list | grep ghippo
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加全局管理的 helm 仓库。

        ```shell
        helm repo add ghippo http://{harbor url}/chartrepo/{project}
        ```

    1. 更新全局管理的 helm 仓库。

        ```shell
        helm repo update ghippo # (1)
        ```

        1. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    1. 选择您想安装的全局管理版本（建议安装最新版本）。

        ```shell
        helm search repo ghippo/ghippo --versions
        ```

        ```none
        [root@master ~]# helm search repo ghippo/ghippo --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        ghippo/ghippo  0.9.0          v0.9.0       A Helm chart for GHippo
        ...
        ```

    1. 备份 __--set__ 参数。

        在升级全局管理版本之前，建议您执行如下命令，备份老版本的 __--set__ 参数。

        ```shell
        helm get values ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. 更新 ghippo crds

        ```shell
        helm pull ghippo/ghippo --version 0.9.0 && tar -zxf ghippo-0.9.0.tgz
        kubectl apply -f ghippo/crds
        ```

    1. 执行 __helm upgrade__ 。

        升级前建议您覆盖 bak.yaml 中的 __global.imageRegistry__ 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade ghippo ghippo/ghippo \
          -n ghippo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.9.0
        ```

=== "通过 chart 包升级"

    1. 备份 __--set__ 参数。

        在升级全局管理版本之前，建议您执行如下命令，备份老版本的 __--set__ 参数。

        ```shell
        helm get values ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. 更新 ghippo crds

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 __helm upgrade__ 。

        升级前建议您覆盖 bak.yaml 中的 __global.imageRegistry__ 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade ghippo . \
          -n ghippo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
