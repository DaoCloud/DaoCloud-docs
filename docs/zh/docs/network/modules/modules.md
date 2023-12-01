---
hide:
  - toc
---

# 网络组件

DCE 5.0 提供的网络方案对当前主流的开源网络组件进行优化组合，能够满足各种复杂场景的需求。

![网络组件](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/components.png)

目前，DCE 5.0 已支持的网络组件包括：

- [Calico](../modules/calico/index.md)：基于 Linux kernel 技术实现的 Virtual Router，完成数据平面的转发。
- [Cilium](../modules/cilium/index.md)：基于 eBPF 内核构建的网络方案
- [Contour](../modules/contour/index.md)：一个开源的 Kubernetes Ingress 控制器，使用 Envoy 作为数据面。
- [f5networks](../modules/f5networks/index.md)：全面控制 F5 设备，将集群中 service 和 ingress 配置同步到 F5 硬件设备上，实现集群北向入口的负载均衡。
- [Ingress-nginx](../modules/ingress-nginx/index.md)：Kubernetes 社区托管的 Ingress 控制器，使用 nginx 作为反向代理和负载均衡。
- [MetalLB](../modules/metallb/index.md)：裸金属版的 Kubernetes 负载均衡器方案。
- [Multus-underlay](../modules/multus-underlay/index.md)：基于 Multus、搭配 Macvlan + SRIOV-CNI 的多网卡方案。
- [Spiderpool](../modules/spiderpool/index.md)：自动化管理 IP 资源
- [Submariner](../modules/submariner/index.md)：跨集群的网络通讯方案
- [Aliyun CNI](../modules/aliyun-terway/index.md)：运行在阿里云上的 CNI 插件，提供稳定、高性能，支持Kubernetes network policy、流控等高级特性。

!!! note

    以上所有 CNI 和 Ingress 等组件可以按需安装。
