---
hide:
  - toc
---

# Token Factory Installation Guide

This page is the main entry point for installing d.run Token Factory (hereinafter "Token Factory"): it outlines the
full installation chain, the document for each stage, and the initialization order after installation.

Token Factory is installed offline: the installer `dce5-installer` runs on a machine called the
[Bootstrap Node](./commercial/deploy-arch.md), uses Kubean to initialize the operating system and create a Kubernetes
cluster, and then deploys the product modules declared in `manifest-cloud-tokfact.yaml` to the global service cluster.
Therefore, four types of offline packages must be prepared beforehand: the offline image package, ISO operating system
images, osPackage offline packages, and optionally Addon offline packages.

!!! tip "Version note"

    Using installer v0.46.0 as an example: the versions of the installer, the offline image package, and the
    osPackage packages must match each other. For version changes, see the
    [installer Release Notes](./release-notes.md).

## Installation Workflow

There are eight stages from environment preparation to daily operations. If the installation fails, locate the cause
first, then retry from the corresponding stage. Click a stage in the diagram to jump to its document.

```mermaid
flowchart TB
    A["1 Prepare environment<br/>Architecture · Hardware · Ports"] --> B["2 Install dependencies<br/>podman · helm · skopeo · kind"]
    B --> C["3 Download offline packages<br/>Image package · ISO · osPackage"]
    C --> D["4 Edit clusterConfig.yaml<br/>Deployment mode and nodes"]
    D --> E["5 Confirm manifest-cloud-tokfact.yaml<br/>Choose the modules to install"]
    E --> F["6 Run the installer<br/>dce5-installer cluster-create"]
    F --> G{"Installation succeeded?"}
    G -- "No" --> H["Troubleshoot the installation<br/>Fix the cause and retry"]
    H --> F
    G -- "Yes" --> I["7 Access the console and request a license<br/>admin/changeme"]
    I --> J["8 Daily operations<br/>Upgrade version by version"]
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

## Next Steps

Once installed and logged in with `admin/changeme`, initialize the platform in this order; business data can be reviewed in [Cockpit](../crane/user-guide/singlepage.md) and [Billing Center](../leopard/index.md):

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
    <span class="tf-path-title">Plan Permissions</span>
    <span class="tf-path-desc">Create users, user groups, and workspaces in Global Management, and plan roles and permissions</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#00acc1" href="../kpanda/intro/">
    <span class="tf-path-num">2</span>
    <span class="tf-path-title">Create Clusters</span>
    <span class="tf-path-desc">Create worker clusters in Container Management to host inference workloads; use GPU nodes</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#43a047" href="../hydra/">
    <span class="tf-path-num">3</span>
    <span class="tf-path-title">Deploy Models</span>
    <span class="tf-path-desc">Deploy or connect models in LLM Studio, and configure Tokens and API access</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#fb8c00" href="../insight/intro/">
    <span class="tf-path-num">4</span>
    <span class="tf-path-title">Observe &amp; Operate</span>
    <span class="tf-path-desc">Verify metrics and log collection in Insight, and review business data in Cockpit as well as metering and billing in Billing Center</span>
    <span class="tf-path-go">Go →</span>
  </a>
</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
