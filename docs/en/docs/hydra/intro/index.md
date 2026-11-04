---
hide:
  - toc
---

# What Is LLM Studio

LLM Studio (Hydra) is a comprehensive AI model service management platform built for enterprise users. It addresses key challenges enterprises face when adopting large models, such as deployment complexity, model selection difficulties, stability issues, and potential security risks.

By offering end-to-end lifecycle services—from model deployment to operational management—the platform helps enterprises and developers efficiently integrate large model capabilities, accelerating digital transformation and intelligent innovation.

[Read or Download the LLM Studio User Manual](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/hydra.pdf){ .md-button }

![LLM Studio architecture](images/hydra-arch.svg)

## Key Capabilities

<div class="grid cards" markdown>

- :material-rocket-launch-outline:{ .lg .middle } __One-Click Deployment and Simplified Operations__

    ---

    Both web UI and API are supported, so mainstream models go live within minutes. Dynamic inference backends such as vLLM and SGLang support real-time scaling and multi-region deployment.

    [:arrow_forward: Deploy a new model](../deploy/deploy.md)

- :material-transit-connection-horizontal:{ .lg .middle } __Traffic Management and Stability__

    ---

    Intelligent traffic policies based on weights, QPS limits, and more, plus three-level rate limiting (global, API key, tenant) to keep services stable.

    [:arrow_forward: Smart routing and rate limiting](../oam/auto-route.md)

- :material-server-network:{ .lg .middle } __Distributed Inference__

    ---

    Multi-node, multi-GPU serving for ultra-large models such as DeepSeek and GLM; compatible with NVIDIA, Ascend, Biren, Muxi, and other GPUs, with round-robin, random, and weighted load balancing.

    [:arrow_forward: Model service overview](../deploy/index.md)

- :material-chart-box-outline:{ .lg .middle } __Accurate Billing and Analytics__

    ---

    Token-level accounting covering mainstream large models; call volume and input/output token analytics by API key, model type, and time.

    [:arrow_forward: API key management](../apikey.md)

- :material-view-grid-outline:{ .lg .middle } __Unified Multimodal Management__

    ---

    The Model Plaza brings together text generation, image generation, and vision models. Send one input and compare responses from multiple models, with rich demos and integration guides.

    [:arrow_forward: Model Plaza](../index.md)

- :material-lan-connect:{ .lg .middle } __Open Ecosystem__

    ---

    An OpenAI-compatible API with rich call examples; mainstream clients such as Cherry Studio, Cline, LobeChat, and Bob work out of the box.

    [:arrow_forward: Client practices](../user-guides/index.md)

</div>

## Workflow

The platform combines the **operations management view + standard user view** to achieve unified model management, trial, and rapid deployment.
The model usage process consists of **three steps + model file download**:

```mermaid
flowchart LR
    EXT["External models<br/>DeepSeek · GLM · Qwen, etc."]
    subgraph OPS["Operations management view"]
        direction TB
        A["① Model Plaza management<br/>Import / create models"]
        B["② MaaS model management<br/>Configure trial runtime"]
        C["③ Model Serving management<br/>GPU / memory / framework"]
    end
    subgraph USER["Standard user view"]
        direction TB
        D["Model Plaza<br/>Browse published models"]
        E["Model Experience<br/>Online trial, no deployment"]
        G["Model Service<br/>Select a model to deploy"]
    end
    F["④ Model file download<br/>Dataset"]
    EXT -->|Import / create| A
    A -->|Auto-sync once published| D
    A --> B
    B -->|Manage| E
    C --> F
    F -->|Model files ready| G
```

??? note "View the original hand-drawn workflow"

    ![Platform usage process](images/OperationalLogic.png)

| Step | Operations management view | Standard user view | Documentation |
| :--- | :--- | :--- | :--- |
| ① Model Plaza management | Import or create models in **Model Plaza Management**; published models sync automatically to the user view | Browse published models in the **Model Plaza** as the entry point for trials or deployments | [Model Plaza Management](../oam/index.md) |
| ② MaaS model management | Set a model as a **MaaS model** and configure its trial runtime environment | Try configured models online in **Model Experience** without local deployment | [MaaS Model Management](../oam/maas.md) |
| ③ Model Serving management | Create deployment profiles for resources and environments, e.g. GPU/memory/runtime framework | Select a model in **Model Service** to deploy quickly without manually filling in complex parameters | [Model Serving Management](../oam/mdm.md) |
| ④ Model file download | Operations staff [download model files to designated locations](../dataset.md) as the foundation for deployment | — | [Dataset management](../dataset.md) |

