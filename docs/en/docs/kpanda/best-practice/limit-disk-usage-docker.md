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
