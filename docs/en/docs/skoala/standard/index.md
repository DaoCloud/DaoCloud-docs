---
hide:
  - toc
---

# Service Integration Standards

This section describes the integration standards that traditional microservices must follow when integrating with the hosted registry of the microservice engine. Only when applications meet the corresponding standards can they properly use the traffic governance, data monitoring, and other capabilities provided by the microservice engine.

## Integration Standards

<div class="grid cards" markdown>

- :material-account-group:{ .lg .middle } __Integrate Nacos SDK__

    ---

    Explains how traditional microservices in different frameworks can integrate with the native Nacos SDK for service registration and discovery.

    [:octicons-arrow-right-24: Get Started](nacos.md)

- :material-format-list-bulleted:{ .lg .middle } __Integrate with Sentinel Specification__

    ---

    Describes the parameter specifications that applications must meet when integrating with the Sentinel console, so as to properly use Sentinel traffic governance and data monitoring capabilities.

    [:octicons-arrow-right-24: Get Started](sentinel.md)

- :material-hub:{ .lg .middle } __Integrate Sentinel Monitoring__

    ---

    Explains how to integrate traditional microservices with the Sentinel monitoring feature, covering dependencies, javaagent parameters, and Kubernetes Service configuration.

    [:octicons-arrow-right-24: Get Started](monitor.md)

- :material-swap-horizontal:{ .lg .middle } __Integrate Sentinel Cluster Flow Control__

    ---

    Describes the configuration adjustments on both the server and client sides when integrating a service with Sentinel cluster flow control.

    [:octicons-arrow-right-24: Get Started](flow-control.md)

</div>
