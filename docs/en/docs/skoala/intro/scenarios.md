---
MTPE: windsonsea
Date: 2024-04-24
hide:
  - toc
---

# Applicable Scenarios

The DaoCloud Microservice Engine is a one-stop microservice management platform designed for mainstream industry microservice ecosystems. It mainly provides functionalities across two dimensions: the Microservice Governance Center and the Microservice Gateway. These include service registration and discovery, configuration management, traffic governance, service-level tracing, API management, domain management, monitoring and alerting, covering a wide range of microservice lifecycle management scenarios.

## Use Cases

Based on the [features provided](./features.md), the microservice engine can be used in scenarios such as service registration and discovery, configuration management, microservice traffic governance, and microservice gateway management. Typical use cases include:

- **One-stop management of large-scale heterogeneous microservices**

    With the explosive growth of application services, the number of microservices continues to increase, and their architectures may vary. Traditional microservices coexist with cloud-native microservices.  
    Interdependencies between microservices can lead to cascading effects, potentially causing system failures. As the operational complexity and cost of microservice systems grow, users need a **one-stop** solution that can manage both traditional and cloud-native microservices, monitor service information, trace service-level calls, unify configuration management, and provide a microservice gateway. The microservice engine fully addresses these needs.

- **Transition from traditional to cloud-native**

    Cloud-native architectures offer advantages in elasticity, abstraction of underlying differences, and fault handling. Some enterprises aim for a gradual transition from traditional microservices to cloud-native microservices in a stable manner, while others may pursue a faster, agile transition.  
    Regardless of approach, the microservice engine is an ideal choice, as it supports unified management of traditional and cloud-native microservices and provides traffic governance via both Sentinel and Service Mesh, suitable for east–west traffic management in traditional and cloud-native microservices respectively.

- **Visualized and high-performance microservice gateway**

    Many open-source gateway products only support command-line operations, which can be complex and difficult to use. In some cases, multiple microservices share a single gateway, increasing resource consumption and potentially becoming a system bottleneck.  
    DaoCloud Microservice Engine enhances Contour with a graphical interface, significantly reducing the learning curve and maintenance cost. It supports multi-gateway management, enabling the creation of multiple gateway instances across different clusters and namespaces. These instances are isolated, providing higher availability and stability. Additionally, gateway routing can support cascading functions to enable dynamic blue-green deployment for microservices.

## Product Advantages

The microservice engine consists of the Microservice Governance Center and Microservice Gateway modules, providing a set of simple, practical, and high-performance governance capabilities, including service registration and discovery, traffic governance, configuration management, and gateway API management. This helps enterprises smoothly upgrade from traditional microservice architectures to cloud-native microservice architectures.

Compared to similar products, the DaoCloud Microservice Engine offers the following advantages:

- **One-stop Governance**

    Provides service registration and discovery, configuration management, traffic governance, tracing, metrics monitoring, gateway management, API management, domain management, alerting, and gateway policies. It covers all stages of the microservice lifecycle, achieving one-stop governance.

- **Seamless Migration**

    Fully compatible with the Nacos open-source registry and Envoy/Contour open-source gateways, enabling migration to the DaoCloud Microservice Engine without any code changes. Traditional microservices can connect through the registry without modification to benefit from traffic governance, configuration management, tracing, and monitoring.

- **Smooth Transition**

    Unified management of traditional and cloud-native microservices, supporting both traditional registries (Zookeeper, Eureka, Nacos, Consul) and cloud-native registries (Kubernetes, Service Mesh). This enables a smooth transition from a traditional microservice ecosystem to a cloud-native one, assisting enterprises in adopting cloud-native architectures.

- **Open and Compatible**

    Supports both traditional and cloud-native registries and mainstream open-source microservice frameworks such as Spring Cloud and Dubbo, as well as open-source gateways like Envoy and Contour. It can also be combined with [DCE 5.0](../../dce/index.md) modules for multi-cloud orchestration, data middleware, service mesh, and application workbench, enabling highly customizable and fine-grained functionality.

- **Visual Interface and Data**

    Provides simple, user-friendly interactive pages, allowing all operations through an intuitive UI. This reduces operational complexity and enables management of the entire microservice lifecycle with just a few clicks.
