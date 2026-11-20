---
hide:
  - toc
---

# Quick Start

Quick Start includes a series of hands-on tutorials that help you quickly experience the features of d.run AI Operating System, from installation, compute onboarding, and model deployment to model training, agents, and operations insight. Two learning paths are provided by role:

- Admin view: deploy the platform and onboard compute;
- User view: deploy models, call models, train models, create agents, and review operations.

Complete the tutorials in order. Each tutorial can be performed independently and helps you quickly get familiar with the core features of d.run AI Operating System.

<style>
.qs-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.qs-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.qs-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.qs-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.qs-path-step:last-child::after{display:none}
.qs-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.qs-path-title{font-weight:700;font-size:0.95rem}
.qs-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.qs-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.qs-path-step::after{display:none}}
</style>

=== "Admin view"

    <div class="qs-path">
      <a class="qs-path-step" style="--path-c:#2196f3" href="deploy-platform/">
        <span class="qs-path-num">1</span>
        <span class="qs-path-title">Install d.run AI Operating System</span>
        <span class="qs-path-desc">Run the installer on the seed node for offline installation</span>
        <span class="qs-path-go">Go →</span>
      </a>
      <a class="qs-path-step" style="--path-c:#00acc1" href="init-users/">
        <span class="qs-path-num">2</span>
        <span class="qs-path-title">Create Users and Workspaces</span>
        <span class="qs-path-desc">Plan a multi-tenant system and grant permissions</span>
        <span class="qs-path-go">Go →</span>
      </a>
      <a class="qs-path-step" style="--path-c:#43a047" href="join-cluster/">
        <span class="qs-path-num">3</span>
        <span class="qs-path-title">Create a Work Cluster</span>
        <span class="qs-path-desc">Attach GPU nodes to host AI workloads</span>
        <span class="qs-path-go">Go →</span>
      </a>
    </div>

    After the three steps above, the platform is ready to use and compute is onboarded. As an admin, you can also continue with the tutorials in the user view to explore the full capabilities of the platform.

=== "User view"

    <div class="qs-path">
      <a class="qs-path-step" style="--path-c:#2196f3" href="deploy-model/">
        <span class="qs-path-num">1</span>
        <span class="qs-path-title">Deploy a Model Service</span>
        <span class="qs-path-desc">Pick a model from the gallery and deploy it in one click</span>
        <span class="qs-path-go">Go →</span>
      </a>
      <a class="qs-path-step" style="--path-c:#00acc1" href="call-model/">
        <span class="qs-path-num">2</span>
        <span class="qs-path-title">Try Out and Call Models</span>
        <span class="qs-path-desc">Try models online and call them with an API Key</span>
        <span class="qs-path-go">Go →</span>
      </a>
      <a class="qs-path-step" style="--path-c:#43a047" href="train-model/">
        <span class="qs-path-num">3</span>
        <span class="qs-path-title">Train Models in AI Lab</span>
        <span class="qs-path-desc">Datasets, Notebook debugging, and training jobs</span>
        <span class="qs-path-go">Go →</span>
      </a>
      <a class="qs-path-step" style="--path-c:#fb8c00" href="deploy-agent/">
        <span class="qs-path-num">4</span>
        <span class="qs-path-title">Create an Agent</span>
        <span class="qs-path-desc">Deploy an agent instance and integrate office suites such as Feishu</span>
        <span class="qs-path-go">Go →</span>
      </a>
      <a class="qs-path-step" style="--path-c:#8e24aa" href="operations/">
        <span class="qs-path-num">5</span>
        <span class="qs-path-title">Operations Insight</span>
        <span class="qs-path-desc">Review end-to-end token operations in the Cockpit</span>
        <span class="qs-path-go">Go →</span>
      </a>
    </div>

    Sign in with the account created by the admin to get started. No local deployment is required; model deployment and invocation are all completed in the console.

## Prerequisites

Before you start, prepare a browser that can access the console, and confirm the following by view:

=== "Admin view"

    - Installation materials are ready: the offline image package, the ISO OS image, the osPackage offline package, and a machine that serves as the [seed node](../install/commercial/deploy-arch.md). See [prerequisites](deploy-platform.md#prereq) for details.
    - Sign in with an account that has the `Admin` or `Folder Admin` role.
    - (Creating a work cluster) Several GPU nodes are ready, and the nodes run the same OS and CPU architecture.

=== "User view"

    - The admin has completed platform deployment, account creation and authorization, and work cluster creation (admin tutorials 1–3).
    - Sign in with the account created and authorized by the admin.
    - GPU resources are available in the work cluster.
    - (AI Lab training) A StorageClass with `ReadWriteMany` access mode (NFS or JuiceFS recommended) is configured in the cluster.

[Download Center](https://docs.daocloud.io/download/){ .md-button }
[Learn about Token Factory](https://docs.daocloud.io/tf/){ .md-button }
[Learn about d.run AI Operating System](https://docs.daocloud.io/drun/){ .md-button }
