---
MTPE: windsonsea
Date: 2024-04-24
hide:
  - toc
---

# Microservice Engine

DaoCloud Microservice Engine is a one-stop microservice management platform for mainstream microservice ecosystems
in the industry. It mainly provides two dimensions of functionalities: Microservice Governance Center and
Microservice Gateway. It covers various management scenarios throughout the microservice lifecycle, including
service registration and discovery, configuration management, traffic governance, service-level tracing, API management,
domain management, monitoring, and alerting. The Microservice Engine has strong compatibility and can seamlessly
integrate with other components of DaoCloud. It also perfectly supports open-source ecosystems such as Spring Cloud
and Dubbo, helping you to build your own microservice system using open-source microservice technologies more conveniently.

## Product Panorama

<style>
.tf-arch-card{min-width:calc(25% - 10px) !important}
.tf-arch{overflow:visible !important}
.tf-arch-card{overflow:visible !important}
.tf-arch-card::after{display:none !important}
.tf-arch-layer:first-child{border-radius:14px 14px 0 0 !important}
.tf-arch-layer:last-child{border-radius:0 0 14px 14px !important}
.tf-arch-card-tip{
  opacity:0;
  position:absolute;
  bottom:calc(100% + 8px);
  left:50%;
  transform:translateX(-50%);
  background:rgba(0,0,0,0.85);
  color:#fff;
  padding:0.35rem 0.65rem;
  border-radius:6px;
  font-size:0.72rem;
  font-weight:500;
  white-space:nowrap;
  z-index:100;
  pointer-events:none;
  box-shadow:0 4px 12px rgba(0,0,0,0.2);
  transition:opacity 0.2s ease
}
.tf-arch-card-tip::after{
  content:"";
  position:absolute;
  top:100%;
  left:50%;
  transform:translateX(-50%);
  border:5px solid transparent;
  border-top-color:rgba(0,0,0,0.85)
}
.tf-arch-card:hover .tf-arch-card-tip{
  opacity:1
}
</style>

<div class="tf-arch tf-arch--compact">
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">Gateway</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/">
        <span class="tf-arch-card-title">Gateway Management</span>
        <span class="tf-arch-card-tip">Lifecycle management of gateway instances</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/api/">
        <span class="tf-arch-card-title">API Management</span>
        <span class="tf-arch-card-tip">API policies and secure authentication</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/domain/">
        <span class="tf-arch-card-title">Domain Management</span>
        <span class="tf-arch-card-tip">Domain and policy configuration</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/alert/">
        <span class="tf-arch-card-title">Monitoring and Alerting</span>
        <span class="tf-arch-card-tip">Resource and service metrics</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">Cloud Native</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="../cloud-ms/traffic-control/">
        <span class="tf-arch-card-title">Traffic Governance</span>
        <span class="tf-arch-card-tip">Mesh and Istio traffic governance</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../cloud-ms/lane/">
        <span class="tf-arch-card-title">Traffic Lane</span>
        <span class="tf-arch-card-tip">End-to-end canary release</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../standard/monitor/">
        <span class="tf-arch-card-title">Sentinel Monitoring</span>
        <span class="tf-arch-card-tip">Observing flow control rules</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">Traditional</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="../trad-ms/hosted/">
        <span class="tf-arch-card-title">Registry and Config Center</span>
        <span class="tf-arch-card-tip">Hosted Nacos and configuration</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../trad-ms/integrated/">
        <span class="tf-arch-card-title">Integrated Registry</span>
        <span class="tf-arch-card-tip">Eureka / ZooKeeper / Nacos / Consul</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../standard/sentinel/">
        <span class="tf-arch-card-title">Integrate with Sentinel</span>
        <span class="tf-arch-card-tip">Flow control, circuit breaking, hotspots</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">Shared Capabilities</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="../plugins/intro/">
        <span class="tf-arch-card-title">Plugin Center</span>
        <span class="tf-arch-card-tip">Wasm plugins with one-click toggle</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="features/">
        <span class="tf-arch-card-title">Features</span>
        <span class="tf-arch-card-tip">Complete feature list</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="scenarios/">
        <span class="tf-arch-card-title">Use Cases</span>
        <span class="tf-arch-card-tip">Typical scenarios and benefits</span>
      </a>
    </div>
  </div>
</div>

## Product Architecture

![Microservice Engine Architecture](../images/archi.svg)

## Documentation Navigation

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

    - [Import/Remove Services](../cloud-ms/traffic-control.md)
    - [Traffic Governance](../cloud-ms/traffic-control.md)
    - [Nacos Stress Testing Report](../tests/nacos-stress-test.md)

-   :material-gate:{ .lg .middle } __Cloud Native Gateway__

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

## Learning Path

<style>
.skoala-path{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0.75rem;margin:1.25rem 0 1.75rem}
.skoala-path-step{display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.skoala-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.skoala-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.skoala-path-step:nth-child(3n)::after,.skoala-path-step:last-child::after{display:none}
.skoala-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.skoala-path-title{font-weight:700;font-size:0.95rem}
.skoala-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.skoala-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.skoala-path{grid-template-columns:repeat(2,minmax(0,1fr))}.skoala-path-step::after{display:none}}
@media screen and (max-width: 520px){.skoala-path{grid-template-columns:1fr}}
</style>

<div class="skoala-path">
  <a class="skoala-path-step" style="--path-c:#2196f3" href="../quickstart/skoala/">
    <span class="skoala-path-num">1</span>
    <span class="skoala-path-title">Deploy the Engine</span>
    <span class="skoala-path-desc">Install Microservice Engine components</span>
    <span class="skoala-path-go">Go →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#00acc1" href="../quickstart/skoala-init/">
    <span class="skoala-path-num">2</span>
    <span class="skoala-path-title">Initialize Components</span>
    <span class="skoala-path-desc">Install the skoala-init cluster component</span>
    <span class="skoala-path-go">Go →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#43a047" href="../quickstart/select-workspace/">
    <span class="skoala-path-num">3</span>
    <span class="skoala-path-title">Select Workspace</span>
    <span class="skoala-path-desc">Define the management boundary</span>
    <span class="skoala-path-go">Go →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#fb8c00" href="../trad-ms/integrated/">
    <span class="skoala-path-num">4</span>
    <span class="skoala-path-title">Integrate Microservices</span>
    <span class="skoala-path-desc">Connect registries and manage traditional and cloud-native microservices</span>
    <span class="skoala-path-go">Go →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#8e24aa" href="../cloud-ms/traffic-control/">
    <span class="skoala-path-num">5</span>
    <span class="skoala-path-title">Govern Traffic</span>
    <span class="skoala-path-desc">Sentinel / Mesh for east-west traffic</span>
    <span class="skoala-path-go">Go →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#e53935" href="../gateway/">
    <span class="skoala-path-num">6</span>
    <span class="skoala-path-title">Configure Gateway</span>
    <span class="skoala-path-desc">Create gateways, manage north-south APIs</span>
    <span class="skoala-path-go">Go →</span>
  </a>
</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
