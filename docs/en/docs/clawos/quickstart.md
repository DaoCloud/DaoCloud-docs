# Quick Start

This guide helps you quickly create and use an OpenClaw instance.

## Prerequisites

- A DCE platform account  
- Real-name verification completed  
- Sufficient account balance or vouchers  

## Create an OpenClaw Instance

1. From the left navigation bar, select **ClawOS**, then click **Create Instance** on the right.

2. Configure the OpenClaw instance:

    - Set an English name, choose the target cluster, namespace, image version, and configure CPU/memory resources, networking, model settings, and API keys  
    - (Optional) Enable **Feishu Integration** and provide the Feishu App ID and App Secret  

    Click **Confirm** in the bottom-right corner.

    

    > For details on how to obtain Feishu configuration and complete integration, see the [Feishu Integration](./feishu.md) guide.

3. Wait for the instance to be created.

    

## Access OpenClaw

Once the instance status shows **Running**:

1. Click **Access Tools** → **openclaw** on the right side.

    

2. Open the OpenClaw management interface.

    

!!! note

    - In some cases, due to network delays, it may take 1–2 minutes after creation before the instance becomes accessible.  
    - If you see a warning prompt, click **Continue to Website** to enter the chat interface and start using the OpenClaw agent.

    

## Backend Debugging for OpenClaw

DCE provides multiple ways to access the backend, including SSH login and web-based noVNC access.

=== "Method 1: SSH Login"

    Access the OpenClaw secure sandbox via SSH.

    

=== "Method 2: Web VNC Client"

    Access the backend via a web-based VNC client.

    

### CLI Operations

Before using the OpenClaw CLI, switch to the `node` user:

```bash
su node  # switch to node user
```

List installed skills:

```bash
openclaw skills list
```



## FAQ

See the [FAQ](./faq.md) for common questions.
