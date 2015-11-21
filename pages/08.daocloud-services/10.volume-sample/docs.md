---
title: '使用 MySQL 和 Volume 创建 Ghost 博客'
taxonomy:
    category:
        - docs
---

![](http://blog.daocloud.io/wp-content/uploads/2015/05/ghost.png)

## Ghost 博客是什么？

还在用 WordPress 做您的博客站点？您 OUT 了！速度切换到 Ghost，用 Markdown 写出最有逼格的技术博客吧。这个出自于 WordPress 前 UX 部门开发者/设计师 John O’Nolan 之手的博客系统，自 2012 年诞生之日起就被冠于类似「WordPress 杀手」、「博客的新纪元」、「年度最令人兴奋的博客体系」之类的头衔。

关于 WordPress 和 Ghost 的比较大家可以参见 **[WordPress VS Ghost](http://www.elegantthemes.com/blog/resources/wordpress-vs-ghost)**（英文版）

动心了吗？马上用一分钟在 DaoCloud 上部署一个属于自己的高逼格 Ghost 博客吧！

## 如何部署 Ghost 博客？

> 提示：Ghost 博客需要绑定 MySQL 数据库，请参考帮助文档「产品功能」中的「服务集成」。
> 注意：在创建 Ghost 博客之前，请在控制台的「服务集成」中创建 MySQL 数据库实例，Ghost 博客与数据库的绑定，需要使用 `mysql` 作为连接字符串的别名。

在**镜像仓库**中选择 **Ghost Blog**，点击「部署最新版本」。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/app-ghost-2.png)

部署时在**服务&环境**绑定 MySQL 服务，切记此处需要使用 `mysql` 作为连接字符串的别名，然后点击**立即部署**。

部署成功后打开应用的 URL，您就可以使用酷炫的 Ghost 博客系统开始您的博客之旅了！

![](http://blog.daocloud.io/wp-content/uploads/2015/05/app-ghost.png)