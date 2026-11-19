---
hide:
  - toc
---

# 快速入门

快速入门包含一系列动手实验，帮助您快速体验 Token 工厂的简单功能，包括从安装部署、纳管算力、生产 Token 到运营结算的功能。按角色分成两条学习路径：

- 管理员视角：完成平台部署与算力纳管；
- 用户视角：完成模型部署、应用构建与运营计费。

建议按顺序完成，每个教程都可以独立操作，帮助您快速熟悉 Token 工厂的核心功能。

<style>
.tf-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.tf-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.tf-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.tf-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.tf-path-step:last-child::after{display:none}
.tf-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.tf-path-title{font-weight:700;font-size:0.95rem}
.tf-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.tf-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.tf-path-step::after{display:none}}
</style>

=== "管理员视角"

    <div class="tf-path">
      <a class="tf-path-step" style="--path-c:#2196f3" href="deploy-platform/">
        <span class="tf-path-num">1</span>
        <span class="tf-path-title">安装 Token 工厂</span>
        <span class="tf-path-desc">在火种节点运行安装器，完成离线安装</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#00acc1" href="init-users/">
        <span class="tf-path-num">2</span>
        <span class="tf-path-title">创建用户与工作空间</span>
        <span class="tf-path-desc">规划多租户体系，为用户授权</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#43a047" href="join-cluster/">
        <span class="tf-path-num">3</span>
        <span class="tf-path-title">创建工作集群</span>
        <span class="tf-path-desc">接入 GPU 节点，承接推理负载</span>
        <span class="tf-path-go">Go →</span>
      </a>
    </div>

    完成以上三步后，平台即可投入使用，算力已就绪。管理员也可以继续阅读用户视角的教程，了解平台的完整能力。

=== "用户视角"

    <div class="tf-path">
      <a class="tf-path-step" style="--path-c:#fb8c00" href="deploy-model/">
        <span class="tf-path-num">1</span>
        <span class="tf-path-title">部署模型服务</span>
        <span class="tf-path-desc">模型广场选型，一键部署推理服务</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#8e24aa" href="call-model/">
        <span class="tf-path-num">2</span>
        <span class="tf-path-title">体验与调用模型</span>
        <span class="tf-path-desc">在线对话体验，创建 API Key 调用</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#5d4037" href="build-app/">
        <span class="tf-path-num">3</span>
        <span class="tf-path-title">构建智能问答应用</span>
        <span class="tf-path-desc">搭建语料库，创建 RAG 应用</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#455a64" href="billing/">
        <span class="tf-path-num">4</span>
        <span class="tf-path-title">运营与计费</span>
        <span class="tf-path-desc">驾驶舱看运营，费用中心管计费</span>
        <span class="tf-path-go">Go →</span>
      </a>
    </div>

    使用管理员创建的账号登录后即可开始。无需本地部署，模型部署与调用全部在控制台完成。

## 前提条件

开始之前，请准备好可以访问控制台的浏览器，并按视角确认以下条件：

=== "管理员视角"

    - 已备齐[安装物料](deploy-platform.md#prereq)：离线镜像包、ISO 操作系统镜像、osPackage 离线包，以及一台作为[火种节点](../install/commercial/deploy-arch.md)的机器。
    - 使用 `Admin` 或 `Folder Admin` 权限的账号登录。
    - （创建工作集群）已准备好若干 GPU 节点，且节点操作系统和 CPU 架构一致。

=== "用户视角"

    - 管理员已完成平台部署、账号创建授权与工作集群创建（管理员视角教程 1–3）。
    - 使用管理员创建并授权的账号登录。
    - 工作集群内 GPU 资源可用。

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
