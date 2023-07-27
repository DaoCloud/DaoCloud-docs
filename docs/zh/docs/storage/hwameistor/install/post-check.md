# 安装后检查

下文的示例来自一个 4 节点的 Kubernetes 集群。

```console
$ kubectl get no
NAME           STATUS   ROLES   AGE   VERSION
k8s-master-1   Ready    master  82d   v1.24.3-2+63243a96d1c393
k8s-worker-1   Ready    worker  36d   v1.24.3-2+63243a96d1c393
k8s-worker-2   Ready    worker  59d   v1.24.3-2+63243a96d1c393
k8s-worker-3   Ready    worker  36d   v1.24.3-2+63243a96d1c393
```

## 检查 Hwameistor 系统组件

运行以下命令检查 hwameistor 相关 Pod。

```console
$ kubectl -n hwameistor get pod
NAME                                                       READY   STATUS                  RESTARTS   AGE
drbd-adapter-10-6-234-40-rhel7-shfgt                      0/2     Completed   0          39s
drbd-adapter-10-6-234-41-rhel7-sw75z                      0/2     Completed   0          39s
drbd-adapter-10-6-234-42-rhel7-4vnl9                      0/2     Completed   0          39s
hwameistor-admission-controller-6995559b48-rxs4s          1/1     Running     0          40s
hwameistor-apiserver-677ddbdb8-9969c                      1/1     Running     0          40s
hwameistor-exporter-66784d5745-xwsxx                      1/1     Running     0          39s
hwameistor-local-disk-csi-controller-5d74d6c8cf-8vx5v     2/2     Running     0          40s
hwameistor-local-disk-manager-9vc75                       2/2     Running     0          40s
hwameistor-local-disk-manager-r42sg                       2/2     Running     0          40s
hwameistor-local-disk-manager-v75qb                       2/2     Running     0          40s
hwameistor-local-storage-csi-controller-758c94489-7g5tl   4/4     Running     0          40s
hwameistor-local-storage-pr265                            2/2     Running     0          40s
hwameistor-local-storage-qvrgb                            2/2     Running     0          40s
hwameistor-local-storage-zvggz                            2/2     Running     0          40s
hwameistor-scheduler-7585d88d9-8tbms                      1/1     Running     0          40s
hwameistor-ui-9885d9dc5-l4tlx                             1/1     Running     0          40s
hwameistor-volume-evictor-56df755847-m4h8b                1/1     Running     0          40s
```

!!! info

    `local-disk-manager` 和 `local-storage` 是 `DaemonSet`。在每个 Kubernetes 节点上都应该有一个 DaemonSet Pod。

## 查看 HwameiStor CRD（即 API）

以下 HwameiStor CRD 必须安装在系统上。

```console
$ kubectl api-resources --api-group hwameistor.io
NAME                       SHORTNAMES   APIVERSION               NAMESPACED   KIND
localdiskclaims            ldc          hwameistor.io/v1alpha1   false        LocalDiskClaim
localdisknodes             ldn          hwameistor.io/v1alpha1   false        LocalDiskNode
localdisks                 ld           hwameistor.io/v1alpha1   false        LocalDisk
localdiskvolumes           ldv          hwameistor.io/v1alpha1   false        LocalDiskVolume
localstoragenodes          lsn          hwameistor.io/v1alpha1   false        LocalStorageNode
localvolumeconverts        lvconvert    hwameistor.io/v1alpha1   true         LocalVolumeConvert
localvolumeexpands         lvexpand     hwameistor.io/v1alpha1   false        LocalVolumeExpand
localvolumegroupconverts   lvgconvert   hwameistor.io/v1alpha1   true         LocalVolumeGroupConvert
localvolumegroupmigrates   lvgmigrate   hwameistor.io/v1alpha1   true         LocalVolumeGroupMigrate
localvolumegroups          lvg          hwameistor.io/v1alpha1   true         LocalVolumeGroup
localvolumemigrates        lvmigrate    hwameistor.io/v1alpha1   true         LocalVolumeMigrate
localvolumereplicas        lvr          hwameistor.io/v1alpha1   false        LocalVolumeReplica
localvolumes               lv           hwameistor.io/v1alpha1   false        LocalVolume
```

## 查看 `LocalDiskNode` 和 `localDisks`

