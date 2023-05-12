# 「DaoCloud 道客」与 Kubernetes

> 为数字世界寻找全局最优解

## 挑战

[「DaoCloud 道客」](https://www.daocloud.io/)云原生领域的创新领导者，成立于 2014 年底，拥有自主知识产权的核心技术，致力于打造开放的云操作系统，为企业数字化转型赋能。这样的目标与使命决定了公司从创立之初就在云原生的世界里耕耘。与传统业务场景不同的是，云原生业务离不开容器，云操作系统更是依赖容器作为基础设施。因此「DaoCloud 道客」面临的首要挑战就是如何高效管理调度多个容器，如何保证容器间的正常通信。

此外，如今的云原生处在高速发展时期，各类云原生技术方案层出不穷且各有利弊，令人眼花缭乱。用户期望的并非解决眼前问题的局部最优解，而是要寻找全局最优解。如何整合这些独立的项目，取长补短，构建整体的云原生解决方案，这是「DaoCloud 道客」面临的又一挑战，也是云原生行业的发展难题。

## 解决方案

Kubernetes 作为容器编排的事实标准，无疑是首选的容器解决方案。「DaoCloud 道客」架构师兼开源团队负责人徐俊杰（Paco）表示 “Kubernetes 是目前容器生态里面比较基础的一环，绝大多数服务都是基于 Kubernetes 部署的，应用绝大多数都是在 Kubernetes 集群中运行和管理。“

面对层出不穷的技术方案，「DaoCloud 道客」研发副总裁潘远航（Peter）认为，“在众多技术面前，坚持以 Kubernetes 为核心，整合周边最佳实践和先进技术，打造一个适合的平台和方案，才是寻找全局最优解的正确路径。”

## 影响

在拥抱云原生的过程中，「DaoCloud 道客」不断向 Kubernetes 等优秀的 CNCF 开源项目学习，逐渐形成了以 [DaoCloud Enterprise](https://docs.daocloud.io/) 云原生应用云平台为核心的产品架构。「DaoCloud 道客」坚持以 Kubernetes 等世界领先的云原生技术为支点，为军工、金融、制造、能源、政务、零售等垂直行业提供了前沿的云原生解决方案，为浦发银行、华泰证券、富国基金、上汽集团、海尔、复旦大学、屈臣氏、吉致汽车金融、国家电网等各行各业的优秀企业都量身定制了满意的数字化转型方案。

!!! note ""

    “随着 DaoCloud Enterprise 越来越强大，客户覆盖面越来越广，有些客户需要使用 Kubernetes 而不是 Swarm 进行应用编排。Kubernetes 作为一套功能强大的应用编排系统，有着强大的社区支持，也受到很多大公司的青睐。我们作为提供商需要满足用户的需求。”

    [刘齐均（Kebe）](https://github.com/kebe7jun),「DaoCloud 道客」服务网格专家

「DaoCloud 道客」成立的初衷就是帮助传统企业进行数字化转型，实现应用上云。公司成立之后发布的首秀产品 DaoCloud Enterprise 1.0 便是一款基于 Docker 的容器引擎平台，可以轻松打包构建镜像并运行容器。随着应用数量的增加，容器越来越多，如何协调和调度这些容器逐渐成为制约产品性能的主要瓶颈。DaoCloud Enterprise 2.0 开始采用 Docker Swarm 管理容器，但随着容器调度系统越来越复杂，Docker Swarm 也开始显得力不从心。

此时恰逢 Kubernetes 崭露头角，凭借多样的功能、稳定的性能、及时的社区支持、强大的兼容性等优势迅速发展成为容器编排的业界标准。Paco 表示“企业容器平台需要容器编排来规范化应用上云的过程。Kubernetes 在 2016 - 2017 年逐渐成为容器编排的事实标准，我们在 2017 年就开始同时支持 Docker Swarm 和 Kubernetes 了。”

经过一系列的评估，2017 年发布的 DaoCloud Enterprise 2.8 版本开始正式采用 Kubernetes（v1.6.7）作为容器编排工具。此后，2018 年发布的 DaoCloud Enterprise 3.0 采用 Kubernetes 1.10 版本，2021 年发布的 DaoCloud Enterprise 4.0 采用 Kubernetes 1.18 版本。2022 年发布的 DaoCloud Enterprise 5.0 支持 Kubernetes 1.23 至 1.26 版本。

六年时间里发布的四个主要版本一直都在坚定不移地使用 Kubernetes，这足以说明当时的选择是正确的。「DaoCloud 道客」用实际经验证明了 Kubernetes 是容器编排的最佳选择，也用自身行动证明了自己一直都是 Kubernetes 的忠实拥趸。

!!! note

    “借力 K8S 的价值体系『自动化大于人工』，产研团队从0到1完成了从研发构建自动化，测试自动化，安全自动化，发布自动化保证了软件交付质量，其次实现了智能化协作沟通，包括产品需求及定义体系、产品多语言协作体系、产品缺陷修复协作体系、疑难杂症攻坚体系，极大的提升了产研同部门、跨部门的协作效率，这是我们走向世界一流基础设施软件产品的基石。”

    叶挺,「DaoCloud 道客」产品创新副总裁

在 Kubernetes 的助力下，「DaoCloud 道客」 的产品性能更优，更具竞争力。「DaoCloud 道客」坚持以 Kubernetes 为核心，整合周边最佳实践和先进技术，打造出 DaoCloud Enterprise 云原生应用云平台，提供应用商店、应用交付、微服务治理、可观测性、数据服务、多云编排、信创异构、云边协同等能力。DaoCloud Enterprise 5.0 是集云原生技术大成的完全形态。

- 「DaoCloud 道客」为上海浦发银行部署 Kubernetes 平台后，应用部署效率提升 82%，交付周期从半年缩短到一个月，交易成功率达到 99.999%；
- 四川天府银行落地基于 Kubernetes 的云原生平台，将弹性响应时间由数小时大幅缩减到平均 2 分钟，产品迭代周期从两个月缩短为两周，应用上线时间缩短 76.76%；
- 为某合资车企搭建基于 Kubernetes 的云原生平台后，将其交付周期从两个月缩短到一两周，应用部署成功率提升 53%，应用上线效率提高 24 倍；为某跨国零售集团部署基于 Kubernetes 的多个云原生平台模块，为其减少了 46% 的应用部署问题，将监控定位效率提升 90% 以上；
- 为某大型综合类券商搭建统一的云原生 PaaS 平台，使其业务流程效率提升 30%，资源成本节约 35% 左右；
- 为富国基金打造基于 Kubernetes 的新一代云原生 PaaS 平台，将标准中间件部署时间从数小时缩短至数分钟，中间件运维能力提升 50%，容器化程度提升 60%，资源利用率提升 40%。

另一方面，「DaoCloud 道客」自身的产品研发工作也是基于 Kubernetes 进行的。公司基于 Kubernetes 部署了 Gitlab，形成了 “Gitlab —> PR —> 自动化测试 —> 构建发布“的产品开发流程，显著提升了开发效率，减少了重复测试的工作量，实现了应用的自动发布。这样一来，大大节省了运维成本，技术人员可以为开发产品投入更多的时间与精力，打磨出更优秀的云原生产品。

!!! note ""

    “我们的开发者很踊跃地贡献开源，沉淀技术实力，在 Kubernetes 和 Istio 社区都有越来越多的贡献。公司第五代产品走的也是开源路线，为云原生技术添砖加瓦，完善技术生态。”

    徐俊杰 Paco,「DaoCloud 道客」架构师/ 开源 & AD 团队负责人

「DaoCloud 道客」深度参与贡献 Kubernetes 等多项云原生开源项目，在云原生开源社区中的参与度、贡献度持续增长。在过去一年里，「DaoCloud 道客」在 Kubernetes 的开源榜单累计贡献度位居全球第三（基于 [Stackalytics 网站 2023/01/05 的数据](https://www.stackalytics.io/cncf?project_type=kubernetes&date=365)）。

在 2022 年 8 月由 Kubernetes 官方组织的社区贡献者访谈活动中，接见了来自亚太地区的 4 位优秀贡献者，其中 [Shiming Zhang](https://github.com/wzshiming) 和 [Paco Xu](https://github.com/pacoxu)都来自「DaoCloud 道客」，二人均是  SIG Node 的 Reviewer。此外在 2022 Kubecon 北美站上，「DaoCloud 道客」的 [Kante Yin](https://github.com/kerthcet) 荣获 Kubernetes 2022 年度贡献者奖。

此外，「DaoCloud 道客」也在坚持践行云原生信仰，持续回馈云原生社区，开源了 Clusterpedia、Kubean、CloudTTY、KLTS.io、Merbridge、HwameiStor、Spiderpool、Piraeus 等优秀项目，不断完善 Kubernetes 生态体系。其中：

- Clusterpedia 兼容 Kubernetes OpenAPI，实现了多集群资源的同步，提供了更强大的搜索功能，可以快速、轻松、有效地获取集群内所有资源信息。
- Kubean 支持快速创建 Kubernetes 集群以及其他厂商的集群。
- CloudTTY 是专为 Kubernetes 云原生环境打造的 Web 终端和 Cloud Shell Operator，可以通过一个 Web 页面随时随地管理 Kubernetes 集群。
- KLTS 为 Kubernetes 早期版本提供长期免费的维护支持。
- Piraeus 是适用于 Kubernetes 的高性能、高可用性、简单安全的存储解决方案。

「DaoCloud 道客」融合自身在各行各业的实战经验，持续贡献 Kubernetes 开源项目，致力于让以 Kubernetes 为代表的云原生技术更平稳、高效地落地到产品和生产实践中。

!!! note ""

    “「DaoCloud 道客」作为首批 CNCF 官方认证的云原生技术培训伙伴，将持续开展赋能培训、项目指导等活动，携手伙伴，为客户导入云原生，共同打造云原生能力的最佳实践路径。”

    郑松,「DaoCloud 道客」中国区技术总经理

「DaoCloud 道客」研发副总裁潘远航（Peter）认为“企业用户需要的是一个全局最优解，这个最优解可以理解为是涵盖多云编排、信创异构、应用交付、可观测性、云边协同、微服务治理、应用商店、数据服务等能力的最大公约数。”在如今的云原生生态体系里，这些功能都离不开 Kubernetes 作为底层的容器编排技术。这就意味着「DaoCloud 道客」在寻找数字世界最优解的过程中也离不开 Kubernetes，未来的产品研发也将继续以 Kubernetes 为基础。

此外，「DaoCloud 道客」一直致力于 Kubernetes 的培训、推广活动。2017年，公司凭借核心产品云原生应用云平台 DaoCloud Enterprise 成为全球首批通过 CNCF Kubernetes 兼容性认证的厂家。2018年，公司成为 CNCF 认证的 Kubernetes 服务提供商，并成为全球首批获得CNCF官方认证的 Kubernetes培训合作伙伴，全面拥抱 Kubernetes 技术生态。

2022 年 11 月 18 日，由 CNCF 和「DaoCloud 道客」、华为云、四川天府银行、 OPPO 联合发起的「Kubernetes Community Days 成都站」成功举办，聚集了来自云原生领域开源社区的最终用户、贡献者和技术专家，分享关于云原生的多行业实践、热门开源项目、社区贡献心得等丰富内容。未来，「DaoCloud 道客」将继续为 Kubernetes 贡献自己的力量，通过项目培训、社区贡献等活动不断扩大 Kubernetes 的影响力。
