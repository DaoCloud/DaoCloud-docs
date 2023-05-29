# Features

This section describes the features supported by the service mesh.

## Traffic Management

- Seven-Layer connection pool management

    Configurable settings include the maximum number of HTTP requests, retries, waiting requests, requests per connection, and idle connection time.

- Four-layer connection pool management

    Configurable settings include the maximum number of TCP connections, connection timeout, maximum number of no responses, minimum idle time, and health check interval.

- Outlier detection

    Supports configuration of service circuit breaking rules, including the number of consecutive errors before an instance is evicted, inspection cycle, basic isolation time, and maximum proportion of isolated instances.

- Retry

    Configurable settings include the number of HTTP retries, retry timeout, and retry conditions.

- Timeouts

    Supports configuring HTTP request timeouts.

- Load balancing

    Supports configuration of random scheduling, round-robin scheduling, least connection, and consistent hash load balancing algorithms.

- HTTP Headers

    Flexible addition, modification, and deletion of specified HTTP headers, including operations on headers before forwarding HTTP requests to target services, and operations on headers before replying to HTTP responses from clients.

- Fault injection

    Supports configuration of delayed and interrupt faults.

## Safety

- Transparent two-way authentication

    Supports mutual authentication between interface configuration services.

- Fine-grained access authorization

    Supports configuration of access authorization between services through the interface (the background API can configure Namespace level authorization, and authorization can be given to a specific interface).

## Observability

- Traffic topology

    Supports viewing the mesh application traffic topology to understand dependencies between services.

- Service operation monitoring

    Supports viewing service access information, including QPS and latency metrics of services and service versions.

- Access log

    Supports collecting and retrieving access logs for services.

- Call chain

    Supports non-intrusive call chain tracing and can pinpoint and locate problems by retrieving call chain data.

## Multi-cluster Mode

- Unified management of multi-cluster configuration

    Supports mesh configuration and cluster configuration management of multiple clusters under the mesh. Supports sidecar injection policies of different clusters with different granularities and supports unified management of data plane configurations such as cross-cluster traffic policies.

- Scalability

    Supports one-click access and removal of clusters.

## Mesh Data Plane Microservice Framework

- Spring Cloud

    Services developed with the Spring Cloud SDK can access the mesh without intrusion and are managed in a unified manner.

- Dubbo

    Services developed by the Dubbo SDK can access the mesh non-intrusively and are managed in a unified manner.

## Compatibility and Extensions

- Version compatibility

    API is fully compatible with common service meshes.

- Plugin support

    Supports Tracing, Prometheus, Kiali, and Grafana.
