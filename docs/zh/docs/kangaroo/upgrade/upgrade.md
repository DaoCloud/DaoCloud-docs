# 离线升级镜像仓库模块

本页说明从[下载中心](../../download/index.md)下载镜像仓库模块后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `kangaroo` 字样是镜像仓库模块的内部开发代号。

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
          intermediateBundlesPath: kangaroo-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/kangaroo # (3)
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
          intermediateBundlesPath: kangaroo-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/kangaroo # (3)
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
    tar xvf kangaroo.bundle.tar
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

=== "通过 helm repo 升级"

    1. 检查全局管理 helm 仓库是否存在。

        ```shell
        helm repo list | grep kangaroo
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加全局管理的 helm 仓库。

        ```shell
        heml repo add kangaroo http://{harbor url}/chartrepo/{project}
        ```

    1. 更新全局管理的 helm 仓库。

        ```shell
        helm repo update kangaroo # (1)
        ```

        1. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    1. 选择您想安装的全局管理版本（建议安装最新版本）。

        ```shell
        helm search repo kangaroo/kangaroo --versions
        ```

        ```none
        [root@master ~]# helm search repo kangaroo/kangaroo --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kangaroo/kangaroo  0.9.0          v0.9.0       A Helm chart for Kangaroo
        ...
        ```

    1. 备份 `--set` 参数。

        在升级全局管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kangaroo -n kangaroo-system -o yaml > bak.yaml
        ```

    1. 查看版本更新记录，如果CRD有更新，更新 kangaroo crds

        ```shell
        helm pull kangaroo/kangaroo --version 0.9.0 && tar -zxf kangaroo-0.9.0.tgz
        kubectl apply -f kangaroo/crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kangaroo kangaroo/kangaroo \
          -n kangaroo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
          --version 0.9.0
        ```

=== "通过 chart 包升级"

    1. 备份 `--set` 参数。

        在升级全局管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kangaroo -n kangaroo-system -o yaml > bak.yaml
        ```

    1. 查看版本更新记录，如果CRD有更新，更新 kangaroo crds

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kangaroo . \
          -n kangaroo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
