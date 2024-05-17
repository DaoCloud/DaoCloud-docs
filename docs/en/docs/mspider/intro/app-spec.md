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

| Field | Required | Value | Explanation |
| ----------- | -------- | ----- | ----------- |
| Port Listening | Yes | The application should not listen on the following ports:<br>- 15000 to 15010<br>- 15020 to 15021<br>- 15053<br>- 15090 | The data plane of the service mesh needs to listen on these ports, so the application should not listen on them. |
| Pod Labels | Yes | The values of the __app__ and __version__ labels of the Pod must match the name of the associated __Service__ , not the labels of the Deployment itself. These labels are usually found in the __.spec.template.metadata.labels__ section of the Pod. | Observability and traffic routing features are based on the __app__ and __version__ labels of the Pod, so it is important to ensure that the labels and their values match the __Service__ . |
| User UID | Yes | The application should not run with a UID of 1337. | The data plane of the service mesh runs with a UID of 1337, and the traffic interception of the sidecar does not handle traffic from this user, so the application should not run with a UID of 1337. |
| HostNetwork | Yes | Pods should not run in HostNetwork mode. | HostNetwork mode is not supported by the service mesh. |
| DNSPolicy | Yes | The DNSPolicy of the Pod should be set to ClusterFirst, and the ndots value should be set to 5. | The sidecar needs to communicate with the control plane and relies on DNS resolution of control plane addresses. |
| Base ID for Applications with Envoy Process | No | If the business application runs Envoy, add the `--base-id XXX` parameter. | Since the sidecar uses Envoy, if the __--base-id__ parameter is not added, two Envoy instances cannot coexist. |

### Application Communication Specifications

| Field | Required | Value | Explanation |
| ----------- | -------- | ----- | ----------- |
| Service Access Method | No | Services should be accessed using the service name or ClusterIP, not the Pod IP or NodePort. | The data plane of the service mesh needs to match policies based on the service name, so applications should not directly use the Pod IP or NodePort. Otherwise, it may cause policy failures or accessibility issues. |
| Port Protocol | No | Configure the protocol of the Service ports correctly. In multi-cluster mode, ensure that the configuration of the service is consistent across all clusters (i.e., services with the same name in the same namespace should have consistent Service.spec configurations). | You can modify the protocol of specific ports in the DCE 5.0 service mesh interface ( __Service Management__ > __Service List__ > __Address Information__ ), or refer to the [Istio documentation](https://istio.io/latest/docs/ops/configuration/traffic-management/protocol-selection/) for configuration. Incorrect configuration may cause access or policy issues. |

## Integration with Distributed Tracing

As an Istio expert, I recommend using [OpenTelemetry](https://opentelemetry.io/) as the standard for distributed tracing
in our Service Mesh. By default, the trace information is reported to the observability module. To use distributed tracing,
you need to import the OpenTelemetry SDK into your application and configure the tracing parameters. You can refer to the
[official OpenTelemetry documentation](https://opentelemetry.io/docs/) for specific guidance.

Alternatively, if you prefer a simpler approach, you can pass through the __TraceContext__ of the W3C standard,
which is detailed in [W3C TraceContext](https://www.w3.org/TR/trace-context/). Specifically, send the __traceparent__ 
and __tracestate__ headers from the request header to the message header that needs to be requested.

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

1. Use the __Mesh Gateway__ to expose services to the outside world.
2. Use the __Cloud Native Gateway__ of the __Microservice Engine__ to expose services to the outside world.

Refer to the relevant documentation for instructions on using the __Cloud Native Gateway__ of the __Microservice Engine__ .
For instructions on using the __Mesh Gateway__ , also refer to the relevant documentation. Separating the VirtualService
that needs to provide services to the outside world from other VirtualServices (such as VirtualService with the same name
as Service) is recommended for better management purposes.
