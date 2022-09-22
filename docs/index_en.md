---
hide:
  - navigation
  - toc
---

# DaoCloud Enterprise 5.0

On the occasion of the golden Autumn of 2022, DaoCloud gladly launches the next-generation, cloud-native, containerized, comprehensive platform by fusing the most popular cloud-native technologies in the open source community. After two years of continuous development, testing, and verification by hundreds of diligent developers, the flower of idealism finally blooms in the land of romantic open-source community. The new platform leads the paces and waves of cloud-native development globally.

DaoCloud Enterprise 5.0 or DCE 5.0 for short, is a high-performance and scalable cloud-native operating system. It is developed with many independent modules. You can use each of them like LEGO bricks, with zero downtime while upgrading one of modules. DCE 5.0 is easy to integrate with hundreds of cloud-native plugins, so you can simply custom solutions for different scenarios. Things go better with such as modular construction.

DCE 5.0 has built a highly adaptable container manager, which can uniformly manage almost all kinds of containerized clusters on the market, with the feature of multi-cloud orchestration to use OpenShift, VMware, and public clouds at the same time. It can centrally control the apps from app stores and registry, natively integrates the CI/CD pipeline and application workbench, and endows the most cutting-edge service mesh and microservice technology. You can easily get insight from detailed and customized metrics of clusters, nodes, workloads, and services. With the support of various types of selected databases and middleware such as RabbitMQ, Elasticsearch, MySQL, Redis, etc., you can easily learn the current service status in time from the dynamically updated dashboard and topology map, through which you can deep dive into your business data to help you make valuable decisions in advance to boost your business.

## Features

DCE 5.0 is a cloud-native operating system with plenty of features for your choice.

![modules](en/images/dce-en.png)

=== "Container Manager"

Compatible with native Kubernetes and much more developed PaaS platform such as OpenShift, Tanzu, and more.
This container manager is aimed to facilitate your cloud-native applications. You can centrally manage multiple clouds and clusters with this container manager,
simplify your applications rolling out to any cloud, and significantly reduce your total cost of ownership. [Learn more](en/kpanda/03ProductBrief/WhatisKPanda.md)

=== "Global Manager"

Global manager is a user-oriented comprehensive service module, including role-based access control, workspaces, audit logs, and personal settings. [Learn more](en/ghippo/01ProductBrief/WhatisGhippo.md)

- User and access control: To securely manage access rights to resources, you can create, manage, delete users/groups, and flexibly configure user/group roles to complete the division of functional rights.

- Workspace and folder: A resource isolation unit with hierarchical structure and access control, you can set the hierarchical structure according to the enterprise development environment and department structure.

- Audit log: Provide you with logs of resource operation, through which you can quickly implement security analysis, resource changes, and troubleshooting.

- Platform settings: This feature enable you custom the security policies, mails, and peronal appearance.

=== "Observability"

The observability module is a new generation cloud native observability platform that focuses on applications analyzing.
It provides the out-of-the-box real-time resources monitoring, metrics, logs, events and other data to help you analyzing application status.
In additionally, it is compatible with popular open source components, and provides alerting, multi-dimensions data visualization, fault locating, one-click monitoring and diagnosing capabilities.
[Learn more](en/insight/03ProductBrief/WhatisKInsight.md)

=== "App Workbench"

The workbench focuses on the process of application automation delivery and infrastructure change, and provides full lifecycle management of business applications from "development - test - deployment - operation and maintenance", which can effectively help enterprises achieve digital transformation and improve their IT delivery capabilities and Competitiveness. [Learn more](en/amamba/01ProductBrief/WhatisAmamba.md)。

=== "Explore more"

