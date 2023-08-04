# Deploying DCE 5.0 Enterprise Package on Oracle Linux R9 U1 Operating System

This page will introduce how to deploy DCE 5.0 on Oracle Linux R9 U1 operating system, which supports v0.8.0 and above.

## Prerequisites

- Please read [Deployment Architecture](../commercial/deploy-arch.md) in advance to confirm the deployment mode.
- Please read [Deployment Requirements](../commercial/deploy-requirements.md) in advance to confirm whether the network, hardware, ports, etc. meet the requirements.
- Please read [Preparation Work](../commercial/prepare.md) in advance to confirm machine resources and pre-checks.

## Offline Installation

1. Download the full-mode offline package, which can be downloaded from the [download center](https://docs.daocloud.io/download/dce5/) for the latest version.

    | CPU Architecture | Version | Download Link |
    | ---------------- | ------- | ------------- |
    | AMD64            | v0.8.0  | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-amd64.tar> |

    After downloading, unzip the offline package:

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-amd64.tar
    tar -xvf offline-v0.8.0-amd64.tar
    ```

2. Download the Oracle Linux R9 U1 image file.

    ```bash
    curl -LO https://yum.oracle.com/ISOS/OracleLinux/OL9/u1/x86_64/OracleLinux-R9-U1-x86_64-dvd.iso
    ```

3. Download the Oracle Linux R9 U1 osPackage offline package.

    ```bash
    curl -LO https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.5.4/os-pkgs-oracle9-v0.5.4.tar.gz
    ```

4. Download the addon offline package, which can be downloaded from the [download center](../../download/index.md) for the latest version (optional).

5. Set up the [clusterConfig.yaml](../commercial/cluster-config.md), which can be obtained under the offline package `offline/sample` and modified as needed.
    
    The reference configuration is:

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
        # Turn on the recommended sysctl configuration to avoid the `too many open files` problem
        node_sysctl_tuning: true
        # Disable kubespray from installing public repo for oracle linux
        use_oracle_public_repo: false
    ```

    !!! note

        Because the `kpanda-controller-manager` component reports an error `failed to create fsnotify watcher: too many open files.` 、
        during the installation process, you need to set `node_sysctl_tuning: true` in the `clusterConfig.yaml` file.

7. Start installing DCE 5.0.

    ```bash
    ./dce5-installer cluster-create -m ./sample/mainfest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        For detailed parameters, you can check with `./dce5-installer --help`:

        - `-z` Minimal installation
        - `-c` Specify the cluster configuration file. When using NodePort to expose the console, you do not need to specify `-c`
        - `-d` Enable debug mode
        - `--serial` Specifies that all installation tasks are executed serially after the specified task

8. After the installation is complete, the command line will prompt that the installation was successful. Congratulations! :smile: Now you can explore the new DCE 5.0 with the default account and password (admin/changeme) using the URL displayed on the screen!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please keep a record of the URL provided for easy access next time.

9. After successfully installing DCE 5.0 Enterprise Package, please contact us for authorization: email [info@daocloud.io](mailto:info@daocloud.io) or call 400 002 6898.