# Deploying DCE 5.0 Enterprise on NeoKylin Linux Advanced Server V7Update6

This article will introduce how to deploy DCE 5.0 on the NeoKylin Linux Advanced Server V7Update6 operating system.

## Prerequisites

- Read the [deployment architecture](../commercial/deploy-arch.md) in advance to confirm the deployment mode.
- Read the [deployment requirements](../commercial/deploy-requirements.md) in advance to confirm if the network, hardware, ports, etc., meet the requirements.
- Read the [preparation work](../commercial/prepare.md) in advance to confirm the machine resources and pre-checks.
- Make sure to install `iptables` and `iproute` on the node in advance.

    ```bash
    # Install iptables
    wget https://rpmfind.net/linux/centos/7.9.2009/os/x86_64/Packages/iptables-1.4.21-35.el7.x86_64.rpm
    rpm -ivh iptables-1.4.21-35.el7.x86_64.rpm
    iptables --version
    
    # Install iproute
    wget https://rpmfind.net/linux/centos/7.9.2009/os/x86_64/Packages/iproute-4.11.0-30.el7.x86_64.rpm
    rpm -ivh iproute-4.11.0-30.el7.x86_64.rpm
    ```

## Offline Installation

1. Download the full mode offline package, you can download the latest version from the [download center](../../download/index.md).

    | CPU Architecture | Version | Download Link |
    | ---------------- | ------- | ------------- |
    | AMD64            | v0.17.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar> |

    Once downloaded, extract the offline package:

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar
    tar -xvf offline-v0.17.0-amd64.tar
    ```

2. Download the NeoKylin Linux Advanced Server V7Update6 image file.

    ```bash
    # Oracle Linux R9 U1
    curl -LO https://yum.oracle.com/ISOS/OracleLinux/OL9/u1/x86_64/OracleLinux-R9-U1-x86_64-dvd.iso
    ```

3. Create the NeoKylin Linux Advanced Server V7Update6 OS Package offline package.

    **Prerequisites:**

    - Check if `libselinux-python` exists. If not, refer to the dependency installation method below.

        ```bash
        rpm -q libselinux-python
        ```

    - Install dependencies `device-mapper-libs`, `conntrack`, `sshpass`,
      Check the [download link for dependencies](https://rpmfind.net/linux/rpm2html/search.php?query=sshpass&submit=Search+). Installation command is as follows:

        ```bash
        rpm -ivh <package name>
        ```

    - Manually modify the `VERSION_ID="7"` in the os-release file.

        ```bash
        vi /etc/os-release
        ```

    **Refer to [Creating OS Package Offline Package](../os-install/otherlinux.md#os-package) to start creating the offline package.**

4. Download the addon offline package, you can download the latest version from the [download center](../../download/index.md) (optional).

5. Set up the [cluster configuration file clusterConfig.yaml](../commercial/cluster-config.md), you can obtain this file under the offline package `offline/sample` and modify it as needed.
    The reference configuration is:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
      creationTimestamp: null
    spec:
      clusterName: my-cluster
      masterNodes:
        - nodeName: "master1"
          ip: 10.6.135.199
          ansibleUser: "root"
          ansiblePass: "dangerous@2024"
      workerNodes: []
      osRepos:
        type: none # (1)!
      imagesAndCharts:
        type: builtin
      binaries:
        type: builtin
      loadBalancer:
        type: NodePort
      fullPackagePath: /home/offline
    ```

    1. Change to `none`.

6. Start installing DCE 5.0.

    ```bash
    ./dce5-installer cluster-create -m ./sample/manifest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        You can check more parameters by using `./dce5-installer --help`:
        
        - `-z` Minimal installation
        - `-c` Specify the cluster configuration file, not required when exposing the console using NodePort
        - `-d` Enable debug mode
        - `--serial` Specify all installation tasks to be executed serially

7. After the installation is completed, the command line will indicate a successful installation. Congratulations! :smile: You can now explore the brand new DCE 5.0 using the URL provided in the prompt with the default account and password (admin/changeme)!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please make a note of the provided URL for future access.

    ![control-UI](../images/ui-neoky.png)

8. After successfully installing DCE 5.0 Enterprise, please contact us for authorization: Email [info@daocloud.io](mailto:info@daocloud.io) or call 400 002 6898.
