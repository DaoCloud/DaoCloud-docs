---
title: 从云端测试环境迁移到自有主机
---

自有主机功能提供将您的主机接入 DaoCloud 的功能。您可以通过 DaoCloud 来统一管理不同平台的大量主机，并无缝享受持续集成、持续发布等服务。

本篇文档演示如何将应用迁移到自有主机。[了解集群和自有主机](http://docs-static.daocloud.io/cluster-mgmt/what-is-cluster#-1)

文档包含以下三个部分，如迁移遇到困难请至 [DaoCloud Services](https://dashboard.daocloud.io) 页面点击右下角联系客服
* [迁移应用到自有主机](http://docs-static.daocloud.io/faq/migrate-from-cloud-limited-env-to-your-own-host#-1)
* [从云端 Mysql 导出数据](http://docs-static.daocloud.io/faq/migrate-from-cloud-limited-env-to-your-own-host#mysql)
* [从云端 Volume 导出数据](http://docs-static.daocloud.io/faq/migrate-from-cloud-limited-env-to-your-own-host#volume)
 
##### 准备您的自有主机
请先准备一台用于生产环境的主机
请根据以下步骤接入主机到 DaoCloud：

### 迁移应用到自有主机

准备一台可以连接互联网的装有Linux系统的主机，然后进行添加主机动作。

![](1-添加主机.png)

![](2-接入主机.png)

如果主机没有安装Docker，则需要在命令行里复制以下代码：

![](3-接入自有主机.png)

然后安装Monit程序：

![](4-接入自由主机.png)

安装完成后，接入成功：

![](5-接入成功.png)

![](6-接入成功.png)

点击跳转，进入主机页面：

![](7-接入成功.png)

连接成功后：

![](8-接入成功.png)

### 迁移应用

查看您的应用列表：

![](9-应用列表.png)

选择您需要迁移的应用，点击所属镜像：

![](10-镜像.png)

然后点击右上角的部署：

![](11-部署.png)

创建应用的时候选择我的主机：

![](11-创建应用.png)

![](12-选择主机.png)

配置好基础设置：

![](13-基础设置.png)

运行成功：

![](14-运行成功.png)

##### 导出云端 Mysql 的数据：
在服务集成页面，选择“我的服务”，并选择一个数据库：

![](1-选择数据库.png)

点击“管理Mysql”：

![](2-管理数据库.png)

然后选择导出数据库：

![](3-导出数据库.png)

点击执行，即可将sql文件导出到本地：

![](4-导出.png)

##### 导出云端 Volume 的数据：

打开Volume页面：

![](1-volume.png)

选择要备份的Volume：

![](2-我的Volume.png)

点击管理Volume：

![](3-管理Volume.png)

然后选择您需要备份的文件：

![](4-列出文件.png)

在文件上右键，下载文件：

![](5-右键下载.png)

或者多项选择文件，右键下载：

![](6-下载全部.png)