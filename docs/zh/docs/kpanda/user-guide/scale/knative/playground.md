# Knative 使用实践

在本节中，我们将通过几个实践来深入了解学习 Knative。

## case 1 - Hello World

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: hello
spec:
  template:
    spec:
      containers:
        - image: m.daocloud.io/ghcr.io/knative/helloworld-go:latest
          ports:
            - containerPort: 8080
          env:
            - name: TARGET
              value: "World"
```

可以使用 kubectl 已部署的应用的状态，这个应用由 knative 自动配置了 ingress 和伸缩器。

```shell
~ kubectl get service.serving.knative.dev/hello
NAME    URL                                              LATESTCREATED   LATESTREADY   READY   REASON
hello   http://hello.knative-serving.knative.loulan.me   hello-00001     hello-00001   True
```

部署出的 Pod YAML 如下，由 2 个 Pod 组成：user-container 和 queue-proxy。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-00003-deployment-5fcb8ccbf-7qjfk
spec:
  containers:
  - name: user-container
  - name: queue-proxy
```

![knative-request-flow](../../../images/knative-request-flow.png)

请求流：

1. case1 在低流量或零流量时，流量将路由到 activator
2. case2 流量大时，流量大于 target-burst-capacity 时才直接路由到 Pod
    1. 配置为 0，只有从 0 扩容存在
    2. 配置为 -1，activator 会一直存在请求路径
    3. 配置为 >0，触发扩缩容之前，系统能够额外处理的并发请求数量。
3. case3 流量再变小时，流量低于 current_demand + target-burst-capacity > (pods * concurrency-target) 时将再次路由到 activator
    
    待处理的请求总数 + 能接受的超过目标并发数的请求数量 > 每个 Pod 的目标并发数 * Pod 数量

## case 2 - 基于并发弹性伸缩

我们首先在集群应用下面 YAML 定义。

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: hello
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/target: "1"
        autoscaling.knative.dev/class: "kpa.autoscaling.knative.dev"
    spec:
      containers:
        - image: m.daocloud.io/ghcr.io/knative/helloworld-go:latest
          ports:
            - containerPort: 8080
          env:
            - name: TARGET
              value: "World"
```

执行下面命令测试，并可以通过 `kubectl get pods -A -w` 来观察扩容的 Pod。

```shell
wrk -t2 -c4 -d6s http://hello.knative-serving.knative.daocloud.io/
```

## case 3 - 基于并发弹性伸缩，达到特定比例提前扩容

我们可以很轻松的实现，例如限制每个容器并发为 10，可以通过 `autoscaling.knative.dev/target-utilization-percentage: 70` 来实现，达到 70% 就开始扩容 Pod。

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: hello
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/target: "10"
        autoscaling.knative.dev/class: "kpa.autoscaling.knative.dev"
        autoscaling.knative.dev/target-utilization-percentage: "70" 
        autoscaling.knative.dev/metric: "concurrency"
     spec:
      containers:
        - image: m.daocloud.io/ghcr.io/knative/helloworld-go:latest
          ports:
            - containerPort: 8080
          env:
            - name: TARGET
              value: "World"
```

## case 4 - 灰度发布/流量百分比

我们可以通过 `spec.traffic` 实现到每个版本流量的控制。

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: hello
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/target: "1"  
        autoscaling.knative.dev/class: "kpa.autoscaling.knative.dev"         
    spec:
      containers:
        - image: m.daocloud.io/ghcr.io/knative/helloworld-go:latest
          ports:
            - containerPort: 8080
          env:
            - name: TARGET
              value: "World"
  traffic:
  - latestRevision: true
    percent: 50
  - latestRevision: false
    percent: 50
    revisionName: hello-00001
