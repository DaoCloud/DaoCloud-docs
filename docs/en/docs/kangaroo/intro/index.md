---
hide:
  - toc
---

# What is a Container Registry

A container registry is a cloud-native image hosting service that supports multi-instance lifecycle management. It allows deploying container registry instances to any cloud-native basic environment and integrating external container registries such as Harbor Registry and Docker Registry.

Through the container registry service, you can assign private registry space to one or more workspaces (tenants) to ensure the security of private images. You can also expose the registry space to all Kubernetes namespaces. The container registry cooperates with the [Container Management](../../kpanda/intro/index.md) service to help users quickly deploy applications.

## Features

- Container Registry Full Lifecycle Management

    The container registry provides full lifecycle management for Harbor, including creating, editing, and deleting container registries.

- Tenant-Based Application Deployment

    The registry supports allocating registry space to one or more workspaces (tenants) and independently associating workspaces (tenants) with external container registries.

- Image Scan

    The registry supports an image scanning feature to identify image security risks.

- Image Selection

    Linked with the container management module, the registry can quickly select images using the "select image" feature to complete application deployment.

[Download DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }