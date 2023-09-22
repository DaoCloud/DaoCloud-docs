# LVM Node Expansion

The storage system can be expanded by adding storage nodes. In HwameiStor, new storage nodes can be added by following these steps.

## Steps

### 1. Prepare the New Storage Node

Add a new node to the Kubernetes cluster or select an existing cluster node (non-HwameiStor node). The node must meet all the prerequisites mentioned in the [Prerequisites](../install/prereq.md) document. In this example, the details of the new storage node and disk are as follows:

- name: k8s-worker-2
- devPath: /dev/sdb
- diskType: SSD disk

After successfully adding the new node to the Kubernetes cluster, check and ensure that the following pods are running on that node and the related resources exist in the cluster:

```console
$ kubectl get node
NAME           STATUS   ROLES            AGE     VERSION
k8s-master-1   Ready    master           96d     v1.24.3-2+63243a96d1c393
k8s-worker-1   Ready    worker           96h     v1.24.3-2+63243a96d1c393
k8s-worker-2   Ready    worker           96h     v1.24.3-2+63243a96d1c393

$ kubectl -n hwameistor get pod -o wide | grep k8s-worker-2
hwameistor-local-disk-manager-sfsf1     2/2     Running   0     19h   10.6.128.150      k8s-worker-2   <none>  <none>

# Check LocalDiskNode resource
$ kubectl get localdisknode k8s-worker-2
NAME           FREECAPACITY   TOTALCAPACITY   TOTALDISK   STATUS   AGE
k8s-worker-2                                              Ready    21d
```

### 2. Add the New Storage Node to the HwameiStor System

First, modify the `owner` information of disk sdb to be local-disk-manager, as shown below:

```console
$ kubectl edit ld k8s-worker-2-sdb
apiVersion: hwameistor.io/v1alpha1
kind: LocalDisk
metadata:
  name: k8s-worker-2-sdb
spec:
  devicePath: /dev/sdb
  nodeName: k8s-worker-2
+ owner: local-disk-manager
...
```

To add a storage node, create a LocalStorageClaim resource to build a StorageClass for the new storage node. By doing this, the node will be successfully added to the HwameiStor system. Follow the steps below:

```console
$ kubectl apply -f - <<EOF
apiVersion: hwameistor.io/v1alpha1
kind: LocalDiskClaim
metadata:
  name: k8s-worker-2
spec:
  nodeName: k8s-worker-2
  owner: local-disk-manager
  description:
    diskType: SSD
EOF
```

### 3. Post-check

After completing the above steps, check the status of the new storage node and its StorageClass to ensure the normal operation of the node and HwameiStor system. Follow the steps below:

```shell
kubectl get localdisknode k8s-worker-2 -o yaml
```

```yaml
apiVersion: hwameistor.io/v1alpha1
kind: LocalDiskNode
metadata:
  name: k8s-worker-2
spec:
  nodeName: k8s-worker-2  
status:  
  pools:
    LocalDisk_PoolSSD:
      class: SSD
      disks:
      - capacityBytes: 214744170496
        devPath: /dev/sdb
        state: Available
        type: SSD
      freeCapacityBytes: 214744170496
      freeVolumeCount: 1     
      totalCapacityBytes: 214744170496
      totalVolumeCount: 1
      type: REGULAR
      usedCapacityBytes: 0
      usedVolumeCount: 0
      volumeCapacityBytesLimit: 214744170496
      volumes:
  state: Ready
```
