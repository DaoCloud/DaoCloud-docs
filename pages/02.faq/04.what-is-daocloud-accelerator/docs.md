---
title: '传说中的 DaoCloud 加速器是什么？'
taxonomy:
    category:
        - docs
---

DaoCloud 加速器是广受欢迎的 Docker 工具，解决了国内用户访问 Docker Hub 缓慢的问题。DaoCloud 加速器经历了两个版本，1.0 版本主要采用了 Docker Registry Mirror 的功能，结合国内的 CDN 服务，为用户提升镜像下载的速度，2.0 版本加入了 DaoCloud 大量自主研发的协议层优化，并提供了可以替代 Docker Pull 的客户端，完美解决国内获取 Docker 镜像 metadata的问题，并在此成倍提升下载速度。

下面我们分别介绍这两个版本的具体细节。


#### Docker 加速器 2.0

Docker 加速器 2.0 是 DaoCloud Toolbox 的一部分。

<!-- 2.0介绍，和FAQ，参考页面内容 -->



#### Docker 加速器 1.0

>>> Docker 加速器 1.0 仍在正常运行，但我们推荐您使用 Docker 加速器 2.0，获得更好的用户体验。

Docker 加速器是 DaoCloud 推出的 Docker Hub Mirror 服务的官方名称。

Docker 官方对 Mirror 的定义：

> Such a registry is provided by a third-party hosting infrastructure but is targeted at their customers only. Some mechanism ensures that public images are pulled from a sponsor registry to the mirror registry, to make sure that the customers of the third-party provider can docker pull those images locally.

Mirror 是 Docker Registry 的一种特殊类型，它起到了类似代理服务器的缓存角色，在用户和 Docker Hub 之间做镜像的缓存。这个功能的设计目的是为了企业客户访问 Docker Hub 时降低网络开销。

##### 加速器是什么？

DaoCloud 加速器是我们为中国开发者提供的 Docker Hub Mirror 服务。DaoCloud 的博客有两篇文章非常详细的介绍了 Docker Hub Mirror 的工作机制，和 DaoCloud 加速器的后台架构：

