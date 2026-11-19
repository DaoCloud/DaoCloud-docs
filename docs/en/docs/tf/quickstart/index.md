---
hide:
  - toc
---

# Quick Start

Quick Start is a series of hands-on labs that help you experience the full workflow of Token Factory in a short time: deploying the platform, onboarding compute, producing Tokens, and running operations and billing. The tutorials are organized into two learning paths by role:

- Admin view: deploy the platform and onboard compute;
- User view: deploy models, build applications, and manage operations and billing.

Complete the tutorials in order. Each one works independently and helps you get familiar with the core features of Token Factory.

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

=== "Admin view"

    <div class="tf-path">
      <a class="tf-path-step" style="--path-c:#2196f3" href="deploy-platform/">
        <span class="tf-path-num">1</span>
        <span class="tf-path-title">Install Token Factory</span>
        <span class="tf-path-desc">Run the installer on the seed node for offline installation</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#00acc1" href="init-users/">
        <span class="tf-path-num">2</span>
        <span class="tf-path-title">Create Users and Workspaces</span>
        <span class="tf-path-desc">Plan the multi-tenant system and grant permissions</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#43a047" href="join-cluster/">
        <span class="tf-path-num">3</span>
        <span class="tf-path-title">Create a Work Cluster</span>
        <span class="tf-path-desc">Attach GPU nodes to host inference workloads</span>
        <span class="tf-path-go">Go →</span>
      </a>
    </div>

    After these three steps, the platform is ready for use and compute is in place. Admins can also continue with the tutorials in the user view to explore the full capabilities of the platform.

=== "User view"

    <div class="tf-path">
      <a class="tf-path-step" style="--path-c:#2196f3" href="deploy-model/">
        <span class="tf-path-num">1</span>
        <span class="tf-path-title">Deploy a Model Service</span>
        <span class="tf-path-desc">Pick a model in the gallery and deploy inference with one click</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#00acc1" href="call-model/">
        <span class="tf-path-num">2</span>
        <span class="tf-path-title">Try Out and Call Models</span>
        <span class="tf-path-desc">Chat online and create an API Key for invocation</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#43a047" href="build-app/">
        <span class="tf-path-num">3</span>
        <span class="tf-path-title">Build an Intelligent App</span>
        <span class="tf-path-desc">Set up a corpus and create a RAG application</span>
        <span class="tf-path-go">Go →</span>
      </a>
      <a class="tf-path-step" style="--path-c:#fb8c00" href="billing/">
        <span class="tf-path-num">4</span>
        <span class="tf-path-title">Operations and Billing</span>
        <span class="tf-path-desc">Dashboard for operations, Cost Center for billing</span>
        <span class="tf-path-go">Go →</span>
      </a>
    </div>

    Sign in with the account created by the admin and start right away. No local deployment is required; model deployment and invocation are all done in the console.

## Prerequisites

Before you start, prepare a browser that can access the console, and confirm the following by view:

=== "Admin view"

    - Prepare [installation materials](deploy-platform.md#prereq): the offline image package, the ISO OS image, the osPackage offline package, and a machine to serve as the [seed node](../install/commercial/deploy-arch.md).
    - Sign in with an account that has the `Admin` or `Folder Admin` permission.
    - (Create a Work Cluster) Prepare several GPU nodes with the same OS and CPU architecture.

=== "User view"

    - The admin has completed the admin view tutorials 1–3: platform deployment, user creation and authorization, and work cluster creation.
    - Sign in with the account created and authorized by the admin.
    - GPU resources are available in the work cluster.

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Explore Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Explore d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
