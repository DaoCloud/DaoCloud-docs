# 开源文档的构建、运营和贡献

本文介绍开源站点常用的构建方法，运营思路和吸引贡献者的经验。

## DaoCloud 自主和捐献的开源站点

本节列出 DaoCloud 自主开源和捐献给社区的一些项目和站点。

### 自主产品

目前 DaoCloud 的主打产品为云原生操作系统 DCE 5.0 和算力运营管控平台 d.run。

| 网站 | 介绍 | 生成器 | 构建方式 | Repo 地址 |
|-----|-----|-------|---------|----------|
| [DCE 5.0](https://docs.daocloud.io) | 一款高性能、可扩展的云原生操作系统。其文档站的源代码完全开源 | mkdocs-material | cloudflare/wrangler-action@v3 | https://github.com/DaoCloud/DaoCloud-docs |
| [d.run](https://docs.d.run) | AIGC 综合算力运维、大模型服务和运营平台。其文档站的源代码完全开源 | mkdocs-material | cloudflare/wrangler-action@v3 | https://github.com/d-run/drun-docs |

### CNCF Sandbox

DaoCloud 捐献给 CNCF 并加入 Sandbox 的开源项目：

| 网站 | 介绍 | 生成器 | 构建方式 | Repo 地址 |
|-----|-----|-------|---------|----------|
| [Clusterpedia](https://clusterpedia.io/) | 这个工具可以方便地检索容器化集群中的所有资源 | Hugo | gh-pages | https://github.com/clusterpedia-io/website |
| [HAMi](https://project-hami.io/) | 这是一个算力虚拟化的中间件，可以支持多种架构的 GPU | Docusaurus 3 | gh-pages | https://github.com/Project-HAMi/website |
| [HwameiStor](https://hwameistor.io/) | 这是一个云原生化的本地存储方案 | Docusaurus | gh-pages | https://github.com/hwameistor/hwameistor |
| [Kubean](https://kubean-io.github.io/kubean/) | 这是基于 Kubespray 构建的 Kubernetes 平台安装工具 | MkDocs | gh-pages | https://github.com/kubean-io/kubean |
| [Merbridge](https://merbridge.io/) | 使用 eBPF 加速网格的工具 | Hugo | gh-pages | https://github.com/merbridge/merbridge |
| [Piraeus](https://piraeus.io/) | 一个云原生数据仓库 | mkdocs-material | gh-pages | https://github.com/piraeusdatastore/piraeus |
| [Spiderpool](https://spidernet-io.github.io/spiderpool/) | 基于 Kubernetes 构建的 Underlay 和 RDMA 网络方案 | mkdocs-material | gh-pages | https://github.com/spidernet-io/spiderpool |

### 更多开源站点

经 DaoCloud 开源，仍在发展中的站点：

| 网站 | 介绍 | 生成器 | 构建方式 | Repo 地址 |
|-----|-----|-------|---------|----------|
| [CloudTTY](https://cloudtty.github.io/cloudtty/) | 这是一个网页版的命令行工具 | 未指定 | gh-pages | https://github.com/cloudtty/cloudtty |
| [EgressGateway](https://spidernet-io.github.io/egressgateway/) | 提供固定的 Egress IP 地址方案 | mkdocs-material | gh-pages | https://github.com/spidernet-io/egressgateway |
| [kdoctor](https://kdoctor-io.github.io/kdoctor/) | 这是一个 Kubernetes 数据面的测试组件，主动探测集群的功能和性能 | mkdocs-material | gh-pages | https://github.com/kdoctor-io/kdoctor |
| [KLTS](https://klts.io/) | 对社区当前 4 个版本之外的 Kubernetes 提供长期维护支持 | Hugo | gh-pages | https://github.com/klts-io |

## 社区热门开源站点

| 网站 | 介绍 | 生成器 | 构建方式 | Repo 地址 |
|-----|-----|-------|---------|----------|
| [k/website](https://kubernetes.io/) | CNCF 社区的基石，云原生的起点 | Hugo | Netlify | https://github.com/kubernetes/website |
| [istio.io](https://istio.io/) | 目前最流行的服务网格 | Hugo | Netlify | https://github.com/istio/istio.io |
| [opentelemetry.io](https://opentelemetry.io/) | 收集和导出分布式系统可观测数据的开源工具集 | Hugo | Netlify | https://github.com/open-telemetry/opentelemetry.io |
| [vLLM](https://docs.vllm.ai/en/latest/) | 一个高效的开源库，用于加速大语言模型的推理性能 | Sphinx | Read the Docs | https://github.com/vllm-project/vllm |
| [Pytorch](https://pytorch.org/) | star 87k，一个开源的深度学习框架，广泛用于研究和生产环境中，以其动态计算图和易用性著称 | Hugo | 未指定 | https://github.com/pytorch/pytorch |
| [huggingface](https://huggingface.co/) | star 140k，汇总了全世界的大模型 | Docusaurus | .github/workflows | https://github.com/huggingface/transformers |
| [KWOK](https://kwok.sigs.k8s.io/) | DaoCloud 捐献给 kubernetes-sigs 的模拟测试项目 | Hugo | Netlify | https://github.com/kubernetes-sigs/kwok |
| [Kueue](https://kueue.sigs.k8s.io/) | DaoCloud 与 kubernetes-sigs 联合维护的 Kubernetes 原生的 Job 排队管理器 | Hugo | Netlify | https://github.com/kubernetes-sigs/kueue |
| [LWS](https://github.com/kubernetes-sigs/lws) | DaoCloud 与 kubernetes-sigs 联合维护，无缝兼容 vLLM、SGLang 等主流架构，一键部署企业级 AI 服务 | 无 | Netlify | https://github.com/kubernetes-sigs/lws |

### 静态生成器对比

仅列出一些上文提及的静态生成器：

| 项目名称 | Star 数量 | 编写语言 | 开源时间 | 体量大小 | Repo 地址 |
|-----------|-----------|---------|--------|--------------|----------|
| **Hugo** | 78.1k | Go | 2014 年 | **超轻量级，极快** | [Hugo repo](https://github.com/gohugoio/hugo) |
| **MkDocs** | 19.9k | Python | 2014 年 | **轻量级** | [MkDocs repo](https://github.com/mkdocs/mkdocs) |
| **Docusaurus** | 58.4k | React | 2017 年 | **中等，依赖 React** | [Docusaurus repo](https://github.com/facebook/docusaurus) |
| **Sphinx** | 6.8k | Python | 2008 年 | **中等，功能强大** | [Sphinx repo](https://github.com/sphinx-doc/sphinx) |

### 构建方式对比

| **构建方式**     | **优点** | **缺点** |
|----------------|---------|---------|
| **GitHub Pages** | ✅ 免费托管，适合开源项目  <br> ✅ 与 GitHub 仓库深度集成，自动部署  <br> ✅ 支持 Jekyll，可直接渲染 Markdown 文件 | ❌ 仅支持静态网站，功能较单一  <br> ❌ 自定义域名需手动配置 HTTPS  <br> ❌ CI/CD 能力有限，难以满足复杂部署需求 |
| **Netlify** | ✅ 支持自动化 CI/CD，构建、预览、部署一体化  <br> ✅ 绑定 Git 仓库，支持多种静态站点生成器  <br> ✅ 提供 Serverless Functions，可支持动态功能 | ❌ 免费额度有限，流量或构建超出需付费  <br> ❌ 部署日志较简洁，调试复杂构建问题时可能不够直观  <br> ❌ 需要额外配置 DNS 以充分利用 Edge Network |
| **Cloudflare Pages** | ✅ 全球 CDN 加速，特别适合国内用户  <br> ✅ 内置 DDoS 防护，安全性高  <br> ✅ 支持 Pages Functions，可结合 Workers 运行动态逻辑 | ❌ 免费版功能有限，部分高级功能需订阅付费方案  <br> ❌ 部署过程较 Netlify 复杂，需手动配置构建和路由  <br> ❌ 部分第三方插件或工具兼容性较差 |

### 开源站点常见 Bot

在 GitHub 上的开源项目（如 Kubernetes 和 Transformers）中，常见的机器人（bots）用于自动化
CI/CD、代码质量检查、发布管理等。以下是一些常见的 bot 及其用途：  

| 分类 | Bot 名称 | 功能描述 |
|-----|----------|--------|
| **代码质量 & Lint** | GitHub Actions Bots | 运行 `black`、`flake8`、`eslint`、`prettier` 等 lint 任务，确保代码风格一致 |
| | LGTM Bot | 分析代码质量，检测潜在的安全漏洞 |
| | Codecov Bot | 检查测试覆盖率，并在 PR 中提供覆盖率变化的报告 |
| | Prettier Bot | 自动格式化 JavaScript、Markdown 等文件，保持代码风格一致 |
| **PR & Issue 管理** | k8s-ci-robot（Prow） | Kubernetes 及 CNCF 生态常用，自动管理 PR、CI/CD 任务 |
| | Stale Bot（probot-stale）| 自动关闭长期未活动的 Issue 和 PR，保持项目整洁 |
| | CLAassistant Bot | 检查贡献者是否签署了贡献者许可协议（CLA） |
| | welcome Bot（probot-welcome） | 对新贡献者的首个 PR 发送欢迎信息 |
| **版本管理 & Release** | Release Drafter | 自动生成 Release Notes，归类 PR 变更 |
| | Semantic Release | 根据 commit 信息自动管理版本号，并发布新版本 |
| | Dependabot | 检测依赖项是否有更新，并自动创建 PR 进行升级 |
| **安全 & 依赖管理** | Snyk Bot | 扫描项目的依赖项，检测安全漏洞 |
| | GitHub Security Bot（Security Alerts） | 自动提醒安全漏洞，并建议修复方案 |

这些 Bot 大多基于 GitHub Actions 或 Prow，可用于提升项目的自动化程度、代码质量和安全性。

## 开源站点运营思考

吸引贡献者的一些举措：

- [构建 Mentor 体系](https://contribute.cncf.io/about/mentoring/)，培训贡献者成长
- 为优秀贡献者提供 d.run 等试用的时间和权限
- 评选公司外部的年度贡献者，并给予 [Badge](https://www.credly.com/users/michael-yao0422/) 或试用奖励
- 定期组织线上线下开源会议，邀请贡献者参与，交流开源技术，拓展人脉资源

文档是拓展开源影响力的重要组成，参见
[2024 中国开源年度报告](./open-source-report.md#35-2024-10)和
[2024 年度中国企业黑马 DaoCloud 的解读](./open-source-report.md#36-2024-openrank-10)。

![DaoCloud 全国排名第 5](https://hackmd.io/_uploads/rkA0CtQU1g.png)

## 开源贡献

在开源社区，贡献不仅仅局限于代码，还包括文档、测试、用户反馈等多个方面。
以下是一些主要的贡献方式，以及如何有效地参与到开源项目中。

### 文档贡献

| 贡献类型 | 具体操作 |
|---------|--------|
| 新编文档 | 翻阅 Issue、Release notes，了解最近的文档需求 |
| 修复错误 | 发现文档中的错别字、格式问题或过时信息，直接提交 PR 进行修复 |
| 改进可读性 | - 通过增加示例、优化表述方式，使文档更加易读和易用 |
| | - 采用 Markdown 等格式，提高排版质量 |
| 本地化 | - 参与项目的 i18n（国际化）工作，贡献多语言版本的文档 |
| | - 例如 Kubernetes、Istio 等项目都设有不同语言的 SIG（Special Interest Group） |

### 社区互动也是一种贡献

| 贡献类型 | 具体操作 |
|---------|--------|
| **回答问题** | - 在 GitHub Discussions、Slack、论坛、微信群等地方，帮助解答新手问题 |
| | - 贡献 FAQ（常见问题解答），降低维护者的支持成本 |
| **组织和参与活动** | - 参与线上或线下的开源会议，例如 KubeCon、Open Source Summit |
| | - 组织 meetup、workshop，推广项目和分享经验 |

### 贡献奖励机制

为了激励贡献者，开源项目通常会设置奖励机制，如：

- **贡献者徽章（Badge）**：如 CNCF 的贡献者认证
- **T-shirt & 周边**：许多开源项目会赠送纪念品给活跃贡献者
- **Mentor 计划**：为新手贡献者提供指导，加速成长
- **优先访问权限**：如 d.run 等云服务可为活跃贡献者提供试用额度

### 如何开始？

| 步骤 | 描述 |
|-----|------|
| 选择感兴趣的项目 | 关注 CNCF Landscape、GitHub Trending，找到与你的技术栈匹配的项目 |
| 阅读贡献指南 | 每个开源项目通常都有 `CONTRIBUTING.md`，阅读并遵循贡献流程 |
| 加入社区 | 订阅邮件列表、加入 Slack / Discord、参与定期会议 |
| 从小任务开始 | 先贡献文档、小 bug 修复，逐步熟悉项目 |
| 持续贡献 | 通过多次贡献建立信誉，成为项目的长期贡献者，甚至晋升为 Maintainer |

开源贡献不仅能提升技术能力，还能拓展人脉，为职业发展打开更多机会。希望更多开发者加入开源社区，共同推动技术进步！

写在最后，开源文档站不仅能扩大企业的影响范围，还能促进产品和文档的自我优化和演进。
在透明、开放的环境下，用户和开发者可以直接反馈问题，推动改进，甚至贡献内容，使文档更具时效性和实用性。
同时，一个活跃的开源文档站点也能帮助企业建立更紧密的社区联系，增强用户粘性，形成良性的技术生态。
唯有持续更新、紧跟行业动态，才能确保文档的生命力，使产品保持长期的竞争力和影响力。
