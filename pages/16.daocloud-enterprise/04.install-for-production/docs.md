---
title: 生产环境安装 DCE
---

本篇文章将向你介绍安装 DCE 的预备知识和安装方法，你能够通过本篇文章了解到如何在生产环境中安装 DCE。

如果你是初次使用 DCE 或 对 DCE 不太了解，建议你先阅读[快速开始](http://docs.daocloud.io/daocloud-enterprise/quickstart)和 [DCE 架构](http://docs.daocloud.io/daocloud-enterprise/architure)。

## DCE 安装说明

DCE 安装包含了 Docker Engine CLI，DCE 通过使用 Docker Enging CLI 运行一套 DCE 运维套件。DCE 运维套件基于一个支持多种命令操作的 Docker 镜像，目前已经支持多种容器集群的安装管理操作，如安装 DCE 主控节点，接入容器节点等。

运维套件命令格式说明：

你能够通过加入 `-i` 参数交互式地使用 DCE 运维套件，下面是使用 DCE 运维套件的命令格式说明：

| Docker 客户端 | Docker 运行命令和参数 | DCE 镜像 | 运维套件子命令和参数 |
| ------------ | ------------------  | -------- | -----------------|
| `docker`  | `run --rm -i` | `daocloud.io/daocloud/dce` | `install --help` |
| `docker`  | `run --rm -i` | `daocloud.io/daocloud/dce` | `join --help` |
| `docker`  | `run --rm -i` | `daocloud.io/daocloud/dce` | `uninstall --help` |


下表为 DCE 运维套件支持的命令：

| 命令 | 说明 |
| ---  | ---  |
| `install`   | 安装 DCE 主控节点和副控节点 |
| `join`    | 安装 ECE 容器节点 |
| `pull`    | 拉取 DCE 服务镜像 |
| `uninstall` | 卸载现有的 DCE 主控节点，副控节点或容器节点 |
| `upgrade` | 升级现有的 DCE 主控节点，副控节点或容器节点 |
| `setup-overlay` | 建立 DCE Overlay 虚拟网络 |
| `start` | 启动 DCE |
| `stop` | 停止 DCE |
| `restart` | 重启 DCE |
| `logs` | 输出 DCE 日志 |
| `status` | 输出 DCE 状态信息 |
| `info` | 输出 DCE 信息 |


DCE 运维套件会从 DaoCloud Hub 拉取用于服务的镜像，并且运行基于这些镜像的容器。


## 安装准备

当你在一个生产环境中安装 DCE 时，你需要确保你的安装是安全的和可拓展的。

为了保证安装可靠无误，你需要先进行一系列的检查：
>* 硬件和软件最低要求
>* 网络检查
>* 存储卷检查

### 硬件和软件最低要求
>* 1.00 GB RAM
>* 3.00 GB 磁盘空间
>* 下列操作系统之一：
>  * RHEL 7.0, 7.1
>  * Ubuntu 14.04 LTS
>  * CentOS 7.1
>* 3.19 或以上的内核版本

>>>>> 如果你的操作系统的内核版本过低，你可以在本页面最底部查看到 Ubuntu 和 Centos 下升级内核的方法。

### 网络检查

因为 DCE 会占用一部分端口来实现容器集群中各个节点间的数据通信，所以在安装 DCE 之前，需要检查集群中的所有节点是否都能够正常通信，并且保证 DCE 占用的端口是打开的，未被其他程序占用。

下表是被 DCE 占用的端口：

| 端口 | 位置 |
| ----- | ----- |
| 12376 | 主控节点，副控节点，容器节点 |
| 12377 | 主控节点，副控节点，容器节点 |
| 80 | 主控节点，副控节点 |
| 2375 | 主控节点，副控节点 |
| 12380 | 主控节点，副控节点 |
| 12379 | 主控节点，副控节点 |


## 安装 Docker Engine

DCE 安装之前，需要在容器集群的所有节点上安装 Docker Engine，包括主控节点，副控节点和容器节点。

在每一个节点，你能够通过运行下面的命令安装在线 Docker Engine：
```bash
curl -sSL https://get.daocloud.io/docker | sh
```

你也可以从[Docker Offline Release](https://github.com/DaoCloud/docker-offline)下载适合你的离线安装包, 然后通过如下命令，离线安装 Docker Engine：
``` bash
tar -zxvf docker-offline-all-<docker-version>.tar.gz
./docker-offline/install.sh
```


安装完成 Docker Engine 后需要检查 Docker 运行状态，确保 Docker 正在运行。

```bash
service docker status
```

出现如下输出时，表示Docker 正在运行：
```bash
Redirecting to /bin/systemctl status  docker.service
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
   Active: active (running) since 二 2016-04-12 23:50:32 EDT; 8s ago
     Docs: https://docs.docker.com
```

如果 Docker 未在运行，你需要手动启动 Docker：
```
service docker start
```

如果你使用 Centos，你还需要将 Docker 加入开机自启，并关闭 selinux 和防火墙：
```bash
chkconfig docker on
setenforce 0 && sed -i '/^SELINUX=/c\SELINUX=disabled' /etc/selinux/config
systemctl stop firewalld
systemctl disable firewalld.service
```

>>>>> 更详细的 Docker Engine 安装可以参考[Docker Engine 安装](http://docs.daocloud.io/faq/install-docker-daocloud)

## 安装主控节点

### 1. 查看 DCE 运维套件可用的 `install` 命令选项
```
bash -c "$(docker run --rm daocloud.io/daocloud/dce install --help)"
```

输出帮助文档：

```
Install the DCE Controller.

Usage: do-install [options]

Description:
  The command will install the DCE controller on this machine.

Options:
  -q, --quiet             Quiet. Do not ask for anything.
  --force-pull            Always Pull Image, default is pull when missing.
  --swarm-port PORT       Specify the swarm manager port(default: 2376).
  --replica               Install as a replica for HA,
  --replica-controller IP Specify the primary controller IP installed.
  --no-overlay            Do not config Overlay network.
  --no-experimental       Disable experimental Swarm Experimental Features.
```

### 2. 通过 `install` 完成安装
```
bash -c "$(docker run --rm daocloud.io/daocloud/dce install)"

```

当出现如下输出时，程序安装完成：
```
Installed DCE
DCE CLI at 'export DOCKER_HOST="192.168.2.125:2375"; docker info'
DCE WEB UI at http://192.168.2.125
```

如果安装完成后，出现重启 Docker 的提示，请按照提示执行相关命令重启 Docker，保证 DCE 能够正常提供服务。
```
################################################################################
################################################################################
# Please run the script to enable Overlay Network :
# Ubuntu 14.04: service docker restart
# CentOS 7: systemctl restart docker
################################################################################
################################################################################
```


## 安装副控节点

DCE 已经支持高可用方案。当你在部署 DCE 的高可用容器集群时，你需要为主控节点配置多个副控节点。

下面将会向你演示如何在已经有 `192.168.2.125` 主控节点的情况下，安装 `192.168.2.126` 副控节点：
### 1. 通过如下命令安装
```
bash -c "$(docker run --rm daocloud.io/daocloud/dce install －－force-pull --replica --replica-controller 192.168.2.125)"

```

当出现如下输出时，安装完成：
```
Installed DCE
DCE CLI at 'export DOCKER_HOST="192.168.2.126:2375"; docker info'
DCE WEB UI at http://192.168.2.126
```
>>>>> 不同主机上显示的 IP 信息不同。

如果安装完成后，出现重启 Docker 的提示，请按照提示执行相关命令重启 Docker，保证 DCE 能够正常提供服务。
```
################################################################################
################################################################################
# Please run the script to enable Overlay Network :
# Ubuntu 14.04: service docker restart
# CentOS 7: systemctl restart docker
################################################################################
################################################################################
```

## 安装容器节点

现在你能够向 DCE 集群中添加容器节点。这些节点将用于运行你自己的容器和应用。

在安装容器节点前，你需要先掌握如下信息：
>* DCE 主控节点的 IP，例如： `192.168.2.125`
>* 容器节点的管理员账号信息

容器节点安装方法如下：

登录到某个容器节点，运行如下 `join` 命令：

```
bash -c "$(docker run --rm daocloud.io/daocloud/dce join －－force-pull 192.168.2.125)"
```

>>>>> `join` 命令将会拉取服务镜像并根据你提供的信息完成容器节点的接入。

在需要被接入的节点上，重复上一步。

安装完成后通过浏览器访问 DCE 控制台，你可以查看到容器集群的详细信息
![](dce.png)


## 卸载
当你需要卸载 DCE 时，你可以使用 `uninstall` 命令。这个命令只会卸载 DCE 的系统容器，对你自己部署的容器和应用不会有任何影响。
在卸载 DCE 时，应当先卸载容器节点和副控节点，将主控节点的卸载留在最后进行。


卸载 DCE
1. 登录到你想要卸载 DCE 的节点
2. 运行如下命令：
```
bash -c "$(docker run --rm daocloud.io/daocloud/dce uninstall)"
```
在卸载 DCE 后，会自动移除本地在 DCE 安装时从 Dokcer Hub 拉取的服务镜像
3. 在容器集群中的每个节点上重复步骤1和步骤2。请确保主控节点最后卸载


## 升级内核

如果你需要升级操作系统内核，你可以按照如下方法升级到新版内核。

### Ubuntu 下升级操作系统内核

首先从 [kernel.ubuntu.com](http://kernel.ubuntu.com/~kernel-ppa/mainline/) 下载你需要安装的内核版本的安装包，一共有三个包需要下载：

```
linux-headers-VERSION-NUMBER_all.deb
linux-headers-VERSION-NUMBER_amd64.deb
linux-image-VERSION-NUMBER_amd64.deb
```

安装并重启系统：

```bash
sudo dpkg -i *.deb
sudo reboot
```

### Centos 下升级操作系统内核

这里以在 Centos 7 下将内核升级到最新版本 4.5.0 作为例子。

首先导入 ELRepo 的公钥并安装 ELRepo:

```bash
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.orguname
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm 
```

更新操作系统内核到最新版本内核并配置 grub2：

```bash
yum install --enablerepo=elrepo-kernel kernel-ml
grub2-set-default 0
grub2-mkconfig -o /boot/grub2/grub.cfg
reboot
```






















