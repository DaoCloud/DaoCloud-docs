# Offline Install in a Standard Kubernetes Cluster

This page will guide you to install DCE Community package offline in a standard Kubernetes cluster, which is recommended in the production environment.

Click [Online Install DCE Community](../../../videos/install.md) to watch a video demo for online install.

## Preparation

- Prepare a Kubernetes cluster. For resources required, see [Cluster Resources for Installing DCE Community](../resources.md).

    - Create a StorageClass and set it the default SC
    - Install CoreDNS in the cluster
    - If there is only one node in the cluster, make sure you have removed taints for that node

- [Install Dependencies](../../install-tools.md).

    You must install certain versions of each dependency:

    - helm ≥ 3.11.1
    - skopeo ≥ 1.11.1
    - kubectl ≥ 1.25.6
    - yq ≥ 4.31.1

## Download and install

1. Download and decompress the offline package of DCE Community on the controller node of your kubernetes cluster, or download and decompress the offline package from [Download Center](../../../download/index.md).

    Take VERSION=0.10.0 as an example

    ```bash
    export VERSION=v0.10.0
    wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-$VERSION-amd64.tar
    tar -xvf offline-community-$VERSION-amd64.tar
    ```

2. Customize `clusterConfig.yaml`

    - If Console is exposed via NodePort (recommended only for PoC use cases), skip this step.

    - In non-public cloud environment (virtual/physical machine), please enable load balancer (metallb) to avoid NodePort instability caused by node IP changes. Plan your network carefully and set up 2 necessary VIPs. Here is an example of `clusterConfig.yaml`:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: metallb
            istioGatewayVip: 10.6.229.10/32
            insightVip: 10.6.229.11/32
          fullPackagePath: absolute-path-of-the-offline-directory # path for decompressed offline package
          imagesAndCharts: # image registry
            type: external
            externalImageRepo: your-external-registry # image registry address, must be http or https
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
         ```

     - If it is a public cloud environment that already has a Kubernetes load balancer, set `clusterConfig.yaml` as follows:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: cloudLB
          fullPackagePath: absolute-path-of-the-offline-directory # path for decompressed offline package
          imagesAndCharts: # image registry
            type: external
            externalImageRepo: your-external-registry # image registry address, must be http or https
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
        ```

     - If Console is exposed via NodePort (recommended only for PoC use cases), set `clusterConfig.yaml` as follows:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: NodePort
          fullPackagePath: absolute-path-of-the-offline-directory # path for decompressed offline package
          imagesAndCharts: # image registry
            type: external
            externalImageRepo: your-external-registry # image registry address, must be http or https
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
         ```

3. Install DCE 5.0.

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```

    !!! note

        - Parameter `-p` specifies the offline directory to decompress the offline package.
        - For `clusterConfig.yaml` file settings, refer to [Online Installation](online.md#_2).
        - `-z` minimal install
        - `-c` specifies the cluster configuration file. You don't need to specify `-c` when using NodePort to expose the console.
        - `-d` enable debug mode
        - `--serial` specifies that all installation tasks are executed serially

4. After the installation is complete, the command line will prompt that the installation is successful. Congratulations!
    
    Now you can use the **default account and password (admin/changeme)** to explore the new DCE 5.0 through the URL prompted on the screen!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        It's recommended to write down the prompted URL for your next visit.

5. Before fully explore the features of DCE 5.0, you need to apply for a license.
   The Community package is provided for free. All you need to do is to [apply for a free license](../../../dce/license0.md).
