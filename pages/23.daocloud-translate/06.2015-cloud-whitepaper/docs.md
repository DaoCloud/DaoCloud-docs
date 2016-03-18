---
title: 译见｜2015年度云之白皮书：业界里程碑回顾与未来展望
---

<!-- reviewed by fiona -->

> 译见系列｜DaoCloud 现推出「译见」系列，每周为开发者提供国外精品译文，主要关注云计算领域的技术和前沿趋势。本系列由 Fiona 翻译。

#### 译者注

Adrian 作为业界领袖，对于云计算有着深刻观察和敏锐的判断。在 2014 年 Gigaom 举办的 Structure 大会，他进行了如下预测：IaaS 爆发式增长； AWS 和 Azure 不断加大投入，巨头间「圈地运动”方兴未艾；Docker 横空出世，掀起颠覆热潮；Openstack 生态日渐成熟；Go 语言成开发者新宠。展望未来，他认为 Docker 将成为标准的生产工具，并且为大量企业使用；数据中心会交叉使用 AWS 、 Azure 和 Google Cloud 的功能；精品级的、高安全系统将会使用云计算来构建。

#### 作者简介

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-1.jpg)

Adrian Cockcroft ，硅谷老牌风投机构 Battery Vetures 的技术专家。在此之前是著名流媒体服务商 Netflix 的云平台架构师，领导了 Netflix 向高扩展、高可用的公有云平台架构的迁移，开源了云原生的 NetflixOSS 平台。他也是 eBay Research Labs 的创始成员之一。作为 Sun Microsystems 杰出工程师，他著有畅销的《Sun Performance and Tuning》一书，也是高性能技术计算部门的首席架构师。

Adrian Cockcroft 毕业于伦敦城市大学，获应用物理和电子学学位，分别于 2011 年和 2012 年两次被 SearchCloudComputing 杂志提名为年度云计算领导者。

---


在 2014 年 6 月，我在 Gigaom 举办的 Structure 大会上进行了题为「云计算趋势」的演讲，阐述了当时云计算行业的态势。在那次演讲中，我在展现云计算生态系统的现状的同时，也预测产业界在今后几年的发展。现在一年过去了，我将重新审视去年的诸多观点。同时鉴于云计算仍在加速创新，我也将提出一些新的展望。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-2.jpg)

鉴于创新的科技公司多年来一直使用云计算来支持公司的 IT 基础设施，因此我预测在 2014 年企业会大规模使用公有云，金融服务这样的传统行业会谨慎而严肃地转向公有云。在去年 10 月，Gartner 的云计算分析师 Lydia Leong 也在推文中肯定了这一趋势：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-3.png)

> 一年之间，差异几何？我的 #GartnerSYM 1：首先，今年大家都安逸地使用 IaaS 服务。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-4.png)

我也预测公有云服务商亚马逊 AWS 和微软 Azure 将会是企业进行服务转移时的安全之选；微软也将加大对 Linux 等开源项目的支持以强化自己独有的软件栈。Leong 的 2014 云计算 Gartner Magic Quadrant 肯定了这一预测，同时也揭示 AWS 已经在公有云市场强化了自己的霸主地位。在部署能力方面，AWS 比所有竞争对手加起来还大 5 倍之多， 2014 年占市场份额为 83%，2015 年增长为 91%。微软位居第二，不过仍领先于 Google 及其他公司。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-5.png)

随着公有云厂商在更多国家和地区开展业务，他们也在全球开展「圈地运动」。由于政府和公司对司法权和数据安全的关注，本地化成为云计算的可行之路。去年 AWS 在中国开展业务，成为第 10 个支持的地区；一直谣传的德国业务最终落地法兰克福。访徳期间的各种谈话也纷纷证明，**本地业务**能够促进当地公司对公有云服务的接纳和使用。

