# 多集群灰度发布

多集群灰度发布的实现逻辑是，通过在不同集群部署不同的业务应用，然后通过服务网格配置相应的策略实现业务版本之间流量调整，然后根据运行情况下线版本。

前置准备，参考网格多云部署文档，搭建网格基础设施。

## 创建 demo 应用并且验证流量

### 集群部署 v1 版本 helloworld

首先选择一个命名空间（gray-demo），并且在网格页面开启该命名空间边车注入。

在应用工作台部署应用，在这里我们以 istio 的 helloworld 为例。

![部署应用](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo.png)

选择对应集群（mdemo-cluster2）与命名空间，并且配置工作负载基本信息。

![配置工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo1.png)

- 选择镜像：docker.m.daocloud.io/istio/examples-helloworld-v1
- 版本：latest

配置服务信息：

- 访问类型：集群内访问
- 端口配置

    - 协议：TCP
    - 名称：http-5000
    - 容器端口：5000
    - 服务端口：5000

![访问类型](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo2.png)

![端口配置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo4.png)

为了区分不同版本的工作负载，需要在 __容器管理平台__ 找到对应的工作负载，点击 __标签与注解__ ，给容器组标签添加键值对：
"version"："v1"

![标签与注解](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-labels.png)

![添加键值对](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-labels1.png)

### 集群部署 v2 版本 helloworld

> 注意服务命名与命名空间必须相同。

首先选择上面一致命名空间（gray-demo），并且在网格页面开启该命名空间边车注入。

部署流程与上面一样，其主要区别是：

- 镜像发生了变化： `docker.m.daocloud.io/istio/examples-helloworld-v2` 
- 在容器平台给相应 **容器组标签** 加上 label "version"："v2"

## 部署灰度应用策略

### 多集群目标规则

首先创建 DestinationRule，通过定义 SubSet 定义不同集群的业务版本。

其标签键值对为上文中添加的容器组标签： __version: <VERSION>__ 。

策略：必须开启 Istio 双向 TLS

![开启双向 TLS](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/demo-dr.png)

![开启双向 TLS](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/demo-dr1.png)

必须开启 **Istio 双向** TLS 模式

![开启双向 TLS](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/demo-dr2.png)

目标规则 YAML 如下：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: helloworld
  namespace: gray-demo
spec:
  host: helloworld
  subsets:
    - labels:
        version: v1
      name: v1
      trafficPolicy:
        tls:
          mode: ISTIO_MUTUAL
    - labels:
        version: v2
      name: v2
      trafficPolicy:
        tls:
          mode: ISTIO_MUTUAL
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL
```

### 通过 ingress 暴露服务

首先需要创建一条网关规则：

![创建一条网关规则](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-gw-ingress.png)

网关规则 YAML 如下：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: gray-demo-gateway
  namespace: gray-demo
spec:
  selector:
    istio: ingressgateway # (1)!
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - "*"
```

1. use istio default controller

然后配置访问服务所需的虚拟服务规则。

![配置虚拟服务规则](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/gw-vs.png)

![配置虚拟服务规则](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/gw-vs1.png)

虚拟服务 YAML 如下：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: gray-demo-vs
  namespace: gray-demo
spec:
  gateways:
    - gray-demo-gateway
  hosts:
    - "*"
  http:
    - name: http-5000
      route:
        - destination:
            host: helloworld.gray-demo.svc.cluster.local
            port:
              number: 5000
            subset: v1
          weight: 80
        - destination:
            host: helloworld.gray-demo.svc.cluster.local
            port:
              number: 5000
            subset: v2
          weight: 20
```

## 验证

**INGRESS_LB_IP** 是指 Ingress 网格负载均衡地址，可以在容器管理平台中查看，如果没有有效的负载均衡 IP 可以通过 NodePort 方式访问。

![验证](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/check-ingress-lb.png)

（由于容器管理平台界面无法直接查看外部 IP，因此使用控制台的能力查看）

在浏览器中访问： http://${INGRESS_LB_IP}/hello

确认其 v1 与 v2 版本的访问比例是否与上面策略的比例为 8:2

![确认](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/get-hello.png)
