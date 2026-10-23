# Quick Start

This guide helps you quickly create and use an OpenClaw instance on DCE.

## Prerequisites

- You have the WS Editor, WS Admin, or Admin role
- An NS is already bound to the resource group of the WS
- An API Key has already been created in the same WS of the LLM Studio

## Create an OpenClaw Instance

1. From the left navigation bar, select **ClawOS**, then click the **Create Instance** button on the right.

1. Configure the OpenClaw instance, then click **Confirm** in the bottom-right corner.

    - Set the instance name, select the target cluster, namespace, and image version, and configure the CPU/memory resources, networking, model (the minimax model is recommended), and API Key.
    - (Optional) Enable **Feishu Integration** and enter the Feishu App ID and App Secret.

    > For details on how to obtain Feishu configuration and complete the integration, see the [Feishu Integration](../workspace/feishu.md) guide.

1. Wait for the instance to be created.

## Access OpenClaw

After an instance's status shows **Running**:

1. Click **Access Tools** -> **openclaw** or **noVNC** (a remote desktop in the browser) on the right side.

2. Open the OpenClaw management page.

3. Open the noVNC management page.

!!! note

    - In some cases, due to network fluctuations, you may need to wait 1-2 minutes after creating the instance before it becomes accessible.
    - If the following prompt appears, click **Continue to Website** to use the OpenClaw agent in the chat window.

## Backend Debugging for OpenClaw

You can perform quick operations through noVNC in the instance list.

### CLI Operations

Check disk space:

```bash
df -h  # check disk space
```

Check memory details:

```bash
free -h
```

## OpenClaw FAQ

See the [FAQ](../faq.md) document.
