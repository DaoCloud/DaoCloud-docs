# 升级 DCE 5.0 GProduct

GProduct 是 DCE 5.0 所有产品模块的统称。

本文将介绍如何使用 dce5-installer 离线升级 DCE 5.0 GProduct。

## 前提条件

- 您需要有一个 DCE 5.0 的集群环境，参阅[离线化部署全模式](commercial/start-install.md)
- 请确保您的火种机器还存活
- 请确认您想要升级的版本，参阅[版本发布说明](release-notes.md)

## 离线升级操作步骤

本次操作步骤演示如何从 v0.5.0 升级到 v0.6.0。

### 第 1 步：下载 v0.6.0 离线包

可以在[下载中心](https://docs.daocloud.io/download/dce5/)下载最新版本。

| CPU 架构 | 版本   | 下载地址                                                     |
| :------- | :----- | :----------------------------------------------------------- |
| AMD64    | v0.6.0 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-amd64.tar |
| ARM64    | v0.6.0 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-arm64.tar |

下载完毕后解压离线包，以 AMD64 架构离线包为例：

```bash
tar -xvf offline-v0.6.0-amd64.tar
```

### 第 2 步：配置集群配置文件 clusterConfig.yaml

!!! note

    离线安装 DCE 5.0 时，集群配置文件采用的是什么配置，升级时也需要一致。
    
    由于 v0.6.0 版本更新了集群配置文件的结构，[集群配置文件说明](commercial/cluster-config.md)，所以需要保证要与 v0.5.0 用的参数一致，但是结构要与 v0.6.0 的一致。
    
    目前仅对 imagesAndCharts 的 builtin 方式进行了测试。

文件在解压后的离线包 `offline/sample` 目录下，参考配置文件如下：

```yaml
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

### 第 3 步：配置 mainfest.yaml（可选）

文件在解压后的离线包 `offline/sample` 目录下。

如果有些产品组件不需要升级，可以在对应组件下选择关闭，如下配置，更新时将不会对 Kpanda 进行升级。

```yaml
  kpanda:
    enable: false
    helmVersion: 0.16.0
    variables:
```

!!! note

    目前仅支持对当前环境中已经安装的产品组件进行升级，不存在的组件将会跳过升级步骤

### 第 4 步：开始升级

执行升级命令

```bash
./offline/dce5-installer cluster-create -c sample/clusterconfig.yaml -m sample/manifest.yaml --upgrade 4,5,gproduct
```

升级参数说明：

- `install-app` 或 `cluster-create`，代表安装 DCE 5.0 的安装模式类型。如果最初的环境是通过 `cluster-create` 来安装的，则升级时也采用这个命令
- `--upgrade` 可以简写为 `-u`，命令后面需要加执行步骤，目前如果升级 GProduct 需要执行 `4,5,gproduct`，后续我们会进行优化。

安装成功结果：

![upgrade](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/install/images/upgrade.png)
