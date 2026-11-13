---
hide:
  - toc
---

# 什么是应用工作台？

应用工作台是基于容器的 DevOps 云原生应用平台，提供了应用创建的统一入口，通过界面化表单创建多种流水线、GitOps、金丝雀、蓝绿、AB 等渐进式发布策略、项目管理、工具链集成等多种功能。

应用工作台着重企业应用自动化交付和基础设施变更的过程，提供业务应用从“开发 -> 测试 -> 部署 -> 运维”的全生命周期管理，能有效帮助企业实现数字化转型，提升企业的 IT 交付能力和竞争力。

=== "层级多租户资源管理"

    以[工作空间](../../ghippo/user-guide/workspace/ws-folder.md)作为最小的租户单元，不仅支持单集群的独享资源的能力，还支持跨集群共享资源的能力：

    - 支持弱绑定集群，从而获得跨集群、跨命名空间共享资源的能力
    - 支持强绑定集群，从而获得独享资源的能力
    - 工作空间管理成员可以在关联的集群中创建命名空间资源
    - 自助式资源创建的模式，用户可以在工作空间内自助创建命名空间来进行资源隔离

    ![多租户资源管理](../images/what01.svg)

=== "以云原生应用为中心"

    支持云原生场景下的“多形态”的云原生应用，包括 Kubernetes 原生应用、Helm 应用、OAM 应用等。
    能够接入 SpringCloud、Dubbo、ServiceMesh 框架的微服务应用，实现微服务的治理，与[微服务引擎](../../skoala/intro/index.md)、[服务网格](../../mspider/intro/index.md)无缝集成。
    支持云原生应用的全生命周期管理，例如应用的扩缩容、日志、监控查看、更新应用等等。

    ![多形态云原生应用](../images/what02.svg)

=== "高效的持续集成"

    支持 Jenkins 和 Tekton 双流水线引擎系统。采用图形化方式编辑流水线，做到所见即所得的效果。可以用不同来源的代码构建应用。

    ![持续集成](../images/what03.svg)

=== "安全自动化渐进式交付"

    应用工作台引入一种为云原生应用实现持续部署的理念 – GitOps，全面拥抱 GitOps，以集成渐进式交付组件 Argo Rollout，支持灰度发布，从而提高应用交付的稳定性和效率。

    ![自动化渐进式交付](../images/what04.svg)

!!! info

    渐进式交付是一种将应用程序的新版本逐步暴露给最初的一小部分用户，然后逐渐变得越来越大的子集的做法，以减轻负面影响（例如错误）的风险。
    
    Argo-Rollout Kubernetes Progressive Delivery Controller，提供更强大的部署能力。包括灰度发布、蓝绿部署、更新测试 (experimentation)、渐进式交付等特性。

## 在产品中的地位

以容器管理为底座，借助全局管理实现层级资源管理，以 CI/CD 流水线和 GitOps 流程增删改查云原生应用，实现渐进式交付。

![应用工作台的地位](../images/what00.svg)

## 部署方法

建议通过[商业版安装包](../../install/commercial/start-install.md)安装应用工作台，因为这样可以一次性安装包括应用工作台在内的所有模块，无需担心组件不兼容的问题。

但是，如果你想单独安装或升级应用工作台模块，依次执行以下命令即可：

```bash
export VERSION=**** # (1)!
helm repo add amamba-release https://release.daocloud.io/chartrepo/amamba
helm repo update amamba-release
helm upgrade --install --create-namespace --cleanup-on-fail amamba amamba-release/amamba -n amamba-system --version=${VERSION}
```

1. 修改为实际部署的版本

## 学习路径

<style>
.amamba-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.amamba-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.amamba-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.amamba-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.amamba-path-step:last-child::after{display:none}
.amamba-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.amamba-path-title{font-weight:700;font-size:0.95rem}
.amamba-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.amamba-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.amamba-path-step::after{display:none}}
</style>

<div class="amamba-path">
  <a class="amamba-path-step" style="--path-c:#2196f3" href="../quickstart/deploy-pipeline/">
    <span class="amamba-path-num">1</span>
    <span class="amamba-path-title">快速上手</span>
    <span class="amamba-path-desc">跑通第一条编译、构建、部署流水线</span>
    <span class="amamba-path-go">前往 →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#00acc1" href="../user-guide/pipeline/create/custom/">
    <span class="amamba-path-num">2</span>
    <span class="amamba-path-title">编排流水线</span>
    <span class="amamba-path-desc">自定义任务、模板与语法，落地 CI</span>
    <span class="amamba-path-go">前往 →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#43a047" href="../user-guide/gitops/create-argo-cd/">
    <span class="amamba-path-num">3</span>
    <span class="amamba-path-title">GitOps 交付</span>
    <span class="amamba-path-desc">声明式应用配置，持续部署到集群</span>
    <span class="amamba-path-go">前往 →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#fb8c00" href="../user-guide/release/canary-guide/">
    <span class="amamba-path-num">4</span>
    <span class="amamba-path-title">渐进式发布</span>
    <span class="amamba-path-desc">灰度、蓝绿发布，新版本平滑上线</span>
    <span class="amamba-path-go">前往 →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#8e24aa" href="../user-guide/tools/integrated-toolchain/">
    <span class="amamba-path-num">5</span>
    <span class="amamba-path-title">集成工具链</span>
    <span class="amamba-path-desc">对接 SonarQube、Harbor、Jira 等工具</span>
    <span class="amamba-path-go">前往 →</span>
  </a>
</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
[查阅《应用工作台用户手册》PDF](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/amamba.pdf){ .md-button }
