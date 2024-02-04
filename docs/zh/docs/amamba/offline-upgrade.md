# 离线升级

应用工作台支持离线升级。您需要先从[安装包](../download/modules/amamba.md)中加载镜像，然后执行相应命令进行升级。

```shell
tar -vxf amamba_x.y.z_amd64.tar
```

解压完成后会得到一个压缩包: amamba_x.y.z.bundle.tar

## 从安装包中加载镜像

支持通过两种方式加载镜像。

### 通过 charts-syncer 同步镜像

如果环境中存在镜像仓库，建议通过 charts-syncer 将镜像同步到镜像仓库，更加高效便捷。

1. 使用如下内容创建 `load-image.yaml` 作为 charts-syncer 的配置文件

    `load-image.yaml` 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并参考如下说明修改各项配置。有关 charts-syncer 配置文件的详细解释，可参考其[官方文档](https://github.com/bitnami-labs/charts-syncer)。

    === "已安装 HARBOR chart repo"

        若当前环境已安装 HARBOR chart repo，charts-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: amamba-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerPrefixRegistry: 10.16.10.111 # 需更改为你的镜像仓库 url
          repo:
            kind: HARBOR # 也可以是任何其他支持的 Helm Chart 仓库类别
            url: http://10.16.10.111/chartrepo/release.daocloud.io # 需更改为 chart repo project url
            auth:
              username: "admin" # 你的镜像仓库用户名
              password: "Harbor12345" # 你的镜像仓库密码
          containers:
            auth:
              username: "admin" # 你的镜像仓库用户名
              password: "Harbor12345" # 你的镜像仓库密码
        ```

    === "已安装 CHARTMUSEUM chart repo"

        若当前环境已安装 CHARTMUSEUM chart repo，charts-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: amamba-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
          containerPrefixRegistry: 10.16.10.111 # 需更改为你的镜像仓库 url
          repo:
            kind: CHARTMUSEUM # 也可以是任何其他支持的 Helm Chart 仓库类别
            url: http://10.16.10.111 # 需更改为 chart repo url
            auth:
              username: "rootuser" # 你的镜像仓库用户名, 如果 chartmuseum 没有开启登录验证，就不需要填写 auth
              password: "rootpass123" # 你的镜像仓库密码
          containers:
            auth:
              username: "rootuser" # 你的镜像仓库用户名
              password: "rootpass123" # 你的镜像仓库密码
        ```

    === "未安装 chart repo"

        若当前环境未安装 chart repo，charts-syncer 也支持将 chart 导出为 `tgz` 文件并存放在指定路径。

        ```yaml
        source:
          intermediateBundlesPath: amamba-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/amamba # (3)
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

2. 将 amamba_x.y.z.bundle.tar 放到 amamba-offline 文件夹下。

3. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### 通过 docker 或 containerd 直接加载镜像

1. 解压 `tar` 压缩包。

    ```shell
    tar -vxf amamba_x.y.z.bundle.tar
    ```

    解压成功后会得到 3 个文件：

    - hints.yaml
    - images.tar
    - original-chart

2. 执行如下命令从本地加载镜像到 Docker 或 Containerd。

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "Containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    - 需要在每个节点上都通过 Docker 或 Containerd 加载镜像。
    - 加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 升级

=== "通过 helm repo 升级"

    1. 检查应用工作台 helm 仓库是否存在。

        ```shell
        helm repo list | grep amamba
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    2. 添加应用工作台的 helm 仓库。

        ```shell
        helm repo add amamba-release http://{harbor url}/chartrepo/{project}
        ```

    3. 更新应用工作台的 helm 仓库。

        ```shell
        helm repo update amamba-release # (1)
        ```

        1. helm 版本过低会导致失败，若失败，请尝试执行 helm update repo

    4. 选择您想安装的应用工作台版本（建议安装最新版本）。

        ```shell
        helm search repo amamba-release/amamba --versions
        ```

        ```text
        NAME                    CHART VERSION  APP VERSION  DESCRIPTION
        amamba-release/amamba	 0.24.0         0.24.0       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.23.0         0.23.0       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.22.1         0.22.1       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.22.0         0.22.0       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.21.2         0.21.2       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.21.1         0.21.1       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.21.0         0.21.0       Amamba is the entrypoint to DCE5.0, provides de...
        ...
        ```

    5. 备份 `--set` 参数。

        在升级应用工作台版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values amamba -n amamba-system -o yaml > bak.yaml
        ```

    6. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade amamba amamba-release/amamba \
        -n amamba-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry \
        --version 0.24.0
        ```

=== "通过 chart 包升级"

    1. 准备好 `original-chart`(解压 amamba_x.y.z.bundle.tar 得到)。

    2. 备份 `--set` 参数。

        在升级应用工作台版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values amamba -n amamba-system -o yaml > bak.yaml
        ```

    3. 执行 `helm upgrade`。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade amamba original-chart \
        -n amamba-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```