亚马逊计划于 2016 年在印度开展 AWS 业务。与此同时微软已经在地区部署上占据领先优势，受 Office365 等类 SaaS 应用的用户需求驱动，他们的服务区域从 15 个增加到 17 个。相反，Google 并未加入竞争。Google 的全部数据中心都位于低开销地区，包括东亚、西欧和美国中部。尽管在过去一年，Google 并未给数据中心增加新的 Google Cloud 支持地区；但是他也开始改变自己的区域模型，与 AWS 类似，在每个地区配备三个协同地带。在这之前，Google 在美国中部仅有两个数据中心，对于依赖网络速度的应用来说远远不够。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-6.jpg)

我在 Structure 大会的演讲中，将 Digital Ocean 称为值得关注的快速成长的云基础设施供应商，而他们确实在过去的一年里持续发展。根据网络主机托管市场份额分析公司 Netcraft 的调查，Digital Ocean 在 2014 年 5 月，已经从第八位一跃成为排名第二的网络主机服务供应商。他们也加倍扩展了自己托管网站的数量。仅在本月（译者注：2015 年 7 月），Digital Ocean 宣布他们获得了 8300 万美元的新投资，目前公司运营大约一万台服务器。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-7.jpg)

在「平台即服务（PaaS）」这一部分，在「Docker all the things」的标题下，我指出，PaaS 供应商 Cloud Foundry 一直以自己的市场份额引领业界，但是 Docker 却颠覆了整个 PaaS 栈。 Docker 提供开放平台供开发者构建、交付并运行分布式应用。 Docker 正通过分解 PaaS 层而持续领导颠覆，高效地把 PaaS 转变为「运行 Docker 容器之所在」。由于担心竞争对手 Docker 不断增加功能，Cloud Foundry 尝试避开与之竞争，转而开发新的容器平台。Docker 已经成功地吸引了各家公司的注意，联合了 PaaS 供应商领导者，共同支持 runC 这一容器平台特性。Docker 将自己的 runC 执行方案贡献给了由 Linux 基金会运营的项目实体。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-8.png)

在数据中心这一战场，去年 VMware 感受到了诸如 Docker 和 Openstack 这些低开销但更为自动化的竞争者的威胁。我也强调了 Mesos，这个集群管理工具能够简化服务器共享池里运行任务的复杂度，在可扩展性和面相开发者方面对 Openstack 构成威胁。作为回应，VMware 在自己的工具中引入 Docker，同时发布了 Photon，一款针对 Docker 进行优化的 Linux 发行版。同时，他们还实现秒级创建虚拟机，提升打包容器的安全性，与别的虚拟机技术相比，实现了最小化。借助 VMware 庞大稳定的生态系统，这种对 Docker 技术的优化，提升了他们的企业接受度。正是基于颠覆自身，VMware 在博弈中取胜，并且将在长期保持。

开源云计算软件 Openstack 正在日渐成熟，尽管少于预期规模，但仍成为诸多新数据中心部署时的首选环境。我曾预测 Openstack 生态系统将会由诸如 Cisco、HP、IBM 和 Oracle 这样的大型企业级厂商主导。确实在过去的一年，许多 OpenStack 及相关基于云的创业公司在市场上苦苦挣扎，最后被巨头收购。Cloudscaling 被 EMC 收购，Metacloud 和 Piston Cloud 被 Cisco 收购，Nebula 的团队被 Oracle 雇佣，Bluebox 被 IBM 收购，Eucalyptus 被 HP 收购， eNovance 和 Inktank 被 RedHat 收购。**唯一**屹立不倒的是 Mirantis ，这家云计算服务公司创造了成功的商业模式，帮助各种机构正确安装 Openstack ，确保其正常运行。从技术的角度看， Openstack 存在诸多难题：太晚才添加面向开发者的功能， Neutron 的软件定义网络的项目扩大了问题规模。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-9.png)

在可扩展的数据中心部署方面，Mesos 是当前赢家。而来自 Google 的竞争对手 Kubernetes 对于更小安装也有兴趣，可以作为 Docker 运行时而成为 Openstack 之上有用的一层。Mesos 已经被 Twitter、AirBnB 和其它公司用于生产，证明自己能够用来创建大型的私有云环境。提供 Mesos 的 Mesophere 公司也在 2015 年初将自己的数据中心操作系统（ DCOS ）从 beta 版升级到生产级。

