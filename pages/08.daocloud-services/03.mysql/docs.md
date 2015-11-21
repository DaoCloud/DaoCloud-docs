---
title: '使用和管理 MySQL服务'
taxonomy:
    category:
        - docs
---

MySQL，有管理直接点击，PHPMyAdmin
Redis，无管理，现在无管理方案
MongoDB，MongoExpress，部署镜像，不支持登陆
InfluxDB，管理UI必须内网访问，用户不可见

<!--一个月后更新 -->

创建 MySQL 服务


使用 MySQL 服务


管理 MySQL 服务


MySQL 使用注意事项
－收费、备份、自有主机、等等


## 服务集成

大部分情况下应用的运行离不开各类后台服务，尤其是数据库。DaoCloud 服务集成功能目前提供 MongoDB、MySQL、Redis 和 InfluxDB 服务。

让我们配置一个常用的 MySQL 数据库来熟悉服务实例的创建和配置过程吧。

> 注意：服务集成目前不支持[自有主机](runtimes/README.md)，请将数据库服务以应用的方式部署到自有主机中。

### 配置步骤

第一步：在控制台点击「服务集成」。

![控制台：点击代码构建](/img/screenshots/features/services/dashboard.png)

---

第二步：在「Dao 服务」列表中选择「MySQL」图标。

![服务集成：准备创建新服务](/img/screenshots/features/services/services-index.png)

---

第三步：接下来点击「创建服务实例」。

![服务集成：MySQL 服务](/img/screenshots/features/services/mysql.png)

---

第四步：为服务实例指定「服务实例名称」，服务实例名称只能包含英文数字、下划线 `_`、小数点 `.`、和减号 `-`，并且不能与现有服务实例重名。

![服务集成：配置新服务](/img/screenshots/features/services/new.png)

---

第五步：选择配置：目前我们提供了从 50MB 到 100MB 不等的数据容量，可供绝大多数应用正常使用。

---

第六步：点击「创建」，DaoCloud 将在云平台为您部署相应的服务实例。

---

第七步：创建成功，进入服务实例页面。

![服务集成：服务创建成功](/img/screenshots/features/services/service-overview.png)

---

就这么简单，您的 MySQL 服务实例已经准备就绪可以和应用对接了。

### 查看服务清单

在「服务集成」页面中，点击「我的服务」即可列出服务清单。

![服务集成：服务列表](/img/screenshots/features/services/services-index-with-service.png)

在服务清单中点击服务实例名称，您可以进入项目的「概览」、「绑定的应用」和「设置」选项卡。

---

概览选项卡可以查看服务的参数：连接地址、实例名、用户和密码。

![「概览」选项卡](/img/screenshots/features/services/service-overview.png)

---

绑定的应用选项卡提供了绑定该服务实例的应用列表。

![「绑定的应用」选项卡](/img/screenshots/features/services/service-binding.png)

---

设置选项卡则允许用户删除服务实例。

![「设置」选项卡](/img/screenshots/features/services/service-settings.png)

### SaaS 服务

DaoCloud 服务市场还将陆续集成各类第三方 SaaS 化服务，目前已经提供 New Relic 服务（见下图）。

![](/img/screenshots/features/services/saas.png)

创建 New Relic 服务实例，输入 `APP_NAME` 和 `LICENSE_KEY` 后，将返回 `NEW_RELIC_APP_NAME` 和 `NEW_RELIC_LICENSE_KEY` 参数，用于和应用绑定。

DaoCloud 会很快增加更多实用的 SaaS 化服务，如果您有感兴趣的服务希望我们集成，请来信告知。

> 提示：请勿在这个环境中保存任何重要数据，请做必要的备份

### 下一步

至此，您已经掌握了如何在 DaoCloud 上创建和配置服务实例。

下面您可以：

* 了解如何部署一个应用镜像并绑定数据库服务：参考[应用部署](deployment.md)。



## 服务集成

大部分情况下应用的运行离不开各类后台服务，尤其是数据库。DaoCloud 服务集成功能目前提供 MongoDB、MySQL、Redis 和 InfluxDB 服务。

让我们配置一个常用的 MySQL 数据库来熟悉服务实例的创建和配置过程吧。

> 注意：服务集成目前不支持[自有主机](runtimes/README.md)，请将数据库服务以应用的方式部署到自有主机中。

### 配置步骤

