---
title: '如何开发一个 PHP + New Relic 的生产级 Docker 化应用'
---

<!-- reviewed by fiona -->

> 目标：我们将为之前创建的 **[PHP + MySQL](https://github.com/DaoCloud/php-apache-mysql-sample)** 应用配置由 **[New Relic](http://www.newrelic.com)** 提供的应用监控探针。

> 本项目代码维护在 **[DaoCloud/php-newrelic-sample](https://github.com/DaoCloud/php-newrelic-sample)** 项目中。

### 创建 PHP 应用容器

> 因所有官方镜像均位于境外服务器，为了确保所有示例能正常运行，DaoCloud 提供了一套境内镜像源，并与官方源保持同步。

#### 首先，选择官方的 PHP 镜像作为项目的基础镜像。

```dockerfile
FROM daocloud.io/php:5.6-apache
```

#### 接着，按照 New Relic 官方 PHP 安装教程，进行脚本的编写。

```dockerfile
# 安装 New Relic
RUN mkdir -p /etc/apt/sources.list.d \
    && echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' \
        >> /etc/apt/sources.list.d/newrelic.list \

    # 添加 New Relic APT 下载时用来验证的 GPG 公钥
    && curl -s https://download.newrelic.com/548C16BF.gpg \
        | apt-key add - \

    # 安装 New Relic PHP 代理
    && apt-get update \
    && apt-get install -y newrelic-php5 \
    && newrelic-install install \

    # 用完包管理器后安排打扫卫生可以显著的减少镜像大小
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```

 - `apt-get update` 下载从仓库的软件包列表并获取软件包版本信息。
 - `apt-get install -y newrelic-php5` 安装 New Relic PHP5 扩展。
 - Docker 镜像采用分层数据存储格式，镜像的大小等于所有层次大小的总和，所以我们应该尽量精简每次构建所产生镜像的大小。

#### 然后，修改 New Relic 配置文件。

```dockerfile
# 覆盖 New Relic 配置文件
RUN sed -i 's/"REPLACE_WITH_REAL_KEY"/\${NEW_RELIC_LICENSE_KEY}/g' \
    /usr/local/etc/php/conf.d/newrelic.ini
RUN sed -i 's/"PHP Application"/\${NEW_RELIC_APP_NAME}/g' \
    /usr/local/etc/php/conf.d/newrelic.ini
```

#### 主要将 `newrelic.appname` 和 `newrelic.license` 按照 DaoCloud 最佳实践通过环境变量的方式暴露出来。

至此，我们 New Relic 的配置全部完成了，将代码复制到指定目录，并执行构建镜像命令完成我们镜像构建的最后一步。

```dockerfile
# /var/www/html/ 为 Apache 目录
COPY src/ /var/www/html/
```

```docker build -t php-newrelic-image .```

### 启动 php-newrelic 容器（本地）

最后，我们将构建好的镜像运行起来

```bash
docker run \
    --name php-newrelic \
    -e NEW_RELIC_LICENSE_KEY=my-newrelic-license \
    -e NEW_RELIC_APP_NAME=my-app-name \
    -d \
    php-newrelic-image
```

- 使用 `--name` 参数，指定容器的名称。
- 使用 `-e` 参数，容器启动时会将环境变量注入到容器中。
- 使用 `-d` 参数，容器在启动时会进入后台运行。
- `php-newrelic-image` 是由我们上面的 `Dockerfile` 构建出来的镜像。

### 启动 php-newrelic 容器（云端）

比起本地创建，在云端创建会更简单。

1. 在 GitHub 上 Fork **[DaoCloud/php-newrelic-sample](https://github.com/DaoCloud/php-newrelic-sample)** 或者添加自己的代码仓库。
2. 注册成为 DaoCloud 用户。
3. 在 DaoCloud 「控制台」中选择「代码构建」。
4. 创建新项目，选择代码源，开始构建镜像。
5. 将构建的应用镜像部署在云端并指定 `NEW_RELIC_APP_NAME` 和 `NEW_RELIC_LICENSE_KEY` 环境变量。

**DaoCloud 使用图文介绍**

- 了解如何用 DaoCloud 进行代码构建：参考**[代码构建](http://help.daocloud.io/features/build-flows.html)**。
- 了解如何用 DaoCloud 进行持续集成：参考**[持续集成](http://help.daocloud.io/features/continuous-integration/index.html)**。
- 了解如何部署一个刚刚构建好的应用镜像：参考**[应用部署](http://help.daocloud.io/features/packages.html)**。

**[DaoCloud 使用视频介绍](http://7u2psl.com2.z0.glb.qiniucdn.com/daocloud_small.mp4)**

### NewRelic Dashboard 截图

![php-newrelic-sample](/content/images/2015/07/newrelic.png "newrelic")