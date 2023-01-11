# 边车流量透传

功能目标：实现对工作负载出站/入站流量的边车透传可控，可针对特定端口、IP实现拦截设置。

功能设置对象：工作负载

设置参数：端口、IP

流向：入站、出站

Istio字段：

traffic.sidecar.istio.io/excludeOutboundPorts

traffic.sidecar.istio.io/excludeOutboundIPRanges



**操作流程**