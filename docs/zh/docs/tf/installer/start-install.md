# 离线安装 d.run Token 工厂效能平台

本文介绍如何离线安装 **d.run Token 工厂效能平台**。安装时请使用产品清单文件 `manifest-cloud-tokfact.yaml`。

请在安装之前阅读并了解[部署要求](../../install/commercial/deploy-requirements.md)、[部署架构](../../install/commercial/deploy-arch.md)、[准备工作](../../install/commercial/prepare.md)，并先完成[安装依赖项](../../install/install-tools.md)。

查阅[安装器 Release Notes](../../install/release-notes.md)，避免所安装版本的已知问题，还可以从中查阅新增的功能特性。

## 第 1 步：下载离线包

请根据业务环境下载对应版本的离线包。Token 工厂完整离线包可在[下载中心 - Token 工厂](../../download/tf/index.md)获取。

### 离线镜像包（必需）

离线镜像包包含安装 Token 工厂所需的配置文件、镜像资源以及 Chart 包。
可以在[下载中心 - Token 工厂](../../download/tf/index.md)下载最新版本。

| CPU 架构 | 版本 | 点击下载 |
| :------- | :----- | :-----|
| AMD64 | v0.44.0 | [offline-v0.44.0-amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.44.0-amd64.tar) |
| <font color="green">ARM64</font> | v0.44.0 | [offline-v0.44.0-arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.44.0-arm64.tar) |

下载完毕后解压离线包。以 amd64 架构离线包为例：

```bash
tar -xvf offline-v0.44.0-amd64.tar
```

### ISO 操作系统镜像文件（必需）

对于 ISO 格式的操作系统镜像文件，在安装过程中请根据不同操作系统来下载对应的 ISO 文件。

ISO 操作系统镜像文件需要在[集群配置文件 clusterConfig.yaml](../../install/commercial/cluster-config.md)中进行配置。

| CPU 架构 | 操作系统版本 | 点击下载 |
| :------- | :--------- | :------- |
| AMD64    | CentOS 7 | [CentOS-7-x86_64-DVD-2009.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso) |
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

安装器从 v0.5.0 版本，需要提供操作系统的 osPackage 离线包，并在[集群配置文件 clusterConfig.yaml](../../install/commercial/cluster-config.md)中定义 `osPackagePath`。

其中 [Kubean](https://github.com/kubean-io/kubean) 提供了不同操作系统的osPackage 离线包，
可以前往 <https://github.com/kubean-io/kubean/releases> 查看。

目前安装器版本要求 osPackage 离线包的版本与之匹配，请根据对应版本下载 osPackage 离线包：

=== "V0.44.0"

    | 操作系统版本 | 点击下载 |
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

    | 操作系统版本 | 点击下载 |
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

    | 操作系统版本 | 点击下载 |
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

### Addon 离线包（可选）

Addon 离线包包含一些常用组件的 Helm Chart 离线包，具体清单请参考 [Addon](../../download/addon/history.md)。

安装器从 v0.5.0 版本，支持了 Addon 的离线包导入能力，如果需要支持 Addon 中所有的 Helm Chart 离线化。
可以在[下载中心](../../download/index.md)下载最新版本。

首先需要事先下载好离线包，并在[集群配置文件 clusterConfig.yaml](../../install/commercial/cluster-config.md)中定义 `addonOfflinePackagePath`。

### 一键下载所需离线包

我们提供了脚本来[一键下载所需的离线包](../../install/air-tag-download.md)。

以下是包含的离线包：

- 前置依赖工具离线包
- osPackage 离线包
- 安装器离线包

!!! note

    由于不同的 ISO 操作系统下载方式不一致，所以一键下载的离线包并不包含 ISO 文件。

## 第 2 步：配置 clusterConfig.yaml

这是集群配置文件，位于离线镜像包 `offline/sample` 目录下，具体的参数介绍请参考 [clusterConfig.yaml](../../install/commercial/cluster-config.md)。

!!! note

    目前离线镜像包中提供了标准的 7 节点模式模板。
    使用 Redhat 9.2 操作系统部署时，需要开启内核调优参数 `node_sysctl_tuning: true`。

## 第 3 步：安装

1. 执行以下命令开始安装 Token 工厂。安装器二进制文件位于 `offline/dce5-installer`，产品清单请使用 `manifest-cloud-tokfact.yaml`。

    ```shell
    ./offline/dce5-installer cluster-create \
      -c ./offline/sample/clusterConfig.yaml \
      -m ./offline/sample/manifest-cloud-tokfact.yaml
    ```

    !!! note

        安装器脚本命令说明：

        - `-c` 指定集群配置文件，必选
        - `-m` 指定产品清单；Token 工厂请使用 `manifest-cloud-tokfact.yaml`
        - `-z` 最小化安装
        - `-d` 开启 debug 模式
        - `--use-original-repo` 从源站下载可执行文件、拉取镜像等
        - 更多参数请使用 `--help` 查询

2. 安装完成后，命令行会提示安装成功。可通过屏幕提示的 URL，使用默认账号和密码（admin/changeme）访问控制台。

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

3. 成功安装 Token 工厂之后，请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
