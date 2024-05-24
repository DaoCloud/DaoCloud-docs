# Volume Expansion

HwameiStor supports `CSI Volume Expansion`. This feature enables online expansion of volumes by
modifying the size of `PVC`. Currently, it supports both manual and automatic expansion methods.

## Manual Expansion

1. Access the proper cluster and navigate to **Storage** -> **Hwameistor**

2. Click **Local Volume** . In the local volume list interface, select a local volume to perform the `expand` operation.



3. In the `Expand` dialog box, enter the new size for expansion. In this example, expand from `1G` to `10G`, then click **OK** .



4. Refresh the current list and check that the capacity of the current local volume has changed from `1G` to `10G`.



## Automatic Expansion

The component hwameistor-pvc-autoresizer provides the capability for automatic PVC expansion.
The expansion behavior is controlled by the `ResizePolicy` CRD.

### ResizePolicy

Below is an example CR:

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

The three int-type fields `warningThreshold`, `resizeThreshold`, and `nodePoolUsageLimit` represent percentages.

- `warningThreshold`: Currently not associated with any alert action. It serves as a target ratio,
  meaning that after expansion, the volume usage will be below this percentage.
- `resizeThreshold`: Indicates a usage ratio. When the volume usage reaches this percentage,
  the expansion action will be triggered.
- `nodePoolUsageLimit`: Represents the upper limit of node storage pool usage.
  If the usage of a pool reaches this percentage, the volumes in this pool will not be automatically expanded.

### Matching Rules

This is an example CR with a label-selector.

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

`ResizePolicy` has three label-selectors:

- `pvcSelector`: Indicates that the PVCs selected by this selector will be automatically expanded according to the policy.
- `namespaceSelector`: Indicates that the PVCs in the namespaces selected by this selector
  will be automatically expanded according to the policy.
- `storageClassSelector`: Indicates that the PVCs created from the storage classes selected by
  this selector will be automatically expanded according to the policy.

These three selectors have an "AND" relationship. If you specify multiple selectors in a `ResizePolicy`,
only the PVCs that meet all the selectors will match the policy. If no selector is specified in the `ResizePolicy`, it becomes a cluster-wide `ResizePolicy`, acting as the default policy for all PVCs in the cluster.

## FAQs

### How to Watch the Expansion Process

The more capacity added, the longer the expansion time required. You can watch the entire expansion process in the `PVC` event logs.

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

### How to Watch the Expanded `PVC/PV`?

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
