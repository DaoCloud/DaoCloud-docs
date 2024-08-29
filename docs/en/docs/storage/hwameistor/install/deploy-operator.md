---
MTPE: WANG0608GitHub
Date: 2024-08-28
hide:
   - toc
---

# Install HwameiStor via hwameistor-operator

This article introduces how to install HwameiStor through the hwameistor-operator on UI. After installing the operator, it will automatically launch the HwameiStor-related
components. The hwameistor-operator is responsible for the following:

- Full lifecycle management (LCM) of all components:
    - LocalDiskManager
    - LocalStorage
    - Scheduler
    - AdmissionController
    - VolumeEvictor
    - Exporter
    - Apiserver
    - Graph UI
- Configuring node disks for different purposes and use cases
- Automatically discovering the type of node disks and creating HwameiStor StorageClass accordingly
- Automatically creating proper StorageClasses based on the configuration and features of the HwameiStor system

## Prerequisites

- Nodes intended for use with HwameiStor must have sufficient free HDD and SSD disks.
- Ensure that all prerequisites in the [Preparation](prereq.md) documentation are met.
- If you plan to use high-availability data volumes, complete the [DRBD installation](drbdinstall.md) process beforehand.
- If deploying to a production environment, please review the [Resource Requirements for Production Environment](proresource.md) documentation beforehand.
- If your Kubernetes distribution uses a different `kubelet` directory, confirm the `kubeletRootDir` parameter beforehand. For more details, refer to [Customize kubelet root directory](customized-kubelet.md).

!!! info

    If there are no available clean disks, the operator will not automatically create a StorageClass.
    During the installation process, the operator will automatically manage the disks and add available disks to the LocalStorage pool.
    If the available disks are provided after the installation, you need to manually issue a LocalDiskClaim to manage the disks in LocalStorageNode.
    Once there are disks in the pool of LocalStorageNode, the operator will automatically create the StorageClass.
    In other words, if there is no capacity, the StorageClass will not be created automatically.

## Steps

Ensure that your cluster has successfully connected to __Container Management__ before proceeding with the
following steps to install HwameiStor.

1. In the left navigation bar, click __Container Management__ -> __Clusters__ , and find the name of the cluster where HwameiStor will be installed.

2. In the left navigation bar, select __Helm Apps__ -> __Helm Charts__ , find and click __hwameistor-operator__.

    ![hwameistor-operator](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/operator1.png)

3. Within the __Version__ section, choose the version to install, and then click __Install__ .

4. On the installation interface, fill in the required installation parameters.

    ![Basic Info](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/operator2.png)

    The parameters in `Value.yaml` are as follows and can't be modified by default:

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

    - `hwameistorImageRegistry`:

        Set the registry address of the HwameiStor image, and the default values for available online registries have already been provided.
        If it is a private environment, it can be modified to a private registry address.

    - `K8s container registry`:

        Set the address of the K8s container registry, and the available online registry has been filled in by default.
        If the environment is privatized, it can be modified to a private registry address.

    - `DRBD`：

        If you need to use high-availability data volumes, please enable the `DRBD` module. If it was not
        enabled during installation, please refer to [Enabling DRBD](drbdinstall.md).

    - `replicas`:

        The recommended number of replicas for each component is `2`.

5. After confirming that the parameters are correct, click __OK__ to complete the installation.
   After the installation is complete, you can click __Helm Apps__ to view the installation status of __hwameistor-operator__.

    ![Check Status](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/operator3.png)

6. After the operator is installed, the HwameiStor components (Local Storage, Local Disk Manager) will be installed by default!
    You can click __Workload__--> __Deployments__, select the proper namespace, and view the status of the HwameiStor component.

    ![Details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/operator4.png)

    To verify the installation effect through the command line, please refer to [Post-installation Check](./post-check.md).
