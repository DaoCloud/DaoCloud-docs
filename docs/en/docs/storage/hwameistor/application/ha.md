# High Availability Volume

HwameiStor uses the open source DRBD data synchronization technology to create a **High Availability Volume**. This section shows how to use a High Availability Volume. Here we use a MySQL application as an example.

!!! note

    The MySQL YAML file below is from the [Kubernetes official repo](https://github.com/kubernetes/website/blob/main/content/en/examples/application/mysql/mysql-statefulset.yaml)

## Prerequisites

- HwameiStor has been installed successfully

- The high availability storage pool has been created. If not, refer to [Create StorageClass](../../../kpanda/user-guide/storage/sc.md).

- The [DRBD kernel module](../install/drbdinstall.md) has been deployed

  After HwameiStor is installed successfully, the Helm chart installs a `StorageClass` named `hwameistor-storage-lvm-hdd` by default, and you can use this storage pool to create local volumes.

    1. Click __Container Management__ -> select the corresponding cluster to enter the cluster details, click __Container Storage__, and check whether the __High Availability Storage Pool__ has been created.

    2. Click __View YAML__ to view the details. The `StorageClass` "hwameistor-storage-lvm-hdd-ha" uses the parameter `replicaNumber: "2"` to enable high availability:

        ```
        $ kubectl apply -f examples/sc_ha.yaml
        $ kubectl get sc hwameistor-storage-lvm-hdd-ha -o yaml

        apiVersion: storage.k8s.io/v1
        kind: StorageClass
        metadata:
          name: hwameistor-storage-lvm-hdd-ha
        parameters:
          replicaNumber: "2"
          convertible: "false"
          csi.storage.k8s.io/fstype: xfs
          poolClass: HDD
          poolType: REGULAR
          striped: "true"
          volumeKind: LVM
        provisioner: lvm.hwameistor.io
        reclaimPolicy: Delete
        volumeBindingMode: WaitForFirstConsumer
        allowVolumeExpansion: true
        ```

## Create `StatefulSet`

After HwameiStor and `StorageClass` are ready, one command can create the MySQL container and its data volume:

```sh
kubectl apply -f exapmles/sts-mysql_ha.yaml
```

Note that `volumeClaimTemplates` uses `storageClassName: hwameistor-storage-lvm-hdd-ha`:

```yaml
spec:
  volumeClaimTemplates:
  - metadata:
      name: data
      labels:
        app: sts-mysql-ha
        app.kubernetes.io/name: sts-mysql-ha
    spec:
      storageClassName: hwameistor-storage-lvm-hdd-ha
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
```

## View MySQL Pod and `PVC/PV`

In this example, the MySQL container is scheduled to node `k8s-worker-3`.

```console
$ kubectl get po -l  app=sts-mysql-ha -o wide
NAME                READY   STATUS    RESTARTS   AGE     IP            NODE        
sts-mysql-ha-0   2/2     Running   0          3m08s   10.1.15.151   k8s-worker-1

$ kubectl get pvc -l  app=sts-mysql-ha
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE   VOLUMEMODE
data-sts-mysql-ha-0   Bound    pvc-5236ee6f-8212-4628-9876-1b620a4c4c36   1Gi        RWO            hwameistor-storage-lvm-hdd    3m   Filesystem
```

## View `LocalVolume` and `LocalVolumeReplica` Objects

By viewing the `LocalVolume(LV)` with the same name as `PV`, you can see that the local volume is created on node `k8s-worker-1` and node `k8s-worker-2`.

```console
$ kubectl get lv pvc-5236ee6f-8212-4628-9876-1b620a4c4c36

NAME                                       POOL                   REPLICAS   CAPACITY     ACCESSIBILITY   STATE   RESOURCE   PUBLISHED                    AGE
pvc-5236ee6f-8212-4628-9876-1b620a4c4c36   LocalStorage_PoolHDD   1          1073741824                   Ready   -1         k8s-worker-1,k8s-worker-2    3m
```

`LocalVolumeReplica (LVR)` further shows the backend logical volume devices on each node:

```console
kubectl get lvr
NAME                                          CAPACITY     NODE           STATE   SYNCED   DEVICE                                                              AGE
5236ee6f-8212-4628-9876-1b620a4c4c36-d2kn55   1073741824   k8s-worker-1   Ready   true     /dev/LocalStorage_PoolHDD-HA/5236ee6f-8212-4628-9876-1b620a4c4c36   4m
5236ee6f-8212-4628-9876-1b620a4c4c36-glm7rf   1073741824   k8s-worker-3   Ready   true     /dev/LocalStorage_PoolHDD-HA/5236ee6f-8212-4628-9876-1b620a4c4c36   4m
```
