# Use a k8s cluster to install the community edition offline

This page briefly describes the offline installation steps for DCE 5.0 Community Edition.

!!! note

    Click [Community Edition Deployment Demo](../../../videos/install.md) to watch a video demo.

## Preparation

- Prepare a Kubernetes cluster. For cluster configuration, please refer to the document [Resource Planning](../resources.md).

    !!! note

        Storage: StorageClass needs to be prepared in advance and set as the default SC

            - Make sure the cluster has CoreDNS installed
            - If it is a single node cluster, make sure you have removed the taint for that node

- [Install Dependencies](../../install-tools.md).

    !!! note

        If all dependencies are installed in the cluster, make sure the dependency versions meet the requirements:

        - helm ≥ 3.9.4
        - skopeo ≥ 1.9.2
        - kubectl ≥ 1.22.0
        - yq ≥ 4.27.5

## Download and install

1. Download and decompress the corresponding offline package of the community version on the k8s cluster control plane node (Master node), or download and decompress the offline package from [Download Center](../../../download/dce5.md).

    ```bash
    # Assume version VERSION=0.3.30
    export VERSION=v0.3.30
    wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-community-$VERSION-amd64.tar
    tar -zxvf offline-centos7-community-$VERSION-amd64.tar
    ```

2. Import the image.

    - Download image import script.

        ```bash
        wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline_image_handler.sh
        ```

        Add executable permissions for `offline_image_handler.sh`:

        ```bash
        chmod +x offline_image_handler.sh
        ```

    - If using a container registry, please push the image of the offline package to the container registry.

        ```bash
        # Specify the address of the container registry, for example:
        export REGISTRY_ADDR=registry.daocloud.io:30080
        # Specify the offline package decompression directory, for example:
        export OFFLINE_DIR=$(pwd)/offline
        # Execute the script to import the image
        ./offline_image_handler.sh import
        ```

        !!! note

            - If the process of importing the image fails, the failure will be skipped and the script will continue to execute.
            - The failed image information will be recorded in the `import_image_failed.list` file in the same directory as the script, for easy location.
            - If the docker pull image reports an error: http: server gave HTTP response to HTTPS client, please enable Insecure Registry.

    - Run the `vim /etc/docker/daemon.json` command on each node of the cluster to edit the daemon.json file, enter the following and save the changes.

        ```json title="daemon.json"
        {
        "insecure-registries" : ["172.30.120.180:80"]
        }
        ```

        !!! note

            Make sure to replace `172.30.120.180:80` with your own Harbor repository address.
            For Linux, the path to the daemon.json file is `/etc/docker/daemon.json`.

    - Run the following command to restart Docker.

        ```bash
        sudo systemctl daemon-reload
        sudo systemctl restart docker
        ```

    - If there is no container registry, please copy the offline package to each node and load it through `docker load/nerdctl load` command:

        ```shell
        # Specify the offline package decompression directory
        export OFFLINE_DIR=$(pwd)/offline
        # Execute the script to load the image
        ./offline_image_handler.sh load
        ```

3. Download the dce5-installer binary file on the k8s cluster control plane node (Master node).

    ```shell
    # Assume VERSION is v0.3.28
    export VERSION=v0.3.28
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    ```

    Add executable permissions for `dce5-installer`:

    ```bash
    chmod +x dce5-installer
    ```

4. Set the cluster configuration file clusterConfig.yaml

    - If it is a non-public cloud environment (virtual machine, physical machine), please enable load balancing (metallb) to avoid NodePort instability caused by node IP changes. Please plan your network carefully and set up 2 necessary VIPs. The configuration file example is as follows:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: metallb
            istioGatewayVip: 10.6.229.10/32 # (1)
            insightVip: 10.6.229.11/32 # (2)
          registry:
            type: external
            externalRegistry: registry.daocloud.io:30080 # (3)
        ```

        1. This is the VIP of Istio gateway, and it will also be the browser access IP of DCE 5.0 console
        2. This is the VIP used by the Insight-Server of the Global cluster to collect the monitoring indicators of all sub-clusters on the network path
        3. Your Harbor or registry domain name or IP

    - If it is a public cloud environment and provides the k8s load balancing capability of the public cloud through the pre-prepared Cloud Controller Manager mechanism, the configuration file example is as follows:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: cloudLB
          registry:
            type: external
            externalRegistry: registry.daocloud.io:30080 # (1)
        ```

        1. Your Harbor or registry domain name or IP

    - If NodePort is used to expose the console (only recommended for PoC), the configuration file example is as follows:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: NodePort
          registry:
            type: external
            externalRegistry: registry.daocloud.io:30080 # (1)
        ```

        1. Your Harbor or registry domain name or IP

5. Unzip and install.

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml -p offline
    ```

    !!! note

        - Parameter -p specifies the offline directory to decompress the offline package.
        - For clusterConfig.yaml file settings, please refer to [Online Installation Step 2](online.md#_2).

6. After the installation is complete, the command line will prompt that the installation is successful. congratulations! :smile: Now you can use the default account and password (admin/changeme) to explore the new DCE 5.0 through the URL prompted on the screen!

    

    !!! success

        Please record the prompted URL for your next visit.

7. In addition, after successfully installing DCE 5.0, you need genuine authorization to use it, please refer to [Apply for free community experience](../../../dce/license0.md).
