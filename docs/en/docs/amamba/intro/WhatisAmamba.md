# What is Application Workbench?

Application workbench is a container-based cloud native DevOps platform, which provides a unified entrypoint for creating DCE 5.0 applications. In additionally, it is built-in with multi tenants supports and cross cluster deployments.

Application workbench is designed for the process of automated delivery of enterprise applications and infrastructures. It enables full lifecycle management of applications from development to testing, deployment and operation.

=== "Multi Tenants Management"

Taking the [workspace](../../ghippo/user-guide/02Workspace/ws-folder.md) as a minimum tenant unit, supports the ability to share resources in a single cluster and across clusters:

- Weak binding clusters, so as to obtain the ability to share resources across clusters and namespaces.
- Strong cluster binding, so as to obtain the ability of exclusive resources.
- Workspace management members can create namespace resources in the associated cluster.
- Self service resource creation mode. Users can self create namespaces in the workspace to divide resources.



=== "Cloud Native Based"

Support popular cloud native applications such as kubernetes manifests, Helm, OAM,OLM, etc. And it can seamlessly integrate with SpingCloud, Dubbo and ServiceMesh frameworks to achieve SOA (Service-Oriented Architecture). In additionally, DCE 5.0 [micro service engine](../../skoala/intro/features.md) and [service mesh](../../mspider/intro/what.md), enables scaling , logging, monitoring and upgrading for applications.



=== "Efficient Continuous Integration"

You can use both Jenkins and Tekton in the same time. The pipeline can be edited simply by web UI. In the maintime, applications workbench support multiple SCM (Source Code Management).



=== "Automated Secure Progressive Delivery"

Application workbench introduces a concept of continuous deployment for cloud native, which designed for cooperate with GitOps. It integrates the progressive delivery component with Argo Rollout and supports grayscale publishing that improved the efficiency of application delivery.



!!! info

    Progressive delivery is an approach to gradually expose a new version to few initial users, and then become a larger subset to mitigate the risk of negative impacts (such as errors).
    
    Argo-Rollout Kubernetes Progressive Delivery Controller，provide powerful deployment capabilities. Including grayscale publishing, blue-green deployment, experimentation, progressive delivery and so on.

## Where the workbench is located in DCE 5.0

The application workbench has a significant role in the roadmap of DCE 5.0 as shown below.



Application workbench is developed on the basis of Container Management and Global Management. It implements the hierarchical resource management and progressive delivery with CI/CD pipelines and GitOps workflow.

[Free trial now](../../dce/license0.md){ .md-button .md-button--primary }
