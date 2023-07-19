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

## GPU (optional)

1. Currently supports Nvidia Tesla series P4, P40, T4 and other GPU models.

    Machines with GPU hardware can be used as edge nodes without GPUs.

    If the edge node uses a GPU, you need to install the GPU driver and Nvidia Docker adaptation (nvidia-docker2) before registration.

    You need to set the default runtime of the container engine to nvidia.

    ```sh
    /etc/docker/daemon.json
    ```

    ```json
    {
      "default-runtime": "nvidia",
      "runtimes": {
        "nvidia": {
          "path": "nvidia-container-runtime",
          "runtimeArgs": []
        }
      }
    }
    ```

2. Other requirements for NVIDIA GPU on ARM64 architecture:

    - It is recommended that the system be installed with Jetpack4.5+.
    - The image needs to be built using the [base image](https://catalog.ngc.nvidia.com/containers) hosted on NVIDIA L4T.

3. Environment verification:

    ```sh
    nvidia-container-cli -k -d /dev/tty info
    ```

    When the above command is successful, you can access it (The above tool comes with nvidia-docker2 after installation).

## Container Runtime

Docker version must be higher than 19.0, and it is recommended to use version 19.03.6.

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
