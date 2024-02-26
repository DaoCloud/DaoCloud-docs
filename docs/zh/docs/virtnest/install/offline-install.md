# 离线升级

本页说明从[下载中心](../../download/index.md)下载虚拟机模块后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 __virtnest__ 字样是虚拟机模块的内部开发代号。

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
          intermediateBundlesPath: virtnest-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerRegistry: 10.16.10.111 # 需更改为你的镜像仓库 url
          containerRepository: release.daocloud.io/virtnest # 需更改为你的镜像仓库
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
          intermediateBundlesPath: virtnest-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerRegistry: 10.16.10.111 # 需更改为你的镜像仓库 url
          containerRepository: release.daocloud.io/virtnest # 需更改为你的镜像仓库
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

### Docker 或 containerd 直接加载

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf virtnest.bundle.tar
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

    1. 检查虚拟机 helm 仓库是否存在。

        ```shell
        helm repo list | grep virtnest
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加虚拟机的 helm 仓库。

        ```shell
        helm repo add virtnest http://{harbor url}/chartrepo/{project}
        ```

    1. 更新虚拟机的 helm 仓库。

        ```shell
        helm repo update virtnest # (1)
        ```

        1. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    1. 选择您想安装的虚拟机版本（建议安装最新版本）。

        ```shell
        helm search repo virtnest/virtnest --versions
        ```

        ```none
        [root@master ~]# helm search repo virtnest/virtnest --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        virtnest/virtnest  0.2.0          v0.2.0       A Helm chart for virtnest
        ...
        ```

    1. 备份 `--set` 参数。

        在升级虚拟机版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values virtnest -n virtnest-system -o yaml > bak.yaml
        ```

    1. 更新 virtnest crds

        ```shell
        helm pull virtnest/virtnest --version 0.2.0 && tar -zxf virtnest-0.2.0.tgz
        kubectl apply -f virtnest/crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade virtnest virtnest/virtnest \
          -n virtnest-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.2.0
        ```

=== "通过 chart 包升级"

    1. 备份 `--set` 参数。

        在升级虚拟机版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values virtnest -n virtnest-system -o yaml > bak.yaml
        ```

    1. 更新 virtnest crds

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade virtnest . \
          -n virtnest-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
