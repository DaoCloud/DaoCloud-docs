# Data Volume IO Throttling

In HwameiStor, it allows users to specify the maximum IOPS and throughput for volumes on a Kubernetes cluster.

Follow these steps to create a volume with maximum IOPS and throughput and create a workload to use it.

## Prerequisites

- The cluster has already [installed HwameiStor](../install/deploy-ui.md)

- cgroup v2 requirements:

    - The operating system distribution enables cgroup v2
    - Linux kernel is 5.8 or higher

For more information, see [Kubernetes official documentation](https://kubernetes.io/zh-cn/docs/concepts/architecture/cgroups/).

## Create a New StorageClass with IOPS and Throughput Parameters

1. Go to the **Container Management** module, find the cluster with HwameiStor installed in the cluster list, and click the cluster name.

2. In the left navigation bar, select **Container Storage** -> **Storage Pools (SC)**, and click the **Create Storage Pool (SC)** button in the upper left corner.

    <!-- Add screenshot later -->

3. Enter the create storage pool interface, paying special attention to filling in the following parameters. Other parameters can refer to [form creation](../../../kpanda/user-guide/storage/sc.md).

    - Name: For this example, enter `hwameistor-storage-lvm-hdd-sample`.
    - Storage System: Select **HwameiStor**.
    - Storage Type: Supports **LVM Type** and **Bare Metal Type**. In this example, select **LVM Type**.
    - Disk Type: Supports **HDD** and **SSD**. In this example, select **HDD**.
    - Custom Parameters: Fill in the following four parameters,

        - `poolType: REGULAR`: Specify the storage pool type, currently only `REGULAR` is supported.
        - `csi.storage.k8s.io/fstype: xfs`: Specify the required file system type, if not defined, the default is `ext4`.
        - `provision-iops-on-creation: "100"`: Specify the maximum IOPS of the volume at creation.
        - `provision-throughput-on-creation: 1Mi`: Specify the maximum throughput of the volume at creation.
  
    <!-- Add screenshot later -->

    <!-- Add screenshot later -->

4. Click **OK** . After the creation is successful, return to the SC list interface.

## Create a PVC Using the StorageClass

1. In the left navigation bar, select **Container Storage** -> **Persistent Volume Claims (PVC)**, and click the **Create Persistent Volume Claim (PVC)** button in the upper left corner.

    <!-- Add screenshot later -->

2. Enter the create persistent volume claim interface, and fill in the following parameters.

    - Name: For this example, enter `pvc-hwameistor-sample`.
    - Storage Pool: Select the SC created above, named `hwameistor-storage-lvm-hdd-sample`.
    - Capacity: For this example, enter `10`.
    - Access Mode: The default is `ReadWriteMany`.

    <!-- Add screenshot later -->

3. Click **Confirm**. After the creation is successful, return to the SC list interface. After completion, you can create a Deployment to use the PVC.

## Create a Deployment with PVC

1. In the left navigation bar, select **Workloads** -> **Stateless Workloads**, and click the **Create from Image** button in the upper left corner.

    <!-- Add screenshot later -->

2. Pay attention to the following parameters:

    - Image: For this example, enter `daocloud.io/daocloud/testtools:latest`.
    - Data Storage:

        - Type: Select `Persistent Volume Claim (PVC)`.
        - Persistent Volume Claim (PVC): Select `pvc-hwameistor-sample`.
        - Container Path (mountPath): Enter `/data`.

    Other parameters have no special requirements.

    <!-- Add screenshot later -->

3. After creating the Deployment, click **Console** in the details interface, and execute the following command to test the IOPS and throughput of the volume:

    ```bash
    fio -direct=1  -iodepth=128 -rw=randwrite -ioengine=libaio -bs=4K -size=50M -numjobs=1 -runtime=600 -group_reporting -filename=/data/file.txt -name=Rand_Write_IOPS_Test
    ```

    It is expected to output the following:

    <!-- Add screenshot later -->

!!! note

    Due to cgroupv1 limitations, the maximum IOPS and throughput settings may not take effect for non-direct IO.

## Change the Maximum IOPS and Throughput of a Volume

The maximum IOPS and throughput are specified in the StorageClass parameters, and you cannot change it directly as it is currently immutable.

Unlike other storage vendors, HwameiStor is a Kubernetes-based storage solution that defines a set of operational primitives based on Kubernetes CRD. This means you can modify the relevant CRD to change the actual maximum IOPS and throughput of the volume.

The following steps show how to change the maximum IOPS and throughput of a volume.

### Find the LocalVolume CR Corresponding to the Given PVC

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

### Modify the LocalVolume CR

```bash
kubectl edit localvolume pvc-cac82087-6f6c-493a-afcd-09480de712ed
```

In the editor, find the `spec.volumeQoS` section and modify the `iops` and `throughput` fields. By the way, empty values mean no limit.

Finally, save the changes and exit the editor. The settings will take effect in a few seconds.

!!! note

    In the future, once Kubernetes supports [this feature](https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/3751-volume-attributes-class#motivation), we will allow users to directly modify the maximum IOPS and throughput of the volume.

### Check the Actual IOPS and Throughput of a Volume

HwameiStor uses [cgroupv1](https://www.kernel.org/doc/Documentation/cgroup-v1/blkio-controller.txt) to limit the IOPS and throughput of the volume, so you can use the following command to check the actual IOPS and throughput of the volume.

```console
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
