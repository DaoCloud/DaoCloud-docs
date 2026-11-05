---
MTPE: windsonsea
date: 2026-11-05
hide:
  - toc
---

# What is AI Lab

AI Lab (formerly known as Intelligent Computing) is an AI computing platform built on a cloud native
operating system, delivering an integrated software-hardware AI experience.
Leveraging DCE, it consolidates heterogeneous computing power, optimizes GPU performance, and enables
unified scheduling and operation of computing resources to maximize efficiency and reduce costs.
It also provides optimized AI development frameworks covering the complete workflow — Notebook
development, training jobs, data management, and model serving — simplifying AI development and
deployment while accelerating AI adoption across industries.

![AI Lab Logical Architecture](../images/baize-arch.svg)

## Key Capabilities

<div class="grid cards" markdown>

- :material-server-network:{ .lg .middle } __Fully Managed Computing Resources__

    ---

    Powered by DCE's robust infrastructure, AI Lab supports large-scale computing clusters and
    one-stop management of heterogeneous GPUs, with software-hardware acceleration options such as
    vGPU, pooling CPU, memory, and GPU resources.

    [:arrow_forward: Create a resource pool](../oam/resource/create.md)

- :material-database-outline:{ .lg .middle } __Data Orchestration & Management__

    ---

    Data management for the entire model development process, including dataset management,
    multi-source data access, dataset preheating, and data labeling — optimized from the underlying
    container storage engine for efficient and stable data access.

    [:arrow_forward: Manage datasets](../developer/dataset/index.md)

- :material-notebook-outline:{ .lg .middle } __Development Environment Management__

    ---

    Built for MLOps and LLMOps engineers, offering development environments such as JupyterLab and
    CodeServer, with support for custom images and one-click mounting of GPUs, datasets, and other
    resources.

    [:arrow_forward: Create a Notebook](../developer/notebooks/index.md)

- :material-run-fast:{ .lg .middle } __Training Job Management__

    ---

    Full lifecycle management of training jobs, supporting mainstream frameworks such as PyTorch,
    TensorFlow, PaddlePaddle, and MPI, with native scheduling for single-node, distributed,
    multi-node, and multi-GPU workloads.

    [:arrow_forward: Create a training job](../developer/jobs/index.md)

- :material-expansion-card:{ .lg .middle } __Model Inference Services__

    ---

    With built-in mainstream inference engines such as Triton and vLLM, create inference services
    from trained models in one click, accelerating the final step from training to production.

    [:arrow_forward: Deploy an inference service](../developer/inference/index.md)

- :material-view-dashboard-outline:{ .lg .middle } __Queue & GPU Governance__

    ---

    Associate queues with workspaces to coordinate and isolate queue resources across clusters;
    aggregate GPU resources and usage globally, with current and historical job views for GPU
    stress assessment.

    [:arrow_forward: View GPU information](../oam/gpu.md)

</div>

## Workflow

Using AI Lab involves two stages — **operations preparation** and **development**: the administrator
first creates resource pools and queues to allocate computing power to workspaces; developers then
complete the closed loop of data preparation, Notebook development, training jobs, and model serving
in the developer console.

```mermaid
flowchart TB
    subgraph OAM["Ops · Admin"]
        direction LR
        A["① Create resource pool<br/>Bind clusters & nodes"] --> B["② Create queue<br/>Link workspaces"]
    end
    subgraph DEV["Dev Console · Developer"]
        direction LR
        C["③ Prepare datasets<br/>Code / data / output"] --> D["④ Notebook dev<br/>JupyterLab · CodeServer"] --> E["⑤ Training jobs<br/>PyTorch · Tensorflow · MPI"] --> F["⑥ Inference services<br/>Triton · vLLM"]
    end
    OAM -->|Allocate to workspaces| DEV
    click A href "../oam/resource/create/"
    click B href "../oam/queue/create/"
    click C href "../developer/dataset/"
    click D href "../developer/notebooks/"
    click E href "../developer/jobs/"
    click F href "../developer/inference/"
```

