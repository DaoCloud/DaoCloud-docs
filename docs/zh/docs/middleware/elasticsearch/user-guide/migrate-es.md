# 基于 Hwameistor 的 Elasticsearch 迁移实践

## 介绍

K8s 的特性，有状态的应用在部署完成后，其是否可以偏移是依赖底层 `CSI` 的能力，在使用 `Hwameistor` 作为`CSI` 时，应用是不具备进行跨 Node的能力。

然而，当我们的最初集群资源可能出现不均匀等一些意外情况，所以需要将一些有状态的应用进行迁移。

这篇文章讲述的是：在使用 `Hwameistor` 时，如果进行 数据服务中间件的迁移，本文以`Elasticsearch` 为例；同时参考 `Hwameistor` 官方提供的迁移指南，演示迁移过程。

## 实验场景介绍

以下梳理了本次实验的基本信息

### 集群基本信息

```bash
[root@prod-master1 ~]# kubectl get node
NAME           STATUS   ROLES           AGE   VERSION
prod-master1   Ready    control-plane   15h   v1.25.4
prod-master2   Ready    control-plane   15h   v1.25.4
prod-master3   Ready    control-plane   15h   v1.25.4
prod-worker1   Ready    <none>          15h   v1.25.4
prod-worker2   Ready    <none>          15h   v1.25.4
prod-worker3   Ready    <none>          15h   v1.25.4
```

### ES 安装的基本信息

```bash
[root@prod-master1 ~]# kubectl get pods -o wide | grep es-cluster-masters-es-data

mcamel-common-es-cluster-masters-es-data-0 Running prod-worker1
mcamel-common-es-cluster-masters-es-data-1 Running prod-worker3
mcamel-common-es-cluster-masters-es-data-2 Running prod-worker2
```

### 获取 es 使用的 pvc 信息

```bash
kubectl -n mcamel-system get pvc -l elasticsearch.k8s.elastic.co/statefulset-name=mcamel-common-es-cluster-masters-es-data
NAME                                                            STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-0   Bound    pvc-61776435-0df5-448f-abb9-4d06774ec0e8   35Gi       RWO            hwameistor-storage-lvm-hdd   15h
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1   Bound    pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c   35Gi       RWO            hwameistor-storage-lvm-hdd   15h
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-2   Bound    pvc-955bd221-3e83-4bb5-b842-c11584bced10   35Gi       RWO            hwameistor-storage-lvm-hdd   15h
```

## 实验目标

将 `prod-worker3` 上的 `mcamel-common-es-cluster-masters-es-data-1` （以下简称 `esdata-1`）迁移到 `prod-master3` 之上

## 准备工作

### 确认需要迁移 PV

明确 `esdata-1` 对应的 `PV` 磁盘是那个

```bash
[root@prod-master1 ~]# kubectl -n mcamel-system get pod mcamel-common-es-cluster-masters-es-data-1 -ojson | jq .spec.volumes[0]
{
  "name": "elasticsearch-data",
  "persistentVolumeClaim": {
    "claimName": "elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1"
  }
}

[root@prod-master1 ~]# kubectl -n mcamel-system get pvc elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1
NAME                                                            STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1   Bound    pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c   35Gi       RWO            hwameistor-storage-lvm-hdd   17h
[root@prod-master1 ~]# kubectl -n mcamel-system get pv pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                                                         STORAGECLASS                 REASON   AGE
pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c   35Gi       RWO            Delete           Bound    mcamel-system/elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1   hwameistor-storage-lvm-hdd            17h
```

根据以上信息确认`PV` 为 `pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c`

### 停止 common-es

停止 `common-es` 主要是 2 条动作：先停止 `operator`, 再停止 `es`

```bash
[root@prod-master1 ~]# kubectl -n mcamel-system get sts
NAME                                       READY   AGE
elastic-operator                           2/2     20h
mcamel-common-es-cluster-masters-es-data   3/3     20h
mcamel-common-kpanda-mysql-cluster-mysql   2/2     20h
mcamel-common-minio-cluster-pool-0         1/1     20h
mcamel-common-mysql-cluster-mysql          2/2     20h
mysql-operator                             1/1     20h
rfr-mcamel-common-redis-cluster            3/3     20h
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts elastic-operator
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts mcamel-common-es-cluster-masters-es-data
# --- wait about 3 mins ----
[root@prod-master1 ~]# kubectl -n mcamel-system get sts
NAME                                       READY   AGE
elastic-operator                           0/0     20h
mcamel-common-es-cluster-masters-es-data   0/0     20h
mcamel-common-kpanda-mysql-cluster-mysql   2/2     20h
mcamel-common-minio-cluster-pool-0         1/1     20h
mcamel-common-mysql-cluster-mysql          2/2     20h
mysql-operator                             1/1     20h
rfr-mcamel-common-redis-cluster            3/3     20h
```

> 以下是命令演示

[![asciicast](https://asciinema.org/a/581583.svg)](https://asciinema.org/a/581583)](https://asciinema.org/a/NUqARym7BTS8BpudRpbmjroFz)

### 建立迁移任务

具体文档可以参考 `Hwameistor` 官方文档： <https://hwameistor.io/docs/quick_start/create_stateful/advanced/migrate>

```bash
[root@prod-master1 ~]# cat migrate.yaml
apiVersion: hwameistor.io/v1alpha1
kind: LocalVolumeMigrate
metadata:
  namespace: hwameistor
  name: migrate-es-pvc # 任务名称
spec:
  sourceNode: prod-worker3 # 来源 node，可以通过 `kubectl get ldn` 获取
  targetNodesSuggested:
  - prod-master3
  volumeName: pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c # 需要迁移的 pvc
  migrateAllVols: false
```

### 执行迁移命令

此时会在命名空间为 `hwameistor` 创建一个 `pod`，用于执行迁移动作：

```bash
[root@prod-master1 ~]# kubectl apply -f migrate.yaml
```

查看迁移状态

```bash
[root@prod-master1 ~]# kubectl get localvolumemigrates.hwameistor.io  migrate-es-pvc -o yaml
apiVersion: hwameistor.io/v1alpha1
kind: LocalVolumeMigrate
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"hwameistor.io/v1alpha1","kind":"LocalVolumeMigrate","metadata":{"annotations":{},"name":"migrate-es-pvc"},"spec":{"migrateAllVols":false,"sourceNode":"prod-worker3","targetNodesSuggested":["prod-master3"],"volumeName":"pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c"}}
  creationTimestamp: "2023-04-30T12:24:17Z"
  generation: 1
  name: migrate-es-pvc
  resourceVersion: "1141529"
  uid: db3c0df0-57b5-42ef-9ec7-d8e6de487767
spec:
  abort: false
  migrateAllVols: false
  sourceNode: prod-worker3
  targetNodesSuggested:
  - prod-master3
  volumeName: pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c
status:
  message: 'waiting for the sync job to complete: migrate-es-pvc-datacopy-elasticsearch-data-mcamel'
  originalReplicaNumber: 1
  state: SyncReplica
  targetNode: prod-master3

```

等到迁移状态为完成后，查看迁移结果。

```bash
[root@prod-master1 ~]# kubectl get lvr
NAME CAPACITY NODE STATE SYNCED DEVICE AGE  
pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 37580963840 prod-master3 Ready true /dev/LocalStorage_PoolHDD/pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 129s  
```

## 恢复 common-es

同样，按照停止顺序来恢复即可。

```bash
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts elastic-operator
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts mcamel-common-es-cluster-masters-es-data
```
