# Applicable scenarios

The specific scenarios where the service mesh is applicable are introduced here.

## Service Traffic Governance

Traffic governance is a very broad topic such as:

- Dynamically modify the load balancing strategy for inter-service access, such as maintaining sessions based on certain request characteristics.

- There are two versions of the same service online, and part of the traffic is cut to a certain version.

- Protect services, such as limiting the number of concurrent connections, limiting the number of requests, isolating faulty service instances, etc.

- Dynamically modify the content in the service, or simulate service failures, etc.

The service mesh can provide non-intrusive traffic management capabilities, and these service governance functions can be realized without modifying any business code. Provide strategic and scenario-based network connection management according to the service agreement. Different governance rules can be configured for specific ports of specific services as needed.

### Scenario Advantages

- Retry

     Service access failure is automatically retried, thereby improving the overall access success rate and quality. Supports configuring the number of HTTP request retries, retry timeout and retry conditions.

- time out

     Service access timeout is automatically handled and fails quickly, thereby avoiding resource locking and request jamming. Supports configuring HTTP request timeout.

- connection pool

     Through connection pool management, the maximum number of TCP connections, connection timeout, maximum number of no responses, minimum idle time and health check interval can be configured for the four-layer protocol;
     The maximum number of HTTP requests, the maximum number of retries, the maximum number of waiting requests, the maximum number of requests per connection, and the maximum idle time of a connection can be configured for the seven-layer protocol, so as to prevent the cascading failure of a service from affecting the entire application.

- fuse

     By fusing parameters such as the number of consecutive errors before the instance is evicted, the eviction interval, the minimum eviction time, and the maximum eviction ratio, etc., the working conditions of the accessed service instances are regularly inspected.
     If access exceptions occur continuously, the service instance will be marked as abnormal and isolated, and no traffic will be assigned to it for a period of time.
     After a period of time, the isolated service instance will be unisolated again and try to process the request. If it is not normal, it will be quarantined for a longer period of time. In this way, fault isolation and automatic fault recovery of abnormal service instances are realized.

- load balancing

     Configure various load balancing strategies, such as random, round robin, least connections, and you can also configure consistent hashing to forward traffic to specific service instances.

-HTTP Header

     Flexibly add, modify, and delete specified HTTP Headers, including manipulating headers before forwarding HTTP requests to target services.
     It is also possible to manipulate the Header before replying the HTTP response to the client to manage the request content in a non-intrusive manner.

- fault injection

     Construct fault scenarios by injecting interruption faults and delay faults into selected services, and perform fault testing without modifying codes.

## End-to-end transparent security

As we all know, splitting traditional monolithic applications into microservices brings various benefits, such as better flexibility, scalability, and reusability, but microservices also face special security requirements. :

- To defend against man-in-the-middle attacks, traffic encryption is required.

- In order to provide flexible service access control, TLS and fine-grained access policies are required.

- Auditing tools are needed to determine who can do what and when.

Facing these demands, Service Mesh provides comprehensive security solutions, including authentication policies, transparent TLS encryption, and authorization and auditing tools.

### Scenario Advantages

- Non-intrusive security

     The service mesh provides users with transparent security capabilities in the form of a security infrastructure, allowing codes that do not involve security issues to run safely, so that people who do not understand security can develop and operate secure services without modifying business code It can provide service access security. The application service mesh provides a transparent distributed security layer, provides an underlying secure communication channel, manages the authentication, authorization, and encryption of service communication, and provides Pod-to-Pod, service-to-service communication security. Developers only need to focus on application-level security on top of this security infrastructure layer.

- Multi-cluster security

     In a multi-cluster scenario, the service mesh provides global service access security. Grids of multiple clusters share a set of root certificates, distribute key and certificate pairs to service instances on the data plane, replace key certificates regularly, and revoke key certificates as needed. When accessing between services, the data plane agent of the grid will act as a proxy for the local service and the peer to perform two-way authentication and channel encryption. The two-way authentication service parties here can come from two different clusters, so as to achieve transparent end-to-end two-way authentication across clusters.

- Fine-grained authorization

     On the basis of authentication, access authorization management between services can be performed, and a certain service or a specific interface of a service can be controlled for authorization management. For example, it is only open to services under a specific Namespace, or it is open to a specific service. The source service and the target service can be in different clusters, even different instances of the source service are in different clusters, and different instances of the target service are in different clusters.

## Service running monitoring

Operating a containerized infrastructure presents a new set of challenges. We need to harden containers, measure the performance of API endpoints, and identify harmful parts of our infrastructure. A service mesh enables API enhancements without code changes and without service latency.

A service mesh can perform telemetry for all service communications within the mesh. This telemetry technology provides observability of service behavior and helps operators troubleshoot, maintain, and optimize their applications without giving service Any additional burden imposed by the developer. With a service mesh, operators gain a comprehensive view of how monitored services interact with other services, as well as the components themselves.

### Scenario Advantages

- Non-intrusive surveillance data collection

     In complex application scenarios, the access topology, call chain, and monitoring between services are all necessary means for positioning and demarcating when service access is abnormal.
     An important capability of the service mesh technology is to provide the collection of these monitoring data in a non-intrusive manner. Users only need to pay attention to their own business development and do not need to pay extra attention to the generation of monitoring data.

- Rich performance monitoring capabilities

     Generate service access data based on the grid, integrate various performance monitoring services, and provide cross-cluster intelligent service operation management.
     Including cross-cluster service call chains, service access topology and service running health status, associating access status between services through a cross-cluster global view, etc.