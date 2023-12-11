# 通过原生应用部署传统微服务

原生应用旨在为客户提供由多个 Kubernets 资源关联组成的应用，并提供统一视图。
本文介绍如何通过原生应用部署传统的微服务应用。本文用到的两个示例微服务应用名为  **adservice**  和  **dataservice** 。

![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native01.png)

## 前提条件

- 当前工作空间下有创建好的托管 Nacos 实例，参考[创建托管注册中心](../../../skoala/trad-ms/hosted/index.md)。
- 准备好需要部署的传统微服务的镜像，在本文中即  **adservice**  和  **dataservice**  的镜像。
- 需要改造传统微服务的代码，在代码中集成 Nacos 注册中心的 SDK。
- 如果要使用 Sentinel 治理传统微服务的流量，则还需要在代码中集成 Sentinel 的 Client。

## 创建原生应用

1. 在 **应用工作台**  ->  **概览** 页面中，点击 **原生应用** 页签，然后在右上角点击 **创建应用** 。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native02.png)

2. 参考以下说明填写基本信息，然后点击 **下一步** 。

    - 名称：原生应用的名称。
    - 别名：原生应用的别名。
    - 部署位置：选择将原生应用部署到哪个集群下的哪个命名空间。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native03.png)

3. 参考以下说明添加传统微服务。

    添加微服务时， **基本信息**  和  **容器配置**  为必填信息，高级配置为选填信息。

    - 基本信息：设置微服务的名称、资源类型和实例数
    - 容器配置

        - 容器镜像：填写微服务的镜像地址
        - 服务配置：端口配置取决于服务代码。就此处的演示应用  **adservice**  而言，需要填写如下信息：

        ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native04.png)

    - 高级配置

        - 接入微服务：即将所添加的传统微服务接入 DCE 5.0 的[微服务引擎](../../../skoala/intro/index.md)模块
        - 选择框架：微服务使用的框架，例如  **Spring Cloud**  或  **Dubbo** 
        - 注册中心实例：选择将所添加的微服务接入哪个注册中心。可选项来自通过微服务引擎模块在当前工作空间下创建的托管 Nacos 注册中心实例。
        - 注册中心命名空间：微服务应用的 Nacos 命名空间
        - 注册中心服务分组：微服务应用的服务分组，即 Nacos 中的 Group 概念
        - 用户名/密码：如果该注册中心实例被认证，则需要填写用户名密码
        - 开启微服务治理：所选的注册中心实例应开启 [Sentinel 或 Mesh 治理能力](../../../skoala/trad-ms/hosted/plugins/plugin-center.md)

        ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native05.png)

    !!! note
    
        如需添加更多微服务，点击屏幕右侧的  **➕**  即可。

        ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native06.png)

4. 根据需要配置路由并在右下角点击 **确定** 。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native07.png)

## 查看原生应用下的微服务

1. 应用创建成功后，点击应用名称，可以查看当前应用下的负载带有 **传统微服务** 标识。

    > 点击弹出的黑色链接可以跳转到微服务引擎下的服务详情页面。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native08.png)

2. 也可以前往 **微服务引擎** 模块，在对应的工作空间和注册中心下查看所添加的服务。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native09.png)

## 模拟服务调用

1. 首先在 **容器管理平台** 将  **adservice**  的服务的访问类型更改为  **NodePort** 。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native10.png)

2. 在服务详情页面点击服务端口为  **8081**  的外部访问地址。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native11.png)

3. 浏览器新开标签出现如下页面，表示  **adservice**  部署成功。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native12.png)

4. 在 URL 地址后增加  **/ad/all**  进行访问，出现下图表示调用  **dataservice**  服务成功。

    ![示意图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native13.png)
