---
hide:
  - toc
---

# Create Virtual Machine

This article will explain how to create a virtual machine using two methods: image and YAML file.

Virtual machine containers, based on KubeVirt technology, manage virtual machines as cloud native applications,
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

1. Click `Container Management` on the left navigation bar, then click `Virtual Machine Containers`
   to enter the `Virtual Machine Management` page.


2. On the virtual machine list page, click `Create Virtual Machine` and select `Create VM from Image`.


3. Fill in the basic information, image configuration, storage and networking, login settings, and click `Confirm` at the bottom right corner to complete the creation.

    The system will automatically return to the virtual machine list. By clicking the `︙` button
    on the right side of the list, you can perform operations such as power on/off, restart,
    clone, update, create snapshots, console access (VNC), and delete virtual machines.
    Cloning and snapshot capabilities depend on the selected StorageClass.


### Basic Information

In the `Create Virtual Machine` page, enter the information according to the table below and click `Next`.

- Name: Up to 63 characters, can only contain lowercase letters, numbers, and hyphens (`-`),
  and must start and end with a lowercase letter or number. The name must be unique within the
  namespace, and cannot be changed once the virtual machine is created.
- Alias: Allows any characters, up to 60 characters.
- Cluster: Select the cluster to deploy the newly created virtual machine.
- Namespace: Select the namespace to deploy the newly created virtual machine.
  If the desired namespace is not found, you can create a new namespace according to the prompts on the page.
- Labels/Annotations: Select the desired labels/annotations to add to the virtual machine.

### Container Configuration

After filling in the image-related information according to the table below, click `Next`.

- Image Source: Supports three types of sources.

    - Image Repository Type: Images stored in the container image repository, supporting the option
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

- CPU Quota, Memory Quota: For CPU, it is recommended to use whole numbers.
  If a decimal is entered, it will be rounded up.

### Storage and Networking Configuration

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

- Networking: If no configuration is done, the system will create a VirtIO-based network by default.

### Login Settings

- Username/Password: Allows login to the virtual machine using a username and password.
- SSH: When selecting the SSH login method, you can bind an SSH key to the virtual machine for future login.

## Create by YAML

In addition to the image method, you can also create a virtual machine more quickly using a YAML file.

1. Go to the virtual machine container list page and click the `Create via YAML` button.


2. Enter or paste the prepared YAML file and click `Confirm` to complete the creation.
