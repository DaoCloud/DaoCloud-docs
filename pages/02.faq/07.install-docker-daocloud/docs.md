---
title: '安装 Docker 环境并配置 DaoCloud 加速器'
---

![](3logo.png)

Docker 可以被安装在绝大多数主流的 Linux 发行版之上，由于内核差异，在 Windwos 和 Mac OS 上使用 Docker，需要采用 Boot2Docker 这个工具，它通过 VirtualBox 在 Windows 和 Mac OS 环境下一个 Linux 虚拟机，来提供 Docker 需要的内核环境。

由于众所周知的国内网络特殊性，保存在 AWS S3 之上的 Docker 的安装源文件，和 Boot2Docker 等在国内访问下载的速度非常缓慢，DaoCloud 提供了 Docker 安装源的镜像站点，[get.daocloud.io](http://get.daocloud.io)，这个网站提供了 Docker、Boot2Dcoker、Docker Toolbox、Docker Compose 等几乎所有主要的 Docker 安装包和工具包，我们采用了 CDN 加速，在国内访问和下载的速度非常快。

下面我们为大家介绍 Linux、Windows 和 Mac OS 上安装 Docker 的步骤，以及如何配置 DaoCloud 加速器。

![](getdocker.png)

#### 主流 Linux 发行版上安装

Docker 的[安装资源文件](https://get.docker.com/)存放在Amazon S3，国内下载速度极其缓慢。您可以通过执行下面的命令，使用 DaoCloud 镜像站点，高速安装Docker。
```
curl -sSL https://get.daocloud.io/docker | sh
```
该安装包适用于 Ubuntu，Debian，Centos 等大部分主流 Linux 发行版，DaoCloud 后台会每隔 3 小时同步一次 Docker 官方资源，确保您第一时间获取最新的 Docker 安装文件。

您也可以安装[体验版](https://github.com/docker/docker/tree/master/experimental)或测试版，体验最新 Docker。
```
curl -sSL https://get.daocloud.io/docker-experimental | sh
curl -sSL https://get.daocloud.io/docker-test | sh
```
如果安装不成功，可以选择使用二进制包安装方式，点击[下载二进制包](https://get.daocloud.io/docker/builds)，DaoCloud 安装镜像也提供了各种历史版本的安装包。

#### Windows 

首先，在 [get.daocloud.io](http://get.daocloud.io) 下载 Windows 版本的 Docker Toolbox，这是 Docker 提供的一个完整的开发组件，适用于 Mac OS X 10.8+ 和 Windows 7 & 8.1，Docker Toolbox 包含：

* Docker Client
* Docker Machine
* Docker Compose (Mac only)
* Docker Kitematic
* VirtualBox

Docker Toolbox 安装文件尺寸在 200M 左右，如果从 Docker 主站下载，速度会非常缓慢，建议您在 [get.daocloud.io](http://get.daocloud.io) 的镜像上下载。

下载完成后，点击安装：

![](Windows_7_x64.png)
![](Windows_7_x64_2.png)

在开始菜单，找到 Docker -> Docker Quickstart Terminal，经过一段时间的等待，即可进入 Docker 的命令行界面。

![](3d078026-c07f-3b1c-8dba-bf5337e154e4.png)

Docker Toolbox 启动了一个运行在 VirtualBox 虚拟机之上的 Linux，并通过类似 ssh 的方式，使 Windows 用户连接进入这个虚拟机的终端，进行各类 Docker 操作。有关 Docker Toolbox 的使用细节，可以参考 Docker 的[官方文档](https://docs.docker.com/engine/installation/windows/)。

现在，我们为 Windows 下的 Docker 环境安装配置 DaoCloud 加速器 v2，这样会成倍的提升下载 Docker Hub 镜像的速度。

登陆到 DaoCloud 控制台，点击「加速器」按钮，点击「立即开始」，在「接入自有主机」界面，点击 Windows 按钮。

![](DashboardDaoCloud1.png)

根据屏幕的提示，安装完成Windows Docker Toolbox（之前已经完成），并执行启动命令`docker-machine start default`，然后点击「安装好了」，进入下一步「安装主机监控程序」流程。

![](DashboardDaoCloudInstall.png)

在 Windows 的 Docker 终端执行界面显示的命令，稍等片刻后，会在 Docker 主机上完成安装包含了 DaoCloud 加速器的组件包，组件包启动后，会在「安装主机监控程序」的 DaoCloud 控制台页面下方显示一台已经接入的主机。

安装完成后，用户可以在 Windows 的 Docker 环境下，使用 `Dao Pull`命令高速下载 Docker Hub 镜像文件，同时，这台 Docker 主机已经被接入 DaoCloud 平台，用户可以在 DaoCloud 控制台的「我的集群」页面发现这台主机，可以执行管理和部署应用的操作。

#### Mac OS

Mac OS 上运行 Docker，也需要安装 Docker Toolbox，您同样可以在 [get.daocloud.io](http://get.daocloud.io) 下载并安装 Mac OS 版本的 Docker Toolbox。步骤与 Windows 版几乎一样，这里就不再重复。

安装完成后，在 Mac 的终端命令行，输入：

```
docker-machine ssh default
```

进入 Docker 的终端控制台后，可按照上述的步骤，完成 DaoCloud 加速器的安装，连接这台主机到 DaoCloud 平台。

![](daopull.png)