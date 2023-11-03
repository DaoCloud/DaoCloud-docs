---
hide:
  - toc
---

# Basic Concept

Workbench is your one-stop-shop for deploying DCE 5.0 cloud native applications, providing lifecycle management for these applications. It lowers the entry barrier for enterprises to use cloud native apps and improves efficiency of the processes from R&D to delivery.

- Workspace

    A [Workspace](../../ghippo/user-guide/workspace/ws-folder.md) coordinates permissions of Global Management and other modules of DCE 5.0 to address resource aggregation and mapping hierarchy issues. Each workspace can be used as a resource space for one project. You can assign different resources (clsuters and namespaces) to a workspace, then users who has admin or editing access to that workspace can use and manage these resources in that workspace, such as creating an application in this workspace.

- Namespace

    A namespace is a smaller (than workspace), isolated resource space. A workspace can [have many namespaces](../../kpanda/user-guide/namespaces/createns.md), but the total resource quotas of these namespaces should not exceed the workspace quota. The namespace allocate resources with a finer granularity, limits container sizes (CPU and memory), improving resource utilization.

- Pipeline

    Use [Pipeline](../quickstart/deploy-pipeline.md) to create a customizable, visualized, and automatic delivery pipeline that helps shorten the delivery cycle and improve efficiency. The pipeline feature in Workbench is based on Jenkins implementation.

- Credential

    To allow pipeline interaction with third-party applications, the user must configure Jenkins [credentials](../user-guide/pipeline/credential.md).

- GitOps

    The core idea of GitOps is that, uses a Git repository that contains a declarative description of infrastructure in the production environment, and automatic processes to ensure that the production environment is consistent with the desired state in the repository. If you want to deploy or update an application, just update the corresponding repository and leave other things to automatic processes. This is similar to using cruise control to manage applications in production environment.

- Canary Release

    Canary Release allows you to progressively update applications, enabling the co-existence of multiple versions, release suspension, traffic percentage switching, among other features. It automates the process and eliminates manual operations in canary release.

- Toolchain Integration

    This means you can integrate your favorite DevOps tools as a toolchain, no need to log into multiple platforms and dealing with different views of these tools.
