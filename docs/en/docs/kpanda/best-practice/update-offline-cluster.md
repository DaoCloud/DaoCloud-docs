# Work Cluster Offline Upgrade Guide

!!! note

    This page describes how to upgrade the kubernetes version of the working cluster created using the DCE 5.0 platform in offline mode, and does not include the upgrade of other kubeneters components.

## Overview

In the offline scenario, users can upgrade the kubernetes version of the working cluster created using the DCE 5.0 platform by making an incremental offline package. The overall upgrade idea is: build the offline package on the networking node → import the offline package into the bootstrapping node → update the kubernetes version list of the Global cluster → use the platform UI to upgrade the kubernetes version of the working cluster.

!!! note
    
    Offline kubernetes builds currently supported are as follows:

    - v1.26.3, v1.26.2, v1.26.1, v1.26.0, v1.25.8
    - v1.25.7, v1.25.6, v1.25.5, v1.25.4, v1.25.3, v1.25.2, v1.25.1, v1.25.0,
    - v1.24.12, v1.24.11, v1.24.10, v1.24.9, v1.24.8, v1.24.7, v1.24.6, v1.24.5, v1.24.4, v1.24.3, v1.24.2, v1.24.1, v1.24.0

## Build Offline Packages at Networked Node

Because the offline environment cannot be connected to the Internet, users need to prepare a machine ** Networked nodes ** in advance to build incremental offline packages and start the Docker service on this node. [How to install Docker?](../../blogs/230315-install-on-linux.md)

1. Check the Docker service running status of the networked nodes

    ```bash
    # Check status of docker process on the node
    ps aux|grep docker 

    # The desired output looks like:
    root     12341  0.5  0.2 654372 26736 ?        Ssl  23:45   0:00 /usr/bin/docked
    root     12351  0.2  0.1 625080 13740 ?        Ssl  23:45   0:00 docker-containerd --config /var/run/docker/containerd/containerd.toml
    root     13024  0.0  0.0 112824   980 pts/0    S+   23:45   0:00 grep --color=auto docker
    ```

2. Create a file named `manifest.yaml` in the directory of the `/root` networked node with the following command:

    ```bash
    vi manifest.yaml
    ```

    `manifest.yaml` includes the following contents:

    ```yaml
    image_arch:
    - "amd64"
    kube_version:
    - "v1.25.5"
    - "v1.25.4"
    - "v1.24.8"
    - "v1.24.5"
    ```

    -  `image_arch` Used to specify the architecture type of the CPU. The available parameters are `amd64` and `arm64`.
    -  `kube_version` Used to specify the version of the kubernetes offline package that needs to be built. Refer to the offline kubernetes version that supports building above.

3. Create a new `/data` folder named under the `/root` directory to store the incremental offline package.

    ```bash
    mkdir data
    ```

    run the following command to generate an offline package using `ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.4.8` the image.

    For more information about `ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.4.8` mirroring, go to [kubean](https://github.com/kubean-io/kubean/pkgs/container/kubean-operator).

    ```bash
    docker run --rm -v $(pwd)/manifest.yml:/manifest.yml -v $(pwd)/data:/data ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.4.8
    ```

    After the docker service finishes running, check `/data` the files under the folder. The file directory is as follows:

    ```bash
    data
    └── v_offline_patch
        ├── amd64
        │   ├── files
        │   │   ├── import_files.sh
        │   │   └── offline-files.tar.gz # binary file
        │   └── images
        │       ├── import_images.sh
        │       └── offline-images.tar.gz # image file
        └── kubeanofflineversion.cr.patch.yaml
    ```

## Import Offline Packages into the Fire Node

1. Copy the files of the `/data` networking node to the directory of the `/root` fire node, and then ** Networking node ** run the following command:

    ```bash
    scp -r data root@x.x.x.x:/root
    ```

    !!! note

        `x.x.x.x` is the IP address of bootstrapping node.

2. Copy the image file in the `/data` folder to the docker registry built in the bootstrapping node.
   After logging in the fire node, run the following command:

    1. Enter the directory where the image file is located
    
        ```bash
        cd data/v_offline_patch/amd64/images
        ```

    2. Run the import _ images. Sh script to import the image into the built-in docker registry of the fire node.
   
        ```bash
        DEST_TLS_VERIFY=false ./import_images.sh 127.0.0.1:443
        ```

    !!! note

        The above command is only applicable to the docker registry registry built in the fire node. If an external registry is used, please use the following command:
        
        ```yaml
        DEST_USER=${username} DEST_PASS=${password} DEST_TLS_VERIFY=false ./import_images.sh https://x.x.x.x:443
        ```
        
        `https://x.x.x.x:443` is the address of the external registry.
        `DEST_USER=${username} DEST_PASS=${password}` includes username and password parameters for the external registry. This parameter can be deleted if the external registry is secret-free.

3. Copy the binary file in the `/data` file to the built-in Minio service of the fire node on the fire node.

    1. Go to the directory where the binary is located
    
        ```bash
        cd data/v_offline_patch/amd64/files/
        ```

    2. Run the import _ files. Sh script to import the binary file into the Minio service built into the Kindle Node.
    
        ```bash
        MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_files.sh http://127.0.0.1:9000
        ```

!!! note

    The above commands are only applicable to the built-in Minio service of the bootstrapping node. If you use an external Minio, please replace `http://127.0.0.1:9000` with the access address of the external Minio.
    `rootuser` and `rootpass123` are the default account and password of the built-in Minio service of bootstrapping nodes.

## Update kubernetes version manifest for Global cluster

1. Copy the inventory configuration file in `kubeanofflineversion.cr.patch` the file of the `/data` networking node
   to any ** Master node ** `/root` directory in the Global cluster, and ** Networking node ** run the following command:

    ```bash
    scp -r data/v_offline_patch/kubeanofflineversion.cr.patch.yaml root@x.x.x.x:/root
    ```

    !!! note

        `x.x.x.x` is the IP address of any Master node in the Global cluster.

2. Log in to any ** Master node ** execution list configuration file in the Global cluster
   after completing the previous step. The command is as follows:

    ```bash
    kubectl apply -f kubeanofflineversion.cr.patch.yaml
    ```

## Upgrade the kubernetes version of the work cluster using the platform UI

Log in to the UI management interface of DCE 5.0, and upgrade the self-built work cluster of the platform
by following [cluster upgrade documentation](../../kpanda/user-guide/clusters/upgrade-cluster).
