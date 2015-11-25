---
title: '如何开发一个 Laravel + MySQL 框架的 Docker 化应用'
---

<!-- reviewed by fiona -->

> 目标：基于主流的 PHP 框架，用 Docker 镜像的方式搭建一个 Laravel + MySQL 的应用。

> 本项目代码维护在 **[DaoCloud/php-laravel-mysql-sample](https://github.com/DaoCloud/php-laravel-mysql-sample)** 项目中。

### 创建 Laravel 应用容器

> 因所有官方镜像均位于境外服务器，为了确保所有示例能正常运行，DaoCloud 提供了一套境内镜像源，并与官方源保持同步。

#### 首先，选择官方的 PHP 镜像作为项目的基础镜像。

```dockerfile
FROM daocloud.io/php:5.6-apache
```

#### 其次，通过安装脚本安装 Laravel 应用所需要的 PHP 依赖。

```dockerfile
# 安装 PHP 相关的依赖包，如需其他依赖包在此添加
RUN apt-get update \
    && apt-get install -y \
        libmcrypt-dev \
        libz-dev \
        git \
        wget \

    # 官方 PHP 镜像内置命令，安装 PHP 依赖
    && docker-php-ext-install \
        mcrypt \
        mbstring \
        pdo_mysql \
        zip \


    # 用完包管理器后安排打扫卫生可以显著的减少镜像大小
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

    # 安装 Composer，此物是 PHP 用来管理依赖关系的工具
    && curl -sS https://getcomposer.org/installer \
        | php -- --install-dir=/usr/local/bin --filename=composer
```

- 依赖包通过 `docker-php-ext-install` 安装，如果依赖包需要配置参数则通过 `docker-php-ext-configure` 命令。
- Docker 镜像采用分层数据存储格式，镜像的大小等于所有层次大小的总和，所以我们应该尽量精简每次构建所产生的镜像的大小。
- Composer 为 Laravel 下载第三方 Vendor 包所必需的插件，Composer 同时也是 PHP 最流行的包管理工具。

#### 接着，创建 Laravel 目录结构：

```dockerfile
# 开启 URL 重写模块
# 配置默认放置 App 的目录
RUN a2enmod rewrite \
    && mkdir -p /app \
    && rm -fr /var/www/html \
    && ln -s /app/public /var/www/html

WORKDIR /app
```

- Laravel 是通过统一的项目的入口文件进入应用系统的，进而需要 Apache 开启链接重写模块。
- Apache 默认的文档目录为 `/var/www/html`，将 `/app` 定义为 Laravel 应用目录，而 Laravel 的项目入口文件位于 `/app/public`。为了方便管理，把 `/var/www/html` 软链接到 `/app/public`。

#### 紧接着，根据 DaoCloud 的最佳实践，我们需要把第三方依赖预先加载好。

```dockerfile
# 预先加载 Composer 包依赖，优化 Docker 构建镜像的速度
COPY ./composer.json /app/
COPY ./composer.lock /app/
RUN composer install  --no-autoloader --no-scripts
```

- 复制 `composer.json` 和 `composer.lock` 到 `/app`，`composer.lock` 会锁定 Composer 加载的依赖包版本号，防止由于第三方依赖包的版本不同导致的应用运行错误。
- `--no-autoloader` 为了阻止 `composer install` 之后进行的自动加载，防止由于代码不全导致的自动加载报错。
- `--no-scripts` 为了阻止 `composer install` 运行时 `composer.json` 所定义的脚本，同样是防止代码不全导致的加载错误问题。

#### 然后，将 Laravel 应用程序复制到 `/app`：

```dockerfile
# 复制代码到 App 目录
COPY . /app

# 执行 Composer 自动加载和相关脚本
# 修改目录权限
RUN composer install \
    && chown -R www-data:www-data /app \
    && chmod -R 0777 /app/storage
```

- `composer install` 执行之前阻止的操作，完成自动加载及脚本运行
- 修改 `/app` 与 `/app/storage` 的权限，保证 Laravel 在运行中有足够的权限
- 因为基础镜像内已经声明了暴露端口和启动命令，此处可以省略。

至此，包含 Laravel 应用的 Docker 容器已经准备好了。Laravel 代码中访问数据库所需的参数，是通过读取环境变量的方式声明的。

`config/database.php` 修改变量为更贴近 Docker 的方式：

```php
'host'      => env('MYSQL_PORT_3306_TCP_ADDR', 'localhost'),
'database'  => env('MYSQL_INSTANCE_NAME', 'forge'),
'username'  => env('MYSQL_USERNAME', 'forge'),
'password'  => env('MYSQL_PASSWORD', ''),
```

这样做是因为在 Docker 化应用开发的最佳实践中，通常将有状态的数据类服务放在另一个容器内运行，并通过容器特有的 `link` 机制将应用容器与数据容器动态的连接在一起。

### 绑定 MySQL 数据容器（本地）

- 首先，需要创建一个 MySQL 容器。

```bash
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d daocloud.io/mysql:5.5
```

- 之后，通过 Docker 容器间的 `link` 机制，便可将 MySQL 的默认端口 (3306) 暴露给应用容器。

```bash
docker run --name some-app --link some-mysql:mysql -d app-that-uses-mysql
```

### 绑定 MySQL 数据服务（云端）

比起本地创建，在云端创建和绑定 MySQL 数据服务会更简单。 

1. 在 GitHub 上 Fork **[DaoCloud/php-laravel-mysql-sample](https://github.com/DaoCloud/php-laravel-mysql-sample)** 或者添加自己的代码仓库。
2. 注册成为 DaoCloud 用户。
3. 在 DaoCloud 「控制台」中选择「代码构建」。
4. 创建新项目，选择代码源，开始构建镜像。
5. 在「服务集成」创建 MySQL 服务实例。
6. 将构建的应用镜像关联 MySQL 服务实例并部署在云端。

**DaoCloud 使用图文介绍**

- 了解如何用 DaoCloud 进行代码构建：参考**[代码构建](http://help.daocloud.io/features/build-flows.html)**。
- 了解如何用 DaoCloud 进行持续集成：参考**[持续集成](http://help.daocloud.io/features/continuous-integration/index.html)**。
- 了解如何用为应用准备一个数据库服务：参考**[服务集成](http://help.daocloud.io/features/services.html)**。
- 了解如何部署一个刚刚构建好的应用镜像：参考**[应用部署](http://help.daocloud.io/features/packages.html)**。

**[DaoCloud 使用视频介绍](http://7u2psl.com2.z0.glb.qiniucdn.com/daocloud_small.mp4)**

### php-laravel-mysql-sample 应用截图

![php-laravel-mysql-sample](/content/images/2015/07/php-laravel-mysql-sample.png "php-laravel-mysql")