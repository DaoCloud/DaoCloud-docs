---
hide:
  - toc
---

# 创建托管网格

DCE 5.0 服务网格支持 3 种网格：

- [托管网格](./hosted-mesh.md)完全托管在 DCE 5.0 服务网格内。这种网格将核心控制面组件从工作集群中分离，控制面可以部署到一个独立的集群中，能够对同一网格中的多集群服务进行统一治理。
- [专有网格](./dedicated-mesh.md)采用 Istio 传统结构，仅支持一个集群，集群内设有专门的控制面。
- [外接网格](./external-mesh.md)指的是可以将企业现成的网格接入到 DCE 5.0 服务网格中进行统一管理。参见[创建外接网格](external-mesh.md)。

## 常见问题

创建网格时常见的一些问题汇总如下：

- [创建网格时找不到所属集群](../../troubleshoot/cannot-find-cluster.md)
- [创建网格时一直处于“创建中”，最终创建失败](../../troubleshoot/always-in-creating.md)
- [创建的网格异常，但无法删除网格](../../troubleshoot/failed-to-delete.md)
- [托管网格纳管集群失败](../../troubleshoot/failed-to-add-cluster.md)
- [托管网格纳管集群时 istio-ingressgateway 异常](../../troubleshoot/hosted-mesh-errors.md)
- [网格空间无法正常解绑](../../troubleshoot/mesh-space-cannot-unbind.md)
- [托管网格多云互联异常](../../troubleshoot/cluster-interconnect.md)
- [创建网格时，集群列表存在未知集群](../../troubleshoot/cluster-already-exist.md)
- [托管网格 APIServer 证书过期处理办法](../../troubleshoot/hosted-apiserver-cert-expiration.md)
