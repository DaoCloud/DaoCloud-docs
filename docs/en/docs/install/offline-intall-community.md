# Air-gap Installation of DCE 5.0

This page describes the air-gap (offline) installation procedure of DCE 5.0.

!!! note

    Click to [watch installation video](../videos/install.md).

## Preparation

- Prepare a k8s cluster.

    !!! note

        - Available cluster resources: CPU > 10 cores, memory > 12 GB, remained storage space > 100 GB (currently, DCE 5.0 provides multiple replicas by default. If you choose a single replica, the resource requirement can be reduced to 4 cores and 8 GB).
        - Kubernetes version: The latest stable version is recommended. It supports v1.20 to v1.24 currrently.
        - Supported CRIs: Docker and containerd.
        - Storage: Prepare StorageClass and set it to the default.
        - Only support X86_64 currently.
        - Ensure your cluster has installed with CoreDNS.
        - If a cluster with a single node, ensure you have removed the taint labels from the node.
    
- Install [dependencies](install-tools.md)

    !!! note

        If you have installed all required dependencies in your cluster, ensure all your dependencies are correctly installed:

        - helm ≥ 3.9.4
        - skopeo ≥ 1.9.2
        - kubectl ≥ 1.22.0
        - yq ≥ 4.27.5

## Air-gap installation

1. Download and unzip the air-gap package.

    ``` bash
    # Assume VERSION=0.3.20
    export VERSION=v0.3.20
    wget http://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-${VERSION}.tar
    tar -zxvf offline-community-${VERSION}.tar
    ```

2. Import the image.

    - Download the image and import the script.

        ```bash
        wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline_image_handler.sh
        ```

        Add the executable permission with `offline_image_handler.sh`:

        ```bash
        chmod +x offline_image_handler.sh
        ```

    - If you already have a registry, push the air-gap package image to the registry.

        Assuming the existing registry access is `registry.daocloud.io:30080`

        ```bash
        # Specify the registry URL
        export REGISTRY_ADDR=registry.daocloud.io:30080
        # Specify the folder to unzip the air-gap package
        export OFFLINE_DIR=$(pwd)/offline
        # Import the image
        ./utils/offline_image_handler.sh import
        ```

        !!! note

            If failed to import the image, the failure will be skipped and the script will continue to run.
            The failure log will be recorded in the `import_image_failed.list` file.

            If you get an error `http: server gave HTTP response to HTTPS client` when running `docker pull`, enable `Insecure Registry`. 
            
            - On each node of your cluster, run `vim /etc/docker/daemon.json` to edit `daemon.json` and input the content below to save your changes.

                ```shell
                {
                "insecure-registries" : ["172.30.120.180:80"]
                }
                ```

                !!! note

                    Ensure you shall replace `172.30.120.180:80` with your own Harbor registry address. For Linux, the path to `daemon.json` is `/etc/docker/daemon.json`.

            - Run the following commands to restart Docker.

                ```bash
                sudo systemctl daemon-reload
                sudo systemctl restart docker
                ```

    - If no any registry, copy the air-gap package to each node in your cluster and load it by running `docker load/nerdctl load`.

        ```shell
        # Specify the folder to unzip the air-gap package
        export OFFLINE_DIR=$(pwd)/offline
        # Load the image
        ./offline_image_handler.sh load
        ```

3. On the k8s control plane (master node), download the dce5-installer binary package.

    ```shell
    # Assume VERSION is v0.3.20
    export VERSION=v0.3.20
    curl -Lo ./dce5-installer http://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-${VERSION}
    ```

    Add the executable permission to `dce5-installer`:

    ```bash
    chmod +x dce5-installer
    ```
    
4. Edit your `clusterConfig.yaml`.

    - For a private cloud (virtual and physical machines), enable your load balancer (metallb) to avoid the NodePort instability caused by IP variations. Carefully plan your network and IP addresses. Here is an example for your reference:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: metallb
            istioGatewayVip: 10.6.229.10/32     # This is VIP for Istio gateway and is also the URL via which you can use DCE 5.0 on your web browser.
            insightVip: 10.6.229.11/32          # This is the VIP used by the Insight-Server of the Global cluster to collect logs, metrics, and traces of all sub-clusters.
          registry:
            type: external
            externalRegistry: registry.daocloud.io:30080
        ```

    - For a public cloud, DCE integrates a Cloud Controller Manager to provide the load balancing capability for kubernetes. Here is an example for your reference:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: cloudLB
          registry:
            type: external
            externalRegistry: registry.daocloud.io:30080 # Replace with your Harbor registry address
        ```

    - If you use NodePort to expose your console (for proof of concept (PoC)), refer to the following example:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: NodePort
          registry:
            type: external
            externalRegistry: registry.daocloud.io:30080 # Replace with your Harbor registry address
        ```

5. Unzip and install.

    ``` shell
    ./dce5-installer install-app -c clusterConfig.yaml -p offline
    ```
    
    !!! note

        The flag `-p` specifies the air-gap folder to unzip the air-gap package.

        For clusterConfig.yaml, see **step 2 of online installation** as above.

6. After installation, you will get a success tip on your screen. Congratulations! :smile: Now you can explore DCE 5.0 via the URL shown on your screen.

    

    !!! note

        Please remember or write down the on-screen URL for your next login.

7. Before use, you may need to [apply for a free trial](../dce/license0.md).
