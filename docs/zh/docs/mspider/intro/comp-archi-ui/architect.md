---
hide:
  - toc
---

# 系统架构

DCE 5.0 服务网格产品支持多种类型的网格实例管理能力，支持托管多集群网格进行云原生微服务治理能力；用户可将不同来源的集群接入托管网格中，进行统一的流量治理和安全治理等。

从整体架构上讲，服务网格产品可分为三个面：网格全局管理面、网格控制面、网格数据面

![系统架构](../../images/architecture1.svg)

- 网格全局管理面

    运行于独立的控制面集群 Global Service Cluster（以下简称 GSC），⽤于对多个服务⽹格实例进⾏统⼀管理，提供友好的管理与控制能力。
    网格全局管理面提供了提供了友好的界面化操作和 YAML 原生资源编辑能力，统一的网格实例生命周期管理、权限隔离等。
    同时，也负责与 DCE 5.0 其它模块的对接的工作，以将减少其它模块的适配成本。
    注意，网格全局管理面仅管理网格实例本身，不参与具体的服务治理事务，因此并不包含 Istio 相关组件。

- 网格控制面

    运行于 Mesh Control Plane Cluster（以下简称 MCPC），网格控制面本质上也是工作在用户的工作集群，同时具备网格控制面的角色。
    Istio 等核心控制组件会安装在该集群，作为网格的核心控制平面，直接对本网格内的网格资源进行管理，进行统一的服务发现和治理策略维护，实际执行、下发各项流量策略和安全策略。
    托管网格实例，支持纳管多工作集群，实现多集群的流量治理和安全治理等。专用网格实例，支持单集群的流量治理和安全治理等。

- 网格数据面

    实际业务应用服务和治理策略生效的工作集群，包含了 Istio 的基本组件，但不会作为控制面使用，仅是提供一个类似管理代理的模式，
    主要负责边车注入、证书转发、xDS 转发等业务，同步来自 MCPC 的策略、服务注册信息下发至集群内的所在业务 Sidecar。
    当网格类型为托管网格时，网格控制面和数据面一般情况是指不同的 Kubernetes 集群，如果您需要对当前集群纳管且不需要同时管理多集群服务时，建议使用专用网格。

贯穿整体架构的拓展模块主要有：可观测模块、微服务治理模块、应用工作台

- 可观测模块

    服务网格的可观测能力，借助 DCE 5.0 可观测性模块处理，服务网格通过接口调用的方式获取流量指标信息绘制拓扑图，并为用户提供各种维度的微服务监控图表。

- 微服务治理模块

    微服务治理模块结合服务网格底座，完成对统一微服务治理的产品建设，赋能其云原生微服务治理和场景化微服务治理能力，方便用户对微服务做统一治理。

- 应用工作台

    应用工作台是 DCE 5.0 的核心模块，用于提供给用户统一的应用编排、部署、流水线管理、CICD、应用监控、日志查询等能力。

## 功能架构

```mermaid
graph LR

    mesh([服务网格]) -.- overview[网格概览]
    mesh -.- service[服务管理]
    mesh -.- traffic[流量治理]
        traffic -.- vs[虚拟服务]
        traffic -.- dr[目标规则]
        traffic -.- gw[网关规则]
    mesh -.- security[安全治理]
        security -.- peer[对等身份认证]
        security -.- request[请求身份认证]
        security -.- authz[认证策略]
    mesh -.- monitor[流量监控]
        monitor -.- tp[服务拓扑]
        monitor -.- list[服务监控列表]
    mesh -.- sidecar[边车管理]
        sidecar -.- ns[命名空间边车管理]
        sidecar -.- workload[工作负载边车管理]
    mesh -.- cluster[集群纳管]
    mesh -.- meshgw[网格网关]
    mesh -.- config[网格配置] -.- istio[Istio 资源管理]

click vs "https://docs.daocloud.io/mspider/user-guide/traffic-governance/virtual-service/"
click dr "https://docs.daocloud.io/mspider/user-guide/traffic-governance/destination-rules/"
click gw "https://docs.daocloud.io/mspider/user-guide/traffic-governance/gateway-rules/"
click peer "https://docs.daocloud.io/mspider/user-guide/security/peer/"
click request "https://docs.daocloud.io/mspider/user-guide/security/request/"
click authz "https://docs.daocloud.io/mspider/user-guide/security/authorize/"
click tp "https://docs.daocloud.io/mspider/user-guide/traffic-monitor/conn-topo/"
click list "https://docs.daocloud.io/mspider/user-guide/traffic-monitor/monitoring-indicators/"
click ns "https://docs.daocloud.io/mspider/user-guide/sidecar-management/ns-sidecar/"
click workload "https://docs.daocloud.io/mspider/user-guide/sidecar-management/workload-sidecar/"
click istio "https://docs.daocloud.io/mspider/user-guide/mesh-config/istio-resources/"

 classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
 classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
 classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

 class vs,dr,gw,peer,request,authz,tp,list,ns,workload,global,istio cluster;
```

如上图所示，服务网格提供了 9 个模块 12 个子模块功能，实现了多样化集群接入、多种模式的网格管理的能力。
