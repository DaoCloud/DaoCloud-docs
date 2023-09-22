# Rook Ceph 部署流程

本文将介绍如何部署 Rook Ceph，用于创建虚拟机。

## 前提条件

具体可参考[部署前提](https://rook.io/docs/rook/latest/Getting-Started/Prerequisites/prerequisites/)和[安装指引文档](https://rook.io/docs/rook/latest/Getting-Started/quickstart/#prerequisites)

- k8s 版本 >= 1.22
- 服务器节点的操作系统需要为 Linux 操作系统，Linux 内核版本必须在 4 以上。建议使用 Ubuntu 18.04、Ubuntu 20.04、CentOS 7.9、CentOS 8.5
- 每个节点都必须至少具有 1 个未格式化且未分区的磁盘，或 1 个未格式化的分区。该磁盘或分区的最低配置为 100 GB，推荐配置为 200 GB

## 部署步骤

1. 安装 Snapshot CRD、Snapshot Controller 和 CSI Driver

    ```sh
    git config --global http.sslVerify "false"
    git clone --single-branch --branch master https://github.com/kubernetes-csi/external-snapshotter.git
    cd external-snapshotter
    kubectl kustomize client/config/crd | kubectl create -f -
    kubectl -n kube-system kustomize deploy/kubernetes/snapshot-controller | kubectl -n kube-system create -f -
    kubectl kustomize deploy/kubernetes/csi-snapshotter | kubectl -n kube-system create -f -
    ```

1. 下载 rook 仓库

    ```git
    git clone --single-branch --branch master https://github.com/rook/rook.git
    ```

1. 部署 rook operator

    ```sh
    cd rook/deploy/examples
    kubectl create -f crds.yaml -f common.yaml -f operator.yaml
    ```

1. Operator 部署就绪后，部署 rook cluster

    ```sh
    kubectl create -f cluster.yaml
    ```

    如果 K8s 集群为单节点，请使用 cluster-test.yaml，不要使用 cluster.yaml。
    如果 K8s 集群为多节点，请按照实际集群配置修改 cluster.yaml（将所有的 `allowMultiplePerNode` 改为 true）后创建 cluster

1. rook cluster 部署成功后，创建 CephFilesystem

    ```sh
    kubectl create -f filesystem.yaml
    ```

    如果为单节点集群，请使用 filesystem-test.yaml

1. 创建 storageclass 以及 snapshotclass

    ```sh
    kubectl create -f csi/cephfs/storageclass.yaml -f csi/cephfs/snapshotclass.yaml
    ```

1. 安装完成后验证

    ```sh
    kubectl get VolumeSnapshotClass
    ```

    输出类似于：

    ```console
    NAME DRIVER DELETIONPOLICY AGE
    csi-cephfsplugin-snapclass rook-ceph.cephfs.csi.ceph.com Delete 10m
    ```

## Rook Ceph 镜像拉不下来怎么办？

由于 rook ceph 使用 Operator 安装，修改 deploy/statefult/daemon 里的镜像地址，再重装 rook ceph 时还是会失效。
这时可以通过拉取代理的镜像地址，然后重新打 tag 为所需的镜像（镜像版本根据实际情况进行替换）

1. 拉取代理地址的镜像：

    ```sh
    crictl pull k8s.m.daocloud.io/sig-storage/csi-provisioner:v3.5.0
    crictl pull k8s.m.daocloud.io/sig-storage/csi-resizer:v1.8.0
    crictl pull k8s.m.daocloud.io/sig-storage/csi-snapshotter:v6.2.2
    crictl pull k8s.m.daocloud.io/sig-storage/csi-attacher:v4.3.0
    crictl pull k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar:v2.8.0
    crictl pull quay.m.daocloud.io/cephcsi/cephcsi:v3.9.0
    crictl pull quay.m.daocloud.io/ceph/ceph:v17.2.6
    crictl pull docker.m.daocloud.io/rook/ceph:v1.11.8
    ```

1. 重新打 tag

    ```console
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-provisioner:v3.5.0 registry.k8s.io/sig-storage/csi-provisioner:v3.5.0
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-resizer:v1.8.0 registry.k8s.io/sig-storage/csi-resizer:v1.8.0
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-snapshotter:v6.2.2 registry.k8s.io/sig-storage/csi-snapshotter:v6.2.2
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-attacher:v4.3.0 registry.k8s.io/sig-storage/csi-attacher:v4.3.0
    ctr --namespace=k8s.io image tag quay.m.daocloud.io/cephcsi/cephcsi:v3.9.0 registry.k8s.io/cephcsi/cephcsi:v3.9.0
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar:v2.8.0 registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.8.0
    ```
