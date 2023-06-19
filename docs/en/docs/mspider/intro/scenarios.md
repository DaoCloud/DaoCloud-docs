# Use Cases

This section introduces the specific cases where the service mesh is applicable.

## Service Traffic Governance

Traffic governance is a broad topic that includes dynamically modifying the load balancing strategy for inter-service access, maintaining sessions based on specific request characteristics, cutting part of the traffic to a certain version of the same service online, and protecting services by limiting the number of concurrent connections, requests, and isolating faulty service instances. Additionally, this includes the ability to modify service content and simulate service failures. 

The service mesh can provide non-intrusive traffic management capabilities, and these service governance features can be realized without modifying any business code. It provides strategic and scenario-based network connection management according to the service agreement, allowing different governance rules to be configured for specific ports of specific services as needed.

### Scenario Advantages

- Retry: Automatically retry service access failures, improving the overall access success rate and quality. Supports configuring the number of HTTP request retries, retry timeout, and retry conditions.

- Timeout: Automatically handle service access timeouts and fail quickly, avoiding resource locking and request jamming. Supports configuring HTTP request timeout.

- Connection Pool: Through connection pool management, configure the maximum number of TCP connections, connection timeout, maximum number of no responses, minimum idle time, and health check interval for the four-layer protocol. The maximum number of HTTP requests, maximum number of retries, maximum number of waiting requests, maximum number of requests per connection, and maximum idle time of a connection can be configured for the seven-layer protocol to prevent the cascading failure of a service from affecting the entire application.

- Fuse: Regularly inspect the working conditions of accessed service instances by fusing parameters such as the number of consecutive errors before the instance is evicted, eviction interval, minimum eviction time, and maximum eviction ratio. If continuous access exceptions occur, the service instance will be marked as abnormal and isolated, and no traffic will be assigned to it for a period. After some time, the isolated service instance will be unisolated again and try to process the request. If it is still not normal, it will be quarantined for an extended period. In this way, fault isolation and automatic fault recovery of abnormal service instances are realized.

- Load Balancing: Configure various load balancing strategies, such as random, round-robin, least connections, and consistent hashing, to forward traffic to specific service instances.

- HTTP Header: Flexibly add, modify, and delete specified HTTP headers, including manipulating headers before forwarding HTTP requests to target services. It is also possible to manipulate the header before replying to the HTTP response to the client to manage the request content in a non-intrusive manner.

- Fault Injection: Construct fault cases by injecting interruption faults and delay faults into selected services, and perform fault testing without modifying codes.

## End-to-End Transparent Security

Splitting traditional monolithic applications into microservices brings various benefits, but microservices also face special security requirements. These include defending against man-in-the-middle attacks, providing flexible service access control, and auditing tools to determine who can do what and when. The service mesh provides comprehensive security solutions, including authentication policies, transparent TLS encryption, and authorization and auditing tools.

### Scenario Advantages

- Non-Intrusive Security: The service mesh provides users with transparent security capabilities in the form of a security infrastructure, allowing codes that do not involve security issues to run safely. People who do not understand security can develop and operate secure services without modifying business code, providing service access security. The application service mesh provides a transparent distributed security layer, manages the authentication, authorization, and encryption of service communication, and provides Pod-to-Pod, service-to-service communication security. Developers only need to focus on application-level security on top of this security infrastructure layer.

- Multicluster Security: The service mesh provides global service access security in a multicluster scenario. Meshes of multiple clusters share a set of root certificates, distribute key and certificate pairs to service instances on the data plane, replace key certificates regularly, and revoke key certificates as needed. When accessing between services, the data plane agent of the mesh will act as a proxy for the local service and the peer to perform two-way authentication and channel encryption.

- Fine-Grained Authorization: On the basis of authentication, access authorization management between services can be performed, and a certain service or a specific interface of a service can be controlled for authorization management. For example, it is only open to services under a specific Namespace or a specific service. The source service and the target service can be in different clusters, even different instances of the source service are in different clusters, and different instances of the target service are in different clusters.

## Service Running Monitoring

Operating a containerized infrastructure presents a new set of challenges, including hardening containers, measuring the performance of API endpoints, and identifying harmful parts of our infrastructure. A service mesh enables API enhancements without code changes and without service latency. The service mesh can perform telemetry for all service communications within the mesh, providing observability of service behavior. This helps operators troubleshoot, maintain, and optimize their applications without giving service any additional burden imposed by the developer. With a service mesh, operators gain a comprehensive view of how monitored services interact with other services and the components themselves.

### Scenario Advantages

- Non-Intrusive Surveillance Data Collection: In complex cases, access topology, call chain, and monitoring between services are necessary for positioning and demarcating when service access is abnormal. An important capability of the service mesh technology is to provide the collection of these monitoring data non-intrusively. Users only need to pay attention to their own business development and do not need to pay extra attention to the generation of monitoring data.

- Rich Performance Monitoring Capabilities: Generate service access data based on the mesh, integrate various performance monitoring services, and provide cross-cluster intelligent service operation management. This includes cross-cluster service call chains, service access topology and service running health status, associating access status between services through a cross-cluster global view, etc.
