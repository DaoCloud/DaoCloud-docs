# Node expansion

The storage system can be expanded by adding storage nodes. In HwameiStor, a new storage node can be added through the following steps.

## Steps

### 1. Prepare a new storage node

Add a new node to the Kubernetes cluster or select an existing cluster node (non-HwameiStor node)
that meets all the requirements listed in the [Prerequisites](../install/prereq.md) section.

In this example, the details of the newly added storage node and disk used are as follows:

- name: k8s-worker-4
- devPath: /dev/sdb
- diskType: SSD disk

After the newly added node has successfully joined the Kubernetes cluster, check to make sure that the following Pods are running on the node and related resources exist in the cluster:

```console
$ kubectl get node
NAME STATUS ROLES AGE VERSION
k8s-master-1 Ready master 96d v1.24.3-2+63243a96d1c393
k8s-worker-1 Ready worker 96h v1.24.3-2+63243a96d1c393
k8s-worker-2 Ready worker 96h v1.24.3-2+63243a96d1c393
k8s-worker-3 Ready worker 96d v1.24.3-2+63243a96d1c393
k8s-worker-4 Ready worker 1h v1.24.3-2+63243a96d1c393

$ kubectl -n hwameistor get pod -o wide | grep k8s-worker-4
hwameistor-local-disk-manager-c86g5 2/2 Running 0 19h 10.6.182.105 k8s-worker-4 <none> <none>
hwameistor-local-storage-s4zbw 2/2 Running 0 19h 192.168.140.82 k8s-worker-4 <none> <none>

# Check the LocalStorageNode resource
$ kubectl get localstoragenode k8s-worker-4
NAME IP ZONE REGION STATUS AGE
k8s-worker-4 10.6.182.103 default default Ready 8d
```

### 2. Add new storage nodes to HwameiStor system

Create a resource LocalStorageClaim for adding storage nodes to build a storage pool for adding storage nodes. In this way, the node has successfully joined the HwameiStor system. details as follows:

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

### 3. Follow-up inspection

After completing the above steps, check the status of the newly added storage node and its storage pool to ensure the normal operation of the node and the HwameiStor system. details as follows:

```console
$ kubectl get localstoragenode k8s-worker-4
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
  state: ready
```