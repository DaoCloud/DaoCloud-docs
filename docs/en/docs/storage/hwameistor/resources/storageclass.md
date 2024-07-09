---
MTPE: windsonsea
date: 2024-07-09
---

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

## Verify `LocalDiskClaim` object

The `LocalDiskClaim` object will be automatically deleted after it is bound.
You can run the following command to check if it has been deleted:

```console
$ kubectl get ldc
No resources found
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
[root@k8s-master home]# kubectl get ld
```

The output is similar to:

```console
NAME                                         NODEMATCH    DEVICEPATH   OWNER           PHASE       STATE    AGE
localdisk-2307de2b1c5b5d051058bc1d54b41d5c   k8s-node1    /dev/sdb     local-storage   Bound       Active   5d23h
localdisk-311191645ea00c62277fe709badc244e   k8s-node2    /dev/sdb                     Available   Active   5d23h
localdisk-37a20db051af3a53a1c4e27f7616369a   k8s-master   /dev/sdb                     Available   Active   5d23h
localdisk-b57b108ad2ccc47f4b4fab6f0b9eaeb5   k8s-node2    /dev/sda     system          Bound       Active   5d23h
localdisk-b682686c65667763bda58e391fbb5d20   k8s-master   /dev/sda     system          Bound       Active   5d23h
localdisk-da121e8f0dabac9ee1bcb6ed69840d7b   k8s-node1    /dev/sda     system          Bound       Active   5d23h
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
