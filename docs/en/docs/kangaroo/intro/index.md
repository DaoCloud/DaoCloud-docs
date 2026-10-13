---
MTPE: ModetaNiu
DATE: 2024-07-11
hide:
  - toc
---

# What is a Container Registry

A container registry is a cloud native image hosting service that supports multi-instance lifecycle management. 
It allows deploying container registry instances to any cloud native basic environment and integrating external 
container registries such as Harbor Registry, Docker Registry and Jfrog Registry.
Through the container registry service, you can assign private registry space to one or more workspaces (tenants) 
to ensure the security of private images. You can also expose the registry space to all Kubernetes namespaces. 
The container registry cooperates with the [Container Management](../../kpanda/intro/index.md) service to help users quickly deploy applications.

## Features

The container registry is a module included in the DCE Commercial Edition, and its features are as follows:

| Feature | Description |
| ------- | --- |
| Full Lifecycle Management | Provides full lifecycle management of the container registry through managed Harbor, including the creation, editing, and deletion of image repositories. |
| Integrated External Registries | Allows administrators to integrate external registries and allocate registry spaces to one or more workspaces (tenants); also allows workspaces to independently integrate external container registries. |
| Image Scanning | Supports image scanning to identify security risks in images. |
| Convenient Application Deployment | Interacts with the Container Management module, allowing quick image selection through the "Select Image" feature to complete application deployment. |
| Image Synchronization | Supports both manual and scheduled image synchronization. Images can be synchronized to the target repository or from the target repository to the local repository. |
| Image Reclaim | Supports setting image recycling rules to manage images in the repository. Images can be moved to the recycle bin based on certain rules either manually or on a scheduled basis. |

## Product Logic Architecture

![Architecture](../images/harbordesign01.jpg)

[Download DCE](../../download/index.md){ .md-button .md-button--primary }
[Install DCE](../../install/index.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }
