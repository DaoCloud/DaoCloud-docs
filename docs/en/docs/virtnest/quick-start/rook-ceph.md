# Rook Ceph Deployment Process

This page explains how to deploy Rook Ceph for creating virtual machines.

## Prerequisites

Refer to the [Prerequisites](https://rook.io/docs/rook/latest/Getting-Started/Prerequisites/prerequisites/) and [Installation Guide](https://rook.io/docs/rook/latest/Getting-Started/quickstart/#prerequisites) for detailed requirements.

- Kubernetes version >= 1.22
- The server nodes must have a Linux operating system with a kernel version of at least 4.
  Recommended operating systems are Ubuntu 18.04, Ubuntu 20.04, CentOS 7.9, or CentOS 8.5.
- Each node must have at least one unformatted and unpartitioned disk or one unformatted partition.
  The minimum configuration for the disk or partition is 100 GB, but it is recommended to have 200 GB.

## Deployment Steps

1. Install Snapshot CRD, Snapshot Controller, and CSI Driver

    ```sh
    git config --global http.sslVerify "false"
    git clone --single-branch --branch master https://github.com/kubernetes-csi/external-snapshotter.git
    cd external-snapshotter
    kubectl kustomize client/config/crd | kubectl create -f -
    kubectl -n kube-system kustomize deploy/kubernetes/snapshot-controller | kubectl -n kube-system create -f -
    kubectl kustomize deploy/kubernetes/csi-snapshotter | kubectl -n kube-system create -f -
    ```

2. Download the Rook repository

    ```git
    git clone --single-branch --branch master https://github.com/rook/rook.git
    ```

3. Deploy the Rook operator

    ```sh
    cd rook/deploy/examples
    kubectl create -f crds.yaml -f common.yaml -f operator.yaml
    ```

4. After the Operator is ready, deploy the Rook cluster

    ```sh
    kubectl create -f cluster.yaml
    ```

    If the Kubernetes cluster is a single-node cluster, use cluster-test.yaml instead of cluster.yaml.
    If the Kubernetes cluster has multiple nodes, modify cluster.yaml according to your actual cluster configuration (change all `allowMultiplePerNode` to true) and then create the cluster.

5. After successfully deploying the Rook cluster, create a CephFilesystem

    ```sh
    kubectl create -f filesystem.yaml
    ```

    If it is a single-node cluster, use filesystem-test.yaml.

6. Create a storage class and snapshot class

    ```sh
    kubectl create -f csi/cephfs/storageclass.yaml -f csi/cephfs/snapshotclass.yaml
    ```

7. Verify the installation

    ```sh
    kubectl get VolumeSnapshotClass
    ```

    The output should be similar to:

    ```console
    NAME DRIVER DELETIONPOLICY AGE
    csi-cephfsplugin-snapclass rook-ceph.cephfs.csi.ceph.com Delete 10m
    ```

## What if Rook Ceph Images Cannot Be Pulled?

If the Rook Ceph images cannot be pulled due to using an Operator for installation and modifying the image address in deploy/stateful/daemon, it may still fail when reinstalling Rook Ceph.
In this case, you can pull the images from a proxy address and retag them as the desired images (replace the image version as needed).

1. Pull the images from the proxy address:

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

2. Retag the images

    ```console
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-provisioner:v3.5.0 registry.k8s.io/sig-storage/csi-provisioner:v3.5.0
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-resizer:v1.8.0 registry.k8s.io/sig-storage/csi-resizer:v1.8.0
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-snapshotter:v6.2.2 registry.k8s.io/sig-storage/csi-snapshotter:v6.2.2
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-attacher:v4.3.0 registry.k8s.io/sig-storage/csi-attacher:v4.3.0
    ctr --namespace=k8s.io image tag quay.m.daocloud.io/cephcsi/cephcsi:v3.9.0 registry.k8s.io/cephcsi/cephcsi:v3.9.0
    ctr --namespace=k8s.io image tag k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar:v2.8.0 registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.8.0
    ```

Now the images are retagged and ready to be used for Rook Ceph deployment.
