# 基于 Hwameistor 的 Elasticsearch 迁移实践

由于 Kubernetes 自身的特性，有状态应用部署完成后是否可以迁移取决于底层 __CSI__ 的能力。<!--使用 [Hwameistor](../../../storage/index.md) 作为 __CSI__ 时，不支持跨节点迁移应用。-->然而当集群出现资源不均等意外情况时，需要跨节点迁移相关的有状态应用。

本文以 __Elasticsearch__ 为例，参考 [Hwameistor](../../../storage/index.md) 官方提供的迁移指南，演示使用 __Hwameistor__ 时如何跨节点迁移数据服务中间件。

## 演示环境

从集群信息、ES 安装信息、PVC 三方面进行介绍演示环境：

=== "集群信息"

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

=== "ES 安装信息"

    ```bash
    [root@prod-master1 ~]# kubectl get pods -o wide | grep es-cluster-masters-es-data

    mcamel-common-es-cluster-masters-es-data-0 Running prod-worker1
    mcamel-common-es-cluster-masters-es-data-1 Running prod-worker3
    mcamel-common-es-cluster-masters-es-data-2 Running prod-worker2
    ```

=== "ES 使用的 PVC"

    ```bash
    kubectl -n mcamel-system get pvc -l elasticsearch.k8s.elastic.co/statefulset-name=mcamel-common-es-cluster-masters-es-data
    NAME                                                            STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE
    elasticsearch-data-mcamel-common-es-cluster-masters-es-data-0   Bound    pvc-61776435-0df5-448f-abb9-4d06774ec0e8   35Gi       RWO            hwameistor-storage-lvm-hdd   15h
    elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1   Bound    pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c   35Gi       RWO            hwameistor-storage-lvm-hdd   15h
    elasticsearch-data-mcamel-common-es-cluster-masters-es-data-2   Bound    pvc-955bd221-3e83-4bb5-b842-c11584bced10   35Gi       RWO            hwameistor-storage-lvm-hdd   15h
    ```

## 演示目标

将 __prod-worker3__ 节点上的 __mcamel-common-es-cluster-masters-es-data-1__ （以下简称 __演示应用__ / __esdata-1__ ）有状态应用跨节点迁移到 __prod-master3__ 节点。

## 准备工作

### 确定需要迁移的 PV

使用如下命令查找演示应用 __esdata-1__ 对应的 __PV__ 磁盘，明确需要迁移哪个 __PV__ 。

1. 查看演示应用绑定的 PVC

    ```bash
    [root@prod-master1 ~]# kubectl -n mcamel-system get pod mcamel-common-es-cluster-masters-es-data-1 -ojson | jq .spec.volumes[0]
    {
      "name": "elasticsearch-data",
      "persistentVolumeClaim": {
        "claimName": "elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1"
      }
    }
    ```

2. 查看该 PVC 绑定的 PV

    ```
    [root@prod-master1 ~]# kubectl -n mcamel-system get pvc elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1
    NAME                                                            STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE
    elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1   Bound    pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c   35Gi       RWO            hwameistor-storage-lvm-hdd   17h
    ```

3. 确认该 PV 绑定的应用是否为需要迁移的应用，即此文中的演示应用 __esdata-1__ 

    [root@prod-master1 ~]# kubectl -n mcamel-system get pv pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c
    NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                                                         STORAGECLASS                 REASON   AGE
    pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c   35Gi       RWO            Delete           Bound    mcamel-system/elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1   hwameistor-storage-lvm-hdd            17h
    ```

上述信息证明，需要迁移的 __PV__ 为 __pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c__ 。

### 停止运行待迁移应用

1. 查看当前正在运行的应用

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
    ```

2. 停止运行 ES operator

    ```
    [root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts elastic-operator
    ```

3. 停止运行 ES：

    ```
    [root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts mcamel-common-es-cluster-masters-es-data
    # --- wait about 3 mins ----
    ```

4. 确认 ES 已经停止运行

    ```
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

视频演示如下：

[![asciicast](https://asciinema.org/a/581583.svg)](https://asciinema.org/a/581583)

## 开始迁移

有关此过程的详细说明，可参考 __Hwameistor__ 官方文档：[迁移数据卷](https://hwameistor.io/docs/quick_start/create_stateful/advanced/migrate)

1. 建立迁移任务

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

2. 执行迁移命令

    ```bash
    [root@prod-master1 ~]# kubectl apply -f migrate.yaml
    ```

    此时会在 __hwameistor__ 命名空间创建一个 __pod__ ，用于执行迁移动作。

3. 查看迁移状态

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

4. 迁移完成后，查看迁移结果

    ```bash
    [root@prod-master1 ~]# kubectl get lvr
    NAME CAPACITY NODE STATE SYNCED DEVICE AGE  
    pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 37580963840 prod-master3 Ready true /dev/LocalStorage_PoolHDD/pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 129s  
    ```

## 恢复 common-es

1. 启动 ES operator

    ```bash
    [root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=2 sts elastic-operator
    ```

2. 启动 ES

    ```[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=3 sts mcamel-common-es-cluster-masters-es-data
    ```

## 相关问题

HwameiStor 使用 rclone 来迁移 PV，而 rclone 在迁移过程中可能会丢失权限（参考 [rclone#1202](https://github.com/rclone/rclone/issues/1202) 和 [hwameistor#830](https://github.com/hwameistor/hwameistor/issues/830)）。如果权限丢失，ES 会启动失败并反复启动，陷入恶性循环。

遇到类似问题时可以通过下述步骤排查并解决故障。

### 确认问题

使用以下命令查看 Pod 日志：

``bash
kubectl -n mcamel-system logs mcamel-common-es-cluster-masters-es-data-0 -c elasticsearch
```

如果日志中包含如下错误信息，则可以确认为权限丢失造成的问题。

```log
java.lang.IllegalStateException: failed to obtain node locks, tried [[/usr/share/elasticsearch/data]] with lock id [0]; maybe these locations are not writable or multiple nodes were started without increasing [node.max_local_storage_nodes] (was [1])?
```

### 解决故障

1. 运行下命令修改 ES 的 CR

    ```bash
    kubectl -n mcamel-system edit elasticsearches.elasticsearch.k8s.elastic.co mcamel-common-es-cluster-masters
    ```

2. 为 ES 的 Pod 添加一个 __initcontainer__ ，内容如下：

    ```yaml
            - command:
              - sh
              - -c
              - chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/data
              name: change-permission
              resources: {}
              securityContext:
                privileged: true
    ```

    __initcontainer__ 在 CR 中的位置如下：
    
    ```yaml
    spec:
      ...
      ...
      nodeSets:
      - config:
          node.store.allow_mmap: false
        count: 3
        name: data
        podTemplate:
          metadata: {}
          spec:
            ...
            ...
            initContainers:
            - command:
              - sh
              - -c
              - sysctl -w vm.max_map_count=262144
              name: sysctl
              resources: {}
              securityContext:
                privileged: true
            - command:
              - sh
              - -c
              - chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/data
              name: change-permission
              resources: {}
              securityContext:
                privileged: true
    ```
