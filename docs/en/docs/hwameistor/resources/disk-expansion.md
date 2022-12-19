# data disk expansion

When the storage capacity of a node in the storage system is insufficient, you can expand the capacity by adding disks to the node.
In HwameiStor, you can add disks (data disks) to nodes through the following steps.

## steps

### 1. Prepare new storage disk

Select the node to be expanded from HwameiStor, and insert the new disk into the disk slot of the node.
In this example, the new storage node and disk information used are as follows:

- name: k8s-worker-4
- devPath: /dev/sdc
- diskType: SSD

After the new disk is inserted into the HwameiStor storage node `k8s-worker-4`, check the status of the new disk on this node, as follows:

```console
# 1. Check whether the newly added disk is successfully inserted into the node and is correctly identified
$ ssh root@k8s-worker-4
$ lsblk | grep sdc
sdc 8:32 0 20G 1 disk

# 2. Check whether HwameiStor has correctly created the resource LocalDisk for the newly added disk, and the status is `Unclaimed`
$ kubectl get localdisk | grep k8s-worker-4 | grep sdc
k8s-worker-4-sdc k8s-worker-4 Unclaimed
```

### 2. Add the new disk to the storage pool of the node

By creating a resource LocalDiskClaim, add the new disk to the storage pool of the node. As follows. After completing the following operations, the new disk should be automatically added to the node's SSD storage pool. If there is no SSD storage pool on this node, HwameiStor will automatically create it and add new disks to it.

```console
$ kubectl apply -f - <<EOF
apiVersion: hwameistor.io/v1alpha1
kind: LocalDiskClaim
metadata:
  name: k8s-worker-4-expand
spec:
  nodeName: k8s-worker-4
  description:
    diskType: SSD
EOF
```

### 3. Follow-up inspection

After completing the above steps, check the status of the newly added disk and its storage pool to ensure the normal operation of the node and the HwameiStor system. details as follows:

```console
apiVersion: hwameistor.io/v1alpha1
kind: LocalStorageNode
metadata:
  name: k8s-worker-4
spec:
  hostname: k8s-worker-4
  storageIP: 10.6.182.103
  topogoly:
    region: default
    zone: default
status:
  pools:
    LocalStorage_PoolSSD:
      class: SSD
      disks:
      - capacityBytes: 214744170496
        devPath: /dev/sdb
        state: InUse
        type: SSD
      - capacityBytes: 214744170496
        devPath: /dev/sdc
        state: InUse
        type: SSD
      freeCapacityBytes: 429488340992
      freeVolumeCount: 1000
      name: LocalStorage_PoolSSD
      totalCapacityBytes: 429488340992
      totalVolumeCount: 1000
      type: REGULAR
      usedCapacityBytes: 0
      usedVolumeCount: 0
      volumeCapacityBytesLimit: 429488340992
      volumes:
  state: ready
```