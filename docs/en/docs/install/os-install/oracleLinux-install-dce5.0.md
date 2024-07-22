# Deploy DCE 5.0 Enterprise on Oracle Linux R9/R8 U1

This page will guide you on how to deploy DCE 5.0 on Oracle Linux R9/R8 U1.
Installer v0.8.0 and higher versions support this deployment method.

## Prerequisites

- Read the [Deployment Architecture](../commercial/deploy-arch.md) in advance to
  confirm the deployment mode for this installation.
- Read the [Deployment Requirements](../commercial/deploy-requirements.md)
  in advance to ensure that the network, hardware, and ports meet the requirements.
- Read the [Preparation](../commercial/prepare.md) in advance to verify
  machine resources and pre-checks.

## Offline Installation

1. Download the full mode offline package. You can download the latest version
   from the [Download Center](../../download/index.md).

    | CPU Architecture | Version | Download Link |
    | ---------------- | ------- | ------------- |
    | AMD64            | v0.17.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar> |

    After downloading, extract the offline package:

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar
    tar -xvf offline-v0.17.0-amd64.tar
    ```

2. Download the Oracle Linux R9/R8 U1 image file.

    ```bash
    # Oracle Linux R9 U1
    curl -LO https://yum.oracle.com/ISOS/OracleLinux/OL9/u1/x86_64/OracleLinux-R9-U1-x86_64-dvd.iso

    # Oracle Linux R8 U1
    curl -LO https://yum.oracle.com/ISOS/OracleLinux/OL8/u7/x86_64/OracleLinux-R8-U7-x86_64-dvd.iso
    ```

3. Download the Oracle Linux R9/R8 U1 osPackage offline package.

    ```bash
    # Oracle Linux R9 U1
    curl -LO https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-oracle9-v0.13.9.tar.gz

    # Oracle Linux R8 U1
    curl -LO https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-oracle8-v0.13.9.tar.gz
    ```

4. Download the addon offline package. You can download the latest version from
   the [Download Center](../../download/index.md) (optional).

5. Set up the [cluster configuration file clusterConfig.yaml](../commercial/cluster-config.md).
   You can find this file in the `offline/sample` directory of the offline package and modify
   it as needed. The reference configuration is as follows:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: oracle-cluster
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
        isoPath: "/root/workspace/iso/OracleLinux-R9-U1-x86_64-dvd.iso"
        osPackagePath: "/root/workspace/os-pkgs/os-pkgs-oracle9-v0.5.4.tar.gz"
      imagesAndCharts:
        type: builtin
      binaries:
        type: builtin
      kubeanConfig: |-
        # Enable recommended sysctl settings to avoid 'too many open files' issues
        node_sysctl_tuning: true
        # Disable kubespray from installing public repo for Oracle Linux
        use_oracle_public_repo: false
    ```

    !!! note

        Due to an error with the `kpanda-controller-manager` component during installation,
        stating `failed to create fsnotify watcher: too many open files.`, it is necessary to
        set `node_sysctl_tuning: true` in the `clusterConfig.yaml` file.

7. Start the installation of DCE 5.0.

    ```bash
    ./dce5-installer cluster-create -m ./sample/manifest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        Here are some parameter introductions. You can refer to `./dce5-installer --help` for more parameters:

        - `-z`: Minimal installation
        - `-c`: Specify the cluster configuration file (not required when exposing the console using NodePort)
        - `-d`: Enable debug mode
        - `--serial`: Run all installation tasks in a serial manner

8. After the installation is complete, the command line will prompt for a successful installation.
   Congratulations! 🎉 Now you can explore the brand new DCE 5.0 using the default account and
   password (admin/changeme) provided in the URL shown on the screen.

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please make sure to record the URL provided for future access.

9. After successfully installing DCE 5.0 Enterprise, please contact us for
   authorization: email [info@daocloud.io](mailto:info@daocloud.io) or call 400 002 6898.
