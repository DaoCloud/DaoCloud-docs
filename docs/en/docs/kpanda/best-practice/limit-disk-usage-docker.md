# Limit Docker Single Container Disk Space Usage

Docker introduced overlay2.size in version 17.07.0-ce. This article introduces how to use overlay2.size to limit the disk space that a single Docker container can occupy.

## Prerequisites

Before configuring docker overlay2.size, you need to adjust the file system type to xfs in the operating system and use pquota method for device mounting.

To format the device as XFS file system, you can execute the following command:

```shell
mkfs.xfs -f /dev/xxx
```

!!! note

    pquota limits project disk quota.

## Set Single Container Disk Space

After meeting the above conditions, users can limit single container disk space by setting docker overlay2.size. Command line example:

```shell
sudo dockerd -s overlay2 --storage-opt overlay2.size=1G
```

## Scenario Walkthrough

Next, let's walk through the overall implementation process of limiting Docker single container disk space usage with a practical example.

### Target

Deploy a Kubernetes cluster and limit the disk space that a single Docker container can occupy to 1G. It cannot be used once it exceeds 1G.

### Procedure

1. Log in to the target node and view the fstab file to obtain the current mounting status of the device.

    ```shell
    $ cat /etc/fstab
    
    # /etc/fstab
    # Created by anaconda on Thu Mar 19 11:32:59 2020
    #
    # Accessible filesystems, by reference, are maintained under '/dev/disk'
    # See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
    #
    /dev/mapper/centos-root /                       xfs     defaults        0 0
    UUID=3ed01f0e-67a1-4083-943a-343b7fed1708 /boot                   xfs     defaults        0 0
    /dev/mapper/centos-swap swap                    swap    defaults        0 0
    ```

    Taking the node device in the figure as an example, you can see that the XFS format device /dev/mapper/centos-root is mounted to the / root directory in the default way (defaults).

2. Configure the xfs file system to be mounted using the pquota method.

    1. Modify the fstab file to update the mounting method from defaults to rw,pquota;

        ```shell
        # Modify the fstab configuration
        $ vi /etc/fstab
        - /dev/mapper/centos-root /                       xfs     defaults         0 0
        + /dev/mapper/centos-root /                       xfs     rw,pquota        0 0
    
        # Verify whether the configuration is correct
        $ mount -a
        ```

    2. Check whether pquota takes effect.

        ```shell
        xfs_quota -x -c print
        ```

        ![View the fstab Configuration](../images/limit-disk-usage-docker-01.png)

    !!! note

        If pquota does not take effect, check whether the pquota option is enabled in the operating system. If it is not enabled, you need to add the `rootflags=pquota` parameter to the system boot configuration /etc/grub2.cfg. After the configuration is complete, you need to reboot the operating system.

    ![Enable the pquota Option in the Operating System](../images/limit-disk-usage-docker-02.png)

3. Add the docker_storage_options parameter in **Create Cluster** -> **Advanced Settings** -> **Custom Parameters** to set the disk space that a single container can occupy.

    ![Add Custom Parameters](../images/limit-disk-usage-docker-03.png)

    !!! note

        You can also operate based on the kubean manifest and add the `docker_storage_options` parameter in vars conf.

        ```yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: sample-vars-conf
          namespace: kubean-system
        data:
          group_vars.yml: |
            unsafe_show_logs: true
            container_manager: docker
        +   docker_storage_options: -s overlay2 --storage-opt overlay2.size=1G  # Add the docker_storage_options parameter
            kube_network_plugin: calico
            kube_network_plugin_multus: false
            kube_proxy_mode: iptables
            etcd_deployment_type: kubeadm
            override_system_hostname: true
            ...
        ```

4. View the running configuration of the dockerd service to check whether the disk limit is set successfully.

    ![Check the Container Disk Limit](../images/limit-disk-usage-docker-04.png)

With the above steps, the overall implementation process of limiting the disk space that a single Docker container can occupy is complete.
