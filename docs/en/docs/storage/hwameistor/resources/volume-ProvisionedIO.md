# Data Volume IO Throttling

In HwameiStor, it allows users to specify the maximum IOPS and throughput for volumes on a Kubernetes cluster.

Please follow the steps below to create a volume with maximum IOPS and throughput and create a workload to use it.

## Create a New StorageClass with Maximum IOPS and Throughput Parameters

By default, HwameiStor does not automatically create such a StorageClass during installation, so you need to create the StorageClass manually.

An example StorageClass is as follows:

```yaml
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: hwameistor-storage-lvm-hdd-sample
parameters:
  convertible: "false"
  csi.storage.k8s.io/fstype: xfs
  poolClass: HDD
  poolType: REGULAR
  provision-iops-on-creation: "100"
  provision-throughput-on-creation: 1Mi
  replicaNumber: "1"
  striped: "true"
  volumeKind: LVM
provisioner: lvm.hwameistor.io
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

Compared to the regular StorageClass created by the HwameiStor installer, the following parameters have been added:

- provision-iops-on-creation: Specifies the maximum IOPS for the volume at creation time.
- provision-throughput-on-creation: Specifies the maximum throughput for the volume at creation time.

After creating the StorageClass, you can use it to create PVC (PersistentVolumeClaim).

## Create PVC using StorageClass

An example PVC is as follows:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-sample
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: hwameistor-storage-lvm-hdd-sample
```

After creating the PVC, you can create a Deployment to use the PVC.

## Create a Deployment with PVC

An example Deployment is as follows:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: pod-sample
  name: pod-sample
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pod-sample
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: pod-sample
    spec:
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: pvc-sample
      containers:
      - command:
        - sleep
        - "100000"
        image: busybox
        name: busybox
        resources: {}
        volumeMounts:
        - name: data
          mountPath: /data
status: {}
```

After creating the Deployment, you can use the following command to test the IOPS and throughput of the volume:

```bash
kubectl exec -it pod-sample-5f5f8f6f6f-5q4q5 -- /bin/sh
dd if=/dev/zero of=/data/test bs=4k count=1000000 oflag=direct
```

**Note**: Due to cgroupv1 limitations, the settings for maximum IOPS and throughput may not take effect on non-direct IO.

## How to Change the Maximum IOPS and Throughput of a Data Volume

The maximum IOPS and throughput are specified in the parameters of the StorageClass, and you cannot directly change them as they are now immutable.

Unlike other storage vendors, HwameiStor is a Kubernetes-based storage solution that defines a set of operational primitives based on Kubernetes CRDs. This means you can modify the relevant CRD to change the actual maximum IOPS and throughput of a volume.

The following steps show how to change the maximum IOPS and throughput of a data volume.

### Find the LocalVolume CR for the Specified PVC

```console
$ kubectl get pvc pvc-sample

NAME             STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                        AGE
demo             Bound     pvc-c354a56a-5cf4-4ff6-9472-4e24c7371e10   10Gi       RWO            hwameistor-storage-lvm-hdd          5d23h
pvc-sample       Bound     pvc-cac82087-6f6c-493a-afcd-09480de712ed   10Gi       RWO            hwameistor-storage-lvm-hdd-sample   5d23h

$ kubectl get localvolume

NAME                                       POOL                   REPLICAS   CAPACITY      USED       STATE   RESOURCE   PUBLISHED   FSTYPE   AGE
pvc-c354a56a-5cf4-4ff6-9472-4e24c7371e10   LocalStorage_PoolHDD   1          10737418240   33783808   Ready   -1         master      xfs      5d23h
pvc-cac82087-6f6c-493a-afcd-09480de712ed   LocalStorage_PoolHDD   1          10737418240   33783808   Ready   -1         master      xfs      5d23h
```

According to the printed output, the LocalVolume CR for the PVC is `pvc-cac82087-6f6c-493a-afcd-09480de712ed`.

### Modify LocalVolume CR

```bash
kubectl edit localvolume pvc-cac82087-6f6c-493a-afcd-09480de712ed
```

In the editor, locate the `spec.volumeQoS` section and modify the `iops` and `throughput` fields. Note that a blank value indicates no limit.

Finally, save the changes and exit the editor. The settings will take effect within a few seconds.

**Note**: In the future, once Kubernetes supports it ([link](https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/3751-volume-attributes-class#motivation)), we will allow users to directly modify the maximum IOPS and throughput of volumes.

## How to Check the Actual IOPS and Throughput of a Data Volume

HwameiStor uses [cgroupv1](https://www.kernel.org/doc/Documentation/cgroup-v1/blkio-controller.txt) to limit the IOPS and throughput of data volumes. Therefore, you can use the following command to check the actual IOPS and throughput of a data volume.

```
$ lsblk
NAME            MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda               8:0    0   160G  0 disk
├─sda1            8:1    0     1G  0 part /boot
└─sda2            8:2    0   159G  0 part
  ├─centos-root 253:0    0   300G  0 lvm  /
  ├─centos-swap 253:1    0   7.9G  0 lvm
  └─centos-home 253:2    0 101.1G  0 lvm  /home
sdb               8:16   0   100G  0 disk
├─LocalStorage_PoolHDD-pvc--cac82087--6f6c--493a--afcd--09480de712ed
                253:3    0    10G  0 lvm  /var/lib/kubelet/pods/3d6bc980-68ae-4a65-a1c8-8b410b7d240f/v
└─LocalStorage_PoolHDD-pvc--c354a56a--5cf4--4ff6--9472--4e24c7371e10
                253:4    0    10G  0 lvm  /var/lib/kubelet/pods/521fd7b4-3bef-415b-8720-09225f93f231/v
sdc               8:32   0   300G  0 disk
└─sdc1            8:33   0   300G  0 part
  └─centos-root 253:0    0   300G  0 lvm  /
sr0              11:0    1   973M  0 rom

$ cat /sys/fs/cgroup/blkio/blkio.throttle.read_iops_device
253:3 100

$ cat /sys/fs/cgroup/blkio/blkio.throttle.write_iops_device
253:3 100

$ cat /sys/fs/cgroup/blkio/blkio.throttle.read_bps_device
253:3 1048576

$ cat /sys/fs/cgroup/blkio/blkio.throttle.write_bps_device
253:3 1048576
```
