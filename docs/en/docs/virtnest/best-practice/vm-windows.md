# Create a Windows Virtual Machine

This document will explain how to create a Windows virtual machine via the command line.

## Prerequisites

1. Before creating a Windows virtual machine, it is recommended to first refer to [installing dependencies and prerequisites for the virtual machine module](../install/install-dependency.md) to ensure that your environment is ready.
2. During the creation process, it is recommended to refer to the official documentation: [Installing Windows documentation](https://kubevirt.io/2022/KubeVirt-installing_Microsoft_Windows_11_from_an_iso.html), [Installing Windows related drivers](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-during-windows-install).
3. It is recommended to access the Windows virtual machine using the VNC method.

## Import an ISO Image

Creating a Windows virtual machine requires importing an ISO image primarily to install the Windows operating system. Unlike Linux operating systems, the Windows installation process usually involves booting from an installation disc or ISO image file. Therefore, when creating a Windows virtual machine, it is necessary to first import the installation ISO image of the Windows operating system so that the virtual machine can be installed properly.

Here are two methods for importing ISO images:

1. (Recommended) Creating a Docker image. It is recommended to refer to [building images](../vm-image/index.md).

2. (Not recommended) Using virtctl to import the image into a Persistent Volume Claim (PVC).

    You can refer to the following command:

    ```sh
    virtctl image-upload -n <namespace> pvc <PVC name> \
       --image-path=<ISO file path> \
       --access-mode=ReadWriteOnce \
       --size=6G \
       --uploadproxy-url=<https://cdi-uploadproxy ClusterIP and port> \
       --force-bind \
       --insecure \
       --wait-secs=240 \
       --storage-class=<SC>
    ```

    For example:

    ```sh
    virtctl image-upload -n <namespace> pvc <PVC name> \
       --image-path=<ISO file path> \
       --access-mode=ReadWriteOnce \
       --size=6G \
       --uploadproxy-url=<https://cdi-uploadproxy ClusterIP and port> \
       --force-bind \
       --insecure \
       --wait-secs=240 \
       --storage-class=<SC>
    ```

## Create a Windows Virtual Machine Using YAML

Creating a Windows virtual machine using YAML is more flexible and easier to write and maintain. Below are three reference YAML examples:

1. (Recommended) Using Virtio drivers + Docker image:

    - If you need to use storage capabilities - mount disks, please install [viostor drivers](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-during-windows-install).
    - If you need to use network capabilities, please install [NetKVM drivers](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-after-windows-install).

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
      labels:
        virtnest.io/os-family: Windows
        virtnest.io/os-version: '10'
      name: windows10-virtio
      namespace: default
    spec:
      dataVolumeTemplates:
        - metadata:
            name: win10-system-virtio
            namespace: default
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 32Gi
              storageClassName: local-path
            source:
              blank: {}
      running: true
      template:
        metadata:
          labels:
            app: windows10-virtio
            version: v1
            kubevirt.io/domain: windows10-virtio
        spec:
          architecture: amd64
          domain:
            cpu:
              cores: 8
              sockets: 1
              threads: 1
            devices:
              disks:
                - bootOrder: 1
                  disk:
                    bus: virtio # Use virtio
                  name: win10-system-virtio 
                - bootOrder: 2
                  cdrom:
                    bus: sata # Use sata for ISO image
                  name: iso-win10
                - bootOrder: 3
                  cdrom:
                    bus: sata # Use sata for containerdisk
                  name: virtiocontainerdisk
              interfaces:
                - name: default
                  masquerade: {}
            machine:
              type: q35
            resources:
              requests:
                memory: 8G
          networks:
            - name: default
              pod: {}
          volumes:
            - name: iso-win10
              persistentVolumeClaim:
                claimName: iso-win10
            - name: win10-system-virtio
              persistentVolumeClaim:
                claimName: win10-system-virtio
            - containerDisk:
                image: kubevirt/virtio-container-disk
              name: virtiocontainerdisk
    ```

2. (Not recommended) Using a combination of Virtio drivers and virtctl tool to import the image into a Persistent Volume Claim (PVC).

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
      labels:
        virtnest.io/os-family: Windows
        virtnest.io/os-version: '10'
      name: windows10-virtio
      namespace: default
    spec:
      dataVolumeTemplates:
        - metadata:
            name: win10-system-virtio
            namespace: default
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 32Gi
              storageClassName: local-path
            source:
              blank: {}
      running: true
      template:
        metadata:
          labels:
            app: windows10-virtio
            version: v1
            kubevirt.io/domain: windows10-virtio
        spec:
          architecture: amd64
          domain:
            cpu:
              cores: 8
              sockets: 1
              threads: 1
            devices:
              disks:
                - bootOrder: 1
                  # Use virtio
                  disk:
                    bus: virtio
                  name: win10-system-virtio
                  # Use sata for ISO image
                - bootOrder: 2
                  cdrom:
                    bus: sata
                  name: iso-win10
                  # Use sata for containerdisk
                - bootOrder: 3
                  cdrom:
                    bus: sata
                  name: virtiocontainerdisk
              interfaces:
                - name: default
                  masquerade: {}
            machine:
              type: q35
            resources:
              requests:
                memory: 8G
          networks:
            - name: default
              pod: {}
          volumes:
            - name: iso-win10
              persistentVolumeClaim:
                claimName: iso-win10
            - name: win10-system-virtio
              persistentVolumeClaim:
                claimName: win10-system-virtio
            - containerDisk:
                image: kubevirt/virtio-container-disk
              name: virtiocontainerdisk
    ```

3. (Not recommended) In a scenario where Virtio drivers are not used, importing the image into a Persistent Volume Claim (PVC) using the virtctl tool. The virtual machine may use other types of drivers or default drivers to operate disk and network devices.

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
      labels:
        virtnest.io/os-family: Windows
        virtnest.io/os-version: '10'
      name: windows10
      namespace: default
    spec:
      dataVolumeTemplates:
        # Create multiple PVC (disks) for system disk
        - metadata:
            name: win10-system
            namespace: default
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 32Gi
              storageClassName: local-path
            source:
              blank: {}
      running: true
      template:
        metadata:
          labels:
            app: windows10
            version: v1
            kubevirt.io/domain: windows10
        spec:
          architecture: amd64
          domain:
            cpu:
              cores: 8
              sockets: 1
              threads: 1
            devices:
              disks:
                - bootOrder: 1
                  # Use sata without virtio driver
                 cdrom:
                    bus: sata
                  name: win10-system
                  # Use sata for ISO
                - bootOrder: 2
                  cdrom:
                    bus: sata
                  name: iso-win10
              interfaces:
                - name: default
                  masquerade: {}
            machine:
              type: q35
            resources:
              requests:
                memory: 8G
          networks:
            - name: default
              pod: {}
          volumes:
            - name: iso-win10
              persistentVolumeClaim:
                claimName: iso-win10
            - name: win10-system
              persistentVolumeClaim:
                claimName: win10-system
    ```

## Cloud Desktop

For Windows virtual machines, remote desktop control access is often required. It is recommended to use
[Microsoft Remote Desktop](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac#get-the-remote-desktop-client) to control your virtual machine.

!!! note

    - Your Windows version must support remote desktop control to use
     [Microsoft Remote Desktop](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac#get-the-remote-desktop-client).
    - You need to disable the Windows firewall.

## Add Data Disks

Adding a data disk to a Windows virtual machine follows the same process as adding one to a Linux virtual machine. You can refer to the provided YAML example for guidance.

```yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  <...>
  spec:
    dataVolumeTemplates:
      # Add a data disk
      - metadata:
        name: win10-disk
        namespace: default
        spec:
          pvc:
            accessModes:
              - ReadWriteOnce
            resources:
              requests:
                storage: 16Gi
            storageClassName: hwameistor-storage-lvm-hdd
          source:
            blank: {}
    template:
      spec:
        domain:
          devices:
            disks:
              - bootOrder: 1
                disk:
                  bus: virtio
                name: win10-system
              # Add a data disk
              - bootOrder: 2
                disk:
                  bus: virtio
                name: win10-disk
            <....>
        volumes:
          <....>
          # Add a data disk
          - name: win10-disk
            persistentVolumeClaim:
              claimName: win10-disk
```

## Snapshots, Cloning, Live Migration

These capabilities are consistent with Linux virtual machines and can be configured using the same methods.

## Access Your Windows Virtual Machine

1. After successful creation, access the virtual machine list page to confirm that the virtual machine is running properly.

    <!-- Add image later -->

2. Click the console access (VNC) to access it successfully.

    <!-- Add image later -->
