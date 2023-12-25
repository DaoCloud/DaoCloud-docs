# Jenkins High Availability Solution

Due to the architecture design of Jenkins itself, it does not natively support a multi-node setup, making horizontal scaling for high availability unfeasible. However, leveraging Kubernetes' fault tolerance mechanism, when a Jenkins Pod fails, Kubernetes can schedule the Pod onto another node, thus achieving high availability.

Thus, the primary focus for Jenkins high availability is on ensuring high availability at the data storage layer.

In DCE 5.0, Jenkins high availability is achieved by utilizing the storage layer of HwameiStor. HwameiStor supports the use of DRBD (Distributed Replicated Block Device) to mount duplicate data copies simultaneously on multiple nodes. When the node hosting Jenkins goes down, Kubernetes can schedule the Pod onto another node seamlessly, allowing continued access to the previous data and thereby achieving high availability.

!!! tip

    HwameiStor, through its implementation of the DRBD solution, ensures high availability at the storage layer. Therefore, theoretically, any Container Storage Interface (CSI) capable of supporting DRBD, such as Linstor, can enable high availability.

The following section will explain how to achieve Jenkins high availability based on HwameiStor.

## Prerequisites

- To install HwameiStor, please refer to <https://hwameistor.io/cn/docs/intro>.
  At least two nodes are required for high availability.
- Ensure that the system has available and clean disks (disks with no existing data or partition information), as HwameiStor cannot utilize disks that are already in use.
  You can use the __kubectl get ld__ command to view disk information in the system.

## Installation Steps

1. Confirm the availability of disks

    ```shell
    kubectl get ld
    ```

    The output should resemble:

    ```console
    localdisk-f24ee676b24652341ed5d61560b7bb16   controller-node-1   /dev/sdb     Available   Active   51m
    ```

    > New disks will have the status "Available" and can be detected after they are added.

2. Confirm disk type

    ```shell
    kubectl get ld localdisk-f24ee676b24652341ed5d61560b7bb16 -o yaml | grep type
    ```

    The output should resemble:

    ```console
    type: HDD
    ```

    > Pay attention to distinguish between HDD and SSD types.

3. Create a LocalDiskClaim to add the disk to HwameiStor's management.

    ```shell
    > kubectl apply -f - <<EOF
    apiVersion: hwameistor.io/v1alpha1
    kind: LocalDiskClaim
    metadata:
      name: controller-node-1      # Change to the current node's name
    spec:
      nodeName: controller-node-1  # Change to the current node's name (kubectl get node)
      owner: local-storage         # "owner" and "disk" types are different; only LVM types support HA (high availability) and scaling. Differentiate between LVM and disk types.
      description:
        diskType: HDD              # Change to the current node's disk type
    EOF
    ```

4. Verify successful inclusion.

    ```shell
    kubectl get localstoragenode $nodeName -o yaml
    ```

    The output should resemble:

    ```yaml
    apiVersion: hwameistor.io/v1alpha1
    kind: LocalStorageNode
    metadata:
      name: controller-node-1
    spec:
      hostname: controller-node-1
      storageIP: 172.30.47.32
      topogoly:
        region: default
        zone: default
    status:
      conditions:
      - lastTransitionTime: "2023-09-11T06:33:57Z"
        lastUpdateTime: "2023-09-11T06:33:57Z"
        message: Successfully to expand storage capacity
        reason: StorageExpandSuccess
        status: "True"
        type: ExpandSuccess
      poolExtendRecords:
        LocalStorage_PoolHDD:
        - description:
            diskType: HDD
          diskRefs:
          - apiVersion: hwameistor.io/v1alpha1
            kind: LocalDisk
            name: localdisk-6285c10750cc3495c59e4cadf275621b
            resourceVersion: "24961890"
            uid: 3406c479-f4d9-4a94-8d84-69dd6f10f8d3
          nodeName: controller-node-1
          owner: local-storage
      pools: # (1)
        LocalStorage_PoolHDD:
          class: HDD
          disks:
          - capacityBytes: 42945478656
            devPath: /dev/sdc
            state: InUse
            type: HDD
          freeCapacityBytes: 38650511360
          freeVolumeCount: 999
          name: LocalStorage_PoolHDD
          totalCapacityBytes: 42945478656
          totalVolumeCount: 1000
          type: REGULAR
          usedCapacityBytes: 4294967296
          usedVolumeCount: 1
          volumeCapacityBytesLimit: 42945478656
          volumes:
          - pvc-26a63717-8b53-4c37-ad99-6d4394288192
      state: Ready
    ```

    1. If the above content is displayed, it signifies successful inclusion.

5. Modify Jenkins' storageClass

    - For Jenkins installed through the UI, you can set the storageClass (storage class __hwameistor-storage-lvm-hdd-ha__) during installation.
    - For Jenkins installed using Helm, you can set the __storageClassName__ in the Helm __value.yaml__ file to __hwameistor-storage-lvm-hdd-ha__.

    !!! note

        - Before installation, ensure that the storageClass exists by running __kubectl get sc__.
        - Generally, after installing HwameiStor, the __hwameistor-storage-lvm-hdd-ha__ storageClass is automatically created. If it does not exist, please contact the administrator.
        - Depending on the added disk type, it could also be __hwameistor-storage-lvm-ssd-ha__. Just specify a high availability (ha) type storageClass.

Once Jenkins is deployed, Jenkins' high availability functionality will be enabled.

!!! caution

    Existing Jenkins instances with data cannot be directly converted to a high availability mode. Reinstall Jenkins and ensure to backup the data.
