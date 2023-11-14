# 网关对接服务网格

本文介绍如何对接 DCE 5.0 云原生网关和服务网格，使得可以通过网关访问服务网格下接入的服务，
并且可以正常使用网格的所有流量治理能力，例如虚拟服务、目标规则等。

## 现状

目前 DCE 5.0 云原生网关采用 contour 作为控制面，无法同步 Istio 的策略。通过云原生网关访问网格服务时，
网关 API 直接连接到网格服务，由于没有同步 Istio 的策略，所以无法应用虚拟服务、目标服务等规则，导致网格能力缺失。

## 对接思路

让云原生网关通过 Istio 的 Sidecar 访问网格服务，从而应用 Istio 的规则。

## 操作步骤

1. [创建云原生网关](../gateway/index.md)时，开启注入 Sidecar。

    ![创建网关](../images/create-gw01.png)

2. 为 Pod 设置 Annotation 注解 `traffic.sidecar.istio.io/includeInboundPorts: ""`。

    这样可以不让 Istio 处理入口流量，减少性能损耗。

3. 在 Envoy 的启动参数中增加 `--base-id 10`，允许同一个命名空间中存在两个 envoy 实例，防止冲突。

    ![参数示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw-mesh01.png)

4. 在网关下[添加 API](../gateway/api/index.md)时，设置 `Host` 请求头。

    这样可以让网关在多集群场景下，通过 Sidecar 访问其他集群的服务，实现服务的跨集群负载均衡。

    ![参数示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw-mesh02.png)

5. 在服务网格模块为网关 Sidecar 配置资源，不低于云原生网关的默认资源配置 1 核 1 G。

## 效果展示

完成上述配置之后，通过网关域名访问服务。可以看到每次请求的是不同集群中的服务，说明网关可以跨集群访问服务。

![参数示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw-mesh03.png)
