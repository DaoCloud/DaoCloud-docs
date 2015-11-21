---
title: 写给开发者的例子
markdown:
    extra: true
gravui:
    enabled: true
    tabs: true
taxonomy:
    category:
        - docs
process:
    twig: true
---

<!--这篇也不需要修改了-->


#### 基础示例

为了帮助开发者快速上手，体验 Docker 和 DaoCloud 带来的便利性，我们针对各种开发语言和后台服务，编写了大量的示例程序，这些程序包含了基本的代码、数据库访问、Dockerfile和用于在 DaoCloud 平台上使用持续集成的 daocloud.yml 文件。在这些示例的基础上，您可以快速为您的项目添加 Dockerfile 和 daocloud.yml。DaoCloud 在 GitHub 的公有仓库分享了所有这些示例程序，我们为您列表如下：

##### 基础开发环境
+ Python ＋ Iphthon 开发环境，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/python-ipython-notebook) 
+ Python 开发环境，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/python-sample-base-image)  
+ Diango 开发环境，包括 Dockerfile 和 compose 文件，[Fork 项目 ](https://github.com/DaoCloud/python-django-sample)
+ Diango 开发环境和持续集成，包括 Dockerfile、compose 文件和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/python-django-cd-sample)
+ PHP 开发环境，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/php-sample) 
+ PHP ＋ Apache 基础运行环境，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/php-apache-image) 

##### 基础数据服务和工具
+ PHPMyAdmin 数据库管理工具，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/phpmyadmin/blob/master/Dockerfile) 
+ Mongo Express 数据库管理工具，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/dao-mongo-express) 
+ Tomcat 服务器，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/dao-tomcat)
+ Redis 服务器，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/dao-redis)
+ MySQL 服务器，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/dao-mysql)
+ MongoDB 服务器，包括 Dockerfile，[Fork 项目](https://github.com/DaoCloud/dao-mongodb)

##### 包含数据访问、性能监控或持续集成测试用例的复杂应用
+ Python ＋ MySQL，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/python-mysql-sample) 
+ Golang ＋ Mongo，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/golang-mongo-sample) 
+ Golang ＋ MySQL，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/golang-mysql-sample) 
+ Golang ＋ Redis，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/golang-redis-sample) 
+ PHP ＋ Laravel ＋ MySQL 示例项目，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/php-laravel-mysql-sample) 
+ PHP ＋ Apache ＋ MySQL 运行环境，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/php-apache-mysql-sample)
+ PHP ＋ Newrelic 监控，包括代码和Dockerfile，[Fork 项目](https://github.com/DaoCloud/php-newrelic-sample)
+ PHP ＋ 透视包监控，包括代码和Dockerfile，[Fork 项目](https://github.com/DaoCloud/php-toushibao-sample)
+ NodeJS ＋ MongoDB 开发示例，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/node-mongo-sample)
+ Golang ＋ InfluxDB 开发示例，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/golang-influxdb-sample)
+ Ruby ＋ MySQL 开发示例，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/ruby-mysql-sample)
+ Python ＋ Redis 开发示例，包括代码、Dockerfile 和 daocloud.yml CI 配置文件，[Fork 项目](https://github.com/DaoCloud/python-redis-sample)

##### 其他
+ 2048 页面游戏，包括代码和 Dockerfile，[Fork 项目 ](https://github.com/DaoCloud/dao-2048)

>>>>> 提示：有关 Dockerfile 和 daocloud.yml 的详细介绍，请您阅读[自动化持续集成和镜像构建](../../ci-image-build)这一部分的帮助文档。

---

#### 开发者的 Docker 之旅

在这部分的帮助文档中，我们将会针对不同的编程语言和框架详细介绍使用 Docker 和部署到 DaoCloud 上的最佳实践。

包括：
+ PHP 开发者的 Docker 之旅
+ Python 开发者的 Docker 之旅
+ 前端开发者的 Docker 之旅

>>>>> 提示：我们将在未来逐步添加 Go、Java、Ruby 等编程语言。

##### PHP 开发者的 Docker 之旅

欢迎进入「PHP 应用 Docker 开发大礼包 - Powered by DaoCloud」，六篇由浅入深、精心设计的系列文章，带领 PHP 开发者领略 Docker 化应用开发和发布的全新体验。

* [PHP 开发者的 Docker 之旅-开篇](../../php-docker/php-docker)
* [如何制作一个定制的 PHP 基础 Docker 镜像（一）](../../php-docker/php-docker-001)
* [如何开发一个 PHP 的 Docker 化应用（二）](../../php-docker/php-docker-002)
* [如何开发一个 PHP + MySQL 的 Docker 化应用（三）](../../php-docker/php-mysql-docker-003)
* [如何配置一个 Docker 化持续集成的 PHP 开发环境（四）](../../php-docker/docker-php-ci)
* [如何开发一个 PHP + NewRelic 的生产级 Docker 化应用（五）](../../php-docker/php-newrelic-docker-05)
* [如何开发一个 Laravel + MySQL 框架的 Docker 化应用（六）](../../php-docker/laravel-mysql-docker-06)

##### Python 开发者的 Docker 之旅

「人生苦短，我用 Python」，四篇由浅入深、精心设计的系列文章，将带领 Python 开发者领略 Docker 化应用开发和发布的全新体验。


* [Python 开发者的 Docker 之旅－开篇](../../python-docker/python-docker)
* [如何开发一个基于 Docker 的 Python 应用（一）](../../python-docker/docker-python-001)
* [如何制作一个定制的 Python 基础 Docker 镜像（二）](../../python-docker/python-docker-002)
* [如何用 Docker Compose 配置 Django 应用开发环境（三）](../../python-docker/docker-compose-django)
* [如何构建具有持续交付能力的 Docker 化 Django 应用（四）](../../python-docker/docker-django)

##### 前端开发者的 Docker 之旅

* [前端开发者的 Docker 之旅－开篇](../../docker-frontend/docker-frontend-open)
* [运维也学学前端，那天下就太平了](../../docker-frontend/frontend-docker-together)
* [Hello Docker](../../docker-frontend/hello-docker)
* [Docker 和 Node Express 应用](../../docker-frontend/docker-node-express)
* [用 Docker 搭建 Angular 前端应用](../../docker-frontend/docker-angular)
* [Angular 应用根据环境变量切换不同的后端 API](../../docker-frontend/angular-api)
* [Angular 应用根据环境变量切换不同的 CDN](../../docker-frontend/angular-cdn)
* [Angular 应用 Docker 启动加速](../../docker-frontend/angular-docker)
* [终极 Docker 构建调试 DaoCloud](../../docker-frontend/docker-daocloud)


---
#### 扩展阅读

您如果有好的 Docker 学习资料推荐，欢迎给我们的文档提 pull request。