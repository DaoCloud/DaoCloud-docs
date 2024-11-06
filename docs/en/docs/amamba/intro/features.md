---
hide:
  - toc
---

# Workbench Features

The Workbench is a module included in DCE 5.0 Enterprise Package, providing the following features.

| Features | Descriptio |
|----------|------------|
| **Application Management**  | - Supports "polyform" cloud native applications in various cloud native scenarios, including Kubernetes native applications, Helm apps, and OAM applications.<br>- Provides comprehensive lifecycle management for cloud native applications, including scaling, logging, monitoring, and application updates.<br>- Enables seamless integration with microservice applications based on Spring Cloud, Dubbo, and Service Mesh frameworks to achieve effective microservice governance. It seamlessly integrates with DCE 5.0's [Microservice Engine](../../skoala/intro/index.md) and [Service Mesh](../../mspider/intro/index.md). |
| **Pipeline Orchestration**  | - Pipeline is a customizable CI/CD mode.<br>- Supports four modes to create pipelines: custom creation, Jenkinsfile-based creation, template-based creation, and create multiple-branch pipelines.<br>- Supports editing pipelines with graphical UI.<br>- Supports building applications from source code in GitHub repos, Jar packages, Helm charts, or container images. |
| **Credential Management**   | Manages different types of credentials for code repositories and image registries used in a pipeline.                        |
| **GitOps**                  | - Introduces the concept of GitOps to achieve continuous deployment of applications, which helps control the application release and deployment process after code building.<br>- Based on Argo CD, automates the deployment of applications to production environments frequently and continuously.<br>- Provides creation, synchronization, and deletion of Argo CD applications. |
| **Repository Management**    | Supports importing code repositories from Git, allowing you to use them for continuous deployment of applications.            |
| **Canary Release**          | - Canary release ensures system stability by allowing you to discover and fix bugs during the initial grayscale phase, reducing the impact range of bugs and vulnerabilities.<br>- Supports advanced release policies such as Canary release, Blue/Green deployment, and A/B Testing.<br>- Canary release supports automated progressive release.<br>- Supports quick rollback based on metric analysis. |
| **Toolchain Integration**    | This means you can integrate your favorite DevOps tools as a toolchain, eliminating the need to log into multiple platforms and deal with different views of these tools. |
