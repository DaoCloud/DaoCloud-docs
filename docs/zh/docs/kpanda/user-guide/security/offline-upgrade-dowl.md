# 离线升级安全管理模块

本页说明[下载安全管理模块](../../../download/modules/dowl.md)后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 __dowl__ 字样是安全管理模块的内部开发代号。

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
          intermediateBundlesPath: dowl # 节点上执行 load-image.yaml 文件的路径。
        target:
          containerRegistry: 10.16.10.111 # 镜像仓库地址
          containerRepository: release.daocloud.io/dowl # 镜像仓库路径
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
          intermediateBundlesPath: dowl # 节点上执行 load-image.yaml 文件的路径。
        target:
          containerRegistry: 10.16.10.111 # 镜像仓库 url
          containerRepository: release.daocloud.io/dowl # 镜像仓库路径
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

1. 解压第一层压缩包。

    ```shell
    tar xvf dowl.amd64.tar
    ```

    解压成功后会得到 1 个新的压缩包：

    - dowl.bundle.tar

2. 解压新的压缩包。

    ```shell
    tar xvf dowl.bundle.tar
    ```

    解压成功后会得到 3 个文件：

    - hints.yaml
    - images.tar
    - original-chart

3. 从本地加载镜像到 Docker 或 containerd。

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

=== "通过 helm repo 升级"

    1. 检查安全管理 helm 仓库是否存在。

        ```shell
        helm repo list | grep dowl
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加安全管理的 helm 仓库。

        ```shell
        helm repo add dowl http://{harbor url}/chartrepo/{project}
        ```

    1. 更新安全管理的 helm 仓库。

        ```shell
        helm repo update dowl
        ```

        > helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    1. 选择您想安装的安全管理版本（建议安装最新版本）。

        ```shell
        helm search repo dowl/dowl --versions
        ```

        ```none
        [root@master ~]# helm search repo dowl/dowl --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        dowl/dowl  0.4.0          v0.4.0       A Helm chart for dowl
        ...
        ```

    1. 备份 __--set__ 参数。

        在升级安全管理版本之前，建议您执行如下命令，备份老版本的 __--set__ 参数。

        ```shell
        helm get values dowl -n dowl-system -o yaml > bak.yaml
        ```

    1. 更新 dowl crds (需要先解压并进入 original-chart 文件)

        ```shell
        helm pull dowl/dowl --version 0.4.0 && tar -zxf dowl-0.4.0.tgz
        kubectl apply -f dowl/crds
        ```

    1. 执行 __helm upgrade__ 。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade dowl dowl/dowl \
          -n dowl-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.4.0
        ```

=== "通过 chart 包升级"

    1. 备份 __--set__ 参数。

        在升级安全管理版本之前，建议您执行如下命令，备份老版本的 __--set__ 参数。

        ```shell
        helm get values dowl -n dowl-system -o yaml > bak.yaml
        ```

    1. 更新 dowl crds (需要先解压并进入 original-chart 文件)

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 __helm upgrade__ 。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade dowl . \
          -n dowl-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
