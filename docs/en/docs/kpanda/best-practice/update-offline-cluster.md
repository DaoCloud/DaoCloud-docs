---
MTPE: windsonsea
Date: 2024-10-25
---

# Offline Deployment/Upgrade Guide for Worker Clusters

!!! note

    This document is specifically designed for deploying or upgrading the Kubernetes version of worker clusters created on the DCE 5.0 platform in offline mode. It does not cover the deployment or upgrade of other Kubernetes components.

This guide is applicable to the following offline scenarios:

- You can follow the operational guidelines to deploy the recommended Kubernetes version in a non-GUI environment created by the DCE 5.0 platform.
- You can upgrade the Kubernetes version of worker clusters created using the DCE 5.0 platform by generating incremental offline packages.

The overall approach is as follows:

1. Build the offline package on an integrated node.
2. Import the offline package to the bootstrap node.
3. Update the Kubernetes version manifest for the [global service cluster](../user-guide/clusters/cluster-role.md#global-service-cluster).
4. Use the DCE 5.0 UI to create or upgrade the Kubernetes version of the worker cluster.

!!! note

    For a list of currently supported offline Kubernetes versions, refer to the [list of Kubernetes versions supported by Kubean](../../community/kubean.md#kubernetes-compatibility).

## Building the Offline Package on an Integrated Node

Since the offline environment cannot connect to the internet, you need to prepare an **integrated node** in advance to build the incremental offline package and start Docker or Podman services on this node. Refer to [How to Install Docker?](../../blogs/2023/230315-install-on-linux.md)

1. Check the status of the Docker service on the integrated node.

    ```bash
    ps aux | grep docker
    ```

    You should see output similar to the following:

    ```console
    root     12341  0.5  0.2 654372 26736 ?        Ssl  23:45   0:00 /usr/bin/docked
    root     12351  0.2  0.1 625080 13740 ?        Ssl  23:45   0:00 docker-containerd --config /var/run/docker/containerd/containerd.toml
    root     13024  0.0  0.0 112824   980 pts/0    S+   23:45   0:00 grep --color=auto docker
    ```

2. Create a file named __manifest.yaml__ in the __/root__ directory of the integrated node with the following command:

    ```bash
    vi manifest.yaml
    ```

    The content of __manifest.yaml__ should be as follows:

    ```yaml title="manifest.yaml"
    image_arch:
    - "amd64"
    kube_version: # Specify the version of the cluster to be upgraded
    - "v1.28.0"
    ```

    - __image_arch__ specifies the CPU architecture type, with options for __amd64__ and __arm64__.
    - __kube_version__ indicates the version of the Kubernetes offline package to be built. You can refer to the supported offline Kubernetes versions mentioned earlier.

3. Create a folder named __/data__ in the __/root__ directory to store the incremental offline package.

    ```bash
    mkdir data
    ```

    Run the following command to generate the offline package using the kubean `airgap-patch` image. Make sure the tag of the `airgap-patch` image matches the Kubean version, and that the Kubean version covers the Kubernetes version you wish to upgrade.

    ```bash
    # Assuming the Kubean version is v0.13.9
    docker run --rm -v $(pwd)/manifest.yaml:/manifest.yaml -v $(pwd)/data:/data ghcr.m.daocloud.io/kubean-io/airgap-patch:v0.13.9
    ```

    After the Docker service completes running, check the files in the __/data__ folder. The folder structure should look like this:

    ```console
    data
    ├── amd64
    │   ├── files
    │   │   ├── import_files.sh
    │   │   └── offline-files.tar.gz
    │   ├── images
    │   │   ├── import_images.sh
    │   │   └── offline-images.tar.gz
    │   └── os-pkgs
    │       └── import_ospkgs.sh
    └── localartifactset.cr.yaml
    ```

## Importing the Offline Package to the Bootstrap Node

1. Copy the __/data__ files from the integrated node to the __/root__ directory of the bootstrap node. On the **integrated node** , run the following command:

    ```bash
    scp -r data root@x.x.x.x:/root
    ```

    Replace `x.x.x.x` with the IP address of the bootstrap node.

2. On the bootstrap node, copy the image files in the __/data__ folder to the built-in Docker registry of the bootstrap node. After logging into the bootstrap node, run the following commands:

    1. Navigate to the directory where the image files are located.
    
        ```bash
        cd data/amd64/images
        ```

    2. Run the __import_images.sh__ script to import the images into the built-in Docker Registry of the bootstrap node.
   
        ```bash
        REGISTRY_ADDR="127.0.0.1" ./import_images.sh
        ```

    !!! note

        The above command is only applicable to the built-in Docker Registry of the bootstrap node. If you are using an external registry, use the following command:
        
        ```shell
        REGISTRY_SCHEME=https REGISTRY_ADDR=${registry_address} REGISTRY_USER=${username} REGISTRY_PASS=${password} ./import_images.sh
        ```

        - REGISTRY_ADDR is the address of the image repository, such as 1.2.3.4:5000.
        - If the image repository requires username and password authentication, set REGISTRY_USER and REGISTRY_PASS accordingly.

3. On the bootstrap node, copy the binary files in the __/data__ folder to the built-in Minio service of the bootstrap node.

    1. Navigate to the directory where the binary files are located.
    
        ```bash
        cd data/amd64/files/
        ```

    2. Run the __import_files.sh__ script to import the binary files into the built-in Minio service of the bootstrap node.
    
        ```bash
        MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_files.sh http://127.0.0.1:9000
        ```

!!! note

    The above command is only applicable to the built-in Minio service of the bootstrap node. If you are using an external Minio, replace `http://127.0.0.1:9000` with the access address of the external Minio. "rootuser" and "rootpass123" are the default account and password for the built-in Minio service of the bootstrap node.

## Updating the Kubernetes Version Manifest for the Global Service Cluster

Run the following command on the bootstrap node to deploy the `localartifactset` resource to the global service cluster:

```bash
kubectl apply -f data/kubeanofflineversion.cr.patch.yaml
```

## Next Steps

Log into the DCE 5.0 UI management interface to continue with the following actions:

1. Refer to the [Creating Cluster Documentation](../user-guide/clusters/create-cluster.md) to create a worker cluster, where you can select the incremental version of Kubernetes.

2. Refer to the [Upgrading Cluster Documentation](../user-guide/clusters/upgrade-cluster.md) to upgrade your self-built worker cluster.
