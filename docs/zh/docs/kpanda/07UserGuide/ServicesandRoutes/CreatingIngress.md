# 创建路由（Ingress）

在 Kubernetes 集群中，[Ingress](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#ingress-v1beta1-networking-k8s-io) 公开从集群外部到集群内服务的 HTTP 和 HTTPS 路由。
流量路由由 Ingress 资源上定义的规则控制。下面是一个将所有流量都发送到同一 Service 的简单 Ingress 示例：

![ingress-diagram](../../images/ingress.svg)

Ingress 是对集群中服务的外部访问进行管理的 API 对象，典型的访问方式是 HTTP。Ingress 可以提供负载均衡、SSL 终结和基于名称的虚拟托管。

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](../Clusters/JoinACluster.md)或者[已创建 Kubernetes](../Clusters/CreateCluster.md)，且能够访问集群的 UI 界面。
- 已完成一个[命名空间的创建](../Namespaces/createns.md)、[用户的创建](../../../ghippo/04UserGuide/01access-control/user.md)，并将用户授权为 [`NS Edit`](../Permissions/PermissionBrief.md#ns-edit) 角色 ，详情可参考[命名空间授权](../Permissions/Cluster-NSAuth.md)。
- 已经完成 [Ingress 实例的创建](../../../network/modules/ingress-nginx/install.md)
- 单个实例中有多个容器时，请确保容器使用的端口不冲突，否则部署会失效。

## 创建路由

1. 以 `NS Edit` 用户成功登录后，点击左上角的`集群列表`进入`集群列表`页面。在集群列表中，点击一个集群名称。

    ![集群列表](../../images/service01.png)

2. 在左侧导航栏中，点击`容器网络`->`路由`进入服务列表，点击右上角`创建路由`按钮。

    ![服务与路由](../../images/ingress01.png)

    !!! tip

        也可以通过 `YAML 创建`一个路由。

3. 打开`创建路由`页面，进行配置。可选择两种协议类型，参考以下两个参数表进行配置。

    ![创建路由](../../images/ingress02.jpg)

### 创建 HTTP 协议路由

| 参数          | 说明                                                         | 举例值  |
| ------------- | :----------------------------------------------------------- | :------ |
| 路由名称      | 【类型】必填<br />【含义】输入新建路由的名称。<br />【注意】请输入4 到 63 个字符的字符串，可以包含小写英文字母、数字和中划线（-），并以小写英文字母开头，小写英文字母或数字。 | Ing-01  |
| 命名空间      | 【类型】必填<br />【含义】选择新建服务所在的命名空间。关于命名空间更多信息请参考[命名空间概述](../Namespaces/createns.md)。<br />【注意】请输入 4 到 63 个字符的字符串，可以包含小写英文字母、数字和中划线（-），并以小写英文字母开头，小写英文字母或数字结尾。 | default |
| 协议          | 【类型】必填<br />【含义】指授权入站到达集群服务的协议，支持 HTTP （不需要身份认证）或 HTTPS（需需要配置身份认证） 协议。这里选择 HTTP 协议的路由。 | HTTP    |
| 域名          | 【类型】必填<br />【含义】使用域名对外提供访问服务。默认为集群的域名 |         |
| Ingress Class | 【类型】选填<br />【含义】选择对应的 Ingress 实例，选择后将流量导入到指定的 Ingress 实例。为 None 时使用默认的 DefaultClass，请在创建 Ingress 实例时设置 DefaultClass，更多信息，请参考 [Ingress Class](../../../network/modules/ingress-nginx/ingressclass.md)<br /> | None    |
| 会话保持      | 【类型】选填<br />【含义】开启后来自特定客户端的连接将传递至相同 Pod，开启后 默认在 Annotation 中增加如下参数：<br />  nginx.ingress.kubernetes.io/affinity: "cookie"<br />  nginx.ingress.kubernetes.io/affinity-mode: persistent | 关闭    |
| 标签          | 【类型】选填<br />【含义】为路由添加标签<br />               | -       |
| 注解          | 【类型】选填<br />【含义】为路由添加注解<br />-              | -       |

### 创建 HTTPS 协议路由

| 参数          | 说明                                                         | 举例值  |
| :------------ | :----------------------------------------------------------- | :------ |
| 路由名称      | 【类型】必填<br />【含义】输入新建路由的名称。<br />【注意】请输入4 到 63 个字符的字符串，可以包含小写英文字母、数字和中划线（-），并以小写英文字母开头，小写英文字母或数字。 | Ing-01  |
| 命名空间      | 【类型】必填<br />【含义】选择新建服务所在的命名空间。关于命名空间更多信息请参考[命名空间概述](../Namespaces/createns.md)。<br />【注意】请输入4 到 63 个字符的字符串，可以包含小写英文字母、数字和中划线（-），并以小写英文字母开头，小写英文字母或数字结尾。 | default |
| 协议          | 【类型】必填<br />【含义】指授权入站到达集群服务的协议，支持 HTTP （不需要身份认证）或 HTTPS（需需要配置身份认证） 协议。这里选择 HTTPS 协议的路由。 | HTTPS   |
| 域名          | 【类型】必填<br />【含义】使用域名对外提供访问服务。默认为集群的域名 |         |
| CA 证书       | 【类型】必填<br />【含义】在服务端与客户端进行身份认证的证书，同时也支持您从本地上传。 |         |
| 转发策略      | 【类型】选填<br />【含义】指定 Ingress 的访问策略。<br />**路径**：指定服务访问的URL路径，默认为根路径/<br />**目标服务**：进行路由的服务名称<br />**目标服务端口**：服务对外暴露的端口 |         |
| Ingress Class | 【类型】选填<br />【含义】选择对应的 Ingress 实例，选择后将流量导入到指定的 Ingress 实例。为 None 时使用默认的 DefaultClass，请在创建 Ingress 实例时设置 DefaultClass，更多信息，请参考 [Ingress Class](../../../network/modules/ingress-nginx/ingressclass.md)<br /> | None    |
| 会话保持      | 【类型】选填<br />【含义】开启后来自特定客户端的连接将传递至相同 Pod，开启后 默认在 Annotation 中增加如下参数：<br />  nginx.ingress.kubernetes.io/affinity: "cookie"<br />  nginx.ingress.kubernetes.io/affinity-mode: persistent | 关闭    |
| 标签          | 【类型】选填<br />【含义】为路由添加标签                     |         |
| 注解          | 【类型】选填<br />【含义】为路由添加注解                     |         |

### 完成路由创建

配置完所有参数后，点击`确定`按钮，自动返回路由列表。在列表右侧，点击 `︙`，可以修改或删除所选路由。

![路由列表](../../images/ingress03.png)
