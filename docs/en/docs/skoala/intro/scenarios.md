---
MTPE: windsonsea
Date: 2024-04-24
hide:
  - toc
---

# Use Cases

DaoCloud Microservice Engine (DME) is a one-stop management platform for common microservice frameworks. It mainly consists of two parts: service governance and cloud native gateway, providing service registration and discovery, configuration management, east-west traffic governance, service monitoring, south-north traffic management, API management, domain name management, etc, covering most user cases throughout the lifecycle of microservice management.

Based on the [features list](./features.md), DME can be used for registration and discovery of microservice, configuration management, traffic governance, and gateway management. Here are some typical use cases:

## One-stop management of heterogeneous microservices

Microservices in the same system may use different architectures. Some use traditional SpringCloud or Dubbo framework, and some may take a more cloud native way with Kubernetes or Service Mesh. As the number of microservices grows quickly, the whole system is susceptible to avalanche caused by cascade effect resulted from complicated invocation relationship between microservices. This will add difficulty and cost of operation and maintenance of microservice system. Therefore, a **one-stop platform** that can manage both traditional and cloud native microservices is in highly demand. This is why DME came into being. It can monitor service information, trace invocations, manage microservice configuration, and govern north-south traffic for the two kind of microservices.

## Transition from traditional to cloud native microservices

Cloud native has significant advantages in scalability, isolation of bottom differences, troubleshooting and other aspects. Under the influence of the cloud native hit, some enterprises may want to steadily and gradually shift from the traditional microservice architecture to the cloud native architecture, and some enterprises may hope to finish the transition with one step. DME can meet both requirements, because it supports unified management of traditional and cloud native microservices, and supports traffic governance by Sentinel and Service Mesh.

## Efficient visualized microservice gateway

Many open-source gateway projects only support command line operation, which is not user-friendly. In some cases, several microservices share the same gateway, which costs a lot of resources and may gradually become the resource bottleneck of the whole system. Based on Contour, DME offers an GUI interface to operate gateways and further enriches some key features, such as API management, domain name, service integrate, etc. It allows multi-gateway management and easy creation of multiple gateway instances in different clusters and namespaces. These gateway instances are isolated from each other, securing higher availability and stability. In addition, the cascade feature of gateway routes can also be used to realize blue and green deployment of microservices.
