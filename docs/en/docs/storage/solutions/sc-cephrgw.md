# Create a Ceph Object Storage (RGW) StorageClass

## Prerequisites

Refer to [Deploy Rook-ceph with the App Store](rook-ceph.md) to install rook-ceph and rook-ceph-cluster through the app store.

## Steps

1. Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __StorageClass (SC)__ -> __Create StorageClass (SC)__ in the left navigation bar.

2. Fill in the basic information. The parameters are described as follows:

    - The StorageClass name, CSI driver, reclaim policy, and disk binding mode cannot be modified after creation.
    - CSI storage driver: enter `rook-ceph.ceph.rook.io/bucket`.
    - The custom parameters are defined as follows:

    | Parameter | Value | Description |
    | --- | --- | --- |
    | objectStoreName | ceph-objectstore | Specifies the name of the object store |
    | objectStoreNamespace | rook-ceph | Specifies the Kubernetes namespace where the object store instance resides |
    | region | us-east-1 | Usually used to specify the geographic region of the object store instance |

    ![rgw01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/rgw01.png)

3. After filling in the information, click __OK__ to create the StorageClass successfully.
