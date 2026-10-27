# Product Manifest manifest-cloud-tokfact.yaml

This YAML file contains information about all product modules of d.run Token Factory,
which are mainly divided into infrastructure modules and product feature modules.

For upgrade operations, refer to [the upgrade documentation](../upgrade.md).

## Manifest Example

The following is a structural example of `manifest-cloud-tokfact.yaml`.
Fields and versions are subject to the file in the extracted offline package.

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

## Key Fields

The key fields in this YAML file are described in the table below,
which covers the components involved in the infrastructure and the product feature modules.

| Fields | Description |
| :----- | :---------- |
| global.installMode | Product form, always `cloud` |
| infrastructures | Product infrastructure, including HwameiStor, Istio, MetalLB, MySQL, Redis, and others. See the offline package for details. |
| components | Product feature modules |
| components.ghippo | Global management |
| components.kpanda | Container management |
| components.insight | Observability |
| components.insight-agent | Data collection component for observability |
| components.mspider | Service mesh |
| components.leopard | Wallet |
| components.crane | Cockpit, enabled by default |
| components.zestu | Compute market |
| components.baize | AI Lab |
| components.hydra | LLM Studio, enabled by default |
| variables.global.tokenfactory.enable | Enables the Token Factory capability. Always `true` |
