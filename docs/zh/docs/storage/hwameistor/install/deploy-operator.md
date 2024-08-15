---
hide:
  - toc
---

# Hwameistor 安装

本文介绍在平台界面通过 Hwameistor Operator 安装 Hwameistor，Operator 安装后会自动将 Hwameistor 相关组件拉起。HwameiStor Operator 负责如下事项：

- 所有组件的全生命周期管理 (LCM)：
    - LocalDiskManager
    - LocalStorage
    - Scheduler
    - AdmissionController
    - VolumeEvictor
    - Exporter
    - Apiserver
    - Graph UI
- 根据不同目的和用途配置节点磁盘
- 自动发现节点磁盘的类型，并以此自动创建 HwameiStor 存储池
- 根据 HwameiStor 系统的配置和功能自动创建相应的 StorageClass

## 前提条件

- 待使用节点上已准备空闲 HDD、SSD 磁盘。
- 已完成[准备工作](prereq.md)中事项。
- 如部署环境为生产环境，请提前阅读[生产环境资源要求](proresource.md)。
- 如果您的 Kubernetes 发行版使用不同的 `kubelet` 目录，请提前确认 `kubeletRootDir`。
  详细信息请参考[自定义 Kubelet 根目录](customized-kubelet.md)。

!!! info

    如果没有可用的干净磁盘，Operator 不会自动创建 StorageClass。
    Operator 会在安装过程中自动纳管磁盘，可用的磁盘会被添加到 LocalStorage 的 pool 里。
    如果可用磁盘是在安装后提供的，则需要手动下发 LocalDiskClaim 将磁盘纳管到 LocalStorageNode 里。
    一旦 LocalStorageNode 的 pool 里有磁盘，Operator 就会自动创建 StorageClass。
    也就是说，如果没有容量，就不会自动创建 StorageClass。

## 安装步骤

请确认您的集群已成功接入`容器管理`平台，然后执行以下步骤安装 Hwameistor。

1. 在左侧导航栏点击 `容器管理` —> `集群列表`，然后找到准备安装 Hwameistor 的集群名称。

2. 在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到并点击 `Hwameistor Operator`。

    ![点击](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator1.jpg)

3. 在`版本选择`中选择希望安装的版本，点击`安装`。

