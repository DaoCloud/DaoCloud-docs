---
MTPE: windsonsea
date: 2024-01-10
---

# Features

This section describes the features supported by the service mesh.

## Service Management

- Service Registration and Discovery

    Support service registration and discovery, including dynamic registration and deregistration of service instances.

- VM Service Registration

    Support VM service registration, allowing for one-line command to register and manage VM services.

- Intelligent Service Diagnosis

    Support automatic inspection of the configuration of services accessing the service mesh based on best practices. Provide strategies for one-click repair and manual repair.

## Traffic Management

- Layer 7 Connection Pool Management

    Configurable settings include the maximum number of HTTP requests, retries, waiting requests, requests per connection, and idle connection time.

- Layer 4 Connection Pool Management

    Configurable settings include the maximum number of TCP connections, connection timeout, maximum number of unresponsive connections, minimum idle time, and health check interval.

- Outlier Detection

    Supports configuration of service circuit breaking rules, including the number of consecutive errors before an instance is evicted, inspection cycle, basic isolation time, and maximum proportion of isolated instances.

- Retry

    Configurable settings include the number of HTTP retries, retry timeout, and retry conditions.

- Timeouts

    Supports configuring HTTP request timeouts.

- Load Balancing

    Supports configuration of random scheduling, round-robin scheduling, least connection, and consistent hash load balancing algorithms.

- HTTP Headers

    Flexible addition, modification, and deletion of specified HTTP headers, including operations on headers before forwarding HTTP requests to target services, and operations on headers before replying to HTTP responses from clients.

- Fault Injection

    Supports configuration of delayed and interrupt faults.

## Security

- Transparent mTLS Authentication

    Supports mTLS authentication on GUI, including peer and request authentications.

- Fine-Grained Access Authorization

    Supports configuration of access authorization between services through the interface (the background API can configure Namespace-level authorization, and authorization can be given to a specific interface).

## Sidecar management

- sidecar injection

    Supports the sidecar injection strategy of configuring services through the interface, and supports the multi-dimensional sidecar default injection strategy.

- Sidecar hot upgrade

    It supports sidecar hot upgrade. After the control plane is upgraded, it automatically detects the sidecar version and gives upgrade suggestions. It supports seamless hot upgrade without interrupting the business.

- Sidecar service discovery scope

    Supports custom configuration of sidecar service discovery scope and greatly reduces the pressure on sidecar resource consumption according to different business scenarios.

## Observability

- Traffic Topology

    Supports viewing the mesh application traffic topology to understand dependencies between services.

- Service Operation Monitoring

    Supports viewing service access information, including QPS and latency metrics of services and service versions.

- Access Log

    Supports collecting and retrieving access logs for services.

- Call Chain

    Supports non-intrusive call chain tracing and can pinpoint and locate problems by retrieving call chain data.

## Multicluster Mode

- Unified Management of Multicluster Configuration

    Supports mesh configuration and cluster configuration management of multiple clusters under the mesh. Supports sidecar injection policies of different clusters with different granularities and supports unified management of data plane configurations such as cross-cluster traffic policies.

- Scalability

    Supports one-click access and removal of clusters.

## Mesh Data Plane Microservice Framework

- Spring Cloud

    Services developed with the Spring Cloud SDK can access the mesh without intrusion and are managed in a unified manner.

- Dubbo Protocol

    Services developed by the Dubbo SDK can access the mesh non-intrusively and are managed in a unified manner.

## Compatibility and Extensions

- Version Compatibility

    The API is fully compatible with common service meshes.

- Plugin Support

    Supports Tracing, Prometheus, Kiali, and Grafana.
