---
hide:
  - toc
---

# Cloud-Native Gateway

A gateway is an intermediate layer between clients and server-side applications, through which all external requests must pass. Cloud-native gateway refers to a decoupled gateway based on the concept of cloud-native declarative APIs. Examples of cloud-native gateways include Zuul, Kong, Nginx, Spring Cloud Gateway, Envoy, and more. The most notable feature of cloud-native gateways is the ability to define the runtime configuration of the gateway through declarations, which can be automatically generated through the control plane's declarations.

The functionality of cloud-native gateways is similar to that of microservices gateways. It includes features such as authentication, routing, monitoring, load balancing, caching, service upgrade and downgrade, static response handling, traffic control, logging, retries, and circuit breaking.

- Sentinel

    Sentinel is a traffic control component designed for distributed service architectures. It focuses on traffic control, circuit breaking, and system adaptive protection to ensure the stability of microservices. Sentinel has been extensively used in core scenarios such as handling the traffic surge during Alibaba's Double 11 shopping festival over the past decade. It provides comprehensive real-time monitoring, allowing users to view second-level data for individual machines in the application through the console. Sentinel also offers integration modules with other open-source frameworks/libraries, such as Spring Cloud, Dubbo, and gRPC, enabling out-of-the-box usage. Additionally, Sentinel provides a simple and complete SPI extension interface, allowing users to customize the logic by implementing the extension interface rapidly.

- Envoy

    Envoy is a high-performance network proxy designed for service architectures. It possesses powerful customization capabilities. Envoy is an L7 proxy and communication bus designed for service architectures, with its core being an L3/L4 network proxy. Envoy typically runs as a sidecar alongside applications or as an edge proxy for the network. Its features include an out-of-process architecture, L3/L4 filter architecture, HTTP L7 filter architecture, first-class HTTP/2 and HTTP/3 support, HTTP L7 routing, gRPC support, service discovery and dynamic configuration, health checks, advanced load balancing, front-end/edge proxy support, and excellent observability.

- Contour

    Contour deploys Envoy as a reverse proxy and load balancer, serving as an ingress controller for Kubernetes. Contour supports dynamic configuration updates and introduces a new Ingress API (HTTPProxy). This API is implemented through custom resource definitions (CRDs) and aims to extend the functionality of the Ingress API, providing a richer user experience and addressing limitations in the original design. Contour's architecture is flexible and can be deployed as a Kubernetes Deployment or DaemonSet. Additionally, Contour provides TLS certificate delegation, allowing administrators to securely delegate access to wildcard certificates.
