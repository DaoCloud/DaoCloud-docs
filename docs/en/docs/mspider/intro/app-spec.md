# Specification for App Integration into Service Mesh

In order for your application to be integrated into the mesh and to experience all the capabilities of the mesh, we need to apply some specifications to the application.
This page introduces the basic principles and structure of the service mesh, as well as the specifications and suggestions for integrating applications into the service mesh.

Of course, if your application does not run as expected after being integrated into the mesh, you can also troubleshoot according to this page to confirm whether the application configuration complies with the specifications.

## Introduction

### Service Mesh Overview

Service Mesh is an infrastructure layer used to handle service-to-service communication.
In a microservice architecture, the service mesh helps form its complex topology so that it can better run, observe, protect, and configure microservices.
Service mesh is usually used in large-scale enterprise applications that contain a large number of microservices.

Our service mesh product is based on the Istio open-source project and provides a complete set of service mesh solutions,
including support for multicloud applications, support for multiple development languages, support for multiple deployment methods, and support for multiple application scenarios.

### Purpose and Scope of Specification

The purpose of this "Specification for App Integration into Service Mesh" is to provide specific guidance to help developers and teams understand the core concepts and workflows of the service mesh,
and correctly integrate applications into the service mesh, ensuring that services run stably, securely, and efficiently.

This specification is mainly applicable to technical personnel who have some basic knowledge of microservices and hope to further understand and use service mesh technology.
Whether you are new to the service mesh or already have some understanding and hope to deepen your understanding of the integration process, this specification will provide you with detailed guidance and practical suggestions.

## Basic Principles and Structure of Service Mesh

The service mesh is an infrastructure layer used to handle service-to-service communication. It is responsible for reliable, fast, and secure network request transmission between services in a microservice architecture.
By providing functions such as service discovery, load balancing, fault recovery, and service access policies, the service mesh helps developers focus on building business logic without having to care about the details of service-to-service communication.

In the service mesh architecture, network communication is abstracted into requests and responses between services. These requests and responses are routed between services through the service mesh,
and the mesh is responsible for handling problems such as retries, timeouts, circuit breaking, and authentication. Developers only need to declare how they want requests and responses to be handled, and the service mesh is responsible for implementing these policies.

To achieve these functions, a service mesh usually consists of two parts: the data plane and the control plane.

- The data plane consists of a set of network proxies that run as sidecars in each service instance of the application, handling the network communication in and out of that instance.
- The control plane manages and configures the proxies of the data plane, and provides management functions of the service mesh, such as traffic management, policy configuration, service discovery, authentication, monitoring, and reporting.

Because sidecars are introduced, we need to apply some specifications to the applications integrated into the mesh to ensure that the applications can run normally.

## Specifications and Suggestions for Service Integration

### Overview of the Integration Process

In the process of integrating your application into the service mesh, you need to pay attention to the following steps to ensure that the integration goes smoothly:

- **Understand the service mesh**: Before integrating the application, developers need to understand the basic concepts, core components, and operation mode of the service mesh.
  Understanding the service mesh can help developers better integrate the application.
- **Evaluate the applicability of the application**: Evaluate whether your application is suitable for running in a service mesh environment, for example, whether it is compatible with the communication protocols of the service mesh and whether it can run in a containerized environment.
  In addition, developers also need to understand the changes brought by the service mesh, for example, traffic routing and load balancing are all controlled by the service mesh.
- **Modification and optimization of the application**: According to the specifications of the service mesh, you may need to modify the application, such as exposing health checks, logs, and tracing information,
  so that the service mesh can monitor and manage it. At the same time, you should also consider how to handle the functions that the service mesh handles outside the application, such as retries and timeout control.
- **Integrate the service mesh**: Carry out code-level integration according to the interface or SDK provided by the service mesh. This usually includes importing the relevant libraries,
  initializing the service, and setting service discovery and load balancing policies.
- **Testing and optimization**: After the application is integrated into the service mesh, sufficient testing is required to ensure the performance and behavior of the application in the service mesh environment.
  In addition, according to the test results, you may need to further optimize the application or the service mesh configuration.

### Application Runtime Environment Requirements

Because a sidecar is introduced into the same Pod instance, the following requirements are imposed on the runtime environment of the application when integrating it into the service mesh:

| Field | Required | Value | Explanation |
| ----- | -------- | ----- | ----------- |
| Port Listening | Yes | The application should not listen on the following ports:<br>- 15000 to 15010<br>- 15020 to 15021<br>- 15053<br>- 15090 | The data plane of the service mesh needs to listen on these ports, so the application should not listen on them. |
| Pod Labels | Yes | The values of the __app__ and __version__ labels of the Pod must match the name of the associated __Service__ , not the labels of the Deployment itself. These labels are usually found in the `.spec.template.metadata.labels` section of the Pod. | Observability and traffic routing features are based on the __app__ and __version__ labels of the Pod, so it is important to ensure that the labels and their values match the __Service__ . |
| User UID | Yes | The application should not run with a UID of 1337. | The data plane of the service mesh runs with a UID of 1337, and the traffic interception of the sidecar does not handle traffic from this user, so the application should not run with a UID of 1337. |
| HostNetwork | Yes | Pods should not run in HostNetwork mode. | HostNetwork mode is not supported by the service mesh. |
| DNSPolicy | Yes | The DNSPolicy of the Pod should be set to ClusterFirst, and the ndots value should be set to 5. | The sidecar needs to communicate with the control plane and relies on DNS resolution of control plane addresses. |
| Base ID for Applications with Envoy Process | No | If the business application runs Envoy, add the `--base-id XXX` parameter. | Since the sidecar uses Envoy, if the __--base-id__ parameter is not added, two Envoy instances cannot coexist. |

### Application Communication Specifications

| Field | Required | Value | Explanation |
| ----- | -------- | ----- | ----------- |
| Service Access Method | No | Services should be accessed using the service name or ClusterIP, not the Pod IP or NodePort. | The data plane of the service mesh needs to match policies based on the service name, so applications should not directly use the Pod IP or NodePort. Otherwise, it may cause policy failures or accessibility issues. |
| Port Protocol | No | Configure the protocol of the Service ports correctly. In multi-cluster mode, ensure that the configuration of the service is consistent across all clusters (i.e., services with the same name in the same namespace should have consistent Service.spec configurations). | You can modify the protocol of specific ports in the DCE service mesh interface ( __Service Management__ -> __Service List__ -> __Address Information__ ), or refer to the [Istio documentation](https://istio.io/latest/docs/ops/configuration/traffic-management/protocol-selection/) for configuration. Incorrect configuration may cause access or policy issues. |

### Integration with Distributed Tracing

We currently use [OpenTelemetry](https://opentelemetry.io/) as the standard for distributed tracing, and by default the trace information is reported to the observability module. If you want to use the distributed tracing feature, you need to import the OpenTelemetry SDK into your application and configure the tracing parameters. For details, refer to the [official OpenTelemetry documentation](https://opentelemetry.io/docs/).

Or, if you want to use it in a simple way, you can simply pass through the TraceContext of the W3C standard. For details, refer to [W3C TraceContext](https://www.w3.org/TR/trace-context/).
That is, send the __traceparent__ and __tracestate__ request headers in the request to the message headers that need to be requested.

### Recommended Configuration

In order for your application to run better in the service mesh environment, we recommend that you make the following configurations in your application:

#### Health Checks

Configure health checks for your application so that the service mesh can better monitor the health status of your application. For details, refer to the
[official Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

#### Retry Mechanism

Due to the existence of the Sidecar mechanism, there may be a situation where the Sidecar starts after the service. During this period,
your service may not be able to access external requests. Therefore, we recommend that you configure a retry mechanism in your application so that requests can be automatically retried after the Sidecar starts.

#### Use HTTP or GRPC as the Application Communication Protocol

Our service mesh currently supports the HTTP and GRPC protocols very well. We recommend that your application also use these two protocols.
If your application uses other protocols, such as BRPC, they will be downgraded to the TCP protocol, which may cause some features to be unavailable.

By default, the service mesh performs TLS encryption (mTLS) for service-to-service access, so we also do not recommend using the HTTPS protocol for service-to-service access (it will be treated as the TCP protocol).

Therefore, we recommend that your application use the HTTP or GRPC protocol.

#### Avoid Using External Registry Mechanisms

Although our product supports integrating services that use a registry into the service mesh, this is not the way we recommend.
We recommend that your application directly use the service discovery mechanism of the service mesh (the Service of Kubernetes), so that the features of the service mesh can be better used.

That is, we do not recommend developing new applications with frameworks such as Spring Cloud, but such existing applications can be supported by our product.
If it is a Java application, we recommend developing the application in the way of Spring Boot.

### Service Exposure to the Outside World

By default, for applications integrated into the service mesh, we do not recommend using methods such as NodePort or LoadBalancer to directly provide services to the outside world, as this will cause some service mesh features to be unavailable.

In the current version, we have two ways to provide services to the outside world:

1. Use the __Mesh Gateway__ to expose services to the outside world.
2. Use the __Cloud Native Gateway__ of the __Microservice Engine__ to expose services to the outside world.

For how to use the __Cloud Native Gateway__ of the __Microservice Engine__ , refer to the relevant documentation.

For how to use the __Mesh Gateway__ , also refer to the relevant documentation. It is worth noting that we recommend separating the VirtualService that provides services to the outside world,
and not mixing it with other VirtualServices (such as the VirtualService with the same name as the Service), so that it can be better managed.
