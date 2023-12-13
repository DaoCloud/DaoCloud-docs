# Volume expansion

HwameiStor supports `CSI volume expansion`. This feature implements online volume expansion by modifying the size of `PVC`.

In the example below, we expand the PVC `data-sts-mysql-local-0` from 1GiB to 2GiB.

Current `PVC/PV` size:

```shell
kubectl get pvc data-sts-mysql-local-0
```
```none
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE
data-sts-mysql-local-0   Bound    pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8   1Gi        RWO            hwameistor-storage-lvm-hdd   85m
```
```shell
kubectl get pv pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8
```
```none
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                            STORAGECLASS                 REASON   AGE
pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8   1Gi        RWO            Delete           Bound    default/data-sts-mysql-local-0   hwameistor-storage-lvm-hdd            85m
```

## Check whether `StorageClass` uses the parameter `allowVolumeExpansion: true`

```shell
kubectl get pvc data-sts-mysql-local-0 -o jsonpath='{.spec.storageClassName}'
```
```none
hwameistor-storage-lvm-hdd
```
```shell
kubectl get sc hwameistor-storage-lvm-hdd -o jsonpath='{.allowVolumeExpansion}'
```
```none
true
```

## Modify the size of `PVC`

```shell
kubectl get edit pvc data-sts-mysql-local-0
```
```yaml
...
spec:
  resources:
    requests:
      storage: 2Gi
...
```

## Observe the expansion process

The more capacity you add, the longer it will take to expand. You can observe the entire expansion process in the event log of `PVC`.

```shell
kubectl describe pvc data-sts-mysql-local-0
```
```none
Events:
  Type     Reason                      Age                From                                Message
  ----     ------                      ----               ----                                -------
  Warning  ExternalExpanding           34s                volume_expand                       Ignoring the PVC: didn't find a plugin capable of expanding the volume; waiting for an external controller to process this PVC.
  Warning  VolumeResizeFailed          33s                external-resizer lvm.hwameistor.io  resize volume "pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8" by resizer "lvm.hwameistor.io" failed: rpc error: code = Unknown desc = volume expansion not completed yet
  Normal   Resizing                    32s (x2 over 33s)  external-resizer lvm.hwameistor.io  External resizer is resizing volume pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8
  Normal   FileSystemResizeRequired    32s                external-resizer lvm.hwameistor.io  Require file system resize of volume on node
  Normal   FileSystemResizeSuccessful  11s                kubelet                             MountVolume.NodeExpandVolume succeeded for volume "pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8" k8s-worker-3
```

## Observe the `PVC/PV` after the expansion is completed

```shell
kubectl get pvc data-sts-mysql-local-0
```
```none
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE
data-sts-mysql-local-0   Bound    pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8   2Gi        RWO            hwameistor-storage-lvm-hdd   96m
```
```shell
kubectl get pv pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8
```
```none
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                            STORAGECLASS                 REASON   AGE
pvc-b9fc8651-97b8-414c-8bcf-c8d2708c4ee8   2Gi        RWO            Delete           Bound    default/data-sts-mysql-local-0   hwameistor-storage-lvm-hdd            96m
```