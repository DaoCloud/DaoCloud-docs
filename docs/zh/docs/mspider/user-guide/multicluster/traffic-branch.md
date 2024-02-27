# 网格下多云网络流量分流配置

本文讲述如何在多云网络中为工作负载配置不同的流量。

前置条件：

- 服务 __helloworld__ 运行于网格 __hosted-mesh__ 的命名空间 __helloworld__ 下
- 开启多云网络互联
- 网格提供 ingressgatway 网关实例

配置步骤：

1.  基于所属集群，对请求流量做权重分流；

    ![流程](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch01.png)

1. 为两个集群的 __helloworld__ 工作负载分别添加标签：

    | 所属集群     | 标签    | 值  |
    | ------------ | ------- | --- |
    | yl-cluster10 | version | v1  |
    | yl-cluster20 | version | v2  |

    ![添加标签](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch02.png)

1. 在左侧导航栏点击 __边车管理__ -> __工作负载边车管理__ ，为两个集群的 helloworld 工作负载注入边车。

    ![集群01](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch03.png)

    ![集群02](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch04.png)

1. 在左侧导航栏点击 __流量治理__ -> __目标规则__ -> __创建__ ，创建两个服务版本。

    ![服务版本](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch05.png)

    对应的 YAML 如下：

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: DestinationRule
    metadata:
      name: helloworld-version
      namespace: helloworld
    spec:
      host: helloworld
      subsets:
        - labels:
    ​      version: v1
    ​      name: v1
        - labels:
    ​      version: v2
          name: v2
    ```

1. 在左侧导航栏点击 __流量治理__ -> __网关规则__ -> __创建__ ，创建网关规则。

    ![网关规则](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch06.png)

    对应的 YAML 如下：

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: helloworld-gateway
      namespace: helloworld
    spec:
      selector:
        istio: ingressgateway
      servers:
        - hosts:
    ​      - hello.m.daocloud
          port:
    ​        name: http
    ​        number: 80
    ​        protocol: http
    ```

1. 在左侧导航栏点击 __流量治理__ -> __虚拟服务__ -> __创建__ ，创建路由规则，基于权重比例把流量分流至两个集群：

    ![虚拟服务](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch07.png)

    对应的 YAML 如下：

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      name: helloworld-version
      namespace: helloworld
    spec:
      gateways:
        - helloworld-gateway
      hosts:
        - helloworld.helloworld.svc.cluster.local
      http:
        - match:
          - uri:
            exact: /hello
          name: helloworld-routes
          route:
            - destination:
              host: helloworld
              port:
                number: 5000
              subset: v1
              weight: 30
            - destination:
              host: helloworld
              port:
                number: 5000
                subset: v2
              weight: 70
    ```

1. 在左侧导航栏点击 __网格配置__ -> __多云网络互联__ ，开启多云网络互联。

    ![多云网络互联](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch08.png)

1. 通过 JMeter 发起 1000 次 get 请求，设置断言

    ![JMeter01](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch09.png)

    ![JMeter02](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch10.png)

1. 查看请求聚合报告（设置断言 helloworld v2），成功率 70%，异常率比例接近 30%。

    ![报告](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/branch11.png)