4. 在安装界面，填写所需的安装参数。

    ![Operator02](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator2.jpg)

    `Value.yaml` 参数如下，默认可不进行修改：

    ```yaml
    global:
      targetNamespace: hwameistor
      notClaimDisk: false
      hwameistorImageRegistry: ghcr.m.daocloud.io
      k8sImageRegistry: k8s.m.daocloud.io
      hwameistorVersion: v0.14.3
    operator:
      replicas: 1
      imageRepository: hwameistor/operator
      tag: v0.14.6
    localDiskManager:
      tolerationOnMaster: true
      kubeletRootDir: /var/lib/kubelet
      manager:
        imageRepository: hwameistor/local-disk-manager
        tag: v0.14.3
      csi:
        registrar:
          imageRepository: sig-storage/csi-node-driver-registrar
          tag: v2.5.0
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        controller:
          replicas: 1
        provisioner:
          imageRepository: sig-storage/csi-provisioner
          tag: v2.0.3
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        attacher:
          imageRepository: sig-storage/csi-attacher
          tag: v3.0.1
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
    localStorage:
      disable: false
      tolerationOnMaster: true
      kubeletRootDir: /var/lib/kubelet
      member:
        imageRepository: hwameistor/local-storage
        tag: v0.14.3
        hostPathSSHDir: /root/.ssh
        hostPathDRBDDir: /etc/drbd.d
      csi:
        registrar:
          imageRepository: sig-storage/csi-node-driver-registrar
          tag: v2.5.0
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        controller:
          replicas: 1
        provisioner:
          imageRepository: sig-storage/csi-provisioner
          tag: v3.5.0
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        attacher:
          imageRepository: sig-storage/csi-attacher
          tag: v3.0.1
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        resizer:
          imageRepository: sig-storage/csi-resizer
          tag: v1.0.1
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        monitor:
          imageRepository: sig-storage/csi-external-health-monitor-controller
          tag: v0.8.0
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        snapshotController:
          imageRepository: sig-storage/snapshot-controller
          tag: v6.0.0
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
        snapshotter:
          imageRepository: sig-storage/csi-snapshotter
          tag: v6.0.0
          resources:
            limits:
              cpu: 500m
              memory: 500Mi
            requests:
              cpu: 1m
              memory: 20Mi
      migrate:
        rclone:
          imageRepository: rclone/rclone
          tag: 1.53.2
        juicesync:
          imageRepository: hwameistor/hwameistor-juicesync
          tag: v1.0.4-01
      snapshot:
        disable: false
    scheduler:
      disable: false
      replicas: 1
      imageRepository: hwameistor/scheduler
      tag: v0.14.3
    admission:
      disable: false
      replicas: 1
      imageRepository: hwameistor/admission
      tag: v0.14.3
      failurePolicy: Ignore
    evictor:
      disable: true
      replicas: 0
      imageRepository: hwameistor/evictor
      tag: v0.14.3
    apiserver:
      disable: false
      replicas: 1
      imageRepository: hwameistor/apiserver
      tag: v0.14.3
      authentication:
        enable: false
        accessId: admin
        secretKey: admin
    exporter:
      disable: false
      replicas: 1
      imageRepository: hwameistor/exporter
      tag: v0.14.3
    auditor:
      disable: false
      replicas: 1
      imageRepository: hwameistor/auditor
      tag: v0.14.3
    failoverAssistant:
      disable: false
      replicas: 1
      imageRepository: hwameistor/failover-assistant
      tag: v0.14.3
    pvcAutoResizer:
      disable: false
      replicas: 1
      imageRepository: hwameistor/pvc-autoresizer
      tag: v0.14.3
    localDiskActionController:
      disable: false
      replicas: 1
      imageRepository: hwameistor/local-disk-action-controller
      tag: v0.14.3
    ui:
      disable: false
      replicas: 1
      imageRepository: hwameistor/hwameistor-ui
      tag: v0.16.0
    ha:
      disable: false
      module: drbd
      deployOnMaster: 'yes'
      imageRepository: hwameistor/drbd9-shipper
      drbdVersion: v9.0.32-1
      shipperChar: v0.4.1
    drbdRhel7:
      imageRepository: hwameistor/drbd9-rhel7
    drbdRhel8:
      imageRepository: hwameistor/drbd9-rhel8
    drbdRhel9:
      imageRepository: hwameistor/drbd9-rhel9
    drbdKylin10:
      imageRepository: hwameistor/drbd9-kylin10
    drbdBionic:
      imageRepository: hwameistor/drbd9-bionic
    drbdFocal:
      imageRepository: hwameistor/drbd9-focal
    preHookJob:
      imageRepository: dtzar/helm-kubectl
      tag: 3.9
    ```  
        

    -  `hwameistorImageRegistry`：

        设置 Hwameistor 镜像的仓库地址，默认已经填写了可用的在线仓库。
        如果是私有化环境，可修改为私有仓库地址。

    -  `K8s image Registry`：

        设置 K8S 镜像仓库地址，默认已经填写可用在线仓库。
        如果私有化环境，可修改为私有仓库地址。
        
    - `DRDB`：

        如果需要使用 高可用数据卷，请开启 `DRDB`模块，如安装时未开启，请参考 [开启 DRDB](drbdinstall.md)

    - `replicas`:
        各组件副本数量，建议使用 `2` 副本。

5. 确认参数无误后，点击`确定`完成安装，完成安装后可点击 `Helm 应用`查看 `Hwameistor Operator` 安装状态。

    ![Operator03](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator3.jpg)

6. Operator 安装完成后，Hwameistor 组件（Local Storage、Local Disk Manager 等）默认进行安装！
   可点击`工作负载`-->`无状态工作负载`，选择对应命名空间，查看 Hwameistor 组件状态。

    ![hwameistor 状态](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator4.jpg)

    通过命令行验证安装效果，请参[安装后检查](./post-check.md)。
