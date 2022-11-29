# 离线升级全局管理模块

本页说明从[下载中心](../../download/dce5.md)下载全局管理模块后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `ghippo` 字样是全局管理模块的内部开发代号。

## 加载镜像文件

参照以下步骤解压并加载镜像文件。

### 解压

解压 tar 压缩包。

```sh
tar zxvf ghippo.bundle.tar
```

解压成功后会得到 `ghippo.bundle` 文件，其中包含 3 个子文件：

- hints.yaml
- images.tar
- original-chart

### 通过 chart-syncer 同步镜像到指定镜像仓库

1. 首先请确认本地是否安装 chart-syncer。如果已安装，则跳过这一步。

    ```shell
    tmp_dir=$(mktemp -d)

    git clone https://github.com/DaoCloud/charts-syncer.git ${tmp_dir}

    cp ${tmp_dir}/charts-syncer /usr/local/bin/charts-syncer

    chmod +x /usr/local/bin/charts-syncer

    rm -rf ${tmp_dir}
    ```

1. 创建 load-image.yaml，完整 yaml 如下：

    ```yaml
    source:
      intermediateBundlesPath: dist/offline # the relative path where your do charts-syncer,but not relative path between this yaml and offline-package
    target:
      containerRegistry: 10.64.0.156 # need change to your harbor url
      repo:
        kind: HARBOR # or as any other supported Helm Chart repository kinds
        url: http://10.64.0.156/chartrepo/ghippo # need change to your harbor url
        auth:
          username: "admin" # the harbor username
          password: "Harbor12345" # the harbor password
      containers:
        auth:
          username: "admin" # the harbor username
          password: "Harbor12345" # the harbor password
    ```

    !!! note

        该 YAML 文件中的各项参数均为必填项。您需要一个私有的 harbor，并修改相关配置。

1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### 本地加载镜像到 Docker

从本地将镜像文件加载到 Docker。

```sh
cd ghippo.bundle
docker load -i images.tar
```

## 升级

有两种升级方式：Harbor 或 Docker。您可以任选其一。

### 通过 Harbor 升级

1. 配置全局管理的 helm 仓库。

    ```shell
    heml repo add ghippo https://{harbor url}/chartrepo/ghippo
    helm repo update ghippo # helm 版本过低会导致失败，若失败，请尝试执行 helm update repo
    ```

1. 选择您想安装的全局管理版本（🔥 建议安装最新版本）

    ```shell
    helm search repo ghippo/ghippo --versions
    ```

    ```none
    [root@master ~]# helm search repo ghippo/ghippo --versions
    NAME                   CHART VERSION  APP VERSION  DESCRIPTION
    ghippo/ghippo  0.9.0          v0.9.0       A Helm chart for GHippo
    ...
    ```

1. 备份 `--set` 参数

    在升级全局管理版本之前，我们建议您执行如下命令，备份上一个版本的 --set 参数。

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > bak.yaml
    ```

1. 执行 helm upgrade

    ```
    helm upgrade ghippo ghippo/ghippo \
    -n ghippo-system \
    -f ./bak.yaml \
    --version 0.9.0
    ```

### 通过 Docker 升级

1. 备份 `--set` 参数

    在升级全局管理版本之前，我们建议您执行如下命令，备份上一个版本的 --set 参数。

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > bak.yaml
    ```

1. 执行 `helm upgrade`

    ```shell
    cd original-chart

    helm upgrade ghippo . \
    -n ghippo-system \
    -f ./bak.yaml
    ```
