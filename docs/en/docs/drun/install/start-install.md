# Offline Install d.run AI OS

This page describes how to install **d.run AI OS (hereinafter referred to as d.run)** offline. Use the manifest file `manifest-cloud.yaml` during installation.

Before installation, read and understand the [deployment requirements](./commercial/deploy-requirements.md), [deployment architecture](./commercial/deploy-arch.md), and [preparation](./commercial/prepare.md), and first complete [installing the dependencies](index.md).

## Step 1: Download Offline Packages

Download the appropriate version of the offline package in accordance with your business environment.
The complete d.run offline package is available at [Download Center - d.run AI OS](../../download/drun/index.md).

### Offline Image Package (Required)

The offline image package contains the configuration files, image resources, and chart packages required for installing d.run.
You can download the latest version from the [Download Center - d.run AI OS](../../download/drun/index.md).

| CPU Architecture | Version | Download |
| :------- | :----- | :-----|
| AMD64 | v0.44.0 | [offline-v0.44.0-amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.44.0-amd64.tar) |
| <font color="green">ARM64</font> | v0.44.0 | [offline-v0.44.0-arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.44.0-arm64.tar) |

After downloading, extract the offline package.
Take the amd64 architecture offline package as an example:

```bash
tar -xvf offline-v0.44.0-amd64.tar
```

### ISO Operating System Image Files (Required)

The ISO format operating system image file should be downloaded based on the different operating systems during the installation process.

The ISO operating system image file needs to be configured in
[clusterConfig.yaml](./commercial/cluster-config.md).

