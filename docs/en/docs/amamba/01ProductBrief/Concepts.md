---
hide:
  - toc
---

# basic concept

The application workbench provides a unified entrance for DCE 5.0 application deployment and supports the entire lifecycle management of cloud-native applications.
It lowers the threshold for enterprises to use cloud-native applications, and improves the efficiency from enterprise software development to application delivery.

- Workspace Workspace

    Through [Workspace](../../ghippo/04UserGuide/02Workspace/ws-folder.md) to coordinate global management and sub-module permission relationship, solve resource aggregation and mapping hierarchical relationship.
    And a workspace corresponds to a project, different resources can be assigned to each workspace, and different users and user groups can be assigned.

- Namespace Namespace

    On the platform, the namespace is a smaller resource space that is isolated from each other under the workspace, and it is also the workspace for users to implement job production.
    You can [create multiple namespaces](../../kpanda/07UserGuide/Namespaces/createtens.md) under a workspace, and the total resource quota that can be occupied cannot exceed the workspace quota.
    While the namespace divides the resource quota in a finer granularity, it also limits the size of the container (CPU, memory) under the namespace, effectively improving resource utilization.

- Pipeline Pipeline

    [Pipeline](../02QuickStart/deploypipline.md) provides a visualized and customizable automatic delivery pipeline to help enterprises shorten the delivery cycle and improve delivery efficiency. Currently the pipeline is implemented based on Jenkins.

-Credential

    When the pipeline interacts with third-party applications, users need to configure Jenkins [credentials](../03UserGuide/Pipeline/Credential.md), and the pipeline can interact with third-party applications.

- GitOps

    The core idea of ​​GitOps is to use a GIt repository that contains a declarative description of the current desired (production environment infrastructure) and automate the process to ensure that the production environment is consistent with the desired state in the repository.
    If you want to deploy a new application or update an existing application, you just need to update the corresponding repository (automated process will take care of the rest). It's like using cruise control to manage your application in production.

- Grayscale release

    Grayscale release is a tool that can help users update apps incrementally. It realizes functions such as multi-version coexistence, release suspension, and traffic percentage switching, which greatly liberates manual operations in the grayscale release process, and fully automates online grayscale traffic switching.