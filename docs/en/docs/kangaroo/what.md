---
hide:
  - toc
---

# What is a container registry

Container registry is a cloud-native image hosting service that supports multi-instance lifecycle management. It supports the deployment of container registry instances to any cloud-native basic environment, and supports the integration of external container registrys (Harbor Registry and Docker Registry).
Through the container registry service, you can assign the private registry space to one or more workspaces (tenants) to ensure the security of the private image, and you can also expose the registry space to all Kubernetes namespaces. The container registry cooperates with [Container Management](../kpanda/intro/WhatisKPanda.md) service helps users quickly deploy applications.

**Features**

- Container registry full lifecycle management

    Provide full lifecycle management of container registrys by hosting Harbor, including creation, editing, deletion, etc. of container registrys.

- Tenant-based application deployment

    Supports the allocation of registry space to one or more workspaces (tenants); supports independent association of workspaces (tenants) with external container registrys.

- Image scan

    Support image scanning function to identify image security risks

- Image selection

    Linked with the container management module, the image can be quickly selected through the "select image" function to complete application deployment.

**Product logical architecture**



[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/intro.md){ .md-button .md-button--primary }
[Free Trial](../dce/license0.md){ .md-button .md-button--primary }