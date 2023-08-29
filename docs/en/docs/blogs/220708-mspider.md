# 5.0 Introduction to Service Mesh Capability

The following figure shows a normal model of mesh-like services. How can such a complex mesh service be managed?

![whatmesh](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/mspider01.png)

DaoCloud Service Mesh is a fully-managed service mesh product with high performance and ease of use. By providing a complete non-invasive microservices governance solution, it can well support unified governance of complex environments with multiple clouds and clusters, and provide users with service traffic governance, security governance, service traffic monitoring, and support for traditional microservices (SpringCloud, Dubbo) access as an infrastructure service. It is also compatible with the community-native Istio open source service mesh and provides native management capabilities for Istio access. At a higher level, Service Mesh helps reduce the complexity of service governance and alleviate the pressure on development and operation teams.

As a member of DCE 5.0 product system, DaoCloud service mesh seamlessly interfaces with container management platform, providing users with plug-and-play experience. It also serves as the infrastructure to support container microservice governance for microservice engine, enabling users to manage various microservice systems through a single platform.

![mspiderlocation](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/mspider02.png)

## Traffic management

Traffic management is a very broad topic, for example:

- Dynamically modify the load balancing strategy for inter-service access, such as session persistence based on some request features.
- If two versions of the same service are online, redirect a portion of the traffic to a specific version.
- Protect services, for example, limit concurrent connections, requests, isolate faulty service instances, etc.
- Dynamically modify the contents of services or simulate service failures.

These service governance features can be implemented in a service mesh without modifying any application code. The service mesh can provide non-intrusive traffic management capabilities for managed services. According to the protocol of the service, provide policy-based and scenario-based network connection management. Select the designated port for the selected service on the application topology and configure various governance rules as needed.

### Scenario advantages

**Retry**

Automatically retry failed service access to improve overall access success rate and quality. Supports configuration of HTTP request retry times, retry timeout, and retry conditions.

**Timeout**

Automatically handle service access timeout and fail fast to avoid resource lockup and request stalls. Supports configuration of HTTP request timeout.

**Connection pool**

Through connection pool management, TCP's maximum number of connections, connection timeout, maximum number of unresponsive times, shortest idle time, and health check interval can be configured for layer 4 protocols. For layer 7 protocols, HTTP's maximum number of requests, maximum number of retries, maximum number of waiting requests, maximum number of requests per connection, and maximum idle time can be configured to prevent a failure of one service from affecting the entire application.

**Outlier detection**

By configuring the number of consecutive errors before the instance is evicted, the eviction interval, the minimum eviction time, the maximum eviction ratio, and other parameters for outlier detection, the working conditions of the accessed service instances are periodically examined. If an access exception occurs continuously, the service instance is marked as abnormal and isolated, and no traffic is allocated to it for a period of time. After that, the isolated service instance will be released from isolation and try to process requests. If it is still not normal, it will be isolated for a longer period of time. This achieves fault isolation and automatic fault recovery for abnormal service instances.

**Load balancing**

Configure various load balancing strategies, such as random, round-robin, least connection, and also configure consistent hashing to forward traffic to specific service instances.

**HTTP header fields**

Flexibly add, modify, and delete specified HTTP header fields, including operations on headers before forwarding HTTP requests to the target service, and operations on headers before responding to HTTP requests to clients, to manage request content in a non-intrusive manner.

**Fault injection**

Construct fault cases by injecting interruption failures and delayed failures into selected services without modifying any code, enabling fault testing.

## End-to-End Transparent Security

As we all know, splitting traditional monolithic applications into microservices brings various benefits, including better flexibility, scalability, and reusability. However, microservices also face special security requirements:

- To resist man-in-the-middle attacks, traffic encryption is required.
- To provide flexible service access control, TLS and fine-grained access policies are required.
- To determine who can do what at what time, auditing tools are required.

In the face of these needs, a service mesh provides a comprehensive security solution, including authentication policies, transparent TLS encryption, and authorization and auditing tools.

### Scenario advantages

**Non-intrusive security**

The service mesh provides transparent security capabilities to users in the form of secure infrastructure, enabling code that does not involve security issues to run securely, allowing people who are not familiar with security to develop and operate secure services, and providing service access security without modifying business code. The application service mesh provides a transparent distributed security layer and provides a bottom-level secure communication channel, managing authentication, authorization, and encryption for service communication, and providing communication security from Pod to Pod and service to service. Developers only need to focus on application-level security on this security infrastructure layer.

**Multicluster security**

In a multicluster scenario, the service mesh provides global service access security. Multiple clusters share a set of root certificates, distribute key pairs and certificates to data plane service instances, and regularly replace key certificates and revoke them as needed. When accessing services between services, the data plane proxy of the mesh will proxy local services and peers for mutual authentication and channel encryption. Here, the two-way authentication of the service can come from two different clusters, achieving transparent end-to-end two-way authentication across clusters.

**Fine-grained authorization**

Based on authentication, service access authorization management can be performed to control a specific service or a specific interface of the service. For example, only open to services in a specific namespace, or open to a particular service. The source service and the target service can be in different clusters, and even different instances of the source service can be in different clusters, and different instances of the target service can be in different clusters.

## Service Runtime Monitoring

Operating containerized infrastructure brings a series of new challenges. We need to enhance containers, evaluate the performance of API endpoints, and identify harmful parts in the infrastructure. The service mesh can implement API enhancement without modifying the code and does not introduce service latency.

The service mesh generates detailed telemetry for all service communication in the mesh, providing observability of service behavior, allowing operators to troubleshoot, maintain and optimize their applications without any extra burden on service developers. Through the service mesh, operators can fully understand how the monitored services interact with other services and components themselves.

### Scenario advantages

**Non-intrusive monitoring data collection** 

In complex cases, the access topology, call chain, and monitoring between services are necessary means for managing the overall operation of services and locating and delineating service access exceptions. An important capability of service mesh technology is to provide non-intrusive collection of these monitoring data in an application, allowing users to focus on their own business development without the need for additional attention to monitoring data generation.

**Rich performance monitoring capabilities** 

Based on the service access data generated by the mesh, various performance monitoring services are integrated to provide intelligent service operation management across clusters. This includes cross-cluster service call chains, service access topology, and service running health status. A global view across clusters is used to correlate the access status between services.

## Graphical User Interface

In the service mesh, the following graphical interactive features are implemented for users:

1. Provide the ability to create, manage, and configure mesh resources under the service mesh. Users can allocate cluster resources to reasonable meshes as needed to achieve aggregated management.
2. Enable users to access cluster resources or place cluster resources that have already deployed ISTIO governance components under the control of the service mesh platform.
3. Provide workspace binding of controlled resources under the mesh, sharing authority over mesh resources through workspaces, facilitating interaction between sub-products.
4. Provide unified viewing and operational features for namespaces and services in an aggregated management manner for users.
5. Provide traffic governance features for namespaces and services, and provide form and YAML two ways of creating and editing forms. Users can almost use all traffic governance features provided by native ISTIO (routing, splitting, outlier detection, etc.).
6. Provide security governance features for namespaces and services, and provide form and YAML two ways of creating and editing forms. Users can match traffic governance to achieve zero trust environment and access authorization within the mesh.
7. Provide flow topology and status chart viewing features for service communication in the mesh. The flow topology provides users with various information such as communication status, protocol usage, and performance parameters between nodes in the mesh. Users can quickly locate problems through search and filtering features. The status chart can provide users with system status information from multiple dimensions such as global, service, and workload.

[Learn about Service Mesh](../mspider/intro/index.md){ .md-button }

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial Now](../dce/license0.md){ .md-button .md-button--primary }
