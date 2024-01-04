# 卷的迁移

`Migrate` 迁移功能是 HwameiStor 中重要的运维管理功能，当应用绑定的数据卷所在节点副本损坏时，
卷副本可以通过迁移到其他节点，并在成功迁移到新节点后，将应用重新调度到新节点，并进行数据卷的绑定挂载。

## 基本概念

`LocalVolumeGroup(LVG)`（数据卷组）管理是 HwameiStor 中重要的一个功能。当应用 Pod 申请多个数据卷 `PVC` 时，
为了保证 Pod 能正确运行，这些数据卷必须具有某些相同属性，例如：数据卷的副本数量，副本所在的节点。
通过数据卷组管理功能正确地管理这些相关联的数据卷，是 HwameiStor 中非常重要的能力。

## 前提条件

LocalVolumeMigrate 需要部署在 Kubernetes 系统中，需要部署应用满足下列条件：

* LVM2 已安装，支持 lvm 类型的卷
* convertible 类型卷（需要在 sc 中增加配置项 convertible: true）
    * 应用 Pod 申请多个数据卷 PVC 时，对应数据卷需要使用相同配置 sc
    * 基于 LocalVolume 粒度迁移时，默认所属相同 LocalVolumeGroup 的数据卷不会一并迁移（若一并迁移，需要配置开关 MigrateAllVols：true）

## 界面操作步骤

1. 创建 convertible `StorageClass`

    通过界面安装，请参考[如何创建 StorageClass](../../../kpanda/user-guide/storage/sc.md)

2. 创建多个 `PVC`

    通过界面创建多个 PVC，请参考[如何创建 PVC](../../../kpanda/user-guide/storage/pvc.md)

3. 部署多数据卷 Pod

    通过界面创建应用，请参考[如何创建工作负载](../../../kpanda/user-guide/workloads/create-deployment.md)，并挂载已创建好 2 个 PVC

4. 解挂载多数据卷 Pod

    迁移之前请先解除 PVC 挂载，可通过`编辑工作负载`进行解挂载。

    ![unbound01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/hwameistor/images/unboundpvc-01.png)

5. 创建迁移任务

    进入`对应集群`--> 点击左侧`容器存储`-->`Hwameistor` 进入 `Hwameistor` 界面，选择 已经解绑的本地卷，
    对应的 PVC 为 `pvc-test01`、`pvc-test02`，点击 `...` 选择`迁移`,选择`源节点`，`目标节点`。

    `源节点`： 本地卷副本所在的节点。

    `目标节点`： 指定后原副本将迁移至目标节点，如选择`自动选择`，则本地卷副本将自动调度至其他节点。

    如两个/多个本地卷挂载在同一个应用上，则两个卷会自动组成 本地卷组 统一进行迁移。

    ![migration01](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/migrationaction-01.jpg)

6. 点击对应的本地卷，进入详情查看迁移状态。

## 在线试用步骤

1. 创建 convertible `StorageClass`

    可执行如下命令，PVC 进行创建：

    ```console
    cd ../../deploy/
    kubectl apply -f storageclass-convertible-lvm.yaml
    ```

2. 创建多个 `PVC`

    执行如下命令，PVC 进行创建：

    ```console
    kubectl apply -f pvc-multiple-lvm.yaml
    ```

3. 部署多数据卷 Pod

    执行如下命令，PVC 进行创建：

    ```console
    kubectl apply -f nginx-multiple-lvm.yaml
    ```

4. 解挂载多数据卷 Pod

    执行如下命令，PVC 进行创建：

    ```console
    kubectl patch deployment nginx-local-storage-lvm --patch '{"spec": {"replicas": 0}}' -n hwameistor
    ```

5. 创建迁移任务

    ```console
    cat > ./migrate_lv.yaml <<- EOF
    apiVersion: hwameistor.io/v1alpha1
    kind: LocalVolumeMigrate
    metadata:
      namespace: hwameistor
      name: <localVolumeMigrateName>
    spec:
    sourceNode: <sourceNodeName>
      targetNodesSuggested: 
      - <targetNodesName1>
      - <targetNodesName2>
      volumeName: <volName>
      migrateAllVols: <true/false>
    EOF
    ```

    ```console
    kubectl apply -f ./migrate_lv.yaml
    ```

6. 查看迁移状态

    ```shell
    kubectl get LocalVolumeMigrate  -o yaml
    ```

    ```yaml
    apiVersion: v1
    items:
    - apiVersion: hwameistor.io/v1alpha1
      kind: LocalVolumeMigrate
      metadata:
      annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"hwameistor.io/v1alpha1","kind":"LocalVolumeMigrate","metadata":{"annotations":{},"name":"localvolumemigrate-1","namespace":"hwameistor"},"spec":{"migrateAllVols":true,"sourceNodesNames":["dce-172-30-40-61"],"targetNodesNames":["172-30-45-223"],"volumeName":"pvc-1a0913ac-32b9-46fe-8258-39b4e3b696a4"}}
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
      - dce-172-30-40-61
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

7. 查看迁移成功状态

    ```shell
    [root@172-30-45-222 deploy]# kubectl get lvr
    ```

    ```none
    NAME                                              CAPACITY     NODE            STATE   SYNCED   DEVICE                                                                  AGE
    pvc-1a0913ac-32b9-46fe-8258-39b4e3b696a4-9cdkkn   1073741824   172-30-45-223   Ready   true     /dev/LocalStorage_PoolHDD-HA/pvc-1a0913ac-32b9-46fe-8258-39b4e3b696a4   77s
    pvc-d9d3ae9f-64af-44de-baad-4c69b9e0744a-7ppmrx   1073741824   172-30-45-223   Ready   true     /dev/LocalStorage_PoolHDD-HA/pvc-d9d3ae9f-64af-44de-baad-4c69b9e0744a   77s
    ```

8. 迁移成功后，重新挂载数据卷 Pod

    ```shell
    kubectl patch deployment nginx-local-storage-lvm --patch '{"spec": {"replicas": 1}}' -n hwameistor
    ```
