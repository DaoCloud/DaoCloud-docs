# Kantive 介绍

Knative 提供了一种更高层次的抽象，简化并加速了在 Kubernetes 上构建、部署和管理应用的过程。它使得开发人员能够更专注于业务逻辑的实现，而将大部分基础设施和运维工作交给 Knative 去处理，从而显著提高生产力。

## 组件

knative-operator 运行组件如下。

```shell
knative-operator   knative-operator-58f7d7db5c-7f6r5      1/1     Running     0     6m55s
knative-operator   operator-webhook-667dc67bc-qvrv4       1/1     Running     0     6m55s
```

knative-serving 组件如下。

```shell
knative-serving        3scale-kourier-gateway-d69fbfbd-bd8d8   1/1     Running     0                 7m13s
knative-serving        activator-7c6fddd698-wdlng              1/1     Running     0                 7m3s
knative-serving        autoscaler-8f4b876bb-kd25p              1/1     Running     0                 7m17s
knative-serving        autoscaler-hpa-5f7f74679c-vkc7p         1/1     Running     0                 7m15s
knative-serving        controller-789c896c46-tfvsv             1/1     Running     0                 7m17s
knative-serving        net-kourier-controller-7db578c889-7gd5l 1/1     Running     0                 7m14s
knative-serving        webhook-5c88b94c5-78x7m                 1/1     Running     0                 7m1s
knative-serving        storage-version-migration-serving-serving-1.12.2-t7zvd   0/1  Completed   0   7m15s
```

| 组件 | 作用 |
|----------|-------------|
| Activator | 对请求排队（如果一个 Knative Service 已经缩减到零）。调用 autoscaler，将缩减到 0 的服务恢复并转发排队的请求。Activator 还可以充当请求缓冲器，处理突发流量。 |
| Autoscaler | Autoscaler 负责根据配置、指标和进入的请求来缩放 Knative 服务。 |
| Controller | 管理 Knative CR 的状态。它会监视多个对象，管理依赖资源的生命周期，并更新资源状态。 |
| Queue-Proxy | Sidecar 容器，每个 Knative Service 都会注入一个。负责收集流量数据并报告给 Autoscaler，Autoscaler 根据这些数据和预设的规则来发起扩容或缩容请求。 |
| Webhooks | Knative Serving 有几个 Webhooks 负责验证和变更 Knative 资源。 |

## Ingress 流量入口方案

| 方案 | 适用场景 |
|----------|-------------|
| Istio | 如果已经用了 Istio，可以选择 Istio 作为流量入口方案。 |
| Contour | 如果集群中已经启用了 Contour，可以选择 Contour 作为流量入口方案。 |
| Kourier | 如果在没有上述 2 种 Ingress 组件时，可以使用 Knative 基于 Envoy 实现的 Kourier Ingress 作为流量入口。 |

## Autoscaler 方案对比

| Autoscaler 类型 | 是否为 Knative Serving 核心部分 | 默认启用 | Scale to Zero 支持 | 基于 CPU 的 Autoscaling 支持 |
| -------------- | -------------------------- | ------------ | ------------------ | -------------- |
| Knative Pod Autoscaler (KPA)    | 是         | 是          | 是      | 否                           |
| Horizontal Pod Autoscaler (HPA) | 否         | 需安装 Knative Serving 后启用 | 否       | 是               |

## CRD

| 资源类型      | API 名称     | 描述 |
| ------------ | ----------- | --- |
| Services       | service.serving.knative.dev       | 自动管理 Workload 的整个生命周期，控制其他对象的创建，确保应用具有 Routes、Configurations 以及每次更新时的新 revision。 |
| Routes         | route.serving.knative.dev         | 将网络端点映射到一个或多个修订版本，支持流量分配和版本路由。 |
| Configurations | configuration.serving.knative.dev | 维护部署的期望状态，提供代码和配置之间的分离，遵循 Twelve-Factor 应用程序方法论，修改配置会创建新的 revision。 |
| Revisions      | revision.serving.knative.dev      | 每次对工作负载修改的时间点快照，是不可变对象，可根据流量自动扩容和缩容。 |
