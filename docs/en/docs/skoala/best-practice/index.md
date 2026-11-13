---
hide:
  - toc
---

# Best Practices

This section collects best practices for the microservice engine, covering typical use cases of microservice governance, the cloud-native gateway, and the registry center. All examples are verified in real environments and can serve as references for production.

## Microservices and Registry

<div class="grid cards" markdown>

- :material-school:{ .lg .middle } __Experience Microservice Governance with Sample Applications__

    ---

    Experience microservice governance features through sample applications, covering the registry and configuration center, cloud-native microservices, and the cloud-native gateway.

    [:octicons-arrow-right-24: Get started](use-skoala-01.md)

- :material-account-group:{ .lg .middle } __Nacos LDAP Integration for User Management__

    ---

    Integrate Nacos (named registry center in the microservice engine) with LDAP for unified user management.

    [:octicons-arrow-right-24: Get started](nacos-ldap.md)

</div>

## Cloud Native Gateway

<div class="grid cards" markdown>

- :material-gate:{ .lg .middle } __Accessing a Service through Gateway__

    ---

    Demonstrate how to integrate a microservice with the cloud-native gateway and access it through the gateway.

    [:octicons-arrow-right-24: Get started](gateway01.md)

- :material-api:{ .lg .middle } __Gateway API Policies__

    ---

    Use a real microservice application to demonstrate how to configure over ten API policies, such as load balancing, timeout retry, and allow/deny lists, along with their actual effects.

    [:octicons-arrow-right-24: Get started](gateway02.md)

- :material-hub:{ .lg .middle } __Integrating Gateway with Service Mesh__

    ---

    Integrate the cloud-native gateway with the service mesh to access services in the mesh through the gateway, with full traffic governance capabilities such as virtual services and destination rules.

    [:octicons-arrow-right-24: Get started](gateway-mesh.md)

- :material-format-list-bulleted:{ .lg .middle } __Add Custom Attributes to Gateway Request Logs__

    ---

    The gateway uses contour as the control plane to deliver configuration to envoy, including request log fields. This guide shows how to add custom attributes.

    [:octicons-arrow-right-24: Get started](add-custom-attributes.md)

- :material-swap-horizontal:{ .lg .middle } __HTTP to Dubbo Protocol Dynamic Routing__

    ---

    Use the protocol conversion capability of Pixiu to convert the HTTP protocol to the Dubbo protocol for dynamic routing.

    [:octicons-arrow-right-24: Get started](http-to-dubbo.md)

</div>
