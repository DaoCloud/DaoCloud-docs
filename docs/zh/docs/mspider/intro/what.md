---
hide:
  - toc
---

# 什么是服务网格

服务网格是基于 Istio 开源技术构建的面向云原生应用的下一代服务网格。

服务网格是一种具备高性能、高易用性的全托管服务网格产品，通过提供完整的非侵入式的微服务治理方案，能够统一治理多云多集群的复杂环境，
以基础设施的方式为用户提供服务流量治理、安全性治理、服务流量监控、以及传统微服务（SpringCloud、Dubbo）接入。

DCE 5.0 的服务网格兼容社区原生 Istio 开源服务网格，提供原生 Istio 接入管理能力。在较高的层次上，服务网格有助于降低服务治理的复杂性，减轻开发运维团队的压力。

服务网格作为 DCE 5.0 产品的体系一员，无缝对接[容器管理](../../kpanda/intro/what.md)平台，可以为用户提供开箱即用的上手体验，
并作为基础设施为[微服务引擎](../../skoala/intro/what.md)提供容器微服务治理支持，方便用户通过单一平台对各类微服务系统做统一管理。

服务网格的学习路径如下：

```mermaid
flowchart TD

    install([安装部署])
    install --> mesh[创建网格]
        subgraph mesh[创建网格]
            managed[托管网格]
            private[专有网格]
            external[外接网格]
            
        end

    mesh --> cluster[纳管集群]

    cluster --> inject[注入边车]

        subgraph inject[注入边车]
            global[全局注入]
            namespace[命名空间注入]
            workload[工作负载注入]
        end

    
    inject -.-> service[服务管理]
    inject -.-> traffic[流量治理]
    inject -.-> security[安全治理]
    inject -.-> sidecar[边车管理]
    inject -.-> watch[流量监控]
    inject -.-> gateway[网格网关]
    inject -.-> upgrade[版本升级]
    

    service -.-> entry[服务条目]
    traffic -.-> virtual[虚拟服务<br>目标规则<br>网关规则]
    security -.-> peer[对等身份认证<br>请求身份认证<br>授权策略]
    sidecar -.-> sidecarm[命名空间边车管理<br>工作负载边车管理<br>全局边车管理<br>边车流量透传]
    watch -.-> watch2[流量监控<br>流量拓扑]

    classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

    class managed,private,external,global,namespace,workload plain
    class install,service,gateway,traffic,watch,upgrade,security,entry,virtual,peer,cluster,sidecar,sidecarm,watch2 cluster

    click install "https://docs.daocloud.io/mspider/install/"
    click managed "https://docs.daocloud.io/mspider/user-guide/servicemesh/create-mesh/"
    click private "https://docs.daocloud.io/mspider/user-guide/servicemesh/create-mesh/"
    click external "https://docs.daocloud.io/mspider/user-guide/servicemesh/integrate-mesh/"
    click cluster "https://docs.daocloud.io/mspider/user-guide/08ClusterManagement/join-clus/"
    click global "https://docs.daocloud.io/mspider/user-guide/07SidecarManagement/GlobalSidecar/"
    click namespace "https://docs.daocloud.io/mspider/user-guide/07SidecarManagement/NamespaceSidecar/"
    click workload "https://docs.daocloud.io/mspider/user-guide/07SidecarManagement/WorkloadSidecar/"
    click gateway "https://docs.daocloud.io/mspider/user-guide/09GatewayInstance/create/"
    click service "https://docs.daocloud.io/mspider/user-guide/servicelist/"
    click traffic "https://docs.daocloud.io/mspider/user-guide/traffic-governance/"
    click security "https://docs.daocloud.io/mspider/user-guide/05Security/"
    click watch "https://docs.daocloud.io/mspider/user-guide/06TrafficMonitor/"
    click upgrade "https://docs.daocloud.io/mspider/user-guide/upgrade/IstioUpdate/"
    click entry "https://docs.daocloud.io/mspider/user-guide/servicelist/service-entry/"
    click virtual "https://docs.daocloud.io/mspider/user-guide/traffic-governance/VirtualService/"
    click peer "https://docs.daocloud.io/mspider/user-guide/05Security/peer/"
    click sidecar "https://docs.daocloud.io/mspider/user-guide/07SidecarManagement/NamespaceSidecar/"
    click sidecarm "https://docs.daocloud.io/mspider/user-guide/07SidecarManagement/passthrough/"
    click watch2 "https://docs.daocloud.io/mspider/user-guide/06TrafficMonitor/connTopo/"
```

[下载 DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
[申请社区免费体验](../../dce/license0.md){ .md-button .md-button--primary }