# Creating Virtual Machines via Templates

This guide explains how to create virtual machines using templates.

With built-in templates and custom templates, users can easily create new virtual machines. Additionally, we provide the ability to convert existing virtual machines into templates, allowing users to manage and utilize resources more flexibly.

## Create Template

Follow these steps to create a virtual machine using a template.

1. Click on `Container Management` in the left navigation menu, then click on `Virtual Machine Container` to access the `Virtual Machine Management` page. On the virtual machine list page, click on `Create Virtual Machine` and select `Create via Template`.

2. On the template creation page, fill in the required information, including basic information, template configuration, storage and networking, and login settings. Then, click `OK` in the bottom-right corner to complete the creation.

    The system will automatically return to the virtual machine list. By clicking on the ellipsis (`︙`) on the right side of the list, you can perform operations such as shutdown/startup, reboot, clone, update, create snapshot, convert to template, console access (VNC), and delete.
    The ability to clone and create snapshots depends on the selected storage pool.


### Basic Information

On the `Create Virtual Machine` page, enter the information according to the table below and click `Next`.



- Name: Can contain up to 63 characters and can only include lowercase letters, numbers, and hyphens (`-`). The name must start and end with a lowercase letter or number.
  Names must be unique within the same namespace, and the name cannot be changed after the virtual machine is created.
- Alias: Can include any characters, up to 60 characters in length.
- Cluster: Select the cluster where the new virtual machine will be deployed.
- Namespace: Select the namespace where the new virtual machine will be deployed.
  If the desired namespace is not found, you can follow the instructions on the page to [create a new namespace](../../kpanda/user-guide/namespaces/createns.md).

### Configure Template

The template list will appear, and you can choose either a built-in template or a custom template based on your needs.

- Select a Built-in Template: The platform provides three standard templates that cannot be edited or deleted. When selecting a built-in template, the image source, operating system, image address, and other information will be based on the template and cannot be modified. Resource quotas will also be based on the template but can be modified.



- Select a Custom Template: These templates are created from virtual machine configurations and can be edited or deleted. When using a custom template, you can modify the image source and other information based on your specific requirements.


### Configure Storage and Networking


- Storage: By default, the system creates a rootfs system disk of VirtIO type for storing the operating system and data. Block storage is used by default. If you need to use clone and snapshot functionality, make sure your storage pool supports the VolumeSnapshots feature and create it in the storage pool (SC). Please note that the storage pool (SC) has additional prerequisites that need to be met.

    - Prerequisites:

        - KubeVirt utilizes the VolumeSnapshot feature of the Kubernetes CSI driver to capture the persistent state of virtual machines. Therefore, you need to ensure that your virtual machine uses a StorageClass that supports VolumeSnapshots and is configured with the correct VolumeSnapshotClass.
        - Check the created SnapshotClass and confirm that the provisioner property matches the Driver property in the storage pool.

    - Supports adding one system disk and multiple data disks.

- Networking: If no configuration is made, the system will create a VirtIO type network by default.

### Login Settings

- Username/Password: You can log in to the virtual machine using a username and password.
- SSH: When selecting SSH login, you can bind an SSH key to the virtual machine for future login purposes.
