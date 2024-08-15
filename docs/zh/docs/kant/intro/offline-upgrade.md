# 离线升级云边协同模块

本页说明[下载云边协同模块](../../download/modules/kant.md)后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 __kant__ 字样是云边协同模块的内部开发代号。

## 从下载的安装包中加载镜像

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 chart-syncer 同步镜像到镜像仓库，该方法更加高效便捷。

### 使用 chart-syncer 同步镜像

使用 chart-syncer 可以将您下载的安装包中的 Chart 及其依赖的镜像包上传至安装器部署 DCE 时使用的镜像仓库和 Helm 仓库。

首先找到一台能够连接镜像仓库和 Helm 仓库的节点（如火种节点），在节点上创建 load-image.yaml 配置文件，填入镜像仓库和 Helm 仓库等配置信息。

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。

    === "已添加 Helm repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kant # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/kant # (3)!
          repo:
            kind: HARBOR # (4)!
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (5)!
            auth:
            username: "admin" # (6)!
            password: "Harbor12345" # (7)!
          containers:
            auth:
              username: "admin" # (8)!
              password: "Harbor12345" # (9)!
        ```

        1. 使用 chart-syncer 之后 .tar.gz 包所在的路径
        2. 镜像仓库地址
        3. 镜像仓库路径
        4. Helm Chart 仓库类别
        5. Helm 仓库地址
        6. 镜像仓库用户名
        7. 镜像仓库密码
        8. Helm 仓库用户名
        9. Helm 仓库密码

    === "未添加 Helm repo"

        若当前节点上未添加 helm repo，chart-syncer 也支持将 chart 导出为 tgz 文件，并存放在指定路径。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kant # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/kant # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. 使用 chart-syncer 之后 .tar.gz 包所在的路径
        2. 镜像仓库 url
        3. 镜像仓库路径
        4. chart 本地路径
        5. 镜像仓库用户名
        6. 镜像仓库密码

1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### 使用 Docker 或 containerd 加载镜像

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf kant.bundle.tar
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

=== "通过 helm repo 升级"

    1. 检查云边协同 Helm 仓库是否存在。

        ```shell
        helm repo list | grep kant-release
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加云边协同的 Helm 仓库。

        ```shell
        helm repo add kant-release http://{harbor url}/chartrepo/{project}
        ```

    1. 更新云边协同的 Helm 仓库。

        ```shell
        helm repo update kant-release
        ```

    1. 选择您想安装的云边协同版本（建议安装最新版本）。

        ```shell
        helm search repo kant-release/kant --versions
        ```

        输出类似于：
        
        ```none
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kant-release/kant  0.5.0          v0.5.0       A Helm chart for kant
        ...
        ```

    1. 备份 `--set` 参数。

        在升级云边协同版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kant -n kant-system -o yaml > bak.yaml
        ```

    1. 更新 kant crds

        ```shell
        helm pull kant-release/kant --version 0.5.0 && tar -zxf kant-0.5.0.tgz
        kubectl apply -f kant/crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kant-release kant-release/kant \
          -n kant-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.5.0
        ```

=== "通过 Chart 包升级"

    1. 备份 `--set` 参数。

        在升级云边协同版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kant -n kant-system -o yaml > bak.yaml
        ```

    1. 更新 kant crds

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kant-release . \
          -n kant-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
