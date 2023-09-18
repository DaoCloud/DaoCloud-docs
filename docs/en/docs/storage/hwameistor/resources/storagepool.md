# Create StorageClass

The following example is from a 4-node Kubernetes cluster:

```console
$ kubectl get no
NAME STATUS ROLES AGE VERSION
k8s-master-1 Ready master 82d v1.24.3-2+63243a96d1c393
k8s-worker-1 Ready worker 36d v1.24.3-2+63243a96d1c393
k8s-worker-2 Ready worker 59d v1.24.3-2+63243a96d1c393
k8s-worker-3 Ready worker 36d v1.24.3-2+63243a96d1c393
```

## Create `LocalDiskClaim` object

HwameiStor creates a `LocalDiskClaim` object according to the storage medium type to create a StorageClass.
To create a HDD StorageClass on all Kubernetes Worker nodes, users need to enter the name of each Worker node through the `storageNodes` parameter:

```console
helm template ./hwameistor \
   -s templates/post-install-claim-disks.yaml \
   --set storageNodes='{k8s-worker-1,k8s-worker-2,k8s-worker-3}' \
   | kubectl apply -f -
```

Or specify all Worker nodes by:

```console
sn="$( kubectl get no -l node-role.kubernetes.io/worker -o jsonpath="{.items[*].metadata.name}" | tr ' ' ',' )"

helm template ./hwameistor \
    -s templates/post-install-claim-disks.yaml \
    --set storageNodes="{$sn}" \
  | kubectl apply -f -
```

## Validate `LocalDiskClaim` object

Run the following command:

```console
$ kubectl get ldc
NAME NODEMATCH PHASE
k8s-worker-1 k8s-worker-1 Bound
k8s-worker-2 k8s-worker-2 Bound
k8s-worker-3 k8s-worker-3 Bound
```

## Verify `StorageClass`

Run the following command:

```console
$ kubectl get sc hwameistor-storage-lvm-hdd
NAME PROVISIONER RECLAIMPOLICY VOLUME BINDING MODE ALLOW VOLUME EXPANSION AGE
hwameistor-storage-lvm-hdd lvm.hwameistor.io Delete WaitForFirstConsumer true 114s
```

## Verify `LocalDisk` object

Run the following command:

```console
kubectl get ld
```

The output is similar to:

```console
NAME NODEMATCH CLAIM PHASE
k8s-worker-1-sda k8s-worker-1 Inuse
k8s-worker-1-sdb k8s-worker-1 k8s-worker-1 Claimed
k8s-worker-1-sdc k8s-worker-1 k8s-worker-1 Claimed
k8s-worker-2-sda k8s-worker-2 Inuse
k8s-worker-2-sdb k8s-worker-2 k8s-worker-2 Claimed
k8s-worker-2-sdc k8s-worker-2 k8s-worker-2 Claimed
k8s-worker-3-sda k8s-worker-3 Inuse
k8s-worker-3-sdb k8s-worker-3 k8s-worker-3 Claimed
k8s-worker-3-sdc k8s-worker-3 k8s-worker-3 Claimed
```

## Watch `VG` (optional)

On a Kubernetes Worker node, observe the creation of the `VG` for the `LocalDiskClaim` object.

Run the following command:

```console
$ vgdisplay LocalStorage_PoolHDD
  --- Volume group ---
  VG Name LocalStorage_PoolHDD
  System ID
  Format lvm2
  Metadata Areas 2
  Metadata Sequence No 1
  VG Access read/write
  VG Status resizable
  MAX LV 0
  Cur LV 0
  Open LV 0
  Max PV 0
  Cur PV 2
  Act PV 2
  VG Size 199.99 GiB
  PE Size 4.00 MiB
  Total PE 51198
  Alloc PE / Size 0 / 0
  Free PE / Size 51198 / 199.99 GiB
  VG UUID jJ3s7g-iyoJ-c4zr-3Avc-3K4K-BrJb-A5A5Oe
```

!!! note

    You can also configure the StorageClass by setting the `storageNode` parameter during HwameiStor installation:

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace \
        --set storageNodes='{k8s-worker-1,k8s-worker-2,k8s-worker-3}'
    ```
