---
MTPE: windsonsea
date: 2024-09-09
---

# Offline Install in a Standard Kubernetes Cluster

This page will guide you to install DCE Community package offline in a standard Kubernetes cluster, which is recommended in the production environment.

## Preparation

- Prepare a machine with internet access.

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

1. Find a machine with internet access and run the command below to download and extract the
   offline package (or download it from the [download center](../../../download/index.md)):

    Take VERSION=v0.33.0 as an example.

    ```bash
    export VERSION=v0.33.0
    wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-$VERSION-amd64.tar
    tar -xvf offline-community-$VERSION-amd64.tar
    ```

1. Upload the extracted files to the K8s control plane node (Controller Node) and configure `clusterConfig.yaml` on that node.

    - For non-public cloud environments (VMs or physical machines), enable load balancing (Metallb) to avoid instability caused by NodePort due to changing node IPs. Carefully plan your network and set up 2 necessary VIPs. Here is a sample configuration:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: metallb
            istioGatewayVip: 10.6.229.10/32
            insightVip: 10.6.229.11/32
          fullPackagePath: absolute-path-of-the-offline-directory # (1)!
          imagesAndCharts: # (2)!
            type: external 
            externalImageRepo: your-external-registry # (3)!
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
        ```

        1. Path after extracting the offline package
        2. Container registry
        3. Container registry address, must be http or https

    - For public cloud environments that provide Kubernetes load balancing through a pre-configured Cloud Controller Manager, use the following sample configuration:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: cloudLB
          fullPackagePath: absolute-path-of-the-offline-directory # (1)!
          imagesAndCharts: # (2)!
            type: external
            externalImageRepo: your-external-registry # (3)!
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
        ```

        1. Path after extracting the offline package
        2. Container registry
        3. Container registry address, must be http or https

    - If using NodePort to expose the console (only recommended for PoC), use the following sample configuration:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: NodePort
          fullPackagePath: absolute-path-of-the-offline-directory # (1)!
          imagesAndCharts: # (2)!
            type: external 
            externalImageRepo: your-external-registry # (3)!
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
        ```

        1. Path after extracting the offline package
        2. Container registry
        3. Container registry address, must be http or https

1. Install DCE 5.0.

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```

    !!! note

        - For `clusterConfig.yaml` file settings, refer to [the previous step](#download-and-install).
        - `-z` minimal install
        - `-c` specifies the cluster configuration file. You don't need to specify `-c` when using NodePort to expose the console.
        - `-d` enable debug mode
        - `--serial` specifies that all installation tasks are executed serially

1. After the installation is complete, the command line will prompt that the installation is successful. Congratulations!
    
    Now you can use the **default account and password (admin/changeme)** to explore the new DCE 5.0 through the URL prompted on the screen!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        It's recommended to write down the prompted URL for your next visit.

1. Before fully explore the features of DCE 5.0, you need to apply for a license.
   The Community package is provided for free. All you need to do is to
   [apply for a free license](../../../dce/license0.md).
