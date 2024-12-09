# 离线安装 DCE 5.0 商业版

请在安装之前阅读并了解[部署要求](deploy-requirements.md)、[部署架构](deploy-arch.md)、[准备工作](prepare.md)。

查阅[安装器 Release Notes](../release-notes.md)，避免所安装版本的已知问题，还可以从中查阅新增的功能特性。

## 第 1 步：下载离线包

请根据业务环境下载对应版本的离线包。

### 离线镜像包（必需）

离线镜像包包含安装 DCE 5.0 各个产品模块所需的配置文件、镜像资源以及 Chart 包。
可以在[下载中心](../../download/index.md)下载最新版本。

| CPU 架构 | 版本 | 点击下载 |
| :------- | :----- | :-----|
| AMD64 | v0.24.0 | [offline-v0.24.0-amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.24.0-amd64.tar) |
| <font color="green">ARM64</font> | v0.24.0 | [offline-v0.24.0-arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.24.0-arm64.tar) |

下载完毕后解压离线包。以 amd64 架构离线包为例：

```bash
tar -xvf offline-v0.24.0-amd64.tar
```

### ISO 操作系统镜像文件（必需）

对于 ISO 格式的操作系统镜像文件，在安装过程中请根据不同操作系统来下载对应的 ISO 文件。

ISO 操作系统镜像文件需要在[集群配置文件 clusterConfig.yaml](./cluster-config.md)中进行配置。

