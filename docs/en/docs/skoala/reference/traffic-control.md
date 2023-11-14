# Traffic Governance

The traffic routing rules of a service mesh allow you to easily control the traffic between services and API calls. A service mesh simplifies the configuration of service-level attributes such as circuit breakers, timeouts, and retries, and enables easy setup of critical tasks. It also provides out-of-the-box fault recovery features that enhance application robustness, allowing better handling of failures in dependent services or network.

The traffic management model of a service mesh is based on the Envoy proxy deployed alongside services. All traffic (data plane traffic) sent and received by services within the mesh goes through the Envoy proxy, making traffic control within the mesh exceptionally simple without requiring any changes to the services.

To route traffic within the mesh, the service mesh needs to know where all the endpoints are and which services they belong to. To locate the service registry, the service mesh connects to a service discovery system. For example, if you install a service mesh on a Kubernetes cluster, it automatically detects the services and endpoints within that cluster.

Using this service registry, the Envoy proxy can direct traffic to the relevant services. In most microservice-based applications, each service workload has multiple instances to handle traffic, known as a load balancing pool. By default, the Envoy proxy distributes traffic within the load balancing pool based on a round-robin scheduling model, sending requests to each member of the pool in sequence until all service instances have received a request, and then starting again from the first pool member.

The basic service discovery and load balancing capabilities of a service mesh provide you with a functional service mesh, but it can do much more. In many cases, you may want more granular control over the traffic within the mesh. As part of A/B testing, you may want to route a specific percentage of traffic to a new version of a service or apply different load balancing strategies to a subset of service instances. You may also want to apply special rules to the incoming and outgoing traffic within the mesh or add external dependencies to the service registry. By using the traffic management API of the service mesh, you can add traffic configuration to the service mesh, and even extend its capabilities further.

Like other service mesh configurations, these APIs are declared using Kubernetes custom resource definitions (CRDs), and you can configure them using YAML.

## Traffic Governance Policies

- Rate Limiting

    Rate limiting refers to the practice of limiting the rate of incoming traffic, allowing only a specified amount of traffic into the system. Traffic exceeding the threshold is either rejected, queued, or subjected to degradation. Rate limiting ensures the stability of machines and the overall business, preventing system overload and cascading failures.

- Degradation

    When server pressure increases significantly, degradation involves selectively not processing or simplifying the handling of non-core, non-critical services based on actual business conditions and traffic. This releases some server resources to ensure the normal or efficient operation of core services. Degradation can be implemented when the overall load of the entire microservices architecture exceeds the preset limit or when the anticipated incoming traffic is expected to exceed the set threshold.

- Circuit Breaking

    The concept of circuit breaking originates from circuit breakers in electrical engineering. In internet systems, when downstream services become slow or fail due to excessive access pressure, surpassing a set threshold, upstream services temporarily cut off calls to the downstream services to protect the overall system's availability. This measure sacrifices a part to preserve the whole and is known as circuit breaking.
