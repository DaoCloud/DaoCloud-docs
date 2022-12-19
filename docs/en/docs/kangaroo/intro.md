---
hide:
  - toc
---

# What is a mirror warehouse

Mirror Warehouse is a cloud-native mirror hosting service that supports multi-instance lifecycle management. It supports the deployment of mirror warehouse instances to any cloud-native basic environment, and supports the integration of external mirror warehouses (Harbor Registry and Docker Registry).
Through the mirror warehouse service, you can assign the private mirror space to one or more workspaces (tenants) to ensure the security of the private mirror, and you can also expose the mirror space to all Kubernetes namespaces. The mirror warehouse cooperates with [Container Management ](../kpanda/03ProductBrief/WhatisKPanda.md) service helps users quickly deploy applications.

**Features**

- Mirror warehouse full life cycle management

    Provide full lifecycle management of mirror warehouses by hosting Harbor, including creation, editing, deletion, etc. of mirror warehouses.

- Tenant-based application deployment

    Supports the allocation of mirror space to one or more workspaces (tenants); supports independent association of workspaces (tenants) with external mirror warehouses.

- mirror scan

    Support image scanning function to identify image security risks

- mirror selection

    Linked with the container management module, the image can be quickly selected through the "select image" function to complete application deployment.

**Product logical architecture**

![Logical Architecture Diagram](./images/architect.png)

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/intro.md){ .md-button .md-button--primary }
[Apply for community free experience](../dce/license0.md){ .md-button .md-button--primary }