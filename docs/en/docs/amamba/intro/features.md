---
hide:
  - toc
---

# Feature Overview

Application Workbench provides the following features:

- Application Management

    - Supports "multi-form" cloud-native applications, including Kubernetes native applications, Helm applications, OAM applications, and so on.
    - Provides full lifecycle management for cloud-native applications, such as scaling, logs, monitoring, and application updates.
    - Supports integrating and managing SpringCloud and Dubbo microservices, as well as cloud-native microservices based on Kubernetes and Service Mesh.

- Pipeline Orchestration

    Pipeline is a customizable CI/CD mode.

    - Supports four modes to create pipelines: custom creation, Jenkinsfile-based creation, tempalte-based creation, and create multiple-branch pipelines.
    - Supports editing pipelines with graphical UI.
    - Supports building applications from source code in GitHub repos, Jar packages, Helm charts, or container images.

- Credential Management

    Manages different types of credentials for code repositories and image registries used in a pipeline.

- GitOps

    Introduces the concept of GitOps to achieve continuous deployment of applications, which helps control the application release and deployment process after code building.

    - Based on Argo CD, automates the deployment of applications to production environments frequently and continuously.
    - Provides creation, synchronization, and deletion of Argo CD applications.

- Repository Management

    Supports importing code repositories from Git, allowing you to use them for continuous deployment of applications.

- Canary Release

    Canary release ensures system stability by allowing you to discover and fix bugs during the initial grayscale phase, reducing the impact range of bugs and vulnerabilities.

    - Supports advanced release policies such as Canary release, Blue/Green deployment, and A/B Testing.
    - Canary release supports automated progressive release.
    - Supports quick rollback based on metric analysis.

- Toolchain Integration

    This means you can integrate your favorite DevOps tools as a toolchain, no need to log into multiple platforms and dealing with different views of these tools.
