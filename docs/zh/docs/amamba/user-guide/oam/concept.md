# OAM 概念介绍

OAM 应用功能基于开源软件 [KubeVela](http://kubevela.net/zh/docs/v1.2/) ，通过开放应用模型（OAM）作为应用交付的顶层抽象，主要是对 Kubernetes 的资源的抽象与整合。

一个 OAM 应用为了实现在混合环境中标准化和高效率的应用交付，由四部分概念组成：
- 一个或多个组件
- 各项运维动作
- 应用的执行策略（Policy）
- 部署工作流（Workflow）

可参考下图，来源于 KubeVela 官方文档站。

![oam1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/oam001.png)

## 核心组件介绍

仅介绍应用工作台涵盖的核心组件的介绍说明。

### 组件

组件（Components）可以定义一个制品或云服务的交付和管理形式，一个应用中可以包括多个组件。
最佳的实践方案是一个应用包括一个主组件（核心业务）和附属组件（强依赖或独享的中间件，运维组件等）。
有关组件类型说明，可参考 [kubevela Component Definition](http://kubevela.net/zh/docs/v1.2/platform-engineers/oam/x-definition#%E7%BB%84%E4%BB%B6%E5%AE%9A%E4%B9%89%EF%BC%88componentdefinition%EF%BC%89)。

目前应用工作台基于 [kubevela](https://kubevela.io/zh/docs/) 开源组件内置了
**Cron-Task、Daemon、K8s-Objects、Task、Webservice** 五种组件。有关各种组件的具体参数介绍，
可参考[内置组件列表](https://kubevela.io/zh/docs/end-user/components/references)。

### 运维特征

运维特征（Traits）是可以随时绑定给待部署组件的、模块化、可拔插的运维能力，
比如：副本数调整（手动、自动）、数据持久化、设置网关策略、自动设置 DNS 解析等。用户可以从社区获取成熟的能力，也可以自行定义。

目前应用工作台基于 [kubevela](https://kubevela.io/zh/docs/) 开源组件内置了
**Affinity、Annotations、Command、Container-Image、Cpuscaler** 等多种运维特征。
有关运维特征的具体参数介绍，可参考[内置运维特征列表](https://kubevela.io/zh/docs/end-user/traits/references)。

### 应用的执行策略（Policy）

应用工作台暂未产品化该能力，[详细介绍前往 kubevela 参考](http://kubevela.net/zh/docs/v1.2/platform-engineers/oam/oam-model#%E5%BA%94%E7%94%A8%E7%9A%84%E6%89%A7%E8%A1%8C%E7%AD%96%E7%95%A5policy)。

### 部署执行工作流（Workflow）

应用工作台暂未产品化该能力，所有没有提供定义工作流的界面，KubeVela 默认会自动按照组件和运维特征数组的顺序进行部署到用户所选择集群中。
[详细介绍前往 kubevela 参考](http://kubevela.net/zh/docs/v1.2/platform-engineers/oam/oam-model#%E9%83%A8%E7%BD%B2%E6%89%A7%E8%A1%8C%E5%B7%A5%E4%BD%9C%E6%B5%81workflow)。

## 自定义功能

Kubevela 可以根据您的需求轻松实现原地定制和扩展。

#### 自定义组件

组件定义（ComponentDefinition）的设计目标是，允许平台管理员将任何类型的可部署制品封装成待交付的“组件”。
只要定义好之后，这种类型的组件就可以被用户在部署计划（Application）中引用、实例化并交付出去。

有关自定义组件的具体操作，可参考官方文档：[自定义组件入门](http://kubevela.net/zh/docs/v1.2/platform-engineers/components/custom-component)。

#### 自定义运维特征

运维特征定义（TraitDefinition）为组件提供了一系列可被按需绑定的运维动作，这些运维动作通常都是由平台管理员提供的运维能力，
为这个组件提供一系列的运维操作和策略，比如添加一个负载均衡策略、路由策略、或者执行弹性扩缩容、灰度发布策略等等。

有关自定义运维特征的具体操作，可参考官方文档：[自定义运维特征](http://kubevela.net/zh/docs/v1.2/platform-engineers/traits/customize-trait)。
