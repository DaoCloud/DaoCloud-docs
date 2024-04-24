# 产品清单文件 manifest.yaml

此 YAML 文件包含了 DCE 5.0 所有模块信息，主要分为基础设施模块、产品功能模块。

升级操作请参考文档 [升级 DCE 5.0](../upgrade.md)。

## Manifest 示例

以下是一个 Manifest 文件示例。

```yaml title="manifest.yaml"
apiVersion: manifest.daocloud.io/v1alpha1
kind: DCEManifest
metadata:
global:
  helmRepo: https://release.daocloud.io/chartrepo
  imageRepo: release.daocloud.io
infrastructures:
  hwameiStor:
    enable: true
    version: v0.10.4
    policy: drbd-disabled
  istio:
    version: 1.16.1
  metallb:
    version: 0.13.9
  contour:
    version: 10.2.2
    enable: false
  cert-manager:
    version: 1.11.0
    enable: false
  mysql:
    version: 8.0.29
    cpuLimit: 1
    memLimit: 1Gi
    enableAutoBackup: true
  redis:
    version: 6.2.6-debian-10-r120
    cpuLimit: 400m
    memLimit: 500Mi
components:
  kubean:
    enable: true
    helmVersion: v0.6.6
    helmRepo: https://kubean-io.github.io/kubean-helm-chart
    variables:
  ghippo:
    enable: true
    helmVersion: 0.18.0
    variables:
  kpanda:
    enable: true
    helmVersion: 0.19.0+rc4
    variables:
  kcoral:
    enable: true
    helmVersion: 0.4.0+rc1
    variables:
  kcollie:
    enable: true
    helmVersion: 0.4.0+rc7
    variables:
  insight:
    enable: true
    helmVersion: 0.18.0-rc5
    variables:
  insight-agent:
    enable: true
    helmVersion: 0.18.0-rc5
    features: tracing
  ipavo:
    enable: true
    helmVersion: 0.10.0
    variables:
  kairship:
    enable: true
    helmVersion: 0.10.1
    variables:
  amamba:
    enable: true
    helmVersion: 0.18.0+alpha.3
    features: argocd
  jenkins:
    enable: true
    helmVersion: 0.1.12
    helmRepo: https://release.daocloud.io/chartrepo/amamba
  skoala:
    enable: true
    helmVersion: 0.23.0
    variables:
  mspider:
    enable: true
    helmVersion: v0.17.0-rc2
    variables:
  mcamel-rabbitmq:
    enable: true
    helmVersion: 0.12.0-rc2
    variables:
  mcamel-elasticsearch:
    enable: true
    helmVersion: 0.9.0-rc2
    variables:
  mcamel-mysql:
    enable: true
    helmVersion: 0.10.0-rc2
    variables:
  mcamel-redis:
    enable: true
    helmVersion: 0.9.0-rc2
    variables:
  mcamel-kafka:
    enable: true
    helmVersion: 0.7.0-rc2
    variables:
  mcamel-minio:
    enable: true
    helmVersion: 0.7.0-rc2
    variables:
  mcamel-postgresql:
    enable: true
    helmVersion: 0.3.0-rc2
    variables:
  mcamel-mongodb:
    enable: true
    helmVersion: 0.1.0-rc1
    variables:
  spidernet:
    enable: true
    helmVersion: 0.8.0
    variables:
  kangaroo:
    enable: true
    helmVersion: 0.9.0
    variables:
  gmagpie:
    enable: true
    helmVersion: 0.3.0
    variables:
  dowl:
    enable: true
    helmVersion: 0.3.0+rc1
```

## 关键字段

该 YAML 文件中的关键字段说明，请参阅下表。其中包含了基础设施所涉及的组件以及产品功能模块涉及的产品。

| 字段                            | 说明                              |
| :------------------------------ | :-------------------------------- |
| infrastructures                 | DCE 5.0 产品基础设施               |
| infrastructures.xxx.enable      | 是否开启当前模块，默认为 true     |
| infrastructures.xxx.helmVersion | 当前模块的 chart 包版本           |
| infrastructures.hwameiStor      | HwameiStor 本地存储               |
| infrastructures.istio           | Istio 服务网格                    |
| infrastructures.metallb         | MetalLB 负载均衡器                |
| infrastructures.contour         | Contour 入口控制器                |
| infrastructures.cert-manager    | Cert Manager 证书管理             |
| infrastructures.mysql           | Mysql 数据库                      |
| infrastructures.redis           | Redis 数据库                      |
| components                      | DCE 5.0 产品功能模块               |
| components.kubean               | 集群声明周期管理                  |
| components.ghippo               | 全局管理                          |
| components.kpanda               | 容器管理                          |
| components.kcoral               | 应用备份                 |
| components.kcollie              | 集群巡检                 |
| components.insight              | 可观测性                          |
| components.insight-agent        | 可观测性的数据采集组件            |
| components.ipavo                | 仪表盘                            |
| components.kairship             | 多云编排                          |
| components.amamba               | 应用工作台                        |
| components.jenkins              | 应用工作台的流水线引擎组件        |
| components.skoala               | 微服务引擎                        |
| components.mspider              | 服务网格                          |
| components.mcamel-*             | 中间件，包含了ES、Kafka、MinIO 等 |
| components.kangaroo             | 镜像仓库                          |
| components.gmagpie              | 报表                              |
| components.dowl                 | 集群安全                          |
