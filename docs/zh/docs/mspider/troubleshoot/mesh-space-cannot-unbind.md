# 网格空间无法正常解绑

## 问题描述

- 网格类型：托管网格
- Istio 版本：0.16.1-mspider

[全局管理](../../ghippo/intro/index.md)的工作空间改变名称后，网格空间无法正常解绑；
同样在全局管理中解除空间绑定后，服务网格依然显示绑定而且无法解绑，网格空间中被全局管理删除的空间无法解除绑定。

![unbind error](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/unbind-error.png)

## 分析

服务网格对工作空间做了缓存，需要清除缓存中的脏数据。

## 解决办法

1. 如果是托管集群，进入对应网格实例所部署的 $ClusterName，找到 mesh-hosted-apiserver

    ```text
    /kpanda/clusters/$ClusterName/namespaces/istio-system/pods/mesh-hosted-apiserver-0/containers
    ```

    如果是专有网格模式，直接在相应集群中操作。

1. 使用以下命令移除对应 namespace 上的 annotation：

    ```shell
    kubectl annotate ns $namespace controller.mspider.io/workspace-id- controller.mspider.io/workspace-name-
    ```
