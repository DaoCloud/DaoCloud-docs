---
hide:
  - toc
---

# Function overview

The application workbench provides the following functions.

- Application management

    - Supports "multi-form" cloud native applications in cloud native scenarios, including Kubernetes native applications, Helm applications, OAM applications, etc.
    - You can manage the full life cycle of cloud native applications, such as application expansion and shrinkage, logging, monitoring, and updating.
    - Supports access to SpingCloud, Dubbo, and ServiceMesh frameworks for micro service governance and seamless integration with [Microservice Engine](../../skoala/intro/what.md) and [Service Mesh](../../mspider/intro/what.md) of DCE 5.0.

- pipelining

    Pipelining is a custom CI/CD schema.

    - Support for custom creation, code repository based jenkinsfile creation pipeline two modes.
    - Support pipelined graphical editing.
    - Applications can be built by means of source code, Jar packages.

- Certificate management

    Provides different types of credential management functions for the code base and image warehouse in the pipeline.

- Continuous deployment

    The concept of GitOps is introduced to realize continuous application deployment, which is used to control the application release and deployment delivery process after the code is built.

    - Argo CD enables frequent and continuous deployment of enterprise applications to production environments in an automated manner.
    - Provide Argo CD Application to create, synchronize, delete management.

- Warehouse management

    Support for importing Git repositories that you can use in continuous deployment for continuous deployment of your applications.

- Grayscale release

    Gray release can ensure the stability of the whole system, and problems can be found and adjusted at the initial gray level to reduce the influence range of problems.

    - Support Canary release, blue-green deployment, A/B Testing advanced release strategy.
    - Canary Publishing supports an automated and progressive publishing process.
    - Supports rapid application rollback based on monitoring indicator analysis.
