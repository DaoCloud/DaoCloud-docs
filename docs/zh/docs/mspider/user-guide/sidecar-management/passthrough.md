# 边车流量透传

流量透传 (traffic passthrough) 指的是工作负载的全部或部分上游、下游流量不经边车转发，直接发送至工作负载本身。

DCE 5.0 服务网格实现了对工作负载出站/入站流量的边车透传可控，可针对特定端口、IP 段实现拦截设置。

- 功能设置对象：工作负载
- 设置参数：端口、IP 段
- 流向：入站、出站

流量透传相关字段：

```none
traffic.sidecar.istio.io/excludeInboundPorts
traffic.sidecar.istio.io/excludeOutboundPorts
traffic.sidecar.istio.io/excludeOutboundIPRanges
```

## 启用流量透传

本节说明如何在 DCE 图形界面上启用/禁用流量透传。

1. 进入某个网格，点击 __边车管理__ -> __工作负载边车管理__ 。

    ![工作负载边车管理](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/pn01.png)

1. 点击某个负载右侧的 __⋮__ ，在弹出菜单中选择 __流量透传设置__ 。

    ![点击菜单项](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/pn02.png)

1. 设置流量透传的参数后，勾选 __立即重启工作负载__ ，点击 __确认变更__ 。

    ![流量透传设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/pn03.png)

    - 入站：仅支持端口，即从外部访问网格内负载的端口
    - 出站：可设置目标的端口或 IP 段

1. 如果设置无误，右上角将出现 __流量透传设置成功__ 的提示消息。您还可以[查验流量透传效果](#_3)。

    ![成功设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/pn04.png)

1. 如果流量透传已启用，上述第 3 步的 __流量透传设置__ 弹窗将显示设置的参数，可点击右侧的 x，勾选 __立即重启工作负载__ ，点击 __确认变更__ 来禁用流量透传。

    ![禁用流量透传](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/pn05.png)

## 查验流量透传效果

在真实的网格集群中，查验流量透传前后的效果。

1. 准备工作

    - 准备一个网格集群，例如 10.64.30.130
    - 在命名空间中，配置工作负载 __helloworld__ ，并注入边车
    - 启用流量透传，然后比对该负载的流量路由变化

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/pn06.png)

1. 通过控制台或 ssh 登录到网格。

    ```bash
    ssh root@10.64.30.130
    ```

1. 查看命名空间中的 svc，获取 clusterIP 和 Port：

    ```bash
    $ kubectl get svc -n default
    NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    helloworld   ClusterIP   10.211.201.221   <none>        5000/TCP         39d
    kubernetes   ClusterIP   10.211.0.1       <none>        443/TCP          62d
    test-cv      NodePort    10.211.72.8      <none>        2222:30186/TCP   62d
    ```

1. 执行 curl 命令查看 helloworld 的流量路由：

    === "启用流量透传前"

        ```bash
        curl -sSI 10.211.201.221:5000/hello
        ```
        ```none
        HTTP/1.1 200 OK
        content-type: text/html; charset=utf-8
        content-length: 65
        server: istio-envoy # (1)!
        date: Tue, 07 Feb 2023 03:08:33 GMT
        x-envoy-upstream-service-time: 100
        x-envoy-decorator-operation: helloworld.default.svc.cluster.local:5000/*
        ```

        1. 流量经过 istio-envoy，即边车的代理

    === "启用流量透传后"

        ```bash
        curl -sSI 10.211.201.221:5000/hello
        ```
        ```none
        HTTP/1.0 200 OK
        Content-Type: text/html; charset=utf-8
        Content-Length: 65
        Server: Werkzeug/0.12.2 Python/2.7.13 # (1)
        Date: Tue, 07 Feb 2023 03:08:10 GMT
        ```

        1. 流量直接进入工作负载本身
