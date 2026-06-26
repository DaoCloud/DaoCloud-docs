# Kubernetes 官方修正几个历史 CVE 记录：不是新增漏洞，而是重新认识风险

近日，Kubernetes 社区发布了一篇值得所有 AI 平台工程团队关注的文章：
[Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs](https://kubernetes.io/blog/2026/05/26/reconciling-unfixed-kubernetes-cves/)

Kubernetes 安全响应委员会（SRC）宣布，将于 2026 年 6 月 1 日修正部分历史 CVE 的元数据记录。修正后，一些企业的漏洞扫描系统可能突然出现“新增漏洞”，但实际上：

- ❌ 这些漏洞不是新发现的
- ❌ 也不是某个版本升级引入的
- ✅ 而是此前错误地标记了“已修复版本”，现在恢复了真实状态——这些风险实际上从未被代码彻底修复。

## 涉及哪些 CVE？

本次主要涉及：

| CVE | 严重性 | 问题描述 | 为什么仍未修复 | 临时规避措施 |
|-----|-------|---------|---------------|---------|
| [CVE-2020-8561](https://github.com/kubernetes/kubernetes/issues/104720) | 中（4.1） | kube-apiserver 与准入 Webhook 通信时会遵循 HTTP 重定向，拥有配置 AdmissionWebhookConfiguration 权限的用户可将 API 服务器请求重定向至内部私有网络。 | 限制重定向行为会破坏许多合法集成所依赖的标准 HTTP 客户端行为。 | 将 API 服务器日志级别设置为小于 10，避免记录响应正文；同时禁用动态性能分析（`--profiling=false`），防止未经授权修改日志级别。 |
| [CVE-2020-8562](https://github.com/kubernetes/kubernetes/issues/101493) | 低（3.1） | API 服务器代理中的 DNS TOCTOU（检查时间到使用时间）竞态条件允许用户绕过 IP 限制。系统先执行 DNS 校验，再进行第二次解析建立连接，攻击者可利用两次解析结果不一致实施攻击。 | 修复需要固定已解析的 IP 地址，但会破坏复杂的分域 DNS 或动态 IP 环境。 | 为 API 服务器使用本地 DNS 缓存服务器（如 `dnsmasq`），并配置 `min-cache-ttl`，确保检查与连接期间返回一致的 DNS 结果。 |
| [CVE-2021-25740](https://github.com/kubernetes/kubernetes/issues/103675) | 低（3.1） | Endpoints 和 EndpointSlice API 对象允许用户手动指定 IP 地址，可利用将 LoadBalancer 或 Ingress 转发到其他命名空间中的后端服务。 | 手动指定 Endpoint 地址是许多网络工具和 Operator 所依赖的基础功能。 | 限制对 Endpoints 和 EndpointSlices 的写权限。自 Kubernetes 1.22 起，默认 `edit` 和 `admin` ClusterRole 已移除这些权限；从旧版本升级的集群应手动审计并调整 `system:aggregate-to-edit` ClusterRole。 |

此外，社区再次强调：

* [CVE-2020-8554](https://www.cve.org/cverecord?id=CVE-2020-8554) 仍属于 Kubernetes 已知的架构性风险。

这些问题有一个共同特点：
**它们并非传统意义上的“打补丁即可修复”的软件漏洞，而是 Kubernetes 架构设计中的安全权衡措施。**

## 为什么这件事值得关注？

很多企业的安全运营流程已经形成固定模式：
发现 CVE → 升级版本 → 漏洞消失。

但 Kubernetes 的这些案例提醒我们：
**并非所有安全问题都能通过升级解决。**

在云原生时代，越来越多的风险来自：

* 配置错误（Misconfiguration）
* 权限设计不当（RBAC）
* 网络边界过宽
* 多租户隔离不足
* DNS、日志、控制面的安全配置

换句话说：
**安全能力正在从“补丁管理”逐渐转向“平台治理”。**

## 企业应该如何应对？

### 1️⃣ 不要把“未修复 CVE”简单视为升级任务

首先需要理解漏洞成因：

* 是否属于架构限制？
* 是否存在现实攻击路径？
* 是否有替代缓解措施？

### 2️⃣ 建立 Kubernetes 基线加固体系

包括：

- ✅ 最小权限 RBAC
- ✅ 控制平面安全配置
- ✅ Admission 策略治理
- ✅ 网络隔离与 NetworkPolicy
- ✅ 审计与可观测性建设
- ✅ 配置持续扫描与合规检查

### 3️⃣ 从“漏洞修复”走向“风险治理”

企业需要回答的问题不再是
**“我升级到哪个版本？”**

而是
**“我的平台是否具备抵御这类风险的防护能力？”**

## DaoCloud 观点

作为 Kubernetes 安全响应委员会（SRC）成员之一，DaoCloud 想借此次 CVE 元数据修正事件，再次强调一个重要观点：
**云原生及 AI 基础设施安全，从来不是简单的 CVE 数量游戏。**

随着 Kubernetes、云原生生态和 AI 基础设施不断演进，越来越多的风险并非源于代码缺陷本身，而是来自：

- 架构设计的复杂性；
- 配置与权限治理；
- 多集群、多租户场景下的安全边界；
- 日益增长的 AI 基础设施和云原生平台运维复杂度。

这也是 DaoCloud 长期深耕云原生平台建设所坚持的方向：
**通过 AI 平台工程能力，将安全能力前置并内建到 Kubernetes 全生命周期中，实现从“漏洞响应”向“持续治理”的转变。**

因为真正的企业级 AI 基础设施安全，不是等漏洞出现后再修补，而是在平台设计之初，就让风险无处遁形。

!!! tip

    关注 DaoCloud，持续获取 Kubernetes、云原生安全与 AI 基础设施的一线实践。
