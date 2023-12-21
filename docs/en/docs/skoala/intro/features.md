# Feature Overview

DCE 5.0 Microservice Engine has the following feature capabilities:

## Microservice Registration and Discovery

Unified management of traditional microservices and cloud-native microservices, enabling a smooth transition from traditional microservice ecosystems to cloud-native environments.

- Supports creating a Nacos management center to manage microservice namespaces, traffic governance, configuration management, service tracing, and monitoring.
- Supports integration with four types of traditional microservice registration centers: Eureka, ZooKeeper, Nacos, and Consul.
- Supports integration with two types of cloud-native microservice registration centers: Kubernetes and Service Mesh.

## Microservice Traffic Governance

In terms of traffic governance, online traffic governance solutions are used to quickly integrate with mainstream open-source microservice frameworks. Sentinel and Mesh are used to address pain points in different production scenarios.

- Supports using Sentinel to govern traditional microservices' east-west traffic with flow control, circuit breaking, degradation, hotspots, system protection, authorization, and cluster flow control rules.
- Supports using Service Mesh to govern microservice traffic within the mesh with virtual services, destination rules, and gateway rules.

## Microservice Configuration Center

The Nacos-managed registration center can serve as a configuration manager for microservices. It can extract common configurations from different projects and centrally manage them, or apply different configurations to the same project for differentiated management.

- Isolates configuration files based on microservice namespaces and groups.
- Supports dynamic configuration updates with the `@RefreshScope` annotation.
- Manages historical versions of configuration files, supports version diff comparison, and provides one-click rollback to specific versions.
- Supports querying the current configuration's listeners and MD5 checksum.
- Provides sample code for easy consumption of the configuration by novice users, reducing the learning curve.

## Microservice Gateway

The microservice gateway plays a vital role in managing and controlling the north-south traffic of microservices. It provides capabilities such as API management, interface rate limiting, various security authentication strategies, blacklisting/whitelisting, routing, MockAPI, etc. It also provides enterprise-level high-performance and highly scalable cloud service capabilities.

- Multi-gateway management: Native support for managing multiple cluster and namespace gateway instances in the [Container Management](../../kpanda/intro/index.md) module, supporting full lifecycle management of gateway instances.
- API policy management: Graphical interface for API CRUD operations and configuration of API policies, such as load balancing, path rewriting, timeout configuration, retry mechanism, request/response header rewriting, WebSocket, local rate limiting, health checks, etc., while ensuring that the capabilities of native APIs are not affected.
- Plugin management: Provides a rich set of plugin functions, supporting security, traffic control, caching, and other plugins, with one-click enable/disable capability.
- Monitoring and alerting: The microservice gateway is automatically configured with monitoring, alerting, and other functions during deployment. Each gateway comes with comprehensive resource monitoring and gateway business monitoring capabilities.
