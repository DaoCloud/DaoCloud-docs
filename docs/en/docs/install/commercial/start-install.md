---
MTPE: ModetaNiu
date: 2024-06-28
---

# Offline Install DCE 5.0 Enterprise

Ensure that you have read and understood the [deployment requirements](deploy-requirements.md),
[deployment architecture](deploy-arch.md), and [preparation](prepare.md) before installation.

Refer to the [release notes](../release-notes.md) to avoid known issues with the
installed version and to check for new features.

## Download Offline Package

Download the appropriate version of the offline package in accordance with your business environment.

### Offline Image Package (Required)

The offline image package contains configuration files, image resources, and
chart packages required for installing DCE 5.0 modules.

You can download the latest version from the [Download Center](../../download/index.md).

| CPU Architecture | Version | Download |
| :--------------- | :------ | :------- |
| AMD64 | v0.19.0 | [offline-v0.19.0-amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.19.0-amd64.tar) |
| ARM64 | v0.19.0 | [offline-v0.19.0-arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.19.0-arm64.tar) |

After downloading, extract the offline package.
Take the amd64 architecture offline package as an example

```bash
tar -xvf offline-v0.19.0-amd64.tar
```

### ISO Operating System Image Files (Required)

The ISO format operating system image file should be downloaded based on the
different operating systems during the installation process.

The ISO operating system image file needs to be configured in
[clusterConfig.yaml](./cluster-config.md), so download for your operating system.

