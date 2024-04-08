# Backup and Restore of Bootstrap Node

This article describes the backup and restore of the kind cluster in the bootstrap node.

## Backup Overview

Installer v0.16.0 supports backup and restore of the kind cluster in the bootstrap node. Currently, the following information is backed up:

1. Two important files: [clusterConfig.yaml](../commercial/cluster-config.md),
   [manifest.yaml](../commercial/manifest.md)

    The information in clusterConfig.yaml and manifest.yaml is stored in the configmap of the kind cluster.

    ```shell
    root@my-cluster-installer-control-plane:/# kubectl get -n default cm
    NAME                       DATA   AGE
    clusterconfig-1710711049   1      4h46m
    kube-root-ca.crt           1      4h46m
    manifest-1710711049        1      4h46m
    ```

2. All data of the kind cluster

    The data of the kind cluster is mounted on the host machine at `/home/kind`,
    and the data of etcd is mounted at `/home/kind/etcd`. Do not delete any files
    in this directory.

    !!! note

        The mount directory can be defined in clusterconfig.yaml with
        `spec.tinderKind.resourcesMountPath`, and the default is `/home/kind`.

## Restore

Since the above backup is enabled by default for users, in case the kind cluster
is accidentally deleted or lost, you can run the installer command:

```shell
./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/manifest.yaml -j1,2
```
