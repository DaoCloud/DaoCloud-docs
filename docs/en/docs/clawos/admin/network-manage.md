# Network Policy Management

ClawOS Network Policy Management productizes Kubernetes network isolation capabilities into reusable policy templates. Platform administrators can predefine network access boundaries, and users can select or automatically apply corresponding policies when creating OpenClaw instances. After an instance is created, ClawOS automatically provisions the underlying network policies to restrict inbound or outbound access.

This capability is suitable for enterprise environments that require security boundaries for Agent runtimes, for example:

* Restricting OpenClaw instances from accessing sensitive internal network segments
* Controlling access to the public Internet
* Allowing access to specific databases or API services
* Isolating instances belonging to different users

## Use Cases

* Restricting OpenClaw instances from accessing enterprise internal network segments
* Providing different network isolation policies for OpenClaw instances with different security levels
* Converting platform security baselines into default policies that automatically take effect when instances are created
* Providing optional network policy templates for instances with special access requirements

## Roles and Permissions

### Platform Administrators

Platform administrators can perform the following operations:

* Create, edit, enable, and disable network policy templates
* Configure whether a template is the platform default policy

### Workspace Members

Workspace members can perform the following operations:

* View available network policy templates when creating an OpenClaw instance
* Select optional network policies allowed by the platform
* View the network policies currently enabled for an instance
* Navigate to Container Management to create custom NetworkPolicies based on their permissions

!!! note

    Regular users cannot directly edit network policy templates created by platform administrators.

## Network Policy Types

Network policy templates in ClawOS can be categorized into the following types.

### Platform Default Policies

Platform default policies are configured by platform administrators and define the security baseline that OpenClaw instances must comply with at runtime.

* Default policies are **automatically enabled** when creating an OpenClaw instance and cannot be disabled by users
* Typically used to ensure overall platform security

### User-Selectable Policies

User-selectable policies are created by platform administrators and can be selected by users as needed when creating OpenClaw instances.

* Users can only choose whether to enable the policy and **cannot modify** its content

### Custom Network Policies

When built-in platform policies cannot satisfy specific scenarios, users can create custom network policies on the native **NetworkPolicy** page in Container Management, provided they have the required permissions (users with Namespace edit permissions can create them).

## Creating a Network Policy Template

1. Click **Create Network Policy Template** in the upper-right corner of the page to enter the creation page.
2. Fill in the template information and configure access rules as prompted.
3. Click **Save** after the configuration is complete.

### Selecting the Policy Type

**Platform Default Policy**

* Automatically takes effect when creating an OpenClaw instance and cannot be disabled by users
* Suitable for mandatory platform security rules, for example:

    * Denying access to sensitive internal network segments
    * Denying access to core cluster services
    * Preserving necessary DNS resolution capabilities

**User-Selectable Policy**

* Displayed on the OpenClaw instance creation page, allowing users to enable it as needed
* Suitable for scenario-specific rules, for example:

    * Allowing access to model services
    * Allowing access to enterprise knowledge bases
    * Allowing access to Teams or Feishu messaging channels
    * Allowing access to designated business systems

### Configuring Access Rules

Policy configuration is divided into **Ingress Policies** and **Egress Policies**. For a source Pod to successfully connect to a target Pod, both the egress policy of the source Pod and the ingress policy of the target Pod must allow the connection. If either side denies the connection, the connection will fail.

Click **➕** to start configuring policies. Multiple policies can be configured. The effects of multiple network policies are cumulative, and a connection can be established only when all applicable network policies permit it.

| ConfigMap | Description | Purpose |
| ------------------- | ---------- | -------- |
| **podSelector** | Select specific Pods | Allow or restrict access to services with specified labels |
| **namespaceSelector** | Select specific namespaces | Allow or restrict access to services in a specific namespace |

!!! note

    After saving, the template appears in the network policy template list. If **Enabled** is selected during creation and the template is configured as a **Platform Default Policy**, it is automatically enabled immediately for both existing and future OpenClaw instances and cannot be disabled by users. If you are unsure about the policy behavior, clear the **Enabled** option during creation.

## Using Network Policies When Creating an OpenClaw Instance

Navigation path: **OpenClaw Instances** → **Create Instance** → **Network Policies**

For related operations, see [OpenClaw Instances](../workspace/openclaw.md).

### Platform Default Policies

* **Enabled by default and cannot be disabled**
* These policies define the security baseline configured by platform administrators and must be followed by all instances

### Optional Policies

* Users can select policies as needed based on the purpose of the instance

### Custom Policies

If neither platform default policies nor optional policies meet the requirements of an OpenClaw instance, users can use the shortcut link to create a native **NetworkPolicy**.

!!! note

    Native NetworkPolicies created afterward **will not** appear in the network policy drop-down list of OpenClaw instances.

## Notes

* **Ingress Policies** control "who can access the current instance"
* **Egress Policies** control "which destinations the current instance can access"
* `podSelector` is used to select Pods with specific labels
* `namespaceSelector` is used to select namespaces with specific labels
* Users cannot disable platform default policies
* Users can select optional policies as needed
* Modifying network policies may affect model invocation, knowledge base access, or message channel communications. Proceed with caution.
