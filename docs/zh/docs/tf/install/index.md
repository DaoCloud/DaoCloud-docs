---
hide:
  - toc
---

# Token 工厂安装指南

本页是 d.run Token 工厂效能平台（以下简称 Token 工厂）的安装总入口，给出完整的安装链路、每个阶段对应的文档，
以及安装完成后的初始化顺序。

Token 工厂采用离线安装：在称为[火种节点](./commercial/deploy-arch.md)的机器上运行安装器 `dce5-installer`，
由它引导 Kubean 完成操作系统初始化与 Kubernetes 集群创建，再把 `manifest-cloud-tokfact.yaml` 中声明的产品模块部署到全局服务集群。
因此安装前需要备齐四类离线物料：离线镜像包、ISO 操作系统镜像、osPackage 离线包，以及可选的 Addon 离线包。

!!! tip "版本说明"

    以安装器 v0.46.0 为例，安装器、离线包与 osPackage 三者的版本必须相互匹配，各版本变化请查阅
    [安装器 Release Notes](./release-notes.md)。

## 安装流程

从环境准备到日常运维共八个阶段。安装失败时先定位原因，修正后从对应阶段重试。点击图中的阶段可直接跳转到对应文档。

```mermaid
flowchart TB
    A["1 环境准备<br/>部署架构 · 软硬件 · 端口"] --> B["2 安装依赖项<br/>podman · helm · skopeo · kind 等"]
    B --> C["3 下载离线包<br/>镜像包 · ISO · osPackage"]
    C --> D["4 配置 clusterConfig.yaml<br/>部署模式与集群节点"]
    D --> E["5 确认 manifest-cloud-tokfact.yaml<br/>选择要安装的模块"]
    E --> F["6 执行安装<br/>dce5-installer cluster-create"]
    F --> G{"安装是否成功"}
    G -- "否" --> H["查阅安装排障<br/>定位原因后重试"]
    H --> F
    G -- "是" --> I["7 访问控制台并申请授权<br/>admin/changeme"]
    I --> J["8 日常运维<br/>逐版本升级 · 变更追踪"]
    click A "commercial/deploy-requirements/"
    click B "dependency/"
    click C "start-install/"
    click D "commercial/cluster-config/"
    click E "commercial/manifest/"
    click F "start-install/"
    click H "faq/"
    click I "start-install/"
    click J "upgrade/"
```

## 下一步

安装完成并用 `admin/changeme` 登录后，建议按以下顺序完成初始化，运营数据可在[驾驶舱](../crane/user-guide/singlepage.md)与[费用中心](../leopard/index.md)中核对：

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

<div class="tf-path">
  <a class="tf-path-step" style="--path-c:#2196f3" href="../ghippo/intro/">
    <span class="tf-path-num">1</span>
    <span class="tf-path-title">规划权限</span>
    <span class="tf-path-desc">全局管理中创建用户、用户组与工作空间，规划角色权限</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#00acc1" href="../kpanda/intro/">
    <span class="tf-path-num">2</span>
    <span class="tf-path-title">创建集群</span>
    <span class="tf-path-desc">容器管理中创建工作集群承接推理负载，建议使用 GPU 节点</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#43a047" href="../hydra/">
    <span class="tf-path-num">3</span>
    <span class="tf-path-title">部署模型</span>
    <span class="tf-path-desc">大模型服务平台部署或接入模型，配置 Token 与 API 调用</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#fb8c00" href="../insight/intro/">
    <span class="tf-path-num">4</span>
    <span class="tf-path-title">观测与运营</span>
    <span class="tf-path-desc">可观测性确认指标与日志采集，驾驶舱与费用中心核对运营数据与计量计费</span>
    <span class="tf-path-go">Go →</span>
  </a>
</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
