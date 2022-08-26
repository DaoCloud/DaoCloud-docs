# 组件版本

DaoCloud 微服务引擎集成了多款组件。各个组件必须满足一定的版本要求才能确保微服务引擎高效运行。具体的组件版本要求如下：

> 稳定支持版本： 经过 Skoala 团队验证的可稳定支持的组件版本，请尽可能使用这些版本。

## DaoCloud 微服务引擎

| 组件类型 | 开源组件                                                     | 稳定支持版本                                                 | 备注                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 必备     | [Nacos](https://github.com/alibaba/nacos)                    | [2.1.0](https://github.com/alibaba/nacos/releases/tag/2.1.0) |                                                              |
| 必备     | [Sentinel](https://github.com/alibaba/Sentinel)              | [v1.8.4](https://github.com/alibaba/Sentinel/releases/tag/1.8.4) |                                                              |
| 必备     | [contour](https://github.com/bitnami/bitnami-docker-contour) | [1.21.1-debian-11-r0](https://github.com/bitnami/bitnami-docker-contour/releases/tag/1.21.1-debian-11-r0) | [Helm contour Chart](https://artifacthub.io/packages/helm/bitnami/contour/8.0.1) |
| 必备     | [envoy](https://github.com/bitnami/bitnami-docker-envoy)     | [1.22.2-debian-11-r1](https://github.com/bitnami/bitnami-docker-envoy/releases/tag/1.22.2-debian-11-r1) |                                                              |
| 必备     | [nginx](https://github.com/bitnami/bitnami-docker-nginx)     | [1.21.6-debian-11-r5](https://github.com/bitnami/bitnami-docker-nginx/releases/tag/1.21.6-debian-11-r5) |                                                              |
| 必备     | [Helm](https://github.com/helm/helm)                         | [v3.8.2](https://github.com/helm/helm/releases/tag/v3.8.2)   |                                                              |
| 必备     | [Grafana](https://github.com/grafana/grafana)                | [v8.4.6](https://github.com/grafana/grafana/releases/tag/v8.4.6) |                                                              |
| 可选     | [Zookeeper](https://github.com/apache/zookeeper)             | [release-3.5.10](https://github.com/apache/zookeeper/releases/tag/release-3.5.10) |                                                              |
| 可选     | [Eureka](https://github.com/Netflix/eureka)                  | [v1.10.17](https://github.com/Netflix/eureka/releases/tag/v1.10.17) |                                                              |
| 可选     | [Istio](https://github.com/istio/istio)                      | [1.14.1](https://github.com/istio/istio/releases/tag/1.14.1) |                                                              |
| 可选     | [Kubernetes](https://github.com/kubernetes/kubernetes)       | 1.23, 1.22, 1.21                                             |                                                              |
| 可选     | [prometheus](https://github.com/prometheus/prometheus)       | [v2.36.0](https://github.com/prometheus/prometheus/releases/tag/v2.36.0) |                                                              |

