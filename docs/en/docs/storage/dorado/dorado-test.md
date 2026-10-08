---
hide:
  - navigation
---

# Test K8S CSI Driver Dorado Storage

Standardized testing of CSI capabilities and storage container awareness capabilities

Git: <https://gitee.com/daocloud/huawei-dorado-test>

## Test Conclusion

**DaoCloud d.run AI Computing Scheduling Platform (also known as DCE5 v3.0 Cloud Native Container Platform) fully supports all container volume functions of OceanStor Dorado based on "CNCF-CSI standard", and also supports all container volume awareness functions based on "Huawei CSM standard".**

**The above conclusion applies to all models included in HUAWEI OceanStor Dorado V700 All-Flash Storage System and OceanStor Hybrid V700 Hybrid Flash Storage System.**

## Test Environment

| Component | Version |
| ------------------------- | ----------------------------- |
| Storage Model | Huawei OceanStor Dorado 5000 v6 |
| Storage Version | V700R001C00SPC200 |
| d.run | DCE5 v3.0.0 |
| Kubernetes | v1.31.6 |
| CSI Driver | eSDK_K8S_Plugin v4.8.0 |
| Storage Monitoring Container | Huawei CSM v2.3.0 |
| csi-attacher | v4.4.0 |
| csi-node-driver-registrar | v2.9.0 |
| csi-provisioner | v3.6.0 |
| csi-resizer | v1.9.0 |
| csi-snapshotter | v6.3.0 |
| livenessprobe | v2.12.0 |
| snapshot-controller | v6.3.0 |

## Network Topology

![](./images/networking.drawio.svg)

## Driver Download

### oceanctl

The macOS version needs to be compiled directly from the source code

<https://github.com/Huawei/eSDK_K8S_Plugin/blob/master/Makefile>

### CSI Driver

<https://github.com/Huawei/eSDK_K8S_Plugin>

### CSM

<https://github.com/Huawei/csm>

## References

### CSI Plugin Manual

<https://github.com/Huawei/eSDK_K8S_Plugin/tree/master/docs>

### Dorado CSI Best Practices

<https://support.huawei.com/enterprise/zh/doc/EDOC1100306385>

### CDM Manual

<https://github.com/Huawei/csm/tree/main/docs>

## Reference Implementation of NFS CSI

### nfs-subdir-external-provisioner

<https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner>

## Test Process

1. Use a MySQL cluster to mount a storage volume and write the initial database;
2. Perform cloning and snapshot;
3. Then mount the new volume with a new MySQL instance

## Operation Process

