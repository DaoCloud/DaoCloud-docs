# Specification for App Integration into Service Mesh

As an Istio expert, I have some recommendations for integrating your application
into the service mesh to ensure it operates efficiently, securely, and reliably. 

## Introduction

### Overview of Service Mesh

Service Mesh is an infrastructure layer that handles communication between services
in a service-to-service architecture. It helps manage complex topology and enables
microservices to run, observe, protect and configure better. Our Istio-based product
provides multi-cloud application support, multiple development languages, multiple
deployment methods, and various application scenarios.

### Purpose and Scope of Specification

The specification offers specific guidance on integrating applications
to the service mesh, ensuring stable, secure, and efficient operation of services. This specification
is mainly applicable to technical personnel with a certain understanding of microservices and hope
to understand and use service mesh technology.

## Basic Principles and Structure of Service Mesh

To achieve reliable, fast, and secure transmission of network requests between various services
in a microservices architecture, Service Mesh uses two parts: the data plane and the control plane.

- The data plane consists of a set of network proxies that run as sidecars in each service instance.
- The control plane manages and configures the proxies of the data plane, provides management
  functionalities of service mesh such as traffic management, policy configuration, service discovery,
  authentication, monitoring, and reporting.

Standardizing the applications that connect to the mesh ensures they operate correctly with the introduction of sidecars.

## Specifications and Suggestions for Service Integration

### Overview of the Integration Process

To ensure successful integrate to the Service Mesh during integration, we recommend following these steps:

- **Understand the Service Mesh**: Understand basic concepts, core components, and the operation mode of the Service Mesh.
- **Integrate Application Compatibility**: Evaluate whether your application is suitable for running in a Service Mesh
  environment and understand changes brought by the Service Mesh like traffic routing, load balancing, etc.
- **Modification and Optimization of Applications**: Modify your application according to the Service Mesh specifications,
  such as exposing health checks, logs, tracking information, etc., to allow the Service Mesh to monitor and manage them.
- **Integrating the Service Mesh**: Integrate at the code level using the interface or SDK provided by the Service Mesh.
- **Testing and Optimization**: Test thoroughly to ensure reliable performance and behavior of the application
  in the Service Mesh environment.

### Application Runtime Environment Requirements

As a sidecar is introduced to the same Pod instance, the following runtime environment requirements
must be met for application integrating to the Service Mesh:

| Requirement                    | Mandatory | Requirement Value                                                                                                                                                                                                                                                         | Explanation                                                                                                                                                                              |
| ------------------------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Port Listening                 | Yes       | The application cannot listen on the following ports: <br><li>15000 - 15010</li><br><li>15020 - 15021</li><br><li>15053</li><br><li>15090</li>                                                                                                                           | As the data plane of the Service Mesh needs to listen on these ports, applications cannot listen on them.                                                                                |
| Pod Label                      | Yes       | The value of the `app` label in the Pod must be the same as the associated `Service` name, not the label of the Deployment itself, but the label of the Pod (usually located in `.spec.template.metadata.labels`). | Observations, Traffic Lanes, and other functionalities are based on the `app` label of the Pod, so it is necessary to ensure that the value of the `app` label is the same as the `Service` name.|
| User UID                       | Yes       | Cannot run as a user with UID of 1337                                                                                                                                                                                                                                       | The data plane of the Service Mesh needs to run as a user with UID of 1337, and the traffic interception of the sidecar will not process traffic from this user, so applications cannot run as a user with UID of 1337. |
| HostNetwork                    | Yes       | The Pod cannot run in HostNetwork mode.                                                                                                                                                                                                                                     | HostNetwork mode is not supported by the Service Mesh.                                                                                                                                   |
| DNSPolicy                      | Yes       | The recommended DNSPolicy for the Pod is ClusterFirst, and the value of ndots is recommended to be set to 5.                                                                                                                                                             | As the sidecar needs to communicate with the control plane, it depends on DNS resolution of the control plane address.                                                                |
| Application base-id containing Envoy process | No      | If the business application runs Envoy, add the `--base-id XXX` parameter.                                                                                                                                                                                                      | As the sidecar uses Envoy, if the `--base-id` parameter is not added, two Envoys cannot coexist.                                                                                          |

### Application Communication Specifications

