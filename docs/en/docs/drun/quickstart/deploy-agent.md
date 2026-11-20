# Create an Agent - User

This tutorial creates an OpenClaw agent instance in [ClawOS](../clawos/intro/index.md), connected to the models and API Keys of LLM Studio,
so that the agent works for you in the browser and can be integrated into office suites such as Feishu.

## Prerequisites

- You have the Workspace Editor, Workspace Admin, or Admin role.
- A namespace is already bound to the resource group of the workspace.
- An [API Key](call-model.md) has been created in the same workspace of LLM Studio.

## Steps

1. Select **ClawOS** from the left navigation bar and click **Create Instance** on the right.

2. Configure the OpenClaw instance and click **OK** in the lower right corner:

    - Set the instance name, select the cluster, namespace, and image version, configure CPU/memory resources, network, model (minimax recommended), and API Key.
    - (Optional) Enable **Integrate Feishu** and enter the Feishu App ID and App Secret.
      For details, see [Feishu Integration](../clawos/workspace/feishu.md).

3. Wait for the instance to be created with the status **Running**.

    !!! note

        In some cases, due to network fluctuation, it may take 1–2 minutes after creation before the instance is accessible.

## Access and use

Once the instance status is **Running**:

1. Click **Access Tools** -> **openclaw** or **noVNC** (a remote desktop in the browser).

2. In the OpenClaw chat interface, chat with the lobster agent and assign tasks to it.

3. For background debugging, enter the instance through the noVNC remote desktop and run commands
   (e.g. `df -h` for disk usage and `free -h` for memory).

## Verify

Send a message to the agent in the chat window and receive a reply, which means the agent is created successfully and the model pipeline is usable.

## Next step

To install and orchestrate skills for the agent, see [Skill Marketplace](../clawos/workspace/skill.md). For issues, see the [ClawOS FAQ](../clawos/faq.md).

Once the agent is running, review the operations data of the platform in [Operations Insight](operations.md).

For the complete usage of ClawOS, see the [ClawOS Quick Start](../clawos/intro/quickstart.md) and [Workspace Overview](../clawos/workspace/index.md).
