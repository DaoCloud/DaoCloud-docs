---
hide:
  - toc
---

# 更新注册中心配置

微服务引擎目前仅支持更新 Nacos/Zookeeper/Eureka 注册中心的配置。

1. 在`接入注册中心列表`页选择需要更新的注册中心，在右侧点击 `⋯` 并选择`编辑`。

    ![进入更新页面](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/integrated/imgs/update-1.png)

2. 增加或删除注册中心的地址，然后在页面底部点击`确定`。

    ![进入更新页面](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/integrated/imgs/update-2.png)

!!! note

    如需更新 Kubernetes/Mesh 注册中心：

    - 可以先[移除已经接入的注册中心](remove-registry.md)，然后再重新接入其他的注册中心。
    - 也可以去容器管理模块[更新对应的集群](../../../kpanda/user-guide/clusters/upgrade-cluster.md)，或者去服务网格模块[更新对应的网格服务](../../../mspider/user-guide/service-mesh/README.md)。
