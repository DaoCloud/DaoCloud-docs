---
hide:
  - toc
---

# 接入注册中心

注册中心支持接入 [Nacos 注册中心](../../reference/registry.md)、[Eureka 注册中心](../../reference/registry.md)、[Zookeeper 注册中心](../../reference/registry.md)、Consul 注册中心、[Kubernetes 注册中心](../../reference/registry.md)、[Mesh 注册中心](../../reference/registry.md)。

相对于托管型注册中心而言，接入型注册中心只支持一些基础操作，例如查看基本信息、监控信息等。如需体验更高级更全面的管理操作，需要创建[托管注册中心](../hosted/create-registry.md)。

接入注册中心的步骤如下：

1. 在左侧导航栏点击`传统微服务`-->`接入注册中心`，然后在页面右上角点击`接入注册中心`。

    ![进入接入注册中心页面](../../images/integrate01.png)

2. 填写配置信息，然后在页面底部点击`确定`。

    接入不同类型的注册中心需要填写不同的配置信息。

    - Kubernetes/Mesh 注册中心：直接选择想要接入的集群或网格服务。

        - 如果找不到想要添加的 Kubernetes 集群，可以去容器管理模块[接入集群](../../../kpanda/user-guide/clusters/integrate-cluster.md)或[创建集群](../../../kpanda/user-guide/clusters/create-cluster.md)。

        - 如果找不到想要添加的网格服务，可以去网格服务模块[创建网格](../../../mspider/user-guide/service-mesh/README.md)。

            ![接入 Mesh/Kubernetes](../../images/integrate02.png)

    - Nacos/Zookeeper/Eureka/Consul 注册中心：填写注册中心的名称和地址，点击`确认`。

        ![接入 Nacos/Zookeeper/Eureka](../../images/integrate03.png)
