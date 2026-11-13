---
MTPE: windsonsea
date: 2025-08-06
hide:
  - toc
---

# What is Workbench?

Workbench is a container-based DevOps cloud native application platform.
It provides a unified entry point for creating applications in DCE.
It offers various functionalities such as graphical form-based creation
of multiple pipelines, GitOps, canary deployments, blue/green deployments,
AB testing, project management, and toolchain integration.

Workbench focuses on automating the delivery of enterprise applications
and infrastructure changes. It provides end-to-end lifecycle management for business
applications from "development -> testing -> deployment -> operation". It effectively
helps enterprises achieve digital transformation and improve IT delivery capabilities and competitiveness.

=== "Hierarchical Multi-Tenant Resource Management"

    Using [Workspace](../../ghippo/user-guide/workspace/ws-folder.md) as the smallest unit of tenancy, it supports both dedicated resources within a single cluster and shared resources across clusters:

    - Supports loosely coupled clusters to share resources across namespaces.
    - Supports tightly coupled clusters to provide dedicated resources.
    - Workspace members can create namespace resources in associated clusters.
    - Self-service resource creation allows users to create namespaces within workspaces for resource isolation.

    ![Multi-tenant management](../images/what01.svg)

=== "Cloud-Native Applications as a Center"

    Supports "polyform" cloud native applications in cloud native scenarios, including Kubernetes native applications, Helm apps, and OAM applications.
    Can integrate microservice applications based on SpingCloud, Dubbo, and ServiceMesh frameworks to achieve microservice governance. Seamlessly integrates with DCE's [Microservice Engine](../../skoala/intro/index.md) and [Service Mesh](../../mspider/intro/index.md).
    Provides lifecycle management for cloud native applications, such as scaling, logging, monitoring, and application updates.

    ![Cloud native apps](../images/what02.svg)

=== "Efficient Continuous Integration"

    Supports Jenkins and Tekton as dual pipeline engine systems. Allows graphical editing of pipelines with a WYSIWYG effect. Can build applications from different code sources.

    ![CI](../images/scenarios01.svg)

=== "Secure Automated Progressive Delivery"

    Workbench embraces the GitOps concept for continuous deployment of cloud native applications. It fully integrates with progressive delivery component Argo Rollout to support canary deployments, improving application delivery stability and efficiency.

    ![Progressive CD](../images/what04.svg)

!!! info

    Progressive delivery is an approach to expose a new version of an application gradually to an initially small portion of users, gradually expanding to larger subsets, in order to mitigate risks such as errors.
    
    Argo-Rollout Kubernetes Progressive Delivery Controller provides powerful deployment capabilities, including canary releases, blue/green deployments, experimentation, and progressive delivery features.

## Positioning in DCE

Built on container management, hierarchical resource management through global management,
creating and managing cloud native applications with CI/CD pipelines and GitOps processes,
facilitating progressive delivery.

![Workbench Role in DCE](../images/what00.svg)

## Deploy

It is recommended to install Workbench using the
[DCE Enterprise Package](../../install/commercial/start-install.md),
as it installs all modules of DCE at once, without worrying about component compatibility.

However, if you want to install or upgrade the Workbench module separately, run the following command successively:

```bash
export VERSION=**** # (1)!
helm repo add amamba-release https://release.daocloud.io/chartrepo/amamba
helm repo update amamba-release
helm upgrade --install --create-namespace --cleanup-on-fail amamba amamba-release/amamba -n amamba-system --version=${VERSION}
```

1. Replace with the actual version to be deployed

## Learning Path

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
    <span class="amamba-path-title">Quick Start</span>
    <span class="amamba-path-desc">Run your first build-and-deploy pipeline</span>
    <span class="amamba-path-go">Go →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#00acc1" href="../user-guide/pipeline/create/custom/">
    <span class="amamba-path-num">2</span>
    <span class="amamba-path-title">Build Pipelines</span>
    <span class="amamba-path-desc">Custom tasks, templates and syntax for CI</span>
    <span class="amamba-path-go">Go →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#43a047" href="../user-guide/gitops/create-argo-cd/">
    <span class="amamba-path-num">3</span>
    <span class="amamba-path-title">GitOps Delivery</span>
    <span class="amamba-path-desc">Declarative configs, continuous deployment</span>
    <span class="amamba-path-go">Go →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#fb8c00" href="../user-guide/release/canary-guide/">
    <span class="amamba-path-num">4</span>
    <span class="amamba-path-title">Progressive Delivery</span>
    <span class="amamba-path-desc">Canary and blue-green releases, smooth rollout</span>
    <span class="amamba-path-go">Go →</span>
  </a>
  <a class="amamba-path-step" style="--path-c:#8e24aa" href="../user-guide/tools/integrated-toolchain/">
    <span class="amamba-path-num">5</span>
    <span class="amamba-path-title">Integrate Tools</span>
    <span class="amamba-path-desc">Connect SonarQube, Harbor, Jira and more</span>
    <span class="amamba-path-go">Go →</span>
  </a>
</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
