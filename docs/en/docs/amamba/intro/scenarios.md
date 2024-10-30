# Use Cases and Benefits

The workbench is a module that enables continuous delivery of applications through methods such as pipelines, GitOps, and Jenkins. It provides a unified entry point for application deployment in DCE 5.0 and supports the entire lifecycle management of cloud native applications. This reduces the barriers for enterprises to adopt cloud native applications and improves the efficiency of software development to application delivery.

## Use Cases

The workbench is suitable for the following scenarios:

- Pipeline for Continuous Delivery

    For complex business systems, each phase, from project creation, compilation, building, unit tests, integrated tests, pre-production verification, to production release, requires a lot of manpower and time, and is prone to human errors. Continuous Integration/Continuous Delivery (CI/CD) can solve this problem by standardizing and automating the process, using code changes as a flow unit, based on the release pipeline, connecting all features of development, testing, and operations, to continuously, quickly, and reliably deliver applications.

    ![CD](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/scenarios01.png)

- Cloud native CD Based on GitOps and Pipelines

    Workbench incorporates the GitOps concept and Argo CD, an open-source software, to deploy applications in Kubernetes.
    Users only need to submit YAML files to the code repository. GitOps can automatically detect the changes in the YAML files and, with the help of merge requests in the code repository, automatically push these changes to the cluster, without the need to learn the deployment commands of Kubernetes or operate the cluster directly.

    ![gitops](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/scenarios02.png)

## Benefits

With years of leading experience in cloud native field, DaoCloud developed a brand-new Workbench that boasts strong competitiveness:

- Enterprise-level CI/CD

    With containerized workflows, Workbench provides continuous integration, continuous delivery, and horizontal scaling, to run thousands of concurrent users and pipelines in a high availability (HA) environment.

- Cloud native Infrastructure

    Workbench containerized the environment of building applications, customized resources such as building machines, ensuring pipeline-level resource isolation. It also supports deployment of multiple types of applications, simplifying the delivery of cloud native applications.

- Higher R&D Efficiency

    Declarative steps are encapsulated in a visualized pipeline building environment, so that you can easily create complicated pipelines without scripts with fool-proof UI guides. Environments can be automatically created or deleted according to resource sizes to avoid waste.

- Canary Release

    Workbench supports progressive delivery with canary release, blue/green release, and A/B test policies, ensuring a stable rollout of new features.

    For example, if an application's release policy is configured as AB Test, where version A should accept 80% traffic and version B 20% traffic. With canary release, both versions of the application are available for processing requests, allowing for easy statistics of the distribution ratio of different application versions.

- GitOps

    Workbench provides progressive delivery based on Kubernetes declarative GitOps. You can deploy automated application deployment and lifecycle management with version control tools.
  
- [Pipeline as code](../quickstart/deploy-pipeline.md)

    Workbench provides declarative pipelines. It is easy to create a pipeline with standardized UI forms. Its configuration also supports version control, modularization, reusability, and declarative syntax.

- Comprehensive Integration

    Workbench integrated popular DevOps tools in the community. Steps in a single pipeline can run on nodes that have multiple operating systems and architectures. It supports independent deployment on public clouds, private clouds, or hosts and can integrate well with self-owned systems and platforms. It also supports integration with mainstream software in the industry, such as Kubernetes, GitLab, SonarQube, and Harbor.

- Experience Accumulation

    After years of cultivation in the cloud native field, DaoCloud has extensive practical experience in industries such as finance, e-commerce, and manufacturing. It can provide stable and reliable IT delivery production lines to help enterprises build a platform suitable for integrated R&D and operation.

## Concepts

| Concepts | Description |
|--------- |-------------|
| Workspace | A [Workspace](../../ghippo/user-guide/workspace/ws-folder.md) coordinates permissions of Global Management and other modules of DCE 5.0 to address resource aggregation and mapping hierarchy issues. Each workspace can be used as a resource space for one project. You can assign different resources (clusters and namespaces) to a workspace, then users who have admin or editing access to that workspace can use and manage these resources in that workspace, such as creating an application in this workspace. |
| Namespace | A namespace is a smaller (than workspace), isolated resource space. A workspace can [have many namespaces](../../kpanda/user-guide/namespaces/createns.md), but the total resource quotas of these namespaces should not exceed the workspace quota. The namespace allocates resources with a finer granularity, limits container sizes (CPU and memory), improving resource utilization. |
| Pipeline | Use [Pipeline](../quickstart/deploy-pipeline.md) to create a customizable, visualized, and automatic delivery pipeline that helps shorten the delivery cycle and improve efficiency. The pipeline feature in Workbench is based on Jenkins implementation. |
| Credential | To allow pipeline interaction with third-party applications, the user must configure Jenkins [credentials](../user-guide/pipeline/credential.md). |
| GitOps | The core idea of GitOps is that it uses a Git repository that contains a declarative description of infrastructure in the production environment, and automatic processes to ensure that the production environment is consistent with the desired state in the repository. If you want to deploy or update an application, just update the corresponding repository and leave other things to automatic processes. This is similar to using cruise control to manage applications in the production environment. |
| Canary Release | Canary Release allows you to progressively update applications, enabling the co-existence of multiple versions, release suspension, traffic percentage switching, among other features. It automates the process and eliminates manual operations in canary release. |
| Toolchain Integration | This means you can integrate your favorite DevOps tools as a toolchain, eliminating the need to log into multiple platforms and deal with different views of these tools. |
