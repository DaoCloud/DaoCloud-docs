---
hide:
  - toc
---

# 外部应用对网格内服务访问

本页说明外部应用如何通过配置来访问网格内的服务。

**前置条件：**

- 服务 `bookinfo.com` 运行于网格 `global-service` 的 `default` 命名空间下

- 网格提供 `ingressgateway` 网关实例

**配置目标：** 实现内部服务 `bookinfo.com` 对外暴露。

1. 通过 URI 匹配方式，实现外部应用对服务 `bookinfo.com` 的指定页面访问路由。

    ![访问路由](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/out-to-in01.png)

2. 点击`流量治理` -> `网关规则` -> `创建`为 istio 网关创建网关规则，对外暴露服务及端口。

    ![创建规则](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/out-to-in02.png)

    完成配置后的 YAML 示例如下：

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: bookinfo-gateway
    spec:
      selector:
        istio: ingressgateway # 使用默认控制器
      servers:
      - port:
          number: 80
          name: http
          protocol: HTTP
        hosts:
        - bookinfo.com
    ```

3. 点击`确定`回到网关规则列表，可见创建成功提示。

4. 点击`流量治理` ->`虚拟服务` -> `创建`来创建路由规则，基于请求中的 URI 路由到指定页面。

    ![创建路由规则](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/out-to-in04.png)

    完成配置后的 YAML 示例如下：

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      name: bookinfo
    spec:
      hosts:
      - bookinfo.com
      gateways:
      - bookinfo-gateway
      http:
      - match:
          - uri:
              exact: /productpage
          - uri:
              exact: /login
          - uri:
              exact: /logout
          - uri:
              prefix: /api/v1/products
        route:
        - destination:
            host: productpage
            port:
              number: 9080
    ```

5. 点击`确定`回到虚拟服务列表，可以看到创建成功的提示。

!!! info

    更直观的操作演示，可参阅[视频教程](../../../videos/mspider.md)。
