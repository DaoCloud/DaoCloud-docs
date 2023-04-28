# KLTS

KLTS 全称为 Kubernetes Long Term Support，主要使命是为 Kubernetes 早期版本提供长期免费的维护支持。

之所以需要维护早期版本，是因为在实际生产环境中，最新版本不一定是最好的，也不是最稳定的。
正常而言，Kubernetes 社区版本的维护周期只有一年左右，请参阅 [Kubernetes 版本发行周期](#release-cycle)。
在社区停止维护后，KLTS 在接下来的三年内提供免费维护服务。  

在实际生产中，为什么大多数企业选择采用早期的 Kubernetes 版本管控集群呢？  

- 首先，升级频率高会带来变更风险，每次升级必须进行充分验证。
特别是金融行业的平台层变更周期通常比较长，因为一旦升级后的新版本存在 bug，就需要被迫回滚或快速响应升级至更新的版本，这样会造成不必要的成本支出。  

- 其次，Kubernetes 升级后部分功能的替代方案还没有完全生产就绪，在生产环境中常会出现不兼容的状况。  

- 最后，Kubernetes 社区仅支持小版本 +1 升级，不支持跨版本升级，因为跨版本升级经常会出现一些不可控的因素，造成更大的生产问题。  

所以大多数企业的选择是沿用早期版本，不会贸然升级。
但 Kubernetes 社区只维护最新的 3 到 4 个版本，如何才能保证这些早期版本免受社区不定时发现的 CVE 漏洞和 bug 的袭扰呢？
这就是 KLTS 的价值所在！我们对早期版本提供长达 3 年的免费维护支持，积极修复早期版本的 CVE 安全漏洞和重大 bug。  

## KLTS 维护周期 {#maint-cycle}

Kubernetes 版本号表示为 x.y.z，其中 x 是大版本号，y 是小版本号，z 是补丁版本，KLTS 提供的补丁版本号通常以 lts1、lts2 … ltsn 表示。为了方便表述，本节用前两位 x.y 描述 Kubernetes 版本号。  

假设社区发布的最新 Kubernetes 版本为 x.y，根据[社区版本维护声明](https://kubernetes.io/zh-cn/releases/version-skew-policy/#supported-versions)，社区仅维护最近的三个版本，而 KLTS 目前维护从 1.10 起的近十个早期版本，如下图所示。  

![k8s 维护等版本](https://docs.daocloud.io/daocloud-docs-images/docs/community/images/klts01.png)

当 Kubernetes 社区发现可能影响生产的 CVE 新漏洞或 bug，受到影响的可能不止是社区正在维护的版本，还有之前已经停止维护、但企业仍在使用、且不能贸然升级的版本，KLTS 团队维护的正是这些社区放弃维护的版本。目前 KLTS 的版本维护周期如下：  

![klts 维护周期](https://docs.daocloud.io/daocloud-docs-images/docs/community/images/klts02.png)

从上图可看出，Kubernetes 社区对某个版本的维护周期通常在一年左右，而 KLTS 可以在接下来的三年内提供长期维护，直至代码无法兼容，才会将相应版本淘汰。
进一步了解 [Kubernetes 补丁发布周期](https://kubernetes.io/zh-cn/releases/patch-releases/)。

## KLTS 修复范围 {#bug-fix}

有些高优先级的 CVE 或严重 Bug 存在于生产环境中会造成较大的安全隐患。
CVE 安全问题是集群的生命线，KLTS 会优先修复中高级别的 CVE，其次会修复重大 Bug，确保生产环境稳定运行。  

以 2021 年 1 月发现的 [CVE-2021-3121](https://www.cvedetails.com/cve/CVE-2021-3121) 安全漏洞为例，CVSS 危急分数高达 7.5。
但截止 2021 年 9 月 Kubernetes 社区：

- 仅修复了 4 个版本：1.18、1.19、1.20、1.21
- 宣称“所有早期版本均有这个安全漏洞，建议用户立即停止使用早期版本”
- 拒绝[修复早期版本漏洞的要求](https://github.com/kubernetes/kubernetes/issues/101435)

![cve 漏洞](https://docs.daocloud.io/daocloud-docs-images/docs/community/images/klts03.png)

KLTS 针对这一现状，默默修复了深受 [CVE-2021-3121](https://www.cvedetails.com/cve/CVE-2021-3121) 安全漏洞影响的 8 个早期版本：

- v1.17.17
- v1.16.15
- v1.15.12
- v1.14.10
- v1.13.12
- v1.12.10
- v1.11.10
- v1.10.13

[了解 KLTS 社区](https://github.com/klts-io){ .md-button }

[查阅 KLTS 官网](https://klts.io/){ .md-button }