| CPU Architecture | Operating System Version | Download |
| :--------------- | :---------------------- | :-------- |
| AMD64 | CentOS 7 | [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso ) |
|   | Redhat 7, 8, 9 | [assembly-field-downloads-page-content-61451](https://developers.redhat.com/products/rhel/download#assembly-field-downloads-page-content-61451) <br />Note: Redhat operating system requires a Redhat account to download |
|   | Ubuntu 20.04 | [ubuntu-20.04.6-live-server-amd64.iso](https://releases.ubuntu.com/focal/ubuntu-20.04.6-live-server-amd64.iso) |
| | ubuntu-22.04.4 | [ubuntu-22.04.4-live-server-amd64.iso](https://releases.ubuntu.com/jammy/ubuntu-22.04.4-live-server-amd64.iso) |
|   | UOS V20 (1020a) | [uniontechos-server-20-1020a-amd64.iso](https://cdimage-download.chinauos.com/uniontechos-server-20-1020a-amd64.iso) |
|   | openEuler 22.03 | [openEuler-22.03-LTS-SP1-x86_64-dvd.iso](https://mirrors.nju.edu.cn/openeuler/openEuler-22.03-LTS-SP1/ISO/x86_64/openEuler-22.03-LTS-SP1-x86_64-dvd.iso) |
|   | OracleLinux R9 U1 | [OracleLinux-R9-U1-x86_64-dvd.iso](https://yum.oracle.com/ISOS/OracleLinux/OL9/u1/x86_64/OracleLinux-R9-U1-x86_64-dvd.iso) |
| | Oracle Linux R8 U7 | [OracleLinux-R8-U7-x86_64-dvd.iso](https://yum.oracle.com/ISOS/OracleLinux/OL8/u7/x86_64/OracleLinux-R8-U7-x86_64-dvd.iso) |
|   | Rocky Linux 9.2 | [Rocky-9.2-x86_64-dvd.iso](https://dl.rockylinux.org/vault/rocky/9.2/isos/x86_64/Rocky-9.2-x86_64-dvd.iso) |
| <font color="green">ARM64</font> | Kylin Linux Advanced Server release V10 (Sword) SP2 | [Request Address](https://www.kylinos.cn/support/trial.html) |

!!! note

    Kylin operating system requires providing personal information to download and use.
    Select V10 (Sword) SP2 when downloading.

### osPackage Offline Packages (Required)

The osPackage offline package is a supplement to the Linux operating system offline software source
provided by the open-source project [Kubean](https://github.com/kubean-io/kubean). For example,
openEuler 22.03 lacks the `selinux-policy-35.5-15.oe2203.noarch.rpm`.

Starting from v0.5.0, the installer requires the osPackage offline package for the
operating system and defines `osPackagePath` in [clusterConfig.yaml](./cluster-config.md).

[Kubean](https://github.com/kubean-io/kubean) provides osPackage offline packages for different
operating systems, which can be found at <https://github.com/kubean-io/kubean/releases>.

Currently, the installer version requires the osPackage offline package version to match.
Download the osPackage offline package based on the corresponding version:

=== "V0.19.0"

    | Operating System | Download |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-centos7-v0.16.3.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-redhat8-v0.16.3.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-redhat7-v0.16.3.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-redhat9-v0.16.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-kylinv10-v0.16.3.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-ubuntu2004-v0.16.3.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-openeuler22.03-v0.16.3.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-oracle9-v0.16.3.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-oracle8-v0.16.3.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.16.3.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-rocky9-v0.16.3.tar.gz) |

=== "V0.18.0"

    | Operating System | Download |
    | :--------------- | :--------- |
    | CentOS 7 | [os-pkgs-centos7-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-centos7-v0.15.3.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-redhat8-v0.15.3.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-redhat7-v0.15.3.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-redhat9-v0.15.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-kylinv10-v0.15.3.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-ubuntu2004-v0.15.3.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-openeuler22.03-v0.15.3.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-oracle9-v0.15.3.tar.gz) |
     | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-oracle8-v0.15.3.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.15.3.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-rocky9-v0.15.3.tar.gz) |

=== "V0.17.0"

    | Operating System | Download |
    | :--------------- | :--------- |
    | CentOS 7 | [os-pkgs-centos7-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-centos7-v0.13.11.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-redhat8-v0.13.11.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-redhat7-v0.13.11.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-redhat9-v0.13.11.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-kylinv10-v0.13.11.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-ubuntu2004-v0.13.11.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-openeuler22.03-v0.13.11.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-oracle9-v0.13.11.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.13.11.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-rocky9-v0.13.11.tar.gz) |

=== "V0.16.1"

    | Operating System | Download |
    | :--------------- | :--------- |
    | CentOS 7 | [os-pkgs-centos7-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-centos7-v0.13.9.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-redhat8-v0.13.9.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-redhat7-v0.13.9.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-redhat9-v0.13.9.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-kylinv10-v0.13.9.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-ubuntu2004-v0.13.9.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-openeuler22.03-v0.13.9.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-oracle9-v0.13.9.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.13.9.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-rocky9-v0.13.9.tar.gz) |

=== "V0.15.0"

    | Operating System | Download |
    | :--------------- | :--------- |
    | CentOS 7 | [os-pkgs-centos7-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-centos7-v0.12.2.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-redhat8-v0.12.2.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-redhat7-v0.12.2.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-redhat9-v0.12.2.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-kylinv10-v0.12.2.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-ubuntu2004-v0.12.2.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-openeuler22.03-v0.12.2.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-oracle9-v0.12.2.tar.gz) |

=== "V0.14.0"

    | Operating System | Download |
    | :--------------- | :--------- |
    | CentOS 7 | [os-pkgs-centos7-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-centos7-v0.11.2.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-redhat8-v0.11.2.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-redhat7-v0.11.2.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-redhat9-v0.11.2.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-kylinv10-v0.11.2.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-ubuntu2004-v0.11.2.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-openeuler22.03-v0.11.2.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-oracle9-v0.11.2.tar.gz) |

=== "V0.13.0"

    | Operating System | Download |
    | :--------------- | :--------- |
    | CentOS 7 | [os-pkgs-centos7-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-centos7-v0.10.0.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-redhat8-v0.10.0.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-redhat7-v0.10.0.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-redhat9-v0.10.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-kylinv10-v0.10.0.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-ubuntu2004-v0.10.0.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-openeuler22.03-v0.10.0.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-oracle9-v0.10.0.tar.gz) |

=== "V0.12.0"

    | Operating System | Download |
    | :-------------- | :--------- |
    | CentOS 7 | [os-pkgs-centos7-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-centos7-v0.9.3.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat8-v0.9.3.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat7-v0.9.3.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat9-v0.9.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-kylinv10-v0.9.3.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-ubuntu2004-v0.9.3.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-openeuler22.03-v0.9.3.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-oracle9-v0.9.3.tar.gz) |

=== "V0.11.0"

    | Operating System | Download |
    | :--------------- | :-------- |
    | CentOS 7 | [os-pkgs-centos7-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-centos7-v0.8.6.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-redhat8-v0.8.6.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-redhat7-v0.8.6.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-redhat9-v0.8.6.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-kylinv10-v0.8.6.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-ubuntu2004-v0.8.6.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-openeuler22.03-v0.8.6.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-oracle9-v0.8.6.tar.gz) |

=== "V0.10.0"

    | Operating System | Download |
    | :--------------- | :-------- |
    | CentOS 7 | [os-pkgs-centos7-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-centos7-v0.7.4.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-redhat8-v0.7.4.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-redhat7-v0.7.4.tar.gz) |
    | Redhat 9 | [os-pkgs-redhat9-v0.8.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.3/os-pkgs-redhat9-v0.8.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-kylinv10-v0.7.4.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-ubuntu2004-v0.7.4.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-openeuler22.03-v0.7.4.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-oracle9-v0.7.4.tar.gz) |

=== "V0.9.0"

    | Operating System | Download |
    | :--------------- | :-------- |
    | CentOS 7 | [os-pkgs-centos7-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-centos7-v0.6.6.tar.gz) |
    | Redhat 8 | [os-pkgs-redhat8-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-redhat8-v0.6.6.tar.gz) |
    | Redhat 7 | [os-pkgs-redhat7-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-redhat7-v0.6.6.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-kylinv10-v0.6.6.tar.gz) |
    | Ubuntu 20.04 | [os-pkgs-ubuntu2004-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-ubuntu2004-v0.6.6.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-openeuler22.03-v0.6.6.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-oracle9-v0.6.6.tar.gz) |

For deploying DCE 5.0 on UOS V20 (1020a) operating system, refer to
[Deploying DCE 5.0 on UOS V20 (1020a)](../os-install/uos-v20-install-dce5.0.md).

### Addon Offline Packages (Optional)

Addon offline packages contain Helm Chart offline packages for commonly used components.
For the specific list, refer to the [addon](../../download/addon/history.md) documentation.

Starting from installer v0.5.0, support for importing addon offline packages is available.
If you want to offline all the Helm charts in the addon package, you can download the latest version
from the [Download Center](../../download/index.md).

First, make sure to download the offline package in advance and define `addonOfflinePackagePath`
in [clusterConfig.yaml](./cluster-config.md).

### One-Click Download Required Offline Packages

We provide a script for [one-click downloading and installing the offline packages required for DCE 5.0](../air-tag-download.md).

The following packages are included:

- Prerequisite Dependency Tool Offline Package
- osPackage Offline Package
- Installer Offline Package

!!! note

    Due to different methods of downloading ISO operating systems, the one-click download
    does not include the ISO files.

## Edit clusterConfig.yaml

`clusterConfig.yaml` is located in the `offline/sample` directory of the offline image package.
For detailed parameter introduction, refer to [clusterConfig.yaml](cluster-config.md).

!!! note

    Currently, the offline image package provides a standard 7-node mode template.
    When deploying with Redhat 9.2 operating system, you need to enable the kernel
    tuning parameter `node_sysctl_tuning: true`.

## Install

1. Run the following command to start installing DCE 5.0. The installer binary file is
   located at `offline/dce5-installer`.

    ```shell
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml
    ```

    !!! note

        Explanation of installer script command:
        
        - Use `-c` to specify clusterConfig.yaml (required).
        - Use `-m` to specify the manifest file.
        - Use `-z` for minimal installation.
        - Use `-d` to enable debug mode.
        - For more options, use `--help` to query.

1. After the installation is complete, the command line will prompt a successful installation.
   Congratulations! Now you can explore the brand new DCE 5.0 using the URL provided with the
   default account and password (admin/changeme) as shown in the screen prompt.

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please record the provided URL for future access.

1. After successfully installing DCE 5.0 Enterprise, contact us for
   authorization: email info@daocloud.io or call 400 002 6898.
