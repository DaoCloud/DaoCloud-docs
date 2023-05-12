# What is an application workbench?

The Application Workbench is a container-based cloud native application platform for DevOps. It provides a unified entry point for DCE 5.0 application creation, a comprehensive hierarchical multi-tenant solution, and supports resource deployment across clusters.

Application workbench focuses on the process of automatic delivery and infrastructure change of enterprise applications, and provides the full life cycle management of business applications from "development -> testing -> deployment -> operation and maintenance". IT can effectively help enterprises realize digital transformation and improve the IT delivery capability and competitiveness of enterprises.

=== "Hierarchical Multi-tenant Resource Management"

If [Workspace](../../ghippo/user-guide/workspace/ws-folder.md) is used as the smallest tenant unit, resources can be shared across clusters as well as in a single cluster.

- Weakly bound clusters are supported, enabling resources to be shared across clusters and namespaces

- Support for strongly binding clusters to obtain exclusive resources

- Workspace management members can create namespace resources in associated clusters

- Self-service resource creation mode. Users can create namespaces in the workspace to isolate resources

<!--![]()screenshots-->

=== "Cloud native app centric"

Supports "multi-form" cloud native applications in cloud native scenarios, including Kubernetes native applications, Helm applications, OAM applications, etc. It can access micro-service applications of SpingCloud, Dubbo and ServiceMesh frameworks to realize micro-service governance and seamlessly integrate with [Microservice Engine](../../skoala/intro/what.md) and [Service Mesh](../../mspider/intro/what.md) of DCE 5.0. Supports the full life cycle management of cloud native applications, such as application expansion and shrinkage, logging, monitoring, and updating.

<!--![]()screenshots-->

=== "Efficient continuous integration"

Support Jenkins and Tekton dual pipelined engine systems. Use graphic editing pipeline to achieve the effect of what you see is what you get. Applications can be built from different sources of code.

<!--![]()screenshots-->

=== "Incremental Delivery of security Automation"

The application Workbench introduces a concept of continuous deployment for cloud native applications -- GitOps. It fully embraces GitOps to integrate the progressive delivery component Argo Rollout and support grayscale publishing, thus improving the stability and efficiency of application delivery.

<!--![]()screenshots-->


## Status in DCE 5.0

The status of the application workbench in DCE 5.0 is shown below.

<!--![]()screenshots-->

With container management as the base, it realizes hierarchical resource management with the help of global management, and uses CI/CD pipeline and GitOps process to add, delete, modify and check cloud native applications to achieve progressive delivery.

## Deployment method

Run the following commands in sequence to deploy the VM.

```bash
export VERSION=**** # Change to version you need to deploy
helm repo add mspider-release https://release.daocloud.io/chartrepo/amamba
helm repo update amamba
helm upgrade --install --create-namespace --cleanup-on-fail amamba amamba-release/amamba -n amamba-system --version=${VERSION}
```

[Download DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }[Install DCE 5.0](../../install/intro.md) { .md-button .md-button--primary }[Free Try](../../dce/license0.md) { .md-button .md-button--primary }
