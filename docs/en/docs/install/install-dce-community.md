# Install DCE 5.0

This page describes the installation procedure of DCE 5.0.

!!! note

    Click to [watch installation video](../videos/install.md).

    For offline installation, see [offline installation](offline-install-community.md)

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

## Online installation (recommended)

1. On the k8s control plane (master node), download the dce5-installer binary package.

    ```shell
    # Assume VERSION is v0.3.30
    export VERSION=v0.3.30
    curl -Lo ./dce5-installer http://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-${VERSION}
    ```

    Add the executable permission to `dce5-installer`:

    ```bash
    chmod +x dce5-installer
    ```

2. Edit your `clusterConfig.yaml`.

    - For a private cloud (virtual and physical machines), enable your load balancer (metallb) to avoid the NodePort instability caused by IP variations. Carefully plan your network and IP addresses. Here is an example for your reference:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: metallb
            istioGatewayVip: 10.6.229.10/32     # This is VIP for Istio gateway and is also the URL via which you can use DCE 5.0 on your web browser.
            insightVip: 10.6.229.11/32          # This is the VIP used by the Insight-Server of the Global cluster to collect logs, metrics, and traces of all sub-clusters.
        ```

    - For a public cloud, DCE integrates a Cloud Controller Manager to provide the load balancing capability for kubernetes. Here is an example for your reference:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: cloudLB
        ```

    - If you use NodePort to expose your console (for proof of concept (PoC)), you can skip the clusterConfig file and go to the next step.

3. Install DCE 5.0 Community Package.

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```
    
    !!! note

        If you use NodePort to expose your console, the flag `-c` is not required.

4. After installation, you will get a success tip on your screen. Congratulations! :smile: Now you can explore DCE 5.0 via the URL shown on your screen.

    

    !!! note

        Please remember or mark down the on-screen URL for your next login.

## Install with kind

!!! note

    If you use a cluster with kind, only the NodePort mode is available.

1. Ensure the port 32000 has been exposed to port 8888 from your cluster to external when you create the cluster with kind. The kind profile looks like:
        
    ``` yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    spec:
      loadBalancer:
       type: cloudLB
    ```

2. Get IP of the host with kind, such as `10.6.3.1` to perform the installation:

    ```shell
    ./dce5-installer install-app -z -k 10.6.3.1:8888
    ```

3. After successful installation, you can go to `https://10.6.3.1:8888` to use DCE 5.0!