第一步：在控制台点击「服务集成」。

![控制台：点击代码构建](/img/screenshots/features/services/dashboard.png)

---

第二步：在「Dao 服务」列表中选择「MySQL」图标。

![服务集成：准备创建新服务](/img/screenshots/features/services/services-index.png)

---

第三步：接下来点击「创建服务实例」。

![服务集成：MySQL 服务](/img/screenshots/features/services/mysql.png)

---

第四步：为服务实例指定「服务实例名称」，服务实例名称只能包含英文数字、下划线 `_`、小数点 `.`、和减号 `-`，并且不能与现有服务实例重名。

![服务集成：配置新服务](/img/screenshots/features/services/new.png)

---

第五步：选择配置：目前我们提供了从 50MB 到 100MB 不等的数据容量，可供绝大多数应用正常使用。

---

第六步：点击「创建」，DaoCloud 将在云平台为您部署相应的服务实例。

---

第七步：创建成功，进入服务实例页面。

![服务集成：服务创建成功](/img/screenshots/features/services/service-overview.png)

---

就这么简单，您的 MySQL 服务实例已经准备就绪可以和应用对接了。

### 查看服务清单

在「服务集成」页面中，点击「我的服务」即可列出服务清单。

![服务集成：服务列表](/img/screenshots/features/services/services-index-with-service.png)

在服务清单中点击服务实例名称，您可以进入项目的「概览」、「绑定的应用」和「设置」选项卡。

---

概览选项卡可以查看服务的参数：连接地址、实例名、用户和密码。

![「概览」选项卡](/img/screenshots/features/services/service-overview.png)

---

绑定的应用选项卡提供了绑定该服务实例的应用列表。

![「绑定的应用」选项卡](/img/screenshots/features/services/service-binding.png)

---

设置选项卡则允许用户删除服务实例。

![「设置」选项卡](/img/screenshots/features/services/service-settings.png)

### SaaS 服务

DaoCloud 服务市场还将陆续集成各类第三方 SaaS 化服务，目前已经提供 New Relic 服务（见下图）。

![](/img/screenshots/features/services/saas.png)

创建 New Relic 服务实例，输入 `APP_NAME` 和 `LICENSE_KEY` 后，将返回 `NEW_RELIC_APP_NAME` 和 `NEW_RELIC_LICENSE_KEY` 参数，用于和应用绑定。

DaoCloud 会很快增加更多实用的 SaaS 化服务，如果您有感兴趣的服务希望我们集成，请来信告知。

> 提示：请勿在这个环境中保存任何重要数据，请做必要的备份

### 下一步

至此，您已经掌握了如何在 DaoCloud 上创建和配置服务实例。

下面您可以：

* 了解如何部署一个应用镜像并绑定数据库服务：参考[应用部署](deployment.md)。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/phpmyadmin.png)

## phpMyAdmin 是什么？

**phpMyAdmin** 是使用 PHP 编写的，以网站的方式管理 MySQL 的数据库管理工具，让数据库管理员可以方便的管理 MySQL 数据库。

它具有两大优势：

1. phpMyAdmin 能够以简易的方式输入繁杂 SQL 语法，尤其是在处理大量数据的导入及导出时更为方便。

2. 由于 phpMyAdmin 与其他 PHP 程序一样在网页服务器上运行，您可以在任何地方使用这些程序产生的 HTML 页面，远程管理 MySQL 数据库，从而方便地创建、查询、修改、删除数据库与表。也可借由 phpMyAdmin 生成 PHP 语句，在编写 PHP 互联网应用时轻松插入 SQL 查询。

## 部署 phpMyAdmin？

首先保证存在一个或新建一个需要被管理的 MySQL 服务实例（如果已有 MySQL 服务实例，可跳过这个步骤）

在**镜像仓库**中选择 **phpMyAdmin**，点击「部署最新版本」。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/app-php-0.png)

部署时在**服务&环境**绑定 MySQL 服务，切记此处需要使用 `mysql` 作为连接字符串的别名，然后点击**立即部署**。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/app-php-1.png)


部署成功后打开应用的 URL，根据您的 MySQL 实例参数，在启动页面的填写相应的**用户名**和**密码**，您就可以开始管理 MySQL 数据库了。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/app-php-2.png)

![](http://blog.daocloud.io/wp-content/uploads/2015/05/app-php-3.png)