---
hide:
  - toc
---

# Applicable scene

The "DaoCloud" microservice engine is a one-stop microservice management platform for the mainstream microservice ecosystem in the industry. It mainly provides two-dimensional functions of microservice governance center and microservice gateway, including service registration discovery, configuration management, and traffic management. , service-level link tracking, API management, domain name management, monitoring alarms, etc., covering various management scenarios in the microservice lifecycle.

Based on the [features](features.md) provided, the microservice engine can be used in scenarios such as microservice registration and discovery, configuration management, microservice traffic management, and microservice gateway management. Typical application scenarios are as follows:

## One-stop management of a large number of heterogeneous microservices

With the explosive growth of application services, the number of microservices is increasing, and the architectures used may also be different. Traditional microservices and cloud-native microservices coexist. The various microservices call each other and depend on each other, and the whole body is affected by a single incident, which is prone to cascading effects and causes an avalanche of the system. With the increasing difficulty and cost of operation and maintenance of microservice systems, users need a system that can manage traditional microservices and cloud-native microservices, monitor service information, track service-level link calls, and manage microservice configurations in a unified manner. Provides a **one-stop** product for microservice gateways. The microservice engine completely covers the requirements of these scenarios and can well meet the needs of users.

## Transformation and transition from traditional to cloud native

Cloud-native has significant advantages in terms of elastic expansion, shielding underlying differences, and fault handling. Under the influence of cloud-native waves, some enterprises hope to adopt a steady-state model and gradually shift from traditional microservice architectures to cloud-native microservice architectures. Some enterprises hope to Adopt agile mode for rapid transformation. Regardless of the steady-state or sensitive-state mode, the microservice engine is a good choice, because it supports the unified management of traditional microservices and cloud-native microservices, and supports two traffic management modes, Sentinel and Service Mesh, which are respectively applicable to traditional East-west traffic management for microservices and cloud-native microservices.

## Visualization and high performance of microservice gateway

Many open source gateway products only support command-line operations, which are difficult and difficult to use. In some cases, multiple microservices share a gateway, and the resource overhead of the gateway is high, and may gradually become the resource bottleneck of the entire system. Using the "DaoCloud Daoke" microservice engine to increase interface operation capabilities on the basis of Contour, greatly reducing the threshold for use and maintenance costs, enabling multi-gateway management, and easily creating multiple gateway instances in different clusters and different namespaces. These gateway instances are isolated from each other for higher availability and stability. In addition, the cascading function of gateway routing can also be used to realize the dynamic switching of blue-green deployment of microservices.