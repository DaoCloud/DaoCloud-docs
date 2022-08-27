# 什么是 DaoCloud 服务网格

DaoCloud 服务网格是基于 Istio 开源技术构建的面向云原生应用的下一代服务网格。

DaoCloud 服务网格是一种具备高性能、高易用性的全托管服务网格产品，通过提供完整的非侵入式的微服务治理解决方案，能够很好的支持多云多集群复杂环境的统一治理，以基础设施的方式为用户提供服务流量治理、安全性治理、服务流量监控、以及对传统微服务（SpringCloud、Dubbo）接入支持。并兼容社区原生 Istio 开源服务网格，提供原生Istio接入管理能力。较高的层次上，服务网格有助于降低服务治理的复杂性，并减轻开发运维团队的压力。

DaoCloud 服务网格作为 DCE 5.0 产品的体系一员，无缝对接容器管理平台，可以为用户提供开箱即用的上手体验，并作为基础设施为微服务引擎提供容器微服务治理支持，方便用户通过单一平台对各类微服务系统做统一管理。

## 部署方法

参考 `make deploy` 命令，使用内部的构建可以按照以下方式部署。

```console
export VERSION=0.0.0-xxxxx # xxxxx means the commit sha of main branch, you can get with `git rev-parse --short HEAD`
helm repo add mspider-ci https://release.daocloud.io/chartrepo/mspider-ci
helm repo update
helm upgrade --install --create-namespace -n mspider-system mspider mspider-ci/mspider --version=${VERSION} --set global.hub=release.daocloud.io/mspider-ci --set global.debug=true
```
