# Requirements to Join Edge Node

The edge nodes need to meet the specifications in the table below.

## Operating System (OS)

- x86_64 architecture

    Ubuntu LTS (Xenial Xerus), Ubuntu LTS (Bionic Beaver), CentOS, RHEL, Kylin, NewStart, NeoKylin, and EulerOS

- armv7i (arm32) architecture

    Raspbian GNU/Linux (stretch)

- aarch64 (arm64) architecture

    Ubuntu LTS (Bionic Beaver), CentOS, and EulerOS

## Memory

The general overhead of edge software is about 150MB, and it may increase appropriately depending on the pressure of edge management.

To ensure the normal operation of business, it is recommended that the memory of edge nodes should be more than 256MB.

## CPU

Not less than 1 core.

## Hard Disk

Not less than 1GB.

## Container Runtime

Docker version must be higher than 19.0, and it is recommended to use version 19.03.6.

Note: If the KubeEdge version is higher than or equal to 1.14 and the cloud Kubernetes version is higher than 1.24, you need to install CRI-Dockerd in addition to Docker.

## glibc

Version must be higher than 2.17.

To check the version:

```sh
ubuntu: ldd --version
```

## Ports

The edge nodes need to use the following ports, please make sure these ports can be used normally.

- 1883: The built-in MQTT broker listening port of the edge node, and this port needs to be opened.

## Time Synchronization

The time of the edge node needs to be consistent with the time of the cloud server, and UTC standard time is recommended.
