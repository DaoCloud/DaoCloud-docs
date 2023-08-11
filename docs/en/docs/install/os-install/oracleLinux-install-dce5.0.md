# Installing DCE 5.0 Enterprise Package on OpenShift OCP

This document will guide you on how to install DCE 5.0 on OCP.

## Prerequisites

- DCE 5.0 supports Kubernetes versions v1.22.x, v1.23.x, v1.24.x, and v1.25.x by default.
- You already have an OCP environment with a version that is not lower than v1.22.x.
- Prepare a private container registry and ensure that the cluster can access it.
- Make sure you have enough resources. It is recommended to have at least 12 cores and 24 GB of available resources in the cluster.

## Offline Installation

1. Log in to the Control plane node via a bastion host.

2. Download the full mode offline package. You can download the latest version from the [Download Center](../../download/index.md).

    | CPU Architecture | Version | Download Link                                                                                          |
    | ---------------- | ------- | ----------------------------------------------------------------------------------------------------- |
    | AMD64            | v0.10.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-amd64.tar> |
    | ARM64            | v0.10.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-arm64.tar> |

    Once downloaded, extract the offline package:

    ```bash
    ## Example using the amd64 architecture offline package
    tar -xvf offline-v0.10.0-amd64.tar
    ```

3. Set up the [cluster configuration file clusterConfig.yaml](../commercial/cluster-config.md). You can find this file in the `offline/sample` directory of the offline package and modify it as needed.

    Reference configuration:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
      creationTimestamp: null
    spec:
      loadBalancer:
        type: metallb # metallb is recommended
        istioGatewayVip: 10.5.14.XXX/32
        insightVip: 10.5.14.XXX/32
      fullPackagePath: /home/offline # offline path
      imagesAndCharts:
        type: external
        externalImageRepo: http://10.5.14.XXX:XXXX # private registry url
        externalImageRepoUsername: admin
        externalImageRepoPassword: Harbor12345
    ```

4. Configure the manifest file (optional). You can find this file in the `offline/sample` directory of the offline package and modify it as needed.

    !!! note

        If you want to use `hwameiStor` as the StorageClass, make sure that there is no default StorageClass in the current cluster.
        If there is, it needs to be removed. If not removed, the default StorageClass needs to disable `hwameiStor` by changing the value of `enable` to `false`.

5. Start installing DCE 5.0.

    ```bash
    ./offline/dce5-installer install-app -m ./offline/sample/manifest.yaml -c ./offline/sample/clusterConfig.yaml --platform openshift -z
    ```

    !!! note

        Here are some parameter descriptions. You can view more parameters by using `./dce5-installer --help`:

        - `-z` Minimal installation
        - `-c` Specify the cluster configuration file. It is not necessary to specify -c when exposing the console using NodePort.
        - `-d` Enable debug mode
        - `--platform` Declare on which Kubernetes distribution DCE 5.0 is deployed. Currently, only openshift is supported.
        - `--serial` Specify to execute all installation tasks in serial order.

6. After the installation is complete, the command line will prompt a successful installation. Congratulations! :smile: Now you can explore the brand new DCE 5.0 using the default account and password (admin/changeme) provided in the prompt URL!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please record the provided URL for future access.

7. After successfully installing DCE 5.0 Enterprise Package, please contact us for authorization: email [info@daocloud.io](mailto:info@daocloud.io) or call 400 002 6898.
