---
title: 使用脚本命令手动添加主机
taxonomy:
    category:
        - docs
process:
    twig: true
---

如果您有一台或多台 Linux 主机（不论是裸机还是虚机），我们推荐您采取手动安装的方式，将自有主机添加的集群。

##### 安装前准备

安装前请确保：

* 已连接至互联网（但不需要公网 IP）。
* 建议使用官方支持的操作系统。

目前由 DaoCloud 官方支持的操作系统：

* Ubuntu
  - 兼容版本：12.04、14.04、15.04\*
* CentOS
  - 兼容版本：6、7
* Debian
  - 兼容版本：7\*
* Fedora
  - 兼容版本：18\*、20\*

> 提示：带有 `*` 的版本仅提供安装支持。

##### 手动添加主机到集群（安装 `daomonit`）

1. 在控制台点击「我的集群」
2. 选择一个目标集群，或者创建一个新的集群
3. 点击添加主机
4. 在接入自有主机界面，将鼠标移到「我已有一台主机」，选中您的操作系统类型，并点击
5. 根据界面提示，完成后续操作
6. 完成后，您将会在集群管理界面看到「检测到主机」

![](cli.png?resize=800)

>>>>> 完成主机的添加后，您可以向主机部署您的应用，或者从 DaoCloud 镜像仓库选择镜像部署，具体的操作步骤，请您参考[使用 DaoCloud 部署和管理应用](../../app-deploy-mgmt)这部分的文档内容。

> `daomonit` 为 DaoCloud 的主机监控程序，帮助与用户账户或组织账户进行绑定以及对 Docker 服务进行监控和管理。

##### 开启或关闭自动启动

* 对于非 systemd 管理的系统请使用 `chkconfig daomonit on|off`。
* 对于 systemd 管理的系统请使用 `systemctl enable|disable daomonit`。

##### 要启动、停止或重启

* 对于非 systemd 管理的系统请使用 `service daomonit start|stop|restart`。
* 对于 systemd 管理的系统请使用 `systemctl start|stop|restart daomonit`。

##### 卸载 `daomonit`

* 对于 CentOS 和 Fedora 请使用 `rpm -e daomonit`。
* 对于 Ubuntu 和 Debian 请使用 `dpkg -r daomonit`。

>>>>> 在添加主机的同时，安装程序会在您的主机上安装 DaoCloud Toolbox，您可以使用 DaoCloud Toolbox 的加速器和清道夫功能，具体您可以参考[介绍文档](../../faq/what-is-daocloud-accelerator)。