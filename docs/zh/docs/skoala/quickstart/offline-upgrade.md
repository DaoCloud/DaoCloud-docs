# 离线升级微服务引擎

DCE 5.0 的各个模块松散耦合，支持独立安装、升级各个模块。此文档适用于通过离线方式安装微服务引擎之后进行的升级。

## 同步镜像

将镜像下载到本地节点之后，需要通过 [chart-syncer](https://github.com/bitnami-labs/charts-syncer) 或容器运行时将最新版镜像同步到您的镜像仓库。推荐使用 chart-syncer 同步镜像，因为该方法更加高效便捷。

### chart-syncer 同步镜像

1. 使用如下内容创建 `load-image.yaml` 作为 chart-syncer 的配置文件

    `load-image.yaml` 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并参考如下说明修改各项配置。有关 chart-syncer 配置文件的详细解释，可参考其[官方文档](https://github.com/bitnami-labs/charts-syncer)。

    === "已安装 chart repo"

        若当前环境已安装 chart repo，则可以使用如下配置直接同步镜像。

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

        若当前环境未安装 chart repo，chart-syncer 也支持将 chart 导出为 `tgz` 文件并存放在指定路径。

        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/skoala # (3)
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

2. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Docker/containerd 同步镜像

1. 解压 `tar` 压缩包。

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
        ctr -n k8s.io image import images.tar
        ```

!!! note

    - 需要在每个节点上都通过 Docker 或 containerd 加载镜像。
    - 加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 开始升级

镜像同步完成之后，就可以开始升级微服务引擎了。

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
        helm repo add skoala-release http://{harbor url}/chartrepo/{project}
        ```

    3. 更新微服务引擎的 helm 仓库。

        ```shell
        helm repo update skoala-release # (1)
        ```

        1. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    4. 选择您想安装的微服务引擎版本（建议安装最新版本）。

        ```shell
        helm search repo skoala-release/skoala --versions
        ```

        ```text
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
