---
MTPE: WANG0608GitHub
Date: 2024-09-10
hide:
  - toc
---

# FAQs

This page lists some questions, answers, and solutions that may arise during the use of HwameiStor local storage.

## How does the HwameiStor scheduler work in the Kubernetes platform?

The HwameiStor scheduler is deployed as a pod in the HwameiStor namespace.

![img](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/img/clip_image002.png)

When an application (Deployment or StatefulSet) is created, the pods of the application are automatically deployed
to worker nodes that have been configured with HwameiStor local storage capability.

## How does HwameiStor handle scheduling for applications with multiple replicas?

Some users may want to understand the scheduling methods used for applications with replicas and how they differ from traditional shared storage systems.

HwameiStor recommends using StatefulSet for applications with multiple replicas.

StatefulSet deploys the replicated replicas to the same worker node, but creates a proper PV volume for each pod
replica. If you need to deploy replicas to different nodes to distribute the workload, you need to manually configure using `podaffinity` .

![img](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/img/clip_image004.png)

Deployment cannot share block volumes, so it is recommended to use a single replica.

For traditional shared storage:

StatefulSet deploys the replicated replicas to different nodes to distribute the workload, but creates a proper
PV volume for each pod replica. Only when the number of replicas exceeds the number of worker nodes will multiple
replicas be on the same node.

Deployment deploys the replicated replicas to different nodes to distribute the workload, and all pods share one
PV volume (currently only NFS is supported). Only when the number of replicas exceeds the number of Worker nodes
will multiple replicas be on the same node. For block storage, since the volume cannot be shared, it is recommended
to use a single replica.

## How is a volume on a Kubernetes node maintained?

HwameiStor provides volume eviction and migration features. When removing or restarting a Kubernetes node, the pods
and volumes on that node can be automatically migrated to other available nodes, ensuring that the pods continue to
run and provide services.

## Removing a node

To ensure the continuous operation of pods and the availability of HwameiStor local data, before removing a Kubernetes
node, you need to migrate the pods and local volumes on that node to other available nodes. This can be done through
the following steps:

1. Drain the node

    ```bash
    kubectl drain NODE --ignore-daemonsets=true --ignore-daemonsets=true
    ```

    This command will evict the pods on the node and reschedule them. It will also trigger the HwameiStor volume eviction
    behavior automatically. HwameiStor will automatically migrate all volume replicas on the node to other nodes and ensure
    that the data remains available.

2. Check the migration progress

    ```bash
    kubectl get localstoragenode NODE -o yaml
    ```

    ```yaml
    apiVersion: hwameistor.io/v1alpha1
    kind: LocalStorageNode
    metadata:
      name: NODE
    spec:
      hostname: NODE
      storageIP: 10.6.113.22
      topogoly:
        region: default
        zone: default
    status:
      ...
      pools:
        LocalStorage_PoolHDD:
          class: HDD
          disks:
          - capacityBytes: 17175674880
            devPath: /dev/sdb
            state: InUse
            type: HDD
          freeCapacityBytes: 16101933056
          freeVolumeCount: 999
          name: LocalStorage_PoolHDD
          totalCapacityBytes: 17175674880
          totalVolumeCount: 1000
          type: REGULAR
          usedCapacityBytes: 1073741824
          usedVolumeCount: 1
          volumeCapacityBytesLimit: 17175674880
         volumes:  # (1)!
      state: Ready
    ```

    1. Ensure that the volumes field is empty

    At the same time, HwameiStor will automatically reschedule the evicted pods and schedule them to nodes with available
    volumes, ensuring that the pods run normally.

3. Remove the node from the cluster

    ```bash
    kubectl delete nodes NODE
    ```

## Restarting a node

Restarting a node usually takes a long time to restore the node to normal. During this time, all pods and local data on
that node cannot run normally. This can be a significant cost, or even unacceptable, for some applications such as databases.

HwameiStor can immediately schedule pods to other available nodes that have volumes and keep them running continuously.
For pods that use HwameiStor multi-replica volumes, this process is very fast, taking about 10 seconds (subject to the
native scheduling mechanism of Kubernetes). For pods that use single-replica volumes, the time required depends on the
time required for volume migration, which is affected by the size of user data.

If you want to keep the volumes on the node and still be able to access them after the node restarts, you can add the
following label to the node to prevent the system from migrating the volumes on that node. The system will still immediately
schedule pods to other nodes that have replicas of the volumes.

1. Add a label (optional)

    If you don't need to migrate the volumes during the node restart, you can add the following label to the node before draining it:

    ```bash
    kubectl label node NODE hwameistor.io/eviction=disable
    ```

2. Drain the node

    ```bash
    kubectl drain NODE --ignore-daemonsets=true --ignore-daemonsets=true
    ```

    - If you performed step 1, you can restart the node after step 2 is successful.
    - If you didn't perform step 1, after step 2 is successful, you should check if the data migration is completed
      (same as step 2 in [Remove a node](#removing-a-node)). After the data migration is completed, you can restart
      the node.

    After the first two steps are successful, you can restart the node and wait for the node system to return to normal.

3. Uncordon the node to restore it to normal in Kubernetes

    ```bash
    kubectl uncordon NODE
    ```

## For traditional shared storage

StatefulSet deploys the replicated replicas to different nodes to distribute the workload, but creates a proper PV volume
for each pod replica. Only when the number of replicas exceeds the number of Worker nodes will multiple replicas be on
the same node.

Deployment deploys the replicated replicas to different nodes to distribute the workload, and all pods share one PV volume
(currently only NFS is supported). Only when the number of replicas exceeds the number of Worker nodes will multiple replicas
be on the same node. For block storage, since the volumes cannot be shared, it is recommended to use a single replica.

## How to handle the error when viewing LocalStorageNode?

When viewing `LocalStorageNode`, if you encounter the following error:

![faq_04](../images/faq4.png)

Possible causes of the error:

1. The LVM2 package is not installed on the node. You can install it with the following command:

    ```bash
    rpm -qa | grep lvm2 # (1)!
    yum install lvm2    # (2)!
    ```

    1. Check if LVM2 is installed
    2. Install LVM2 on each node

2. Check if the proper disk has GPT partition:

    ```bash
    blkid /dev/sd*     # (1)!
    wipefs -a /dev/sd* # (2)!
    ```

    1. Check if the disk has clean partitions
    2. Clean the disk

## Why were no StorageClasses automatically created after installing hwameistor-operator?

Possible reasons:

1. There are no remaining bare disks on the nodes that can be automatically managed. You can check with the following command:

    ```bash
    kubectl get ld # (1)!
    kubectl get lsn <node-name> -o yaml # (2)!
    ```

    1. Check the disks
    2. Check if the disks are properly managed

2. The Hwameistor-related components (excluding drbd-adapter) are not working properly. You can check with the following command:

    ```bash
    kubectl get pod -n hwameistor # (1)!
    kubectl get hmcluster -o yaml # (2)!
    ```

    1. Check if the pods are running properly
    2. Check the health field

    !!! note
        
        The drbd-adapter component only takes effect when HA is enabled. If it is not enabled, you can ignore the related errors.