```console
$ kubectl get localdisknodes
NAME          TOTALDISK   FREEDISK
10-6-234-40   1
10-6-234-41   8
10-6-234-42   8

$ kubectl get localdisks
NAME              NODEMATCH     PHASE
10-6-234-40-sda   10-6-234-40   Bound
10-6-234-41-sda   10-6-234-41   Bound
10-6-234-41-sdb   10-6-234-41   Bound
10-6-234-41-sdc   10-6-234-41   Bound
10-6-234-41-sdd   10-6-234-41   Bound
10-6-234-41-sde   10-6-234-41   Bound
10-6-234-41-sdf   10-6-234-41   Bound
10-6-234-41-sdg   10-6-234-41   Bound
10-6-234-41-sdh   10-6-234-41   Bound
10-6-234-42-sda   10-6-234-42   Bound
10-6-234-42-sdb   10-6-234-42   Bound
10-6-234-42-sdc   10-6-234-42   Bound
10-6-234-42-sdd   10-6-234-42   Bound
10-6-234-42-sde   10-6-234-42   Bound
10-6-234-42-sdf   10-6-234-42   Bound
10-6-234-42-sdg   10-6-234-42   Bound
10-6-234-42-sdh   10-6-234-42   Bound
```

## 查看 `LocalStorageNodes` 及存储池

HwameiStor 为每个存储节点创建一个 CRD 资源 `LocalStorageNode (LSN)`。
每个 LSN 将会记录该存储节点的状态，及节点上的所有存储资源，包括存储池、数据卷、及相关配置信息。

```console
$ kubectl get lsn
NAME          IP            STATUS   AGE
10-6-234-40   10.6.234.40   Ready    3m52s
10-6-234-41   10.6.234.41   Ready    3m54s
10-6-234-42   10.6.234.42   Ready    3m55s

$ kubectl get lsn 10-6-234-41 -o yaml
apiVersion: hwameistor.io/v1alpha1
kind: LocalStorageNode
metadata:
  creationTimestamp: "2023-04-11T06:46:52Z"
  generation: 1
  name: 10-6-234-41
  resourceVersion: "13575433"
  uid: 4986f7b8-6fe1-43f1-bdca-e68b6fa53f92
spec:
  hostname: 10-6-234-41
  storageIP: 10.6.234.41
  topogoly:
    region: default
    zone: default
status:
  pools:
    LocalStorage_PoolHDD:
      class: HDD
      disks:
      - capacityBytes: 10733223936
        devPath: /dev/sdb
        state: InUse
        type: HDD
      - capacityBytes: 1069547520
        devPath: /dev/sdc
        state: InUse
        type: HDD
      - capacityBytes: 1069547520
        devPath: /dev/sdd
        state: InUse
        type: HDD
      - capacityBytes: 1069547520
        devPath: /dev/sde
        state: InUse
        type: HDD
      - capacityBytes: 1069547520
        devPath: /dev/sdf
        state: InUse
        type: HDD
      - capacityBytes: 1069547520
        devPath: /dev/sdg
        state: InUse
        type: HDD
      freeCapacityBytes: 16080961536
      freeVolumeCount: 1000
      name: LocalStorage_PoolHDD
      totalCapacityBytes: 16080961536
      totalVolumeCount: 1000
      type: REGULAR
      usedCapacityBytes: 0
      usedVolumeCount: 0
      volumeCapacityBytesLimit: 16080961536
  state: Ready
```

## 查看 StorageClass

HwameiStor Operator 在完成 HwameiStor 系统组件安装和系统初始化之后，
会根据系统配置（例如：是否开启 HA 模块、磁盘类型等）自动创建相应的 `StorageClass` 用于创建数据卷。

```console
$ kubectl get sc
NAME                                     PROVISIONER         RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
hwameistor-storage-lvm-hdd               lvm.hwameistor.io   Delete          WaitForFirstConsumer   false                  23h
hwameistor-storage-lvm-hdd-convertible   lvm.hwameistor.io   Delete          WaitForFirstConsumer   false                  23h
hwameistor-storage-lvm-hdd-ha            lvm.hwameistor.io   Delete          WaitForFirstConsumer   false                  23h
```

## （可选）检查 DRBD 的安装

在每个 Worker 节点上，DRBD 的内核模块必须被加载，例如在节点 `k8s-worker-1` 上：

```console
[root@k8s-worker-1 ~]$ lsmod | grep ^drbd
drbd_transport_tcp     22227  0
drbd                  606840  1 drbd_transport_tcp

$ cat /proc/drbd
version: 9.0.32-1 (api:2/proto:86-121)
GIT-hash: 7d2933d5a3764fcc5e0bf54b71fd9cfb0363be1a build by @4904565a901d, 2022-09-07 08:53:17
Transports (api:17): tcp (9.0.32-1)
```
