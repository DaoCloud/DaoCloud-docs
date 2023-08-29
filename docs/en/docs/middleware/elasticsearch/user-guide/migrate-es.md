# Elasticsearch migration practice based on Hwameistor

## introduce

The characteristics of K8s, after the stateful application is deployed, whether it can be shifted depends on the underlying `CSI` capability. When `Hwameistor` is used as `CSI`, the application does not have the ability to cross Node.

However, when our initial cluster resources may have some unexpected situations such as unevenness, some stateful applications need to be migrated.

This article is about: When using `Hwameistor`, if you want to migrate the data service middleware, this article takes `Elasticsearch` as an example; at the same time, refer to the migration guide officially provided by `Hwameistor` to demonstrate the migration process.

## Experimental scene introduction

The basic information of this experiment is summarized as follows

### Cluster basic information

```bash
[root@prod-master1 ~]# kubectl get node
NAME STATUS ROLES AGE VERSION
prod-master1 Ready control-plane 15h v1.25.4
prod-master2 Ready control-plane 15h v1.25.4
prod-master3 Ready control-plane 15h v1.25.4
prod-worker1 Ready <none> 15h v1.25.4
prod-worker2 Ready <none> 15h v1.25.4
prod-worker3 Ready <none> 15h v1.25.4
```

### Basic information about ES installation

```bash
[root@prod-master1 ~]# kubectl get pods -o wide | grep es-cluster-masters-es-data

mcamel-common-es-cluster-masters-es-data-0 Running prod-worker1
mcamel-common-es-cluster-masters-es-data-1 Running prod-worker3
mcamel-common-es-cluster-masters-es-data-2 Running prod-worker2
```

### Get the pvc information used by es

```bash
kubectl -n mcamel-system get pvc -l elasticsearch.k8s.elastic.co/statefulset-name=mcamel-common-es-cluster-masters-es-data
NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGE CLASS AGE
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-0 Bound pvc-61776435-0df5-448f-abb9-4d06774ec0e8 35Gi RWO hwameistor-storage-lvm-hdd 15h
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1 Bound pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 35Gi RWO hwameistor-storage-lvm-hdd 15h
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-2 Bound pvc-955bd221-3e83-4bb5-b842-c11584bced10 35Gi RWO hwameistor-storage-lvm-hdd 15h
```

## Experiment Objectives

Migrate `mcamel-common-es-cluster-masters-es-data-1` (hereafter referred to as `esdata-1`) on `prod-worker3` to `prod-master3`

## Preparation

### Confirm that the PV needs to be migrated

Make sure that the `PV` disk corresponding to `esdata-1` is the one

```bash
[root@prod-master1 ~]# kubectl -n mcamel-system get pod mcamel-common-es-cluster-masters-es-data-1 -ojson | jq .spec.volumes[0]
{
  "name": "elasticsearch-data",
  "persistentVolumeClaim": {
    "claimName": "elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1"
  }
}

[root@prod-master1 ~]# kubectl -n mcamel-system get pvc elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1
NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGE CLASS AGE
elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1 Bound pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 35Gi RWO hwameistor-storage-lvm-hdd 17h
[root@prod-master1 ~]# kubectl -n mcamel-system get pv pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c
NAME CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM STORAGE CLASS REASON AGE
pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 35Gi RWO Delete Bound mcamel-system/elasticsearch-data-mcamel-common-es-cluster-masters-es-data-1 hwameistor-storage-lvm-hdd 17h
```

According to the above information, it is confirmed that `PV` is `pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c`

### stop common-es

Stopping `common-es` is mainly 2 actions: first stop `operator`, then stop `es`

```bash
[root@prod-master1 ~]# kubectl -n mcamel-system get sts
NAME READY AGE
elastic-operator 2/2 20h
mcamel-common-es-cluster-masters-es-data 3/3 20h
mcamel-common-kpanda-mysql-cluster-mysql 2/2 20h
mcamel-common-minio-cluster-pool-0 1/1 20h
mcamel-common-mysql-cluster-mysql 2/2 20h
mysql-operator 1/1 20h
rfr-mcamel-common-redis-cluster 3/3 20h
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts elastic-operator
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=0 sts mcamel-common-es-cluster-masters-es-data
# --- wait about 3 mins ----
[root@prod-master1 ~]# kubectl -n mcamel-system get sts
NAME READY AGE
elastic-operator 0/0 20h
mcamel-common-es-cluster-masters-es-data 0/0 20h
mcamel-common-kpanda-mysql-cluster-mysql 2/2 20h
mcamel-common-minio-cluster-pool-0 1/1 20h
mcamel-common-mysql-cluster-mysql 2/2 20h
mysql-operator 1/1 20h
rfr-mcamel-common-redis-cluster 3/3 20h
```

