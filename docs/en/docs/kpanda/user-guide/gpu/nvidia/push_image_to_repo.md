# Uploading RedHat GPU Operator Offline Image to Ignition Repository

This guide explains how to upload an offline image to the Ignition repository using the `nvcr.io/nvidia/driver:525.105.17-rhel8.4` offline driver image for RedHat 8.4 as an example.

## Prerequisites

1. The Ignition node and its components are running properly.
2. Prepare a node that has internet access and can access the Ignition node. Docker should also be installed on this node. You can refer to [Installing Docker](../../../../install/community/kind/online.md) for installation instructions.

## Procedure

### Step 1: Obtain the Offline Image on an Internet-Connected Node

Perform the following steps on the internet-connected node:

1. Pull the `nvcr.io/nvidia/driver:525.105.17-rhel8.4` offline driver image:

    ```bash
    docker pull nvcr.io/nvidia/driver:525.105.17-rhel8.4
    ```

2. Once the image is pulled, save it as a compressed archive named `nvidia-driver.tar`:

    ```bash
    docker save nvcr.io/nvidia/driver:525.105.17-rhel8.4 > nvidia-driver.tar
    ```

3. Copy the compressed image archive `nvidia-driver.tar` to the Ignition node:

    ```bash
    scp nvidia-driver.tar user@ip:/root
    ```

    For example:

    ```bash
    scp nvidia-driver.tar root@10.6.175.10:/root
    ```

### Step 2: Push the Image to the Ignition Repository

Perform the following steps on the Ignition node:

1. Log in to the Ignition node and import the compressed image archive `nvidia-driver.tar`:

    ```bash
    docker load -i nvidia-driver.tar
    ```

2. View the imported image:

    ```bash
    docker images -a | grep nvidia
    ```

    Expected output:

    ```bash
    nvcr.io/nvidia/driver                 e3ed7dee73e9   1 days ago   1.02GB
    ```

3. Retag the image to correspond to the target repository in the remote Registry repository:

    ```bash
    docker tag <image-name> <registry-url>/<repository-name>:<tag>
    ```

    Replace `<image-name>` with the name of the Nvidia image from the previous step, `<registry-url>` with the address of the Registry service on the Ignition node, `<repository-name>` with the name of the repository you want to push the image to, and `<tag>` with the desired tag for the image.

    For example:

    ```bash
    docker tag nvcr.io/nvidia/driver 10.6.10.5/nvcr.io/nvidia/driver:525.105.17-rhel8.4
    ```

4. Push the image to the Ignition image repository:

    ```bash
    docker push {ip}/nvcr.io/nvidia/driver:525.105.17-rhel8.4
    ```

## What's Next

Refer to [Building RedHat 8.4 Offline Yum Source](./upgrade_yum_source_redhat8_4.md) and [Offline Installation of GPU Operator](./install_nvidia_driver_of_operator.md) to deploy the GPU Operator to your cluster.
