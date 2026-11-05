---
hide:
  - toc
---

# What Is ClawOS

ClawOS is an enterprise-grade Agent runtime and governance platform for creating, managing, integrating, observing, and operating AI Agents within an organization. In the current release, the primary type of Agent managed by ClawOS is the OpenClaw instance. In the future, the platform can be extended to support more types of enterprise Agents.

In simple terms, ClawOS is the **control plane** and **governance plane** for running AI Agents within an enterprise. It is not merely an Agent inventory management platform, but integrates Agents into existing enterprise systems for permissions, networking, collaboration, auditing, and operations, making Agent capabilities **manageable, auditable, integrable, and scalable** in enterprise environments.

![ClawOS Logical Architecture](../images/clawos-arch.svg)

## Key Capabilities

<div class="grid cards" markdown>

- :material-cube-outline:{ .lg .middle } __Instance Lifecycle Management__

    ---

    Create, view, edit, and delete Agent instances in the console. Each instance corresponds to actual service resources running on cloud-native infrastructure such as Kubernetes. Operational impacts of modifying key configurations (images, resource specifications, models, API Keys) are clearly presented to users.

    [:arrow_forward: Manage OpenClaw instances](../workspace/openclaw.md)

- :material-shield-account:{ .lg .middle } __Permissions and Multi-Tenant Isolation__

    ---

    Capability boundaries follow the enterprise organizational structure: regular users can manage only their own instances, tenant administrators can view instance status within their workspaces, and platform administrators can manage global resources, policies, and configurations.

    [:arrow_forward: View ClawOS permissions](../../ghippo/permissions/clawos/)

- :material-lan-connect:{ .lg .middle } __Network Policy Governance__

    ---

    Centrally manage Agent network access boundaries: which instances can access internal services, which can only access designated APIs, which policies are enforced by default, and which are left to users.

    [:arrow_forward: Configure network policies](../admin/network-manage/)

- :material-package-variant-closed:{ .lg .middle } __Skill Management and Distribution__

    ---

    ClawHub works as an enterprise capability shelf: Skills are reviewed, published, distributed, authorized, tracked, and retired, so organizations can accumulate valuable Skills and distribute them to teams and instances by permission.

    [:arrow_forward: Browse the Skill marketplace](../workspace/skill/)

- :material-forum-outline:{ .lg .middle } __Messaging Channel Integration__

    ---

    Integrate enterprise messaging platforms such as Feishu and Microsoft Teams, enabling OpenClaw instances to send and receive messages, process files, and respond to tasks in group chats, private chats, and channels — from "an instance on a platform" to "a digital employee in a collaboration system."

    [:arrow_forward: Integrate Feishu](../workspace/feishu/)

- :material-chart-line:{ .lg .middle } __Observability and Operations__

    ---

    Provides instance status, Token usage, request counts, error rates, top users, and model distribution, along with session transcripts and trajectory logs, so administrators know whether Agents are healthy, whether costs are under control, and what exactly happened during a task.

    [:arrow_forward: View the workspace overview](../workspace/)

</div>

## Workflow

Using ClawOS involves two stages: **platform preparation** and **workspace usage**. Administrators first complete the installation, plan permissions and network policies, and publish reviewed Skills to ClawHub;
workspace users then create OpenClaw instances, access and debug them through the OpenClaw page or noVNC, integrate messaging channels such as Feishu and Teams as needed, and continuously monitor usage and cost on the overview page.

```mermaid
flowchart TB
    subgraph ADMIN["Platform Administrator"]
        direction LR
        A["① Install ClawOS<br/>Offline / online install"] --> B["② Permissions & network policy<br/>Roles · isolation"] --> C["③ Review & publish Skills<br/>ClawHub shelf"]
    end
    subgraph WS["Workspace User"]
        direction LR
        D["④ Create an instance<br/>Model · API Key · resources"] --> E["⑤ Access & debug<br/>OpenClaw · noVNC · CLI"] --> F["⑥ Integrate channels<br/>Feishu · Teams"] --> G["⑦ Monitor usage<br/>Token · calls · errors"]
    end
    ADMIN -->|Open workspaces after the platform is ready| WS
    click A href "install/"
    click B href "../admin/network-manage/"
    click C href "../admin/skillmanage-admin/"
    click D href "quickstart/"
    click E href "quickstart/"
    click F href "../workspace/feishu/"
    click G href "../workspace/"
```

