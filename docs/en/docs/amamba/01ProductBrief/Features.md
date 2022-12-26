---
hide:
  - toc
---

# Features

Application Workbench provides the following functions.

- Application management

    - Supports "polymorphic" cloud-native applications in cloud-native scenarios, including Kubernetes-native applications, Helm applications, and OAM applications.
    - Provides full lifecycle management of cloud-native applications, such as application scaling, logging, monitoring and viewing, and updating applications.
    - Supports access to microservice applications of SpingCloud, Dubbo, and ServiceMesh frameworks to achieve microservice governance. It is compatible with DCE 5.0's [Microservice Engine](../../skoala/intro/features.md), [Service Mesh ](../../mspider/01Intro/WhatismSpider.md) seamlessly integrated.

- Pipeline orchestration

    Pipeline is a custom CI/CD pattern.

    - Supports two modes of custom creation and pipeline creation based on the jenkinsfile of the codebase.
    - Support pipeline graphical editing.
    - The application can be built through source code and Jar package.

- Credential management

    Provide different types of credential management functions for codebases and container registrys in the pipeline.

- Continuous deployment

    Introduce the concept of GitOps to implement continuous application deployment, which is used to control the application release and deployment delivery process after code construction.

    - Based on Argo CD, deploy enterprise applications to the production environment frequently and continuously in an automated manner.
    - Provides Argo CD Application creation, synchronization, and deletion management.

- registry management

    Support importing Git code repository, after importing, you can use this repository for continuous deployment of applications in continuous deployment.

- Grayscale release

    Grayscale publishing can ensure the stability of the overall system, and problems can be found and adjusted at the initial grayscale to reduce the scope of the problem.

    - Supports canary release, blue-green deployment, and A/B Testing advanced release strategies.
    - Canary releases support automated incremental release processes.
    - Supports quick rollback of applications through monitoring indicator analysis.