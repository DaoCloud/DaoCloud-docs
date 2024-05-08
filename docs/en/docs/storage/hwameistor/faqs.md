---
hide:
  - toc
---

# FAQs

**Question 1: How does the HwameiStor local storage scheduler work in a Kubernetes cluster?**

The HwameiStor scheduler is deployed as a Pod in the HwameiStor namespace.

![img](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/img/clip_image002.png)

When an application (Deployment or StatefulSet) is created, the Pods of the application are automatically deployed to worker nodes that have been configured with HwameiStor local storage capability.

**Question 2: How does HwameiStor handle scheduling for applications with multiple replicas? How is it different from traditional shared storage?**

HwameiStor recommends using StatefulSet for applications with multiple replicas.

StatefulSet deploys the replicated replicas to the same worker node, but creates a corresponding PV volume for each Pod replica. If you need to deploy replicas to different nodes to distribute the workload, you need to manually configure pod affinity.

![img](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/img/clip_image004.png)

Deployment cannot share block volumes, so it is recommended to use a single replica.

For traditional shared storage:

StatefulSet deploys the replicated replicas to different nodes to distribute the workload, but creates a corresponding PV volume for each Pod replica. Only when the number of replicas exceeds the number of worker nodes will multiple replicas be on the same node.

Deployment deploys the replicated replicas to different nodes to distribute the workload, and all Pods share one PV volume (currently only NFS is supported). Only when the number of replicas exceeds the number of worker nodes will multiple replicas be on the same node. For block storage, since the volume cannot be shared, it is recommended to use a single replica.

**Question 3: How do I maintain a Kubernetes node?**

HwameiStor provides volume eviction and migration functionality. When removing or restarting a Kubernetes node, the Pods and volumes on that node can be automatically migrated to other available nodes, ensuring that the Pods continue to run and provide services.

**Removing a Node**

To ensure the continuous operation of Pods and the availability of HwameiStor local data, before removing a Kubernetes node, you need to migrate the Pods and local volumes on that node to other available nodes. This can be done through the following steps:

1. Drain the node

    ```bash
    kubectl drain NODE --ignore-daemonsets=true --ignore-daemonsets=true
    ```

    This command will evict the Pods on the node and reschedule them. It will also trigger the HwameiStor volume eviction behavior automatically. HwameiStor will automatically migrate all volume replicas on the node to other nodes and ensure that the data remains available.

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

    At the same time, HwameiStor will automatically reschedule the evicted Pods and schedule them to nodes with available volumes, ensuring that the Pods run normally.

3. Remove the node from the cluster

    ```bash
    kubectl delete nodes NODE
    ```

**Restarting a Node**

Restarting a node usually takes a long time to restore the node to normal. During this time, all Pods and local data on that node cannot run normally. This can be a significant cost, or even unacceptable, for some applications such as databases.

HwameiStor can immediately schedule Pods to other available nodes that have volumes and keep them running continuously. For Pods that use HwameiStor multi-replica volumes, this process is very fast, taking about 10 seconds (subject to the native scheduling mechanism of Kubernetes); for Pods that use single-replica volumes, the time required depends on the time required for volume migration, which is affected by the size of user data.

If you want to keep the volumes on the node and still be able to access them after the node restarts, you can add the following label to the node to prevent the system from migrating the volumes on that node. The system will still immediately schedule Pods to other nodes that have replicas of the volumes.

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
    - If you didn't perform step 1, after step 2 is successful, you should check if the data migration is completed (same as step 2 in "Removing a Node"). After the data migration is completed, you can restart the node.

    After the first two steps are successful, you can restart the node and wait for the node system to return to normal.

3. Uncordon the node to restore it to normal in Kubernetes

    ```bash
    kubectl uncordon NODE
    ```

**For traditional shared storage**

StatefulSet deploys the replicated replicas to different nodes to distribute the workload, but creates a corresponding PV volume for each Pod replica. Only when the number of replicas exceeds the number of worker nodes will multiple replicas be on the same node.

Deployment deploys the replicated replicas to different nodes to distribute the workload, and all Pods share one PV volume (currently only NFS is supported). Only when the number of replicas exceeds the number of worker nodes will multiple replicas be on the same node. For block storage, since the volumes cannot be shared, it is recommended to use a single replica.

**Question 4: How to handle the error when viewing LocalStorageNode?**

When viewing `LocalStorageNode`, if you encounter the following error:

![faq_04](img/faq04.png)

Possible causes of the error:

1. The LVM2 package is not installed on the node. You can install it with the following command:

    ```bash
    rpm -qa | grep lvm2 # (1)!
    yum install lvm2    # (2)!
    ```

    1. Check if LVM2 is installed
    2. Install LVM2 on each node

2. Check if the corresponding disk has GPT partition:

    ```bash
    blkid /dev/sd*     # (1)!
    wipefs -a /dev/sd* # (2)!
    ```

    1. Check if the disk has clean partitions
    2. Clean the disk

**Question 5: Why were no StorageClasses automatically created after installing Hwameistor-operator?**

Possible reasons:

1. There are no remaining bare disks on the nodes that can be automatically managed. You can check with the following command:

    ```bash
    kubectl get ld # (1)!
    kubectl get lsn <node-name> -o yaml # (2)!
    ```

    1. Check the disks
    2. Check if the disks are properly managed

2. The Hwameistor-related components (excluding drbd-adapter) are not working properly. You can check with the following command:

    > The drbd-adapter component only takes effect when HA is enabled. If it is not enabled, you can ignore the related errors.

    ```bash
    kubectl get pod -n hwameistor # (1)!
    kubectl get hmcluster -o yaml # (2)!
    ```

    1. Check if the pods are running properly
    2. Check the health field
