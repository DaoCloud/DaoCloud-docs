# Use the Kubernetes cluster to install the community version online

This page briefly explains the online installation steps for DCE 5.0 Community Release.

!!! note

     - Click [Online Install Community Release](../../../videos/install.md) to watch a video demo.
     - If offline installation is required, please refer to [Offline Installation Steps](offline.md).

## Preparation

- Prepare a K8s cluster. For cluster configuration, please refer to the document [Cluster Resource Planning](../resources.md).

     !!! note

         - Storage: StorageClass needs to be prepared in advance and set as the default SC
         - Make sure the cluster has CoreDNS installed
         - If it is a single node cluster, make sure you have removed the taint for that node

- [Install Dependencies](../../install-tools.md).

     If all dependencies are installed in the cluster, make sure the dependency versions meet the requirements:

     - helm ≥ 3.11.1
     - skopeo ≥ 1.11.1
     - kubectl ≥ 1.25.6
     - yq ≥ 4.31.1

## Download and install

1. Download the dce5-installer binary file on the control plane node (Master node) of the K8s cluster (you can also [download via browser](../../../download/dce5.md)).

     Assume VERSION is v0.7.0.
     If it is an ARM architecture, please update `dce5-installer-$VERSION` to `dce5-installer-$VERSION-linux-arm64`.

     ```shell
     export VERSION=v0.7.0
     curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
     chmod +x ./dce5-installer
     ```

2. Set the configuration file clusterConfig.yaml

     - If using NodePort to expose the console (recommended only for PoC), go to the next step directly.

     - If it is a non-public cloud environment (virtual machine, physical machine), please enable load balancing (metallb) to avoid NodePort instability caused by node IP changes. Please plan your network carefully and set up 2 necessary VIPs. The configuration file example is as follows:

         ```yaml title="clusterConfig.yaml"
         apiVersion: provision.daocloud.io/v1alpha3
         kind: ClusterConfig
         spec:
           loadBalancer:
             type: metallb
             istioGatewayVip: 10.6.229.10/32 # (1)
             insightVip: 10.6.229.11/32 # (2)
         ```

         1. This is the VIP of the Istio gateway and also the browser access IP of the DCE 5.0 console
         2. The VIP used by the Insight-Server of the global service cluster to collect the network paths of all sub-cluster monitoring metrics

     - If it is a public cloud environment and provides the K8s load balancing capability of the public cloud through the pre-prepared Cloud Controller Manager mechanism, the configuration file example is as follows:

         ```yaml title="clusterConfig.yaml"
         apiVersion: provision.daocloud.io/v1alpha3
         kind: ClusterConfig
         spec:
           loadBalancer:
             type: cloudLB
         ```

3. Install DCE 5.0.

     ```shell
     ./dce5-installer install-app -c clusterConfig.yaml -z
     ```

     !!! note

         - Parameter -p specifies the offline directory to decompress the offline package.
         - For clusterConfig.yaml file settings, please refer to [Online Installation Step 2](online.md#_2).
         - `-z` minimal install
         - `-c` specifies the cluster configuration file. You don't need to specify `-c` when using NodePort to expose the console.
         - `-d` enable debug mode
         - `--serial` specifies that all installation tasks are executed serially

4. After the installation is complete, the command line will prompt that the installation is successful. congratulations!
    Now you can use the **default account and password (admin/changeme)** to explore the new DCE 5.0 through the URL prompted on the screen!

     ![Installation succeeded](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

     !!! success

         Please record the prompted URL for your next visit.

5. In addition, after successfully installing DCE 5.0, you need genuine authorization to use it. Please refer to [Apply for free community experience](../../../dce/license0.md).
