---
title: 'Docker 监控'
taxonomy:
    category:
        - docs
process:
    twig: true
---

<!-- reviewed by fiona -->

>>>>> APM 厂商「云智慧」是 DaoCloud 的合作伙伴，云智慧提供了用于 Docker 监控的产品，可用于 DaoCloud 上部署的应用，以下内容由云智慧公司提供。

---


## Docker 监控

2015年9月7日，中国 APM 厂商云智慧（CloudWise）正式发布上线 Docker 监控。产品从部署到使用，整个过程都非常的简单。

Docker 监控不仅能够实时监控宿主机和 Docker 容器的性能信息（包括 CPU、Mem、磁盘、NetIn/out），还可以自定义响应的告警策略。

以下主要介绍 Docker 监控的**技术原理**、**部署**、**监控信息**、**告警信息**这几个方面。

### Docker 监控的技术原理

云智慧在 APM 领域率先提出了端到端的一体化监控模型，并且在此模型上，发布了技术领先、便于部署和管理的 SmartAgent 软件架构。此次 Docker 监控的实现，也是基于 SmartAgent 的架构来完成的。

SmartAgent 以部署的快捷高效和智能化见长。整个部署过程，用户在两分钟内便可完成。Docker 监控部署需要两个控件：

- SendProxy：数据发送代理，提供一个高效的本地数据接收队列与数据发送引擎，并且可以在局域网部署，使得不能上网的机器监控也可以正常地通过 SendProxy 高效的传输到云智慧的 SaaS 平台。

- DockerAgent：遵循了 SmartAgent 的插件规范，用户可以直接使用。DockerAgent 有三个线程，分别是DockerProcess、DockerConfig、DockerPing，以及一个对象 Task。三个线程各司其职，同时受 Task 对象控制。Task 的核心属性是任务唯一标识、任务状态以及任务频率。这些属性由 Dockerconfig 与 CloudWise 云平台定时同步。

当任务正常状态正常运行时，DockerProcess 线程开始采集数据，并遵守频率规范。DockerPing 负责心跳检测，定时产生心跳数据。这些数据都由 DockerAgent 交给 SendProxy，再由 SendProxy 存储进入队列，并异步地推送至 CloudWise 平台。

### 部署

请到 http://www.jiankongbao.com 注册试用云智慧的 Docker 监控服务。

**第一步**：进入云智慧监控宝管理中心，选择监控，选择 Docker 监控，点击「创建监控项目」，输入基本信息，包括名称和监控频率后，就可以看到具体的部署步骤。

进入云智慧监控宝平台管理中心
![](http://i.imgur.com/jQNW3u3.png)

选择监控，选择 Docker 监控，选择「创建监控项目」

![](http://i.imgur.com/KnfB2HL.png)

输入基本信息，然后保存后就可以看到插件使用说明

![](http://i.imgur.com/vPOvD4E.png)

插件使用说明

![](http://i.imgur.com/6Y1dxBP.png)

**第二步：**在监控机器上安装代理 SendProxy 和 Docker 插件

首先下载、解压和启动。

```
1. 安装SendProxy
    首先下载 SendProxy：【下载】
	解压zip后，执行以下命令启动SendProxy:
	chmod u+x SendProxy.sh
	./SendProxy.sh start

2. 安装Docker插件
    下载Docker插件zip包 : 【下载】
	解压后执行以下命令:
	chmod u+x start.sh
	chmod u+x stop.sh
	chmod u+x status.sh
	接下来就可以启动插件了：
	./start.sh(运行插件)
	./stop.sh (停止插件)
	./status.sh(查看插件运行状态)
```

经过这两步的操作，在云智慧监控宝的 Docker 监控页面就可以看到，刚刚创建的监控项目已经获取到了监控机器上的数据了。

不知道大家有没有疑问，「数据是怎么定位到刚刚创建的监控项目？」，创建监控项目时，输入的名称和设定的监控频率在保存监控项目后，将监控项目信息写入了 Docker Agent 的配置文件中。

### 监控信息

**一、**部署完成后，可以进入具体的信息展示页面:
![](http://i.imgur.com/KHmJdSP.png)

**二、**选中我们监控的宿主服务器，可以查看相关 Docker 信息

![](http://i.imgur.com/yUqQnFI.png)

**三、**详细信息包含**容器总数、容器总 CPU 占用量、容器总 Mem 占用量、容器总磁盘占用量、容器总 Net In/Out 占用量**，详细信息都有图标展示：

1. 容器总数：状态分为：总共、暂停、销毁、运行中
![](http://i.imgur.com/SrrUUWl.png)
2. 容器总 CPU 占用量
![](http://i.imgur.com/yLlEXeU.png)
3. 容器总 Mem 占用量
![](http://i.imgur.com/7iZUZkw.png)
4. 容器总磁盘占用量
![](http://i.imgur.com/1Oa8vkX.png)
5. 容器总 Net In/Out 占用量
![](http://i.imgur.com/LgNZ0zV.png)

### 告警信息

告警功能，无疑是运维人员和开发者最重视的一个功能。在云智慧监控宝的 Docker 监控中，用户可以自定义告警设置。告警对象主要是针对容器的资源使用情况以及容器的存活率。

告警策略：根据统计数据（平均值、和值）进行相应阈值的设定，高于、低于或者等于设定的阈值时进行告警。对于资源的使用情况，可以针对所有容器或者单个容器进行告警设置。

添加自定义告警线：
![](http://i.imgur.com/NzuMvcR.png)

监控宝的告警方式非常全面，可以通过电子邮件、手机短信、电话语音、APP 推送、微信等方式进行通知。

告警通知方式：
![](http://i.imgur.com/FkmMukx.png)

若触发了告警指标，则会自动的发送告警通知。

## 其他

Docker监控只是云智慧监控宝的一个功能模块，监控宝还支持网站监控、服务器监控、相关服务监控（Apache、nginx、tomcat、Oracle、MySQL、SQL Server、MongoDB、Redis、Memcache、Lighttpd、IIS 等）、业务流程（API）监控和页面性能监控管理等。
![](http://i.imgur.com/zGzeBg5.png)


### 联系我们

![](http://i.imgur.com/RiIfLW1.png)
