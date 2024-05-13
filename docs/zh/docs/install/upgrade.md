# 升级 DCE 5.0 组件

DCE 5.0 组件的升级包含升级 DCE 5.0 产品功能模块、升级 DCE 5.0 基础设施模块

其中 DCE 5.0 由容器管理、全局管理、可观测性等十几个子模块构成，主要指 [manifest.yaml](commercial/manifest.md) 文件中的 `components` 部分。

DCE 5.0 基础设施模块的组件特指 [manifest.yaml](commercial/manifest.md) 文件中的 `infrastructures` 部分。

## 前提条件

- 您需要有一个 DCE 5.0 的集群环境，参阅[离线化部署商业版](commercial/start-install.md)
- 请确保您的火种机器还存活
- 请确认您想要升级的版本，参阅[版本发布说明](release-notes.md)

## 离线升级操作步骤

本次操作步骤演示如何从 v0.8.0 升级到 v0.9.0。目前升级到从低版本升级到 v0.9.0 时，需要同时升级 DCE 5.0 产品功能模块和 DCE 5.0 基础设施模块，从而使用到 `istio-gateway` 组件的高可用功能。

### 第 1 步：下载 v0.9.0 离线包

可以在[下载中心](../download/index.md)下载最新版本。

| CPU 架构 | 版本   | 下载地址                                                     |
| :------- | :----- | :----------------------------------------------------------- |
| AMD64    | v0.9.0 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-amd64.tar |
| ARM64    | v0.9.0 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-arm64.tar |

下载完毕后解压离线包，以 AMD64 架构离线包为例：

```bash
tar -xvf offline-v0.9.0-amd64.tar
```

### 第 2 步：配置集群配置文件 clusterConfig.yaml

!!! note

    - 需要确保[集群配置文件](commercial/cluster-config.md) 与安装时使用的参数一致
    - 目前仅对 imagesAndCharts 的 builtin 方式进行了测试

文件在解压后的离线包 `offline/sample` 目录下，参考配置文件如下：

```yaml title="clusterConfig.yaml"
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
spec:
  clusterName: my-cluster
  loadBalancer:
    type: metallb 
    istioGatewayVip: 172.30.**.**/32 
    insightVip: 172.30.**.**/32      
  masterNodes:
    - nodeName: "g-master1" 
      ip: 172.30.**.**
      ansibleUser: "root"
      ansiblePass: "*****"
  workerNodes:
    - nodeName: "g-worker1"
      ip: 172.30.**.**
      ansibleUser: "root"
      ansiblePass: "*****"
    - nodeName: "g-worker2"
      ip: 172.30.**.**
      ansibleUser: "root"
      ansiblePass: "*****"
 
  fullPackagePath: "/home/installer/offline"
  osRepos:
    type: builtin
    isoPath: "/home/installer/CentOS-7-x86_64-DVD-2207-02.iso"
    osPackagePath: "/home/installer/os-pkgs-centos7-v0.4.4.tar.gz"
  imagesAndCharts:
    type: builtin
 
  addonPackage:
  binaries:
    type: builtin  # (1)
```

1. official-service(if omit or empty), builtin or external

### 第 3 步：配置 manifest.yaml（可选）

文件在解压后的离线包 `offline/sample` 目录下。

#### DCE 5.0 产品功能模块配置

DCE 5.0 产品功能模块的组件特指 [manifest.yaml](commercial/manifest.md) 文件中的 `components` 部分。
如果有些产品组件不需要升级，可以在对应组件下选择关闭。如果采用以下配置，更新时将不会对 Kpanda（容器管理）进行升级：

```yaml title="manifest.yaml"
  components:
    kpanda:
      enable: false
      helmVersion: 0.17.0
      variables:
```

#### DCE 5.0 基础设施模块配置

DCE 5.0 基础设施模块的组件特指 [manifest.yaml](commercial/manifest.md) 文件中的 `infrastructures` 部分，如下配置就是基础设施中的 `hwameiStor` 组件：

```yaml title="manifest.yaml"
  infrastructures:
    hwameiStor:
      enable: true
      version: v0.10.4
      policy: drbd-disabled
```

!!! note

    目前仅支持对当前环境中已经安装的产品组件进行升级，不存在的组件将会跳过升级步骤。

### 第 4 步：开始升级

#### DCE 5.0 产品功能模块升级

执行升级命令

```bash
./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml --upgrade gproduct
```

#### DCE 5.0 基础设施模块升级

执行升级命令

```bash
./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml --upgrade infrastructure
```

#### DCE 5.0 升级

执行升级命令

```bash
./offline/dce5-installer cluster-create --help

provision DaoCloud 5.0 clusters and install software stacks

Usage:
  dce5-installer cluster-create [flags]

Flags:
  -c, --clusterConfig string   The cluster config file
  -y, --dry-run                Dump installer scripts only
  -h, --help                   help for cluster-create
  -m, --manifest string        manifest BOM file
      --max-tasks int          Controls the maximum number of concurrent tasks. Must be positive number. (default 4)
      --multi-arch             Whether to use the multi-arch image import mode.
      --serial                 Disable concurrent run
  -u, --upgrade string         Choose the component which you want to upgrade, for example  tinder,cluster,infrastructure,hwameistor,middleware,gproduct,addon .

Global Flags:
  -s, --customized-script string   (Optional)Your override script path
  -d, --debug                      Enable debug output
  -l, --logfile string             The installation log to be dump (default "/var/log/dce5.log")
  -z, --minimized-replicas         Whether to minimized all components replicas as small as possible.
  -j, --steps string               (Optional)Debug Only, to specific a range of steps to be executed(format, 2+;  1,2,4; 3 ) (default "1+")
  -t, --tinder-host-ip string      (Optional)The desired host IP on tinder node if it is not on default route.

./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml --upgrade infrastructure,gproduct
```

升级参数说明：

- `install-app` 或 `cluster-create`，代表安装 DCE 5.0 的安装模式类型。如果最初的环境是通过 `cluster-create` 来安装的，则升级时也采用这个命令
- `--upgrade` 可以简写为 `-u`，目前支持升级：
    - DCE 5.0 产品功能模块（gproduct）
    - 基础设施模块（infrastructure）
    - 本地存储模块（hwameistor）
    - 中间件模块（middleware）
- 如果需要一起升级产品功能模块和基础设施模块，则可以指定参数 `--upgrade infrastructure,gproduct`
- 安装器 v0.12.0 支持了 `--multi-arch` 参数，主要是用户在当前环境存在多架构镜像时，进行升级过程中添加该参数可以避免覆盖原有的多架构镜像。

### 第 5 步：安装成功提示

![upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/upgrade.png)
