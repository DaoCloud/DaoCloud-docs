# Helm 应用多架构和升级导入步骤

通常在多架构集群中，也会使用多架构的 Helm 包来部署应用，以解决架构差异带来的部署问题。
本文将介绍如何将单架构 Helm 应用融合为多架构，以及多架构与多架构 Helm 应用的相互融合。

## 导入

### 单架构导入

准备好待导入的离线包 `addon-offline-full-package-${version}-${arch}.tar.gz` ，可从
[下载中心](../../../download/addon/history.md)下载。
把路径填写至 __clusterConfig.yml__ 配置文件，例如：

```yaml
addonPackage:
  path: "/home/addon-offline-full-package-v0.9.0-amd64.tar.gz"
```

然后执行导入命令：

```shell
~/dce5-installer cluster-create -c /home/dce5/sample/clusterConfig.yaml -m /home/dce5/sample/manifest.yaml -d -j13
```

### 多架构融合

准备好待融合的离线包 `addon-offline-full-package-${version}-${arch}.tar.gz` ，可从
[下载中心](../../../download/addon/history.md)下载。

以 addon-offline-full-package-v0.9.0-arm64.tar.gz 为例，执行导入命令：

```shell
~/dce5-installer import -addon -c /home/dce5/sample/clusterConfig.yaml --addon-path=/home/addon-offline-full-package-v0.9.0-arm64.tar.gz
```

## 升级

### 单架构升级

准备好待导入的离线包 `addon-offline-full-package-${version}-${arch}.tar.gz` ，可从[下载中心](../../../download/addon/history.md)下载。

把路径填写至 clusterConfig.yml 配置文件，例如：

```yaml
addonPackage:
  path: "/home/addon-offline-full-package-v0.11.0-amd64.tar.gz"
```

然后执行导入命令：

```shell
~/dce5-installer cluster-create -c /home/dce5/sample/clusterConfig.yaml -m /home/dce5/sample/manifest.yaml -d -j13
```

### 多架构融合

准备好待融合的离线包 `addon-offline-full-package-${version}-${arch}.tar.gz` ，可从[下载中心](../../../download/addon/history.md)下载。

以 addon-offline-full-package-v0.11.0-arm64.tar.gz 为例，执行导入命令：

```shell
~/dce5-installer import -addon -c /home/dce5/sample/clusterConfig.yaml --addon-path=/home/addon-offline-full-package-v0.11.0-arm64.tar.gz
```

## 注意事项

### 磁盘空间

离线包比较大，且过程中需要解压和 load 镜像，需要预留充足的空间，否则可能在过程中报 “no space left” 而中断。

### 失败后重试

如果在多架构融合步骤执行失败，重试前需要清理一下残留：

```shell
rm -rf addon-offline-target-package
```

### 镜像空间

如果融合的离线包中包含了与导入的离线包不一致的镜像空间，可能会在融合过程中因为镜像空间不存在而报错：

![helm](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/multi-arch-helm.png)

解决办法：只需要在融合之前创建好该镜像空间即可，例如上图报错可通过创建镜像空间 localhost 提前避免。

### 架构冲突

升级至低于 0.12.0 版本的 addon 时，由于目标离线包里的 charts-syncer 没有检查镜像存在则不推送功能，因此会在升级的过程中会重新把多架构冲成单架构。例如：在 v0.10 版本将 addon 实现为多架构，此时若升级为 v0.11 版本，则多架构 addon 会被覆盖为单架构；若升级为 0.12.0 及以上版本则仍能够保持多架构。
