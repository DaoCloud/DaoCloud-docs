---
MTPE: windsonsea
date: 2024-06-28
---

# manifest.yaml

This YAML file contains information about all modules of DCE 5.0, which are mainly divided into the base configuration module and product feature modules.

For upgrading instructions, refer to [Upgrade DCE 5.0](../upgrade.md).

## Manifest Example

Here is an example of a manifest file.

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
    helmVersion: v0.18.0-rc2
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

## Key Fields

Please refer to the table below for an explanation of the key fields in this YAML file.
It includes components related to the infrastructure and products involved in the functionality modules of the product.

| Fields                          | Description                                         |
| :------------------------------ | :-------------------------------------------------- |
| infrastructures                 | DCE 5.0 product infrastructure modules              |
| infrastructures.xxx.enable      | Whether to enable the current module, default: true |
| infrastructures.xxx.helmVersion | The chart package version for the current module    |
| infrastructures.hwameiStor      | HwameiStor local storage                            |
| infrastructures.istio           | Istio service mesh                                  |
| infrastructures.metallb         | MetalLB load balancer                               |
| infrastructures.contour         | Contour ingress controller                          |
| infrastructures.cert-manager    | Cert Manager certificate management                 |
| infrastructures.mysql           | Mysql database                                      |
| infrastructures.redis           | Redis database                                      |
| components                      | DCE 5.0 product feature                             |
| components.kubean               | Cluster lifecycle management                        |
| components.ghippo               | Global management                                   |
| components.kpanda               | Container management                                |
| components.kcoral               | Application backup                                  |
| components.kcollie              | Cluster inspection                                  |
| components.insight              | Observability                                       |
| components.insight-agent        | Data collection component for observability         |
| components.ipavo                | Dashboard                                           |
| components.kairship             | MultiCloud Management                               |
| components.amamba               | Workbench                                           |
| components.jenkins              | Pipeline engine component for Workbench             |
| components.skoala               | Microservice engine                                 |
| components.mspider              | Service mesh                                        |
| components.mcamel-\*            | Middleware including ES, Kafka, MinIO, etc.         |
| components.kangaroo             | Container registry                                  |
| components.gmagpie              | Billing and reporting                               |
| components.dowl                 | Cluster security                                    |
| components.kant                 | Cloud Edge Collaboration                            |
| components.virtnest             | Virtual Machine                                     |
| components.kolm                 | OLM management                                      |
| components.baize                | Intelligent Engine                                  |