| Modules                                       | Features                                                     |
| ----------------------------------------------- | ------------------------------------------------------------ |
| [Cluster lifecycle management](en/community/kubean.md)      | Features with fully automated and complete lifecycle (install, upgrade, and configure) Kubernetes cluster management. It supports for the dual-state architecture that separates the management cluster from the business cluster. |
| [Network](en/network/intro/what-is-net.md)         | Compatible with various underlying network environment (public cloud, private cloud, virtual machines, physical machines, and SDN), it has capabilities of combining different CNIs, network policies, and acceleration schemes. |
| [Storage](en/hwameistor/intro/what.md)             | Provides strong enterprise-level storage capabilities, comes with high-performance local storage, supports filesystem, block, and object storage, and can integrate with 99% of current storage vendors. |
| Registry                                        | Registry provides full lifecycle management for container images and Helm Charts, featurs with easy to use, safe, and reliable, can be seamlessly integrated with container platforms to help enterprises reduce delivery complexity and create a one-stop solution for cloud-native application rollout. |
| [Multi-cloud orchestration](en/kairship/01product/whatiskair.md) | This module provides the centralized management of multi-cloud and hybrid cloud, and provides capabilities of cross-cloud application deployment, delivery, and operation and maintenance. |
| [Middlewares](en/middleware/rabbitmq/intro/what.md)  | These are selected stateful middlewares that can run reliably in the production environment, including RabbitMQ high-performance message queue, Kafka daily message queue, MySQL relational database, Redis memory database, and Elasticsearch log retrieval. |
| [Microsevice engine](en/skoala/intro/features.md)       | The main functions of the microservice module are to access and host registries, manage microservice traffic, microservice gateway and API management. It is suitable for microservice registration and discovery, configuration management, traffic governance, gateway management, and other scenarios. |
| [Service mesh](en/mspider/01Intro/What'smSpider.md) | It provides non-intrusive traffic governance features to solve the service governance problems of users in the multi-cloud and multi-cluster container environment, and achieve the goals of unified governance and monitoring. It also provides the governance capability support of containerized microservices and traditional microservice access support for the integrated microservice management engine. |

Just like Lego bricks, it combines dozens of the best open source technologies into a platform. After many dialectical selection, adaptation and running-in, coding debugging, and massive testing, a sword is sharpened in ten years. The new generation of containerized platforms can meet the needs of various scenarios for enterprises migrating to the cloud.

![img](zh/images/ops-tech.png)

## Editions

![modules](zh/images/dce-modules01.png)

=== "Community Edition"

    With the cloud native base as the core and many more self-developed plugins, this edition provides cloud native computing, network, storage, and other capabilities, shields the complexity of the underlying infrastructure, reduces the threshold for enterprises to use cloud native applications, and improves application development efficiency.

    [Free Trial Now](en/dce/license0.md){ .md-button .md-button--primary }

=== "Standard Edition"

    This edition has a production-grade cloud-native base and supports for Xinchuang heterogeneity and cloud-edge collaboration.
    It is compatible with a variety of underlying infrastructures. With this edition, you can easily create and manage large-scale multi-clusters.
    CI/CD pipelines realizes automatic application delivery and deployment, innovative integration with GitOps, and progressive delivery.
    The app store selects ecological applications in ten categories and provides a complete software stack for enterprise users.

=== "Advanced Edition"

    In addition to those features provided by standard edition, this edition has developed with cutting-edge microservices and mesh technologies, supports for non-invasive access to traditional, cloud-native, and open source microservice frameworks, and uniformly realizes microservice lifecycle management, provides non-intrusive traffic governance features, to solve the service governance problem of users in the complex cloud-native environment of multi-cloud and multi-cluster.
    With the observability, this edition can trace through every traffic, automatically collects data, watches metrics of clusters, nodes, applications, and services in real time, and quickly locates faults.

=== "Platinum Edition"

    In addition to those features provided by advanced edition, this edition includes multi-cloud orchestration technology to realize centralized management of multi-cloud and hybrid clouds, provides cross-cloud application deployment, release, and O&M capabilities, supports for scalability based on cluster resources, and achieves global load balancing. If any disaster occurs, this edition can effectively implement the failover.
    This edition includes many selected middleware such as databases, distributed messages and log retrieva,l and provides middleware management capabilities for the full lifecycle of multi-tenancy, deployment, observability, backup, and O&M to keep your business with high availability.
