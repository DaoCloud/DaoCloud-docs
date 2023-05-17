# What is Application Workbench?

Application Workbench (or Workbench for short) is a container-based DevOps platform for cloud-native applications. Workbench provides a unified entry point for creating applications in DCE 5.0, flexible and easy-to-use pipelines, GitOps, progressive delivery, project management, integration of tools about product lifecycle and agile development.

Workbench focuses on the process of automation application delivery and infrastructure change, providing full lifecycle management for applications from "development -> testing -> deployment -> operation". This can promote digital transformation and improve IT delivery competence and competitiveness.

=== "Hierarchical Multi-Tenant Resource Management"

Using [Workspace](../../ghippo/user-guide/workspace/ws-folder.md) as the smallest tenant unit, it not only supports the ability of exclusive resources in a single cluster but also supports the ability to share resources across clusters:

- Supports loosely bound clusters to obtain the ability to share resources across clusters and namespaces

- Supports strongly bound clusters to obtain exclusive resource capabilities

- Workspace management members can create namespace resources in associated clusters

- The self-service resource creation model allows users to create namespaces for resource isolation within the workspace.

![Multi-Tenant Resource Management](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/what01.png)

=== "Centered Around Cloud-Native Applications"

Supports "multi-form" cloud-native applications in cloud-native scenarios, including Kubernetes native applications, Helm applications, OAM applications, etc.
Can integrate microservice applications based on SpringCloud, Dubbo, and ServiceMesh frameworks to achieve microservice governance while seamlessly integrating with DCE 5.0's [Microservice Engine](../../skoala/intro/what.md) and [Service Mesh](../../mspider/intro/what.md).
Provides full lifecycle management for cloud-native applications, such as scaling, log monitoring, and application updates.

![Multi-Form Cloud Native Applications](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/what02.png)

=== "Efficient Continuous Integration"

Supports Jenkins and Tekton dual pipeline engine systems. The pipeline can be edited graphically to achieve a "what you see is what you get" effect. Applications can be built using code from different sources.

![Continuous Integration](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/what03.png)

=== "Secure Automated Progressive Delivery"

The Application Workbench introduces the concept of continuous deployment for cloud-native applications - GitOps, fully embraces GitOps, and integrates the progressive delivery component Argo Rollout to support grayscale release, thereby improving the stability and efficiency of application delivery.

![Automated Progressive Delivery](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/what04.png)

!!!info

    Progressive delivery is an approach that gradually exposes a new version of an application to an initial small subset of users, then increasingly to larger subsets, in order to mitigate the risk of negative impact (e.g., errors).
    
    Argo-Rollout Kubernetes Progressive Delivery Controller provides more powerful deployment capabilities. It includes features such as Canary release, Blue/Green deployment, update testing (experimentation), and progressive delivery.

## Position in DCE 5.0

The position of Application Workbench in DCE 5.0 is shown in the following figure.

![Position of Application Workbench in DCE 5.0](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/what00.png)

Based on container management, hierarchical resource management is achieved through global management, while cloud-native applications are added, modified, and deleted through CI/CD pipelines and GitOps processes, allowing progressive delivery.

## Deployment Method

Execute the following commands in sequence to deploy Application Workbench.

```bash
export VERSION=**** # Modify to the actual version deployed.
helm repo add mspider-release https://release.daocloud.io/chartrepo/amamba
helm repo update amamba
helm upgrade --install --create-namespace --cleanup-on-fail amamba amamba-release/amamba -n amamba-system --version=${VERSION}
```

[Download DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
[Apply for a free community experience](../../dce/license0.md){ .md-button .md-button--primary }
