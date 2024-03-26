# Kantive Introduction

Knative provides a higher level of abstraction, simplifying and speeding up the process of building, deploying, and managing applications on Kubernetes. It allows developers to focus more on implementing business logic, while leaving most of the infrastructure and operations work to Knative, significantly improving productivity.

## Components

The Knative operator runs the following components.

```shell
knative-operator   knative-operator-58f7d7db5c-7f6r5      1/1     Running     0     6m55s
knative-operator   operator-webhook-667dc67bc-qvrv4       1/1     Running     0     6m55s
```

The Knative serving components are as follows.

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

| Component | Function |
|----------|-------------|
| Activator | Queues requests (if a Knative Service has scaled to zero). Calls the autoscaler to bring back services that have scaled down to zero and forward queued requests. The Activator can also act as a request buffer, handling bursts of traffic. |
| Autoscaler | Responsible for scaling Knative services based on configuration, metrics, and incoming requests. |
| Controller | Manages the state of Knative CRs. It monitors multiple objects, manages the lifecycle of dependent resources, and updates resource status. |
| Queue-Proxy | Sidecar container injected into each Knative Service. Responsible for collecting traffic data and reporting it to the Autoscaler, which then initiates scaling requests based on this data and preset rules. |
| Webhooks | Knative Serving has several Webhooks responsible for validating and mutating Knative resources. |

## Ingress Traffic Entry Solutions

| Solution | Use Case |
|----------|-------------|
| Istio | If Istio is already in use, it can be chosen as the traffic entry solution. |
| Contour | If Contour has been enabled in the cluster, it can be chosen as the traffic entry solution. |
| Kourier | If neither of the above two Ingress components are present, Knative's Envoy-based Kourier Ingress can be used as the traffic entry solution. |

## Autoscaler Solutions Comparison

| Autoscaler Type | Core Part of Knative Serving | Default Enabled | Scale to Zero Support | CPU-based Autoscaling Support |
| -------------- | -------------------------- | ------------ | ------------------ | -------------- |
| Knative Pod Autoscaler (KPA)    | Yes         | Yes          | Yes      | No                           |
| Horizontal Pod Autoscaler (HPA) | No         | Needs to be enabled after installing Knative Serving | No       | Yes               |

## CRD

| Resource Type       | API Name                          | Description                                                         |
| -------------- | --------------------------------- | ------------------------------------------------------------ |
| Services       | service.serving.knative.dev       | Automatically manages the entire lifecycle of Workloads, controls the creation of other objects, ensures applications have Routes, Configurations, and new revisions with each update. |
| Routes         | route.serving.knative.dev         | Maps network endpoints to one or more revision versions, supports traffic distribution and version routing. |
| Configurations | configuration.serving.knative.dev | Maintains the desired state of deployments, provides separation between code and configuration, follows the Twelve-Factor App methodology, modifying configurations creates new revisions. |
| Revisions      | revision.serving.knative.dev      | Snapshot of the workload at each modification time point, immutable object, automatically scales based on traffic. |
