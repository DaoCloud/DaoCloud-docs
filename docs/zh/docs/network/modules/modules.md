---
hide:

- toc

---

# 网络组件

DCE 5.0 提供的网络方案对当前主流的开源网络组件进行优化组合，能够满足各种复杂场景的需求。

![网络组件](../images/components.png)

目前，DCE 5.0 已支持的网络组件包括：

- [Calico](../modules/calico/what.md)：基于 Linux kernel 技术实现的 Virtual Router，完成数据平面的转发。
- [Cilium](../modules/cilium/what.md)：基于 eBPF 内核构建的网络方案
- [Contour](../modules/contour/what.md)：一个开源的 Kubernetes Ingress 控制器，使用 Envoy 作为数据面。
- [f5networks](../modules/f5networks/what.md)：全面控制 F5 设备，将集群中 service 和 ingress 配置同步到 F5 硬件设备上，实现集群北向入口的负载均衡。
- [Ingress-nginx](../modules/metallb/what.md)：Kubernetes 社区托管的 Ingress 控制器，使用 nginx 作为反向代理和负载均衡。
- [MetalLB](../modules/metallb/what.md)：裸金属版的 Kubernetes 负载均衡器方案。
- [Multus-underlay](../modules/multus-underlay/what.md)：基于 Multus、搭配 Macvlan + SRIOV-CNI 的多网卡方案。
- [Spiderpool](../modules/spiderpool/what.md)：自动化管理 IP 资源
- [falco](../modules/falco/what.md)：是云原生运行时安全工具，旨在检测应用程序中的异常活动。
- [falco](../modules/falco-exporter/what.md)：是一个用于 Falco 输出事件的Prometheus Metrics导出器。
- 
  > 以上所有 CNI 和 Ingress 等组件可以按需安装。
