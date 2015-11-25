---
title: '如何制作一个定制的 PHP 基础 Docker 镜像'
---

<!-- reviewed by fiona -->

> 目标：准备一个定制的 PHP 基础镜像。基础镜像，通常为含最小功能的系统镜像，之后的应用镜像都以此为基础。

> 本项目代码维护在 **[DaoCloud/php-apache-image](https://github.com/DaoCloud/php-apache-image)** 项目中。

### 制作基础镜像

- 选择 Ubuntu 官方的 14.04 版本为我们依赖的系统镜像。

```dockerfile
FROM ubuntu:trusty
```

> 因所有官方镜像均位于境外服务器，为了确保所有示例能正常运行，DaoCloud 提供了一套境内镜像源，并与官方源保持同步。如果使用 DaoCloud 的镜像源，则指向：`FROM daocloud.io/ubuntu:trusty`

- 设置镜像的维护者，相当于镜像的作者或发行方。

```dockerfile
MAINTAINER Captain Dao <support@daocloud.io>
```

- 用 RUN 命令调用 apt-get 包管理器安装 PHP 环境所依赖的程序包。

> 安装依赖包相对比较固定，因此该动作应该尽量提前，这样做有助于提高镜像层的复用率。

```dockerfile
RUN apt-get update \
    && apt-get -y install \
        curl \
        wget \
        apache2 \
        libapache2-mod-php5 \
        php5-mysql \
        php5-sqlite \
        php5-gd \
        php5-curl \
        php-pear \
        php-apc \
```

- 用 RUN 命令调用 Linux 命令对 Apache 服务和 PHP 参数进行配置。

```dockerfile
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf \
```

- 用 RUN 命令调用 mkdir 来准备一个干净的放置代码的目录。

```dockerfile
RUN mkdir -p /app && rm -rf /var/www/html && ln -s /app /var/www/html
```

- 将本地的代码添加到目录，并指定其为当前的工作目录。

```dockerfile
COPY . /app
WORKDIR /app
```

- 设置启动脚本的权限，指定暴露的容器内端口地址。

- 最后指定容器启动的进程。

```dockerfile
RUN chmod 755 ./start.sh
EXPOSE 80
CMD ["./start.sh"]
```

至此一个 PHP 的基础镜像制作完毕，你可以在本地运行 `docker build -t my-php-base .` 来构建出这个镜像并命名为 `my-php-base`。

> 由于网络环境的特殊情况，在本地运行 `docker build` 的时间会很长，并且有可能失败。推荐使用 **[DaoCloud 加速器](http://help.daocloud.io/intro/accelerator.html)** 和 DaoCloud 的云端 **[代码构建](http://help.daocloud.io/features/build-flows.html)** 功能。

### 完整的 Dockerfile

```dockerfile
# Ubuntu 14.04，Trusty Tahr（可靠的塔尔羊）发行版
FROM ubuntu:trusty

# 道客船长荣誉出品
MAINTAINER Captain Dao <support@daocloud.io>

# APT 自动安装 PHP 相关的依赖包，如需其他依赖包在此添加
RUN apt-get update \
    && apt-get -y install \
        curl \
        wget \
        apache2 \
        libapache2-mod-php5 \
        php5-mysql \
        php5-sqlite \
        php5-gd \
        php5-curl \
        php-pear \
        php-apc \

    # 用完包管理器后安排打扫卫生可以显著的减少镜像大小
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

    # 安装 Composer，此物是 PHP 用来管理依赖关系的工具
    # Laravel Symfony 等时髦的框架会依赖它
    && curl -sS https://getcomposer.org/installer \
        | php -- --install-dir=/usr/local/bin --filename=composer

# Apache 2 配置文件：/etc/apache2/apache2.conf
# 给 Apache 2 设置一个默认服务名，避免启动时给个提示让人紧张.
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf \

    # PHP 配置文件：/etc/php5/apache2/php.ini
    # 调整 PHP 处理 Request 里变量提交值的顺序，解析顺序从左到右，后解析新值覆盖旧值
    # 默认设定为 EGPCS（ENV/GET/POST/COOKIE/SERVER）
    && sed -i 's/variables_order.*/variables_order = "EGPCS"/g' \
        /etc/php5/apache2/php.ini

# 配置默认放置 App 的目录
RUN mkdir -p /app && rm -rf /var/www/html && ln -s /app /var/www/html
COPY . /app
WORKDIR /app
RUN chmod 755 ./start.sh

EXPOSE 80
CMD ["./start.sh"]
```