# Volume migration

`Migrate` migration feature is an important operation and maintenance management feature in HwameiStor. When the copy of the node where the data volume bound to the application is located is damaged, the copy of the volume can be migrated to other nodes, and the application will be rescheduled after successfully migrating to the new node to the new node, and bind mount the data volume.

## Basic concept

`LocalVolumeGroup(LVG)` (data volume group) management is an important feature in HwameiStor. When the application Pod applies for multiple data volumes `PVC`, in order to ensure the correct operation of the Pod, these data volumes must have certain attributes, such as: the number of copies of the data volume, and the node where the copies are located. It is a very important capability in HwameiStor to correctly manage these associated data volumes through the data volume group management function.

## Prerequisites

LocalVolumeMigrate needs to be deployed in the Kubernetes system, and the deployment application needs to meet the following conditions:

* Support for lvm type volumes
* convertible type volume (need to add ConfigMap convertible: true in sc)
    * When the application Pod applies for multiple data volume PVCs, the corresponding data volumes need to use the same configuration sc
    * When migrating based on LocalVolume granularity, data volumes belonging to the same LocalVolumeGroup will not be migrated together by default (if they are migrated together, you need to configure the switch MigrateAllVols: true)

## Step 1: Create convertible `StorageClass`

```console
cd ../../deploy/
kubectl apply -f storageclass-convertible-lvm.yaml
```

## Step 2: Create multiple `PVC`

```console
kubectl apply -f pvc-multiple-lvm.yaml
```

## Step 3: Deploy the multi-volume Pod

```console
kubectl apply -f nginx-multiple-lvm.yaml
```

## Step 4: Unmount the multi-volume Pod

```console
kubectl patch deployment nginx-local-storage-lvm --patch '{"spec": {"replicas": 0}}' -n hwameistor
```

## Step 5: Create the migration task

```console
cat > ./migrate_lv.yaml <<- EOF
apiVersion: hwameistor.io/v1alpha1
kind:LocalVolumeMigrate
metadata:
  namespace: hwameistor
  name: <localVolumeMigrateName>
spec:
  targetNodesNames:
  - <targetNodesName1>
  - <targetNodesName2>
  sourceNodesNames:
  - <sourceNodesName1>
  - <sourceNodesName2>
  volumeName: <volName>
  migrateAllVols: <true/false>
EOF
```

```console
kubectl apply -f ./migrate_lv.yaml
```

## Step 6: View Migration Status

```console
$ kubectl get LocalVolumeMigrate -o yaml
apiVersion: v1
items:
- apiVersion: hwameistor.io/v1alpha1
  kind:LocalVolumeMigrate
  metadata:
  annotations:
  kubectl.kubernetes.io/last-applied-configuration: |
  {"apiVersion":"hwameistor.io/v1alpha1","kind":"LocalVolumeMigrate","metadata":{"annotations":{},"name":"localvolumemigrate-1","namespace":"hwameistor" },"spec":{"migrateAllVols":true,"sourceNodesNames":["dce-172-30-40-61"],"targetNodesNames":["172-30-45-223"],"volumeName" :"pvc-1a0913ac-32b9-46fe-8258-39b4e3b696a4"}}
  creationTimestamp: "2022-07-07T12:34:31Z"
  generation: 1
  name: localvolumemigrate-1
  namespace: hwameistor
  resourceVersion: "12828637"
  uid: 78af7f1b-d701-4b03-84de-27fafca58764
  spec:
  abort: false
  migrateAllVols: true
  sourceNodesNames:
  -dce-172-30-40-61
    targetNodesNames:
  - 172-30-45-223
    volumeName: pvc-1a0913ac-32b9-46fe-8258-39b4e3b696a4
    status:
    replicaNumber: 1
    state: InProgress
    kind: List
    metadata:
    resourceVersion: ""
    selfLink: ""
```

## Step 7: View migration success status

```console
[root@172-30-45-222 deploy]# kubectl get lvr
NAME CAPACITY NODE STATE SYNCED DEVICE AGE
pvc-1a0913ac-32b9-46fe-8258-39b4e3b696a4-9cdkkn 1073741824 172-30-45-223 Ready true /dev/LocalStorage_PoolHDD-HA/pvc-1a0913ac-32b9-46fe-8258-39b4e4e3b79
pvc-d9d3ae9f-64af-44de-baad-4c69b9e0744a-7ppmrx 1073741824 172-30-45-223 Ready true /dev/LocalStorage_PoolHDD-HA/pvc-d9d3ae9f-64af-44de-baad-4c69b9e7s744a 7
```

## Step 8: After successful migration, remount the data volume Pod

```console
kubectl patch deployment nginx-local-storage-lvm --patch '{"spec": {"replicas": 1}}' -n hwameistor
```
