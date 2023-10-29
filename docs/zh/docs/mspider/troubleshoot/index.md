# 创建网格故障排查

本文将持续统计和梳理创建网格过程可能因环境或操作不规范引起的报错，以及服务网格使用过程中遇到某些报错的问题分析、解决方案。
若遇到服务网格的使用问题，请优先查看此排障手册。

- 托管模式：控制面和数据面分开，创建一个虚拟集群用来保存托管的 Istio CRD 资源

    创建托管网格时，会在托管控制面集群创建托管控制面虚拟集群 API Server 用来保存 Istio CRD 资源；
    原则上一套 DCE 5.0 环境仅允许有一个托管网格。
    DCE 5.0 的 global 集群含有全局管理所依赖的 Istio 相关组件，
    不允许使用该集群创建托管模式网格，demo 时可以使用外接网格创建。

- 专有模式：控制面和数据面部署在一个集群
- 外接模式：所属集群必须含有 istio 相关组件

## 常见故障案例

- [创建网格时找不到所属集群](./cannot-find-cluster.md)
- [创建网格时一直处于“创建中”，最终创建失败](./always-in-creating.md)
- [创建的网格异常，但无法删除网格](./failed-to-delete.md)
- [托管网格纳管集群失败](./failed-to-add-cluster.md)
- [托管网格纳管集群时 istio-ingressgateway 异常](./hosted-mesh-errors.md)
- [网格空间无法正常解绑](./mesh-space-cannot-unbind.md)
- [DCE 4.0 接入问题追踪](./dce4.0-issues.md)
- [命名空间边车配置与工作负载边车冲突](./sidecar.md)
