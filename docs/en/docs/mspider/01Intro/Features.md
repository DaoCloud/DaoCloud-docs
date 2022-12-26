# Function overview

The features supported by the service mesh are described here.

### Traffic management

- Layer 7 connection pool management

    Supports configuring the maximum number of HTTP requests, the maximum number of retries, the maximum number of waiting requests, the maximum number of requests per connection, and the maximum idle time of a connection.

- Four-layer connection pool management

    Supports configuring the maximum number of TCP connections, connection timeout, maximum number of no responses, minimum idle time, and health check interval.

- fuse

    Supports configuration of service circuit breaking rules, including the number of consecutive errors before an instance is evicted, the inspection cycle, the basic isolation time, and the maximum proportion of isolated instances.

- Retry

    Supports configuring the number of HTTP retries, retry timeout, and retry conditions.

- time out

    Supports configuring HTTP request timeout.

- load balancing

    Supports configuration of random scheduling, round-robin scheduling, least connection and consistent hash load balancing algorithms.

-HTTP Header

    You can flexibly add, modify, and delete specified HTTP Headers, including operations on Headers before forwarding HTTP requests to target services, and operations on Headers before replying HTTP responses to clients.

- fault injection

    Supports configuration of delayed faults and interrupt faults.

### Safety

- Transparent two-way authentication

    Support mutual authentication between interface configuration services.

- Fine-grained access authorization

    Support for configuring access authorization between services through the interface (the background API can configure Namespace level authorization, and the authorization will be given to a specific interface).

### Observability

- traffic topology

    Support viewing the mesh application traffic topology to understand the dependencies between services.

- Service operation monitoring

    Support viewing service access information, including indicators such as QPS and latency of services and service versions.

- access log

    Supports collecting and retrieving access logs for services.

- call chain

    Supports non-intrusive call chain burying, and can delimit and locate problems by retrieving call chain data.

### Multi-cluster mode

- Unified management of multi-cluster configuration

    Supports mesh configuration and cluster configuration management of multiple clusters under the mesh; supports sidecar injection policies of different clusters with different granularities, and supports unified management of data plane configurations such as cross-cluster traffic policies.

- Scalability
    
    Supports one-click access and removal of clusters

### mesh Data Plane Microservice Framework

-Spring Cloud

    Services developed with the Spring Cloud SDK are supported to access the mesh without intrusion and are managed in a unified manner.

- Dubbo

    Services developed by the Dubbo SDK are supported for non-intrusive access to the mesh and unified management.

### Compatibility and extensions

- version compatible

    The API is fully compatible with common service meshes.

- Plugin support

    Support Tracing, Prometheus, Kiali, Grafana.