| Step | Role | Description |
| ---- | ---- | ----------- |
| [① Install ClawOS](install.md) | Platform Administrator | Install ClawOS components from offline packages or Helm, and integrate with d.run or similar environments |
| [② Permissions and network policy](../admin/network-manage.md) | Platform Administrator | Plan role boundaries and define internal services and external APIs that instances can access |
| [③ Review and publish Skills](../admin/skillmanage-admin.md) | Platform Administrator | Review Skill content, publish to ClawHub, and distribute to teams by permission |
| [④ Create an instance](quickstart.md) | Workspace User | Select cluster, namespace, image, and resources; configure models, API Keys, and messaging channels |
| [⑤ Access and debug](quickstart.md) | Workspace User | Operate instances through the OpenClaw page, the noVNC remote desktop, or the CLI |
| [⑥ Integrate messaging channels](../workspace/feishu.md) | Workspace User | Configure a Feishu custom app or Teams to bring Agents into daily collaboration |
| [⑦ Monitor usage](../workspace/index.md) | Tenant Administrator | Review Token quotas and consumption, request trends, error rates, and model distribution |

## Quick Start

<style>
.clawos-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.clawos-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.clawos-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.clawos-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.clawos-path-step:last-child::after{display:none}
.clawos-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.clawos-path-title{font-weight:700;font-size:0.95rem}
.clawos-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.clawos-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.clawos-path-step::after{display:none}}
</style>

=== ":material-shield-account: Administrator: Platform Setup"

    <div class="clawos-path">
      <a class="clawos-path-step" style="--path-c:#2196f3" href="install/">
        <span class="clawos-path-num">1</span>
        <span class="clawos-path-title">Install ClawOS</span>
        <span class="clawos-path-desc">Offline package / Helm</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#00acc1" href="../../ghippo/permissions/clawos/">
        <span class="clawos-path-num">2</span>
        <span class="clawos-path-title">Permission planning</span>
        <span class="clawos-path-desc">Users · tenants · admins</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#43a047" href="../admin/network-manage/">
        <span class="clawos-path-num">3</span>
        <span class="clawos-path-title">Network policies</span>
        <span class="clawos-path-desc">Define ingress & egress</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#fb8c00" href="../admin/skillmanage-admin/">
        <span class="clawos-path-num">4</span>
        <span class="clawos-path-title">Publish Skills</span>
        <span class="clawos-path-desc">Review and publish to ClawHub</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#8e24aa" href="../admin/">
        <span class="clawos-path-num">5</span>
        <span class="clawos-path-title">Global overview</span>
        <span class="clawos-path-desc">Platform-wide usage & risks</span>
        <span class="clawos-path-go">Go →</span>
      </a>
    </div>

=== ":material-account: Workspace User: Create & Use Agents"

    <div class="clawos-path">
      <a class="clawos-path-step" style="--path-c:#2196f3" href="quickstart/">
        <span class="clawos-path-num">1</span>
        <span class="clawos-path-title">Quick start</span>
        <span class="clawos-path-desc">Create and access your first instance</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#00acc1" href="../workspace/openclaw/">
        <span class="clawos-path-num">2</span>
        <span class="clawos-path-title">Instance management</span>
        <span class="clawos-path-desc">View · edit · delete instances</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#43a047" href="../workspace/feishu/">
        <span class="clawos-path-num">3</span>
        <span class="clawos-path-title">Feishu integration</span>
        <span class="clawos-path-desc">Bring Agents into chats</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#fb8c00" href="../workspace/teams-info/">
        <span class="clawos-path-num">4</span>
        <span class="clawos-path-title">Teams configuration</span>
        <span class="clawos-path-desc">Integrate Microsoft Teams</span>
        <span class="clawos-path-go">Go →</span>
      </a>
      <a class="clawos-path-step" style="--path-c:#8e24aa" href="../workspace/">
        <span class="clawos-path-num">5</span>
        <span class="clawos-path-title">Usage monitoring</span>
        <span class="clawos-path-desc">Tokens · calls · error rate</span>
        <span class="clawos-path-go">Go →</span>
      </a>
    </div>

