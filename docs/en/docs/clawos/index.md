# OpenClaw Agent: From “Conversational” to “Action-Oriented”

## What is OpenClaw

**OpenClaw** is a new-generation open-source AI agent runtime that represents a leap in AI capabilities — no longer just passively answering questions, but actively planning tasks, invoking tools, and autonomously executing workflows, like a true digital employee handling end-to-end complex work.

| Capability Dimension | Traditional AI Assistant | OpenClaw Agent |
|---|---|---|
| Interaction Mode | Passive Q&A, single-turn responses | Active planning, multi-turn autonomous execution |
| Capability Boundary | Text-only output | Tool invocation, OS interaction, code execution |
| Use Cases | Information lookup, simple generation | End-to-end automated workflows |

**OpenClaw** provides five native capability layers:

- **User Access Layer:** Supports chat interfaces, CLI, IDE plugins, IM tools (Feishu / WeChat / DingTalk), and Web APIs  
- **Agent Core Engine:** Task planning, context management, workflow engine, sub-agent orchestration, multi-agent architecture  
- **Tool Execution Layer:** File system, terminal commands, browser control, API calls, custom skills, third-party integrations  
- **Memory & Knowledge Layer:** Short-term session memory, long-term vector storage, knowledge retrieval, cross-session persistence  
- **Model Integration Layer:** Compatible with Claude, GPT, local open-source models, enterprise private models, and OpenAI API protocols  

## Using OpenClaw on DCE

DCE now offers **ClawOS v0.1**, an enterprise-grade hosted runtime platform for OpenClaw. No need to configure environments or manually integrate models — your AI digital employee can be up and running in under 5 minutes.

For detailed steps, see the [Quick Start](./quickstart.md) guide.

### Feishu Integration

**ClawOS v0.1** natively supports seamless Feishu integration. When creating an instance, simply enable the **Feishu Integration** toggle and provide your Feishu application's **App ID** and **App Secret**.

Once configured, OpenClaw can send and receive messages, process files, and reply in group chats directly within Feishu — no need to switch interfaces.

For detailed setup instructions, see the [Feishu Integration](./feishu.md) guide.

## Typical Use Cases

### HR Resume Screening at Scale

Faced with dozens of PDF resumes in different formats, OpenClaw can automatically read, extract key technical skills, score candidates based on job requirements, and output structured evaluation reports. What used to take half a day can now be completed in minutes.





!!! note

    Resumes contain sensitive personal information (PII). DCE private deployment ensures data never leaves the internal network and prohibits sending resumes to external public cloud APIs.

### Software Development Assistant

After integrating with GitHub, configure a multi-agent architecture (Main Agent + Research + Reviewer + Codex) to let OpenClaw analyze source code, identify bugs, create pull requests, and enforce CI standards — building a fully personalized automated development orchestrator.



### Batch Document Review

Encapsulate the full workflow — “read documents → extract key data → validate rules → generate review comments” — into a reusable custom Skill using `createSkill`. With one click, process dozens of reports and output a consolidated CSV, eliminating repetitive work.

## Product Advantages

| Advantage | Description |
| --- | --- |
| One-click setup, ready out of the box | No manual configuration of environments, model integration, or permissions required. The system automatically provisions sandboxes and injects tokens. Business users can start instantly without IT involvement. |
| Secure sandbox isolation | Each OpenClaw instance runs in an isolated container sandbox powered by DaoCloud’s **zestU** kernel-level isolation technology. Even if compromised, the impact is strictly confined within the sandbox, preventing intrusion into internal networks or host file tampering. |
| Persistent data, memory never lost | The `~/.openclaw` directory is fully persisted in the DCE storage system. Conversations, configurations, and memory remain intact across restarts, pauses, or instance releases. |
| Secure and controlled model access | All model calls are routed through the DCE AI gateway with enforced security policies — no direct exposure to the public internet. Your data and conversations stay protected within the platform. |
| Full backend access | DCE provides both [SSH access and noVNC web access](quickstart.md#_4) to OpenClaw instances, supporting full CLI operations for advanced debugging and customization. |

## Features

| Feature | Status |
|---|---|
| [One-click OpenClaw instance creation](./quickstart.md#openclaw) | Available |
| [Feishu seamless integration](./feishu.md) | Available |
| Secure container sandbox isolation | Available |
| Persistent data storage | Available |
| [SSH or noVNC web access](./quickstart.md#__tabbed_1_1) | Available |
| File management and upload | Available |
| Token usage analytics and cost control | Coming soon |
| More model support | Coming soon |
| Unified instance management (admin view) | Planned |
| Audit tracking and operation replay | Planned |
