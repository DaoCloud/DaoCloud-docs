# Install Virtual Machine Module

This page explains how to install the virtual machine module.

!!! info

    The term `virtnest` appearing in the following commands or scripts is the internal development code name for the global management module.

## Configure Helm Repo

Helm-charts repository address: <https://release.daocloud.io/harbor/projects/10/helm-charts/virtnest/versions>

```shell
helm repo add virtnest-release https://release.daocloud.io/chartrepo/virtnest
helm repo update virtnest-release
```

If you want to experience the latest development version of virtnest, then please add the following repository address (the development version of virtnest is extremely unstable)

```shell
helm repo add virtnest-release-ci https://release-ci.daocloud.io/chartrepo/virtnest
helm repo update virtnest-release-ci
```

## Choose a Version that You Want to Install

It is recommended to install the latest version.

```shell
[root@master ~]# helm search repo virtnest-release/virtnest --versions
NAME                   CHART VERSION  APP VERSION  DESCRIPTION
virtnest-release/virtnest  0.9.0          v0.9.0       A Helm chart for virtnest
```

## Create a Namespace

```shell
kubectl create namespace virtnest-system
```

## Perform Installation Steps

```shell
helm install virtnest virtnest-release/virtnest -n virtnest-system --version 0.9.0
```

## Upgrade

### Update the virtnest Helm Repository

```shell
helm repo update virtnest-release
```

### Back up the --set Parameters

> Before upgrading the virtnest version, we recommend executing the following command to backup the --set parameters of the previous version

```shell
helm get values virtnest -n virtnest-system -o yaml > bak.yaml
```

### Perform Helm Upgrade

```shell
helm upgrade virtnest virtnest-release/virtnest \
-n virtnest-system \
-f ./bak.yaml \
--version 0.9.3
```

## Uninstall

```shell
helm delete virtnest -n virtnest-system
```