| CPU 架构 | 操作系统版本 | 点击下载 |
| :------- | :--------- | :------- |
| AMD64    | CentOS 7 | - |
| | Redhat 7、8、9 | [assembly-field-downloads-page-content-61451](https://developers.redhat.com/products/rhel/download#assembly-field-downloads-page-content-61451) <br />注意：Redhat 操作系统需要 Redhat 的账号才可以下载 |
| | Ubuntu 20.04.6 LTS | [ubuntu-20.04.6-live-server-amd64.iso](https://releases.ubuntu.com/focal/ubuntu-20.04.6-live-server-amd64.iso) |
| | Ubuntu 22.04.5 LTS | [ubuntu-22.04.5-live-server-amd64.iso](https://releases.ubuntu.com/jammy/ubuntu-22.04.5-live-server-amd64.iso) |
| | 统信 UOS V20（1020a）| [uniontechos-server-20-1020a-amd64.iso](https://cdimage-download.chinauos.com/uniontechos-server-20-1020a-amd64.iso) |
| | openEuler 22.03 | [openEuler-22.03-LTS-SP1-x86_64-dvd.iso](https://mirrors.nju.edu.cn/openeuler/openEuler-22.03-LTS-SP1/ISO/x86_64/openEuler-22.03-LTS-SP1-x86_64-dvd.iso) |
| | Oracle Linux R9 U1 | [OracleLinux-R9-U1-x86_64-dvd.iso](https://yum.oracle.com/ISOS/OracleLinux/OL9/u1/x86_64/OracleLinux-R9-U1-x86_64-dvd.iso) |
| | Oracle Linux R8 U7 | [OracleLinux-R8-U7-x86_64-dvd.iso](https://yum.oracle.com/ISOS/OracleLinux/OL8/u7/x86_64/OracleLinux-R8-U7-x86_64-dvd.iso) |
| | Rocky Linux 9.2 | [Rocky-9.2-x86_64-dvd.iso](https://dl.rockylinux.org/vault/rocky/9.2/isos/x86_64/Rocky-9.2-x86_64-dvd.iso) |
| | Rocky Linux 8.10 | [Rocky-8.10-x86_64-dvd1.iso](https://download.rockylinux.org/pub/rocky/8/isos/x86_64/Rocky-8.10-x86_64-dvd1.iso) |
| <font color="green">ARM64</font> | Kylin Linux Advanced Server release V10 (Sword) SP2 | [查看申请地址](https://www.kylinos.cn/support/trial.html) |
| | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [查看申请地址](https://www.kylinos.cn/support/trial.html) |

!!! note

    - 建议所有操作系统以 Server 模式安装
    - 麒麟操作系统需要提供个人信息才能下载使用，下载时请选择 V10 (Sword) SP2

### osPackage 离线包（必需）

osPackage 离线包是 [Kubean](https://github.com/kubean-io/kubean)这个开源项目为 Linux
操作系统离线软件源做的补充内容，例如 openEuler 22.03 中缺少了selinux-policy-35.5-15.oe2203.noarch.rpm。

安装器从 v0.5.0 版本，需要提供操作系统的 osPackage 离线包，并在[集群配置文件 clusterConfig.yaml](./cluster-config.md)中定义 `osPackagePath`。

其中 [Kubean](https://github.com/kubean-io/kubean) 提供了不同操作系统的osPackage 离线包，
可以前往 <https://github.com/kubean-io/kubean/releases> 查看。

目前安装器版本要求 osPackage 离线包的版本与之匹配，请根据对应版本下载 osPackage 离线包：

=== "V0.24.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-centos7-v0.21.1.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-redhat8-v0.21.1.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-redhat7-v0.21.1.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-redhat9-v0.21.1.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-ubuntu2004-v0.21.1.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-ubuntu2204-v0.21.1.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-openeuler22.03-v0.21.1.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-oracle9-v0.21.1.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-oracle8-v0.21.1.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.21.1.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-rocky9-v0.21.1.tar.gz) |
    | Rocky Linux 8.10 | [os-pkgs-rocky8-v0.21.1.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-rocky8-v0.21.1.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-kylin-v10sp2-v0.21.1.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.21.1.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.21.1/os-pkgs-kylin-v10sp3-v0.21.1.tar.gz) |

=== "V0.23.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-centos7-v0.19.0.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-redhat8-v0.19.0.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-redhat7-v0.19.0.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-redhat9-v0.19.0.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-ubuntu2004-v0.19.0.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-ubuntu2204-v0.19.0.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-openeuler22.03-v0.19.0.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-oracle9-v0.19.0.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-oracle8-v0.19.0.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.19.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-rocky9-v0.19.0.tar.gz) |
    | Rocky Linux 8.10 | [os-pkgs-rocky8-v0.19.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-rocky8-v0.19.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-kylin-v10sp2-v0.19.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-kylin-v10sp3-v0.19.0.tar.gz) |

=== "V0.22.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-centos7-v0.19.0.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-redhat8-v0.19.0.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-redhat7-v0.19.0.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-redhat9-v0.19.0.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-ubuntu2004-v0.19.0.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-ubuntu2204-v0.19.0.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-openeuler22.03-v0.19.0.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-oracle9-v0.19.0.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-oracle8-v0.19.0.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.19.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-rocky9-v0.19.0.tar.gz) |
    | Rocky Linux 8.10 | [os-pkgs-rocky8-v0.19.0.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-rocky8-v0.19.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-kylin-v10sp2-v0.19.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.19.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.19.0/os-pkgs-kylin-v10sp3-v0.19.0.tar.gz) |

=== "V0.21.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-centos7-v0.18.5.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-redhat8-v0.18.5.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-redhat7-v0.18.5.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-redhat9-v0.18.5.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-ubuntu2004-v0.18.5.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-ubuntu2204-v0.18.5.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-openeuler22.03-v0.18.5.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-oracle9-v0.18.5.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-oracle8-v0.18.5.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.18.5.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-rocky9-v0.18.5.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-kylin-v10sp2-v0.18.5.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.18.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.18.5/os-pkgs-kylin-v10sp3-v0.18.5.tar.gz) |

=== "V0.20.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-centos7-v0.17.5.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-redhat8-v0.17.5.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-redhat7-v0.17.5.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-redhat9-v0.17.5.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-ubuntu2004-v0.17.5.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-ubuntu2204-v0.17.5.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-openeuler22.03-v0.17.5.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-oracle9-v0.17.5.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-oracle8-v0.17.5.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.17.5.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-rocky9-v0.17.5.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-kylin-v10sp2-v0.17.5.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Halberd) SP3 | [os-pkgs-kylinv10sp3-v0.17.5.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.17.5/os-pkgs-kylin-v10sp3-v0.17.5.tar.gz) |

=== "V0.19.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-centos7-v0.16.3.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-redhat8-v0.16.3.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-redhat7-v0.16.3.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-redhat9-v0.16.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-kylinv10-v0.16.3.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-ubuntu2004-v0.16.3.tar.gz) |
    | Ubuntu 22.04  | [os-pkgs-ubuntu2204-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-ubuntu2204-v0.16.3.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-openeuler22.03-v0.16.3.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-oracle9-v0.16.3.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.16.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-oracle8-v0.16.3.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.16.3.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-rocky9-v0.16.3.tar.gz) |

=== "V0.18.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-centos7-v0.15.3.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-redhat8-v0.15.3.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-redhat7-v0.15.3.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-redhat9-v0.15.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-kylinv10-v0.15.3.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-ubuntu2004-v0.15.3.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-openeuler22.03-v0.15.3.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-oracle9-v0.15.3.tar.gz) |
    | Oracle Linux R8 U7 | [os-pkgs-oracle8-v0.15.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-oracle8-v0.15.3.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.15.3.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.15.3/os-pkgs-rocky9-v0.15.3.tar.gz) |

=== "V0.17.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-centos7-v0.13.11.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-redhat8-v0.13.11.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-redhat7-v0.13.11.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-redhat9-v0.13.11.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-kylinv10-v0.13.11.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-ubuntu2004-v0.13.11.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-openeuler22.03-v0.13.11.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.13.11.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-oracle9-v0.13.11.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.13.11.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.13.11/os-pkgs-rocky9-v0.13.11.tar.gz) |

=== "V0.16.1"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-centos7-v0.13.9.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-redhat8-v0.13.9.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-redhat7-v0.13.9.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-redhat9-v0.13.9.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-kylinv10-v0.13.9.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-ubuntu2004-v0.13.9.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-openeuler22.03-v0.13.9.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.13.9.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-oracle9-v0.13.9.tar.gz) |
    | Rocky Linux 9.2 | [os-pkgs-rocky9-v0.13.9.tar.gz](https://github.com/kubean-io/kubean/releases/download/v0.13.9/os-pkgs-rocky9-v0.13.9.tar.gz) |

=== "V0.15.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-centos7-v0.12.2.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-redhat8-v0.12.2.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-redhat7-v0.12.2.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-redhat9-v0.12.2.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-kylinv10-v0.12.2.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-ubuntu2004-v0.12.2.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-openeuler22.03-v0.12.2.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.12.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.12.2/os-pkgs-oracle9-v0.12.2.tar.gz) |

=== "V0.14.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-centos7-v0.11.2.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-redhat8-v0.11.2.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-redhat7-v0.11.2.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-redhat9-v0.11.2.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-kylinv10-v0.11.2.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-ubuntu2004-v0.11.2.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-openeuler22.03-v0.11.2.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.11.2.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.11.2/os-pkgs-oracle9-v0.11.2.tar.gz) |

=== "V0.13.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-centos7-v0.10.0.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-redhat8-v0.10.0.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-redhat7-v0.10.0.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-redhat9-v0.10.0.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-kylinv10-v0.10.0.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-ubuntu2004-v0.10.0.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-openeuler22.03-v0.10.0.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.10.0.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.10.0/os-pkgs-oracle9-v0.10.0.tar.gz) |

=== "V0.12.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-centos7-v0.9.3.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat8-v0.9.3.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat7-v0.9.3.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat9-v0.9.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-kylinv10-v0.9.3.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-ubuntu2004-v0.9.3.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-openeuler22.03-v0.9.3.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.9.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-oracle9-v0.9.3.tar.gz) |

=== "V0.11.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-centos7-v0.8.6.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-redhat8-v0.8.6.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-redhat7-v0.8.6.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-redhat9-v0.8.6.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-kylinv10-v0.8.6.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-ubuntu2004-v0.8.6.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-openeuler22.03-v0.8.6.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.8.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.6/os-pkgs-oracle9-v0.8.6.tar.gz) |

=== "V0.10.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-centos7-v0.7.4.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-redhat8-v0.7.4.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-redhat7-v0.7.4.tar.gz) |
    | Redhat 9     | [os-pkgs-redhat9-v0.8.3.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.8.3/os-pkgs-redhat9-v0.8.3.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-kylinv10-v0.7.4.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-ubuntu2004-v0.7.4.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-openeuler22.03-v0.7.4.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.7.4.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-oracle9-v0.7.4.tar.gz) |

=== "V0.9.0"

    | 操作系统版本 | 点击下载 |
    | :--------- | :------ |
    | CentOS 7     | [os-pkgs-centos7-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-centos7-v0.6.6.tar.gz) |
    | Redhat 8     | [os-pkgs-redhat8-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-redhat8-v0.6.6.tar.gz) |
    | Redhat 7     | [os-pkgs-redhat7-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-redhat7-v0.6.6.tar.gz) |
    | Kylin Linux Advanced Server release V10 (Sword) SP2 | [os-pkgs-kylinv10-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-kylinv10-v0.6.6.tar.gz) |
    | Ubuntu 20.04  | [os-pkgs-ubuntu2004-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-ubuntu2004-v0.6.6.tar.gz) |
    | openEuler 22.03 | [os-pkgs-openeuler22.03-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-openeuler22.03-v0.6.6.tar.gz) |
    | Oracle Linux R9 U1 | [os-pkgs-oracle9-v0.6.6.tar.gz](https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-oracle9-v0.6.6.tar.gz) |

统信 UOS V20（1020a）osPackage 部署请参考 [UOS V20 (1020a) 操作系统上部署 DCE 5.0](../os-install/uos-v20-install-dce5.0.md)。

### Addon 离线包（可选）

Addon 离线包包含一些常用组件的 Helm Chart 离线包，具体清单请参考 [Addon](../../download/addon/history.md)。

安装器从 v0.5.0 版本，支持了 Addon 的离线包导入能力，如果需要支持 Addon 中所有的 Helm Chart 离线化。
可以在[下载中心](../../download/index.md)下载最新版本。

首先需要事先下载好离线包，并在[集群配置文件 clusterConfig.yaml](./cluster-config.md)中定义 `addonOfflinePackagePath`。

### 一键下载所需离线包

我们提供了脚本来[一键下载安装 DCE 5.0 所需的离线包](../air-tag-download.md)。

以下是包含的离线包：

- 前置依赖工具离线包
- osPackage 离线包
- 安装器离线包

!!! note

    由于不同的 ISO 操作系统下载方式不一致，所以一键下载的离线包并不包含 ISO 文件。

## 第 2 步：配置 clusterConfig.yaml

这是集群配置文件，位于离线镜像包 `offline/sample` 目录下，具体的参数介绍请参考 [clusterConfig.yaml](cluster-config.md)。

!!! note

    目前离线镜像包中提供了标准的 7 节点模式模板。
    使用 Redhat 9.2 操作系统部署时，需要开启内核调优参数 `node_sysctl_tuning: true`。

## 第 3 步：安装

1. 执行以下命令开始安装 DCE 5.0，安装器二进制文件位于 `offline/dce5-installer`。

    ```shell
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml
    ```

    !!! note

        安装器脚本命令说明：
        
        - -c 来指定集群配置文件，必选
        - -m 参数指定 manifest 文件
        - -z 最小化安装
        - -d 开启 debug 模式
        - --use-original-repo 从源站下载可执行文件、拉取镜像等
        - 更多参数请使用 --help 查询

1. 安装完成后，命令行会提示安装成功。恭喜您！现在可以通过屏幕提示的 URL 使用默认的账号和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

1. 成功安装 DCE 5.0 商业版之后，请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
