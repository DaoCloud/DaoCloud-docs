# Deploy DCE 5.0 Enterprise on UOS V20 (1020a)

This page introduces how to deploy DCE 5.0 on UOS V20(1020a).
Installer v0.6.0 and higher versions support this deployment method.

## Prerequisites

- Read [Deployment Architecture](../commercial/deploy-arch.md) in advance to confirm this deployment mode.
- Read [Deployment Requirements](../commercial/deploy-requirements.md) in advance to confirm whether the
  network, hardware, ports, etc. meet the requirements.
- Read [Preparation](../commercial/prepare.md) in advance to confirm machine resources and pre-check.

## Offline installation

1. Since the installer depends on python, you need to install `python3.6` on the tinder machine first.

    ```bash
    # download dependencies
    dnf install -y --downloadonly --downloaddir=rpm/python36

    # start the installation
    rpm -ivh python3-pip-9.0.3-18.uelc20.01.noarch.rpm python3-setuptools-39.2.0-7.uelc20.2.noarch.rpm python36-3.6.8-2.module+uelc20+36 +6174170c.x86_64.rpm
    ```

2. Download the full mode offline package, you can download the latest version in [Download Center](../../download/index.md).

    | CPU Architecture | Version | Download URL |
    | -------- | ------ | --------------------- |
    | AMD64 | v0.16.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.0-amd64.tar> |

    Unzip the offline package after downloading:

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.0-amd64.tar
    tar -xvf offline-v0.16.0-amd64.tar
    ```

3. Download the UnionTech Server V20 1020a ISO image.

    ```bash
    curl -LO https://cdimage-download.chinauos.com/uniontechos-server-20-1020a-amd64.iso
    ```

4. Make the **os-pkgs-uos-20.tar.gz** file.

    Download the production script

    ```bash
    curl -Lo ./build.sh https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/uos_v20/build.sh
    chmod +x build.sh
    ```

    Run the script to generate **os-pkgs-uos-20.tar.gz** file:

    ```bash
    ./build.sh
    ```

5. Download the addon offline package, you can download the latest version in [Download Center](../../download/index.md) (optional)

6. Edit [clusterConfig.yaml](../commercial/cluster-config.md), which can be obtained under the offline package
   `offline/sample` and modified as needed. The sample configuration is for your reference:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: my-cluster
      masterNodes:
        - nodeName: "g-master1"
          ip: 10.5.14.XX
          ansibleUser: "root"
          ansiblePass: "XXXX"
      fullPackagePath: "/home/offline"
      osRepos:
        type: builtin
        isoPath: "/home/uniontechos-server-20-1020a-amd64.iso" ## directory of ISO
        osPackagePath: "/home/os-pkgs-uos-20.tar.gz" ## directory of os-pkgs
      imagesAndCharts:
        type: builtin
      addonPackage:
        path: "/home/addon-offline-full-package-v0.5.3-alpha2-amd64.tar.gz" ## directory of addon
      binaries:
        type: builtin
    ```

7. Start the installation of DCE 5.0.

    ```bash
    ./dce5-installer cluster-create -m ./sample/manifest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        Some parameters are introduced, and more parameters can be viewed through `./dce5-installer --help`:

        - `-z` minimal install
        - `-c` specifies the cluster configuration file, and does not need to specify `-c` when using NodePort to expose the console
        - `-d` enable debug mode
        - `--serial` specifies that all installation tasks are executed serially

8. After the installation is complete, the command line will prompt that the installation is successful.
   Congratulations! :smile: Now you can use the default account and password (admin/changeme) to explore
   the new DCE 5.0 through the URL prompted on the screen!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please record the prompted URL for your next visit.

9. After successfully installing DCE 5.0 Enterprise, please contact us for authorization: email [info@daocloud.io](mailto:info@daocloud.io) or call 400 002 6898.
