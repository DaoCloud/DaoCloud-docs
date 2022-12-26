---
hide:
  - toc
---

# Environmental requirements

Various components are integrated in the microservice engine. Each component must reach a specific version to ensure the efficient operation of the microservice engine. The specific component version requirements are as follows:

!!! note

    Stable support version: The component version that the microservice engine team believes can be stably supported after verification. It is recommended to refer to the following table to use a specific version of the component.

| Component Type | Open Source Component | Stable Support Version | Remarks |
| -------- | ----------------------------------------- -------------------- | ----------------------------- ------------------------------- | ------------------ --------------------------------------------- |
| Required | [Nacos](https://github.com/alibaba/nacos) | [2.1.0](https://github.com/alibaba/nacos/releases/tag/2.1.0) | |
| Required | [Sentinel](https://github.com/alibaba/Sentinel) | [v1.8.4](https://github.com/alibaba/Sentinel/releases/tag/1.8.4) | |
| Required | [contour](https://github.com/bitnami/bitnami-docker-contour) | [1.21.1-debian-11-r0](https://github.com/bitnami/bitnami-docker -contour/releases/tag/1.21.1-debian-11-r0) | [Helm contour Chart](https://artifacthub.io/packages/helm/bitnami/contour/8.0.1) |
| Required | [envoy](https://github.com/bitnami/bitnami-docker-envoy) | [1.22.2-debian-11-r1](https://github.com/bitnami/bitnami-docker -envoy/releases/tag/1.22.2-debian-11-r1) | |
| Required | [nginx](https://github.com/bitnami/bitnami-docker-nginx) | [1.21.6-debian-11-r5](https://github.com/bitnami/bitnami-docker -nginx/releases/tag/1.21.6-debian-11-r5) | |
| Required | [Helm](https://github.com/helm/helm) | [v3.8.2](https://github.com/helm/helm/releases/tag/v3.8.2) | |
| Required | [Grafana](https://github.com/grafana/grafana) | [v8.4.6](https://github.com/grafana/grafana/releases/tag/v8.4.6) | |
| Optional | [Zookeeper](https://github.com/apache/zookeeper) | [release-3.5.10](https://github.com/apache/zookeeper/releases/tag/release-3.5.10 ) | |
| Optional | [Eureka](https://github.com/Netflix/eureka) | [v1.10.17](https://github.com/Netflix/eureka/releases/tag/v1.10.17) | |
| Optional | [Istio](https://github.com/istio/istio) | [1.14.1](https://github.com/istio/istio/releases/tag/1.14.1) | |
| Optional | [Kubernetes](https://github.com/kubernetes/kubernetes) | 1.23, 1.22, 1.21 | |
| Optional | [prometheus](https://github.com/prometheus/prometheus) | [v2.36.0](https://github.com/prometheus/prometheus/releases/tag/v2.36.0) | |