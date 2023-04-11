# Use a k8s cluster to install the community edition online

This page briefly explains the online installation steps for DCE 5.0 Community Edition.

!!! note

    - Click [Online Install Community Edition](../../../videos/install.md) to watch a video demo.
    - If offline installation is required, please refer to [Offline Installation Steps](offline.md).

## Preparation

- Prepare a K8s cluster. For cluster configuration, please refer to the document [Cluster Resource Planning](../resources.md).

    !!! note

        - Storage: StorageClass needs to be prepared in advance and set as the default SC
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

1. Download the dce5-installer binary file on the control plane node (Master node) of the K8s cluster (you can also [download via browser](../../../download/dce5.md)).

    ```shell
    # Assume VERSION is v0.3.30
    export VERSION=v0.3.30
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    ```

    Add executable permissions for `dce5-installer`:

    ```bash
    chmod +x dce5-installer
    ```

2. Set the configuration file clusterConfig.yaml

    - If using NodePort to expose the console (recommended only for PoC), go to the next step directly.

    - If it is a non-public cloud environment (virtual machine, physical machine), please enable load balancing (metallb) to avoid NodePort instability caused by node IP changes. Please plan your network carefully and set up 2 necessary VIPs. The configuration file example is as follows:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: metallb 
            istioGatewayVip: 10.6.229.10/32 # (1)
            insightVip: 10.6.229.11/32 # (2)
        ```

        1. VIP of Istio gateway, also browser access IP of DCE 5.0 console
        2. The VIP used by the Insight-Server of the global service cluster to collect the network paths of all sub-cluster monitoring indicators

    - If it is a public cloud environment and provides the K8s load balancing capability of the public cloud through the pre-prepared Cloud Controller Manager mechanism, the configuration file example is as follows:

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: cloudLB
        ```

3. Install DCE 5.0.

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```

    !!! note

        If a NodePort is used to expose the console, the command does not need to specify the `-c` parameter.

4. After the installation is complete, the command line will prompt that the installation is successful. congratulations! :smile: Now you can use the **default account and password (admin/changeme)** to explore the new DCE 5.0 through the URL prompted on the screen!

    

    !!! success

        Please record the prompted URL for your next visit.

5. In addition, after successfully installing DCE 5.0, you need genuine authorization to use it. Please refer to [Apply for free community experience](../../../dce/license0.md).
