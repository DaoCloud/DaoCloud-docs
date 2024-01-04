---
hide:
  - toc
---

# Create Virtual Machine

This article will explain how to create a virtual machine using two methods: image and YAML file.

Virtual machine, based on KubeVirt technology, manage virtual machines as cloud native applications,
seamlessly integrating with containers. This allows users to easily deploy virtual machine applications and
enjoy a smooth experience similar to containerized applications.

## Prerequisites

Before creating a virtual machine, make sure you meet the following prerequisites:

- Install the virtnest-agent within the cluster.
- Create a [namespace](../../kpanda/user-guide/namespaces/createns.md) and [user](../../ghippo/user-guide/access-control/user.md).
- The current user should have [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)
  or higher permissions. Refer to the documentation on
  [namespace authorization](../../kpanda/user-guide/namespaces/createns.md) for more details.
- Prepare the required images in advance.

## Image Creation

Follow the steps below to create a virtual machine using an image.

1. Click `Container Management` on the left navigation bar, then click `Virtual Machine` to enter the `Virtual Machine Management` page.

    ![VM](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm01.png)

2. On the virtual machine list page, click `Create VMs` and select `Create with Image`.

    ![Create VM from Image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm02.png)

3. Fill in the basic information, image configuration, storage and networking, login settings, and click `OK` at the bottom right corner to complete the creation.

    The system will automatically return to the virtual machine list. By clicking the `︙` button
    on the right side of the list, you can perform operations such as power on/off, restart,
    clone, update, create snapshots, console access (VNC), and delete virtual machines.
    Cloning and snapshot capabilities depend on the selected StorageClass.

    ![VM Management](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm03.png)

### Basic Information

In the `Create VMs` page, enter the information according to the table below and click `Next`.

![Basic Information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm04.png)

- Name: Up to 63 characters, can only contain lowercase letters, numbers, and hyphens (`-`),
  and must start and end with a lowercase letter or number. The name must be unique within the
  namespace, and cannot be changed once the virtual machine is created.
- Alias: Allows any characters, up to 60 characters.
- Cluster: Select the cluster to deploy the newly created virtual machine.
- Namespace: Select the namespace to deploy the newly created virtual machine.
  If the desired namespace is not found, you can create a new namespace according to the prompts on the page.
- Label/Annotation: Select the desired labels/annotations to add to the virtual machine.

### Image Settings

After filling in the image-related information according to the table below, click `Next`.

    ![Image Repository](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm05.png)

- Image Source: Supports three types of sources.

    - Image Repository: Images stored in the container image repository, supporting the option
      to enable or disable using system-built images. When enabled, you can use the platform's
      built-in images. When disabled, you can select images from the image repository as needed.
    - HTTP Type: Images stored in a file server using the HTTP protocol, supporting both
      `HTTPS://` and `HTTP://` prefixes.
    - Object Storage (S3): Virtual machine images obtained through the object storage protocol (S3).
      For non-authenticated object storage files, please use the HTTP source.

- Currently, the following operating systems and versions are supported.

    | Operating System | Corresponding Version | Image Address |
    | :--------------: | :------------------: | ------------- |
    |      CentOS      |       CentOS 8.3      | release-ci.daocloud.io/virtnest/system-images/centos-7.9-x86_64:v1 |
    |      Ubuntu      |     Ubuntu 22.04      | release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1 |
    |      Debian      |       Debian 12       | release-ci.daocloud.io/virtnest/system-images/debian-12-x86_64:v1 |

- Image Secret: Only supports the default (Opaque) type of key, for specific operations you can refer to [Create Secret](create-secret.md).

- CPU Quota, Memory Quota: For CPU, it is recommended to use whole numbers.
  If a decimal is entered, it will be rounded up.

### Storage and Network

    ![Storage and Network](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm06.png)

- Storage: By default, a VirtIO-based rootfs system disk is created to store the operating system and data.
  Block storage is used by default. If you need to use cloning and snapshot functions, make sure your
  StorageClass supports VolumeSnapshots functionality and create it in the StorageClass (SC).
  Please note that the StorageClass (SC) has other prerequisites that need to be met.

    - Prerequisites:
    
        - KubeVirt utilizes the VolumeSnapshot feature of the Kubernetes CSI driver to capture
          the persistent state of the virtual machine. Therefore, ensure that your virtual machine
          uses a StorageClass that supports VolumeSnapshots and configure the correct VolumeSnapshotClass.
        - Check the created SnapshotClass and confirm that the provisioner property matches the
          Driver property in the StorageClass.

          > Multi-disk support will be added in the future.

- Network: If no configuration is done, the system will create a VirtIO-based network by default.

### Login Settings

- Username/Password: Allows login to the virtual machine using a username and password.
- SSH: When selecting the SSH login method, you can bind an SSH key to the virtual machine for future login.

![Login Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm07.png)

## Create by YAML

In addition to creating virtual machines using images, you can also create them more quickly using YAML files.

Go to the virtual machine container list page and click on the `Create with YAML` button.

![Create with YAML](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/createvm08.png)

??? note "Click to view an example YAML for creating a virtual machine"

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: example
      namespace: default
    spec:
      dataVolumeTemplates:
        - metadata:
            name: systemdisk-example
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 10Gi
              storageClassName: rook-ceph-block
            source:
              registry:
                url: >-
                  docker://release-ci.daocloud.io/virtnest/system-images/centos-7.9-x86_64:v1
      runStrategy: Always
      template:
        spec:
          domain:
            cpu:
              cores: 1
            devices:
              disks:
                - disk:
                    bus: virtio
                  name: systemdisk-example
                - disk:
                    bus: virtio
                  name: cloudinitdisk
              interfaces:
                - masquerade: {}
                  name: default
            machine:
              type: q35
            resources:
              requests:
                memory: 1Gi
          networks:
            - name: default
              pod: {}
          volumes:
            - dataVolume:
                name: systemdisk-example
              name: systemdisk-example
    ```
