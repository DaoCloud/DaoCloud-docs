# What is Workbench?

Workbench (or Workbench for short) is a container-based DevOps platform for cloud-native applications. Workbench serves as a unified entry point for creating applications in DCE 5.0, providing flexible and easy-to-use pipelines, GitOps, progressive delivery, project management, integration of tools about product lifecycle and agile development.

Workbench focuses on the process of automation application delivery and infrastructure change, providing full lifecycle management for applications from "development -> testing -> deployment -> operation". This can promote digital transformation and improve IT delivery competence and competitiveness.

## Features

Workbench features application management, pipeline orchestration, credential management, GitOps, repository management, canary release, and toolchain integration. For more details, see [Feature Overview](features.md)

## Role in DCE 5.0

DaoCloud Enterprise 5.0 is a high-performance, scalable cloud-native operating system. It can provide a consistent and stable experience in any infrastructure and environment, supporting heterogeneous clouds, edge clouds, and Multicloud Management. DCE 5.0 integrates the latest service mesh and microservice technologies, which can track the entire lifecycle of each traffic, help you understand the detailed metrics of clusters, nodes, applications, and services, and visualize the health status of applications through dynamic dashboards and topology maps.

Based on the Cloud Native Foundation of DCE 5.0 for container, permission, and resource management, Workbench can create applications, pipelines, GitOps processes, canary release jobs, and toolchains, functioning as a underlying infrastructure of higher-level modules, such as Microservice Engine, Servie Mesh, Multicloud Management, etc.

![Workbench Role in DCE 5.0](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/what01.png)

## Separate Install

It is recommended to install Workbench through the installation package of [DCE 5.0 Enterprise Package](../../install/commercial/start-install.md), because you can install all modules of DCE 5.0 once a time with that package, no need to worry about incompatibility.

However, if you want to install or upgrade Workbench separately, run the following commands:

```bash
export VERSION=**** # Modify to the actual version deployed.
helm repo add mspider-release https://release.daocloud.io/chartrepo/amamba
helm repo update amamba
helm upgrade --install --create-namespace --cleanup-on-fail amamba amamba-release/amamba -n amamba-system --version=${VERSION}
```

[Download DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
