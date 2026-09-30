# Create a Ceph File Storage (CephFS) StorageClass

## Prerequisites

Refer to [Deploy Rook-ceph with the App Store](rook-ceph.md) to install rook-ceph and rook-ceph-cluster through the app store.

## Steps

1. Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __StorageClass (SC)__ -> __Create StorageClass (SC)__ in the left navigation bar.

2. Fill in the basic information. The parameters are described as follows:

    - The StorageClass name, CSI driver, reclaim policy, and disk binding mode cannot be modified after creation.
    - CSI storage driver: enter `rook-ceph.cephfs.csi.ceph.com`.
    - The custom parameters are defined as follows:

    | clusterID | rook-ceph | The namespace where the rook-ceph cluster runs |
    | --- | --- | --- |
    | csi.storage.k8s.io/fstype | ext4 | Specifies the file system type of the volume. If not specified, csi-provisioner defaults to "ext4". "xfs" is not recommended |
    | csi.storage.k8s.io/controller-expand-secret-name | rook-csi-rbd-provisioner | The name of the Kubernetes Secret used by the CSI provisioner when creating a volume |
    | csi.storage.k8s.io/controller-expand-secret-namespace | rook-ceph | The namespace where the above Secret resides |
    | csi.storage.k8s.io/node-stage-secret-name | rook-csi-cephfs-node | The name of the Secret used by the CSI controller when performing volume expansion |
    | csi.storage.k8s.io/node-stage-secret-namespace | rook-ceph | The namespace where the Secret resides when performing volume expansion |
    | csi.storage.k8s.io/provisioner-secret-name | rook-csi-cephfs-provisioner | The name of the Secret used by the CSI node plugin when mounting volumes on nodes |
    | csi.storage.k8s.io/provisioner-secret-namespace | rook-ceph | The namespace where the Secret resides when mounting volumes on nodes |
    | fsName | ceph-filesystem | Defines the CephFS file system name of the volume |
    | pool | ceph-filesystem-data0 | Defines the Ceph pool name of the volume |

    ![fs01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/fs01.png)

    ![fs02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/fs02.png)

3. After filling in the information, click __OK__ to create the StorageClass successfully