Docker 对公有云环境的支持也日趋成熟；AWS 提供了类 Mesos 的 EC2 Container Service（EC2 容器服务，简称 ECS）；Azure 除了支持基于 Linux 的 Docker 容器技术，还开发自己的基于 Windows 的容器技术；Google 推出了基于 Kubernetes 的 Google Kontainer Service；而 Digital Ocean 则与 Mesosphere 合作。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-10.jpg)

在应用层面，我在去年指出软件即服务（SaaS）将随着应用的标准化交付模型而被接受。除了企业采用，SaaS 也迅速波及全球厂商。厂商们发现他们再也无需在每个市场提供驻场安装和支持团队。SaaS 的价值实际远远大于云基础设施的价值。 Salesforce 和 Workday 这样的大型 SaaS 厂商继续走强，风投们对 SaaS 服务提供商的投资也持续加大，许多大型企业级厂商正在快速迁移到 SaaS。Azure 的很大一部分就是用来支持包括 Office 365 在内的 Microsoft 的 SaaS 产品。 IBM 已经整合了对 Softlayer 的收购，用来支持公司的 SaaS 服务。Oracle 和 HP 正在构建云服务去支持各自的 SaaS 应用业务。这也让这些厂商们宣称「云收入」的巨大，尽管与 AWS 相比，他们部署的 IaaS 体量不过九牛一毛。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-11.png)

我对 2014 年回顾的最后一点，请注意 Google 的 Go 语言的兴起。使用 Go 的开发者们仍在继续使用这门语言，当前几乎每个新且有趣的项目都用 Go 写。Docker 生态系统几乎全部用 Go，在 CoreOS 和 Hashicorp 的套件也是如此，其它 PaaS 服务，从 Cloud Foundry 到 Apcera、以及新的 SaaS 产品，不一而足。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-12.png)

展望未来，我能看到 Docker 会逐渐成长为标准的生产工具，也期待它能到 2015 年末被更多企业部署。这也从一个侧面反映出 Docker 容器的高接受度，新技术通常需要多年才能被不同公司使用，从早期使用者到传统企业。高接受度是受商业用户和厂商的需求驱动的。各类机构以快速交付创新的云服务（开发者负责开发这些服务）为目标，云厂商们则需要为公有云、私有云、数据中心基础设施市场提供 Docker 容器。Docker 的挑战是要谨慎管理生态系统，同时快速添加功能以支持生产部署。目前为止，Docker 已经阻止了一次生态系统的分裂，同时也宣布了插件化架构，有助于公司轻松替换、增加或者扩展核心功能。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-13.jpg)

审视云技术的未来，除了上文提及的趋势，新趋势也崭露头角 AWS、Azure 和 Google Cloud 的功能在数据中心的功能中交叉使用，而不是像以往那样被用作子集。实际上，如果你希望创建一个靠谱的数据中心，你可以马上在公有云环境中创建，能够弹性扩展、高性能。缺点是它不方便 IT 专家使用公有云厂家提供的各种新功能进行维护。Digital Ocean 却是个例外，他们以简单易用、功能精简为特色。像 AWS re:Invent（亚马逊 AWS 年度用户大会）这样的活动很快就增加了培训和认证的环节。

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/yijian-3-14.png)

最后，对我而言，去年最让我感兴趣的新技术是 AWS Lambda。这是一个高安全、事件驱动的技术模型，能够针对每个事件进程创建新容器。数据变化会生成事件，从而创建一个菊花链网络拓扑，执行业务进程。对于 Lambda，AWS 以十分之一秒为单位、按照容器运行时间收费，每个月可免费请求一百万次。如果你想起黑客们是如何侵入 IT 系统的，就能明白以秒为单位的服务真的是门精妙的技术。配合 AWS 身份和进程管理功能（AWS identity and access management，简称 IAM ）和安全密钥管理服务，数据的每个交互和环节都能被控制、加密和审计。我相信这一模型最终会成为管理至关重要的数据的最佳实践。随着不断有数据中心被侵入，越来越多的人会意识到精品级的、高安全系统应该使用云计算来构建。