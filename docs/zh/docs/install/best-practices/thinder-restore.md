# 火种机的备份与还原

本文描述的是火种机器中 kind 集群的备份与还原。

## 备份概述

安装器 v0.16.0 支持了对 火种机 的 kind 集群的备份与还原。目前备份以下信息：

1. 两个重要文件：[clusterConfig.yaml](../commercial/cluster-config.md)、[manifest.yaml](../commercial/manifest.md)

    其中 clusterConfig.yaml、manifest.yaml 中的信息存在了 kind 集群 的 configmap 中

    ```shell
    root@my-cluster-installer-control-plane:/# kubectl get -n default cm
    ```
    ```output
    NAME                       DATA   AGE
    clusterconfig-1710711049   1      4h46m
    kube-root-ca.crt           1      4h46m
    manifest-1710711049        1      4h46m
    ```

2. kind 集群的所有数据

    kind 集群的数据都挂载到了宿主机 /home/kind，etcd 的数据挂载到了 /home/kind/etcd，请勿删除该目录下的文件。

    !!! note

        其中挂载目录可以在 clusterConfig.yaml 中的 `spec.tinderKind.resourcesMountPath` 定义，默认是 `/home/kind`。

## 还原

由于上述备份已经默认为用户开启，所以在 kind 集群被意外删除或丢失后，执行安装器命令即可：

```shell
./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/manifest.yaml -j1,2
```
