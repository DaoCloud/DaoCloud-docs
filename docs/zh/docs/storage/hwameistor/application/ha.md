# 使用高可用卷

HwameiStor 使用开源的 DRBD 数据同步技术创建**高可用卷**，本章节展示 高可用卷的使用这里我们使用一个 MySQL 应用作为例子。

!!! note

    下面的 MySQL Yaml 文件来自 [Kubernetes 的官方 Repo](https://github.com/kubernetes/website/blob/main/content/en/examples/application/mysql/mysql-statefulset.yaml)

## 前提条件

- Hwameistor 已经安装成功

- 已经完成高可用存储池创建，如未创建请进行[存储池 StorageClass 创建](../../../kpanda/user-guide/storage/sc.md)。

- 已经完成[DRDB 内核组件部署](../install/drbdinstall.md) 

  目前 HwameiStor 安装成功后，Helm chart 会默认安装一个名为 `hwameistor-storage-lvm-hdd` 的 `StorageClass`，可使用此存储池创建本地数据卷。

    1. 点击`容器管理` -> 选择对应集群，进入集群详情，点击`容器存储`，确认是否已创建`高可用存储池`

        ![sc01](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/ha-sc01.jpg)

    2. 点击`查看 YAML`，查看详情。`StorageClass` "hwameistor-storage-lvm-hdd-ha" 使用参数 `replicaNumber: "2"` 开启高可用功能：

        ![sc-yaml](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/ha-sc02.jpg)

        ```
        $ kubectl apply -f examples/sc_ha.yaml
        $ kubectl get sc hwameistor-storage-lvm-hdd-ha -o yaml
        
        apiVersion: storage.k8s.io/v1
        kind: StorageClass
        metadata:
          name: hwameistor-storage-lvm-hdd-ha
        parameters:
          replicaNumber: "2"
          convertible: "false"
          csi.storage.k8s.io/fstype: xfs
          poolClass: HDD
          poolType: REGULAR
          striped: "true"
          volumeKind: LVM
        provisioner: lvm.hwameistor.io
        reclaimPolicy: Delete
        volumeBindingMode: WaitForFirstConsumer
        allowVolumeExpansion: true
        ```

## 创建 `StatefulSet`

在 HwameiStor 和 `StorageClass` 就绪后, 一条命令就能创建 MySQL 容器和它的数据卷:

```sh
kubectl apply -f exapmles/sts-mysql_ha.yaml
```

请注意 `volumeClaimTemplates` 使用 `storageClassName: hwameistor-storage-lvm-hdd-ha`:

```yaml
spec:
  volumeClaimTemplates:
  - metadata:
      name: data
      labels:
        app: sts-mysql-ha
        app.kubernetes.io/name: sts-mysql-ha
    spec:
      storageClassName: hwameistor-storage-lvm-hdd-ha
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
```

## 查看 MySQL Pod and `PVC/PV`

在这个例子里，MySQL 容器被调度到了节点 `k8s-worker-3`。

```console
$ kubectl get po -l  app=sts-mysql-ha -o wide
NAME                READY   STATUS    RESTARTS   AGE     IP            NODE        
sts-mysql-ha-0   2/2     Running   0          3m08s   10.1.15.151   k8s-worker-1

$ kubectl get pvc -l  app=sts-mysql-ha
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE   VOLUMEMODE
data-sts-mysql-ha-0   Bound    pvc-5236ee6f-8212-4628-9876-1b620a4c4c36   1Gi        RWO            hwameistor-storage-lvm-hdd    3m   Filesystem
```

## 查看 `LocalVolume` and `LocalVolumeReplica` 对象

通过查看和 `PV` 同名的 `LocalVolume(LV)`, 可以看到本地卷创建在了节点 `k8s-worker-1` 和节点 `k8s-worker-2`.

```console
$ kubectl get lv pvc-5236ee6f-8212-4628-9876-1b620a4c4c36

NAME                                       POOL                   REPLICAS   CAPACITY     ACCESSIBILITY   STATE   RESOURCE   PUBLISHED                    AGE
pvc-5236ee6f-8212-4628-9876-1b620a4c4c36   LocalStorage_PoolHDD   1          1073741824                   Ready   -1         k8s-worker-1,k8s-worker-2    3m
```

`LocalVolumeReplica (LVR)` 进一步显示每个节点上的后端逻辑卷设备：

```console
kubectl get lvr
NAME                                          CAPACITY     NODE           STATE   SYNCED   DEVICE                                                              AGE
5236ee6f-8212-4628-9876-1b620a4c4c36-d2kn55   1073741824   k8s-worker-1   Ready   true     /dev/LocalStorage_PoolHDD-HA/5236ee6f-8212-4628-9876-1b620a4c4c36   4m
5236ee6f-8212-4628-9876-1b620a4c4c36-glm7rf   1073741824   k8s-worker-3   Ready   true     /dev/LocalStorage_PoolHDD-HA/5236ee6f-8212-4628-9876-1b620a4c4c36   4m
```
