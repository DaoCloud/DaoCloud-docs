# 离线升级云原生网络模块

DCE 5.0 的各个模块松散耦合，支持独立安装、升级各个模块。此文档适用于通过离线方式升级云原生网络模块 Spidernet。

Spidernet 为云原生网络管理引擎，主要提供 Spidernet、Multus CR、Egress IP 等网络模块功能的管理。

## 从下载的安装包中加载镜像

您需要先从[安装包](../../download/modules/spidernet.md)中获取 Spidernet 的离线包，然后可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 chart-syncer 同步镜像到镜像仓库，该方法更加高效便捷。

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
          intermediateBundlesPath: spidernet-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerRegistry: 10.16.23.145 # 需更改为你的镜像仓库 url
          containerRepository: release.daocloud.io/spidernet # 需更改为你的镜像仓库
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

    === "未添加 Helm repo"

        若当前节点上未添加 helm repo，chart-syncer 也支持将 chart 导出为 tgz 文件，并存放在指定路径。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: spidernet-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/spidernet # (3)
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
  
#### 方式二：使用 Docker 或 containerd 加载镜像

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf spidernet.bundle.tar
    ```
  
    解压成功后会得到 3 个文件：

    - hints.yaml
    - images.tar
    - original-chart

2. 从本地加载镜像到 Docker 或 Containerd。
  
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

    1. 检查网络服务引擎的 helm 仓库是否存在。

        ```shell
        helm repo list | grep spidernet
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    2. 添加网络服务引擎的 helm 仓库。

        ```shell
        helm repo add spidernet-release http://{harbor url}/chartrepo/{project}
        ```

    3. 更新网络服务引擎的 helm 仓库。

        ```shell
        helm repo update spidernet-release # (1)
        ```

    4. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    5. 选择您想安装的网络服务引擎版本（建议安装最新版本）。

        ```shell
        helm search repo spidernet-release/spidernet --versions
        ```

        ```none
        [root@master ~]# helm search repo spidernet-release/spidernet --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        spidernet-release/spidernet  0.8.0          v0.8.0       A Helm chart for spidernet
        ...
        ```

    6. 备份 `--set` 参数。

        在升级网络服务引擎版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values spidernet -n spidernet-system -o yaml > bak.yaml
        ```

    7. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `spidernet.image.registry` 和 `ui.image.registry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade spidernet spidernet-release/spidernet \
        -n spidernet-system \
        -f ./bak.yaml \
        --set spidernet.image.registry=$imageRegistry \
        --set ui.image.registry=$imageRegistry \
        --version 0.8.0
        ```

=== "通过 chart 包升级"

    1. 备份 `--set` 参数。

        在升级网络服务引擎版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values spidernet -n spidernet-system -o yaml > bak.yaml
        ```

    2. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `spidernet.image.registry` 和 `ui.image.registry`  为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade spidernet . \
        -n spidernet-system \
        -f ./bak.yaml \
        --set spidernet.image.registry=$imageRegistry \
        --set ui.image.registry=$imageRegistry \
        ```
