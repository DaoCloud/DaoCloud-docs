---
MTPE: ModetaNiu
Date: 2024-06-12
---

# Introduction to OAM

The OAM application functionality is based on the open-source software
[KubeVela](http://kubevela.net/zh/docs/v1.2/), which uses the Open Application Model (OAM)
as the top-level abstraction for application delivery. It mainly abstracts and integrates Kubernetes resources.

An OAM application consists of four main concepts to achieve standardized and efficient
application delivery in a hybrid environment:

- One or more components
- Operational actions
- Application execution policies (Policy)
- Deployment workflows (Workflow)

You can refer to the following diagram from the KubeVela official documentation for a visual representation:

![oam1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/oam001.png)

## Introduction to Core Components

This section only introduces the core components covered by the Workbench.

### Components

Components define the form of delivery and management for artifacts or cloud services.
An application can include multiple components. The recommended practice is to include one
main component (core business logic) and additional components (middleware with strong dependencies
or exclusive use, operational components, etc.) in an application. For more information about component
types, please refer to the [kubevela Component Definition](http://kubevela.net/docs/v1.2/platform-engineers/oam/x-definition) documentation.

Currently, the Workbench includes five built-in components based on the open-source
[kubevela](https://kubevela.io/zh/docs/) components: __Cron-Task, Daemon, K8s-Objects, Task, Webservice__ .
For specific parameter introductions for each component, please refer to the
[Built-in Component List](https://kubevela.io/docs/end-user/components/references) documentation.

### Traits

Traits are modular and pluggable operational capabilities that can be bound to deployable components at any time. 
Examples include manual or automatic scaling of replicas, data persistence, setting gateway policies, 
and automatic DNS resolution. Users can obtain mature capabilities from the community or define their own traits.

Currently, the Workbench includes multiple built-in traits based on the open-source
[kubevela](https://kubevela.io/docs/) components, such as __Affinity, Annotations, Command, Container-Image, Cpuscaler__ .
For specific parameter introductions for each trait, refer to the
[Built-in Trait List](https://kubevela.io/docs/end-user/traits/references) documentation.

### Application Execution Policies (Policies)

The Workbench does not currently provide a productized capability for application execution
policies. For detailed information, refer to the [kubevela reference](http://kubevela.net/docs/v1.2/platform-engineers/oam/oam-model) documentation.

### Deployment Workflows

The Workbench does not currently provide a productized capability for defining deployment
workflows. KubeVela automatically deploys components and traits in the order specified
in the arrays. For detailed information, refer to the [kubevela reference](http://kubevela.net/docs/v1.2/platform-engineers/oam/oam-model) documentation.

## Customization

KubeVela allows easy customization and extension based on your needs.

#### Custom Components

Component Definitions allow platform administrators to package any type of deployable artifact as a deliverable "component". 
Once defined, components of this type can be referenced, instantiated,
and delivered in deployment plans (Applications) by users.

For specific operations on custom components, please refer to the official documentation:
[Getting Started with Custom Components](http://kubevela.net/docs/v1.2/platform-engineers/components/custom-component).

#### Custom Traits

Trait Definitions provide a set of operational actions that can be bound to components as needed.
These operational actions are usually provided by platform administrators as operational capabilities,
providing a range of operational operations and policies for a component, such as adding a
load balancing strategy, routing strategy, or performing elastic scaling, canary release strategies, and more.

For specific operations on custom traits, please refer to the official documentation:
[Customize traits](http://kubevela.net/docs/v1.2/platform-engineers/traits/customize-trait).
