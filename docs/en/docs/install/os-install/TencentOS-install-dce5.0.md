# Deploy DCE 5.0 Enterprise on TencentOS Server 3.1

This document will guide you on how to deploy DCE 5.0 on TencentOS Server 3.1.
Installer v0.9.0 and higher versions support this deployment method.

## Prerequisites

- Read the [Deployment Architecture](../commercial/deploy-arch.md) beforehand to confirm the deployment mode.
- Read the [Deployment Requirements](../commercial/deploy-requirements.md) beforehand to verify if the network, hardware, and ports meet the requirements.
- Read the [Preparation](../commercial/prepare.md) beforehand to ensure machine resources and pre-checks.

## Offline Installation

1. Download the full mode offline package. You can download the latest version
   from the [Download Center](../../download/index.md).

    | CPU Architecture | Version | Download Link                                                                                 |
    | ---------------- | ------- | --------------------------------------------------------------------------------------------- |
    | AMD64            | v0.9.0  | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-amd64.tar> |

    After downloading, extract the offline package:

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-amd64.tar
    tar -xvf offline-v0.9.0-amd64.tar
    ```

2. Download the TencentOS Server 3.1 image file.

    ```bash
    curl -LO http://mirrors.tencent.com/tlinux/3.1/iso/x86_64/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso
    ```

3. Download the TencentOS Server 3.1 osPackage offline package.

    ```bash
    curl -LO https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-tencent31-v0.6.6.tar.gz
    ```

4. Download the addon offline package. You can download the latest version from the [Download Center](../../download/index.md) (optional).

5. Set up the [clusterConfig.yaml](../commercial/cluster-config.md). You can find this file in the `offline/sample` directory
   of the offline package and modify it as needed. The reference configuration is as follows:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: tencent-cluster
      loadBalancer:
        type: metallb
        istioGatewayVip: 172.30.41.XXX/32
        insightVip: 172.30.41.XXX/32
      masterNodes:
        - nodeName: "g-master"
          ip: 172.30.41.XXX
          ansibleUser: "root"
          ansiblePass: "******"
      fullPackagePath: "/root/workspace/offline"
      osRepos:
        type: builtin
        isoPath: "/root/workspace/iso/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso"
        osPackagePath: "/root/workspace/os-pkgs/os-pkgs-tencent31-v0.6.1.tar.gz"
      imagesAndCharts:
        type: builtin
      binaries:
        type: builtin
      kubeanConfig: |-
        allow_unsupported_distribution_setup: true
        redhat_os_family_extensions:
          - "TencentOS"
    ```

    !!! note

        - TencentOS Server 3.1 belongs to the Redhat system family, so you need to define the
          `redhat_os_family_extensions` parameter in kubeanConfig.
        - Run the following command to check the OS Family identifier for TencentOS Server 3.1.
          The output should be `TencentOS`.

            ```bash
            export USER=root
            export PASS=dangerous
            export ADDR=172.30.41.166
            export ANSIBLE_HOST_KEY_CHECKING=False
            ansible -m setup -a 'filter=ansible_os_family' -e "ansible_user=${USER} ansible_password=${PASS}" -i ${ADDR}, all
            ```

6. Start installing DCE 5.0.

    ```bash
    ./dce5-installer cluster-create -m ./sample/mainfest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        Here are some parameter descriptions. For more parameters, you can use `./dce5-installer --help` to view:

        - `-z`: Minimize installation
        - `-c`: Specify the cluster configuration file. Not required when exposing the console using NodePort.
        - `-d`: Enable debug mode
        - `--serial`: Execute all installation tasks sequentially

7. After the installation is complete, the command line will prompt a successful installation. Congratulations! :smile: Now you can explore the brand new DCE 5.0 using the default account and password (admin/changeme) provided in the URL shown on the screen.

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please make a note of the provided URL for future access.

8. After successfully installing DCE 5.0 Enterprise, please contact us for authorization: email [info@daocloud.io](mailto:info@daocloud.io) or call 400 002 6898.
