# Use the Kubernetes cluster to install the community edition offline

This page briefly describes the offline installation steps for DCE 5.0 Community Release.

Click [Community Release Deployment Demo](../../../videos/install.md) to watch a video demo.

## Preparation

- Prepare a Kubernetes cluster. For cluster configuration, please refer to the document [Resource Planning](../resources.md).

     !!! note

         - Storage: StorageClass needs to be prepared in advance and set as the default SC
         - Make sure the cluster has CoreDNS installed
         - If it is a single node cluster, make sure you have removed the taint for that node

- [Install Dependencies](../../install-tools.md).

     !!! note

         If all dependencies are installed in the cluster, make sure the dependency versions meet the requirements:
        
         - helm ≥ 3.11.1
         - skopeo ≥ 1.11.1
         - kubectl ≥ 1.25.6
         - yq ≥ 4.31.1

## Download and install

1. Download and decompress the corresponding offline package of the community version on the k8s cluster control plane node (Master node), or download and decompress the offline package from [Download Center](../../../download/dce5.md).

     Assume version VERSION=0.7.0

     ```bash
     export VERSION=v0.7.0
     wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-$VERSION-amd64.tar
     tar -xvf offline-community-$VERSION-amd64.tar
     ```

1. Set the cluster configuration file clusterConfig.yaml

     - If it is a non-public cloud environment (virtual machine, physical machine), please enable load balancing (metallb) to avoid NodePort instability caused by node IP changes. Please plan your network carefully and set up 2 necessary VIPs. The configuration file example is as follows:

         ```yaml title="clusterConfig.yaml"
         apiVersion: provision.daocloud.io/v1alpha3
         kind: ClusterConfig
         spec:
           loadBalancer:
             type: metallb
             istioGatewayVip: 10.6.229.10/32
             insightVip: 10.6.229.11/32
           fullPackagePath: absolute-path-of-the-offline-directory # The path after decompressing the offline package
           imagesAndCharts: # mirror warehouse
             type: external
             externalImageRepo: your-external-registry # Mirror repository address, must be http or https
             # externalImageRepoUsername: admin
             # externalImageRepoPassword: Harbor123456
         ```

     - If it is a public cloud environment and provides the k8s load balancing capability of the public cloud through the pre-prepared Cloud Controller Manager mechanism, the configuration file example is as follows:

         ```yaml title="clusterConfig.yaml"
         apiVersion: provision.daocloud.io/v1alpha3
         kind: ClusterConfig
         spec:
           loadBalancer:
             type: cloudLB
           fullPackagePath: absolute-path-of-the-offline-directory # The path after decompressing the offline package
           imagesAndCharts: # mirror warehouse
             type: external
             externalImageRepo: your-external-registry # Mirror repository address, must be http or https
             # externalImageRepoUsername: admin
             # externalImageRepoPassword: Harbor123456
         ```

     - If NodePort is used to expose the console (only recommended for PoC), the configuration file example is as follows:

         ```yaml title="clusterConfig.yaml"
         apiVersion: provision.daocloud.io/v1alpha3
         kind: ClusterConfig
         spec:
           loadBalancer:
             type: NodePort
           fullPackagePath: absolute-path-of-the-offline-directory # The path after decompressing the offline package
           imagesAndCharts: # mirror warehouse
             type: external
             externalImageRepo: your-external-registry # Mirror repository address, must be http or https
             # externalImageRepoUsername: admin
             # externalImageRepoPassword: Harbor123456
         ```

1. Install DCE 5.0.

     ```shell
     ./dce5-installer install-app -c clusterConfig.yaml
     ```

     !!! note

         - For clusterConfig.yaml file settings, please refer to [Online Installation Step 2](online.md#_2).
         - `-z` minimal install
         - `-c` specifies the cluster configuration file. You don't need to specify `-c` when using NodePort to expose the console.
         - `-d` enable debug mode
         - `--serial` specifies that all installation tasks are executed serially

1. After the installation is complete, the command line will prompt that the installation is successful. congratulations!
    Now you can use the default account and password (admin/changeme) to explore the new DCE 5.0 through the URL prompted on the screen!

    ![Installation succeeded](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

     !!! success

         Please record the prompted URL for your next visit.

1. In addition, after successfully installing DCE 5.0, you need genuine authorization to use it, please refer to [Apply for free community experience](../../../dce/license0.md).
