---
title: 'DaoCloud ToolBox'
taxonomy:
    category:
        - docs
---

#### DaoCloud Toolbox 是什么？

DaoCloud Toolbox 由一系列 Linux 下的命令行工具和后台服务组成，是一款集成了 Docker Hub 下载加速、Docker 宿主垃圾回收、混合式容器管理等多种功能于一身的工具软件。


##### 工具一：Docker 清道夫

随着 Docker 的使用和容器被创建、销毁， Docker 宿主机上往往会产生各类「垃圾」。DaoCloud Toolbox 提供了Docker 清道夫工具，可以有效地识别各类破损镜像、无主 Volume 等 Docker 运行过程中的垃圾，并且完成安全的清除工作。

1. 运行 sudo dao clean，即可完成宿主机上的垃圾清理工作。
2. 为了避免误删除，dao clean 命令还支持「试运行」功能，使用 –d 参数，可以列出所有已经被识别的垃圾，由用户决定是否需要清理。


##### 工具二：DaoCloud 自有主机管理

接入自有主机到 DaoCloud 平台是一项我们推出已久的功能，这次发布 DaoCloud Toolbox，我们决定把自有主机的宿主机监控 Agent 集成进入 DaoCloud Toolbox。

自有主机管理服务是 DaoCloud 的一项独创技术，使用这项功能，DaoCloud 用户可以通过一致的界面和流程，管理在公有云、私有云甚至是企业防火墙之后的各类物理和虚拟主机资源，把这些资源汇聚成跨云跨网的分布式容器主机资源池，实现容器化应用的高速部署和灵活调度。

##### DaoCloud Toolbox 使用指南

** DaoCloud Toolbox 如何试用？** 

请登录 DaoCloud 控制台，依次点击「我的主机」、「添加新主机」。点击「免费胶囊主机」，请根据提示，执行我们提供的安装命令。

备注：免费胶囊主机，是客户无需预付款，即可获得的容器主机，每天我们会通过合理计算调度，从数据中心节点中腾挪出闲散的计算资源组成「胶囊集群」。每台「胶囊主机」自带 Docker 运行环境，并自动接入 DaoCloud 容器管理平台。每颗「胶囊」的生命目前是 120 分钟，到期后会自动消失。装载到「胶囊」里的应用信息会保留并自动迁移。「胶囊主机」到期后可以重复创建。

** DaoCloud Toolbox 如何安装？** 

1. 请登录 DaoCloud 控制台，依次点击「我的主机」、「添加新主机」。
2. 请根据提示，在需要安装 DaoCloud Toolbox 的主机终端，执行我们提供的安装命令。
3. 安装完成后，可以在主机终端执行 `sudo dao –version`，验证安装成功与否。
4. 您也可以在 DaoCloud 控制台的「我的主机」界面，看到刚才完成安装的主机信息。您可以在 DaoCloud 控制台，管理这台主机，具体方法，可以参考我们的帮助文档。

** 使用DaoCloud Toolbox 对 Docker 客户端有什么要求？** 

DaoCloud Toolbox 中的 dao 命令，会调用本机 Docker 客户端的 API，来完成各类操作。DaoCloud Toolbox 支持包括最新 Docker 1.8 在内的各个版本 Docker 客户端。

** 是否支持 Boot2Docker、Kitematic？** 

支持。安装时，请确保Boot2Docker、Kitematic 已经正确配置，Docker 客户端已经安装并且运行正常。

** DaoCloud 加速器是否提供离线安装版？** 

DaoCloud 加速器整合了宿主机工具包和自有主机监控管理，需要与用户的 DaoCloud ID 绑定，目前我们不提供离线单独安装的版本。

** DaoCloud Toolbox 今后会提供什么工具？** 

我们将不断扩充 DaoCloud Toolbox，并且会考虑接纳各类第三方开发的工具。如果您有好的想法，欢迎与我们联系，请发送邮件到 [support@daocloud.io](mailto:support@daocloud.io)。