| CPU Architecture | Operating System Version | Download |
| :------- | :--------- | :------- |
| AMD64    | CentOS 7 | [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso) |
| | Redhat 7, 8, 9 | [assembly-field-downloads-page-content-61451](https://developers.redhat.com/products/rhel/download#assembly-field-downloads-page-content-61451) <br />Note: Downloading the Red Hat requires a proper account. |
| | Ubuntu 20.04.6 LTS | [ubuntu-20.04.6-live-server-amd64.iso](https://releases.ubuntu.com/focal/ubuntu-20.04.6-live-server-amd64.iso) |
| | Ubuntu 22.04.5 LTS | [ubuntu-22.04.5-live-server-amd64.iso](https://releases.ubuntu.com/jammy/ubuntu-22.04.5-live-server-amd64.iso) |
| | UOS V20 (1020a) | [uniontechos-server-20-1020a-amd64.iso](https://cdimage-download.chinauos.com/uniontechos-server-20-1020a-amd64.iso) |
| | openEuler 22.03 | [openEuler-22.03-LTS-SP1-x86_64-dvd.iso](https://mirrors.nju.edu.cn/openeuler/openEuler-22.03-LTS-SP1/ISO/x86_64/openEuler-22.03-LTS-SP1-x86_64-dvd.iso) |
| | Oracle Linux R9 U1 | [OracleLinux-R9-U1-x86_64-dvd.iso](https://yum.oracle.com/ISOS/OracleLinux/OL9/u1/x86_64/OracleLinux-R9-U1-x86_64-dvd.iso) |
| | Oracle Linux R8 U7 | [OracleLinux-R8-U7-x86_64-dvd.iso](https://yum.oracle.com/ISOS/OracleLinux/OL8/u7/x86_64/OracleLinux-R8-U7-x86_64-dvd.iso) |
| | Rocky Linux 9.2 | [Rocky-9.2-x86_64-dvd.iso](https://dl.rockylinux.org/vault/rocky/9.2/isos/x86_64/Rocky-9.2-x86_64-dvd.iso) |
| | Rocky Linux 8.10 | [Rocky-8.10-x86_64-dvd1.iso](https://download.rockylinux.org/pub/rocky/8/isos/x86_64/Rocky-8.10-x86_64-dvd1.iso) |
| <font color="green">ARM64</font> | Kylin Linux Advanced Server release V10 (Sword) SP2 | [Request URL](https://www.kylinos.cn/support/trial.html) |
| | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [Request URL](https://www.kylinos.cn/support/trial.html) |

!!! note

    - It is recommended to install all operating systems in Server mode.
    - The Kirin operating system requires personal information to be provided for download.
      When downloading, please select V10 (Sword) SP2.

### osPackage Offline Packages (Required)

The osPackage offline package is a supplement to the Linux operating system offline software source
provided by the open-source project [Kubean](https://github.com/kubean-io/kubean). For example,
openEuler 22.03 lacks the `selinux-policy-35.5-15.oe2203.noarch.rpm`.

The installer needs to provide the osPackage offline package for the operating system and define
`osPackagePath` in [clusterConfig.yaml](./commercial/cluster-config.md).

[Kubean](https://github.com/kubean-io/kubean) provides osPackage offline packages for different
operating systems. You can visit <https://github.com/kubean-io/kubean/releases> to check them out.

Currently, the osPackage offline package version must match the installer version.
Download the osPackage offline package according to the corresponding version:

=== "V0.44.0"

    | Operating System | Download |
    | :--------- | :------ |
    | Redhat 8     | [os-pkgs-redhat8-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-redhat8-v0.37.0.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-redhat7-v0.37.0.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-redhat9-v0.37.0.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-ubuntu2004-v0.37.0.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-ubuntu2204-v0.37.0.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-openeuler22.03-v0.37.0.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-oracle9-v0.37.0.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-oracle8-v0.37.0.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.37.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-rocky9-v0.37.0.tar.gz) |
    | Rocky Linux 8.10 | [os-pkgs-rocky8-v0.37.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-rocky8-v0.37.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-kylin-v10sp2-v0.37.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.37.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.37.0/os-pkgs-kylin-v10sp3-v0.37.0.tar.gz) |

=== "V0.43.0"

    | Operating System | Download |
    | :--------- | :------ |
    | Redhat 8     | [os-pkgs-redhat8-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-redhat8-v0.36.0.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-redhat7-v0.36.0.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-redhat9-v0.36.0.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-ubuntu2004-v0.36.0.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-ubuntu2204-v0.36.0.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-openeuler22.03-v0.36.0.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-oracle9-v0.36.0.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-oracle8-v0.36.0.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.36.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-rocky9-v0.36.0.tar.gz) |
    | Rocky Linux 8.10 | [os-pkgs-rocky8-v0.36.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-rocky8-v0.36.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-kylin-v10sp2-v0.36.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.36.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.36.0/os-pkgs-kylin-v10sp3-v0.36.0.tar.gz) |

=== "V0.42.0"

    | Operating System | Download |
    | :--------- | :------ |
    | Redhat 8     | [os-pkgs-redhat8-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-redhat8-v0.35.1.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-redhat7-v0.35.1.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-redhat9-v0.35.1.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-ubuntu2004-v0.35.1.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-ubuntu2204-v0.35.1.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-openeuler22.03-v0.35.1.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-oracle9-v0.35.1.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-oracle8-v0.35.1.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.35.1.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-rocky9-v0.35.1.tar.gz) |
    | Rocky Linux 8.10 | [os-pkgs-rocky8-v0.35.1.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-rocky8-v0.35.1.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-kylin-v10sp2-v0.35.1.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.35.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.35.1/os-pkgs-kylin-v10sp3-v0.35.1.tar.gz) |

### Addon Offline Packages (Optional)

Addon offline packages contain Helm Chart offline packages for commonly used components.
For the specific list, refer to the [addon](../../download/addon/history.md) documentation.

The installer supports importing addon offline packages.
If you want to offline all the Helm charts in the addon package, you can download the latest version
from the [Download Center](../../download/index.md) in advance.

First, make sure to download the offline package in advance and define `addonOfflinePackagePath`
in [clusterConfig.yaml](./commercial/cluster-config.md).

### One-Click Download Required Offline Packages

We provide a script for [one-click downloading the required offline packages](air-tag-download.md).

The following packages are included:

- Prerequisite Dependency Tool Offline Package
- osPackage Offline Package
- Installer Offline Package

!!! note

    Due to different methods of downloading ISO operating systems, the one-click download
    does not include the ISO files.

## Step 2: Edit clusterConfig.yaml

This is the cluster configuration file, located in the `offline/sample` directory of the offline image package.
For detailed parameter introduction, refer to [clusterConfig.yaml](./commercial/cluster-config.md).

!!! note

    Currently, the offline image package provides a standard 7-node mode template.
    When deploying with Redhat 9.2 operating system, you need to enable the kernel
    tuning parameter `node_sysctl_tuning: true`.

## Step 3: Install

1. Run the following command to start installing d.run. The installer binary file is located at `offline/dce5-installer`. For the manifest, use `offline/sample/manifest-cloud.yaml` in the offline package.

    ```shell
    ./offline/dce5-installer cluster-create \
      -c ./offline/sample/clusterConfig.yaml \
      -m ./offline/sample/manifest-cloud.yaml
    ```

    !!! note

        Explanation of installer script command:

        - Use `-c` to specify clusterConfig.yaml (required).
        - Use `-m` to specify the manifest file. For d.run, use `manifest-cloud.yaml`.
        - Use `-z` for minimal installation.
        - Use `-d` to enable debug mode.
        - Use `--use-original-repo` to download binaries and pull images
        - For more options, use `--help` to query.

    The following is an example of `manifest-cloud.yaml` (fields and versions are subject to the extracted offline package; this is only to illustrate the structure):

    ```yaml title="manifest-cloud.yaml"
    apiVersion: manifest.daocloud.io/v1alpha3
    kind: DCEManifest
    metadata:
      creationTimestamp: null
    global:
      helmRepo: https://release.daocloud.io/chartrepo
      imageRepo: release.daocloud.io
      installMode: cloud
    infrastructures:
      # ... See the offline package for details
    middlewares:
      # ... See the offline package for details
    components:
      hydra:
        enable: true
        helmVersion: v0.18.3
        dependencies:
          - ghippo
          - kpanda
          - mspider
          - insight
          - leopard
      # Other components such as ghippo, kpanda, insight, crane, zestu, leopard, and baize are omitted. See the offline package for details
    ```

    The core fields of the d.run manifest are described as follows:

    - `global.installMode` is set to `cloud`.
    - LLM Studio (`hydra`) is enabled by default; Cockpit (`crane`) is disabled by default.
    - Comparison with [Token Factory](../../tf/install/index.md): `global.tokenfactory.enable` is not enabled, and Cockpit is not enabled by default.

2. After the installation is complete, the command line will prompt a successful installation. You can access the console using the URL provided on the screen with the default account and password (admin/changeme).

    !!! success

        Please record the provided URL for future access.

3. After successfully installing d.run, contact us for authorization: email info@daocloud.io or call 400 002 6898.
