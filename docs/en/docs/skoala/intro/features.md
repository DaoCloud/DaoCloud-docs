---
MTPE: windsonsea
Date: 2025-12-30
hide:
  - toc
---

# Microservice Engine Features

The DCE 5.0 Microservice Engine provides the following features:

| Feature | Subfeature | Description |
| ------ | ---------- | ----------- |
| Microservice Registration and Discovery | Unified Management | Unified management of traditional microservices and cloud-native microservices, enabling a smooth transition from traditional microservice ecosystems to cloud-native microservice ecosystems and helping enterprises move toward cloud-native adoption. |
| | Nacos Managed Center | Supports creating a Nacos managed center to manage microservice namespaces, govern microservice traffic, manage microservice configurations, perform distributed tracing, and monitoring. |
| | Access Support | Supports integration with four traditional microservice registries: Eureka, Zookeeper, Nacos, and Consul. |
| | Cloud-Native Support | Supports integration with two cloud-native microservice registries: Kubernetes and Service Mesh. |
| Microservice Traffic Governance | Online Traffic Governance | At the traffic governance layer, an online traffic governance solution is adopted, enabling rapid integration with mainstream open-source microservice frameworks and addressing pain points in different production scenarios using Sentinel and Mesh. |
| | Sentinel Support | Supports using Sentinel to govern east–west traffic of traditional microservices through rules such as flow control, circuit breaking and degradation, hotspot protection, system protection, authorization, and cluster flow control. |
| | Service Mesh Capabilities | Supports leveraging service mesh capabilities to govern microservice traffic within the mesh using VirtualServices, DestinationRules, and Gateway rules. |
| | Istio Support | Supports using Istio to apply rules such as load balancing, circuit breaking, outlier detection, rewriting, fault injection, retries, timeouts, and global rate limiting for east–west traffic governance at the service port level. |
| | Wasm Plugins | Supports extending cloud-native microservice governance capabilities by creating and configuring Wasm plugins. |
| | Traffic Lane Mode | Supports traffic management using the traffic lane (canary lane) mode. |
| Microservice Configuration Center | Nacos Managed Registry | The Nacos managed registry can act as a configuration manager for microservices. It allows extracting common configurations from different projects for unified management, or applying multiple configurations to the same project to enable differentiated management. |
| | Configuration File Isolation | Isolates configuration files based on microservice namespaces and groups. |
| | Dynamic Updates | Dynamically updates configuration items using the `@RefreshScope` annotation. |
| | Historical Version Management | Manages historical versions of configuration files, supports version comparison, and enables one-click rollback to a specific version. |
| | Listener Query | Supports querying listeners of the current configuration and the MD5 checksum value. |
| | Canary Release | Supports targeted canary release of configuration files. |
| | Sample Code | Provides sample code to help beginners quickly use client-side programming to consume configurations, lowering the learning barrier. |
| Microservice Gateway | North–South Traffic Control | The microservice gateway plays a critical role in managing north–south traffic. It provides API management, API rate limiting, multiple security authentication strategies, blacklists and whitelists, routing and forwarding, Mock APIs, and more, while delivering enterprise-grade high performance and scalability as a cloud service. |
| | Multi-Gateway Management | Natively supports managing gateway instances across multiple clusters and namespaces in the [Container Management](../../kpanda/intro/index.md) module, including full lifecycle management of gateway instances. |
| | API Policy Management | Provides a graphical interface for creating, reading, updating, and deleting APIs, and configuring API policies such as load balancing, path rewriting, timeout settings, retry mechanisms, request/response header rewriting, WebSocket support, local rate limiting, health checks, and more, **while ensuring that native API capabilities remain unaffected**. |
| | Monitoring Capabilities | Automatically configures monitoring features during gateway deployment. Each gateway comes with comprehensive resource monitoring and gateway business monitoring. |
| Plugin Center | Feature-Rich Plugins | Provides a wide range of feature-rich plugins, including security hardening, traffic management, and data caching, to enhance user experience. Custom plugins are also supported to meet personalized requirements. |
| | Plugin Management | All plugins can be enabled or disabled with a simple one-click operation, ensuring convenient and efficient management. |
| | JWT Authentication | Supports JWT authentication, security authentication, global rate limiting plugins, and custom multi-gateway API authentication strategies, enabling quick one-click integration with gateway instances. |
| | Custom Wasm Plugins | Supports users in creating custom Wasm plugins. |