The commands have been encapsulated in the [Makefile](https://gitee.com/daocloud/huawei-dorado-test/blob/master/Makefile)

```
# Install CSI
$ make csi

# Install CSM
$ make csm

# Install backend
$ make backend

# Create test
$ make create

# Delete test
$ make delete
```

## Test Results

| Test Item | Method | Result | Remarks |
| ---------- | ------------------------------------------------------ | ------ | --------------------------------- |
| Volume Creation | Dynamically create pvc => pv | Passed | |
| Volume Expansion | Modify pvc capacity online | Passed | |
| Volume Mount 1 | Mount an exclusive RWO volume | Passed | |
| Read/Write IO | Write database data, then read it | Passed | |
| Volume Unmount | Delete the MySQL container, then check with mount -l whether the nfs mount is removed | Passed | |
| Volume Deletion | Delete the PVC and check whether the volume is shown as deleted on the storage UI | Passed | |
| Volume Sharing | Mount a volume across hosts by multiple containers in ReadWriteMany mode | Passed | |
| Volume Snapshot | CSI VolumeSnapShot in conjunction with storage snapshot | Passed | |
| Volume Snapshot Restore | Restore a PVC from a snapshot | Passed | |
| Volume Clone | Clone and copy a PVC | Passed | |
| Tenant Control | Place all volumes in a specific tenant | Passed | |
| Ephemeral Volume | Create a CSI Ephemeral volume | Passed | |
| PV Awareness | The storage side displays the K8S PV | Passed | |
| Pod Awareness | The storage side displays the K8S Pod | Passed\* | Currently, Pods mounting ephemeral volumes cannot be displayed |

## Test Screenshots

### Frontend

#### kubectl

![](./images/cli.png)

#### mount -l

![](./images/nfs.png)

### Backend

#### File System

![](./images/volume.png)

#### Clone

![](./images/clone1.png)
![](./images/clone2.png)

#### Snapshot

![](./images/snapshot.png)

#### PV Awareness

![](./images/pv1.png)
![](./images/pv2.png)

#### Pod Awareness

![](./images/pv1.png)
![](./images/pv2.png)

## FAQs

### How to configure a daocloud tenant

1. Create a daocloud tenant in the backend web UI;
2. Services => Multi-tenancy, daocloud tenant => Summary Information, associate StoragePool001;
3. Services => Network => Logical Port, under the daocloud tenant, configure an independent IP and enable the management URL function;
4. Configure the tenant URL in backends.yaml;

### How to ensure the PV volume file system is generated under the daocloud tenant

In backends.yaml, you need to log in to the tenant using the URL of the tenant logical port. For details, see the difference between backends.yaml and backends_admin.yaml

### How to configure NFS 4.x

Settings => File Service => NFS Service, under the daocloud tenant, enable each 4.x service
Note: The CSI filters StoragePool according to the NFS version in mountOption

### Does CSM need to be configured with a storage backend?

No. It reads the information of storagebackendclaims.xuanwu.huawei.io

## CSM Logs

The CSM container sends PV/POD information to the REST API of the storage

```
$ cat /var/log/huawei-csm/csm-storage-service/cmi-service
2025-08-19 14:30:51.301498 1[requestID:4226085859] [INFO]:  call request POST https://100.115.9.220:8088/deviceManager/rest/2102353SYPFSLC000003/container_pv, request: map[clusterName:dce5 pvName:pvc-b8b2c41c-fc34-4629-ae45-a630e1800ec8

2025-08-19 14:31:20.858171 1[requestID:4042092947] [INFO]:  call request POST https://100.115.9.220:8088/deviceManager/rest/2102353SYPFSLC000003/container_pod, request: map[nameSpace:default podName:mysql-0 resourceId:844 resourceType:40]
```

## Known Issues

### 1. CSM does not support ephemeral volumes

Already submitted to GitHub:
[Need to support monitoring pods that mount ephemeral volumes #1
](https://github.com/Huawei/csm/issues/1)

## Appendix

### CLI Output

#### Script

```
$ make create
kubectl apply -f sc.yaml
storageclass.storage.k8s.io/dorado-nfs created
kubectl apply -f pvc.yaml
persistentvolumeclaim/data-mysql created
kubectl wait pvc/data-mysql \
                --for=jsonpath='{.status.phase}'='Bound' \
                --timeout=600s
persistentvolumeclaim/data-mysql condition met
kubectl apply -f mysql.yaml
statefulset.apps/mysql created
configmap/mysql unchanged
service/mysql created
service/mysql-read created
kubectl rollout status --watch --timeout=600s sts/mysql
Waiting for 3 pods to be ready...
Waiting for 2 pods to be ready...
Waiting for 2 pods to be ready...
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
partitioned roll out complete: 3 new pods have been updated...
kubectl apply -f pvc-expand.yaml
persistentvolumeclaim/data-mysql configured
kubectl wait pvc/data-mysql \
                --for=jsonpath='{.status.capacity.storage}'='2Gi' \
                --timeout=600s
persistentvolumeclaim/data-mysql condition met
kubectl apply -f pvc-clone.yaml
persistentvolumeclaim/data-mysql-clone created
kubectl wait pvc/data-mysql-clone \
                --for=jsonpath='{.status.phase}'='Bound' \
                --timeout=600s
persistentvolumeclaim/data-mysql-clone condition met
kubectl apply -f mysql-clone.yaml
statefulset.apps/mysql-clone created
service/mysql-clone created
service/mysql-clone-read created
kubectl rollout status --watch --timeout=600s sts/mysql-clone
Waiting for 1 pods to be ready...
partitioned roll out complete: 1 new pods have been updated...
kubectl apply -f snapshotclass.yaml
volumesnapshotclass.snapshot.storage.k8s.io/dorado-ssc created
kubectl apply -f snapshot.yaml
volumesnapshot.snapshot.storage.k8s.io/data-mysql-snapshot created
kubectl wait volumesnapshot/data-mysql-snapshot \
                --for=jsonpath='{.status.readyToUse}'=true \
                --timeout=600s
volumesnapshot.snapshot.storage.k8s.io/data-mysql-snapshot condition met
kubectl apply -f mysql-restore.yaml
statefulset.apps/mysql-restore created
service/mysql-restore created
service/mysql-restore-read created
kubectl rollout status --watch --timeout=600s sts/mysql-restore
Waiting for 1 pods to be ready...
partitioned roll out complete: 1 new pods have been updated...
```

#### Instance

```
$ kubectl get po,pvc,volumesnapshot
NAME                  READY   STATUS    RESTARTS        AGE
pod/mysql-0           2/2     Running   0               8m57s
pod/mysql-1           2/2     Running   1 (7m45s ago)   8m12s
pod/mysql-2           2/2     Running   1 (7m11s ago)   7m36s
pod/mysql-clone-0     1/1     Running   0               6m29s
pod/mysql-restore-0   1/1     Running   0               5m45s

NAME                                         STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/data-mysql             Bound    pvc-b8b2c41c-fc34-4629-ae45-a630e1800ec8   2Gi        RWX            dorado-nfs     <unset>                 9m
persistentvolumeclaim/data-mysql-clone       Bound    pvc-52a19048-8e7c-46c8-b82d-01b68ffbdfa1   2Gi        RWX            dorado-nfs     <unset>                 6m59s
persistentvolumeclaim/mysql-restore-0-data   Bound    pvc-66ed9c89-c141-4045-9a05-49f509a1081d   2Gi        RWO            dorado-nfs     <unset>                 5m46s

NAME                                                         READYTOUSE   SOURCEPVC    SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS   SNAPSHOTCONTENT                                    CREATIONTIME   AGE
volumesnapshot.snapshot.storage.k8s.io/data-mysql-snapshot   true         data-mysql                           2Gi           dorado-ssc      snapcontent-857dddba-b266-42d1-a048-aaf6bcaf53f4   17m            5m49s
```

### CSI

```
$ kubectl -n huawei-csi get po
NAME                                     READY   STATUS    RESTARTS   AGE
huawei-csi-controller-6c8c87bc8d-sg7s8   9/9     Running   0          5d21h
huawei-csi-node-9gtsj                    3/3     Running   0          5d21h
```

### CSM

```
$ kubectl -n huawei-csm get po
NAME                                      READY   STATUS    RESTARTS   AGE
csm-prometheus-service-7c79866c7b-9nvpp   3/3     Running   0          6d10h
csm-storage-service-59876749df-58kpk      3/3     Running   0          6d10h
```

### CRDs

```
$ kubectl api-resources --api-group xuanwu.huawei.io
NAME                     SHORTNAMES   APIVERSION            NAMESPACED   KIND
resourcetopologies       rt           xuanwu.huawei.io/v1   false        ResourceTopology
storagebackendclaims     sbc          xuanwu.huawei.io/v1   true         StorageBackendClaim
storagebackendcontents   sbct         xuanwu.huawei.io/v1   false        StorageBackendContent
volumemodifyclaims       vmc          xuanwu.huawei.io/v1   false        VolumeModifyClaim
volumemodifycontents     vmct         xuanwu.huawei.io/v1   false        VolumeModifyContent
```

### mount -l

```
$ mount -l | grep /pvc-b8b2c41c-fc34-4629-ae45-a630e1800ec8/mount
100.115.9.220:/pvc_b8b2c41c_fc34_4629_ae45_a630e1800ec8 on /var/lib/kubelet/pods/83aca192-3c4d-4ed4-812d-aef164b1938c/volumes/kubernetes.io~csi/pvc-b8b2c41c-fc34-4629-ae45-a630e1800ec8/mount type nfs4 (rw,relatime,vers=4.2,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=100.115.8.120,local_lock=none,addr=100.115.9.220)
```
