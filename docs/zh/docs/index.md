---
hide:
  - navigation
  - toc
---

# DaoCloud 文档

DaoCloud 是全球 AI 领域的开源先锋，致力于通过云原生技术加速企业智能化转型。
旗下拥有三大产品线：**DCE 5.0** 云原生 AI 操作系统、**d.run** 企业级 AI 服务平台、**Token 工厂** 一体化智算运营平台，
覆盖从基础设施、算力调度到模型推理和应用构建的全栈能力。

## DCE 5.0 文档

DaoCloud Enterprise 5.0 (DCE 5.0) 是一款高性能、可扩展的云原生 AI 操作系统，
是[经 CNCF 认证的 Kubernetes - AI Platform](./dce/kcsp.md)。
它能够在任何基础设施和任意环境中提供一致、稳定的体验，支持异构云、边缘云和多云编排。

<div class="tf-arch tf-arch--compact">
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">应用层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="amamba/intro/">
        <span class="tf-arch-card-title">应用工作台</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="baize/intro/">
        <span class="tf-arch-card-title">AI Lab</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="hydra/intro/">
        <span class="tf-arch-card-title">大模型服务平台</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="clawos/intro/">
        <span class="tf-arch-card-title">ClawOS</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="kant/intro/">
        <span class="tf-arch-card-title">云边协同</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="virtnest/intro/">
        <span class="tf-arch-card-title">虚拟机</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">治理层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="kairship/intro/">
        <span class="tf-arch-card-title">多云编排</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="skoala/intro/">
        <span class="tf-arch-card-title">微服务引擎</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="mspider/intro/">
        <span class="tf-arch-card-title">服务网格</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="middleware/">
        <span class="tf-arch-card-title">中间件</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="insight/intro/">
        <span class="tf-arch-card-title">可观测性</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">底座层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="kpanda/intro/">
        <span class="tf-arch-card-title">容器管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="kangaroo/intro/">
        <span class="tf-arch-card-title">镜像仓库</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="network/intro/">
        <span class="tf-arch-card-title">云原生网络</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="storage/">
        <span class="tf-arch-card-title">云原生存储</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="ghippo/intro/">
        <span class="tf-arch-card-title">全局管理</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">资源</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="install/">
        <span class="tf-arch-card-title">安装</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="download/">
        <span class="tf-arch-card-title">下载中心</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="dce/bphome/">
        <span class="tf-arch-card-title">最佳实践</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="dce/faq/">
        <span class="tf-arch-card-title">常见问题</span>
      </a>
    </div>
  </div>
</div>

---

## d.run 文档

d.run 是 DaoCloud 推出的企业级 AI 服务平台，集算力管理、模型市场、推理部署和应用构建于一体，
覆盖 AI 全生命周期。通过高效的异构 GPU 调度、灵活的资源管理和完善的安全机制，
帮助企业更快、更经济地运行大模型和 AI 应用。

<div class="tf-arch">
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">AI 应用层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="https://docs.d.run/dak/index.html">
        <span class="tf-arch-card-title">AI 应用</span>
        <span class="tf-arch-card-desc">智能问答 · 应用构建</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="https://docs.d.run/clawos/index.html">
        <span class="tf-arch-card-title">ClawOS</span>
        <span class="tf-arch-card-desc">多智能体运行与治理</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">模型服务层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="https://docs.d.run/models/index.html">
        <span class="tf-arch-card-title">大模型服务平台</span>
        <span class="tf-arch-card-desc">模型市场 · 部署 · 体验</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">算力与管理层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="https://docs.d.run/zestu/index.html">
        <span class="tf-arch-card-title">算力云</span>
        <span class="tf-arch-card-desc">GPU 算力市场 · 容器实例</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="https://docs.d.run/leopard/index.html">
        <span class="tf-arch-card-title">计费中心</span>
        <span class="tf-arch-card-desc">钱包 · 账单 · 订单</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="https://docs.d.run/manage/personal/index.html">
        <span class="tf-arch-card-title">管理</span>
        <span class="tf-arch-card-desc">个人中心 · 账号管理</span>
      </a>
    </div>
  </div>
</div>

---

## Token 工厂文档

Token 工厂是 DaoCloud 面向 AI 智算场景打造的一体化运营平台，围绕大模型推理、算力调度和集群运维提供端到端的能力支撑。
平台深度整合大模型服务平台与 InferX 推理引擎，向上承接模型部署与推理加速，
向下依托容器管理实现 GPU 算力的精细化调度与资源编排，
配合可观测性和全局管理构建从算力接入到模型服务的完整闭环。

<div class="tf-arch">
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">模型服务层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="hydra/intro/">
        <span class="tf-arch-card-title">Token 工厂管理</span>
        <span class="tf-arch-card-desc">大模型平台 · 部署与运营</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="inferx/">
        <span class="tf-arch-card-title">InferX 推理引擎</span>
        <span class="tf-arch-card-desc">GPU 推理加速 · 模型服务</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">算力调度层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="kpanda/intro/">
        <span class="tf-arch-card-title">容器管理</span>
        <span class="tf-arch-card-desc">GPU 资源池化 · 多租户调度</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">运维管理层</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="insight/intro/">
        <span class="tf-arch-card-title">可观测性</span>
        <span class="tf-arch-card-desc">性能监控 · 利用率追踪</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="ghippo/intro/">
        <span class="tf-arch-card-title">全局管理</span>
        <span class="tf-arch-card-desc">用户权限 · 日志治理</span>
      </a>
    </div>
  </div>
</div>

[申请 DCE 5.0 社区免费体验](./dce/license0.md){ .md-button .md-button--primary }
[注册体验 d.run](https://console.d.run/){ .md-button .md-button--primary }
[Token 工厂概览](tf/index.md){ .md-button .md-button--primary }
