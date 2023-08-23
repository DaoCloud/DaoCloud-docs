# Install DCE 5.0 Enterprise on OpenShift OCP

This page describes how to install DCE 5.0 on OCP.

## Prerequisites

- The default Kubernetes versions supported by DCE 5.0 are v1.22.x, v1.23.x, v1.24.x, v1.25.x
- Already have an OCP environment, and the version is not lower than v1.22.x
- Prepare a private container registry and ensure that the cluster can access it
- Ensure sufficient resources, it is recommended that the cluster has at least 12 cores and 24 GB of available resources

## Offline installation

1. Log in to the Control plane node through the bastion host.

2. Download the full mode offline package, you can download the latest version in [Download Center](../../download/index.md).

     | CPU Architecture | Version | Download URL |
     | -------- | ------ | ------------------------------ -------------------------------------------------- -------------- |
     | AMD64 | v0.10.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-amd64.tar> |
     | ARM64 | v0.10.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-arm64.tar> |

     Unzip the offline package after downloading:

     ```bash
     ## Take the amd64 architecture offline package as an example
     tar -xvf offline-v0.10.0-amd64.tar
     ```

3. Set [clusterConfig.yaml](../commercial/cluster-config.md), which can be obtained under the offline package `offline/sample` and modified as needed.

     The reference configuration is:

     ```yaml
     apiVersion: provision.daocloud.io/v1alpha3
     kind: ClusterConfig
     metadata:
       creationTimestamp: null
     spec:
       loadBalancer:
         type: metallb # suggest metallb
         istioGatewayVip: 10.5.14.XXX/32
         insightVip: 10.5.14.XXX/32
       fullPackagePath: /home/offline # offline package directory
       imagesAndCharts:
         type: external
         externalImageRepo: http://10.5.14.XXX:XXXX # Private container registry address
         externalImageRepoUsername: admin
         externalImageRepoPassword: Harbor12345
     ```

4. Configure the manifest file (optional), which can be obtained under the offline package `offline/sample` and modified as needed.

     !!! note

         If you want to use `hwameiStor` as StorageClass, please make sure there is no default StorageClass in the current cluster.
         If present, it needs to be removed. If it is not removed, the default StorageClass needs to close `hwameiStor`, that is, change the value of enable to `fasle`.

5. Start the installation of DCE 5.0.

     ```bash
     ./offline/dce5-installer install-app -m ./offline/sample/manifest.yaml -c ./offline/sample/clusterConfig.yaml --platform openshift -z
     ```

     !!! note

         Some parameters are introduced, and more parameters can be viewed through `./dce5-installer --help`:

         - `-z` minimal install
         - `-c` specifies the cluster configuration file, and does not need to specify -c when using NodePort to expose the console
         - `-d` enable debug mode
         - `--platform` is used to declare which Kubernetes distribution to deploy DCE 5.0 on, currently only supports openshift
         - `--serial` specifies that all installation tasks are executed serially

6. After the installation is complete, the command line will prompt that the installation is successful. congratulations! :smile: Now you can use the default account and password (admin/changeme) to explore the new DCE 5.0 through the URL prompted on the screen!

     ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

     !!! success

         Please record the prompted URL for your next visit.

7. After successfully installing DCE 5.0 Enterprise Package, please contact us for authorization: email [info@daocloud.io](mailto:info@daocloud.io) or call 400 002 6898.
