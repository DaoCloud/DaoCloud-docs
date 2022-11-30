# 离线升级全局管理模块

本页说明从[下载中心](../../download/dce5.md)下载全局管理模块后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `ghippo` 字样是全局管理模块的内部开发代号。

## 通过 chart-syncer 同步镜像到指定镜像仓库

1. 创建 load-image.yaml，完整 yaml 如下：  

    !!! note  
        
        该 YAML 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并修改相关配置。
    ```yaml
    source:
      intermediateBundlesPath: ghippo-offline # the relative path where your do charts-syncer,but not relative path between this yaml and offline-package
    target:
      containerRegistry: 10.16.10.111 # need change to your image registry url
      containerRepository: release.daocloud.io/ghippo # need change to your image Repository
      repo:
        kind: HARBOR # or as any other supported Helm Chart repository kinds
        url: http://10.16.10.111/chartrepo/release.daocloud.io # need change to your chart repo url
        auth:
          username: "admin" # your image registry username
          password: "Harbor12345" # your image registry password
      containers:
        auth:
          username: "admin" # your image registry username
          password: "Harbor12345" # your image registry password
    ```


1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```
    
## 通过镜像包加载镜像文件

参照以下步骤解压并加载镜像文件。

### 解压

解压 tar 压缩包。

```sh
tar xvf ghippo.bundle.tar
```

解压成功后会得到 3 个文件：

- hints.yaml
- images.tar
- original-chart

### 本地加载镜像到 Docker

从本地将镜像文件加载到 Docker或Container中。

docker:
```sh
docker load -i images.tar
```

Container:
```sh
ctr image import images.tar
```
!!! note

    load完成后需要tag镜像，保持Registry、Repository与安装时一致

## 升级

有两种升级方式：Harbor 或 Docker。您可以任选其一。  
    
!!! note  

    当从 v0.11.x (或更低版本) 升级到 v0.12.0 (或更高版本) 时，需要将步骤2 bak.yaml 中所有 key 为 keycloak 的修改为 keycloakx。  
        
示例：  

```shell
USER-SUPPLIED VALUES:
keycloak:
    ...
```

修改为

```shell
USER-SUPPLIED VALUES:
keycloakx:
    ...
```

### 通过镜像仓库升级

1. 检查全局管理 helm 仓库是否存在。

    ```
    helm repo list | grep ghippo
    ```
    
    若返回结果为空或如下提示，则进行第二步配置全局管理的 helm 仓库，反之则跳过第二步，直接进行第三步
    
    ```
    Error: no repositories to show
    ```

1. 添加全局管理的 helm 仓库。

    ```shell
    heml repo add ghippo http://{harbor url}/chartrepo/{project}
    ```
    
1. 更新全局管理的 helm 仓库。

    ```shell
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
    --set global.imageRegistry=temp-registry.daocloud.io
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
