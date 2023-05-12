---
hide:
   - toc
---

# Install via Operator

This page introduces how to install Hwameistor through the Hwameistor Operator.
After the Operator is installed, it will automatically start Hwameistor related components.

## Prerequisites

- Free HDD and SSD disks have been prepared on the nodes to be used
- Completed the items in [Preparation](prereq.md)
- If you need to use highly available data volumes, please complete [DRDB installation](drbdinstall.md) in advance
- If the deployment environment is a production environment, please read [Resource Requirements for Production Environment](proresource.md) in advance
- If your Kubernetes distribution uses a different `kubelet` directory, please confirm `kubeletRootDir` in advance.
  For details, please refer to [Customize Kubelet root directory](customized-kubelet.md)

## Steps

Please confirm that your cluster has successfully connected to `container management` platform, and then perform the following steps to install Hwameistor.

1. On the left navigation bar, click `Container Management` —> `Cluster List`, and find the name of the cluster where Hwameistor is to be installed.

2. In the left navigation bar, select `Helm Application` -> `Helm chart`, find and click `Hwameistor Operator`.

     ![click](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator1.jpg)

3. In `Version Selection`, select the version you want to install, and click `Install`.

4. On the installation interface, fill in the required installation parameters.

     ![Operator02](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator2.jpg)

     **`Value.yaml`** parameters are as follows, the default can not be modified:

     ```yaml
     global:
       targetNamespace: hwameistor
       hwameistorImageRegistry: ghcr.io
       k8sImageRegistry: registry.k8s.io
       hwameistorVersion: v0.9.2
     operator:
       replicas: 1
       imageRepository: hwameistor/operator
       tag: ''
     localDiskManager:
       tolerationOnMaster: true
       kubeletRootDir: /var/lib/kubelet
       manager:
         imageRepository: hwameistor/local-disk-manager
         tag: ''
       csi:
         registrar:
           imageRepository: sig-storage/csi-node-driver-registrar
           tag: v2.5.0
         provisioner:
           imageRepository: sig-storage/csi-provisioner
           tag: v2.0.3
         attacher:
           imageRepository: sig-storage/csi-attacher
           tag: v3.0.1
     localStorage:
       tolerationOnMaster: true
       kubeletRootDir: /var/lib/kubelet
       member:
         imageRepository: hwameistor/local-storage
         tag: ''
       csi:
         registrar:
           imageRepository: sig-storage/csi-node-driver-registrar
           tag: v2.5.0
         provisioner:
           imageRepository: sig-storage/csi-provisioner
           tag: v2.0.3
         attacher:
           imageRepository: sig-storage/csi-attacher
           tag: v3.0.1
         resizer:
           imageRepository: sig-storage/csi-resizer
           tag: v1.0.1
         monitor:
           imageRepository: sig-storage/csi-external-health-monitor-controller
           tag: v0.8.0
     scheduler:
       imageRepository: hwameistor/scheduler
       tag: ''
     admission:
       imageRepository: hwameistor/admission
       tag: ''
     evictor:
       imageRepository: hwameistor/evictor
       tag: ''
     apiserver:
       imageRepository: hwameistor/apiserver
       tag: ''
     exporter:
       imageRepository: hwameistor/exporter
       tag: ''
     ui:
       imageRepository: hwameistor/hwameistor-ui
       tag: ''
     ha:
       module: drbd
       deployOnMaster: 'yes'
     ```

     - `hwameistorImageRegistry`:

         Set the registry address of the Hwameistor mirror, and the available online registrys have been filled in by default.
         If it is a privatized environment, it can be modified to a private registry address.

     - `K8s image Registry`:

         Set the address of the K8S container registry, and the available online registry has been filled in by default.
         If the environment is privatized, it can be modified to a private registry address.

5. After confirming that the parameters are correct, click `OK` to complete the installation. After the installation is complete, you can click `Helm Application` to view the installation status of `Hwameistor Operator`.

     ![Operator03](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator3.jpg)

6. After the Operator is installed, the Hwameistor components (Local Storage, Local Disk Manager, etc.) will be installed by default!
    You can click `Workload`-->`Stateless Workload`, select the corresponding namespace, and view the status of the Hwameistor component.

     ![hwameistor status](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/operator4.jpg)

     To verify the installation effect through the command line, please refer to [Post-installation Check](./post-check.md).