## Quick Start

<style>
.hydra-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.hydra-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.hydra-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.hydra-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.hydra-path-step:last-child::after{display:none}
.hydra-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.hydra-path-title{font-weight:700;font-size:0.95rem}
.hydra-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.hydra-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.hydra-path-step::after{display:none}}
</style>

=== ":material-shield-account: Admin: deploy and operate the platform"

    <div class="hydra-path">
      <a class="hydra-path-step" style="--path-c:#2196f3" href="deploy-ws/">
        <span class="hydra-path-num">1</span>
        <span class="hydra-path-title">Deploy the platform</span>
        <span class="hydra-path-desc">Install LLM Studio in WS mode</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#00acc1" href="../oam/">
        <span class="hydra-path-num">2</span>
        <span class="hydra-path-title">Publish models</span>
        <span class="hydra-path-desc">Import or create models and publish</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#43a047" href="../oam/maas/">
        <span class="hydra-path-num">3</span>
        <span class="hydra-path-title">Configure trials</span>
        <span class="hydra-path-desc">Set up MaaS trial environments</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#fb8c00" href="../oam/mdm/">
        <span class="hydra-path-num">4</span>
        <span class="hydra-path-title">Configure serving</span>
        <span class="hydra-path-desc">Plan GPUs, memory, and frameworks</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#8e24aa" href="../dataset/">
        <span class="hydra-path-num">5</span>
        <span class="hydra-path-title">Prepare model files</span>
        <span class="hydra-path-desc">Download models with Dataset</span>
        <span class="hydra-path-go">Go →</span>
      </a>
    </div>

=== ":material-account: User: try and call models"

    <div class="hydra-path">
      <a class="hydra-path-step" style="--path-c:#2196f3" href="../">
        <span class="hydra-path-num">1</span>
        <span class="hydra-path-title">Choose a model</span>
        <span class="hydra-path-desc">Browse and compare in Model Plaza</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#00acc1" href="../exp/">
        <span class="hydra-path-num">2</span>
        <span class="hydra-path-title">Try online</span>
        <span class="hydra-path-desc">Chat and generate images in Model Experience</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#43a047" href="../deploy/deploy/">
        <span class="hydra-path-num">3</span>
        <span class="hydra-path-title">Deploy a service</span>
        <span class="hydra-path-desc">One-click model deployment</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#fb8c00" href="../apikey/">
        <span class="hydra-path-num">4</span>
        <span class="hydra-path-title">Create an API key</span>
        <span class="hydra-path-desc">Manage credentials and rate limits</span>
        <span class="hydra-path-go">Go →</span>
      </a>
      <a class="hydra-path-step" style="--path-c:#8e24aa" href="../user-guides/">
        <span class="hydra-path-num">5</span>
        <span class="hydra-path-title">Connect a client</span>
        <span class="hydra-path-desc">Cherry Studio / Cline / LobeChat</span>
        <span class="hydra-path-go">Go →</span>
      </a>
    </div>

## Security and Audit {: #security-audit }

The audit feature is a core part of the LLM Studio module. By recording key operation events, it keeps user behavior and system changes traceable to meet compliance, traceability, and security auditing requirements. The main audit items are:

| Audit category | Covered operations | Event identifiers |
| :--- | :--- | :--- |
| **Model management** | Create, update, and delete models; enable/disable the MaaS model trial feature; publish and unpublish models | `Model`, `EnabledMAASModel`, `PublishModel`, `UnPublishModel` |
| **Deployment template management** | Add and update model deployment templates | `AddDeployTemplates`, `UpdateDeployTemplates` |
| **Model provider management** | Create, update, and delete model providers | `ModelProvider` |
| **Workspace API key management** | Create and delete workspace API keys | `CreateWSAPIKey`, `DeleteWSAPIKey` |
| **Model service management** | Create and delete workspace model services; update replicas; perform service actions | `CreateWSModelServing`, `DeleteWSModelServing`, `UpdateWSModelServingReplicas`, `DoModelWSServingAction` |

These audit items cover every aspect of the model lifecycle, ensuring that every operation is traceable.

For instructions, see [Security Audit Logs](../oam/security-audit-logs.md). For the complete list of audit items, see [LLM Studio Audit Items](../../ghippo/user-guide/audit/gproduct-audit/hydra.md).

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
