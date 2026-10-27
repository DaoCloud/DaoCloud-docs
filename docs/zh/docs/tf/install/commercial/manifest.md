# 产品清单文件 manifest-cloud-tokfact.yaml

此 YAML 文件包含了 Token 工厂的所有产品模块信息，主要分为基础设施模块、产品功能模块。

有关升级操作，请参考[升级文档](../upgrade.md)。

## Manifest 示例

以下为 `manifest-cloud-tokfact.yaml` 的结构示例，字段与版本以解压后离线包内的该文件为准。

```yaml title="manifest-cloud-tokfact.yaml"
apiVersion: manifest.daocloud.io/v1alpha3
kind: DCEManifest
metadata:
  creationTimestamp: null
global:
  helmRepo: https://release.daocloud.io/chartrepo
  imageRepo: release.daocloud.io
  installMode: cloud
infrastructures:
  # ... 详见离线包
middlewares:
  # ... 详见离线包
components:
  ghippo:
    enable: true
  kpanda:
    enable: true
  insight:
    enable: true
  mspider:
    enable: true
  leopard:
    enable: true
  crane:
    enable: true
  zestu:
    enable: true
  baize:
    enable: true
  hydra:
    enable: true
    helmVersion: v0.18.3
    variables:
      global.tokenfactory.enable: true
    dependencies:
      - ghippo
      - kpanda
      - mspider
      - insight
      - leopard
```

## 关键字段

该 YAML 文件中的关键字段说明如下表。其中包含了基础设施所涉及的组件以及产品功能模块涉及的产品。

| 字段 | 说明 |
| :--- | :--- |
| global.installMode | 产品形态，固定为 `cloud` |
| infrastructures | 产品基础设施，包含 HwameiStor、Istio、MetalLB、MySQL、Redis 等，详见离线包 |
| components | 产品功能模块 |
| components.ghippo | 全局管理 |
| components.kpanda | 容器管理 |
| components.insight | 可观测性 |
| components.insight-agent | 可观测性的数据采集组件 |
| components.mspider | 服务网格 |
| components.leopard | 钱包 |
| components.crane | 驾驶舱，默认开启 |
| components.zestu | 算力市场 |
| components.baize | AI Lab |
| components.hydra | 大模型服务平台，默认开启 |
| variables.global.tokenfactory.enable | 启用 Token 工厂能力，固定为 `true` |
