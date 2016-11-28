---
title: 'Docker 入门'
---

作者：[刘思贤](http://starlight36.com/aboutme)，授权 DaoCloud 刊登使用。

---
 
关注 Docker 这项技术差不多一年多了，最近关于 Docker 的使用案例越来越多，于是就想动手实验下这项技术。自己整理了一个入门手册，分享给大家。

### Docker 是什么

Docker 是一种容器技术，它可以将应用和环境等进行打包，形成一个独立的，类似于 iOS 的 APP 形式的「应用」，这个应用可以直接被分发到任意一个支持 Docker 的环境中，通过简单的命令即可启动运行。Docker 是一种最流行的容器化实现方案。和虚拟化技术类似，它极大的方便了应用服务的部署；又与虚拟化技术不同，它以一种更轻量的方式实现了应用服务的打包。使用 Docker 可以让每个应用彼此相互隔离，在同一台机器上同时运行多个应用，不过他们彼此之间共享同一个操作系统。Docker 的优势在于，它可以在更细的粒度上进行资源的管理，也比虚拟化技术更加节约资源。

 ![](http://blog.daocloud.io/wp-content/uploads/2015/05/vm-vs-docker-architecture1.png)

<center>上图：虚拟化和 Docker 架构对比，来自 Docker 官网</center>


### 基本概念

开始试验 Docker 之前，我们先来了解一下 Docker 的几个基本概念：

**镜像**：我们可以理解为一个预配置的系统光盘，这个光盘插入电脑后就可以启动一个操作系统。当然由于是光盘，所以你无法修改它或者保存数据，每次重启都是一个原样全新的系统。Docker 里面镜像基本上和这个差不多。

**容器**：同样一个镜像，我们可以同时启动运行多个，运行期间的产生的这个实例就是容器。把容器内的操作和启动它的镜像进行合并，就可以产生一个新的镜像。

### 开始

Docker 基于 [LXC](http://baike.baidu.com/view/6572152.htm) 技术实现，依赖于 Linux 内核，所以 Docker 目前只能在 Linux 以原生方式运行。目前主要的 Linux 发行版在他们的软件仓库中内置了 Docker：

- Ubuntu:
	- Ubuntu Trusty 14.04 (LTS)
	- Ubuntu Precise 12.04 (LTS)
	- Ubuntu Saucy 13.10

- CentOS:
	- CentOS 7

Docker 要求 64 位环境，这些操作系统下可以直接通过命令安装 Docker，老一些操作系统 Docker 官方也提供了安装方案。下面的实验基于 CentOS 7 进行。关于其他版本操作系统上 Docker 的安装，请参考官方文档：[https://docs.docker.com/installation/](https://docs.docker.com/installation/)

#### 在 CentOS 7 上安装 Docker

使用 yum 从软件仓库安装 Docker：

```shell
yum install docker
```

首先启动 Docker 的守护进程：

```shell
service docker start
```

如果想要 Docker 在系统启动时运行，执行：

```shell
chkconfig docker on
```

**Docker 在 CentOS 上好像和防火墙有冲突，应用防火墙规则后可能导致 Docker 无法联网，重启 Docker 可以解决**。

由于众所周知的原因，国内安装 Docker 和 Docker 周边的一些工具，访问 Docker Hub 的速度都非常慢。推荐大家使用 DaoCloud 提供的[镜像站点](http://get.daocloud.io/)，这个站点提供了 Docker 安装文件，Boot2Docker 工具的高速下载，并且提供 Docker Hub 加速器服务，有效提升 docker pull image 的速度。

### Docker仓库

Docker 使用类似 git 的方式管理镜像。通过基本的镜像可以定制创建出来不同种应用的 Docker 镜像。[Docker Hub](https://registry.hub.docker.com) 是 Docker 官方提供的镜像中心。在这里可以很方便地找到各类应用、环境的镜像。由于 Docker 使用联合文件系统，所以镜像就像是夹心饼干一样一层层构成，相同底层的镜像可以共享。所以 Docker 还是相当节约磁盘空间的。要使用一
个镜像，需要先从远程的镜像注册中心拉取，这点非常类似 git。

```shell
docker pull ubuntu
```

我们很容易就能从 Docker Hub 镜像注册中心下载一个最新版本的 ubuntu 镜像到本地。国内网络可能会稍慢，[DaoCloud](https://www.daocloud.io)提供了 Docker Hub 的国内加速服务，可以尝试配置使用。

>>>>> 关于安装 Docker 和 DaoCloud 加速器，请阅读「[安装 Docker 环境并配置 DaoCloud 加速器](../../faq/install-docker-daocloud)」一文。

### 运行一个容器

使用 Docker 最关键的一步就是从镜像创建容器。有两种方式可以创建一个容器：使用 `docker create` 命令创建容器，或者使用 `docker run` 命令运行一个新容器。两个命令并没有太大差别，只是前者创建后并不会立即启动容器。

以 Ubuntu 为例，我们启动一个新容器，并将 Ubuntu 的 Shell 作为入口：

```shell
docker run -it ubuntu:latest sh -c '/bin/bash'
```

这时候我们成功创建了一个 Ubuntu 的容器，并将当前终端连接为这个 Ubuntu 的 bash shell。这时候就可以愉快地使用 Ubuntu 的相关命令了。

参数 `-i` 表示这是一个交互容器，会把当前标准输入重定向到容器的标准输入中，而不是终止程序运行，`-t` 指为这个容器分配一个终端。

好了，按 `Ctrl+D` 可以退出这个容器了。

在容器运行期间，我们可以通过 `docker ps` 命令看到所有当前正在运行的容器。添加-a参数可以看到所有创建的容器：

```shell
docker ps -a
```

```
[root@localhost ~]# docker ps -a
CONTAINER ID        IMAGE                        COMMAND                CREATED             STATUS                      PORTS               NAMES
cb2b06c83a50        ubuntu:latest                "sh -c /bin/bash"      7 minutes ago       Exited (0) 7 seconds ago                        trusting_morse
```

每个容器都有一个唯一的 ID 标识，通过 ID 可以对这个容器进行管理和操作。在创建容器时，我们可以通过 `--name` 参数指定一个容器名称，如果没有指定系统将会分配一个，就像这里的「trusting_morse」。

当我们按 `Ctrl+D` 退出容器时，命令执行完了，所以容器也就退出了。要重新启动这个容器，可以使用 `docker start` 命令：

```shell
docker start -i trusting_morse
```

同样，`-i` 参数表示需要交互式支持。

**注意：每次执行 `docker run` 命令都会创建新的容器，建议一次创建后，使用 `docker start/stop` 来启动和停用容器。**

### 存储

在 Docker 容器运行期间，对文件系统的所有修改都会以增量的方式反映在容器使用的联合文件系统中，**并不是真正的对只读层数据信息修改**。每次运行容器对它的修改，都可以理解成对夹心饼干又添加了一层奶油。这层奶油仅供当前容器使用。当删除 Docker 容器，或通过该镜像重新启动时，之前的更改将会丢失。这样做并不便于我们持久化和共享数据。Docker 的数据卷这个东西可以帮到我们。

>>> 使用 Docker，或者在 DaoCloud 部署应用时，请特别注意容器内数据持久化的问题，具体请阅读「[如何在容器中保存数据](../../faq/how-to-keep-data-in-docker)」一文。

在创建容器时，通过 `-v` 参数可以指定将容器内的某个目录作为数据卷加载：

```shell
docker run -it -v /home/www ubuntu:latest sh -c '/bin/bash'
```

在容器中会多一个 /home/www 挂载点，在这个挂载点存储数据会绕过联合文件系统。我们可以通过下面的命令来找到这个数据卷在主机上真正的存储位置：

```shell
docker inspect -f {{.Volumes}} trusting_morse
```

你会看到输出了一个指向到`/var/lib/docker/vfs/dir/...`的目录。`CD` 进入后你会发现在容器中对 `/home/www` 的读写创建，都会反映到这儿。事实上，`/home/www` 就是挂载自这个位置。

有时候，我们需要将本地的文件目录挂载到容器内的位置，同样是使用数据卷这一个特性，`-v`参数格式为：

```shell
docker run -it -v [host_dir]:[container_dir]
```

`host_dir`是主机的目录，`container_dir`是容器的目录。

容器和容器之间是可以共享数据卷的，我们可以单独创建一些容器，存放如数据库持久化存储、配置文件一类的东西，然而这些容器并不需要运行。

```shell
docker run --name dbdata ubuntu echo "Data container."
```

在需要使用这个数据容器的容器创建时 `--volumes-from [容器名]` 的方式来使用这个数据共享容器。

### 网络

Docker 容器内的系统工作起来就像是一个虚拟机，容器内开放的端口并不会真正开放在主机上。可以使我们的容器更加安全，而且不会产生容器间端口的争用。想要将 Docker 容器的端口开放到主机上，可以使用类似端口映射的方式。

在 Docker 容器创建时，通过指定 `-p` 参数可以暴露容器的端口在主机上：

```shell
docker run -it -p 22 ubuntu sh -c '/bin/bash'
```

现在我们就将容器的 22 端口开放在了主机上，注意主机上对应端口是自动分配的。如果想要指定某个端口，可以通过 `-p [主机端口]:[容器端口]` 参数指定。

容器和容器之间想要网络通讯，可以直接使用 `--link` 参数将两个容器连接起来。例如 WordPress 容器对 some-mysql 的连接：

```shell
docker run --name some-wordpress --link some-mysql:mysql -p 8080:80 -d wordpress
```

### 环境变量

通过 Docker 打包的应用，对外就像是一个密闭的 exe 可执行文件。有时候我们希望 Docker 能够使用一些外部的参数来使用容器，这时候参数可以通过环境变量传递进去，通常情况下用来传递比如 MySQL 数据库连接这种的东西。环境变量通过 `-e` 参数向容器传递：

```shell
docker run --name some-wordpress -e WORDPRESS_DB_HOST=10.1.2.3:3306 \
    -e WORDPRESS_DB_USER=... -e WORDPRESS_DB_PASSWORD=... -d wordpress
```

关于 Docker 到现在就有了一个基本的认识了。接下来我会给大家介绍如何创建镜像。

### 创建镜像

Docker 强大的威力在于可以把自己开发的应用随同各种依赖环境一起打包、分发、运行。要创建一个新的 Docker 镜像，通常基于一个已有的 Docker 镜像来创建。Docker 提供了两种方式来创建镜像：把容器创建为一个新的镜像、使用 Dockerfile 创建镜像。

#### 将容器创建为镜像

为了创建一个新的镜像，我们先创建一个新的容器作为基底：

```shell
docker run -it ubuntu:latest sh -c '/bin/bash'
```

现在我们可以对这个容器进行修改了，例如我们可以配置 PHP 环境、将我们的项目代码部署在里面等：

```shell
apt-get install php
# some other opreations ...
```

当执行完操作之后，我们按 `Ctrl+D` 退出容器，接下来使用 `docker ps -a` 来查找我们刚刚创建的容器 ID：

```shell
docker ps -a
```

可以看到我们最后操作的那个 Ubuntu 容器。这时候只需要使用 `docker commit` 即可把这个容器变为一个镜像了：

```shell
docker commit 8d93082a9ce1 ubuntu:myubuntu
```

这时候 docker 容器会被创建为一个新的 Ubuntu 镜像，版本名称为 `myubuntu`。以后我们可以随时使用这个镜像来创建容器了，新的容器将自动包含上面对容器的操作。

如果我们要在另外一台机器上使用这个镜像，可以将一个镜像导出：

```shell
docker save -o myubuntu.tar.gz ubuntu:myubuntu
```

现在我们可以把刚才创建的镜像打包为一个文件分发和迁移了。要在一台机器上导入镜像，只需要：

```shell
docker import myubuntu.tar.gz
```

这样在新机器上就拥有了这个镜像。

**注意：通过导入导出的方式分发镜像并不是 Docker 的最佳实践，因为我们有 Docker Hub。**

Docker Hub 提供了类似 GitHub 的镜像存管服务。一个镜像发布到 Docker Hub 不仅可以供更多人使用，而且便于镜像的版本管理。在一个企业内部可以通过自建 [Docker Registry](https://github.com/docker/docker-registry) 的方式来统一管理和发布镜像。将 Docker Registry 集成到版本管理和上线发布的工作流之中，还有许多工作要做，在我整理出最佳实践后会第一时间分享。

#### 使用 Dockerfile 创建镜像

使用命令行的方式创建 Docker 镜像通常难以自动化操作。在更多的时候，我们使用 Dockerfile 来创建 Docker 镜像。Dockerfile 是一个纯文本文件，它记载了从一个镜像创建另一个新镜像的步骤。撰写好 Dockerfile 文件之后，我们就可以轻而易举的使用 `docker build` 命令来创建镜像了。

Dockerfile 非常简单，仅有以下命令在 Dockerfile 中常被使用：

<table>
<tbody>
<tr>
<th>命令</th>
<th>参数</th>
<th>说明</th>
</tr>
<tr>
<td>#</td>
<td>-</td>
<td>注释说明</td>
</tr>
<tr>
<td>FROM</td>
<td>&lt;image&gt;[:&lt;tag&gt;]</td>
<td>从一个已有镜像创建，例如ubuntu:latest</td>
</tr>
<tr>
<td>MAINTAINER</td>
<td>Author &lt;some-one@example.com&gt;</td>
<td>镜像作者名字，如Max Liu &lt;some-one@example.com&gt;</td>
</tr>
<tr>
<td>RUN</td>
<td>&lt;cmd&gt;或者['cmd1', 'cmd2'…]</td>
<td>在镜像创建用的临时容器里执行单行命令</td>
</tr>
<tr>
<td>ADD</td>
<td>&lt;src&gt; &lt;dest&gt;</td>
<td>将本地的&lt;src&gt;添加到镜像容器中的&lt;dest&gt;位置</td>
</tr>
<tr>
<td>VOLUME</td>
<td>&lt;path&gt;或者['/var', 'home']</td>
<td>将指定的路径挂载为数据卷</td>
</tr>
<tr>
<td>EXPOSE</td>
<td>&lt;port&gt; [&lt;port&gt;...]</td>
<td>将指定的端口暴露给主机</td>
</tr>
<tr>
<td>ENV</td>
<td>&lt;key&gt; &lt;value&gt; 或者 &lt;key&gt; = &lt;value&gt;</td>
<td>指定环境变量值</td>
</tr>
<tr>
<td>CMD</td>
<td>["executable","param1","param2"]</td>
<td>容器启动时默认执行的命令。注意一个Dockerfile中只有最后一个CMD生效。</td>
</tr>
<tr>
<td>ENTRYPOINT</td>
<td>["executable", "param1", "param2"]</td>
<td>容器的进入点</td>
</tr>
</tbody>
</table>

下面是一个 Dockerfile 的例子：

```
# This is a comment
FROM ubuntu:14.04
MAINTAINER Kate Smith <ksmith@example.com>
RUN apt-get update && apt-get install -y ruby ruby-dev
RUN gem install sinatra
```

这里其他命令都比较好理解，唯独 `CMD` 和 `ENTRYPOINT` 我需要特殊说明一下。`CMD` 命令可用指定 Docker 容器启动时默认的命令，例如我们上面例子提到的 `docker run -it ubuntu:latest sh -c '/bin/bash'`。其中 `sh -c '/bin/bash'` 就是通过手工指定传入的 CMD。如果我们不加这个参数，那么容器将会默认使用 CMD 指定的命令启动。ENTRYPOINT 是什么呢？从字面看是进入点。没错，它就是进入点。**ENTRYPOINT 用来指定特定的可执行文件、Shell 脚本，并把启动参数或 CMD 指定的默认值，当作附加参数传递给 ENTRYPOINT。**

不好理解是吧？我们举一个例子：

```shell
ENTRYPOINT ['/usr/bin/mysql']
CMD ['-h 192.168.100.128', '-p']
```

假设这个镜像内已经准备好了 mysql-client，那么通过这个镜像，不加任何额外参数启动容器，将会给我们一个 mysql 的控制台，默认连接到192.168.100.128 这个主机。然而我们也可以通过指定参数，来连接别的主机。但是不管无论如何，我们都无法启动一个除了 mysql 客户端以外的程序。因为这个容器的 ENTRYPOINT 就限定了我们只能在 mysql 这个客户端内做事情。这下是不是明白了~

因此，我们在使用 Dockerfile 创建文件的时候，可以创建一个 `entrypoint.sh` 脚本，作为系统入口。在这个文件里面，我们可以进行一些基础性的自举操作，比如检查环境变量，根据需要初始化数据库等等。下面两个文件是我在日常工作的项目中添加的 Dockerfile 和 entrypoint.sh，仅供参考：

- [https://github.com/starlight36/SimpleOA/blob/master/Dockerfile](https://github.com/starlight36/SimpleOA/blob/master/Dockerfile)

- [https://github.com/starlight36/SimpleOA/blob/master/docker-entrypoint.sh](https://github.com/starlight36/SimpleOA/blob/master/docker-entrypoint.sh)

在准备好 Dockerfile 之后，我们就可以创建镜像了：

```shell
docker build -t starlight36/simpleoa .
```

关于 Dockerfile 的更详细说明，请参考 [https://docs.docker.com/reference/builder/](https://docs.docker.com/reference/builder/)。

### 杂项和最佳实践

在产品构建的生命周期里使用 Docker，**最佳实践是把 Docker 集成到现有的构建发布流程里面**。这个过程并不复杂，可以在持续集成系统构建测试完成后，将打包的步骤改为 docker build，持续集成服务将会自动将构建相应的 Docker 镜像。打包完成后，可以由持续集成系统自动将镜像推送到 Docker Registry 中。生产服务器可以直接 Pull 最新版本的镜像，更新容器即可很快地实现更新上线。目前 Atlassian Bamboo 已经支持 Docker 的构建了。

由于 Docker 使用联合文件系统，所以并不用担心多次发布的版本会占用更多的磁盘资源，相同的镜像只存储一份。所以**最佳实践是在不同层次上构建Docker镜像**。比如应用服务器依赖于 PHP+Nginx 环境，那么可以把定制好的这个 PHP 环境作为一个镜像，应用服务器从这个镜像构建镜像。这样做的好处是，如果 PHP 环境要升级，更新了这个镜像后，重新构建应用镜像即可完成升级，而不需要每个应用项目分别升级 PHP 环境。

新手经常会有疑问的是关于 Docker 打包的粒度，比如 MySQL 要不要放在镜像中？**最佳实践是根据应用的规模和可预见的扩展性来确定 Docker 打包的粒度**。例如某小型项目管理系统使用 LAMP 环境，由于团队规模和使用人数并不会有太大的变化（可预计的团队规模范围是几人到几千人），数据库也不会承受无法承载的记录数（生命周期内可能一个表最多会有数十万条记录），并且客户最关心的是快速部署使用。那么这时候把 MySQL 作为依赖放在镜像里是一种不错的选择。当然如果你在为一个互联网产品打包，那最好就是把 MySQL 独立出来，因为 MySQL 很可能会单独做优化做集群等。

使用公有云构建发布运行 Docker 也是个不错的选择。**[DaoCloud](https://www.daocloud.io)提供了从构建到发布到运行的全生命周期服务**。特别适合像微擎这种微信公众平台、或者中小型企业 CRM 系统。上线周期更短，比使用 IaaS、PaaS 的云服务更具有优势。

**参考资料：**

* 深入理解 Docker Volume [http://dockone.io/article/128
](http://dockone.io/article/128)
* WordPress [https://registry.hub.docker.com/_/wordpress/](https://registry.hub.docker.com/_/wordpress/)
* Docker 学习——镜像导出 [http://www.sxt.cn/u/756/blog/5339](http://www.sxt.cn/u/756/blog/5339)
* Dockerfile Reference [https://docs.docker.com/reference/builder/
](https://docs.docker.com/reference/builder/)
* 关于 Dockerfile [http://blog.tankywoo.com/docker/2014/05/08/docker-2-dockerfile.html](http://blog.tankywoo.com/docker/2014/05/08/docker-2-dockerfile.html)

---

本文来自[刘思贤](http://starlight36.com/aboutme)的个人[博客](http://starlight36.com/post/startup-to-docker)， DaoCloud 在获得授权后将其转载。

博客原文：[Docker技术入门](http://starlight36.com/post/startup-to-docker)