> The following is a demonstration of the command

[![asciicast](https://asciinema.org/a/581583.svg)](https://asciinema.org/a/581583)](https://asciinema.org/a/NUqARym7BTS8BpudRpbmjroFz)

### Create a migration task

For specific documents, please refer to `Hwameistor` official documentation: <https://hwameistor.io/docs/quick_start/create_stateful/advanced/migrate>

```bash
[root@prod-master1 ~]# cat migrate.yaml
apiVersion: hwameistor.io/v1alpha1
kind:LocalVolumeMigrate
metadata:
  namespace: hwameistor
  name: migrate-es-pvc # task name
spec:
  sourceNode: prod-worker3 # source node, can be obtained through `kubectl get ldn`
  targetNodesSuggested:
  -prod-master3
  volumeName: pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c # pvc that needs to be migrated
  migrateAllVols: false
```

### Run the migration command

At this point, a `pod` will be created for `hwameistor` in the namespace to perform the migration action:

```bash
[root@prod-master1 ~]# kubectl apply -f migrate.yaml
```

View migration status

```bash
[root@prod-master1 ~]# kubectl get localvolumemigrates.hwameistor.io migrate-es-pvc -o yaml
apiVersion: hwameistor.io/v1alpha1
kind:LocalVolumeMigrate
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"hwameistor.io/v1alpha1","kind":"LocalVolumeMigrate","metadata":{"annotations":{},"name":"migrate-es-pvc"},"spec": {"migrateAllVols": false,"sourceNode":"prod-worker3","targetNodesSuggested":["prod-master3"],"volumeName":"pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c"}}
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
  -prod-master3
  volumeName: pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c
status:
  message: 'waiting for the sync job to complete: migrate-es-pvc-datacopy-elasticsearch-data-mcamel'
  originalReplicaNumber: 1
  state: SyncReplica
  targetNode: prod-master3

```

Wait until the migration status is complete to view the migration results.

```bash
[root@prod-master1 ~]# kubectl get lvr
NAME CAPACITY NODE STATE SYNCED DEVICE AGE
pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 37580963840 prod-master3 Ready true /dev/LocalStorage_PoolHDD/pvc-7d4c45c9-49d6-4684-aca2-8b853d0c335c 129s
```

## restore common-es

Similarly, it is enough to resume in the order of stopping.

```bash
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=2 sts elastic-operator
[root@prod-master1 ~]# kubectl -n mcamel-system scale --replicas=3 sts mcamel-common-es-cluster-masters-es-data
```

## Privilege Restoration

Since HwameiStor uses rclone to migrate PV, rclone may lose permissions during migration (see [rclone#1202](https://github.com/rclone/rclone/issues/1202) and [hwameistor#830](https: //github.com/hwameistor/hwameistor/issues/830)).

The specific phenomenon on es is that es keeps failing to start repeatedly. Use the following command to view pod logs:
```bash
kubectl -n mcamel-system logs mcamel-common-es-cluster-masters-es-data-0 -c elasticsearch
```

The log contains the following error messages:
``` log
java.lang.IllegalStateException: failed to obtain node locks, tried [[/usr/share/elasticsearch/data]]] with lock id [0]; maybe these locations are not writable or multiple nodes were started without increasing [node.max_local_storage_nodes ] (was [1])?
```

At this time, we need to use the following command to modify the CR of es:
```bash
kubectl -n mcamel-system edit elasticsearches.elasticsearch.k8s.elastic.co mcamel-common-es-cluster-masters
```

Add an initcontainer to the pod of es. The content of the initcontainer is as follows:
```yaml
        - command:
          -sh
          - -c
          - chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/data
          name: change-permission
          resources: {}
          securityContext:
            privileged: true
```

Its location in CR is as follows:
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
          -sh
          - -c
          - sysctl -w vm.max_map_count=262144
          name: sysctl
          resources: {}
          securityContext:
            privileged: true
        - command:
          -sh
          - -c
          - chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/data
          name: change-permission
          resources: {}
          securityContext:
            privileged: true
```