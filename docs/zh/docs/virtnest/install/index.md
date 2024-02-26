# 安装虚拟机模块

本页说明如何安装虚拟机模块。

!!! info

    下述命令或脚本内出现的 __virtnest__ 字样是全局管理模块的内部开发代号。

## 配置 virtnest helm 仓库

helm-charts 仓库地址：<https://release.daocloud.io/harbor/projects/10/helm-charts/virtnest/versions>

```shell
helm repo add virtnest-release https://release.daocloud.io/chartrepo/virtnest
helm repo update virtnest-release
```

如果您想体验最新开发版的 virtnest，那么请添加如下仓库地址（开发版本的 virtnest 极其不稳定）

```shell
helm repo add virtnest-release-ci https://release-ci.daocloud.io/chartrepo/virtnest
helm repo update virtnest-release-ci
```

## 选择您想安装的 virtnest 版本

建议安装最新版本。

```shell
[root@master ~]# helm search repo virtnest-release/virtnest --versions
NAME                   CHART VERSION  APP VERSION  DESCRIPTION
virtnest-release/virtnest  0.6.0          v0.6.0       A Helm chart for virtnest
```

## 创建 namespace

```shell
kubectl create namespace virtnest-system
```

## 执行安装步骤

```shell
helm install virtnest virtnest-release/virtnest -n virtnest-system --version 0.6.0
```

## 升级

### 更新 virtnest helm 仓库

```shell
helm repo update virtnest-release
```

### 备份 --set 参数

> 在升级 virtnest 版本之前，我们建议您执行如下命令，备份上一个版本的 --set 参数

```shell
helm get values virtnest -n virtnest-system -o yaml > bak.yaml
```

### 执行 helm upgrade

```shell
helm upgrade virtnest virtnest-release/virtnest \
    -n virtnest-system \
    -f ./bak.yaml \
    --version 0.6.0
```

## 卸载

```shell
helm delete virtnest -n virtnest-system
```
