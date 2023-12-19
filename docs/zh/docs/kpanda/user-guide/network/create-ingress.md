# 创建路由（Ingress）

在 Kubernetes 集群中，[Ingress](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#ingress-v1beta1-networking-k8s-io) 公开从集群外部到集群内服务的 HTTP 和 HTTPS 路由。
流量路由由 Ingress 资源上定义的规则控制。下面是一个将所有流量都发送到同一 Service 的简单 Ingress 示例：

![ingress-diagram](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/ingress.svg)

Ingress 是对集群中服务的外部访问进行管理的 API 对象，典型的访问方式是 HTTP。Ingress 可以提供负载均衡、SSL 终结和基于名称的虚拟托管。

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[已创建 Kubernetes](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。
- 已完成一个[命名空间的创建](../namespaces/createns.md)、[用户的创建](../../../ghippo/user-guide/access-control/user.md)，并将用户授权为 [NS Edit](../permissions/permission-brief.md#ns-edit) 角色 ，详情可参考[命名空间授权](../permissions/cluster-ns-auth.md)。
- 已经完成 [Ingress 实例的创建](../../../network/modules/ingress-nginx/install.md)，已[部署应用工作负载](../workloads/create-deployment.md)，并且已[创建对应 Service](create-services.md)
- 单个实例中有多个容器时，请确保容器使用的端口不冲突，否则部署会失效。

## 创建路由

1. 以 __NS Edit__ 用户成功登录后，点击左上角的 __集群列表__ 进入 __集群列表__ 页面。在集群列表中，点击一个集群名称。

    ![集群列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ingress01.png)

2. 在左侧导航栏中，点击 __容器网络__ -> __路由__ 进入服务列表，点击右上角 __创建路由__ 按钮。

    ![服务与路由](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ingress02.png)

    !!! note

        也可以通过 __YAML 创建__ 一个路由。

3. 打开 __创建路由__ 页面，进行配置。可选择两种协议类型，参考以下两个参数表进行配置。

### 创建 HTTP 协议路由

  输入如下参数：
  ![创建路由](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ingress03.png)
  
- __路由名称__ :必填，输入新建路由的名称。
- __命名空间__ ：必填，选择新建服务所在的命名空间。关于命名空间更多信息请参考命名空间概述。
- __设置路由规则__ ：
  - __域名__ ：必填，使用域名对外提供访问服务。默认为集群的域名。
  - __协议__ ：必填，指授权入站到达集群服务的协议，支持 HTTP （不需要身份认证）或 HTTPS（需需要配置身份认证） 协议。这里选择 HTTP 协议的路由。
  - __转发策略__ :选填，指定 Ingress 的访问策略。 __路径__ ：指定服务访问的URL路径，默认为根路径； __目标服务__ ：进行路由的服务名称； __目标服务端口__ ：服务对外暴露的端口。
- __负载均衡器类型__ :必填，[Ingress 实例的使用范围](../../../network/modules/ingress-nginx/scope.md)
  - __平台级负载均衡器__ ：同一个集群内，共享同一个 Ingress 实例，其中 Pod 都可以接收到由该负载均衡分发的请求。
  - __租户级负载均衡器__ ：租户负载均衡器，Ingress 实例独属于当前命名空，或者独属于某一工作空间，并且设置的工作空间中包含当前命名空间，其中 Pod 都可以接收到由该负载均衡分发的请求。
- __Ingress Class__ :选填，选择对应的 Ingress 实例，选择后将流量导入到指定的 Ingress 实例。
  - 为 None 时使用默认的 DefaultClass，请在创建 Ingress 实例时设置 DefaultClass，更多信息，请参考 [Ingress Class](../../../network/modules/ingress-nginx/ingressclass.md)。
  - 若选择其他实例（如 __ngnix__ ），则会出现高级配置，可设置 __会话保持__ ， __路径重写__ ， __重定向__ ，和 __流量分发__ 。
- __会话保持__ ：选填，会话保持分为 三种类型： __L4 源地址哈希__ ， __Cookie Key__ ， __L7 Header Name__ ,开启后根据对应规则进行会话保持。
  - __L4 源地址哈希__ : :开启后默认在 Annotation 中加入如下标签：nginx.ingress.kubernetes.io/upstream-hash-by: "$binary_remote_addr"
  - __Cookie Key__ ：开启后来自特定客户端的连接将传递至相同 Pod，开启后 默认在 Annotation 中增加如下参数：nginx.ingress.kubernetes.io/affinity: "cookie"。nginx.ingress.kubernetes.io/affinity-mode: persistent
  - __L7 Header Name__ :开启后默认在 Annotation 中加入如下标签：nginx.ingress.kubernetes.io/upstream-hash-by: "$http_x_forwarded_for"
- __路径重写__ :选填， __rewrite-target__ ，某些场景中后端服务暴露的URL与Ingress规则中指定的路径不同，如果不进行URL重写配置，访问会出现错误。
- __重定向__ ：选填， __permanent-redirect__ ，永久重定向，输入重写路径后，访问路径重定向至设置的地址。
- __流量分发__ ：选填，开启后并设置后，根据设定条件进行流量分发。
  - __基于权重__ ：设定权重后，在创建的 Ingress 添加如下：Annotation: __nginx.ingress.kubernetes.io/canary-weight: "10"__ 。
  - __基于 Cookie__ ：设定 Cookie 规则后，流量根据设定的 Cookie 条件进行流量分发。
  - __基于 Header__ ： 设定 Header 规则后，流量根据设定的 Header 条件进行流量分发。
- __标签__ ：选填，为路由添加标签。
- __注解__ ：选填，为路由添加注解。
### 创建 HTTPS 协议路由

  输入如下参数：
  ![创建路由](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ingress04.png)

   !!! note

        注意：与 HTTP 协议 __设置路由规则__ 不同，增加密钥选择证书，其他基本一致。

- __协议__ :必填指授权入站到达集群服务的协议，支持 HTTP （不需要身份认证）或 HTTPS（需需要配置身份认证） 协议。这里选择 HTTPS 协议的路由。
- __密钥__ ：必填，Https TLS 证书，[创建秘钥](../configmaps-secrets/create-secret.md)。

### 完成路由创建

配置完所有参数后，点击 __确定__ 按钮，自动返回路由列表。在列表右侧，点击 __︙__ ，可以修改或删除所选路由。

![路由列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ingress05.png)
