# Upgrade DCE 5.0 Submodules

DCE 5.0 consists of more than ten sub-modules, such as container management, global management, observability, etc. Each sub-module can be independently upgraded.

This guide will introduce how to use `dce5-installer` package to upgrade any of these submodules offline.

## Prerequisites

- Deploy DCE 5.0, refer to [Offline Install Enterprise Package](commercial/start-install.md).
- Make sure that your bootstrapping node is running well.
- Decide which version you want to upgrade to, refer to [Release Notes](release-notes.md).

## Upgrade Steps

This section demonstrates how to upgrade a submodule from v0.5.0 to v0.6.0.

!!! note

    Only the submodules that have already been installed in the current environment will be upgraded. Those not installed will be skipped.

1. Download v0.6.0 Offline Package

    You can download the latest version from the [Download Center](https://docs.daocloud.io/download/dce5/).

    | CPU | Version | Download|
    | :--------------- | :------ | :----------- |
    | AMD64            | v0.6.0  | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-amd64.tar |
    | ARM64            | v0.6.0  | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-arm64.tar |

    After downloading, decompress the offline package. Take the offline package for AMD64 architecture as an example:

    ```bash
    tar -xvf offline-v0.6.0-amd64.tar
    ```

2. Modify `clusterConfig.yaml` to make it applicable in your environment.

    !!! note

        As v0.6.0 updated the structure of `clusterConfig.yaml` file, refer to [Cluster Configuration File Description](commercial/cluster-config.md), you must ensure that the parameters used are consistent with those in v0.5.0 and that the file structure is consistent with that of v0.6.0 during upgrading.
    
        Currently, only the `built-in` method of `imagesAndCharts` has been tested.

    The file is located in the `offline/sample` directory of the decompressed offline package. The sample configuration file is as follows:

    ??? note "Example of `clusterConfig.yaml`"
        
        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        metadata:
        spec:
          clusterName: my-cluster
          loadBalancer:
            type: metallb
            istioGatewayVip: 172.30.**.**/32
            insightVip: 172.30.**.**/32
          masterNodes:
            - nodeName: "g-master1"
              ip: 172.30.**.**
              ansibleUser: "root"
              ansiblePass: "*****"
          workerNodes:
            - nodeName: "g-worker1"
              ip: 172.30.**.**
              ansibleUser: "root"
              ansiblePass: "*****"
            - nodeName: "g-worker2"
              ip: 172.30.**.**
              ansibleUser: "root"
              ansiblePass: "*****"
        
          fullPackagePath: "/home/installer/offline"
          osRepos:
            type: builtin
            isoPath: "/home/installer/CentOS-7-x86_64-DVD-2207-02.iso"
            osPackagePath: "/home/installer/os-pkgs-centos7-v0.4.4.tar.gz"
          imagesAndCharts:
            type: builtin
        
          addonPackage:
          binaries:
            type: builtin # (1)
        ```

        1. official-service (default value), builtin or external

3. Configure `mainfest.yaml` (optional)

    The `mainfest.yaml` file locates in the `offline/sample` directory of the decompressed offline package.

    If some submodules do not need upgrade, you can set `enable` as `false`. For example, the following configuration means `Kpanda` (i.e., Container Management) will not be upgraded.

    ```yaml
      kpanda:
        enable: false
        helmVersion: 0.16.0
        variables:
    ```

4. Execute the upgrade command

    ```bash
    ./offline/dce5-installer cluster-create -c sample/clusterconfig.yaml -m sample/manifest.yaml --upgrade 4,5,gproduct
    ```

    Upgrade parameters:

    - `install-app` or `cluster-create`: means the mode used when you installed DCE 5.0. If the original submodules were installed with `cluster-create`, also use this command when upgrading
    - `--upgrade` can be abbreviated as `-u`.
    - After v0.7.0, you can only use `--upgrade gproduct`, instead of `--upgrade 4,5,gproduct`

    When you succeeded, you will see:

    ![upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/upgrade.png)
