# Feature Overview

Microservices architecture has been universally applied in practice. Microservice Governance is a one-stop management platform
for common microservice frameworks. It mainly consists of two parts: service governance and cloud native gateway,
providing service registration and discovery, configuration management, east-west traffic governance, service monitoring,
south-north traffic management, API management, domain name management, etc. Microservice Governance covers most
use cases throughout the lifecycle of microservice management.

Microservice Governance boasts strong compatibility, working well with other components of DCE and
different open-source ecosystems like Spring Cloud and Dubbo. With Microservice Governance,
microservices can be built system more quickly and efficiently.

Microservice Governance provides the capabilities to create Nacos registries for managing microservice namespaces,
governing east-west traffic, setting configuration files, and monitoring invocation traces. It also integrates
four traditional microservice registries: Eureka, Zookeeper, Nacos, and Consul. Additionally, Microservice Governance
integrates with two cloud native microservice registries, Kubernetes and Service Mesh.

Microservice Governance leverages Sentinel and Service Mesh to address the distinct requirements governing
service-to-service traffic for both traditional and cloud native microservices. It uses Sentinel to enforce
flow control, circuit breaking, degradation, hotspot protection, system protection, authorization, and
cluster flow control rules, effectively managing the east-west traffic of traditional microservices.
Furthermore, Microservice Governance leverages Service Mesh to configure virtual services, destination rules,
and gateway rules, enabling fine-grained control over traffic between services within a mesh environment.

## Microservice Registration & Discovery

Microservice Governance can manage both traditional microservices and cloud native microservices.
It facilitates the process of "Go to Cloud" by making it easier to change traditional microservices to cloud native ones.

With Microservice Governance, you can:

- Create Nacos registries to manage microservice namespaces, govern east-west traffic, set configuration files, and monitor invocation traces.
- Integrate four traditional microservice registries: Eureka, Zookeeper, Nacos, and Consul.
- Integrate two cloud native microservice registries: Kubernetes and Service Mesh.

## Traffic Governance

Microservice Governance uses Sentinel and service mesh to meet the different demands of governing service-to-service traffic of traditional and cloud native microservices.

- Use Sentinel to set flow control, circuit breaker, degradation, hotspot, system, authorization, cluster flow control and other rules to govern the east-west traffic of traditional micro services.
- Use Service Mesh to set virtual services, target rules and gateway rules to control traffic between services in a mesh.

## Microservice Configuration Center

Nacos registry can be used as a configuration manager, which extracts common configurations from different projects for unified management, and applies different configurations for the same project.

- Isolate configuration files based on microservice namespaces and Groups.
- Dynamically update configuration items with `@RefreshScope` annotations.
- Manage historical versions of configuration files, compare version differences, and roll back to a specific version.
- Query the listener and MD5 checksum of configurations.
- Provide sample code to help novices understand and use this function.

## Microservice Gateway

The microservice gateway takes the role of managing the north-south traffic of microservices, providing API management, rate limit, security authentication, black/white list, routing and forwarding, MockAPI and other capabilities.

- Multi-gateway: manage gateway instances in clusters or namespaces through their life-cycles.
- API policy: add, delete, modify, and check APIs on UI interfaces, and configure API policies, such as load balancing,
  path rewriting, timeout, retry, request/response header rewriting, WebSocket, local rate limit, health check,
  cookie rewrite, black/white list, etc. **At the same time, the capabilities of your original APIs will not be damaged.**

- Plugins: provides various plugins about security, traffic control, and caches.
- Alerts: provide monitoring and alerting for each gateway by default.