| Requirement   | Mandatory | Requirement Value                                                                                                                                                    | Explanation                                                                                                                                                                                                                            |
| ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Traffic Protocol | Yes       | The Service Mesh supports HTTP/1.1, HTTP/2, and gRPC traffic only.                                                                                           | The Service Mesh cannot support traffic protocols other than these.                                                                                                                                                                   |
| Protocol Scheme  | Yes       | Applications must use http:// or https:// scheme in the URL to integrate services in the Service Mesh.                                                           | The Service Mesh uses the HTTP protocol as the unified communication protocol, and the scheme is used to distinguish between plaintext and encrypted traffic.                                                                       |
| Service Discovery    | Yes       | Integrate the service using the hostname of the service instead of integrating it directly through the IP address.                                           | The Service Mesh uses Istio's service discovery mechanism, which relies on DNS resolution of the service name, so applications need to integrate services using the hostname of the service.                                      |
| Sidecar Injection | Yes / No   | If auto sidecar injection is enabled, applications do not need to add sidecars. Otherwise, you need to manually add the sidecar to the Pod.             | By default, the Service Mesh automatically injects a sidecar into the Pod, but if it is disabled, the application needs to manually add the sidecar to the Pod.                                                                      |
| Service Port     | Yes       | Configure the application to use the port provided by the Service Mesh when integrating the service.                                                       | After the sidecar is injected, the application integrates the service through the localhost:port, where port numbers are assigned by the Service Mesh dynamically.                                                             |
| Distributed Tracing | No      | To enable distributed tracing, the application needs to write tracing information into the HTTP headers according to the W3C Trace Context standard, or use the OpenTelemetry SDK to integrate with the Service Mesh. | To facilitate distributed tracing in the Service Mesh, applications can write tracing information into the HTTP headers according to the W3C Trace Context standard, or use the OpenTelemetry SDK to integrate with the Service Mesh. |

## Integration with Distributed Tracing

As an Istio expert, I recommend using [OpenTelemetry](https://opentelemetry.io/) as the standard for distributed tracing
in our Service Mesh. By default, the trace information is reported to the observability module. To use distributed tracing,
you need to import the OpenTelemetry SDK into your application and configure the tracing parameters. You can refer to the
[official OpenTelemetry documentation](https://opentelemetry.io/docs/) for specific guidance.

Alternatively, if you prefer a simpler approach, you can pass through the `TraceContext` of the W3C standard,
which is detailed in [W3C TraceContext](https://www.w3.org/TR/trace-context/). Specifically, send the `traceparent`
and `tracestate` headers from the request header to the message header that needs to be requested.

## Recommended Configuration

To ensure optimal operation of your application in the Service Mesh environment,
make the following configurations in your application:

### Health Checks

Configure health checks for your application so that the Service Mesh can monitor the health status of
your application more effectively. Refer to the
[official Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
for specific guidance.

### Retry Mechanism

The Sidecar mechanism in the Service Mesh may cause situations where the Sidecar starts after the service.
During this period, your service may not be able to integrate external requests. Therefore, configure
a retry mechanism in your application to automatically retry requests after the Sidecar starts.

### Use HTTP or GRPC as the Application Communication Protocol

Our Service Mesh supports HTTP and GRPC protocols efficiently. Therefore, we recommend your application
also using these two protocols. If your application uses other protocols such as BRPC, it will be downgraded
to the TCP protocol, causing some functions to be unavailable.

By default, the Service Mesh performs TLS encryption (mTLS) for service-to-service communication. Therefore,
we do not recommend using HTTPS protocol for communication between services as it will be treated as the TCP protocol.

### Avoid Using External Registry Mechanisms

Although our product supports using a registry center to integrate the Service Mesh, this is not the recommended approach.
We recommend that your application directly use the service discovery mechanism of the Service Mesh (Kubernetes Service)
so that you can better utilize the functionalities of the Service Mesh.

We do not recommend developing new applications using frameworks like Spring Cloud, but these types of
existing applications can be supported by our product. If you are developing Java applications, we
recommend using the Spring Boot framework.

## Service Exposure to the Outside World

By default, I recommend that applications connected to the Service Mesh avoid using NodePort or LoadBalancer
to directly expose their services to the outside world as this will prevent certain Service Mesh functionalities from being used.

In the current version, two ways can be used to expose services to the outside world:

1. Use the `Mesh Gateway` to expose services to the outside world.
2. Use the `Cloud-Native Gateway` of the `Microservice Engine` to expose services to the outside world.

Refer to the relevant documentation for instructions on using the `Cloud-Native Gateway` of the `Microservice Engine`.
For instructions on using the `Mesh Gateway`, also refer to the relevant documentation. Separating the VirtualService
that needs to provide services to the outside world from other VirtualServices (such as VirtualService with the same name
as Service) is recommended for better management purposes.
