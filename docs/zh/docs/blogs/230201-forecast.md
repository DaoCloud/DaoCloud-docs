# 2023 年云原生预测

![头图](./images/forecast01.png)

> 作者：Chris Aniszczyk

我希望每个人都和心爱的人度过了愉快的假期！CNCF 最近发布了关于我们去年完成的所有工作的[年度报告](https://www.cncf.io/reports/cncf-annual-report-2022/)。
我建议每个人都抽空仔细阅读这份报告，因为我们花了很多时间来记录社区所做的所有令人惊叹的工作。另外，自从我发布年度预测已经有几年了，所以我为延迟道歉，希望你喜欢今年的清单！

## 云原生 IDE 成为常态

最近，GitHub Codespaces 完成测试阶段，虽然我们没有很多来自 GitHub 的公共使用数据，
但 Twitter 上似乎有很多正面情绪。此外，GitPod 与该领域的其他公司一起完成了首轮融资，这些公司已经进行了令人印象深刻的融资。

我 100% 相信，短暂的开发工作区以及开发人员在设置工作区时节省的时间，将推动这项技术成为行业规范。
你看到 Uber、Shopify、Slack、Stripe 等公司使用这种形式的开发是有原因的，随着 Codespace 和 Gitpod
等产品成为常态，这些最佳实践将传播到行业的其他地方。

最后，Gitpod 整理了一套优秀的 [CDE3（Cloud Develompent Environment，云开发环境）](https://www.gitpod.io/cde)原则，
我建议你看看。Redmonk 的优秀员工也分享了我的观点，他们发表了关于“[云开发环境之年](https://redmonk.com/jgovernor/2022/12/01/the-year-of-the-cloud-development-environment/)”的精彩文章，我建议从分析师的角度阅读。

## FinOps 成为主流并向左移

几年前，Linux 基金会帮助建立了 [FinOps 基金会](https://www.finops.org/blog/linux-foundation)，
以培养这一领域的创新。FinOps 基金会有了一个很好的开始，从主办第一次 [FinOpsX](https://x.finops.org/)
会议到发起 [FinOps 状况调查](https://data.finops.org/)，以及一些很棒的[介绍材料](https://www.edx.org/course/introduction-to-finops)。

为什么今年对 FinOps 来说是重要的一年？云支出在过去几年中大幅增加，正在成为组织内的一项大成本，有时甚至与工资不相上下。

此外，你可以将 FinOps 的就业趋势与 [Google 的趋势](https://trends.google.com/trends/explore?date=today%205-y&q=finops)结合起来，寻找经济增长已经到达拐点的指标。

所有这些市场压力的另一个好处是更多的标准化和开源选项，如 [OpenCost](https://www.opencost.io/)。
传统上，破解云账单是一个困难的问题，如果你使用多个云，这个问题会变得更加复杂（没有涵盖所有主要云的云定价和成本管理的开放标准）。

这些市场压力加上全球经济衰退将增加大多数组织的 FinOps 实践，而不仅仅是高科技海湾地区的公司。
与过去相比，FinOps 将成为一个更大的工程问题，在过去，工程团队可以自由支配云消费。
你将看到 FinOps 信息向开发者转移，并最终成为 pull request 基础设施的一部分。

最后，成本管理和 FinOps 将默认成为可观察性解决方案的一部分（例如，Datadog
宣布推出[成本管理产品](https://www.datadoghq.com/about/latest-news/press-releases/datadog-introduces-cloud-cost-management/)）。
我预计这一领域也会出现大量整合，大型传统公司会通过收购进入该领域。

## 开源 SBOM 无处不在

美国政府在过去几年中制定了有关提高软件安全性的政策和法律，从 2021 年的行政命令到最近的“美国保护开源软件法案”，
涵盖了无数的安全改进。OpenSSF（Open Source Security Foundation，开源安全基金会）对该法案有一个很好的总结，
以及他们关于如何解决开源安全问题的[动员计划](https://openssf.org/oss-security-mobilization-plan/)。

此外，就在最近，美国政府通过了一项法律，强制要求医疗器械制造商必须生产 SBOM。

不可避免的是，这种趋势将继续下去，并影响开源软件，像 Kubernetes 这样的领先关键项目已经在生产供消费的 SBOM。
在所有行业强制推行 SBOM 的道路上可能会有一些坎坷，但我个人认为，通过监管或行业刚好成熟，这是不可避免的。

这一领域还将有许多新的开源创新、初创公司和项目，它们致力于聚合大量这种安全信息（参见 https://deps.dev 作为一个简单的示例）。
我个人关注的项目有 [GUAC](https://github.com/guacsec/guac)、[Scorecard](https://github.com/ossf/scorecard)、
[Sigstore](https://www.sigstore.dev/)、[Witness](https://github.com/testifysec/witness) 等等。

## GreenOps 合并到 FinOps

永续发展是一个热门话题，ESG 领域的人员都知道计算基于云的工作负载的碳足迹有多复杂。普华永道最近的[研究](https://www.pwc.com/us/en/tech-effect/cloud/esg.html)发现，
“财富 1000 强企业中，60% 的企业领导者正在使用或计划使用云来增强 ESG 报告，59%的企业领导者正在使用或计划使用云来改善其 ESG 战略。”

我相信，在我们提高云的效率时，这里会出现一种杰文斯悖论的情况……此外，有趣的研究表明，“未来运行全球自动驾驶汽车车队的计算机所需的能源可能会产生与当今世界所有数据中心一样多的温室气体排放。”

在我看来，GreenOps 是一种专注于云工作负载碳足迹的 FinOps 形式。我希望这些社区合并成一个，并在该领域的开放规范和标准上进行合作，
例如[扩展 OpenCost](https://github.com/opencost/opencost/issues/1011)，以包括跨云的碳足迹信息。跨公司和行业的开源合作有很多机会。

## GitOps 逐渐成熟，并进入生产高峰期

自从 Alexis Richardson 在 2017 年首次创造了 GitOps 这个词以来，当谈到 GitOps 工具的成熟时，这个领域的事情发生了巨大的变化。
在 CNCF，Argo 和 Flux 项目[最近已经毕业](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247529234&idx=1&sn=8baa2faf2de26366ba86ed56de129aef&scene=21#wechat_redirect)，
显示了项目的稳定性和成熟的治理以及快速的采用水平。此外，它们也是 CNCF
生态系统中[开源速度最高的项目](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247529664&idx=1&sn=fbd001427d06e607e50d182bed913071&scene=21#wechat_redirect)。

如果你对这个领域感兴趣，我推荐你参与上面的开源项目，并加入 CNCF [Open GitOps 工作组](https://opengitops.dev/)。

## OpenTelemetry 日趋成熟

如果你看看来自 CNCF 的最新开源项目速度数据，
[OpenTelemetry 排名第二](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247529664&idx=1&sn=fbd001427d06e607e50d182bed913071&scene=21#wechat_redirect)，
仅次于 Kubernetes，对于这样一个年轻的项目来说，这令人难以置信。

在过去的几年里，几乎每一家主要的现代可观测性供应商都致力于集成 OTel。
OTel collector 框架将供应商从实现这一功能的需要中解放出来，并使最终用户的生活变得更好。
2023 年，你不仅会看到[许多技术先进的公司](https://github.blog/2021-05-26-why-and-how-github-is-adopting-opentelemetry/)采用 OTel，还会看到传统的企业最终用户利用这项技术。

## Backstage 开发者门户成熟度

开发人员的体验一直是那些达到一定规模以提高工程吞吐量的组织所关心的问题。随着越来越多的组织开始他们的云原生之旅，这对大多数行业来说变得非常重要。
在我的上一组[预测](https://www.aniszczyk.org/2021/01/19/cloud-native-predictions-for-2021-and-beyond/)中，提到“服务目录”将成为一种必需品，但它将不止于此。

在 CNCF 社区，Backstage 是我见过的少数几个甚至在采用 Kubernetes 之前就在传统企业中部署的项目之一。
在这方面有点独特，但它确实被银行或[航空公司](https://backstage.spotify.com/blog/adopter-spotlight/american-airlines-runway/)等传统企业，
以及 Spotify 等尖端科技公司所使用。你可以从他们的 [ADOPTERS.md](https://github.com/backstage/backstage/blob/master/ADOPTERS.md)
文件和 BackstageCon 视频中看到项目中的一些疯狂采用。

为了更上一层楼，Backstage 需要巩固它的 API，并继续培养它的插件生态系统，在本质上成为了这个领域的“Jenkins”。

关于 Backstage 和现代开发者门户的另一个有趣的事情是，Gartner 甚至已经注意到并开始在这个领域进行研究，这总是后来成熟的标志。

## WebAssembly 创新+启蒙斜坡

我坚信 WebAssembly（Wasm）将在不久的将来成为计算的主导形式，它正在探索浏览器之外的用例，从边缘到服务器工作负载。
我发现 Sapphire Ventures 关于 Wasm 承诺的这篇[文章](https://sapphireventures.com/blog/whats-up-with-webassembly-computes-next-paradigm-shift/)是这个主题中较好的文章之一。
从个人经验来看，我不断看到 Wasm 出现在面向未来云原生生态系统的更多领域，从 Envoy 中的插件系统重构，
或 WasmCloud 和 WasmEdge 等项目。还有，甚至 [Docker](https://www.docker.com/blog/docker-wasm-technical-preview/)在最近的技术预览版中也支持 Wasm。

然而，随着 Wasm 用例的发现、运行时的成熟，以及技术的全面发展，将会有一些成长的烦恼。用炒作周期的说法，
Wasm 将介于幻灭的低谷和启蒙的斜坡之间。虽然有很多关于 Wasm 潜力的正面报道，但当有很多像 [WASI](https://wasi.dev/)
和 tail calls 这样的移动部件没有得到完全支持时，实现这些东西是一个要面对的现实。

此外，我认为你将看到 Cloudflare 等精品云提供商和较小的初创公司为这项技术的成熟铺平道路，超大规模企业将在今年开始提供他们的第一批 Wasm 相关产品。

最后，我想明确一点，我看到了一个容器、Wasm 甚至 VM 将并存的世界……甚至我们在 Docker
的朋友[也这么说](https://www.docker.com/blog/why-containers-and-webassembly-work-well-together/)。

## 削减成本有利于精品云（或任何“超级云”）

继续今年的成本管理主题，我相信随着组织退后一步评估他们的云使用情况，精品云提供商
（或任何[超级云](https://blog.cloudflare.com/welcome-to-the-supercloud-and-developer-week-2022/)）将从这一趋势中受益。
有关 2023 年这一趋势的示例，请参见 Cloudflare
最近发布的[公告](https://www.prnewswire.com/news-releases/palantir-announces-strategic-partnership-with-cloudflare-focused-on-cloud-cost-optimization-301717292.html)…“
Palantir 宣布与 Cloudflare 建立战略合作伙伴关系，重点关注云成本优化”，以及他们如何将其
[R2](https://www.cloudflare.com/press-releases/2022/cloudflare-makes-r2-storage-available-to-all/) 产品与 S3 产品进行比较。

这些精品云提供商将把自己定位为关注这一特定领域的成本优化和客户服务。他们将在这一领域宣布新的收购和产品，与更大的云竞争。

## Kubernetes 有其 Linux 风格的成熟时刻

不提 Kubernetes 我就做不了云原生预测，对不！？就在最近，我在云原生生态系统内外发布了一篇关于 [2022 年开源项目 velocity](https://mp.weixin.qq.com/s/-AbkMXTPdERsW0OFNPwvyw)
也采用 Kubernetes。还有，Kubernetes 是运行在每一间 [Chick-Fil-A](https://medium.com/chick-fil-atech/enterprise-restaurant-compute-f5e2fd63d20f)
餐厅，甚至有一些基于边缘的计算为你服务！甚至还有人在[轨道](https://www.suse.com/success/hypergiant/)上运行 Kubernetes，甚至在[太空](https://www.youtube.com/watch?v=Yk6wRsckroA)！

当我说 Kubenetes 正在经历其 Linux 风格的成熟时刻时，我的意思是，Linux 最初是为一个特定的业余爱好者用例而构建的，
然后最终更广泛的生态系统扩展到在电话、汽车、实时系统等等上运行。Kubernetes 项目正在经历类似的演变，组织正在扩展 Kubernetes，
以在该项目最初没有设计的新型环境中运行，如嵌入式设备。这些新的用例，将创新推回到 Kubernetes 项目和更广泛的生态系统中，
就像在 Linux 中发生的一样。开源创新的引擎已经准备好了，并将继续下去。

## 其它预测

- 生成式人工智能将被立法，并在开源社区中引起摩擦。围绕归属、版权和遵守开源基金会和公司政策的有趣问题将会很有趣
  （例如，一些公司已经禁止使用 CoPilot 生成的代码）。我们也看到在这一领域对 CoPilot 甚至艺术版权和 Stable Diffusion 的诉讼，
  这只会加速并可能导致一些版权法的变化。Heather Meeker 有一篇关于 [copyright eating AI](https://heathermeeker.com/2023/01/19/is-copyright-eating-ai/)
  的很棒的博文，我强烈推荐给读者。
- VSCode 将继续增长并主导 IDE 领域。这是一个非常活跃的项目，到目前为止，微软在管理社区方面做得很好。
  如果你看看 Stackoverflow 的调查或 Top IDE index 的数据，就会发现 VSCode 将成为几乎所有主流编程语言的主流 IDE
  （甚至不包括它在 Codespaces 和 Gitpod 中的嵌入式使用）。
- RISC-V 将作为一个开源社区走向成熟，并在嵌入式和移动领域得到广泛应用。就在最近，谷歌宣布 Android 计划支持 RISC-V 作为“Tier 1”架构，
  这意味着在不久的将来，你会在 Android 看到 RISC-V。世界各地还存在有利于某些地区采用 RISC-V 的地缘政治逆风。
- 游戏引擎行业的开源创新飞速发展。游戏行业与云原生世界有些不同……大多数 AAA 风格的开发仍然发生在 Windows 机器、巨大的
  monorepo 以及 Unity 和 Unreal 等专有游戏引擎上。正如 [a16z 在 2016 年所说](https://a16z.com/2016/06/01/open-source-gaming-vr/)……
  我们需要游戏领域更多的开源，这一点随着 Bevy、Godot、[O3DE](https://o3de.org/) 等开源游戏引擎的出现终于实现了。
- 由于监管和安全问题的增加，OSPO 在行业和政府中不断增长。我是 TODO Group 的联合创始人之一，
  该组织是开源项目办公室（Open Source Program Office，OSPO）网络的所在地，我见证了 OSPO 在高科技行业中的发展。
  随着我们依赖的越来越多的软件是基于开源的，组织将需要一种战略方法来管理创新和安全风险。
  此外，欧盟各国政府开始[规范 OSPO](https://openforumeurope.org/wp-content/uploads/2022/06/The-OSPO-A-New-Tool-for-Digital-Government-2.pdf)，其他国家将会效仿。

## 最后，2023 年快乐，祝好运

我总是有一些更多的预测和趋势要分享，尤其是围绕最终用户驱动的开源、eBPF、服务网格和保护软件供应链，
但我会在今年晚些时候发布更详细的帖子，几个预测就足以开始新的一年了！无论如何，感谢你的阅读，
我希望在 [CloudNativeSecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/) 上见到大家，
当然还有我们于 2023 年 4 月在阿姆斯特丹举行的[欧洲 KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)
大型会议，已开放注册！

---

**DaoCloud 公司简介**

「DaoCloud 道客」云原生领域的创新领导者，成立于 2014 年底，拥有自主知识产权的核心技术，致力于打造开放的云操作系统为企业数字化转型赋能。
产品能力覆盖云原生应用的开发、交付、运维全生命周期，并提供公有云、私有云和混合云等多种交付方式。成立迄今，公司已在金融科技、先进制造、智能汽车、
零售网点、城市大脑等多个领域深耕，标杆客户包括交通银行、浦发银行、上汽集团、东风汽车、海尔集团、屈臣氏、金拱门（麦当劳）等。
目前，公司已完成了 D 轮超亿元融资，被誉为科技领域准独角兽企业。公司在北京、南京、武汉、深圳、成都设立多家分公司及合资公司，
总员工人数超过 400 人，是上海市高新技术企业、上海市“科技小巨人”企业和上海市“专精特新”企业，并入选了科创板培育企业名单。

网址：www.daocloud.io

邮件：info@daocloud.io

电话：400 002 6898
