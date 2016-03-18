---
title: '如何开发一个 PHP 的 Docker 化应用'
---

<!-- reviewed by fiona -->

> 目标：基于 PHP 的 Docker 基础镜像，开发一个 Docker 化的示例 PHP 应用 。

> 本项目代码维护在 **[DaoCloud/php-sample](https://github.com/DaoCloud/php-sample)** 项目中。

### Docker 化应用的关键元素
- 镜像是 Docker 应用的静态表示，是应用的交付件，镜像中包含了应用运行所需的所有依赖，包括应用代码、应用依赖库、应用运行时和操作系统。
- Dockerfile 是一个描述文件，描述了产生 Docker 镜像的过程。详细文档请参见 [Dockerfile文档](https://docs.docker.com/reference/builder/)
- 容器是镜像运行时的动态表示，如果把镜像想象为一个 Class 那么容器就是这个 Class 的 instance 实例。

一个应用 Docker 化的第一步就是通过 Dockerfile 产生应用镜像。

### 编写 Dockerfile

> 本次基础镜像使用 PHP 官方镜像，也可以根据自己的项目需求与环境依赖使用 [定制的 PHP 基础镜像](http://open.daocloud.io/ru-he-zhi-zuo-yi-ge-ding-zhi-de-php-ji-chu-docker-jing-xiang/)。

> 因所有官方镜像均位于境外服务器，为了确保所有示例能正常运行，DaoCloud 提供了一套境内镜像源，并与官方源保持同步。

官方镜像维护了自 5.4 版本起的所有 PHP 基础镜像，所有镜像均采用 `debian:jessie` 作为系统镜像。

- 首先，选择官方的 `php:5.6-cli` 镜像作为项目的基础镜像。

```dockerfile
FROM daocloud.io/php:5.6-cli
```

由于该示例代码较为简单，我们采用仅安装 PHP CLI 的 Docker 镜像来运行。

- 接着，将代码复制到目标目录。

```dockerfile
COPY . /app
WORKDIR /app
CMD [ "php", "./hello.php" ]
```

`ADD` 与 `COPY` 的区别，总体来说 `ADD` 和 `COPY` 都是添加文件的操作，其中 `ADD` 比 `COPY` 功能更多，`ADD` 允许后面的参数为 URL，还有 `ADD` 添加的文件为压缩包的话，它将自动解压。

`CMD` 为本次构建出来的镜像运行起来时候默认执行的命令，我们可以通过 `docker run` 的启动命令修改默认运行命令。

Dockerfile 具体语法请参考：**[Dockerfile](https://docs.docker.com/reference/builder/)**。

有了 Dockerfile 以后，我们可以运行下面的命令构建 PHP 应用镜像并命名为 `my-php-app`：

`docker build -t my-php-app .`

- 最后，让我们从镜像启动容器：

`docker run my-php-app`

```nohighlight
Welcome the world of Docker !
```

如果看到这段字符串，那么就说明你成功进入到了一个 Docker 化的世界。

欢迎来到 Docker 的世界，这个世界有你意想不到的精彩！
