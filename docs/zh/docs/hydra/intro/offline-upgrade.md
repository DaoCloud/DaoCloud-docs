# 离线升级大模型服务平台

本页说明[下载大模型服务平台模块](https://docs.daocloud.io/download/modules/hydra/)后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 __hydra__ 字样是大模型服务平台模块的内部开发代号。

## 解压下载的包得到 bundle 包

```shell
tar -xvf hydra_v0.9.0_amd64.tar
```

解压后可得到 hydra、hydra-agent、web-search-agent 这 3 个 bundle.tar 包。

```shell
$ ll hydra_v0.9.0_amd64
-rw-r--r--@ 1 nicole  staff    72M Sep 12 12:05 hydra_v0.9.0.bundle.tar
-rw-r--r--@ 1 nicole  staff   502M Sep 12 12:05 hydra-agent_v0.9.0.bundle.tar
-rw-r--r--@ 1 nicole  staff   105M Sep 12 12:05 web-search-agent_v0.9.0.bundle.tar
```

## 从安装包中加载镜像

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 __chart-syncer__ 同步镜像到镜像仓库，该方法更加高效便捷。

### chart-syncer 同步镜像到镜像仓库

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并修改相关配置。

    === "已安装 chart repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: hydra-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/hydra # (3)!
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
          intermediateBundlesPath: hydra-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/hydra # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        2. 需更改为你的镜像仓库 url
        3. 需更改为你的镜像仓库
        4. chart 本地路径
        5. 你的镜像仓库用户名
        6. 你的镜像仓库密码

1. 执行同步镜像命令。

    ```bash
    charts-syncer sync --config load-image.yaml
    ```

### Docker 或 containerd 直接加载

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```bash
    tar xvf hydra.bundle.tar
    ```

    解压成功后会得到 3 个文件：

    - hints.yaml
    - images.tar
    - original-chart

2. 从本地加载镜像到 Docker 或 containerd。

    === "Docker"

        ```bash
        docker load -i images.tar
        ```

    === "containerd"

        ```bash
        ctr -n k8s.io image import images.tar
        ```

!!! note

    每个 node 都需要做 Docker 或 containerd 加载镜像操作，
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 升级

升级前注意预先备份网格的配置文件，也就是 `--set` 参数，避免升级时配置丢失导致的问题。

### 检查本地是否存在 hydra-release 仓库

```bash
helm repo list | grep hydra-release
```

若返回结果为空或如下提示，则进行下一步；反之则跳过下一步，直接进行更新即可。

```none
Error: no repositories to show
```

### 添加 Helm 仓库

```bash
helm repo add hydra-release http://{harbor_url}/chartrepo/{project}
```

更新大模型服务平台的 Helm 仓库。

```bash
helm repo update hydra-release
```

选择您想安装的大模型服务平台版本（建议安装最新版本）。

```bash
# 更新 hydra-release 仓库内的镜像版本
helm update repo

# 获取最新大模型服务平台的版本
helm search repo hydra-release/hydra --versions

# 工作集群大模型服务平台组件
helm search repo hydra-release/hydra-agent --versions

# 工作集群可选支持网页搜索组件
helm search repo hydra-release/web-search-agent --versions
```

```output
NAME                     	CHART VERSION	APP VERSION	DESCRIPTION
hydra-release/hydra      	v0.9.0       	v0.9.0     	A Helm chart for Kubernetes
...
```

### 备份 `--set` 参数

在升级大模型服务平台版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

```bash
helm get values hydra -n hydra-system -o yaml > bak.yaml
```

### 执行 `helm upgrade`

升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

```bash
export imageRegistry={YOUR_IMAGE_REGISTRY}
```

```bash
helm upgrade hydra hydra-release/hydra \
    -n hydra-system \
    -f ./bak.yaml \
    --set global.imageRegistry=$imageRegistry \
    --version v0.9.0
```
