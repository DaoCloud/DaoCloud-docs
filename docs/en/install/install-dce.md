# Install DCE 5.0

This page describes the installation procedure of DCE 5.0.

!!! note

    Click to [watch installation video](../videos/install.md).

## Preparation

- Prepare a k8s cluster. See [how to deploy a k8s cluster](install-k8s.md)

    !!! note

        - Available cluster resources: CPU > 10 cores, memory > 12 GB, remained storage space > 100 GB (currently, DCE 5.0 provides multiple replicas by default. If you choose a single replica, the resource consumption can be reduced to 2 cores and 4 GB)
        - Kubernetes version: The latest stable version is recommended. It supports v1.21 to v1.24 currrently.
        - Supported CRIs: Docker and containerd
        - Storage: Prepare StorageClass and set it to the default. For details see [how to deploy a k8s cluster](install-k8s.md)
        - Only support X86_64 currently
        - Ensure your cluster has installed with CoreDNS
    
- Install [dependencies](install-tools.md)

    !!! note

        If you have installed all required dependencies in your cluster, ensure all your dependencies are correctly installed:

        - helm ≥ 3.9.4
        - skopeo ≥ 1.9.2
        - kubectl ≥ 1.22.0
        - yq ≥ 4.27.5

## Online installation (recommended)

1. On the k8s control plane (master node), download the dce5-installer binary package.

    ```shell
    # Assume VERSION is v0.3.12
    export VERSION=v0.3.12
    curl -Lo ./dce5-installer http://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-${VERSION}
    ```

    Add the executable permission to `dce5-installer`:

    ```bash
    chmod +x dce5-installer
    ```

2. Edit your `clusterConfig.yaml`

    - For a private cloud (virtual and physical machines), enable your load balancer (metallb) to avoid the NodePort instability caused by IP variations. Carefully plan your network and IP addresses. Here is an example for your reference:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        LoadBalancer: metallb
        istioGatewayVip: 10.6.229.10/32     # This is VIP for Istio gateway and is also the URL via which you can use DCE 5.0 on your web browser.
        insightVip: 10.6.229.11/32          # This is the VIP used by the Insight-Server of the Global cluster to collect logs, metrics, and traces of all sub-clusters.
        ```

    - For a public cloud, DCE integrates a Cloud Controller Manager to provide the load balancing capability for kubernetes. Here is an example for your reference:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        LoadBalancer: cloudLB
        ```

    - If you use NodePort to expose your console (for proof of concept (PoC)), you can skip the clusterConfig file and go to the next step.

3. Install DCE 5.0 Community Package.

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```
    
    !!! note

        If you use NodePort to expose your console, the flag `-c` is not required.

4. After installation, you will get a successful tip on your screen. Congratulations! :smile: Now you can explore DCE 5.0 via the URL shown on your screen.

    ![success](images/success.png)

    !!! note

        Please remember or mark down the on-screen URL for your next login.

## Air-gap installation

1. Download and unzip the air-gap package.

    ``` bash
    # Assume VERSION=0.3.12
    export VERSION=v0.3.12
    wget http://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-${VERSION}.tar
    tar -zxvf offline-community-${VERSION}.tar
    ```

2. Import the image.

    !!! note
        
        You can manually download the script in this step: http://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline_image_handler.sh

    - If you use a registry, push the air-gap package image to the registry.

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

    - If no any registry, copy the air-gap package to each node in your cluster and load it by running `docker load/nerdctl load`.

        ```shell
        # Specify the folder to unzip the air-gap package
        export OFFLINE_DIR=$(pwd)/offline
        # Load the image
        ./utils/offline_image_handler.sh load
        ```

3. Unzip and install.

    ``` shell
    ./dce5-installer install-app -c clusterConfig.yaml -p offline
    ```
    
    !!! note

        The flag `-p` specifies the air-gap folder to unzip the air-gap package.

        For clusterConfig.yaml, see **step 2 of online installation** as above.

4. After installation, you will get a successful tip on your screen. Congratulations! :smile: Now you can explore DCE 5.0 via the URL shown on your screen.

    ![success](images/success.png)

    !!! note

        Please remember or write down the on-screen URL for your next login.
