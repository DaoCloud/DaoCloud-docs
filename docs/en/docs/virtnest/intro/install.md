# Install the Virtual Machine Container Module

This page explains how to install the Virtual Machine Container module.

!!! info

    The term "virtnest" appearing in the following commands or scripts is the internal development code name for the global management module.

## Configure the virtnest Helm repository

> Helm charts repository: <https://release.daocloud.io/harbor/projects/10/helm-charts/virtnest/versions>

```shell
helm repo add virtnest-release https://release.daocloud.io/chartrepo/virtnest

helm repo update virtnest-release
```

> If you want to experience the latest development version of virtnest, add the following repository address (the development version of virtnest is highly unstable).

```shell
helm repo add virtnest-release-ci https://release-ci.daocloud.io/chartrepo/virtnest

helm repo update virtnest-release-ci
```

## Choose the version of virtnest you want to install

It is recommended to install the latest version.

```shell
helm search repo virtnest-release/virtnest --versions
[root@master~]# helm search repo virtnest-release/virtnest --versions
NAME                   CHART VERSION  APP VERSION  DESCRIPTION
virtnest-release/virtnest  0.9.0          v0.9.0       A Helm chart for virtnest
...
```

## Create namespace

```shell
kubectl create namespace virtnest-system
```

## Install

```shell
helm install virtnest virtnest-release/virtnest -n virtnest-system --version 0.9.0
```

## Upgrade

### Update the virtnest Helm repository

```shell
helm repo update virtnest-release
```

### Back up the --set flag

> Before upgrading the virtnest version, we recommend executing the following command to back up the --set flag of the previous version.

```shell
helm get values virtnest -n virtnest-system -o yaml > bak.yaml
```

### Hhelm upgrade

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
