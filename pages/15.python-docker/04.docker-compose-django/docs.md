---
title: '如何用 Docker Compose 配置 Django 应用开发环境'
---

<!-- reviewed by fiona -->

> 目标：搭建基于 Docker 的 Django 应用开发环境。
> 
> 本项目代码维护在 **[DaoCloud/python-django-sample](https://github.com/DaoCloud/python-django-sample)** 项目中。
>
> 您可以在 GitHub 找到本项目并获取本文中所提到的所有代码文件。

### 前言

工欲善其事，必先利其器。这次我们将使用：

- Docker >= 1.8.0
- Docker Machine >= 0.4.1
- Docker Compose >= 1.4.0

等工具，配置基于 Docker 的 Django 开发环境。

#### Docker

一款轻量级容器管理引擎，由 Docker Daemon、Docker Client 组成。

#### Docker Daemon

Docker 架构中常驻后台的系统进程，负责接收处理用户发送的请求和管理所有的 Docker 容器，所谓的**运行 Docker** 即代表**运行 Docker Daemon**。

#### Docker Client

Docker 架构中用户与 Docker Daemon 建立通信的客户端。

#### Docker Machine

Docker 官方提供的部署工具。帮助用户快速在运行环境中创建虚拟机服务节点，在虚拟机中安装并配置 Docker，最终帮助用户配置 Docker Client，使得 Docker Client 有能力与虚拟机中的 Docker 建立通信。

#### Docker Compose

Docker 官方提供的容器编配工具。随着服务的复杂度增长，容器管理过程的配置项将变得冗长，Compose 可有效帮助用户缓解甚至解决容器部署的复杂性。

#### 通过 Docker Machine 安装 Docker

> 如果您是 Windows 或 OS X 用户推荐阅读以下章节，将指导您使用 Docker Machine 安装与管理 Docker。

- 首先通过 `create` 命令创建一台名为 dev 的 VirtualBox 虚拟机，并已经安装好了 Docker。

```bash
$ docker-machine create -d virtualbox dev;
INFO[0000] Creating CA: /Users/dev/.docker/machine/certs/ca.pem
INFO[0000] Creating client certificate: /Users/dev/.docker/machine/certs/cert.pem
INFO[0001] Downloading boot2docker.iso to /Users/dev/.docker/machine/cache/boot2docker.iso...
INFO[0035] Creating SSH key...
INFO[0035] Creating VirtualBox VM...
INFO[0043] Starting VirtualBox VM...
INFO[0044] Waiting for VM to start...
INFO[0094] "dev" has been created and is now the active machine.
To point your Docker client at it, run this in your shell: $(docker-machine env dev)
```

> **提示**
>
> 由于 `create` 命令在初始化的时候，会从海外下载一个 ISO 镜像，由于国内网络不稳定，所以可能会在这一步耗费很长时间。
> 
> 我们可以通过以下办法进行加速。
> 
> **OS X**
> 
> ```bash
> $ mkdir ~/.boot2docker
> $ echo ISOURL = \"https://get.daocloud.io/boot2docker/boot2docker-lastest.iso\" > ~/.boot2docker/profile
> ```
> 
> **Win**
> 
> ```bash
> $ ISOURL = "https://get.daocloud.io/boot2docker/boot2docker-lastest.iso"
> ```

- 设置环境变量以将本机的 Docker Client 和 dev 上的 Docker Daemon 建立通信。

```bash
$ eval "$(docker-machine env dev)"
```

- 查看当前所有正在运行的 Machines

```bash
$ docker-machine ls
NAME   ACTIVE   DRIVER       STATE     URL
dev    *        virtualbox   Running   tcp://192.168.99.100:2376

```

- 启动 Machine(dev)

```bash
$ docker-machine start dev
Starting VM ...
```

- 获取 Machine(dev) 的 IP

```bash
$ docker-machine ip dev
192.168.99.100
```

- 通过 SSH 进入 Machine(dev)

```bash
$ docker-machine ssh dev
Starting VM ...
```

#### 通过 Docker Compose 编配应用

> 因所有官方镜像均位于境外服务器，为了确保所有示例能正常运行，示例中使用与官方镜像保持同步的 DaoCloud 境内镜像：

*docker-compose.yml*

```yaml
web:
  build: .
  ports:
    - "8000:8000"
  links:
    - mysql:mysql
    - redis:redis
  env_file: .env
  volume: . /code
  command: /code/manage.py runserver 0.0.0.0:8000

mysql:
  image: daocloud.io/mysql:latest
  environment:
    - MYSQL_DATABASE=django
    - MYSQL_ROOT_PASSWORD=mysql
  ports:
    - "3306:3306"

redis:
  image: daocloud.io/redis:latest
  ports:
    - "6379:6379"
```

在这个文件中。我们定义了 3 个 Docker 微服务 `web`、`mysql`、`redis`。

- 通过 `build/image` 为微服务指定了 Docker 镜像。
- 通过 `links` 为 `web` 关联 `mysql` 和 `redis` 服务。
- 通过 `ports` 指定该服务需要公开的端口。
- 通过 `command` 指定该服务启动时执行的命令（可覆盖 Dockerfile 里的声明）。
- 通过 `volume` 将源码挂载至服务中，保证代码实时更新至开发环境中。

现在万事俱备，该让我们使应用运行起来，构建镜像并运行服务：

```bash
$ docker-compose build
$ docker-compose up -d
```

别忘记要为项目初始化数据库：

```bash
$ docker-compose run web /usr/local/bin/python manage.py migrate
```

这样我们的 Demo 就可以通过浏览器来访问了

**！！！**如果是使用 Docker Machine 的读者，您需要用

```bash
$ docker-machine ip dev
```

获取容器实际运行环境的 IP，并访问 `<ip>:8000`。

对于 Docker 安装在本地 Linux 机器上的读者，则直接使用 `127.0.0.1:8000` 即可。不出意外的话，您应该可以看到如下页面：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/python-django-sample-pic.png)

#### 总结

- Docker Machine 安装 Docker
- Docker Compose 编排服务
- 通过 Volume 将代码挂载入容器
- 在开发状态下，容器只是单纯的运行环境
- 通过 `docker-compose run service xxx` 执行 `xxx` 指令
