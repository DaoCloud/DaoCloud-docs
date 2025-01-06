# 2024 中国开源年度报告

> 转载自 [HackMD](https://hackmd.io/SEEXRfW3QXa67RO3SOx2dQ)

## 概述

2024 中国开源年度报告以深入全面的数据洞察为基础，共分为九大部分：

- 第一部分 **总体宏观洞篇** ，通过对基础事件、活跃仓库、活跃用户、开源许可证和编程语言等方面的深入分析，揭示中国在全球开源生态中的全貌。
- 第二部分 **OpenRank 排行榜篇** ，提供了全球和中国各领域开源项目、企业、基金会、开发者以及协作机器人的排名，为业界提供全面系统的 OpenRank 指标信息服务。
- 第三和第四部分为 **企业洞察篇** 和 **基金会洞察篇** ，通过演变图和趋势分析，呈现了全球和中国企业、基金会在开源领域中的演化。
- 第五部分 **技术领域洞察篇** ，深入研究了各领域 Top10 榜单和项目变化情况，展示了前沿技术的发展方向和趋势。
- 第六部分 **开源项目洞察篇** ，深入探讨了不同项目类型、领域和主题的多样性和创新方向。
- 第七部分 **开发者洞察篇** ，则通过对开发者类型、工作时间分布、地区分布和机器人使用情况的分析，展现了开发者群体的多样性和工作特征。
- 第八部分 **商业开源洞察篇** ，
- 第九部分 **高校开源洞察篇** 整体而言，数据篇通过丰富多彩的数据洞察与分析，勾勒出中国开源生态在 2024 年的全景图。

### 指标介绍

**OpenRank**

OpenRank 指标是由 X-lab 开放实验室所研发，基于开源开发者-项目协作关系网络构建的协作网络指标，不仅能够很好的表征项目的整体发展状态、社区参与度，同时也引入了开源生态的要素，能够很好地将开源生态中位于关键协作位置的项目、人、组织等实体识别并展示出来。OpenRank 目前已经得到了工业界和学术界的广泛认同，被包括中国标准化研究院系列开源治理标准、信通院开源治理白皮书、开放原子开源基金会全球开源大屏、企业开源办公室治理工具箱等所广泛采纳。

关于该指标的定义请参考：

[1] [Shengyu Zhao et al: OpenRank Leaderboard: Motivating Open Source Collaborations Through Social Network Evaluation in Alibaba. ICSE, 2024](https://www.researchgate.net/publication/376686121_OpenRank_Leaderboard_Motivating_Open_Source_Collaborations_Through_Social_Network_Evaluation_in_Alibaba)

[2] [赵生宇: 如何评价一个开源项目（三）价值流网络, 2021](https://blog.frankzhao.cn/how_to_measure_open_source_3)

[3] 工业和信息化部标准化研究院: 《信息技术 开源治理 第 3 部分：社区治理与运营》[T/CESA 1270.3-2023]、《信息技术 开源治理 第 5 部分：开源贡献者评价模型》[T/CESA 1270.5-2023], 2023

**活跃度（Activity）**

活跃度是 X-lab 研发的评价项目或开发者活跃程度的统计性指标。开发者活跃度由开发者 Issue、PR 及代码 Review 等行为加权得到。项目活跃度由项目中所有开发者活跃度总和进行数值处理后得到。

关于该指标的定义请参考：

[1] [Xiaoya Xia et al: Exploring activity and contributors on GitHub: Who, what, when, and where. APSEC, 2023](https://ieeexplore.ieee.org/abstract/document/10043221)

[2] [赵生宇：如何评价一个开源项目（一）——活跃度，2021](https://blog.frankzhao.cn/how_to_measure_open_source_1)

## 1. 总体宏观洞察

### 1.1 基础事件

**基础事件** 是本数据篇分析的数据基础，是指全球化开源协作平台上（如 GitHub、Gitee 等）由于开发者活动行为所产生一系列事件日志数据。对基础事件的统计分析，可以宏观洞察全球开原生态发展的态势。本次开源年度报告所涉及的开源协作平台包括 GitHub、Gitee 以及 GitLink。

#### 1.1.1 GitHub 全域事件趋势

首先，统计分析全域 GitHub 的事件⽇志总体数量，如下图所示。

![GitHub_annual_events_trend](https://hackmd.io/_uploads/H1PPypmUJl.png)

图 1.1 GitHub 年度事件数趋势

可以看到近⼏年全球开源的总体活跃情况和活跃仓库数量都在明显上升，显⽰了全球开源发展中的增速。2023 年 GitHub ⽇志数据达到了 17.5 亿，相⽐ 2023 年增⻓了约 10%。在经过了 2018-2023 的高增长后，GitHub 平台的年度事件增长数量逐渐下降，2024 年的增长率为 10% 左右。但由于整体体量的关系，10% 的增长率还是一个非常大的数字，继续凸显出开源科技的发展在全球数字化转型中的活跃与关键地位。

#### 1.1.2 GitHub 和 Gitee 的总事件数趋势比较

由于 GitHub 平台活跃事件的庞大，接下来的分析工作，建立在每个平台的前 3 万个活跃仓库的基准之上。为了方便比较，我们选取了 GitHub 与 Gitee 中与开源参与相关性较大的 8 类事件进行统计分析，包括 CommitCommentEvent、ForkEvent、IssueCommentEvent、IssuesEvent、PullRequestEvent、PullRequestReviewCommentEvent、PushEvent 和 WatchEvent。

![GitHuB&Gitee_events_count](https://hackmd.io/_uploads/HJgPyamIyx.png)

图 1.2 GitHub 与 Gitee 活跃仓库事件数

可以看到两个平台的事件数量都呈现上升趋势，但是 GitHub 平台的事件数目波动相比于 Gitee 更大。而 Gitee 的上身则更加稳定。但是由于 GitHub 的先发优势，且为全球平台，其排名前 3 万的仓库的累积事件数量仍然远高于 Gitee 排名前 3 万的仓库。但是国内活跃开源项目的稳步增长态势。反映了国内开发者积极参与和贡献到开源社区的热情，为技术创新和知识共享注入了新的活力。

然而，需要强调的是，单纯依靠前 3 万个活跃项目的数据无法完全揭示全球 GitHub 平台的真实情况，因为长尾效应在全球范围内仍然非常明显。这一点将在后续的分析中更为清晰地体现出来，特别是 GitHub 平台作为全球领先的开源社区的广泛和多样性。在未来，随着技术的不断演进和开源文化的推动，可以期待中国开源社区在全球范围内继续蓬勃发展。

再进一步，分析基础事件的细分领域数据，结果如下图所示

![GitHub_events_type_distribute](https://hackmd.io/_uploads/ry4UJTmL1l.png)

图 1.3 GitHub 细分事件类型占比

![Gitee_events_type_distribute](https://hackmd.io/_uploads/By2rJa7U1x.png)

图 1.4 Gitee 细分事件类型占比

从分析结果可以看到：

- 在 GitHub 平台上，最多的事件类型是 Watch 事件，Pull Request 事件和 Issue Comment 事件分别居二三席。其中各个事件的发生次数占比基本上没有太大的变化，这体现出 GitHub 的开源生态模式在走向一个稳定的趋势。
- 在 Gitee 平台上，事件数据在 2018 年有极大的增长，最初以 Watch 事件为主。但在 2020 年后，Pull Request、 Review Comment 事件开始快速增长，在 2022 年成为最多的事件类型，并且在 2024 年也有持续的增长，占比变为最大。Gitee 事件数据的结构性变化，体现出国内开发者从关注者到贡献者角色的巨大转变，这和全球范围内的观察都是一致的。

### 1.2 活跃仓库

#### 1.2.1 GitHub 全域活跃仓库数目趋势

统计分析了全域 GitHub 活跃仓库的数量信息，如下图所示。

![image](https://hackmd.io/_uploads/SyKT42Q8yx.png)

图 1.5 GitHub 年度活跃仓库数量趋势

活跃仓库数量总体上呈现增长趋势，但增长率在逐年下降。具体而言，2020 年至 2021 年间，GitHub 上的活跃仓库数量增长了约 30%，这是一个非常显著的增长。然而，从 2021 年到 2022 年，增长率下降至约 25%，尽管仓库数量仍在增加，但增速有所放缓。

更显著的变化发生在 2022 年至 2023 年，增长率骤降至 5% 左右。这表明尽管活跃仓库数量仍在增长，但增速明显减缓。到 2024 年，增长率保持在 5% ，活跃仓库数量达到约 9,163 万。

#### 1.2.2 GitHub 和 Gitee 总体活跃仓库活跃情况对比

统计分析 2018 至 2024 年里在 GitHub 和 Gitee 平台上仓库的活跃情况，如下图所示。

![image](https://hackmd.io/_uploads/BJ5lS37L1g.png)

从总体活动量来看：
GitHub 的事件数量远远超过 Gitee，这是因为 GitHub 是全球最大的代码托管平台，活跃用户和项目数量极为庞大。Gitee 的事件数量虽然相对较少，但它在 中国市场 的增长潜力不可忽视。它逐渐成为国内开发者和企业的首选平台。

从增长趋势来看：
虽然 GitHub 的事件数量持续增长，但增长幅度逐年减缓。这表明，尽管 GitHub 依然是主流平台，且其基础庞大，但增速受到了平台成熟和用户增长放缓的影响。相对于 GitHub，Gitee 在过去几年表现出更快的增长，尤其是在 2020 年以后，事件数量增速显著。2020 年前的增幅较小，可能因为 Gitee 的用户基数相对较小。但在 2020 到 2024 年，随着平台功能和用户群体的扩展，Gitee 的事件数量增长势头非常强劲。

![image](https://hackmd.io/_uploads/SJUVB2mLkl.png)

![image](https://hackmd.io/_uploads/BJ0rSh781e.png)

在 Gitee 平台中，审查 PR 事件占据了绝对主导地位，高达 75.6%，紧随其后的是 issue 评论和创建，分别占 7.2% 和 7.1%。PR 事件相对较少，累计为 10% 左右。
而在 GitHub 平台中，issue 评论是最主要的活跃度事件，占 29.1%，显示出用户在问题讨论上的高度参与。PR 事件的创建和合并分别占 24.1% 和 22.3%，表明拉取请求在 GitHub 上同样是一个重要的互动环节。issue 的创建占 15.3%，而审查 PR 事件则相对较少，仅占 9.2%。

![image](https://hackmd.io/_uploads/BJCJO27I1l.png)

根据从 Gitee 平台中提取的前 3 万个仓库逐年 openrank 数据，虽然 Gitee 的 openrank 值呈现稳步增长的趋势，但与 GitHub 相比，仍存在较大的差距。从 2018 年到 2024 年，GitHub 的 openrank 总值持续增长，增幅明显且稳定。相比之下，Gitee 的 openrank 总值虽然也在稳步上升，但其增长速度尽管较快，但仍未能在总量上追赶上 GitHub。

具体来看，GitHub 在过去几年内展现出强劲的增长动力，尤其是在 2020 年至 2021 年间增幅较大。而 Gitee 尽管在 2020 年后进入快速增长期，尤其是在 2022 年和 2023 年的增幅显著，年增长量达到了近 30 万，但与 GitHub 的差距仍然明显，且增长趋势的对比也表明，Gitee 虽然在国内市场的影响力不断提升，但在全球范围内的普及度和活跃度还需进一步加强。

### 1.3 活跃用户

#### 1.3.1 GitHub 总体活跃用户数量趋势

统计分析 GitHub 总体活跃用户数量，如下图所示。

![image](https://hackmd.io/_uploads/SyshunXUyx.png)

活跃开发者数量总体上呈增长趋势，从 2020 年的约 1,454 万增长到 2024 年的约 2,511 万。然而，增长率在 2020 年到 2023 年间逐年下降，从 20% 下降到 9%。2023 年到 2024 年，增长率有所回升，从 9% 增加到 14%。虽然增长速度有所波动，但平台仍在持续吸引开发者。

#### 1.3.2 活跃用户地理分布与排名

1. 全球开发者地域分布

    首先统计分析全球开发者的地域分布，如下图表所示。

    ![image](https://hackmd.io/_uploads/rkG25n7Ikx.png)

    图 1.10 全球开发者地域分布

    表 1.1 全球开发者国家/地区人数分布（Top 10）

    | 排名 |      国家      | 总人数 |  占比  | 年度活跃数 | 活跃率 |
    | :--: | :------------: | :----: | :----: | :--------: | :----: |
    |  1   | United States  | 435202 | 17.11% |            | 57.92% |
    |  2   |     India      | 252054 | 9.91%  |            | 60.26% |
    |  3   |     China      | 184085 | 7.23%  |            | 73.81% |
    |  4   |     Brazil     | 174811 | 6.87%  |            | 73.08% |
    |  5   |    Germany     | 126397 | 4.96%  |            | 73.04% |
    |  6   | United Kingdom | 103061 | 4.05%  |            | 66.28% |
    |  7   |     Canada     | 82627  | 3.24%  |            | 64.74% |
    |  8   |     France     | 78288  | 3.07%  |            | 70.18% |
    |  9   |     Russia     | 60735  | 2.38%  |            | 66.79% |
    |  10  |  South Korea   | 44006  | 1.73%  |            | 64.83% |
    |  11  |     Poland     | 43009  | 1.69%  |            | 69.25% |
    |  12  |   Indonesia    | 42419  | 1.66%  |            | 71.07% |
    |  13  |     Japan      | 41234  | 1.62%  |            | 70.83% |
    |  14  |  Netherlands   | 40852  | 1.60%  |            | 67.44% |
    |  15  |     Spain      | 40527  | 1.59%  |            | 77.00% |

    总体而言，各国的开发者都在不断增加：

    - 美国凭借其在开源领域的先发、以及科技人才优势，位居第一；
    - 按照表中美国总人数（40.9 万）进行折算，实际 GitHub 上的美国开发者总人数大约在 2101 万左右，和 GitHub 公布的官方数据（2200 万）偏差大约在 4%；
    - 印度、中国和巴西以其庞大的人口基数，开发者数量分别位居二三四位，但从活跃率（年度活跃数/总人数）可以看到，中国是前四名中最高的；
    - 欧洲各国的开源开发者也是一股不小的力量，联合起来体量将上升到第二；
    - 根据 GitHub 和 Gitee 公布的官方数据（均是 1200 万左右），中国的全球开源开发者总数将很有可能超过 2000 万，仅从数量上来说，这大约和美国相当。

2. 中国开发者地域分布

    进一步分析，统计中国开发者的地域分布数，如下图表所示。其中，数据来源为“中国”的用户中，正确填写省份信息的开发者，样本数量近 15 万人。

    ![image](https://hackmd.io/_uploads/r1Jat37IJl.png)

    图 1.11 中国开发者地域分布

    北上广深地区的开发者数量占据了中国开发者的主要份额。这些地区凭借其经济、科技、教育和创新资源的集中，吸引了大量的开发者。相比之下，中西部地区的开发者数量明显较少，占比远低于北上广深。尽管中西部一些省份（如四川、湖北、陕西等）近年来有所发展，但整体上，开发者的分布仍集中在经济发达的东部和沿海地区，中西部的开发者数量和集中度仍存在较大差距。

    根据 GitHub 2024 年最新的报告数据，中国开发者总量超过了 900 万，依据比例可以估计各省实际开发者总量。

    表 1.2 中国开发者人数分布（Top 10）

    | 排名 | 省份 | 总人数 | 全国占比 | 实际总量  |
    | :--: | :--: | :----: | :------: | :-------: |
    |  1   | 北京 | 38323  |  22.04%  | 198.36 万 |
    |  2   | 上海 | 28393  |  16.43%  | 147.87 万 |
    |  3   | 广东 | 24959  |  14.49%  | 130.41 万 |
    |  4   | 台湾 | 15894  |  9.53%   | 85.77 万  |
    |  5   | 浙江 | 15816  |  8.13%   | 73.17 万  |
    |  6   | 江苏 |  9369  |  4.90%   |  44.1 万  |
    |  7   | 四川 |  8186  |  4.69%   | 42.21 万  |
    |  8   | 香港 |  6625  |  3.13%   | 28.17 万  |
    |  9   | 湖北 |  5732  |  2.95%   | 26.55 万  |
    |  10  | 陕西 |  3669  |  1.88%   | 16.92 万  |
    |  11  | 福建 |  2853  |  1.61%   | 14.49 万  |
    |  12  | 山东 |  2737  |  1.36%   | 12.24 万  |
    |  13  | 湖南 |  2366  |  1.24%   | 11.16 万  |
    |  14  | 安徽 |  2242  |  1.22%   | 10.98 万  |
    |  15  | 重庆 |  2206  |  0.99%   |  8.91 万  |

    根据上表中的数据，可以观察到中国开源开发者的地域分布与各地区经济发展水平之间的密切关系：

    - 北京、上海、广东、台湾 四大地区的开源开发者人数远超其他省份，尤其是 北京，其开发者人数达到 38,323，占全国的 22.04%，凸显了首都在技术创新和人才集聚方面的显著优势。上海和广东分别位列第二和第三，开发者人数也分别达到 28,393 和 24,959，表明这些地区在开源生态和科技创新领域的领先地位。
    - 台湾位居第四，尽管其面积较小，但其 15,894 名开发者仍占据了全国的 9.53%，反映出台港地区在开源开发中的重要地位，且其高科技产业和开放的政策环境促进了大量开发者的参与。
    - 长三角地区（包括上海、浙江、江苏）和 珠三角地区（包括广东）开源开发者数量庞大，总人数超过 150,000，这反映了东部沿海经济发达地区的强大科技创新力和吸引力，尤其在教育、投资和基础设施方面的优势。
    - 中西部地区，如 四川、湖北 和 陕西，尽管在总量上不及东部地区，但其开发者数量相对较高，尤其是 四川，以 8,186 名开发者位居第七，显示出其良好的宜居环境和快速发展的软件产业吸引了大量技术人才。这些地区逐步形成了较为活跃的技术创新生态，并且随着当地经济的不断发展，吸引力日益增强。

### 1.4 开源许可证

#### 1.4.1 使用开源许可证的仓库数量

统计了 GitHub 的活跃仓库采用的开源许可证的数量，如下图所示。

![license_distribute](https://hackmd.io/_uploads/HJamkTmUJe.png)

图 1.12 使用开源许可证的仓库数量占比

分析发现目前使用最多的开源许可证，包括 MIT 许可证、Apache 许可证 v2.0、GNU 通用公共许可证 v3.0、BSD 3-Clause 许可证。其中 MIT 许可证以接近 43% 的占比排名第一。MIT 许可证以麻省理工学院（Massachusetts Institute of Technology）为名，最早由该学院使用，因此得名。MIT 许可证的简洁和灵活性使其成为许多开发者选择的许可证之一，它提供了最小的法律限制，鼓励开发者自由地使用和传播软件。相比于 2023 年，MIT 许可证的比例下降较多，Apache2.0 许可证比例有所提高，从 15.7%提高到 19.4%。

#### 1.4.2 开源许可证种类变化趋势

统计分析了开源许可证种类变化趋势，如下图所示。

![license_type_count_trend](https://hackmd.io/_uploads/r1Gmkpm8Jg.png)

图 1.13 开源许可证种类数量变化趋势

总体来看，开源许可证的种类在 2017 年以来不断增加。Eclipse 公共许可证 2.0 和欧盟公共许可证 1.2 以及其他许可证的推出造成了 2017-2018 年的增长。在此之后开源许可证种类的增长速度放缓，在 2021 年至 2022 年间，一批新的开源许可证如木兰系列许可证、CERN（欧洲核子研究组织）许可证 v2 开始崭露头角，随后发展趋于稳定，目前 GitHub 上主流许可证的种类也持续两年稳定在 47 个。

#### 1.4.3 使用开源许可证仓库数量变化趋势

根据日志数据显示，2023 年有接近 770 万个活跃仓库使用了各种开源许可证（占全体活跃仓库的 8.76%），其中由于 MIT 许可证强大的影响力，我们将其数据单独展示。

1. 使用 MIT 许可证仓库数量变化趋势

    统计分析了 MIT 许可证仓库数量变化趋势，如下图所示。

    ![MIT_repo_count_trend](https://hackmd.io/_uploads/B1Lf1T7I1x.png)

    图 1.14 使用 MIT 许可证的仓库数量变化趋势

    可以看到：

    - MIT 许可证是目前最流行的开源许可证，2023 年有 158 万个活跃仓库使用了该许可证；但 2024 年反而只有不到 100 万个仓库使用。同时由于 Apache2.0 许可证的占比提高，可以分析得出开源许可证的参与者们希望代码被修改后需要声明修改而不再仅仅是不需要任何声明。
    - 使用 MIT 许可证的仓库在 2024 年有大幅的减少，更多的不同的许可证能够在开源领域有所应用。

1. 其余前五的开源许可证数量变化趋势

    统计分析了其他前五开源许可证仓库数量变化趋势，如下图所示。

    ![Var_license_repo_count_trend](https://hackmd.io/_uploads/HJsbJ67I1l.png)

    图 1.15 使用其他许可证的仓库数量变化趋势

    可以看到：

    - 各类开源许可证的数量在 2024 年都有下降，但是开源许可证种类的头牌依旧还是以 MIT、Apache、GNU 等为主；
    - 小众开源许可证和热门开源许可证的差异仍然存在；
    - 热门许可证的下降比例大于小众许可证。

#### 1.4.4 使用木兰系列许可证仓库数量变化趋势

统计分析使用木兰系列许可证仓库数量的变化趋势，如下图所示，该图表示的是每个月增加的使用木兰许可证的仓库数量。

![Mulan_repo_count_trend](https://hackmd.io/_uploads/BJieypQIyl.png)

图 1.16 使用木兰系列许可证的活跃仓库数量累加图

木兰系列许可证（包含 “木兰宽松许可证” 和“木兰公共许可证”等），均由北京大学作为牵头单位，依托全国信标委云计算标准工作组和中国开源云联盟，联合开源生态圈（如开源社）及产学研团队和个体、尤其是开源法务和律师，起草、修订并发布。其中 Mulan PSL 是国内首个被 OSI 认定的 “开源软件协议”。

我们观测了 GitHub 中使用木兰许可证的活跃仓库（其中，活跃仓库是指仓库里有 issue 和 PR 或者有被用户标星等活动）的趋势，从 2022 年 9 月开始，使用木兰许可证的仓库开始增长。在 2024 年 1 月后，每个月的增长数已经能够稳定在 50 以上 ，木兰开源许可证的影响力在逐渐展现。

### 1.5 编程语言

#### 1.5.1 2024 年开发者使用编程语言榜单

编程语言的受欢迎程度也是开发者所喜闻乐见的，分析了 2024 年度最受开发者欢迎的编程语言，如下表所示。

表 1.3 开发者使用编程语言排行榜（Top 15）

| 排名 |     编程语言     | 使用该语言开发者数 | 使用该语言仓库数 |
| :--: | :--------------: | :----------------: | :--------------: |
|  1   |    JavaScript    |       591223       |      654037      |
|  2   |      Python      |       540751       |      499644      |
|  3   |    TypeScript    |       439954       |      462496      |
|  4   |       HTML       |       424901       |      401084      |
|  5   |       Java       |       281403       |      328123      |
|  6   |       C++        |       143135       |      106444      |
|  7   |       CSS        |       137566       |      114166      |
|  8   |        C#        |       131549       |      163796      |
|  9   |        Go        |       125521       |      121209      |
|  10  | Jupyter Notebook |       119874       |      79415       |
|  11  |       PHP        |       100984       |      108019      |
|  12  |      Shell       |       93726        |      76276       |
|  13  |        C         |       84253        |      60389       |
|  14  |       Rust       |       68199        |      62969       |
|  15  |      Kotlin      |       53503        |      48013       |

从上表中可以看出：开发者使用人数前五名的开发语言分别为 JavaScript、Python、TypeScript、HTML、Java，是开发者使用的主要编程语言，而从第 6 名的 C++ 开始，使用人数相较于第 5 名的 Java 降低了接近一半。

#### 1.5.2 2019-2024 年开发者使用编程语言趋势

统计分析了开发者使用编程语言的趋势，如下图所示。

![Var_language_user_trend](https://hackmd.io/_uploads/Syus02X81l.png)

图 1.17 2019 - 2023 年开发者使用编程语言趋势

从上图中可以看出：

- JavaScript、Python、TypeScript、HTML、Java 五种编程语言是开发者使用的主要编程语言；
- Python、TypeScript 相对于其他的三个主要语言增长迅速，并且近 5 年内一直保持着快速增长的趋势；
- 其中 TypeScript 近 5 年来使用人数飞速增长，在 2021 年与排在其后的编程语言拉开了显著差距，成为了开发者使用的主要编程语言之一，2024 年其开发者使用数将超过在 2023 年排名第 3 的 HTML 编程语言，成为开发者喜爱使用的编程语言新的第三名。

## 2. OpenRank 排行榜

在开源领域，排行榜不仅是衡量项目影响力和活跃度的重要工具，也是反映全球开源生态动态的视图窗口。2024 年的中国开源年报通过 OpenRank 排行榜，提供了一个独特的视角，集中展现开源社区的关键参与者，包括项目、地区、企业、基金会以及新势力项目的活跃度和影响力。报告不仅包括了国内的数据，还整合了 GitHub 和 Gitee 平台上的全球数据，提供了全球性视角的贡献与分析。通过排行榜，我们期望能够进一步推动开源文化的普及和开源技术的应用，同时鼓励更多的企业和个人参与到开源项目中来。

![全球项目排行榜](https://hackmd.io/_uploads/HJ7hkTmUye.png)

图 2.1 2024 年全球项目 OpenRank 排行榜 Top 30

根据 2024 年全球项目 OpenRank 排行榜 Top 30，中国开源项目 OpenHarmony 以 67538.71 的 OpenRank 值位居榜首，显示出其在开源社区中的极高活跃度和影响力。Azure 和 .Net 分别位列第二和第三。OpenHarmony 和 LLVM 在 OpenRank 分数上有显著增长，反应了它们在特定领域或技术栈中具有巨大的增长潜力与社区影响力。

![中国项目排行榜](https://hackmd.io/_uploads/S13QZTXL1e.png)

图 2.2 2024 年中国项目 OpenRank 排行榜 Top 30

2024 年中国项目 OpenRank 排行榜中包括了操作系统（如 OpenHarmony）、人工智能（如 MindSpore）、数据库（如 openGauss、TiDB）、大数据处理（如 Apache Flink）等多个领域的项目，显示了中国开源项目的多样性。华为在排行榜中占据了多个位置，包括 OpenHarmony 和 openEuler，这显示了华为在中国开源社区中的显著影响力和对开源项目的贡献。

![企业排行榜](https://hackmd.io/_uploads/r1Y8M6XL1e.png)

图 2.3 2024 年全球企业 OpenRank 排行榜 Top 30

2024 年全球企业 OpenRank 排行榜中，美国企业占据了绝大多数的位置，显示出美国在全球开源项目中的领导地位。特别是微软（Microsoft）、谷歌（Google）、亚马逊（Amazon）等公司在 OpenRank 分数上遥遥领先。同时也可以看到中国企业的快速发展，华为（Huawei）和阿里巴巴（Alibaba）分别位列第二和第八位，反应了中国企业在全球开源领域的影响力正在增强。

![04 中国企业排行榜](https://hackmd.io/_uploads/Hycfmp7I1g.png)

图 2.4 2024 年中国企业 OpenRank 排行榜 Top 30

2024 年中国企业 OpenRank 排行榜中多为大型公司的贡献，如华为（Huawei）、蚂蚁（Ant group）、百度（Baidu）、阿里巴巴（Alibaba）等，这表明中国的大型企业在推动开源项目方面扮演着重要角色。

![05 基金会排行榜](https://hackmd.io/_uploads/B1X4XTXIkx.png)

图 2.5 2024 年开源基金会 OpenRank 排行榜 Top 30

2024 年开源基金会 OpenRank 排行榜中，开放原子基金会（OpenAtom Foundation）位列第一，这表明中国在开源领域的影响力正在增强，尤其是在推动大型开源项目方面。此外，美国拥有多个高排名的开源基金会，如 Cloud Native Computing Foundation、Apache Software Foundation 和 Linux Foundation。

![06 行政区排行榜](https://hackmd.io/_uploads/HJcEX6m8ke.png)

图 2.6 2024 年全球行政区划开发者 OpenRank 排行榜 Top 30

2024 年全球行政区划开发者 OpenRank 排行榜中主要包括美国、中国、德国、法国、加拿大、日本等多个科技水平较高的行政区划城市。

![07 中国行政区排行榜](https://hackmd.io/_uploads/SJzS7a7Lyx.png)

图 2.7 2024 年中国行政区划开发者 OpenRank 排行榜 Top 30

2024 年中国行政区划开发者 OpenRank 排行榜中北京和上海占据中国开源发展的领导地位，此外，沿海岸城市与西部地区都有较高的开发者数量和发展潜力。

![新势力项目](https://hackmd.io/_uploads/SJnHXaXI1x.png)

图 2.8 2024 年全球新势力项目 OpenRank 排行榜 Top 30

2024 年全球项目新势力 OpenRank 排行榜以项目级标签统计排名，反应了高度活跃的核心项目与开发团队，代表了未来的技术趋势或者创新方向。

## 3. 企业洞察

企业在开源生态中的角色与表现正日益成为评估其技术创新能力与行业影响力的重要维度。从全球化的技术竞争到本地化的行业应用，开源已经成为企业数字化转型和技术突破的重要驱动力。随着开源生态的不断扩展，企业的开源活跃度、贡献度以及影响力逐步形成了衡量其综合实力的重要指标。本节内容将通过分析全球和中国企业近十年的 OpenRank 演变趋势，结合 2024 年度的活跃度与 OpenRank 排名情况，深入探讨企业在开源领域的表现及其对行业生态的贡献。特别是针对今年中国企业中的黑马 DaoCloud，将通过数据可视化、核心项目生态协作网络与社区协作网络的分析，展现其在云原生技术领域的快速崛起与战略布局。

### 3.1 近 10 年全球企业 OpenRank 演变图

![img](https://kaiyuanshe.github.io/2023-China-Open-Source-Report/image/data/chapter_3/3-1.png)

- 微软从十多年前（2008 年）开始布局开源，在 2016 年站到了全球开源影响力的巅峰，直到今天无人撼动；
- 2019 年，华为正式被美国制裁开始，将开源作为重要战略方向，一路飙升，并于今年完成了对 Google 和 Amazon 的超越；
- 阿里巴巴在 2021 年前，一直是国内开源的领先者，并至今稳居世界第六的排名；
- 蚂蚁集团在近三年的表现也是非常抢眼，并于 2023 年正式进入世界前十；
- 国内开源的第四大巨头百度，由于国内快速的开源态势变化，目前排名全球 12；
- 根据 OpenLeaderboard 榜单，进入全球前 30 的中国企业还有字节跳动（18）、PingCAP（19）、飞致云（24）、Deepin（25）、腾讯（26）、以及 Espressif（27）。

### 3.2 近 10 年中国企业 OpenRank 演变图

![img](https://kaiyuanshe.github.io/2023-China-Open-Source-Report/image/data/chapter_3/3-2.png)

本图能够很好表现国内公司的开源战略及其变化趋势：

- 华为 2019 年开始发力，仅用 2 年的时间就做到了国内第一，全球第二的位置；
- 阿里和蚂蚁作为国内老牌开源引领的企业，表现稳定；
- 百度则由于前面三家的竞争，滑落第四；
- 字节跳动则是近几年肉眼可见的进步神速；
- Espressif（乐鑫科技）是国内开源界相对低调的半导体开源王者；
- Fit2Cloud 则是作为另一家低调但非常务实的开源企业，旗下多款开源软件深受开发者喜爱；
- 腾讯、PingCAP、JD、TAOS 等近两年略有下跌趋势，印证了后疫情时代的开源竞争将更加激烈。

### 3.3 2024 年度全球企业的活跃度前 10

![image](https://hackmd.io/_uploads/rklKk5XIye.png)

微软 (Microsoft) 稳居第一，以绝对优势（活跃度 706,985.92）在各项指标上表现最为出色，证明其持续在开源生态中的领导地位。华为 (Huawei) 超越谷歌，上升两位至第二名，展现了其在开源社区中的强劲增长（活跃度增长 147,619.52）。谷歌 (Google) 下滑一位至第三名，活跃度仍维持在较高水平（290,417.81）。亚马逊 (Amazon) 和 Red Hat 分列第四和第五，前者活跃度略有下降。Mozilla 上升一位至第六名，表明其在开源领域的贡献有提升。
其他企业如 Meta、IBM、阿里巴巴 (Alibaba) 和 Elastic 也保持了在前十名中的竞争力。

- 华为的快速崛起：活跃度和贡献指标均显著增长，反映出其对开源生态的持续投入，特别是在 PR 审查和 Issue 评论上的活跃表现。
- RedHat 和 Mozilla 的稳定贡献：作为传统开源社区的领导者，这两家公司继续在开源项目贡献中扮演重要角色，展现了持续的影响力。
- 中国企业的表现：除华为外，阿里巴巴也榜上有名，排名第九。这表明中国企业在全球开源领域的影响力正在逐步上升。
- Microsoft 是开源生态中无可争议的领导者，各项指标均表现优异。
- 华为 和 Google 在开源贡献上的竞争日益激烈。
- 其他老牌开源企业如 RedHat 和 Mozilla 依然保持了在社区中的活跃度和贡献力。
- 从整体上看，这份 OpenRank 榜单反映了全球开源生态中的多样化和竞争格局，以及企业对开源的日益重视。

### 3.4 2024 年度全球企业的 OpenRank 前 10

![image](https://hackmd.io/_uploads/S1pc7aQLkx.png)

- 北美企业的强势地位：前十中，北美企业占据七席，微软、谷歌和亚马逊继续主导开源生态。这些企业在基础设施、AI、云计算等领域贡献巨大，是全球开源的核心推动力。
- 中国企业的崛起：华为的高速增长显示其在开源技术和全球化方面的显著进步。
- 阿里巴巴的排名下降则反映了开源生态中新的挑战。
- 老牌企业的复苏：Red Hat、IBM 等传统企业重新发力，显示出老牌技术公司依然具有强大的技术积累和生态价值。
  未来趋势：
- 全球企业的开源竞争将更加激烈，各大公司需要在技术贡献、社区互动和生态扩展方面进一步投入。

### 3.5 2024 年度中国企业的活跃度前 10

![image](https://hackmd.io/_uploads/rkA0CtQU1g.png)

- 华为 (Huawei) 稳居第一，其活跃度（422,865.51）远高于其他企业，展示了在开源领域的绝对领先地位。
- 阿里巴巴 (Alibaba) 和 蚂蚁集团 (Ant Group) 分列第二和第三，显示了阿里系在开源领域的持续深耕。
- 百度 (Baidu) 保持第四，活跃度为 53,851.9。
- DaoCloud 是本次榜单的黑马，上升 10 位至第五名，活跃度大幅增长。
- 其他企业如 字节跳动 (ByteDance)、PingCAP、ESPRESSIF、腾讯 (Tencent) 和 Fit2Cloud 则分列第六至第十名。
- 华为的绝对优势：在所有指标上均位列榜首，充分展现了其在开源社区的主导地位。
- DaoCloud 的强势崛起：活跃度大幅提升，并在创建 Issue 和 Pull Request 上表现出色，成为本年度榜单的一大亮点。
- 阿里系的整体实力：阿里巴巴 和 蚂蚁集团 双双跻身前三，显示出阿里系企业对开源生态的持续投入。
- 中小型企业的竞争力：企业如 ESPRESSIF 和 Fit2Cloud 尽管体量较小，但也展示了显著的开源贡献。

这份榜单体现了中国企业在全球开源领域的强劲表现：

- 头部企业（如华为、阿里巴巴）持续扩大领先优势。
- 新兴企业（如 DaoCloud）快速崛起，带来了更多活力。
- 数据表明，中国企业在开源领域不仅注重贡献代码，还积极参与社区互动和治理，推动了全球开源生态的发展。

### 3.6 2024 年度中国企业的 OpenRank 前 10

![image](https://hackmd.io/_uploads/BkFQG6XI1l.png)

- 华为凭借高额得分和显著增长继续稳居榜首。
- 阿里巴巴和百度依旧占据前列，但受到其他新兴企业的挑战。
- DaoCloud 的跃升和 Fit2Cloud 的新进入，说明中小型企业在开源领域的活跃度逐渐增强。
- 整体来看，榜单中的企业在多样化领域（如云计算、IoT、数据库等）都展现了开源的深度参与。

### 3.7 2024 年度中国企业黑马 DaoCloud 的解读

在 2024 年度的中国企业 OpenRank 和活跃度两个榜单中，DaoCloud 以令人瞩目的表现跻身前十，OpenRank 从去年的排名中上升了整整 9 位（来到全国第 6）；同时活跃度上升了 10 位（来到全国第 5），成为了本年度当之无愧的“黑马”。
**值得关注的是 2024 年 6 月各高校 Docker 镜像网站被封，大量开发者转向 DaoCloud，带来了 DaoCloud 的快速崛起。**
DaoCloud 得益于其在开源领域的持续投入和创新，不仅通过技术创新推动了容器云和微服务架构的普及，还积极参与了多个国内外主流开源项目的研发与贡献，例如 Kubernetes 生态、容器编排工具和云原生开发框架等。这种崛起也反映了中国科技企业在开源技术发展和社区参与中的多样化探索与成功实践。DaoCloud 的表现不仅提升了自身的行业影响力，也为其他中小型企业提供了开源发展的参考路径。

#### 3.7.1 DaoCloud 企业洞察大屏

![image](https://github.com/user-attachments/assets/25d53bf8-31ed-4c9d-9b1b-993d5f9a872d)

这张图是 DaoCloud 洞察大屏，展示了 DaoCloud 的总体贡献情况、活跃项目排行、贡献者分布以及一些重要的开源活动指标（如 Issue、Commit 和 PR 的变化趋势）。

DaoCloud 活动趋势分析

- Issue 月度变化：2024 年 5 月，Issue 数量出现高峰（超过 60,000），可能是因为新版本发布或重大事件推动了社区讨论。
- 后续的关闭和处理趋势表明社区对问题的响应效率较高。
- Commit 月度分布：历史上社区的 Commit 活动有明显波动：
- 2020 年和 2023 年分别出现两次较大峰值，可能对应社区的重要版本发布或功能更新。
- 最近一次（2024 年底）Commit 数量也显著上升，显示出社区活跃度的增长。
  PR 月度变化：PR 的打开、合并和关闭数量在 2024 年度整体保持稳定，显示出社区开发活动的高效和有序。

总结与观察

- 核心项目表现突出：public-image-mirror 和 DaoCloud-docs 是社区的核心项目，贡献了主要的活跃度和影响力。
- 社区协作紧密：从 PR 和 Issue 的处理效率可以看出，社区对开发者的反馈及时且高效，增强了社区凝聚力。
- 持续增长的活跃度：贡献者数量、Commit 活动和 PR 活跃度均表明社区仍在快速发展，具备持续吸引新开发者的能力。
- 整体健康的社区生态：多样化的贡献者结构、活跃的项目管理和稳定的开发活动使 DaoCloud 社区在开源生态中占据了重要位置。

public-image-mirror（公开镜像服务）和 DaoCloud-docs（相关文档协作）是 DaoCloud 的两大核心项目，下面对这两个仓库进行解读

#### 3.7.2 DaoCloud 核心项目 DaoCloud-docs 的生态协作网络

![image](https://hackmd.io/_uploads/BkK8p678yx.png)

这个图是 DaoCloud 社区中 DaoCloud-docs 项目 的生态网络，旨在展示项目与其他项目、组织之间的相互联系，以及它们的开发活动和合作关系。

主要发现：

- 与 Kubernetes 的强联系：DaoCloud-docs 与多个 Kubernetes 相关项目（如 kubernetes/kubernetes、kubernetes/website）有较强的联系，这表明它在 Kubernetes 生态中扮演了重要角色。这种联系可能来自于 DaoCloud 对 Kubernetes 的深度使用、扩展或贡献。
- 与 Istio 的合作：DaoCloud-docs 与 Istio 项目也有显著的关联（如 istio/istio、istio/istio.io），说明其在服务网格技术上的协同作用。
- 其他合作伙伴：除了 Kubernetes 和 Istio，DaoCloud-docs 还与 GoogleCloudPlatform、Kubean-io 等多个项目有联系，显示了其在多云和容器技术中的活跃度。

#### 3.7.3 DaoCloud 核心项目 DaoCloud-docs 的社区协作网络

![image](https://hackmd.io/_uploads/rJtT2i7Iyx.png)

这个图展示了 DaoCloud-docs 项目的社区网络（Project Community Network），通过开发活动和组织关联分析了项目社区的分布和组成。

主要发现：

- 社区的核心力量：中国开发者和组织 是该项目社区的核心力量，主要的贡献者和关联组织均来自中国。开发者 samzong 是贡献最多的个人，其提交的 PR 数量表明其在项目中的主导作用。
- 国际化影响力：尽管社区的核心集中在中国，但该项目也得到了其他国家和地区开发者的关注，如美国和韩国，这表明 DaoCloud-docs 项目具有一定的国际化影响力。
- 组织协作：不同组织如 EMC 和 @DaoCloud 的参与显示了跨组织协作的特点，有助于提升项目的多样性和影响力。

[DaoCloud-docs](https://github.com/DaoCloud/DaoCloud-docs/)
项目社区展现出了显著的本地化特性，以中国的开发者和组织为主要贡献力量，同时也具有国际化的潜力。

#### 3.7.4 DaoCloud 核心项目 public-image-mirror 的生态协作网络

![image](https://hackmd.io/_uploads/ByUmKTQIyg.png)

强连接的项目：

- kubesre/docker-registry-mirrors（连接强度：161）和 DigitalPlatDev/FreeDomain（连接强度：176）是与 public-image-mirror 项目联系最紧密的两个项目，可能是共同开发、资源共享或技术集成的结果。
- kubernetes/kubernetes（71）和 alibaba/nacos（52）也与其有显著关联，表明它们可能使用或依赖于该镜像项目。
- 与多个工具和镜像服务的协作：项目与 imdingtalk/image-mirror 和 langenius/dify 等镜像工具有较多互动，这表明 public-image-mirror 项目可能为这些工具提供了基础设施支持。
- 与其他核心项目的合作：DaoCloud/DaoCloud-docs 是与其关系密切的同属 DaoCloud 的另一个核心项目，可能协作于文档和配置相关的开发。

#### 3.7.5 DaoCloud 核心项目 public-image-mirror 的社区协作网络

![image](https://hackmd.io/_uploads/rkpkTT7LJl.png)

主要贡献者：

- samzong 提交了大量 PR（279），是该项目的核心贡献者。
- 其他贡献者如 JaredTan95、yank1 和 cuisongliu 也通过 PR 和 Star 等形式为项目做出了显著贡献。

主要贡献来源：

- 中国（China）是社区协作的主要来源，显示出该项目的本地化特性。
- 美国（United States）和 台湾（Taiwan）也参与了协作，表明项目具有一定的国际影响力。

## 4. 基金会洞察

作为非营利性开源组织，基金会在推动开源项目和社区的组织、发展以及协同创新中发挥了不可或缺的作用。它不仅为开源软件的孵化提供技术支持、运营管理和法律保障等全方位服务，还为社区建设和运营提供了科学指导，成为孵化器和加速器的结合体，为开源生态注入了持续发展的动力。基金会作为开源生态的重要组织者，其规范化的运作模式和资源整合能力，使其在连接开发者、企业与社区间发挥桥梁作用。本部分从基金会这一维度，对开源生态的发展进行分析，旨在通过数据洞察揭示基金会在开源生态中的核心地位和实际贡献。

### 4.1 全球基金会 OpenRank 趋势分析

![image](https://github.com/user-attachments/assets/9f4213a6-fd08-4eb0-9fbb-855fc352f5fe)

- OpenAtom Foundation 的表现尤为突出，其影响力继续快速攀升，成为 2024 年的最大亮点。体现了其强大的生态扩展能力和项目影响力。
- 相比之下，CNCF（Cloud Native Computing Foundation） 和 Apache Software Foundation 的增长势头明显放缓，虽然仍保持较高影响力，但 2024 年未能进一步扩大领先优势，甚至出现小幅下降，这可能反映了云原生技术进入成熟期以及竞争加剧的挑战。
- 与此同时，Linux Foundation 继续保持稳健发展，展现出较强的稳定性。而 OpenJS Foundation、Hyperledger Foundation 等基金会排名且波动不大，说明其社区和项目影响力提升有限。

2024 年整体趋势表明，快速增长的基金会正在凭借创新技术和强大的社区生态获得市场认可，而成熟基金会则需要在保持现有优势的同时，寻找新的突破点来应对日益激烈的竞争。

### 4.2 全球基金会项目 OpenRank 趋势分析

![image](https://github.com/user-attachments/assets/da1ec28f-f4af-4f40-bedc-813c3dd251bd)

- 2024 年，一些项目影响力快速上升，例如 OpenHarmony/docs，其 OpenRank 在 2024 年达到历史新高。自 2023 年开始，该项目的影响力显著增长，可能得益于生态系统的扩展和社区活动的推动。这样的表现说明该项目在市场推广和技术应用方面取得了较大的突破。
- 相比之下，Kubernetes/kubernetes 的 OpenRank 自 2020 年以来持续下降，2024 年，其影响力进一步削弱，这可能与社区活跃度的降低或竞争对手的崛起密切相关。这种趋势表明，曾经主导市场的项目也可能在市场环境变化中失去优势。
- Apache/doris 是另一个值得关注的项目，其 OpenRank 在 2024 年继续保持稳步增长。这表明该项目在数据处理领域的表现受到越来越多用户和社区的认可，其技术和功能的不断优化是影响力提升的重要原因。
- 同时，一些成熟的项目，如 Cilium/cilium 和 Envoyproxy/envoy，在 2024 年的表现相对平稳，OpenRank 的波动较小。这说明这些项目已进入稳定发展阶段，影响力保持在一定水平。

### 4.3 基金会旗下中国项目 OpenRank 趋势分析

![image](https://github.com/user-attachments/assets/f53a5538-b604-4d90-a3f7-73e21fad22cd)

2024 年基金会旗下中国项目 OpenRank 总体呈上升趋势。可以看出，中国开源项目在不同技术领域展现了强劲的影响力和发展潜力。

- 其中，openharmony/docs 排名第一，也体现了 OpenHarmony 社区在推动生态建设方面的高度重视。此外，OpenHarmony 的其他核心模块（如 graphic_graphic_2d、interface_sdk-js 和 xts_acts）也位列前茅，这说明其在操作系统领域已构建出较为成熟和活跃的社区生态，核心组件获得了开发者的广泛关注和参与。
- 在分布式数据处理和存储领域，apache/doris 作为高性能分析型数据库项目，排名第二，显示出其在大数据和分析场景中的重要地位。类似地，milvus-io/milvus 专注于向量数据库的开发，在人工智能和大数据技术的快速发展中具有重要的应用前景。与之相近的 apache/flink 和 apache/shardingsphere。则代表了国内开发者在实时计算和分布式数据库技术方向的创新能力，突显了中国开源社区在全球化技术领域中的影响力。
- 此外，openeuler/kernel 作为 openEuler 的核心模块，是国内操作系统领域的代表性项目，反映了基础软件技术的持续进步和社区协作的成果。而 openharmony-sig/arkcompiler_runtime_core 则表明国内操作系统生态不仅关注内核开发，也注重编译器和运行时等关键技术的突破。

综合来看，这些项目展现了中国开源社区在操作系统、数据库、人工智能和大数据等领域的多样化技术实力。排名靠前的项目通常拥有成熟的社区生态和广泛的开发者基础，推动了国内外技术交流与合作。未来，这些项目可以通过进一步强化文档质量、社区运营和技术创新来扩大影响力，同时加强跨项目协作，推动中国开源技术在更多领域取得突破。

### 4.4 开放原子基金会旗下项目 OpenRank 趋势分析

![image](https://github.com/user-attachments/assets/be6ee79f-22a3-48a1-8cb6-6df409bd92e9)

- OpenHarmony 遥遥领先，显示出其在开源社区中的核心地位。作为分布式操作系统框架，OpenHarmony 支持多场景应用，拥有广泛的开发者基础和强大的社区支持。紧随其后的 openEuler 以服务器操作系统为主，分值也大幅领先其他项目，说明其在企业和技术社区中具有重要影响力。
- 排名中间的 Anolis OS 和 openKylin 均为国内操作系统领域的项目，分值接近，表明两者在开源社区中都有一定的技术认可度和贡献度。相比之下，跨端开发框架 Taro 的分值虽显著低于操作系统类项目，但在前端开发领域展现了较高的知名度和使用率。

整体来看，头部项目占有较高的影响力，展现出明显的头部效应。整体分值较高的为操作系统类项目因；

## 5. 技术领域洞察

技术领域的发展在开源技术中起着风向标的作用，众多技术子领域展现出快速的进步和变革：操作系统领域不断适配新架构，在开源社区中持续演化；云原生技术推动企业实现数字化转型，其开源项目生态活跃且增长迅速；数据库作为数据创新的核心基础设施，开源技术的广泛应用促进了多样化场景的突破；大数据领域依托开源工具，正为智能决策提供强大支撑；人工智能借助开源框架加速各行业的自动化进程；前端技术则通过开源项目推动交互体验与视觉设计的不断提升。这些领域以其开放性和创新性吸引了众多开发者与投资者的关注，本节将基于影响力和活跃度两大指标对其进行数据洞察分析。

### 5.1 各子领域近 5 年变化趋势

![image](https://hackmd.io/_uploads/H1tQ2s78yx.png)

OpenRank of Technology Category 2020-2024

![image](https://hackmd.io/_uploads/B1h7tT78Jl.png)

Activity of Technology Category 2020-2024

从各子领域近 5 年的变化趋势来看，云原生优势明显，该领域下仓库数量相对其他领域较多；AI 在近几年的快速发展中增速显著；数据库作为关键的基础软件，以其活跃性稳居前列；大数据热度在 2024 年略有下降；操作系统领域虽仓库数量较少，但其影响力逐年上升，展现出基础软件高价值的特性；前端领域的影响力则呈现逐年降低的趋势。

### 5.2 各领域 OpenRank Top 10 项目近五年变化趋势

#### 大数据

![image](https://hackmd.io/_uploads/SJ3AnoXLJx.png)

OpenRank of Big data 2020-2024

![image](https://hackmd.io/_uploads/rJB76i7Iye.png)

Activity of Big data 2020-2024

大数据领域的双指标整体呈现上升趋势，其中 Kibana 和 Grafana 在影响力和活跃度上始终位居前二。值得注意的是，2023 年两者之间的差距逐渐缩小，而到了 2024 年，这一差距又开始扩大。此外，Clickhouse 和 Doris 在大数据领域的竞争也日益激烈。

Kibana 是一款开源的数据可视化与探索工具，与 ElasticSearch 无缝集成，支持对 ElasticSearch 数据的查询、分析和可视化。
Grafana 则是一款功能强大的开源数据可视化工具，广泛应用于监控与报告场景。它支持多种数据源，包括 Prometheus、InfluxDB 和 Graphite 等，能够生成多种类型的图表和仪表板，为用户提供灵活的数据展示与分析能力。

#### 数据库

![image](https://hackmd.io/_uploads/S1CT6jQI1l.png)

OpenRank of Database 2020-2024

![image](https://hackmd.io/_uploads/SJpRTsmLyg.png)

Activity of Database 2020-2024

ClickHouse 数据库双指标持续稳定增长，ElasticSearch 重回榜单前三，Doris 的增速虽有所放缓，但活跃度指标已接近第一，预计其双指标未来有望超越 ClickHouse。此外，YDB 增速显著，在 2024 年成功进入榜单前十。

ClickHouse 是由俄罗斯 Yandex 公司开源的一款基于 MPP 架构的高性能分析引擎，其向量化执行引擎使其号称比传统事务型数据库快 100-1000 倍，同时具备丰富的功能和极高的可靠性。
Apache Doris 是百度贡献的开源 MPP 分析型数据库产品，具有简洁的分布式架构，便于运维，广泛应用于高效的实时分析场景。

YDB 作为开源项目于 2020 年发布，旨在提供支持 ACID 事务的高效分布式数据库解决方案，尤其适合高并发和分布式应用场景。YDB 的设计和开发旨在解决 Yandex 自身的技术挑战，随着开源后，它吸引了越来越多的开发者和企业的关注，并成为了现代分布式数据库领域的一部分。

#### 操作系统

![image](https://hackmd.io/_uploads/BJkUCjQ8Jl.png)

OpenRank Operating System 2020-2024

![image](https://hackmd.io/_uploads/HkX_Rj78Jx.png)

Activity of Operating System 2020-2024

可以看到，OpenHarmony 项目下的多个仓库位居榜单前十。本次洞察结合了 Gitee 平台的数据，更直观地展现了国产操作系统的多方面优势。此外，OpenEuler Kernel 项目也表现不俗。

#### 云原生

![image](https://hackmd.io/_uploads/r170Ro78yl.png)

OpenRank of Cloud Native 2020-2024

![image](https://hackmd.io/_uploads/H1zJ1hXL1x.png)

Activity of Cloud Native 2020-2024

LLVM-Project 增速显著，双指标位居第一；Grafana 增速放缓，排名第二；Kubernetes 双指标下降明显，其余项目竞争激烈。
LLVM 是一个模块化、可重用的编译器框架和工具链技术的集合，近 3 年来活跃度增长迅速，深受广大开发者喜爱。

#### 前端

![image](https://hackmd.io/_uploads/HJQq12X8Jx.png)

OpenRank of Frontend 2020-2024

![image](https://hackmd.io/_uploads/Bktj1nmLJe.png)

Activity of Frontend 2020-2024

Flutter 虽然双指标逐年下降，但相较于 Next.js 仍具明显优势。Next.js 自 2023 年起表现亮眼，增速显著，但在 2024 年有所回落；排名 3-10 的项目竞争激烈，差距较小。

Flutter 是由 Google 开发的框架，前端和全栈开发人员可使用它通过单一代码库为多个平台构建用户界面。
Next.js 是由 Vercel 创建的开源框架，基于 Node.js 和 Babel 构建，设计与 React 单页应用框架配合使用，同时提供预览模式、快速开发编译和静态导出等实用功能。

#### 人工智能

![image](https://hackmd.io/_uploads/SJFzg2Q81g.png)

OpenRank of AI 2020-2024

![image](https://hackmd.io/_uploads/BJdXxhQLye.png)

Activity of AI 2020-2024

自 2020 年起，TensorFlow 的双指标持续下滑，至 2024 年已跌出 OpenRank 榜单前十。相比之下，PyTorch 稳步增长，与其他项目的差距逐步拉大。值得一提的是，LangChain 自 2022 年开源后双指标一直稳居前三，尽管 2024 年热度略有回落，但其影响力依然显著。同时，vllm 增速显著，超越 LangChain 位居第二，而 Huggingface/Transformers 项目则保持双指标的稳定增长。

LangChain 是 Harrison Chase 于 2022 年 10 月推出的开源项目，已成为 LLM 开发中备受欢迎的框架之一。
vllm-project/vllm 是一个高效、可扩展的分布式推理框架，专为大规模语言模型（LLM）的高效推理优化而设计。近 3 年活跃度显著增长，深受开发者喜爱。

### 5.3 各领域 OpenRank Top 10 榜单

下面再给出 2024 年各领域的项目 OpenRank 排行榜。

![image](https://hackmd.io/_uploads/SJq6827Ikx.png)

大数据领域 OpenRank TOP 10 榜单

![image](https://hackmd.io/_uploads/H1Kj_nmIkg.png)

数据库领域 OpenRank TOP 10 榜单

![image](https://hackmd.io/_uploads/rkQCO37Lyg.png)

操作系统领域 OpenRank TOP 10 榜单

![image](https://hackmd.io/_uploads/By-sPh7Ikx.png)

云原生领域 OpenRank TOP 10 榜单

![image](https://hackmd.io/_uploads/Skj6t2mI1x.png)

前端领域 OpenRank TOP 10 榜单

![image](https://hackmd.io/_uploads/H1My93Q8kl.png)

人工智能领域 OpenRank TOP 10 榜单

## 6. 开源项目洞察

2024 年，开源项目在经历了 AI 大模型、生成式 AI 的快速发展后逐渐呈现平稳演进的态势，以及在数据库领域的稳步发展后，呈现出新的活力。本章节从开源项目的视角出发，深入分析了项目的多维度数据，以获得更全面的洞察。通过对开源项目的 Topic 进行统计分析，揭示了全球开源社区在 2024 年的共同兴趣点。

### 6.1 项目类型

本小节选取了 GitHub 活跃度排名前 10,000 的仓库数据进行统计分析。

#### 6.1.1 不同项目类型数量比例

![App-Proportion](https://hackmd.io/_uploads/BkTufhQUJx.png)

图 6.1 不同项目类型数量比例

- Application Software（应用软件）：用蓝色表示，占据了饼图的 24.3%，这表明应用软件在所分析的数据集中占有相当的比例，反映出应用软件在软件生态中的重要性。
- Libraries and Frameworks（库和框架）：用橙色表示，占比最大，达到 31.4%。这显示了库和框架在软件开发中的广泛应用，它们为开发者提供了构建应用的基础设施和工具。
- Non Software（非软件）：绿色部分，占 23.2%。这一类别可能包括与软件直接开发不相关的项目，如文档、设计资源或其他非代码资产。
- Software Tools（软件工具）：红色部分，占 18.9%。这类工具可能包括编译器、调试器、版本控制系统等，它们是软件开发过程中不可或缺的辅助工具。
- System Software（系统软件）：紫色部分，占比最小，仅为 2.3%。这可能包括操作系统、驱动程序等，它们是计算机系统运行的基础，但在这个数据集中所占比例较小。

#### 6.1.2 不同项目类型 OpenRank 加总比例

![APP-Openrank-Propotion](https://hackmd.io/_uploads/HkpKM2QL1e.png)

图 6.2 不同项目类型 2024 年 OpenRank 加总比例

- 最大的变化，就是内容资源类型（Non Software）项目虽然在活跃项目的数量上占比较多，但其 2024 年的影响力相对较低；
- 而系统软件类型（System Software）虽然活跃项目数量上占比很少，但其 2024 年的影响力占比相对更多；软件工具类型（Software Tools）项目也有类似的现象；
- 组件框架类型和应用软件类型则没有太多变化，都是属于占比较多的类型。

#### 6.1.3 不同项目类型近 5 年 OpenRank 变化趋势

![App-Openrank](https://hackmd.io/_uploads/BkQMgA7U1e.png)

图 6.3 不同项目类型近 5 年 OpenRank 变化趋势

从上面的五年 OpenRank 演化图上可以看得出来，系统软件类型（System Software）的影响力逐年升高，软件工具（Software Tools）影响力在今年略有下降，库和框架（Libraries and Frameworks）、应用软件（Application Software）整体呈下降趋势，而内容资源类型（Non Software）项目的影响力比例是在逐年下降。

### 6.2 项目 Topic 分析

本节同样选取 GitHub OpenRank 排名前 10,000 的仓库数据进行分析，并获取仓库下的 Topic 标签进行深入洞察。

#### 6.2.1 热门 topic

![projectTopic-plot](https://hackmd.io/_uploads/SJijGnQIJg.png)

图 6.4 出现次数前十的 Topic

前十的主题涵盖了多个领域，反映了开源社区的广泛兴趣。其中，hacktoberfest 是 GitHub 上的一个开源活动，鼓励开发者贡献代码,以 1132 次的出现次数遥遥领先，显示诸多项目对开发者的欢迎。Python、JavaScript、TypeScript、Java 和 Rust 等 Topic 数量表现了这些语言受到了开源软件开发的青睐。此外，kubernets 和 machine-learning 等是在开源中具有较高关注度的 Topic。

#### 6.2.2 热门 Topic 的仓库总 OpenRank 趋势

![topicOpenrank-plot](https://hackmd.io/_uploads/SJUnzhQI1e.png)

图 6.5 出现次数前十的 Topic 下仓库的 OpenRank 变化 (2019 - 2023)

- 从 2020 至 2024 年，Hacktoberfest 的 OpenRank 显著增长，表现突出。Hacktoberfest 的目标是鼓励更多人参与开源项目，它反映了人们对于开源项目、社区参与和贡献的热情。
- Python 和 React 稳步上升，反映其流行度。JavaScript 和 TypeScript 增长稳定，显示前端以及应用开发的持续需求。
- Kubernetes 和 Machine Learning 增长，体现云和 AI 领域的发展。
- 其他如 Java、Rust、Android 增长平缓，显示成熟技术市场的稳定。

### 6.3 数据库领域项目分析

#### 6.3.1 数据库各子领域近五年增长趋势

![3-1](https://hackmd.io/_uploads/r1epGh7Ikx.png)

图 6.18 数据库各子领域 2020 - 2024 年 OpenRank 变化趋势

![3-2](https://hackmd.io/_uploads/SJDTz3mL1x.png)

图 6.18 数据库各子领域 2020 - 2024 年 活跃度变化趋势

- 数据库各子领域的发展相对平稳，在过去的五年中，关系型数据库独占鳌头。在 2024 年虽然发展相对放缓，但依然展现了足够的统治力
- 键值类型数据库在 2024 年的影响力与活跃度有所降低，并且在一定程度上被文档型数据库追平甚至有所超越。
- 文档行数据库在过去的发展中保持了稳定的上升。前三名的数据库子领域的两项指标累计均占数据库领域两项指标的 70% 以上。

#### 6.3.2 开源数据库项目 OpenRank 和活跃度 Top 10 变化趋势

![3.3](https://hackmd.io/_uploads/SyWjhh7Ikg.png)

图 6.20 开源数据库 领域 活跃度 Top 10 项目近 5 年变化趋势

![3.4](https://hackmd.io/_uploads/Byzsnn7I1e.png)

图 6.20 开源数据库 领域 OpenRank Top 10 项目近 5 年变化趋势

- ClickHouse 以其优秀的大数据处理能力稳居 2024 年活跃度以及影响力榜首。
- Apache 基金会相关两个项目进入 Top10，显示了其项目的卓越影响力以及 Apache 基金会在世界开源领域的重要地位。
- ydb 在 2023 年以来其各项指标有了明显的提升，期待其在 2025 的进一步发展。

#### 6.3.3 开源数据库项目工作活跃时间分析

此处将根据开源数据库项目 OpenRank Top 30 在 2024 全年中的事件按事件分布情况的打孔数据，观察项目的工作时间分布情况。

![box-plot](https://hackmd.io/_uploads/SkMCz2mIyg.png)

图 6.18 数据库开源项目工作时间箱型图

![violin-plot](https://hackmd.io/_uploads/Hka0M3mUkx.png)

图 6.18 数据库开源项目工作时间小提琴图

![Swarm-Plot](https://hackmd.io/_uploads/SyQJ7nXL1e.png)

图 6.18 数据库开源项目工作时间蜂巢图

![image](https://hackmd.io/_uploads/SyQpnU4Uyg.png)

图 6.18 数据库 OpenRank Top30 项目的平均工作时间分布打孔图

- 根据箱型图的时间分布数据可以看出，绝大多数的数据库项目的中位数工作时间都集中在 2-5 的时间段。活跃时间有同一性
- 根据小提琴图以及蜂巢图进行更细致的时间分析可以发现，在 2 时间段左右的时间中，数据库项目普遍最活跃。并且大部分项目都存在两个峰值工作时间，一个主峰一个次峰。可能与大部分数据库类型的项目都存在公司背景有关系。

#### 6.3.4 数据库子领域 OpenRank 榜单和活跃度 Top 10 榜单

表 6.3 数据库子领域 OpenRank 排行

| 排名 |   子领域名称    | OpenRank |
| :--: | :-------------: | :------: |
|  1   |   Relational    | 55635.51 |
|  2   |    Document     | 18384.45 |
|  3   |    Key-value    | 18376.55 |
|  4   |   Wide Column   | 11294.02 |
|  5   |  Search Engine  | 7589.15  |
|  6   |   Time Series   | 7120.22  |
|  7   |     Vector      | 5208.63  |
|  8   |      Graph      |  4281.4  |
|  9   | Object Oriented | 3557.65  |
|  10  |  Hierarchical   | 1036.42  |
|  11  |       RDF       |  433.08  |
|  12  |      Array      |  344.02  |
|  13  |      Event      |  281.65  |
|  14  |     Spatial     |  239.08  |
|  15  |    Columnar     |  228.52  |
|  16  |   Native XML    |  132.76  |
|  17  |     Content     |  25.65   |

表 6.3 数据库子领域 活跃度排行

| 排名 |   子领域名称    | activity  |
| :--: | :-------------: | :-------: |
|  1   |   Relational    | 165677.16 |
|  2   |    Document     | 57491.37  |
|  3   |    Key-value    | 56071.49  |
|  4   |   Wide Column   | 32835.39  |
|  5   |  Search Engine  | 24881.79  |
|  6   |   Time Series   | 22610.51  |
|  7   |     Vector      | 17463.42  |
|  8   |      Graph      |   13128   |
|  9   | Object Oriented | 10190.06  |
|  10  |  Hierarchical   |  3021.28  |
|  11  |       RDF       |  1405.37  |
|  12  |      Array      |  1009.34  |
|  13  |     Spatial     |  812.11   |
|  14  |      Event      |  735.62   |
|  15  |    Columnar     |  568.63   |
|  16  |   Native XML    |   549.4   |
|  17  |     Content     |   77.83   |

从数据库领域各子领域 2024 年的 OpenRank 和活跃度排行可以看出：

- Relational、Key-value、Document 在以上两项指标中都稳据前三，前三名的数据库子领域的两项指标累计均占数据库领域两项指标的 70% 以上；
- Relational 的各项指标超过了第二至第五名的总和，其两项指标均占数据库领域两项指标的 40% 以上，是一个超大子类。
- Columnar 作为新加入榜单的数据库项目发展势头迅猛
- 向量数据库在 2024 年也有了显著的提升。

### 6.4 生成式 AI 领域项目分析

在经历了新的一年的行业发展，生成式 AI 展现了新的发展样态。

#### 6.4.1 生成式 AI 各子领域近五年增长趋势

![3](https://hackmd.io/_uploads/SJJzQhQ81e.png)

图 6.18 生成式 AI 各子领域 2020 - 2024 年 OpenRank 变化趋势

![4](https://hackmd.io/_uploads/B1vfX3X81g.png)

图 6.19 生成式 AI 各子领域 2020 - 2024 年活跃度变化趋势

- 对于不同种类别的划分的分类分析，各类生成式 AI 项目的活跃度与影响力都出现了一定程度的回落。
- 工具类 AIGC 开源项目的影响力与活跃度均显著高于模型类和应用类
- 模型类项目影响力自 2022 年开始增长迅速，在 2023 年超过基础类，整体呈现上升趋势，代表着 2023 年是 AIGC 创新应用开发的大爆发之年，而 2024 年发展放缓，这可能体现了在过去一段时间中，生成式 AI 的发展相对趋于稳定。

#### 6.4.2 生成式 AI 领域项目 OpenRank 和活跃度 Top 10 变化趋势

![1](https://hackmd.io/_uploads/B1fX7hm8kg.png)

图 6.20 生成式 AI 领域 OpenRank Top 10 项目近 5 年变化趋势

![2](https://hackmd.io/_uploads/B1wXm3mUye.png)

图 6.21 生成式 AI 领域 活跃度 Top 10 项目近 5 年变化趋势

- vllm 影响力和活跃度双排名第一，备受开发者的关注；
- langchain 的影响力以及活跃度排名在新的一年有所回落，但是依然保持了相当高的排名。
- transformers 作为从问世以来的新时代 AI 的基石，在最新一年中依然保持了极高的关注度，面对新的诸如 mamba 等最新架构的挑战，transformer 依然是当下大模型 AI 的核心。
- stable-diffusion-webui 在 2023 年展现了非常强大的发展势头，曾被认为是 transformer 的有力挑战者，但其在 2024 年的各种指标的发展都有所降低，依然没有动摇 transformer 的地位。
- Langchain-Chatchat 作为一个本地部署的知识库，在 2024 年依然保持了稳定上升的发展态势。

#### 6.4.3 2024 年生成式 AI 领域项目 OpenRank 和活跃度 Top 10 榜单

表 6.3 生成式 AI 领域 OpenRank 度排行

| 排名 | 项目名称                          | OpenRank |
| ---- | --------------------------------- | -------- |
| 1    | vllm-project/vllm                 | 4611     |
| 2    | huggingface/transformers          | 4212.26  |
| 3    | langchain-ai/langchain            | 4292.13  |
| 4    | ggerganov/llama.cpp               | 3110.07  |
| 5    | run-llama/llama_index             | 2665.89  |
| 6    | milvus-io/milvus                  | 1955.52  |
| 7    | facebookincubator/velox           | 1641.14  |
| 8    | chatchat-space/Langchain-Chatchat | 1097.79  |
| 9    | microsoft/DeepSpeed               | 983.42   |
| 10   | invoke-ai/InvokeAI                | 971.2    |

表 6.4 生成式 AI 领域 活跃度排行

| 排名 | 项目名称                             | OpenRank |
| ---- | ------------------------------------ | -------- |
| 1    | vllm-project/vllm                    | 17556.02 |
| 2    | langchain-ai/langchain               | 16413.39 |
| 3    | huggingface/transformers             | 14454.74 |
| 4    | ggerganov/llama.cpp                  | 10599.61 |
| 5    | run-llama/llama_index                | 10272.5  |
| 6    | milvus-io/milvus                     | 6978.76  |
| 7    | facebookincubator/velox              | 4832.71  |
| 8    | chatchat-space/Langchain-Chatchat    | 4315.73  |
| 9    | AUTOMATIC1111/stable-diffusion-webui | 3782.55  |
| 10   | getcursor/cursor                     | 3579.97  |

## 7. 开发者洞察

### 7.1 开发者的地区分布

#### 7.1.1 GitHub 活跃开发者地理分布

![image](https://github.com/user-attachments/assets/668c90c4-f668-4430-bc1b-a7474eebd99d)

图 7-1 2024 全球开发者分布图

![image](https://github.com/user-attachments/assets/f28d26f5-07f0-47a6-a571-b18b6252d241)

图 7-2 2024 中国开发者分布图

#### 7.1.2 GitHub 活跃开发者国家 / 地区分布

![image](https://github.com/user-attachments/assets/bb313a67-eaf5-4fb4-a6ab-580267f0d2a8)

图 7-3 2024 全球 GitHub 活跃开发者国家 / 地区分布图

表 7-1 2024 全球活跃开发者数量国家 / 地区排名

| 排名 | 国家           | 活跃数量 |
| ---- | -------------- | -------- |
| 1    | United States  | 435,202  |
| 2    | India          | 252,054  |
| 3    | China          | 184,085  |
| 4    | Brazil         | 174,811  |
| 5    | Germany        | 126,397  |
| 6    | United Kingdom | 103,061  |
| 7    | Canada         | 82,627   |
| 8    | France         | 78,288   |
| 9    | Russia         | 60,735   |
| 10   | South Korea    | 44,006   |

![image](https://github.com/user-attachments/assets/dc407c46-92ad-4209-b64d-851f66869b0e)

图 7-4 2024 中国 GitHub 活跃开发者地区分布图

表 7-2 2024 中国活跃开发者数量地区排名

| 排名 | 省份 / 地区 | 数量   |
| ---- | ----------- | ------ |
| 1    | 北京        | 38,323 |
| 2    | 上海        | 28,393 |
| 3    | 广东        | 24,959 |
| 4    | 台湾        | 15,894 |
| 5    | 浙江        | 15,816 |
| 6    | 江苏        | 9,369  |
| 7    | 四川        | 8,186  |
| 8    | 香港        | 6,625  |
| 9    | 湖北        | 5,732  |
| 10   | 陕西        | 3,669  |

### 7.2 开发者工作时间分析

#### 7.2.1 全域开发者工作时间分布

![image](https://github.com/user-attachments/assets/a87be22b-c8f0-444b-ad13-1f92e20761e8)

图 7-5 GitHub 全域开发者工作时间分布

![image](https://github.com/user-attachments/assets/6bcd76ea-6205-4582-b54a-e76943080666)

图 7-6 Gitee 全域开发者工作时间分布

![image](https://github.com/user-attachments/assets/e371f8d0-a841-46d6-84f0-9c11dfb4daaa)

图 7-7 除去机器人的全域开发者时间分布

#### 7.2.2 项目工作时间分布

##### 全球 GitHub 仓库 OpenRank 前四名工作时间分布

1. [NixOS/nixpkgs](https://github.com/NixOS/nixpkgs)

    ![image](https://github.com/user-attachments/assets/0d99a62a-c89c-49f5-98bc-73cd1d35c872)

1. [llvm/llvm-project](https://github.com/llvm/llvm-project)

    ![image](https://github.com/user-attachments/assets/c303f4b5-6841-4e0e-b22f-cc96859da22e)

1. [home-assistant/core](https://github.com/home-assistant/core)

    ![image](https://github.com/user-attachments/assets/6eb34367-dffe-4e65-8692-4a68acd8a792)

1. [pytorch/pytorch](https://github.com/pytorch/pytorch)

    ![image](https://github.com/user-attachments/assets/27d72c73-6256-4b93-a0b2-fcc1c3cb233f)

##### 中国仓库 OpenRank 前四名工作时间分布

1. openharmony

    ![image](https://github.com/user-attachments/assets/a52ef9e3-6fbb-4a8e-a19c-402c9e0f00e9)

1. DaoCloud

    ![image](https://github.com/user-attachments/assets/e98237a7-5e42-4f46-8217-8db6fcde95b4)

1. PaddlePaddle

    ![image](https://github.com/user-attachments/assets/ddc2dab7-afba-4ead-b785-951beafe7105)

1. doris

    ![image](https://github.com/user-attachments/assets/1c333de4-198a-4411-bed1-458c72763852)

### 7.3 开发者角色分析

#### 7.3.1 2024 年各角色数量分布

表 7-3 OpenRank 排名前 10 项目各开发者角色数量分布

| 仓库名                                   | 探索者 | 参与者 | 贡献者 | 提交者 |
| ---------------------------------------- | ------ | ------ | ------ | ------ |
| NixOS/nixpkgs                            | 4897   | 3606   | 4339   | 3484   |
| llvm/llvm-project                        | 6789   | 3241   | 2365   | 2092   |
| home-assistant/core                      | 10596  | 7472   | 1300   | 989    |
| pytorch/pytorch                          | 12513  | 2599   | 1424   | 823    |
| digitalinnovationone/dio-lab-open-source | 3813   | 4462   | 21276  | 224    |
| odoo/odoo                                | 7659   | 650    | 1035   | 661    |
| microsoft/vscode                         | 14701  | 12522  | 579    | 388    |
| DigitalPlatDev/FreeDomain                | 32967  | 35332  | 3      | 0      |
| zephyrproject-rtos/zephyr                | 2314   | 1054   | 1276   | 1120   |
| godotengine/godot                        | 15208  | 3314   | 1072   | 678    |

![image](https://github.com/user-attachments/assets/690532aa-401f-4ac5-abf9-1d910b5e09bd)

图 7-5 开发者角色分布图

#### 7.3.2 2024 年各角色新增情况

表 7-4 OpenRank 排名前 10 项目新增开发者角色数量分布

| 仓库名                                   | 新增探索者 | 新增参与者 | 新增贡献者 | 新增提交者 |
| ---------------------------------------- | ---------- | ---------- | ---------- | ---------- |
| NixOS/nixpkgs                            | 4836       | 2392       | 2187       | 1605       |
| llvm/llvm-project                        | 6689       | 2191       | 1517       | 1223       |
| home-assistant/core                      | 10483      | 5502       | 819        | 565        |
| pytorch/pytorch                          | 12321      | 1938       | 946        | 496        |
| digitalinnovationone/dio-lab-open-source | 3809       | 4455       | 21254      | 224        |
| odoo/odoo                                | 7559       | 445        | 467        | 239        |
| microsoft/vscode                         | 14416      | 10614      | 450        | 312        |
| DigitalPlatDev/FreeDomain                | 32967      | 35332      | 3          | 0          |
| zephyrproject-rtos/zephyr                | 2278       | 687        | 690        | 554        |
| godotengine/godot                        | 14774      | 2216       | 738        | 445        |

![image](https://github.com/user-attachments/assets/4ba2b6c2-608b-4a9d-8546-a0c7f15e3992)

图 7-6 2024 年开源社区角色新增图

#### 7.3.3 开发者演化视角

表 7-5 OpenRank 排名前 10 项目角色转化数量分布

| 仓库名                                   | 贡献者 -> 提交者 | 参与者 -> 贡献者 | 探索者 -> 参与者 |
| ---------------------------------------- | ---------------- | ---------------- | ---------------- |
| NixOS/nixpkgs                            | 287              | 188              | 204              |
| llvm/llvm-project                        | 134              | 289              | 185              |
| home-assistant/core                      | 66               | 103              | 155              |
| pytorch/pytorch                          | 82               | 78               | 168              |
| digitalinnovationone/dio-lab-open-source | 0                | 21               | 3                |
| odoo/odoo                                | 48               | 33               | 28               |
| microsoft/vscode                         | 23               | 50               | 272              |
| DigitalPlatDev/FreeDomain                | 0                | 0                | 0                |
| zephyrproject-rtos/zephyr                | 62               | 45               | 46               |
| godotengine/godot                        | 67               | 115              | 242              |

![image](https://github.com/user-attachments/assets/6c544916-a765-4b69-89a8-44c1db18f68a)

图 7-7 开发者角色演化图

## 8. 商业开源洞察

### 8.1 商业开源的定义与特征

商业开源是指企业在开源软件的基础上，通过提供增值服务、技术支持、定制化解决方案等方式实现商业化盈利的一种模式。商业开源是通过更多人的参与，减少软件的缺陷，丰富软件的功能，同时也避免了少数人在软件里留一些不正当的后门。企业通过开源的商业模式可以直接获得经济利润，开源软件最终还会反哺商业，让商业公司为用户提供更好的产品。它与传统开源的核心区别是传统开源主要是为了促进软件的自由使用、修改和分发，往往由社区驱动来推动技术进步。但商业开源虽然也遵循开源的原则，但主要目的还是为了盈利。

### 8.2 商业开源的发展历程

**全球商业开源发展历程：**

![3301735793780_.pic](https://hackmd.io/_uploads/ByHMC5XLyl.jpg)

**中国商业开源发展历程：**
![3321735794278_.pic](https://hackmd.io/_uploads/rkw5C5X8ke.jpg)

### 8.3 商业开源融资阶段分析

我们收集并分析了从天使投资（Angel）到私募股权（Private Equity Round）等多个融资阶段的数据，下表显示了融资金额前 10 的各个融资阶段情况。B 阶段以 8819.80 万美元的融资金额位居首位，这可能表明 B 阶段的公司已经过了初创期，正在快速成长，需要更多资金来扩大市场份额或进行产品开发。而 Growth 阶段以 3493 万美元位居第五，这表明一公司可能在特定成长阶段需要大量资金来加速增长。

表 8-1 融资金额前 10 的各个融资阶段情况

| 阶段   | 总融资金额 |
| ------ | ---------- |
| B      | 8819.7980  |
| C      | 7073.0600  |
| A      | 5809.2530  |
| D      | 5720.3000  |
| Growth | 3493.0000  |
| E      | 2683.4000  |
| Seed   | 2371.3043  |
| F      | 1889.0000  |
| G      | 1870.0000  |
| H      | 1600.0000  |

我们可以看出在早期阶段（如 A、Seed）的资金需求相对较小，而成长阶段（如 B、C）的资金需求较大。同时这也表明市场对成熟初创企业的投资热情较高。

### 8.4 商业开源时间趋势分析

我们首先分析融资总额趋势，发现从 2016 年到 2021 年融资总额呈现逐年增长的趋势，特别是在 2021 年，融资总额达到了 16296.2230，是近年来的最高点。而 2022 年和 2023 年融资总额有所下降，但仍然保持在较高水平。
![时间趋势](https://hackmd.io/_uploads/BkVboimI1g.png)

融资事件数量从 2016 年到 2019 年逐年增加，这表明市场活跃度在提升。2020 年和 2021 年融资事件数量达到高峰，分别为 195 和 309，显示出市场的高活跃度。同样融资事件数量在 2022 年和 2023 年融资事件数量有所下降。
![时间事件数趋势](https://hackmd.io/_uploads/S12Wio7Ikl.png)

## 9. 高校开源洞察

[2024 开源之夏 OSPP](https://summer-ospp.ac.cn/)作为高校与开源社区深度互动的重要平台，在本年度取得了显著成果，有效促进了开源技术的发展与高校人才培养。2024 开源之夏活动为高校学生提供了一个展示才华和实践技能的平台，同时也为开源社区带来了新的活力和创新。通过本次活动，学生们不仅提升了自己的技术能力，还为开源项目的发展做出了实质性的贡献。而从首届 OSPP 开始，X-lab 开放实验室便深度参与其中，本年度便针对 OSPP 2024 年的相关数据进行如下介绍性分析。

### 9.1 OSPP 基本宏观情况分析

- **OSPP 2024 基本情况** ：本次 OSPP 汇聚了来自多个领域的 168 个开源社区，包括但不限于操作系统、编程语言、人工智能等各个领域。这些社区为学生提供了丰富的项目资源，涵盖了从基础软件架构搭建到前沿技术应用探索等不同层次的开发任务，促进了开源技术在高校范围内的广泛传播与交流，拓宽了学生的技术视野。如图 9.1 所示，来自全球不同高校的 2537 名学生上线了共 561 个开源项目，并最终顺利结项了 455 个优秀项目。

![总览](https://hackmd.io/_uploads/ByFnqOE8kg.png)

图 9.1 活动参与情况总览

- **社区数量** ：从首届 OSPP 起，每年参与活动的社区数量呈现出令人瞩目的增长态势。至 2024 年，社区数量飙升至 168 个，较 2023 年实现了大幅增长，取得了第二高的增长幅度（仅次于首届 OSPP 至第二届的增长幅度）。这种增长趋势主要归因于多个因素。一方面，开源理念在全球范围内的认可度不断攀升，越来越多的开发者和项目团队意识到开源协作的强大力量，积极投身于开源社区建设，这使得开源社区的基数持续扩大，进而吸引了更多社区参与到 OSPP 活动中。另一方面，高校对于开源教育的重视程度与日俱增，纷纷加强与开源社区的合作，为学生提供实践平台。众多高校的积极参与为 OSPP 注入了源源不断的活力，促使更多社区看到了与高校人才对接的巨大潜力，从而踊跃加入。此外，OSPP 自身在组织管理、项目匹配机制以及宣传推广等方面不断优化完善，提升了活动的影响力和吸引力，也成为社区数量增长的重要推动力量。
- **学生与高校数量** ：在过往的发展历程中，OSPP 的学生参与数量和高校参与数量呈现出类似的变化轨迹。从 2020 年至 2023 年期间，学生参与数量处于平稳上升的通道，这得益于开源文化在高校的逐步渗透以及 OSPP 活动影响力的持续扩散，越来越多的学生意识到参与开源项目对于自身技术能力提升和实践经验积累的重要性，积极投身其中。然而，在 2024 年，学生参与数量出现了略微降低的情况，降至 2537 人。这可能是由于本年度项目难度和要求的适度调整，以及同期其他类似开源活动竞争导致部分潜在参与者分流的影响。而关于高校参与数量的变化，自活动开展以来，其与学生数量的变化情况基本相同。即从 2020 年至 2023 年期间平稳上升，而在 2024 年略有下降，其原因与学生数量的变化原因大致相同。
- **项目数量** ：在 2024 年的 OSPP 活动中，项目的结项率都取得了显著的增长成绩。得益于开源社区的不断壮大与丰富多样的需求，虽然今年参与 OSPP 的总人数略有下降，但项目数量仍达到了 561 个，展现出蓬勃的发展活力。随着开源理念在技术领域的深入渗透，各个社区积累了大量亟待解决的实际问题与创新方向，从而催生了更多具有挑战性和价值性的项目提案。同时，高校与社区之间的合作愈发紧密，双方积极沟通协调，基于对学生能力与兴趣的深入了解，共同精心策划并拓展了项目范畴，使得项目数量得以保持。而在结项方面，455 个项目成功结项，结项率高达 81%。这一出色的结项率归因于多方面因素。首先，活动组织方在项目管理流程上进行了优化，在项目启动初期，为学生和导师提供了更为详细且具有针对性的指导手册与培训课程，涵盖从项目规划到技术难点攻克等各个环节，确保双方明确目标与路径，有效提升了项目执行的效率和质量。其次，社区导师在本年度发挥了更为积极关键的作用，他们不仅在技术上给予学生专业的指导，还在时间管理、团队协作等方面提供了宝贵的经验分享，帮助学生合理安排进度、解决团队内可能出现的问题，有力推动项目顺利推进。再者，学生自身对于开源项目的重视程度和投入度持续增加，经过前期的经验积累和技术沉淀，他们在面对项目任务时具备了更强的应对能力和创新思维，能够高效地完成项目开发工作，从而使得结项率实现了显著的提升，为 2024 年 OSPP 活动交上了一份令人满意的答卷。

### 9.2 OSPP 年度学生高校相关分布情况分析

- **高校地理分布** ：本次活动得到了众多高校的支持和参与，共有来自全球 498 所高校的学生参与了项目。这些高校分布在全国各个地区，涵盖了综合性大学、理工科院校、师范院校等不同类型的高校。本届开源之夏活动中全球参与高校的地理分布情况如图 9.2 所示，与 2023 年的分布情况对比如表 9.1 所示。2023 年，参与的高校总数为 592 所，其中国内高校 489 所，国外高校 103 所，国外高校占比 17.4%。而到了 2024 年，高校总数降至 498 所，国内高校数量相应减少至 399 所，国外高校数量为 99 所，但国外高校占比略有上升，达到 19.9%。这一变化表明，尽管高校参与的总体规模有所收缩，但国际交流在其中的相对比重有所增加。可能的原因在于，一方面，全球教育资源在开源领域的布局出现了调整，部分高校可能由于自身发展战略或资源配置的变化，调整了在 OSPP 项目中的参与度。另一方面，随着 OSPP 国际影响力的提升，吸引了更多国外高校的关注，虽然绝对数量有所波动，但在相对占比上体现出国际合作的深化趋势，这对于促进全球范围内的开源技术交流与人才培养的国际化融合具有重要意义，也预示着 OSPP 在未来的发展中，国际合作将成为一个重要的增长方向和特色亮点。

    ![高校](https://hackmd.io/_uploads/ryIa9_EIJl.png)

    图 9.2 OSPP 2024 参与高校分布情况

    表 9.1 OSPP 2023 至 2024 国内外高校分布变化情况

    | OSPP 年份 | 高校总数 | 国内高校总数 | 国外高校总数 | 国外高校占比 |
    | --------- | -------- | ------------ | ------------ | ------------ |
    | 2023      | 592      | 489          | 103          | 17.4%        |
    | 2024      | 498      | 399          | 99           | 19.9%        |

- **学生学历分布** ：OSPP 2024 参与学生的学历分布情况如图 9.3 所示，与 2023 年的对比情况如表 9.2 所示。可以看到除了来自中国的大量优秀学生，还有来自全球各个国家的众多学生参与其中。而所有学生中参与的主力为本科生与硕士生，少部分为博士生。具体分析而言，对比 2023 年与 2024 年 OSPP 学生学历分布情况可知，整体格局虽保持相对稳定，但仍存在细微变化。

    在 2023 年，学生总数为 3475 人，其中本科 / 专科在读学生占比 57%，硕士在读学生占 41%，博士在读学生占 2%。而 2024 年学生总数降至 2537 人，本科 / 专科在读占比微降至 56%，硕士在读占比上升至 42%，博士在读占比依旧维持在 2%。从数据变化来看，学生总数的减少可能与多种因素相关，如当年活动宣传覆盖范围的波动、同期其他开源项目竞争吸引部分潜在参与者等。在学历结构方面，硕士在读学生占比的提升，反映出开源项目对具有更高专业知识水平和研究能力学生的吸引力在增强，或许是因为项目难度和深度的适度增加，使得硕士研究生在项目实践中更具优势，进而参与度有所上升。本科 / 专科在读学生占比的略微下降，可能暗示着这一群体在面对项目资源竞争或学业与开源项目平衡时，部分学生做出了不同选择。博士在读学生占比稳定，表明在当前 OSPP 项目设置下，该群体的参与度已趋于饱和，项目尚未出现大幅改变其参与热情的因素。总体而言，学历分布的变化体现了 OSPP 项目在不同学历层次学生间的动态发展态势处于一个稳定的状态中，其面向的主要群体仍是本科或硕士阶段的学生。

    ![学生分布](https://hackmd.io/_uploads/S1DAcuNIyg.png)

    图 9.3 OSPP 2024 参与学生学历分布情况

    表 9.2 OSPP 2023 至 2024 参与学生学历分布变化情况

    | OSPP 年份 | 学生总数 | 本科/专科在读占比 | 硕士在读占比 | 博士在读占比 |
    | --------- | -------- | ----------------- | ------------ | ------------ |
    | 2023      | 3475     | 57%               | 41%          | 2%           |
    | 2024      | 2537     | 56%               | 42%          | 2%           |

### 9.3 OSPP 年度项目结项情况分析

OSPP 吸引了众多高校学生参与，旨在通过开源项目实践提升学生的技术能力与协作水平，并为开源社区注入创新活力。活动期间，学生与社区导师紧密合作，共同推进各类开源项目的进展。经严格评审与开发过程，众多项目成功结项，成果涵盖功能优化、性能提升、新特性开发等多个方面，切实解决了开源社区中的部分技术问题与需求，部分成果已被社区纳入主分支代码库，对开源项目的稳定发展提供了有力支持，体现了高校学生在开源实践中的专业能力与创新思维。本届 OSPP 项目的结项情况如图 9.4 所示，可以看到绝大多数项目均顺利完成了结项流程，且其中大部分为复杂度更高的进阶项目；而与 2023 年结项情况的对比如表 9.3 所示。2023 年项目上线数目为 593 个，成功结项的有 418 个，结项占比达 70.5%，其中进阶项目占比 65%。而到了 2024 年，虽然项目上线数目略有减少至 561 个，但结项数目却提升至 455 个，结项占比大幅增长至 81.1%，进阶项目占比也上升至 67%。
这种变化反映出多方面的积极进展。首先，结项占比的显著提升表明项目管理与执行效率在 2024 年得到了有效增强。这得益于活动组织方在项目流程优化方面所做的努力，例如为学生和导师提供了更为完善的指导手册与培训课程，加强了项目过程中的监督与反馈机制，使得项目在推进过程中遇到的问题能够及时得到解决，从而提高了项目的成功率。其次，进阶项目占比的上升意味着项目的难度与深度有所增加，且学生和导师在应对这些挑战时表现出了更强的能力与协作精神。这可能是由于开源社区经过多年发展，对项目的质量和创新性提出了更高要求，同时也反映出参与学生和导师在专业技能和实践经验方面的积累与提升，使得他们能够更好地应对更具挑战性的项目任务。总之，尽管 2024 年项目上线数目稍有减少，但整体结项情况的大幅改善显示出 OSPP 活动在项目运作和人才培养方面正朝着更加高效、优质的方向发展，为开源社区的持续发展提供了更有力的支持。

![2](https://hackmd.io/_uploads/BySyjdNL1l.png)

图 9.4 OSPP 2024 结项数目数量分布情况

表 9.3 OSPP 2023 至 2024 结项数目数量分布变化情况

| OSPP 年份 | 项目上线数目 | 结项数目 | 结项占比 | 进阶项目占比 |
| --------- | ------------ | -------- | -------- | ------------ |
| 2023      | 593          | 418      | 70.5%    | 65%          |
| 2024      | 561          | 455      | 81.1%    | 67%          |

### 9.4 OSPP 年度贡献度情况分析

在上述统计数据的基础上，我们结合 OSPP 近两年全年的贡献度数据和社区 OpenRank 算法对各参与高校以及参与到各社区学生的贡献度进行了详细的分析。

#### 9.4.1 高校贡献度

通过 OpenRank 算法计算得出的高校贡献度年度排行榜如图 9.5 和图 9.6 所示，其中图 9.5 展示了 OSPP 2023 中贡献最为突出的二十所高校，而图 9.6 则展示了 OSPP 2024 所对应的高校排行榜。

在 2023 年的排行榜中，华中科技大学以 OpenRank 值 67.3 位居榜首，参与学生数目为 21 人，人均 OpenRank 为 3.21。浙江大学和北京邮电大学分别位列第二和第三，OpenRank 值分别为 61.23 和 60.19。可以看出，这些高校在 OSPP 中的整体贡献度较高，而其中华中科技大学虽然参与学生数目不是最多，但人均 OpenRank 表现出色，使其拥有了最高的总 OpenRank 值，说明了该校学生该年度的参与热情相当突出。另一方面，复旦大学、陇东学院、武汉大学、成都信息工程大学等高校虽然在学生数量上并不占优，但因为个别学生的贡献度较高而使得最终的排名较高。

而在 2024 年的排行榜中，西安邮电大学以 OpenRank 值 85.13 跃居第一，参与学生数目为 15 人，人均 OpenRank 为 5.68，西安邮电大学在 2024 年的表现尤为突出，不仅 OpenRank 值大幅提升，且参与学生数目也较为可观，其人均 OpenRank 也较高，说明该校在 OSPP 中的综合贡献度有显著提升。陇东学院以 OpenRank 值 61.37 位列第二，不过其参与学生数目仅为 1 人，人均 OpenRank 高达 61.37。陇东学院在 2024 年的表现极具特色，虽然只有一名学生参与 OSPP 项目，但该学生的贡献度极高，使其在排行榜上占据重要位置，这种情况可能是由于该校该名学生在特定项目中具备独特的技术优势或创新能力，能够独立完成具有高价值的项目任务。类似地，上海大学以 OpenRank 值 42.21 位列第三，其同样也只有两名学生参与活动。

- **OSPP 2023 年度高校贡献度排行榜**：

    ![2023高校](https://hackmd.io/_uploads/SJKbxU_8Jg.png)

    图 9.5 OSPP 2023 年度高校贡献度排行榜

- **OSPP 2024 年度高校贡献度排行榜**：

    ![2024高校](https://hackmd.io/_uploads/BkbMlLOUyg.png)

    图 9.6 OSPP 2024 年度高校贡献度排行榜

对比 2023 年和 2024 年的高校贡献度排行榜，我们从排名与贡献度等多个角度对榜单的变化情况进行了进一步分析。

首先在排名变化方面，显著上升的高校有西安邮电大学和陇东学院。前者从 2023 年的第六名上升到 2024 年的第一名，实现了巨大的跨越。这种排名的提升反映了该校在开源项目实践方面的快速发展和积极进取。在这一年间，西安邮电大学可能在项目资源整合、学生激励机制、技术指导等方面采取了有效的措施，从而显著提升了学生在 OSPP 项目中的参与度和贡献度；而后者从 2023 年的第十二名上升到 2024 年的第二名，其排名上升幅度同样令人瞩目。该校在 2024 年虽然只有一名学生参与项目，但该学生取得了极高的贡献度，这可能是学校在特定技术领域培养出了具有突出能力的学生，或者该学生在项目中发现了独特的切入点，从而实现了高价值的项目成果。

而在贡献度变化方面，部分高校在总 OpenRank 值上有较大幅度的提升，例如西安邮电大学和陇东学院。西安邮电大学从 2023 年的 55.67 提升到 2024 年的 85.13，陇东学院从 39.48 提升到 61.37。这种提升表明这些高校在 OSPP 项目中的整体实力和影响力在增强，可能是通过优化项目管理流程、加强与开源社区的合作、提高学生技术水平等方式实现的。而在人均 OpenRank 值上，陇东学院在 2024 年的人均 OpenRank 高达 61.37，与 2023 年相比有了更进一步的飞跃，主要原因是 2024 年该校仍然只有一名高贡献度的学生参与项目，而该学生在去年的基础上取得了更进一步的成果。而其他高校如华中科技大学和北京邮电大学的人均 OpenRank 则有所下降，这反映了在竞争加剧的情况下，这些高校在提升学生个体贡献度方面面临一定的挑战，需要进一步优化项目参与机制和学生培养模式，以提高人均贡献水平。

总而言之，从 2023 年到 2024 年，各高校在 OSPP 中的贡献度发生了显著的动态变化。这种变化反映了高校在开源项目实践中的不断探索和竞争态势，也为各高校进一步优化开源项目参与策略、提升学生实践能力和创新精神提供了有价值的参考依据。

#### 9.4.2 学生贡献度

在 OSPP 项目中，学生的贡献度对于项目的发展以及开源社区的繁荣至关重要。通过社区 OpenRank 算法对各参与高校学生的贡献度进行量化分析，能够清晰地展现学生在不同社区中的表现情况，以下我们将对 OSPP 2023 和 2024 的学生贡献度排行榜数据及其变化情况展开详细分析。

在两近年的学生贡献度排行榜中，学生来自多所高校。其中，复旦大学、上海交通大学、陇东学院等学校的学生在排行榜前列。这表明不同层次和类型的高校都有学生积极参与 OSPP 项目，但顶尖高校和在相关专业有优势的高校在高贡献度学生数量上可能相对较多。从参与的社区来看，学生参与的开源社区十分多样化。涵盖了诸如 Apache Hadoop、MatrixOne、Spring Cloud Alibaba 等不同类型的社区。这反映出 OSPP 项目覆盖了广泛的技术领域，为学生提供了在不同方向上进行开源实践的机会。

整体来看 2023 年的学生贡献度排行榜，可以发现学生的贡献度有一定的集中趋势。排名靠前的少数学生的 OpenRank 值相对较高，与后面学生的差距较为明显。这可能意味着在开源项目中，存在部分学生能够更深入地参与并做出显著贡献，而大部分学生的贡献度相对较为平均或者较低。具体到前列的同学来看，王同学在 2023 年的学生贡献度排名中位居榜首。来自复旦大学的他在 Apache Hadoop 社区取得了显著的贡献。王同学能够在这样的社区取得高 OpenRank 值，很可能是因为他在项目开发、代码优化或者社区问题解决等方面表现突出，以及复旦大学在计算机科学等相关领域有着深厚的学术底蕴。类似地，来自上海交通大学的潘同学以44.955的 OpenRank 值位列第二，这也得益于上海交通大学在工程和计算机领域的强劲实力，其学术资源和科研氛围有助于学生参与开源项目。

2024 年的排行榜上，学校分布出现了一些变化。陇东学院、上海大学、西安财经大学等学校的学生进入了前列。这显示出在开源项目中，并非只有传统的优势高校学生能够取得高贡献度，一些相对不那么知名的高校学生如果有足够的能力和投入，也能在排行榜上崭露头角。在参与社区方面，与 2023 年类似，学生参与的社区依旧多样。不过，在一些特定社区中，如 Spring Cloud Alibaba、MindSpore 等，学生的贡献度有显著提升，这可能与这些社区在 2024 年的项目需求、发展方向以及学生对相关技术的兴趣增长有关。另一方面，2024 年的贡献度集中程度有所变化。虽然仍有部分学生的 OpenRank 值较高，但整体的差距相较于 2023 年有缩小的趋势。这可能是由于随着 OSPP 项目的推广和发展，更多学生掌握了有效的开源项目参与方法，提高了自身的贡献度，使得高贡献度学生之间的竞争更加激烈。另一方面，具体到最前列的学生来看，来自陇东学院的姬同学在去年的基础上更进一步，不仅取得了更高的 OpenRank 值，还在总排名上进步到了第一名，超越了众多来自知名高校的同学。以姬同学为代表的参加了多届 OSPP 的学生在今年所取得的突出表现，也体现出了 OSPP 这类活动对在校学生提升开源相关技能、参与开源贡献的有力帮助，其不仅为来自世界各地不同层次高校的同学积累了开发经验，还为相关的开源社区注入了宝贵的新鲜血液。

- **OSPP 2023 年度学生贡献度排行榜**：

    ![2023学生](https://hackmd.io/_uploads/BJoflLOL1g.png)

    图 9.7 OSPP 2023 年度学生贡献度排行榜

- **OSPP 2024 年度学生贡献度排行榜**：

    ![2024学生](https://hackmd.io/_uploads/HyBQgIuUkl.png)

    图 9.8 OSPP 2024 年度学生贡献度排行榜

通过对 OSPP 2023 和 2024 年学生贡献度数据的分析，可以看出学生在开源项目中的贡献度是动态变化的。不同高校的学生都有机会在开源社区中取得突出成绩，个人努力、学校资源和社区环境等因素都会影响学生的贡献度。而在未来的 OSPP 项目中，学生们可以借鉴这些经验，不断提升自己在开源项目中的参与度和贡献度，同时高校和开源社区也可以根据这些数据进一步优化资源配置和项目支持，以促进开源项目的更好发展。
