# Data disk expansion

When the storage capacity of a node in the storage system is insufficient, you can increase the capacity by adding disks to that node. In HwameiStor, you can follow the steps below to add disks (data disks) to a node:

Here are the specific steps:

## Steps

### Prepare the new storage disk

Add a new node to the Kubernetes cluster or select an existing cluster node (non-HwameiStor node). This node must meet all the requirements listed in the [Prerequisites](/../install/prereq.md) section. In this example, the details of the new storage node and disk used are as follows:

- Name: k8s-worker-4
- Device path: /dev/sdb
- Disk type: SSD disk

After inserting the new disk into the HwameiStor storage node `k8s-worker-4`, check the status of the new disk on that node as follows:

1. Verify if the new disk has been successfully inserted into the node and correctly recognized.

    ```shell
    # 1. Check if the new disk has been successfully inserted into the node and correctly recognized.
    $ ssh root@k8s-worker-4
    $ lsblk | grep sdc
    sdc        8:32     0     20G  1 disk
    
    # 2. Check if HwameiStor has correctly created the LocalDisk resource for the new disk and its status is 'Unclaimed'.
    $ kubectl get localdisk | grep k8s-worker-4 | grep sdc
    k8s-worker-4-sdc   k8s-worker-4       Unclaimed 
    ```

2. Check if HwameiStor has correctly created the LocalDisk resource for the new disk and its status is 'Unclaimed'.

    ```shell
    kubectl get localdisk | grep k8s-worker-4 | grep sdc
    ```

    ```none
    k8s-worker-4-sdc   k8s-worker-4       Unclaimed 
    ```

### Add the new disk to the node's StorageClass

To add the new disk to the node's StorageClass, create a LocalDiskClaim resource. After performing the following steps, the new disk should be automatically added to the SSD StorageClass of the node. If there is no SSD StorageClass on that node, HwameiStor will create one automatically and add the new disk to it.

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

## Post check

After completing the above steps, you should check the status of the
newly added disk and its StorageClass to ensure the normal operation
of both the node and the HwameiStor system. Here are the specific steps:

```yaml
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
