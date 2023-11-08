# 使用非高可用本地卷

使用 HwameiStor 能非常轻松的运行有状态的应用。本文使用一个 MySQL 应用作为例子。

## 前提条件

- Hwameistor 已经安装成功

- 已经完成存储池创建，如未创建请进行[存储池 StorageClass 创建](../../../kpanda/user-guide/storage/sc.md)。
    
    目前 HwameiStor 安装成功后，Helm chart 会默认安装一个名为 `hwameistor-storage-lvm-hdd` 的 `StorageClass`，可使用此存储池创建本地数据卷。

      1. 点击`容器管理` -> 选择对应集群，进入集群详情，点击`容器存储`，选择`存储池`
      
         ![sc01](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/sc01.jpg)

      2. 点击`查看 YAML`，查看详情。

         ```yaml
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: hwameistor-storage-lvm-hdd
         parameters:
           convertible: "false"
           csi.storage.k8s.io/fstype: xfs
           poolClass: HDD
           poolType: REGULAR
           replicaNumber: "1"
           striped: "true"
           volumeKind: LVM
         provisioner: lvm.hwameistor.io
         reclaimPolicy: Delete
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         ```

         如果这个 `storageClass` 在安装时创建失败，可以[通过界面创建存储池 StorageClass ](../../../kpanda/user-guide/storage/sc.md)或 YAML 创建方式完成安装，YAML 方式如下：

         ```sh
         kubectl apply -f examples/sc-local.yaml
         ```

## 操作步骤

### 通过界面创建 `StatefulSet`

1. 点击 `容器管理` -> `选择对应集群`，进入集群详情，点击`容器存储`选择`工作负载`下的`有状态工作负载`，点击`镜像创建`。

    ![imagecreate](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/imagecreate01.jpg)

2. 完成`基本信息`进入到下一步，点击`创建数据卷声明模板`输入如下参数信息：

    ![pvctmp](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/pvctmp01.jpg)

    - `存储池`：已经创建的本地存储池。
    - `容量`：本地数据卷容量大小。
    - `访问模式`：Pod 读写模式，建议使用 ReadWriteOnce。
    - `容器路径`：数据存储挂载到容器上的路径。

3. 完成后点击`确定`，连续点击`下一步`完成创建。创建完成后点击`数据卷`列表查看对应的`数据卷状态`是否正常。

    ![pvctmp02](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/pvctmp02.jpg)

### 通过 YAML 创建 `StatefulSet`

!!! note

    下面的 MySQL Yaml 文件来自 [Kubernetes 的官方 Repo](https://github.com/kubernetes/website/blob/main/content/en/examples/application/mysql/mysql-statefulset.yaml)

在 HwameiStor 和 `StorageClass` 就绪后, 一条命令就能创建 MySQL 容器和它的数据卷:

```sh
kubectl apply -f sts-mysql_local.yaml
```

请注意 `volumeClaimTemplates` 使用 `storageClassName: hwameistor-storage-lvm-hdd`:

```yaml
spec:
  volumeClaimTemplates:
  - metadata:
      name: data
      labels:
        app: sts-mysql-local
        app.kubernetes.io/name: sts-mysql-local
    spec:
      storageClassName: hwameistor-storage-lvm-hdd
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
```

和 `schedulerName: hwameistor-scheduler`:

```yaml
spec:
  template:
    spec:
      schedulerName: hwameistor-scheduler
```

### 查看 MySQL 容器和 `PVC/PV`

在这个例子里，MySQL 容器被调度到了节点 `k8s-worker-3`。

```console
$ kubectl get po -l  app=sts-mysql-local -o wide
NAME                READY   STATUS    RESTARTS   AGE     IP            NODE        
sts-mysql-local-0   2/2     Running   0          3m08s   10.1.15.154   k8s-worker-3

$ kubectl get pvc -l  app=sts-mysql-local
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE   VOLUMEMODE
data-sts-mysql-local-0   Bound    pvc-accf1ddd-6f47-4275-b520-dc317c90f80b   1Gi        RWO            hwameistor-storage-lvm-hdd    3m   Filesystem
```

### 查看 `LocalVolume` 对象

通过查看和 `PV` 同名的 `LocalVolume(LV)`, 可以看到本地卷创建在了节点 `k8s-worker-3`上：

```console
$ kubectl get lv pvc-accf1ddd-6f47-4275-b520-dc317c90f80b

NAME                                       POOL                   REPLICAS   CAPACITY     ACCESSIBILITY   STATE   RESOURCE   PUBLISHED      AGE
pvc-accf1ddd-6f47-4275-b520-dc317c90f80b   LocalStorage_PoolHDD   1          1073741824                   Ready   -1         k8s-worker-3    3m
```

### [可选] 扩展 MySQL 应用成一个三节点的集群

HwameiStor 支持 `StatefulSet` 的横向扩展. `StatefulSet`容器都会挂载一个独立的本地卷：

```console
$ kubectl scale sts/sts-mysql-local --replicas=3

$ kubectl get po -l  app=sts-mysql-local -o wide
NAME                READY   STATUS     RESTARTS   AGE     IP            NODE        
sts-mysql-local-0   2/2     Running    0          4h38m   10.1.15.154   k8s-worker-3
sts-mysql-local-1   2/2     Running    0          19m     10.1.57.44    k8s-worker-2
sts-mysql-local-2   0/2     Init:0/2   0          14s     10.1.42.237   k8s-worker-1

$ kubectl get pvc -l  app=sts-mysql-local -o wide
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE     VOLUMEMODE
data-sts-mysql-local-0   Bound    pvc-accf1ddd-6f47-4275-b520-dc317c90f80b   1Gi        RWO            hwameistor-storage-lvm-hdd   3m07s   Filesystem
data-sts-mysql-local-1   Bound    pvc-a4f8b067-9c1d-450f-aff4-5807d61f5d88   1Gi        RWO            hwameistor-storage-lvm-hdd   2m18s   Filesystem
data-sts-mysql-local-2   Bound    pvc-47ee308d-77da-40ec-b06e-4f51499520c1   1Gi        RWO            hwameistor-storage-lvm-hdd   2m18s   Filesystem

$ kubectl get lv
NAME                                       POOL                   REPLICAS   CAPACITY     ACCESSIBILITY   STATE   RESOURCE   PUBLISHED      AGE
pvc-47ee308d-77da-40ec-b06e-4f51499520c1   LocalStorage_PoolHDD   1          1073741824                   Ready   -1         k8s-worker-1   2m50s
pvc-a4f8b067-9c1d-450f-aff4-5807d61f5d88   LocalStorage_PoolHDD   1          1073741824                   Ready   -1         k8s-worker-2   2m50s
pvc-accf1ddd-6f47-4275-b520-dc317c90f80b   LocalStorage_PoolHDD   1          1073741824                   Ready   -1         k8s-worker-3   3m40s
```
