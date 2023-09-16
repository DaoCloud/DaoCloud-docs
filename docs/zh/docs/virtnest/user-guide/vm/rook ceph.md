---
hide:
  - toc
---

# Rook Ceph 部署流程

本文将介绍如何部署 Rook Ceph，用于创建虚拟机。

## 前提条件

具体可参考[部署前提](https://rook.io/docs/rook/latest/Getting-Started/Prerequisites/prerequisites/)和[安装指引文档](https://rook.io/docs/rook/latest/Getting-Started/quickstart/#prerequisites) 

    - k8s版本 >= 1.22
    - 服务器节点的操作系统需要为 Linux 操作系统，Linux 内核版本必须在 4 以上。建议使用 Ubuntu 18.04、Ubuntu 20.04、CentOS 7.9、CentOS 8.5
    - 每个节点都必须至少具有 1 个未格式化且未分区的磁盘，或 1 个未格式化的分区。该磁盘或分区的最低配置为 100 GB，推荐配置为 200 GB


## 部署步骤:

1. 安装Snapshot CRDs , Snapshot Controller 和 CSI Driver

  `git config --global http.sslVerify "false"`
  `git clone --single-branch --branch master https://github.com/kubernetes-csi/external-snapshotter.git`
  `cd external-snapshotter`
  `kubectl kustomize client/config/crd | kubectl create -f -`
  `kubectl -n kube-system kustomize deploy/kubernetes/snapshot-controller | kubectl -n kube-system create -f -`
  `kubectl kustomize deploy/kubernetes/csi-snapshotter | kubectl -n kube-system create -f -`

2. 下载rook仓库

  `git clone --single-branch --branch master https://github.com/rook/rook.git`

3. 部署 rook operator

  `cd rook/deploy/examples`
  `kubectl create -f crds.yaml -f common.yaml -f operator.yaml`

4. operator部署就绪后, 部署rook cluster

  `kubectl create -f cluster.yaml`
  `// 如果k8s集群为单节点,请使用cluster-test.yaml,不要使用cluster.yaml, 如果k8s集群为多节点, 请按照实际集群配置修改cluster.yaml (将所有的 allowMultiplePerNode 改为true) 后创建cluster`

5. rook cluster部署成功后, 创建CephFilesystem

  `kubectl create -f filesystem.yaml`
  `// 如果为单节点集群,请使用 filesystem-test.yaml`

6. 创建storageclass以及snapshotclass

  `kubectl create -f csi/cephfs/storageclass.yaml -f csi/cephfs/snapshotclass.yaml`

7. 安装完成后验证

  `kubectl get VolumeSnapshotClass`
  `NAME                         DRIVER                          DELETIONPOLICY   AGE`
  `csi-cephfsplugin-snapclass   rook-ceph.cephfs.csi.ceph.com   Delete           10m`

## Rook Ceph镜像拉不下来怎么办？

由于 rook ceph 使用operator 安装, 修改 deploy/statefult/daemon 里的镜像地址,在重装 rook ceph 时还是会失效。可以通过拉取公司代理的镜像地址，然后重新打 tag 为所需的镜像(镜像版本根据实际情况进行替换)"

1. 拉取代理地址的镜像

  `crictl pull k8s.m.daocloud.io/sig-storage/csi-provisioner:v3.5.0`
  `crictl pull k8s.m.daocloud.io/sig-storage/csi-resizer:v1.8.0` 
  `crictl pull k8s.m.daocloud.io/sig-storage/csi-snapshotter:v6.2.2`
  `crictl pull k8s.m.daocloud.io/sig-storage/csi-attacher:v4.3.0`
  `crictl pull k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar:v2.8.0`
  `crictl pull quay.m.daocloud.io/cephcsi/cephcsi:v3.9.0`
  `crictl pull quay.m.daocloud.io/ceph/ceph:v17.2.6`
  `crictl pull docker.m.daocloud.io/rook/ceph:v1.11.8`
2. 重新打 tag
  `ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-provisioner:v3.5.0  registry.k8s.io/sig-storage/csi-provisioner:v3.5.0`
  `ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-resizer:v1.8.0  registry.k8s.io/sig-storage/csi-resizer:v1.8.0` 
  `ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-snapshotter:v6.2.2 registry.k8s.io/sig-storage/csi-snapshotter:v6.2.2`
  `ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-attacher:v4.3.0 registry.k8s.io/sig-storage/csi-attacher:v4.3.0`
  `ctr --namespace=k8s.io image tag quay.m.daocloud.io/cephcsi/cephcsi:v3.9.0  registry.k8s.io/cephcsi/cephcsi:v3.9.0`
  `ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar:v2.8.0  registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.8.0`

