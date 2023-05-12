---
hide:
  - toc
---

# Basic concept

The application Workbench provides a unified entry point for DCE 5.0 application deployment and supports lifecycle management of cloud native applications. It lowers the threshold for enterprises to use cloud native applications and improves the efficiency from enterprise software research and development to application delivery.

- Workspace

    Use [Workspace](../../ghippo/user-guide/workspace/ws-folder.md) to coordinate the permission relationship between global management and submodules to resolve the resource aggregation and mapping hierarchy. And each workspace corresponds to a project. You can assign different resources to each workspace and assign different users and user groups.

- Namespace

    A namespace on a platform is a smaller resource space that is isolated from each other under the workspace, and it is also the workspace where the user implements job production. A workspace can [contain many namespaces](../../kpanda/user-guide/namespaces/createns.md), but the total number of available resource quotas cannot exceed the workspace quota. The namespace divides resource quotas in a finer granularity and limits the size of containers (CPU and memory) in the namespace, effectively improving resource utilization.

- Assembly line Pipeline

    [Pipeline](../quickstart/deploy-pipeline.md) provides a visual and customizable automatic delivery pipeline to help enterprises shorten delivery cycle and improve delivery efficiency. The current pipeline is based on Jenkins implementation.

- Credential

    When the pipeline interacts with third-party applications, Jenkins [credentials](../user-guide/pipeline/credential.md) needs to be configured by the user to enable the pipeline to interact with third-party applications.

- GitOps

    The core idea of GitOps is to use a GIt repository that contains a declarative description of the currently expected (production environment infrastructure) and automate the process to ensure that the production environment is consistent with the desired state in the repository. If you want to deploy a new application or update an existing one, you just need to update the appropriate repository (the automated process takes care of that). This is like using cruise control to manage applications in production.

- Grayscale release

    Grayscale publishing is a tool that helps users update their applications incrementally. It realizes multiple version coexistence, release suspension, traffic percentage switching and other functions, greatly liberates the manual operation in the gray release process, and fully automates the online gray traffic switching.

- Tool chain integration

    Integrating DevOps toolchains allows teams to bring existing tools they already know and use into the application workbench. This avoids logging into multiple platforms and dealing with the difficulty of not having a unified view across different tools.