| Step | Role | Description |
| ---- | ---- | ----------- |
| [① Create a resource pool](../oam/resource/create.md) | Admin | Define available CPU, memory, GPU, and other computing resources in the cluster; bind workloads and node types |
| [② Create a queue](../oam/queue/create.md) | Admin | Create queues and associate them with workspaces to coordinate and isolate queue resources across clusters |
| [③ Prepare datasets](../developer/dataset/index.md) | Developer | Create code, data, and output datasets, with multi-source access and preheating support |
| [④ Notebook development](../developer/notebooks/index.md) | Developer | Develop and debug in JupyterLab / CodeServer, with SSH access and custom images |
| [⑤ Submit training jobs](../developer/jobs/index.md) | Developer | Submit single-node or distributed training jobs and analyze them with Tensorboard |
| [⑥ Deploy inference services](../developer/inference/index.md) | Developer | Serve trained models as inference services through Triton / vLLM |

## Quick Start

<style>
.baize-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.baize-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.baize-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.baize-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.baize-path-step:last-child::after{display:none}
.baize-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.baize-path-title{font-weight:700;font-size:0.95rem}
.baize-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.baize-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.baize-path-step::after{display:none}}
</style>

=== ":material-shield-account: Admin: Prepare the environment"

    <div class="baize-path">
      <a class="baize-path-step" style="--path-c:#2196f3" href="install/">
        <span class="baize-path-num">1</span>
        <span class="baize-path-title">Install components</span>
        <span class="baize-path-desc">Deploy the required AI Lab components</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#00acc1" href="first/">
        <span class="baize-path-num">2</span>
        <span class="baize-path-title">First-time use</span>
        <span class="baize-path-desc">Select a workspace and cluster</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#43a047" href="../oam/resource/create/">
        <span class="baize-path-num">3</span>
        <span class="baize-path-title">Create a resource pool</span>
        <span class="baize-path-desc">Plan CPU, memory, and GPU</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#fb8c00" href="../oam/queue/create/">
        <span class="baize-path-num">4</span>
        <span class="baize-path-title">Create a queue</span>
        <span class="baize-path-desc">Associate workspaces and quotas</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#8e24aa" href="../oam/gpu/">
        <span class="baize-path-num">5</span>
        <span class="baize-path-title">View GPUs</span>
        <span class="baize-path-desc">Monitor load, power, and temperature</span>
        <span class="baize-path-go">Go →</span>
      </a>
    </div>

=== ":material-account: Developer: From training to inference"

    <div class="baize-path">
      <a class="baize-path-step" style="--path-c:#2196f3" href="../developer/quick-start/">
        <span class="baize-path-num">1</span>
        <span class="baize-path-title">Quick start</span>
        <span class="baize-path-desc">Full workflow from dataset to training</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#00acc1" href="../developer/notebooks/">
        <span class="baize-path-num">2</span>
        <span class="baize-path-title">Create a Notebook</span>
        <span class="baize-path-desc">Mount GPUs and datasets in one click</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#43a047" href="../developer/jobs/">
        <span class="baize-path-num">3</span>
        <span class="baize-path-title">Submit a training job</span>
        <span class="baize-path-desc">PyTorch / Tensorflow / MPI</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#fb8c00" href="../developer/dataset/">
        <span class="baize-path-num">4</span>
        <span class="baize-path-title">Manage datasets</span>
        <span class="baize-path-desc">Multi-source access and labeling</span>
        <span class="baize-path-go">Go →</span>
      </a>
      <a class="baize-path-step" style="--path-c:#8e24aa" href="../developer/inference/">
        <span class="baize-path-num">5</span>
        <span class="baize-path-title">Deploy an inference service</span>
        <span class="baize-path-desc">Triton / vLLM serving</span>
        <span class="baize-path-go">Go →</span>
      </a>
    </div>

## Best Practices & Troubleshooting

<div class="grid cards" markdown>

- :material-book-open-page-variant:{ .lg .middle } __Best Practices__

    ---

    Hands-on experience including fine-tuning ChatGLM3, submitting DeepSpeed training jobs,
    topology-aware scheduling, the checkpoint mechanism, NFS dataset preheating, and deploying
    Label Studio.

    [:arrow_forward: View best practices](../best-practice/index.md)

- :material-format-list-bulleted:{ .lg .middle } __Troubleshooting__

    ---

    Diagnosis and solutions for common issues, such as clusters missing from the dropdown list,
    Notebooks not controlled by queue quotas, and local queue initialization failures.

    [:arrow_forward: View troubleshooting](../troubleshoot/index.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
[View the AI Lab User Manual](https://harbor-test2.cn-sh2.ufileos.com/docs/download/ai-lab.pdf){ .md-button .md-button--primary }
