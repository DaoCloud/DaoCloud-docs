# OpenClaw Instances

OpenClaw instances are currently the primary type of Agent managed by ClawOS. Each instance can be considered an independently running AI Agent that can invoke models, use tools, integrate with messaging channels, and perform tasks in enterprise environments.

Through the **OpenClaw Instances** module, ClawOS helps users create, access, configure, and operate these Agents. The platform currently focuses on OpenClaw instances and can be extended to support more types of enterprise Agents in the future.

## Creating an Instance

On the instance list page, click **Create Instance** in the upper-right corner to open the OpenClaw instance creation page.

### Network Configuration

Network configuration is used to generate access endpoints for the instance, including quick access, remote desktop, and file manager.

If you are unsure how to configure ports, you can use the default ports and randomly assigned NodePorts. The platform automatically allocates available access ports.

### Model Configuration

Select the primary model used by the instance. The primary model is the default model invoked by OpenClaw when executing tasks. The model can be a public model provided by the platform or a private model integrated by the workspace (tenant).

If fallback models are configured, the system automatically tries them in sequence when the primary model fails, times out, or becomes unavailable. Fallback models are primarily used to improve instance stability and are suitable for production workloads or scenarios with high availability requirements.

### API Key

Select the API Key used by the instance to invoke models. If no API Key is available, click **Create API Key** to create one.

!!! note

    If the API Key is misconfigured or becomes invalid, the instance may fail to invoke models properly.

### Configuring Messaging Channels

OpenClaw instances can integrate with enterprise messaging tools, allowing users to interact directly with Agents in Feishu or Microsoft Teams. During instance creation, you can enable messaging channels and select the desired channel type.

**Feishu**

* Supports quick configuration by scanning a QR code
* Also supports manually creating a custom enterprise application. For details, see [Feishu Integration](./feishu.md)

**Microsoft Teams**

After selecting Microsoft Teams, you need to provide:

* Client ID
* Client Secret
* Tenant ID

After the instance is created, the system generates a **Messaging endpoint** on the instance details page. Copy this address to **Configuration > Messaging endpoint** in your Microsoft Azure Bot configuration. Once configured, messages from Teams are sent to the corresponding OpenClaw instance and processed by the Agent.

## Instance Details

Click the instance name to enter the instance details page and view the status of an individual OpenClaw instance, including **Overview** and **Invocation Records**.

### Overview

The Overview page mainly includes:

* **Basic Information**: Instance name, instance ID, status, model, and creation time
* **Messaging Channels**: Whether Feishu or Teams is enabled and the corresponding Messaging endpoint
* **Token Consumption**: Today's, monthly, and cumulative Token usage
* **Usage Metrics**: Request count, success rate, and average response time
* **Behavior Analysis**: Skill invocation distribution, model usage, and more

The Overview page helps determine whether the instance is running normally, whether messaging channels are configured correctly, and whether the usage and stability of the instance are healthy.

### Invocation Records

Invocation records help you understand when an instance was invoked, what input the user provided, how many Tokens were consumed, how long the request took, and whether the invocation succeeded.

The invocation details page displays the complete execution chain of a conversation or task, including conversations, responses, tool invocations, and model outputs. Metadata for each node is displayed on the right side, including the conversation ID, span ID, start time, end time, and Token usage.

This page is primarily used to investigate the following questions:

* What did the user say?
* How did the Agent understand and respond?
* Were any tools invoked?
* Which step took the longest?
* How many Tokens were consumed by this request?
* At which step did the failure occur?

Invocation records are suitable for operations troubleshooting, cost analysis, and audit tracing. For production OpenClaw instances, it is recommended to review invocation records first whenever abnormalities occur, response times increase, Token consumption rises, or user feedback does not meet expectations.

## Common Operations

On the instance list page, you can perform the following operations on OpenClaw instances:

| Operation | Description |
| --------- | ----------- |
| **Open** | Enter the access portal of the OpenClaw instance |
| **Remote Desktop** | Access the desktop environment of the instance, suitable for troubleshooting or performing desktop-based operations |
| **File Manager** | View and manage files in the instance, such as uploading materials, downloading results, or inspecting task artifacts |
| **Edit** | Modify instance configurations such as models, fallback models, API Keys, messaging channels, or resource specifications. Some changes may trigger an instance restart, during which the instance will be temporarily unavailable |
| **Restart** | Used when the instance is abnormal, configuration changes have not taken effect, or the environment needs to be reloaded |
| **Shut Down** | Stops the instance. After shutdown, the instance is inaccessible and no longer consumes runtime resources |
| **Delete** | Removes the associated runtime resources. Before deletion, ensure that there are no files, configurations, or task results that need to be retained |
