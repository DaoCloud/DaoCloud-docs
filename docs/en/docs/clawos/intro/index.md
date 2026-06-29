# What Is ClawOS

ClawOS is an enterprise-grade Agent runtime and governance platform for creating, managing, integrating, observing, and operating AI Agents within an organization. In the current release, the primary type of Agent managed by ClawOS is the OpenClaw instance. In the future, the platform can be extended to support more types of enterprise Agents.

## ClawOS: An Enterprise Agent Runtime and Governance Platform

> In simple terms, ClawOS is the **control plane** and **governance plane** for running AI Agents within an enterprise.

It is not merely an Agent inventory management platform, nor is it just a backend for creating a few intelligent agent instances. It is closer to the infrastructure of the Agent era, helping enterprises run Agents securely, reliably, and in a controlled manner while integrating them into existing enterprise systems for permissions, networking, collaboration, auditing, and operations.

If OpenClaw gives AI Agents the ability to **perform tasks**, then ClawOS answers the question of how to make that capability **manageable, auditable, integrable, and scalable** in enterprise environments.

## What Is OpenClaw

**OpenClaw** is a new-generation open-source AI Agent runtime designed to evolve AI from "passively answering questions" to "actively planning and executing tasks." OpenClaw does more than chat with users—it combines model capabilities with tool calling, file systems, terminal commands, browser automation, APIs, Skills, and multi-Agent collaboration to accomplish complex end-to-end tasks.

| Capability Dimension | Traditional AI Assistants | OpenClaw Agents |
| -------------------- | ------------------------- | --------------- |
| Interaction Model | Passive Q&A and single-turn responses | Active planning and autonomous multi-step execution |
| Capability Boundary | Text generation only | Calls tools, interacts with operating systems, executes code |
| Typical Scenarios | Information retrieval and simple generation | End-to-end automated workflows |

**OpenClaw** typically provides the following core capabilities:

* **Task Planning**: Understands user objectives and breaks them down into execution steps
* **Tool Calling**: Interacts with file systems, command lines, browsers, APIs, and third-party tools
* **Skill Extension**: Encapsulates reusable capabilities through Skills
* **Context Management**: Maintains task state throughout multi-step workflows
* **Memory and Knowledge**: Combines short-term sessions, long-term memory, and knowledge bases to complete tasks
* **Multi-Model Integration**: Connects to different foundation models or enterprise private models

OpenClaw is essentially a specific Agent runtime instance that performs work, while ClawOS is the platform that manages these OpenClaw instances.

### Relationship Between ClawOS and OpenClaw

| Object | Positioning |
| ------ | ----------- |
| OpenClaw | The runtime object that provides task execution capabilities for Agents |
| ClawOS | The runtime and governance platform that enables Agents to run in a controlled manner within enterprises |

In enterprise scenarios, a team may create multiple OpenClaw instances: some summarize Feishu messages, some process tickets, some perform knowledge base Q&A, some assist with software development, and others review documents.

If each OpenClaw instance is configured, maintained, and integrated with models and tools independently by individuals, enterprises will quickly encounter management challenges: uncontrolled permissions, invisible costs, inaccessible logs, unclear network boundaries, unreusable Skills, and unresolved incidents.

The value of ClawOS lies in making these distributed Agents **runnable, manageable, observable, and auditable**.

## Key Capabilities

The first problem ClawOS solves is **enterprise-grade Agent operations**. For individual users, the focus is usually on user experience, model intelligence, and task completion. For enterprises, the priorities shift to security, governance, cost management, integration, and operations.

### Instance Lifecycle Management

Users and administrators can create, view, edit, and delete OpenClaw instances in ClawOS. Each instance corresponds to actual service resources, typically running on cloud-native infrastructures such as Kubernetes or DCE.

When users modify key configurations such as images, resource specifications, model configurations, API Keys, or messaging channels, instance restarts or temporary unavailability may occur. Therefore, ClawOS clearly presents these operational impacts to users.

For detailed operations, see [Quick Start](./quickstart.md).

### Permissions and Multi-Tenant Isolation

ClawOS is designed for enterprise organizational structures, where different roles have different capability boundaries:

* Regular users can manage only their own instances
* Tenant administrators can view instance status within their workspaces
* Platform administrators can manage global resources, policies, and configurations

This permission model ensures that Agents do not become a "black-box tool that anyone can use arbitrarily" but are instead integrated into the enterprise's identity, role, and workspace isolation systems. For details, see [ClawOS Permissions](../../ghippo/permissions/clawos.md).

### Network Policy Governance

Once an Agent can access networks, invoke tools, and connect to systems, it must have clearly defined network boundaries. ClawOS helps enterprises manage Agent network access policies, such as:

