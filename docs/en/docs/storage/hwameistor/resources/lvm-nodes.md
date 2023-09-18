# LVM Node Expansion

The storage system can be expanded by adding storage nodes. In HwameiStor, new storage nodes can be added by following these steps.

## Steps

### 1. Prepare the New Storage Node

Add a new node to the Kubernetes cluster or select an existing cluster node (non-HwameiStor node). The node must meet all the prerequisites mentioned in the [Prerequisites](../install/prereq.md) document. In this example, the details of the new storage node and disk are as follows:

- name: k8s-worker-4
- devPath: /dev/sdb
- diskType: SSD disk

After successfully adding the new node to the Kubernetes cluster, check and ensure that the following pods are running on that node and the related resources exist in the cluster:

```shell
kubectl get node
```

```none
NAME           STATUS   ROLES            AGE     VERSION
k8s-master-1   Ready    master           96d     v1.24.3-2+63243a96d1c393
k8s-worker-1   Ready    worker           96h     v1.24.3-2+63243a96d1c393
k8s-worker-2   Ready    worker           96h     v1.24.3-2+63243a96d1c393
k8s-worker-3   Ready    worker           96d     v1.24.3-2+63243a96d1c393
k8s-worker-4   Ready    worker           1h      v1.24.3-2+63243a96d1c393
```

```shell
kubectl -n hwameistor get pod -o wide | grep k8s-worker-4
```

```none
hwameistor-local-disk-manager-c86g5     2/2     Running   0     19h   10.6.182.105      k8s-worker-4   <none>  <none>
hwameistor-local-storage-s4zbw          2/2     Running   0     19h   192.168.140.82    k8s-worker-4   <none>  <none>
```

Check the LocalStorageNode resource:

```shell
kubectl get localstoragenode k8s-worker-4
```

```none
NAME                 IP           ZONE      REGION    STATUS   AGE
k8s-worker-4   10.6.182.103       default   default   Ready    8d
```

### 2. Add the New Storage Node to the HwameiStor System

To add a storage node, create a LocalStorageClaim resource to build a StorageClass for the new storage node. By doing this, the node will be successfully added to the HwameiStor system. Follow the steps below:

```console
$ kubectl apply -f - <<EOF
apiVersion: hwameistor.io/v1alpha1
kind: LocalDiskClaim
metadata:
  name: k8s-worker-4
spec:
  nodeName: k8s-worker-4
  description:
    diskType: SSD
EOF
```

### 3. Post-check

After completing the above steps, check the status of the new storage node and its StorageClass to ensure the normal operation of the node and HwameiStor system. Follow the steps below:

```shell
kubectl get localstoragenode k8s-worker-4
```

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
      freeCapacityBytes: 214744170496
      freeVolumeCount: 1000
      name: LocalStorage_PoolSSD
      totalCapacityBytes: 214744170496
      totalVolumeCount: 1000
      type: REGULAR
      usedCapacityBytes: 0
      usedVolumeCount: 0
      volumeCapacityBytesLimit: 214744170496
      volumes:
  state: Ready
```
