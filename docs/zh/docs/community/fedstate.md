# 云原生联邦中间件 FedState

FedState 指的是 Federation Stateful Service，主要的设计目标是为了解决在多云、
多集群、多数据中心的场景下，有状态服务的编排、调度、部署和自动化运维等能力。

FedState 对需要部署在多云环境上的中间件、数据库等有状态的服务通过 Karmada
下发到各个成员集群，使其正常工作的同时并提供一些高级运维能力。

## 架构

![架构图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/community/images/structure.png)

组件说明：

- FedStateScheduler: 多云有状态服务调度器，在 Karmada 调度器的基础上，
  添加了一些与中间件服务相关的调度策略。
- FedState：多云有状态服务控制器主要负责按需配置各个管控集群与通过 Karmada 分发。
- Member Operator：表示部署在管控平面的有状态服务 Operator，
  FedState 内置了 Mongo Operator，后续会支持更多的有状态服务。
- FedStateCR：表示多云有状态服务实例的一个概念。
- FedStateCR-Member：表示多云有状态服务被下发到管控平面的实例。

## 参考文档

- 博文：[介绍云原生联邦中间件 FedState](../blogs/230605-fedstate.md)
- Repo 地址: https://github.com/fedstate/fedstate