* Which instances can access internal services
* Which instances can only access designated APIs
* Which policies are enforced by default by the platform
* Which policies can be selected by users

The more powerful an Agent becomes, the more important it is to clearly define what it can and cannot access.

### Skill Management and Distribution

Skills are a critical mechanism for extending Agent capabilities. In personal scenarios, users can install or develop Skills on their own. In enterprises, however, Skills must be reviewed, published, distributed, authorized, tracked, and retired.

Therefore, ClawHub/SkillHub in ClawOS functions more like an enterprise capability marketplace. Organizations can accumulate valuable Skills, manage them centrally, and distribute them to different teams and instances according to permissions.

### Messaging Channel Integration

Agents should not exist only in a management console. Truly valuable Agents should become part of employees' daily workflows.

ClawOS integrates with enterprise messaging platforms such as Feishu and Teams, enabling OpenClaw instances to send and receive messages, process files, and respond to tasks in group chats, private chats, and channels. In this way, an Agent evolves from "an instance on a platform" into "a digital employee in a collaboration system."

For Feishu integration steps, see [Feishu Integration](../workspace/feishu.md).

### Observability, Logging, and Operations

In enterprise environments, Agents must not only be able to respond but also be troubleshootable, traceable, and auditable. ClawOS provides information such as instance status, runtime logs, session transcripts, trajectory logs, Token usage, request counts, error rates, and alerts.

These capabilities help administrators understand whether Agents are running normally, where failures occur, whether costs are under control, and what exactly happened during a particular task execution.

## Core Value

The core value of ClawOS is not to prove that a particular Agent is more useful than ChatGPT, Claude, Codex, or Cursor—those personal AI tools solve individual productivity problems. ClawOS addresses the challenge of **using Agents at enterprise scale**.

It enables enterprises to answer questions such as:

* How many Agents are running?
* Which teams are they serving?
* Which Agents are healthy and which are not?
* Which users and instances consume the most Tokens?
* Which Skills are used most frequently?
* Which models incur the highest costs?
* Which tasks have abnormally high failure rates?
* Which operations require auditing and replay?
* Which network accesses pose risks?

In other words, ClawOS transforms Agents from **personal tools** into **enterprise operational assets**.

## Typical Use Cases

### HR Resume Screening at Scale

When dealing with dozens of PDF resumes in different formats, OpenClaw can automatically read them, extract key technology stacks, rank candidates according to job requirements, and generate structured evaluation reports. What previously required half a day of manual work can now be completed in minutes.

!!! note

    Resumes contain personally identifiable information (PII). DCE private deployment ensures that data never leaves the internal network and prevents resumes from being sent to external public cloud APIs.

### Software Development Assistant

By integrating with GitHub and configuring a multi-Agent architecture (Main Agent + Research + Reviewer + Codex), OpenClaw can analyze source code, locate bugs, create pull requests, and execute CI standards, creating a fully customized automated development orchestrator.

### Batch Document Review

Package the entire workflow—"read documents → extract key data → validate rules → generate review comments"—into a reusable custom Skill (`createSkill`) and process dozens of reports with one click while generating a consolidated CSV output, eliminating repetitive work.

## Product Advantages

| Advantage | Description |
| --------- | ----------- |
| One-Click Creation, Ready to Use | No manual environment configuration, model integration, or permission setup is required. The system automatically creates sandboxes and injects Tokens, allowing business users to start immediately without IT involvement. |
| Secure Sandbox Isolation | Each OpenClaw instance runs in an isolated container sandbox powered by DaoCloud's **zestU** kernel-level isolation technology. Even if compromised, the impact is strictly confined to the sandbox and cannot penetrate the internal network or tamper with host files. |
| Persistent Data and Durable Memory | The `~/.openclaw` directory is fully persisted in the DCE storage system. Conversations, configurations, and memories remain intact after instance restarts, pauses, or releases. |
| Secure and Controlled Model Access | All model requests are routed through the DCE AI Gateway and governed by security policies, without exposing public endpoints. Data and conversations remain protected within the platform. |
| Full Backend Access | DCE provides both [SSH access and noVNC web access](./quickstart.md#openclaw_2), supporting full CLI operations and meeting advanced debugging and customization requirements. |

## Documentation Guide

* [Installation](./install.md)
* [Quick Start](./quickstart.md)
* [Feishu Integration](../workspace/feishu.md)
* [FAQ](../faq.md)
* [Release Notes](./release-notes.md)
* [ClawOS Permissions](../../ghippo/permissions/clawos.md)

[Quick Start](./quickstart.md){ .md-button .md-button--primary }
[Feishu Integration](../workspace/feishu.md){ .md-button .md-button--primary }
