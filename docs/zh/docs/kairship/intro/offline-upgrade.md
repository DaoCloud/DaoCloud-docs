# 离线升级

多云编排支持离线升级。您需要先从安装包中加载镜像，然后执行相应命令进行升级。

!!! info

    下述命令或脚本内出现的 __kairship__ 字样是多云编排模块的内部开发代号。

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
          intermediateBundlesPath: kairship # 节点上执行 load-image.yaml 文件的路径。
        target:
          containerRegistry: 10.16.10.111 # 镜像仓库地址
          containerRepository: release.daocloud.io/kairship # 镜像仓库路径
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
          intermediateBundlesPath: kairship # 节点上执行 load-image.yaml 文件的路径。
        target:
          containerRegistry: 10.16.10.111 # 镜像仓库 url
          containerRepository: release.daocloud.io/kairship # 镜像仓库路径
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
    tar xvf kairship.bundle.tar
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

    1. 检查多云编排 helm 仓库是否存在。
    
        ```shell
        helm repo list | grep kairship
        ```
    
        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。
    
        ```none
        Error: no repositories to show
        ```
    
    1. 添加多云编排的 helm 仓库。
    
        ```shell
        helm repo add kairship http://{harbor url}/chartrepo/{project}
        ```
    
    1. 更新多云编排的 helm 仓库。
    
        ```shell
        helm repo update kairship
        ```
    
    1. 选择您想安装的多云编排版本（建议安装最新版本）。
    
        ```shell
        helm search repo kairship/kairship --versions
        ```
    
        输出类似于：
        
        ```none
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kairship/kairship  0.20.0          v0.20.0       A Helm chart for kairship
        ...
        ```
    
    1. 备份 `--set` 参数。
    
        在升级多云编排版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。
    
        ```shell
        helm get values kairship -n kairship-system -o yaml > bak.yaml
        ```
    
    1. 更新 kairship crds
    
        ```shell
        helm pull kairship/kairship --version 0.21.0 && tar -zxf kairship-0.21.0.tgz
        kubectl apply -f kairship/crds
        ```
    
    1. 执行 `helm upgrade` 。
    
        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。
    
        ```shell
        export imageRegistry={你的镜像仓库}
        ```
    
        ```shell
        helm upgrade kairship kairship/kairship \
          -n kairship-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.21.0
        ```

=== "通过 chart 包升级"

    1. 备份 `--set` 参数。
    
        在升级多云编排版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。
    
        ```shell
        helm get values kairship -n k pan da-system -o yaml > bak.yaml
        ```
    
    1. 更新 kairship crds
    
        ```shell
        kubectl apply -f ./crds
        ```
    
    1. 执行 `helm upgrade` 。
    
        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。
    
        ```shell
        export imageRegistry={你的镜像仓库}
        ```
    
        ```shell
        helm upgrade kairship . \
          -n kairship-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