* **[玩转 Docker 镜像](http://blog.daocloud.io/how-to-master-docker-image/)**
* **[DaoCloud 宣布 Docker Hub Mirror 服务永久免费](http://blog.daocloud.io/daocloud-mirror-free/)**

Docker 镜像的分层文件系统是非常有趣的创新，作为 Docker 用户，大家感兴趣可以阅读 DaoCloud 成员孙宏亮撰写的 Docker 源码分析系列中有关 **[Docker镜像](http://blog.daocloud.io/docker-source-code-analysis-part9/)** 的文章。

##### 使用加速器的必要性

* 使用 Docker 的时候，需要经常从官方获取镜像。由于显而易见的网络原因，获取镜像的过程较慢，令人非常痛苦。因此 DaoCloud 推出 Docker 加速器解决这个难题。Docker 加速器利用 Docker 官方的 Mirror 机制，一次配置，无缝使用。
* 值得一提的是，DaoCloud 系统本身也是加速器的重度用户。我们在运行 Docker 的机器上都配置了加速器服务，有效的节省了抓取镜像的时间。

##### 加速方法

请先确定您的 Docker 版本高于 1.3.2。

然后参考 **[控制台中加速器](https://dashboard.daocloud.io/mirror)** 的操作手册。

##### Mirror 与 Private Registry 的区别

二者有着本质的差别。

* Private Registry 是开发者或者企业自建的镜像存储库，通常用来保存企业内部的 Docker 镜像，用于内部开发流程和产品的发布、版本控制。
* Mirror 是一种代理中转服务，我们提供的 Mirror 服务，直接对接 Docker Hub 的官方 Registry。Docker Hub 上有数以十万计的各类 Docker 镜像。
* 在使用 Private Registry 时，需要在 Docker Pull 或 Dockerfile 中直接键入 Private Registry 的地址，通常这样会导致与 Private Registry 的绑定，缺乏灵活性。
* 使用 Mirror 服务，只需要在 Docker 守护进程（Daemon）的配置文件中加入 Mirror 参数，即可在全局范围内透明的访问官方的 Docker Hub，避免了对 Dockerfile 镜像引用来源的修改。

##### 加速器与其他第三方提供的镜像有何区别？

* 加速器机制（Mirror 机制）是 Docker 的官方机制，兼容性好，方便，安全，高效。
* 加速器机制是 Docker 官方推出，在 1.3.2 版本之后提供长期的稳定支持，今后官方会在 Mirror 之上做更多的功能。
* 加速器可以 Docker 无缝集成，无需修改 Dockerfile，也无需修改命令。
* 加速器直接使用 Docker 官方的镜像，由于有 Docker 内置安全机制，可以确保不会有任何篡改。相比与其他第三方镜像，不会有安全隐患更不会留有后门。

##### 为什么我使用加速器后，没有明显提速？

* 请确保您的 docker 版本是 1.3.2 及以上，您可以使用 `docker -v` 查看您当前的版本。并且确保当您启动 `Docker Deamon` 进程时指定了 `–-registry-mirror` 参数，您可以参考加速器页面的“操作手册”获得详尽的配置帮助。

##### 工作原理

Mirror 是 Docker 的官方机制，它是 Registry 的一种特殊类型，在部署了 Registry 之后，需要开启 Mirror 模式并做一定的配置。具体的流程如下图：

![](http://blog.daocloud.io/wp-content/uploads/2015/03/1.jpg)

##### 准备工作

* 在公有云环境部署 Mirror Registry，并优化存储和网络访问（后文会详述）。
* 在客户端，修改 Docker 的配置文件，添加 `--registry-mirror` 参数（Mirror 控制台中有详细的配置步骤）。

##### Docker 加速器云端部署架构

下图是 DaoCloud 在搭建 Mirror 服务时，采用的架构：

![](http://blog.daocloud.io/wp-content/uploads/2015/03/Mirror_Arch.jpg)

我们选择了 UCloud 和七牛云存储。这样的架构是基于以下的几个考虑：

* 我们的 Mirror 服务主节点位于 UCloud 北京 BGP 机房。BGP 机房网络上行下行的速度都非常快，有助于获得稳定高速的对外访问带宽，在 Docker Hub Regsitry 下载 Image，获得不错的速度。
* 我们扩展了 Mirror 的 Registry Disk Driver，使它可以支持 UCloud 的 UDisk 服务。
* BGP 机房的云主机需要绑定外网 IP，并且是根据带宽收费。提供类似镜像下载服务，开销巨大。因此我们把下载缓存完成后的静态镜像文件，定期同步到七牛云，即降低了带宽成本，同时也享受到了 CDN 的加速。

##### 工作流程

Docker Hub 由 Index 和 Registry 构成，Index 保存镜像层（Image Layer）的散列值（Hash）和关联关系等元数据（Metadata），Registry 用于存储镜像层的实际二进制数据。在客户端没有配置 `--registry-mirror` 参数的情况下，每一次镜像抓取，客户端都会先连接 Index 获取元数据，然后再连接 Registry 获取实际的Image文件。由于 Docker Hub 的 Index 节点和 Regsitry 都部署国外，国内用户访问，经常遭遇连接超时或中断的情况，下载速度也极其缓慢。

在启用了 Mirror 之后，访问流程如下：

* 客户端的 Docker 守护进程（Daemon）连接 Index 获取元数据，这一部分的数据量极小，直连国外的速度可以忍受。
* 根据元数据的信息，Docker 的守护进程与 Mirror 服务器建立连接。如果抓取的镜像在 Mirror 上已经有缓存，就直接在 Mirror 上返回地址并下载。
* 如果镜像在 Mirror 并无缓存，Mirror 会与 Docker Hub Registry 建立连接，下载镜像，提供给用户的同时，在本地缓存。
* Mirror 下载 Docker Hub 镜像采用流传输的方式，即可以一边下载，一边提供给客户端的 Docker 守护进程，不必等待镜像完成下载。

通过以上的描述，可以发现，对于常用的镜像，Mirror 缓存命中率会非常高，如 Ubuntu 等基础镜像，这会极大的提高下载速度。同时 Docker 镜像采用分层的结构，即使镜像被更新，也只会下载被更新的数据层。

Mirror 服务亦可以通过网络优化，加速对远端 Docker Hub Registry 的访问速度，如采用高速的商业 VPN 建立从 Mirror 到 Docker Hub Registry 的访问。通过七牛等云存储和 CDN 分发网络，会进一步提高国内客户端的下载速度。