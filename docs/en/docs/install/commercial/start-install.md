# Install DCE 5.0 commercial offline

Please make sure you read and understand [Deployment Requirements](deploy-requirements.md), [Deployment Architecture](deploy-arch.md), [Preparation](prepare.md) before installation

Please see the [Release Notes](../release-notes.md) to avoid known issues with your installed version and to see what's new

## Offline installation steps

### Step 1: Download offline package

Please download the corresponding offline package according to the business environment.

#### Offline image package (required)

You can download the latest version at [Download Center](https://docs.daocloud.io/download/dce5/).

| CPU Architecture | Version | Download URL |
| :------- | :----- | :-------------------------------- ------------------------------ |
| AMD64 | v0.10.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-amd64.tar> |
| ARM64 | v0.10.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-arm64.tar> |

Unzip the offline package after downloading:

```bash
# Take the amd64 architecture offline package as an example
tar -xvf offline-v0.10.0-amd64.tar
```

#### addon offline package (optional)

From version v0.5.0, the installer supports the addon's offline package import capability, and if necessary, supports the offlineization of all helm charts in the addon. You can download the latest version at [Download Center](https://docs.daocloud.io/download/dce5/).

First, you need to download the offline package in advance, and define `addonOfflinePackagePath` in [cluster configuration file (clusterConfig.yaml)](./cluster-config.md).

| CPU Architecture | Version | Download URL |
| :------- | :----- | :-------------------------------- ------------------------------ |
| AMD64 | v0.10.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_DigitalX_Addon/addon-offline-full-package-v0.10.0-amd64.tar.gz> |
| ARM64 | v0.10.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_DigitalX_Addon/addon-offline-full-package-v0.10.0-arm64.tar.gz> |

#### ISO offline package (required)

The ISO offline package needs to be configured in [cluster configuration file](./cluster-config.md), please download according to the operating system.

| CPU Architecture | Operating System Version                              | Download Link                                                 |
| :--------------- | :--------------------------------------------------- | :----------------------------------------------------------- |
| AMD64            | CentOS 7                                             | [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso) |
|                  | Red Hat 7, 8                                         | [Red Hat Downloads](https://developers.redhat.com/products/rhel/download#assembly-field-downloads-page-content-61451) <br />Note: Red Hat operating system requires a Red Hat account to download |
|                  | Ubuntu 20.04                                        | [ubuntu-20.04.6-live-server-amd64.iso](https://releases.ubuntu.com/focal/ubuntu-20.04.6-live-server-amd64.iso) |
|                  | UnionTech UOS V20 (1020a)                            | [uniontechos-server-20-1020a-amd64.iso](https://cdimage-download.chinauos.com/uniontechos-server-20-1020a-amd64.iso) |
|                  | openEuler 22.03                                      | [openEuler-22.03-LTS-SP1-x86_64-dvd.iso](https://mirrors.nju.edu.cn/openeuler/openEuler-22.03-LTS-SP1/ISO/x86_64/openEuler-22.03-LTS-SP1-x86_64-dvd.iso) |
|                  | Oracle Linux R9 U1                                   | [OracleLinux-R9-U1-x86_64-dvd.iso](https://yum.oracle.com/ISOS/OracleLinux/OL9/u1/x86_64/OracleLinux-R9-U1-x86_64-dvd.iso) |
| ARM64            | Kylin Linux Advanced Server release V10 (Sword) SP2  | Application Link: [Kylin OS](https://www.kylinos.cn/scheme/server/1.html) <br />Note: Kylin OS requires personal information to be provided for downloading and usage. Choose V10 (Sword) SP2 during download. |

#### osPackage offline package (required)

The installer from version v0.5.0 needs to provide the osPackage offline package of the operating system, and define `osPackagePath` in [clusterConfig.yaml](./cluster-config.md).

Among them, [Kubean](https://github.com/kubean-io/kubean) provides osPackage offline packages for different operating systems. You can visit <https://github.com/kubean-io/kubean/releases> to view them.

| OS version | Download url |
| :-------------------------------------------------- | :----------------------------------------------------------- |
| Centos 7                                            | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-centos7-v0.7.4.tar.gz> |
| Redhat 8                                            | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-redhat8-v0.7.4.tar.gz> |
| Redhat 7                                            | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-redhat7-v0.7.4.tar.gz> |
| Kylin Linux Advanced Server release V10 (Sword) SP2 | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-kylinv10-v0.7.4.tar.gz> |
| Ubuntu20.04                                         | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-ubuntu2004-v0.7.4.tar.gz> |
| openEuler 22.03                                     | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-openeuler22.03-v0.7.4.tar.gz> |
| OracleLinux R9 U1                                   | https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-oracle9-v0.7.4.tar.gz |

For UOS V20 (1020a) osPackage deployment, please refer to [Deploying DCE 5.0 on UOS V20 (1020a) operating system](../os-install/uos-v20-install-dce5.0.md)

### Step 2: Configure the cluster configuration file

The cluster configuration file is located in the `offline/sample` directory of the offline image package. For specific parameter introduction, please refer to [clusterConfig.yaml](cluster-config.md).

!!! note

    Currently, the standard 7-node mode template is provided in the offline image package.

### Step 3: Start the installation

1. run the following command to start installing DCE 5.0, the location of the installer binary file is `offline/dce5-installer`

    ```shell
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml
    ```

    !!! note

        Installer script command description:
       
        - -c to specify the cluster configuration file, required
        - The -m parameter specifies the manifest file,
        - -z minimal install
        - -dEnable debug mode
        - For more commands, please use --help query

1. After the installation is complete, the command line will prompt that the installation is successful. congratulations! Now you can use the default account and password (admin/changeme) to explore the new DCE 5.0 through the URL prompted on the screen!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please record the prompted URL for your next visit.

1. After successfully installing DCE 5.0 commercial version, please contact us for authorization: email info@daocloud.io or call 400 002 6898.
