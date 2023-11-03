---
hide:
  - toc
---

# Cloud Native Gateway

The gateway is the middle layer between the client and the server, and all external requests need to go through the gateway layer.
The cloud native gateway refers to a gateway developed based on the cloud native declarative API concept and decoupled from the business, such as Zuul, Kong, Nginx, Spring Cloud Gateway, Envoy, etc.
The most notable feature of the cloud native gateway is that the runtime configuration of the gateway can be defined in a declarative manner, and the configuration can be automatically generated through the declaration of the control plane.
The features of the cloud native gateway are basically similar to those of the microservice gateway, such as authentication, routing, monitoring, load balancing, caching, service upgrading and upgrading, static response processing, flow control, logging, retrying, circuit breaking, etc.

- Sentinel

    Sentinel is a flow control component for distributed service architecture. It mainly takes flow as the entry point to ensure the stability of microservices from multiple dimensions such as flow control, fuse degradation, and system adaptive protection.
    Sentinel has a wealth of use cases, and has undertaken the core use cases of Alibaba's Double Eleven traffic promotion in the past 10 years. Sentinel has complete real-time monitoring, and users can see the second-level data of a single machine connected to the application in the console.
    Sentinel provides integration modules with other open source frameworks/libraries, such as integration with Spring Cloud, Dubbo, and gRPC, which can be used out of the box.
    In addition, Sentinel can also provide an easy-to-use and complete SPI extension interface, and users can quickly customize logic by implementing the extension interface.

-Envoy

    Envoy is a high-performance network proxy for service-oriented architecture with strong customization capabilities.
    Envoy is an L7 proxy and communication bus designed for service-oriented architecture, and its core is a L3/L4 network proxy.
    Envoy usually runs around the application as a sidecar, and can also run as an edge proxy of the network.
    Envoy's features include: out-of-process architecture, L3/L4 filter architecture, HTTP L7 filter architecture, first-class HTTP/2 support, HTTP/3 support, HTTP L7 routing, gRPC support, service discovery and dynamic configuration, Health checks, advanced load balancing, frontend/edge proxy support, best-in-class observability, and more.

-Contour

    Contour deploys Envoy as a reverse proxy and load balancer, acting as an ingress controller for Kubernetes.
    Contour supports dynamic configuration updates and also introduces a new ingress API (HTTPProxy).
    The API is implemented as a Custom Resource Definition (CRD) with the goal of extending the functionality of the Ingress API, providing a richer user experience and addressing shortcomings in the original design.
    Contour has a flexible architecture and can be deployed as a Kubernetes Deployment or Daemonset. In addition, Contour also has a TLS certificate authority feature, administrators can securely delegate wildcard certificate access.