---
hide:
  - toc
---

# Microservice Engine

DaoCloud Microservice Engine is a one-stop microservice management platform for mainstream microservice ecosystems
in the industry. It mainly provides two dimensions of functionalities: Microservice Governance Center and
Microservice Gateway. It covers various management scenarios throughout the microservice lifecycle, including
service registration and discovery, configuration management, traffic governance, service-level tracing, API management,
domain management, monitoring, and alerting. The Microservice Engine has strong compatibility and can seamlessly
integrate with other components of DCE 5.0. It also perfectly supports open-source ecosystems such as Spring Cloud
and Dubbo, helping you to build your own microservice system using open-source microservice technologies more conveniently.

<div class="grid cards" markdown>

-   :material-run-fast:{ .lg .middle } __Quick Start__

    ---

    - [Manage Components of Microservice Engine](../quickstart/skoala.md)
    - [Initialize Component of Microservice Engine Cluster](../quickstart/skoala-init.md)
    - [Select Workspace](../quickstart/select-workspace.md)
    - [Troubleshoot skoala-init](../troubleshoot/auth-server.md)

-   :material-connection:{ .lg .middle } __Service Integration Specification__

    ---

    - [Integrate with Sentinel](../standard/sentinel.md)
    - [Integrate with Nacos SDK](../standard/nacos.md)
    - [Integrate with Sentinel Monitoring](../standard/monitor.md)
    - [Integrate with Sentinel Cluster Flow Control](../standard/flow-control.md)

-   :fontawesome-solid-cubes-stacked:{ .lg .middle } __Best Practices__

    ---

    - [Experience Microservice Governance with Sample Applications](../best-practice/use-skoala-01.md)
    - [Using JWT Plugin in Cloud-Native Microservices](../best-practice/plugins/jwt.md)
    - [Integrate Microservice Gateway with Authentication Server](../best-practice/auth-server.md)
    - [Gateway API Policy](../best-practice/gateway02.md)

-   :material-engine:{ .lg .middle } __Cloud Native Microservices__

    ---

    - [Import/Remove Services](../cloud-ms/index.md)
    - [Traffic Governance](../cloud-ms/traffic-control.md)
    - [Nacos Stress Testing Report](../tests/nacos-stress-test.md)

-   :simple-amazonapigateway:{ .lg .middle } __Cloud Native Gateway__

    ---

    - [Gateway Management](../gateway/index.md)
    - [API Management](../gateway/api/index.md)
    - [Service Integration](../gateway/service/manual-integrate.md)
    - [Monitoring and Alerting](../gateway/alert.md)
    - [Domain Management](../gateway/domain/index.md)
    - [Gateway Stress Testing Report](../tests/gateway-stress-test.md)

-   :simple-legacygames:{ .lg .middle } __Traditional Microservices__

    ---

    - [Hosted Registration and Configuration Center](../trad-ms/hosted/index.md)
        - [Microservice List](../trad-ms/hosted/services/index.md)
        - [Microservice Configuration Management](../trad-ms/hosted/configs.md)
        - [Microservice Monitoring](../trad-ms/hosted/monitor/microservices.md)
    - [Integrated Registration Center](../trad-ms/integrated/index.md)
        - [Microservice Management](../trad-ms/integrated/manage-service.md)
        - [Service Tracing](../trad-ms/integrated/trace.md)

</div>
