
# Jenkins 的高可用性方案

由于jenkins本身的架构设计并不支持多节点的方式，因此不支持以横向扩展的方式来实现高可用，依赖于k8s的故障转移机制，当jenkins pod发生故障时，可以通过k8s的调度机制将pod调度到其他节点上，从而实现高可用。因此jenkins的高可用主要考虑的是数据存储层的高可用。

DCE5.0中，通过使用hwameistor的存储层来实现jenkins的高可用。hwameistor支持使用`DRBD`的方式，可以将一份数据副本同时挂载到多个node节点上，当jenkins所在节点宕机时，通过k8s的调度，可以将pod调度到其他节点上，此时pod依旧可以继续使用之前的数据，以此来实现高可用。

> tips: hwameistor基于DRBD方案实现了存储层的高可用，因此理论上只需要CSI能支持DRBD都能实现高可用，如：Linstor等。

下面将介绍如何基于hwameistor来实现jenkins的高可用。

## 前置条件

- 安装`hwameistor`请看：https://hwameistor.io/cn/docs/intro, 因为高可用至少需要两个节点，因此node数量至少为2个。
- 确保系统中有空闲的，干净的磁盘（磁盘中无数据，无分区信息），否则无法被hwameistor使用。可以通过`kubectl get ld`来查看系统中的磁盘信息。

## 安装步骤

1. 确认有空闲的磁盘

    ```shell
    $ kubectl get ld
    localdisk-f24ee676b24652341ed5d61560b7bb16   controller-node-1   /dev/sdb     Avilaible   Active   51m  # 状态为Avilaible为新加的硬盘，当添加完硬盘之后就能查到
    ```

2. 确认磁盘类型

    ```shell
    $ kubectl get ld localdisk-f24ee676b24652341ed5d61560b7bb16 -o yaml | grep type
    type: HDD  #注意区分是HDD还是SSD
    ```

3. 创建LocalDiskClaim，将磁盘加入到hwameistor的管理中

    ```shell
    > kubectl apply -f - <<EOF
    apiVersion: hwameistor.io/v1alpha1
    kind: LocalDiskClaim
    metadata:
      name: controller-node-1              # 改为当前节点的名称
    spec: 
      nodeName: controller-node-1          # 改为当前节点的名称(kubectl get node)
      owner: local-storage                # owner与disk类型是不同的，只有lvm类型的才支持HA和扩容。注意区分lvm和disk类型
      description:
        diskType: HDD                 # 改为当前节点的磁盘类型
    EOF
    ```

4. 验证是否加入成功

    ```shell
    > kubectl get localstoragenode $nodeName -o yaml
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
      pools:                                 # 出现以下内容代表加入成功
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

5. 修改jenkins的storageClass

    - 通过界面的方式安装的jenkins，可以在安装时设置storageClass(存储类)为`hwameistor-storage-lvm-hdd-ha`.
    - 通过helm安装时，可以设置helm value.yaml中的`storageClassName`改为`hwameistor-storage-lvm-hdd-ha`.

    > 在安装之前确认storageClass是否存在，可以通过`kubectl get sc`查看
    > 一般情况下在安装了hwameistor之后，会自动创建`hwameistor-storage-lvm-hdd-ha`这个storageClass，如果没有，请联系管理员。
    > 根据添加的磁盘类型，也有可能是`hwameistor-storage-lvm-ssd-ha`。只需要指定为ha类型的storageClass即可。

部署完jenkins后即可实现jenkins的高可用功能。

**注意**：不支持已有数据的jenkins直接转为高可用模式，需要重新安装jenkins，请注意备份数据。