## OpenClaw vs. ClawOS

**OpenClaw** is a new-generation open-source AI Agent runtime designed to evolve AI from "passively answering questions" to "actively planning and executing tasks": it combines model capabilities with tool calling, file systems, terminal commands, browser automation, APIs, Skills, and multi-Agent collaboration to accomplish complex end-to-end tasks.

| Capability Dimension | Traditional AI Assistants | OpenClaw Agents |
| -------------------- | ------------------------- | --------------- |
| Interaction Model | Passive Q&A and single-turn responses | Active planning and autonomous multi-step execution |
| Capability Boundary | Text generation only | Calls tools, interacts with operating systems, executes code |
| Typical Scenarios | Information retrieval and simple generation | End-to-end automated workflows |

| Object | Positioning |
| ------ | ----------- |
| OpenClaw | The runtime object that provides task execution capabilities for Agents |
| ClawOS | The runtime and governance platform that enables Agents to run in a controlled manner within enterprises |

If each OpenClaw instance is configured, maintained, and integrated with models and tools independently by individuals, enterprises will quickly encounter uncontrolled permissions, invisible costs, inaccessible logs, and unreusable Skills. The value of ClawOS is to make distributed Agents **runnable, manageable, observable, and auditable**, transforming Agents from **personal tools** into **enterprise operational assets**.

## Typical Use Cases

### HR Resume Screening at Scale

When dealing with dozens of PDF resumes in different formats, OpenClaw can automatically read them, extract key technology stacks, rank candidates according to job requirements, and generate structured evaluation reports. What previously required half a day of manual work can now be completed in minutes.

!!! note

    Resumes contain personally identifiable information (PII). d.run private deployment ensures that data never leaves the internal network and prevents resumes from being sent to external public cloud APIs.

### Software Development Assistant

By integrating with GitHub and configuring a multi-Agent architecture (Main Agent + Research + Reviewer + Codex), OpenClaw can analyze source code, locate bugs, create pull requests, and execute CI standards, creating a fully customized automated development orchestrator.

### Batch Document Review

Package the entire workflow—"read documents → extract key data → validate rules → generate review comments"—into a reusable custom Skill (`createSkill`) and process dozens of reports with one click while generating a consolidated CSV output, eliminating repetitive work.

## Why ClawOS

| Advantage | Description |
| --------- | ----------- |
| One-Click Creation, Ready to Use | No manual environment configuration, model integration, or permission setup is required. The system automatically creates sandboxes and injects Tokens, allowing business users to start immediately without IT involvement. |
| Secure Sandbox Isolation | Each OpenClaw instance runs in an isolated container sandbox powered by DaoCloud's **zestU** kernel-level isolation technology. Even if compromised, the impact is strictly confined to the sandbox and cannot penetrate the internal network or tamper with host files. |
| Persistent Data | `/openclaw/data` is stored on a persistent volume, so OpenClaw work files and FileBrowser uploads are retained when the Pod restarts or is recreated. Files saved in noVNC under `/home/node` or other directories are not guaranteed to persist. See the [FAQ](../faq.md). |
| Secure and Controlled Model Access | All model requests are routed through the AI Gateway and governed by security policies, without exposing public endpoints. Data and conversations remain protected within the platform. |
| Full Backend Access | Provides both [SSH access and noVNC web access](quickstart.md#backend-debugging-for-openclaw), supporting full CLI operations and meeting advanced debugging and customization requirements. |

## More Resources

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __FAQ__

    ---

    Answers to common questions about instance creation and access, data persistence directories, Token quotas, and more.

    [:arrow_forward: View the FAQ](../faq.md)

- :material-book-open-page-variant:{ .lg .middle } __Upgrade and Compatibility__

    ---

    Upgrade notes and version compatibility details. Read them carefully before upgrading.

    [:arrow_forward: View upgrade notes](upgrade-notes.md)

- :material-console:{ .lg .middle } __Gateway API Access__

    ---

    Reference configuration for accessing OpenClaw instances through Gateway API.

    [:arrow_forward: View the reference](../reference/gateway-access.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
[View or Download the ClawOS User Manual](https://harbor-test2.cn-sh2.ufileos.com/docs/download/ClawOS.pdf){ .md-button .md-button--primary }
