# 创建存储池

下面的例子来自一个 4 节点的 Kubernetes 集群：

```console
$ kubectl get no
NAME           STATUS   ROLES   AGE   VERSION
k8s-master-1   Ready    master  82d   v1.24.3-2+63243a96d1c393
k8s-worker-1   Ready    worker  36d   v1.24.3-2+63243a96d1c393
k8s-worker-2   Ready    worker  59d   v1.24.3-2+63243a96d1c393
k8s-worker-3   Ready    worker  36d   v1.24.3-2+63243a96d1c393
```

## 创建 `LocalDiskClaim` 对象

HwameiStor 根据存储介质类型创建 `LocalDiskClaim` 对象来创建存储池。
要在所有 Kubernetes Worker 节点上创建一个 HDD 存储池，用户需要通过 `storageNodes` 参数输入各个 Worker 节点名：

```console
helm template ./hwameistor \
   -s templates/post-install-claim-disks.yaml \
   --set storageNodes='{k8s-worker-1,k8s-worker-2,k8s-worker-3}' \
   | kubectl apply -f -
```

或者通过以下方法指定所有 Worker 节点：

```console
sn="$( kubectl get no -l node-role.kubernetes.io/worker -o jsonpath="{.items[*].metadata.name}" | tr ' ' ',' )"

helm template ./hwameistor \
    -s templates/post-install-claim-disks.yaml \
    --set storageNodes="{$sn}" \
  | kubectl apply -f -
```

## 验证 `LocalDiskClaim` 对象

`LocalDiskClaim` 对象在挂载（bound）后会被自动删除，你可以运行以下命令查看其是否已被删除：

```console
$ kubectl get ldc
No resources found
```

## 验证 `StorageClass`

运行以下命令：

```console
$ kubectl get sc hwameistor-storage-lvm-hdd
NAME                         PROVISIONER         RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
hwameistor-storage-lvm-hdd   lvm.hwameistor.io   Delete          WaitForFirstConsumer   true                   114s
```

## 验证 `LocalDisk` 对象

运行以下命令：

```console
[root@k8s-master home]# kubectl get ld
```

输出类似于：

```console
NAME                                         NODEMATCH    DEVICEPATH   OWNER           PHASE       STATE    AGE
localdisk-2307de2b1c5b5d051058bc1d54b41d5c   k8s-node1    /dev/sdb     local-storage   Bound       Active   5d23h
localdisk-311191645ea00c62277fe709badc244e   k8s-node2    /dev/sdb                     Available   Active   5d23h
localdisk-37a20db051af3a53a1c4e27f7616369a   k8s-master   /dev/sdb                     Available   Active   5d23h
localdisk-b57b108ad2ccc47f4b4fab6f0b9eaeb5   k8s-node2    /dev/sda     system          Bound       Active   5d23h
localdisk-b682686c65667763bda58e391fbb5d20   k8s-master   /dev/sda     system          Bound       Active   5d23h
localdisk-da121e8f0dabac9ee1bcb6ed69840d7b   k8s-node1    /dev/sda     system          Bound       Active   5d23h
```

## 观察 `VG` (可选)

在一个 Kubernetes Worker 节点上，观察为 `LocalDiskClaim` 对象创建 `VG`。

运行以下命令：

```console
$ vgdisplay LocalStorage_PoolHDD
  --- Volume group ---
  VG Name               LocalStorage_PoolHDD
  System ID
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               199.99 GiB
  PE Size               4.00 MiB
  Total PE              51198
  Alloc PE / Size       0 / 0
  Free  PE / Size       51198 / 199.99 GiB
  VG UUID               jJ3s7g-iyoJ-c4zr-3Avc-3K4K-BrJb-A5A5Oe
```

!!! note

    在安装 HwameiStor 期间也可以通过设置 `storageNode` 参数配置存储池：

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace \
        --set storageNodes='{k8s-worker-1,k8s-worker-2,k8s-worker-3}'
    ```
