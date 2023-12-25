# Volume Expansion

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

## Automatic volume expansion

The component `hwameistor-pvc-autoresizer` provides the capability for automatic expansion of PVC. The expansion behavior is controlled through the CRD called `ResizePolicy`.

### ResizePolicy

Here is a CR example:

```yaml
apiVersion: hwameistor.io/v1alpha1
kind: ResizePolicy
metadata:
  name: resizepolicy1
spec:
  warningThreshold: 60
  resizeThreshold: 80
  nodePoolUsageLimit: 90
```

The three `int` type fields `warningThreshold`, `resizeThreshold`, and `nodePoolUsageLimit` represent propotion rate.

- `warningThreshold`: Not associated with any warning actions currently, it serves as a target ratio. After the expansion, the volume utilization will be below this ratio.
- `resizeThreshold`: Indicating a utilization ratio. When the volume utilization reaches this ratio, the expansion action is triggered.
- `nodePoolUsageLimit`: Representing the upper limit of the node storage pool utilization. If the utilization of a pool reaches this ratio, volumes in this pool will not automatically expand.

### Matching rules

Here is a CR example  with a label selector:

```yaml
apiVersion: hwameistor.io/v1alpha1
kind: ResizePolicy
metadata:
  name: example-policy
spec:
  warningThreshold: 60
  resizeThreshold: 80
  nodePoolUsageLimit: 90
  storageClassSelector:
    matchLabels:
      pvc-resize: auto
  namespaceSelector:
    matchLabels:
      pvc-resize: auto
  pvcSelector:
    matchLabels:
      pvc-resize: auto
```

The `ResizePolicy` has three label-selector:

- `pvcSelector`: PVC selected by this selector will automatically expand according to the policy that selects them.
- `namespaceSelector`: PVC in the namespace selected by this selector will automatically expand according to this policy.
- `storageClassSelector`: PVC created from the storageclass selected by this selector will automatically expand according to this policy.

These three selectors have an "AND" relationship. If you specify multiple selectors in `ResizePolicy`, PVC that satisfy all selectors will match this policy. If no selectors are specified in the `ResizePolicy`, it is a cluster-wide `ResizePolicy`, acting as the default policy for all PVC in the entire cluster.
