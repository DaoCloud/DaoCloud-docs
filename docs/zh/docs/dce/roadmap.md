---
hide:
  - toc
---

# DCE 产品路线图

!!! note "声明"

    本路线图反映当前规划方向，具体功能和时间节点可能调整。以版本发布说明为准。

<style>
.roadmap-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid var(--md-default-fg-color--lightest);
  overflow: hidden;
  line-height: 1.6;
}
.roadmap-table thead th {
  background: var(--md-primary-fg-color);
  color: var(--md-primary-bg-color);
  padding: 12px 16px;
  font-weight: 600;
  border: none;
  text-align: left;
}
.roadmap-table thead th:first-child {
  text-align: center;
  width: 64px;
}
.roadmap-table tbody td {
  vertical-align: top;
  padding: 14px 16px;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  border-right: 1px solid var(--md-default-fg-color--lightest);
}
.roadmap-table tbody td:last-child {
  border-right: none;
}
.roadmap-table tbody tr:last-child td {
  border-bottom: none;
}
.roadmap-table .cat-label {
  font-weight: 700;
  text-align: center;
  letter-spacing: 2px;
  border-left-width: 4px;
  border-left-style: solid;
  background: var(--md-default-bg-color--light);
  border-right: 1px solid var(--md-default-fg-color--lightest);
}
.roadmap-table .cat-ai    { border-left-color: #00b267; color: #00894f; }
.roadmap-table .cat-infra { border-left-color: #2ecc71; color: #1fa85a; }
.roadmap-table .cat-plat  { border-left-color: #66d99a; color: #3cb371; }
.roadmap-table .cat-eco   { border-left-color: #a3e4be; color: #5dba8a; }
.roadmap-table ul {
  margin: 0;
  padding-left: 16px;
}
.roadmap-table li {
  margin-bottom: 4px;
}
.roadmap-table li::marker {
  color: var(--md-default-fg-color--lighter);
}
.roadmap-table a {
  color: var(--md-typeset-a-color);
  text-decoration: none;
  border-bottom: 1px dashed var(--md-accent-fg-color);
}
.roadmap-table a:hover {
  color: var(--md-accent-fg-color);
}
.roadmap-table mark {
  background: var(--md-accent-fg-color--transparent);
  color: inherit;
  padding: 1px 4px;
  border-radius: 3px;
}
.roadmap-table sup a {
  border-bottom: none;
  font-weight: 600;
  color: var(--md-accent-fg-color);
}
</style>

<table class="roadmap-table">
<thead>
<tr>
<th></th>
<th>H1 2026</th>
<th>H2 2026</th>
<th>2027+</th>
</tr>
</thead>
<tbody>
<tr>
<td class="cat-label cat-ai">AI</td>
<td><ul>
<li>推理运行时集成（vLLM / SGLang），适配国产 GPU</li>
<li>模型资产中心 MVP（用户/项目/仓库管理、模型与数据集上下载、CLI）</li>
<li>国产模型仓库预集成（Qwen / GLM / Baichuan）</li>
<li>推理加速：多级 KV Cache、拓扑感知调度（<a href="https://kueue.sigs.k8s.io/">Kueue</a> / Gang）</li>
<li>训推混部基础支持</li>
<li>AI 故障诊断（多源日志关联 + 根因分析）</li>
<li>预测性告警（时序异常检测、资源耗尽预警）</li>
</ul></td>
<td><ul>
<li><mark>DCE AI Runtime GA</mark></li>
<li>统一推理 API（兼容 OpenAI API / Llama Stack）</li>
<li>微调 / LoRA 支持</li>
<li>多模态推理（图文、音视频）</li>
<li>模型资产中心完善（远程复制/同步、安全扫描、预热加速、多语言）</li>
<li><a href="https://github.com/matrixhub-ai/matrixhub">MatrixHub</a> 提交 CNCF<sup><a href="#fn-matrixhub">1</a></sup></li>
<li>AI Agent 基础设施 Beta（沙箱、记忆与上下文、语义路由）</li>
<li>故障自愈（集成训练/推理框架自动恢复）</li>
<li>告警降噪（相关告警自动归并）</li>
<li>大模型安全（模型访问控制、推理内容安全策略）</li>
</ul></td>
<td><ul>
<li>分布式推理</li>
<li>训推混部优化</li>
<li>AI 全栈自动化（AutoML + Agent）</li>
</ul></td>
</tr>
<tr>
<td class="cat-label cat-infra">算力</td>
<td><ul>
<li><mark>沐曦 GPU 适配启动</mark>（网络拓扑、Lustre GDS）</li>
<li>昇腾 910C NPU 调度（CANN 驱动）</li>
<li>海光 DCU GPU 调度</li>
<li>AI 高性能存储（Lustre 文件系统）</li>
<li>Kueue / Gang Scheduling / <a href="https://lws.sigs.k8s.io/">LWS</a> / DRA 集成</li>
<li><a href="https://github.com/Project-HAMi/HAMi">HAMi</a> 商业版集成<sup><a href="#fn-hami">2</a></sup></li>
<li>containerd 增强（容器磁盘限制）</li>
</ul></td>
<td><ul>
<li><mark>国产 GPU 全面 GA</mark>（沐曦 / 昇腾 / 海光 / 壁仞）</li>
<li>沐曦超节点发布</li>
<li>超节点方案（8/16 卡高密度，GPU 共享调度）</li>
<li>GPU Operator 混合调度（CPU + GPU + NPU），利用率 → 80%+</li>
<li>分布式存储方案（云场景）</li>
</ul></td>
<td><ul>
<li>DPU / NPU 统一调度</li>
<li>算力网络，多集群算力联邦</li>
<li>InfiniBand 拓扑识别（通过 UFM）</li>
</ul></td>
</tr>
<tr>
<td class="cat-label cat-plat">平台</td>
<td><ul>
<li>一键安装（Web UI + CLI，自动环境检测）</li>
<li>Preflight 预检框架（插件化，检测网络/存储/权限）</li>
<li><a href="https://gateway-api.sigs.k8s.io/">Gateway API</a> 迁移启动（Ingress 退休）</li>
<li>日志聚合能力增强</li>
<li>算力云运营平台管理后台</li>
<li>算力基线梳理与计费模式优化</li>
<li>Ghippo 管理后台界面化</li>
<li>CSP 用户双因子认证（2FA）</li>
</ul></td>
<td><ul>
<li>滚动升级（零停机，金丝雀 + 回滚）</li>
<li><mark>Gateway API 迁移完成</mark></li>
<li>部署时间 → 15 分钟（从 ~2 小时）</li>
<li>算力云运营平台完善（租户隔离、库存管理、计费互转、GPU 升降级）</li>
<li>裸金属部署工具（集群装机、自动化测试、单机排障）</li>
</ul></td>
<td><ul>
<li>轻量化内核，边缘原生</li>
<li>自适应平台（自动调优 + 自愈）</li>
</ul></td>
</tr>
<tr>
<td class="cat-label cat-eco">生态</td>
<td><ul>
<li>Kueue / LWS / Gang Scheduling 等 K8s AI/ML SIG 贡献</li>
<li><a href="https://github.com/spidernet-io/spiderpool">Spiderpool</a> DRA 实现、DRANet</li>
<li>Spiderpool 支持沐曦 GPU</li>
<li>GAIE / NIXL / LMCache 等推理优化项目参与</li>
</ul></td>
<td><ul>
<li>MatrixHub Sandbox</li>
<li><a href="https://github.com/DaoCloud/unifabric">unifabric</a> 1.0（网络健康检查、容灾标记、KV Cache 同步监控）</li>
<li>metal-deployer 工程交付</li>
<li>GAIE / NIXL 社区席位</li>
</ul></td>
<td><ul>
<li>unifabric Sandbox、InfiniBand 支持</li>
<li>低代码编排，自然语言运维</li>
</ul></td>
</tr>
</tbody>
</table>

<small>

<span id="fn-matrixhub">**[1]** MatrixHub — DaoCloud 开源的模型资产中心，对标 Harbor 之于容器镜像的定位。</span>
<br>
<span id="fn-hami">**[2]** HAMi — 异构 AI 算力虚拟化中间件，支持 GPU 共享与隔离。</span>

</small>

---

## 战略方向

DCE 已具备 [AI Lab](../baize/intro/index.md)（训练）和[大模型服务平台](../hydra/intro/index.md)（模型管理与推理）。2026 年在此基础上集中做两件事：

1. **AI 深化** — 补全企业推理场景，适配国产 GPU，打通训练到推理
2. **平台深化** — 运维体验、部署效率、算力管理，把已有能力做扎实

---

## DCE 5.0 现有能力

各模块可独立升级，不需要整体停机。

| 模块 | 能力 | 文档 |
|------|------|------|
| **容器管理** | 多集群管理、集群生命周期、弹性伸缩、Helm 应用 | [:material-book-open-outline:](../kpanda/intro/index.md) |
| **应用工作台** | CI/CD 流水线、GitOps、灰度发布 | [:material-book-open-outline:](../amamba/intro/index.md) |
| **多云编排** | 跨云资源调度与应用编排 | [:material-book-open-outline:](../kairship/intro/index.md) |
| **微服务引擎** | Spring Cloud / Dubbo 管理 | [:material-book-open-outline:](../skoala/intro/index.md) |
| **服务网格** | 基于 Istio 的流量治理与可观测 | [:material-book-open-outline:](../mspider/intro/index.md) |
| **云原生网络** | 多 CNI、网络策略、负载均衡 | [:material-book-open-outline:](../network/intro/index.md) |
| **云原生存储** | CSI 标准、HwameiStor、多存储后端 | [:material-book-open-outline:](../storage/index.md) |
| **可观测性** | 指标/日志/链路追踪、多维告警 | [:material-book-open-outline:](../insight/intro/index.md) |
| **中间件** | Redis / MySQL / Kafka / ES / PG 生命周期管理 | [:material-book-open-outline:](../middleware/index.md) |
| **镜像仓库** | 多实例管理，兼容 Harbor | [:material-book-open-outline:](../kangaroo/intro/index.md) |
| **全局管理** | 身份认证、多租户、权限、审计 | [:material-book-open-outline:](../ghippo/intro/index.md) |
| **虚拟机** | KubeVirt，VM 管理、快照、热迁移 | [:material-book-open-outline:](../virtnest/intro/index.md) |
| **AI Lab** | 训练推理、PyTorch / TensorFlow | [:material-book-open-outline:](../baize/intro/index.md) |
| **大模型服务** | 大模型部署运维，vLLM / SGLang | [:material-book-open-outline:](../hydra/intro/index.md) |
| **云边协同** | 边缘集群与节点管理 | [:material-book-open-outline:](../kant/intro/index.md) |

---

## 运营保障

| 类别 | 内容 |
|------|------|
| **高可用** | 管理面多副本 + etcd 集群，单节点故障自动恢复 |
| **数据备份** | etcd 快照、应用备份（Velero）、跨集群灾备 |
| **离线运行** | 完全离线部署和运行，不依赖外部网络 |
| **升级回滚** | 所有版本升级支持一键回滚 |
| **安全合规** | 等保三级、审计日志、镜像扫描、模型访问控制 |
| **身份认证** | LDAP / OIDC / 企业统一身份平台 |
| **技术支持** | [文档站](https://docs.daocloud.io) + 培训认证 + TAM + 7×24 应急响应 |

---

## 生态与合作

**开源贡献：** Kubernetes 核心仓库贡献中国第一、全球前三。参与 Istio / Cilium / [Spiderpool](https://github.com/spidernet-io/spiderpool) / [HwameiStor](https://hwameistor.io) 等 CNCF 项目。Kueue / LWS / Gang Scheduling 等 K8s AI/ML SIG 活跃贡献者。

| 领域 | 合作伙伴 |
|------|---------| 
| 芯片与算力 | 华为昇腾、海光、壁仞、沐曦、NVIDIA |
| 操作系统 | 麒麟、统信 UOS |
| 数据库与中间件 | 达梦、OceanBase、TiDB |

**行业落地：** 金融 · 制造 · 能源 · 电信 · 政务，累计服务 500+ 企业客户。
