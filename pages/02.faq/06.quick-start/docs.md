---
title: 'DaoCloud 快速上手指南'
---

DaoCloud 提供一站式 Docker 容器化软件交付服务，为开发者带来 Code to Cloud 的自动化流程，提升了软件开发、构建、运维的效率。为了帮助您更好了解 DaoCloud 的产品结构和背后的设计理念，我们编写了「快速上手指南」这篇指南列出了使用 DaoCloud 的主要步骤，和一些关键的概念和核心功能。。

---

#### 关联代码库，开启 DaoCloud 之旅
![](Part1-01.png?resize=800)
正文：将代码仓库与云端的 DaoCloud 持续集成和镜像构建引擎完成对接后，即可一键触发全自动的容器化应用测试及发布流程。DaoCloud 支持包扩 GitHub、Bitbucket、Coding 和 GitCafe 在内的代码仓库，也支持与企业内部的私有 GitLab仓库对接。[立即关联代码仓库](https://dashboard.daocloud.io/build-flows/new)

#### 自动触发的持续集成
![](Part1-02.jpg?resize=800)
在代码发生变化时实现自动化触发的持续集成和镜像构建，是提升开发和交付效率的必要手段。DaoCloud 默认在代码仓库发生 commit 事件时触发持续集成测试，在对代码分支打 tag 事件发生时触发镜像构建操作。我们提供了一个例子，供您体验尝试。[体验自动化镜像构建](https://dashboard.daocloud.io/build-flows/new)

#### 代码库管理的最佳实践
在多人协作的开发场景下，代码库和开发分支的管理尤其重要，我们推荐用户采用 Gitflow 模型管理代码提交的工作流，Vincent Driessen的文章「[A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)」值得一读。

#### Dockerfile 的格式
![](Part2-01.png?resize=800)
我们认为，Docker 镜像将成为未来软件的交付标准，Dockerfile 是生成镜像的关键文件，每一位云时代的开发者都应该了解和学习 Dockerfile 的格式和最佳实践。Docker镜像可以通过「编译」得到，这里的「编译」是指一种构建行为，通过手动编写或者从 GitHub获取 Dockerfile 来构建一个镜像。可以把 Dockerfile 看成是一个脚本，这个脚本会在容器被构建时执行。一般在 Dockerfile 里面需要编写基础软件的安装脚本和配置脚本。[Dockerfile 的教程](../../ci-image-build/dockerfile)

#### 适用于各种编程语言的 Dockerfile
![](Part2-02.png)
DaoCloud 提供了一些预先编写好的 Dockerfile 模版和最佳实践，供用户快速上手。编写完 Dockerfile后，可以在安装了 Docker 引擎的机器上手工构建，也可以通过 DaoCloud 的持续交付引擎执行自动构建。您可以 fork 这些项目并在 DaoCloud 上测试构建和部署。[Dockerfile 模版](../../ci-on-daocloud/sample)

#### Dockerfile 的最佳实践
调整和优化 Dockerfile 中命令的顺序，可以降低 Docker 镜像的尺寸，提升加载速度。[酷推网站上有一篇译文](http://www.tuicool.com/articles/Yr2ema)，值得一读；另外，GitHub 也有很多[精彩的例子](https://github.com/kstaken/dockerfile-examples)。

#### 配置镜像构建
![](Part3-01.png?resize=800)
微服务架构的分布式应用，必须采用合适的自动化持续集成和测试工具。以流水线方式实现交付标准化、自动化是当前开发管理的一大趋势。关联代码仓库，并正确编写 Dockerfile 后，DaoCloud 会在每次项目代码的 master 分支发生 tag commit 时，完成镜像构建操作，您也可以手工构建其他代码分支。构建完成的镜像，会保存在镜像仓库中。这是实现自动化交付流水线的重要环节。[开始构建](https://dashboard.daocloud.io/build-flows)

#### 执行持续集成
![](Part3-02.png?resize=800)
DaoCloud 持续集成（CI）是我们自主研发的执行引擎，目前支持 Golang、Python、Ruby、Java、Javascript（NodeJS）、PHP、C（gcc） 等编程语言，和MySQL、Redis、MongoDB 等数据服务。持续集成会在您每次代码提交后执行，并通知您测试结果。[学习如何编写 daocloud.yml](../../ci-image-build/daocloud-yml)。

#### 什么是持续交付？
持续交付是以快速、高效、可靠的方式向用户交付新功能的原则和技术实践。通过实现自动化的构建、部署和测试过程，并改进开发人员、测试人员、运维人员之间的协作，交付团队可以在几小时（甚至几分钟）内发布软件变更，而这不受项目大小和代码复杂性的影响。《[持续交付](http://item.jd.com/1043529147.html)》一书对这个领域做了精彩的论述，值得一读。

---

#### 我的镜像
![](Part4-01.png?resize=800)
DaoCloud 镜像仓库汇聚了代码构建产生的私有容器镜像,也囊括了来自软件发行商和社区的优质产品镜像。玲琅满目，等您来探索！在持续集成环节自动化构建的镜像，都会被保存在「我的镜象」中。我们保证镜像的版本与代码 tag 版本一一对应，实现版本可追溯、发布可回滚。您可以使用 docker pull 和 push 命令下载或上传镜像。[访问我的镜像](https://dashboard.daocloud.io/packages)。

#### DaoCloud 镜像
![](Part4-02.png?resize=800)
DaoCloud 预制了大量常用镜像，有些可用在 daocloud.yml 中作为 CI 测试的基础镜像，有些可以实现数据库管理配置操作。我们还提供了 StarCraft 和 2048这类页面游戏镜像，[赶紧去看看吧](https://dashboard.daocloud.io/packages)！Docker Hub 是世界上最大最完整的容器镜像仓库，超过 10 万款各类应用。DaoCloud 在镜像仓库提供了访问 Docker Hub 的便捷入口，输入关键字即可搜索并高速下载。

#### Docker Hub 加速器升级版
![](Part5-01.png?resize=800)
DaoCloud Toolbox 由一系列 Linux 下的命令行工具和后台服务组成，是一款集成了 Docker Hub 下载加速、Docker 宿主机垃圾回收、混合式容器管理等多种功能于一身的工具软件。DaoCloud 在 2015 年年初推出的 Docker 加速器  提供 Docker Hub 镜像下载的加速功能，极大提升了国内网络访问 Docker Hub 的速度，拥有广泛的用户群体。DaoCloud 工具箱包含了 Docker 加速器的 v2.0 升级版，使用 dao pull 命令行工具下载 Docker Hub 镜像，可以获得类似迅雷、BT 一般的超高速下载体验。dao pull 可以完全替代 docker pull。[立即使用](../../faq/what-is-daocloud-accelerator)。

#### Docker 清道夫
![](Part5-02.png?resize=800)
随着Docker 的使用和容器被创建、销毁， Docker 宿主机上往往会产生各类「垃圾」。DaoCloud Toolbox 提供了Docker 清道夫工具，可以有效的识别各类破损镜像、无主Volume 等Docker 运行过程中的垃圾，并且完成安全的清除工作。[立即使用](../../faq/what-is-daocloud-accelerator)。

由于受到 Docker Registry 原理所限，使用了加速器 1.0，仍无法避免直接连接 Docker Hub 元数据服务器时链接缓慢甚至中断的问题。因此，我们又进一步推出了加速器 2.0，通过采用智能路由和缓存机制，结合Docker 1.8 最新技术，实现多路并行下载，使得国内网络拉取 Docker Hub 镜像的速度，较之加速器 1.0，又有了成倍的提升。

---

#### 在 DaoCloud 云平台部署应用
![](Part6-01.png?resize=800)
DaoCloud 云平台建立在国内外各大公有云之上，为容器化应用提供全生命周期的自动化运维能力，并在此基础上增加弹性扩容、性能监控、远程管理等高级功能。在镜像仓库选中应用，并点击「部署」按钮，提供容器配置、数据中心、端口选择、服务和 Volume绑定等简单信息，容器一键部署，应用秒级启动。您再也无需为底层资源、虚拟机、操作系统等配置劳神费心。[开始部署](https://dashboard.daocloud.io/packages)。

#### DaoCloud 云平台的高级功能
![](Part6-02.png?resize=800)
DaoCloud 云平台提供了弹性扩容、参数修改、性能监控、应用日志、修改事件、域名绑定、自动发布、容器远程登录、站点 SSL 加密等众多高级功能。[立刻体验](https://dashboard.daocloud.io/apps)。

Heroku 创始人Adam Wiggins曾发布“十二要素应用宣言（The Twelve-Factor App），为云端应用的开发和部署提出了指导性的建议，InfoQ 上有一篇[译文](http://www.infoq.com/cn/news/2012/09/12-factor-app)，推荐大家阅读。

#### 我的集群
![](Part7-01.png?resize=800)
混合式集群管理服务是 DaoCloud 的一项独创技术，使用「自有集群」功能，DaoCloud 用户可以通过一致的界面和流程，管理在公有云、私有云甚至是企业防火墙之后的各类物理和虚拟主机资源，把这些资源汇聚成跨云跨网的分布式主机集群资源池，实现容器化应用的高速部署和灵活调度。我们以集群为单位管理 DaoCloud 云平台和用户接入的各类主机，创建自有集群后，可以添加主机，部署应用，并实现应用在集群内和跨集群的调度迁移。[立即创建集群](https://dashboard.daocloud.io/cluster)。

#### 接入自有主机
![](Part7-02.png?resize=800)
DaoCloud支持包括所有公有云、私有云、物理机在内的主机类型，用户可采用自动或手动方式把主机接入 DaoCloud，接入过程不需要修改网络防火墙，并可立即享受 DaoCloud 工具箱带来的各类便利。[接入您的主机](https://dashboard.daocloud.io/cluster)。

使用自有集群功能，用户可将各类分散的资源汇聚在一起，如将开发工作站作为测试集群，内网服务器作为预发布集群，公有云虚拟机作为生产环境，实现测试发布环境的一站式管理，和各类测试交付部署的快速完成。

#### 向自有集群部署应用
![](Part8-01.png?resize=800)
引入自有集群为用户带来的巨大的便利性，享受 DaoCloud 带来的自动化交付和运维功能的同时，用户仍可以对主机享有全面控制，进行必要的资源优化和安全控制。在应用部署的界面，选择「我的主机」，系统会列出所有已经接入的主机，并引导您完成后续操作。自有集群提供更灵活的端口选择、容器权限、自动更新、故障恢复和跨集群迁移的高级功能。[开始部署](https://dashboard.daocloud.io/cluster)。

#### 部署复杂多节点容器应用
![](Part8-02.png?resize=800)
多容器的应用编排服务可以帮助您创建并管理新一代的可移植分布式应用程序，这些应用程序是由独立且互通的容器快速组合而成，他们有动态的生命周期，并且可以在任何地方以可扩展的方式运行。[了解应用编排细节](https://dashboard.daocloud.io/stack)。

微服务架构其实是一种软件架构的模式，在这种理念的指导下，传统应用在开发过程中，被解耦成许多微小的应用，变成小而专的应用。把系统拆分成小的系统之后，就简化了开发的流程，缩短了开发周期，提升了运维的效率。DaoCloud 为微服务架构应用的交付部署提供了全方位的支持，技术细节可[阅读此文](http://cloud.it168.com/a2015/1024/1771/000001771325.shtml)。

---

#### 使用服务集成
![](Part9-01.png?resize=800)
容器被设计为无状态实例，应用的运行和数据持久化，需要各类数据服务支持。DaoCloud 在平台层面集成了主流的数据库和文件服务，方便开发者直接使用。服务集成汇集了一系列来自于 DaoCloud 以及其他第三方SaaS提供商的热门应用服务，包括常用的 MongoDB、MySQL、Redis、InfluxDB等，创建服务后，可以在部署应用时，通过绑定的方式，与服务建立连接。[创建数据服务](https://dashboard.daocloud.io/services)。

#### 使用Volume
![](Part9-02.png?resize=800)
除了数据库，DaoCloud 提供了文件存储的 Volume 功能。可以在一个或者多个容器里共享，它绕过了容器内部的文件系统为持久化数据、共享数据提供了有用的特性：容器可以通过把数据写在 Volume 上来实现数据持久化，Volume 可以在不同的容器之间共享和重用数据，容器数据的备份、恢复和迁移都可以通过 Volume 实现。[创建和使用 Volume](https://dashboard.daocloud.io/stack)。

深入理解 Docker 和数据持久化：DaoCloud 团队撰写了一系列精彩文章，剖析 Docker 底层工作原理，分析日志、数据访问等细节，欢迎[访问阅读](../../allen-docker)。

---

#### 创建组织
![](Part10-01.png?resize=800)
DaoCloud 提供了「组织中心」功能，支持团队协作开发和应用交付管理。在DaoCloud用户中心，您可以创建组织，并邀请同事或项目协作者加入组织。组织内成员共享所有绑定的项目和容器镜像。[创建组织](https://dashboard.daocloud.io/settings/new-org)。

#### 绑定微信
![](Part10-02.png?resize=800)
DaoCloud 提供的丰富的用户交互和通知功能，其中大部分通过微信来完成。我们强烈建议您绑定微信账号，我们会为您提供额外的 DaoCloud 云平台资源。[立即绑定](https://dashboard.daocloud.io/settings/profile)。

DaoCloud 产品社区：Docker 是新兴的技术，为了降低您的学习门槛，我们为用户提供了丰富的技术文档和开发者指南，包括 PHP、Python 开发者文档、Docker 源码分析等精彩内容，[尽在 DaoCloud 产品社区](../../)。

#### 如何联系客服
![](Part11-02.png?resize=800)
DaoCloud 提供了丰富的技术支持手段，我们首选的技术支持方式，是在 DaoCloud 网站点击右下角的问号按钮，我们的「道客船长」客服团队会为您在第一时间答疑解惑。您也可以通过 [support@daocloud.io](mailto:support@daocloud.io)与我们联系。

---

#### 恭喜您！
至此，您已经了解了 DaoCloud 的主要功能模块，和我们的一些设计理念，现在，我们一起开始精彩的 DaoCloud 之旅吧！
