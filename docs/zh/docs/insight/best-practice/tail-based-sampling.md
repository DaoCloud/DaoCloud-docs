# 链路数据采样介绍与配置

使用分布式链路跟踪，可以在分布式系统中观察请求如何在各个系统中流转。不可否认，它非常实用，例如了解您的服务连接和诊断延迟问题，以及许多其他好处。

但是，如果您的大多数请求都成功了 200 秒，并且没有出现不可接受的延迟或错误，那么您真的需要所有这些数据吗？所以，你并不总是需要大量的数据来找到正确的见解。您只需要通过恰当的的数据采样即可。

采样背后的想法是控制发送到可观察性收集器的链路，从而降低采集成本。不同的组织有不同的原因，比如为什么要抽样，以及想要抽样什么杨的数据。所以，我们需要自定义采样策略：

- 管理成本：如果需要存储大量的遥测数据，则需要付出更多的计算、存储成本。
- 关注有趣的跟踪：不同组织关注的数据也不同。
- 过滤掉噪音：例如，您可能希望过滤掉健康检查。

在讨论采样时使用一致的术语是很重要的。Trace 或 Span 被视为 **采样** 或 **未采样**：

- 采样：Trace 或 Span 被处理并保存。为它被采样者选择为总体的代表，所以它被认为是 **抽样的**。
- 未采样：不被处理或保存的 Trace 或 Span。因为它不是由采样器选择的，所以被认为是 **未采样**。

## 采样的方式有哪些？

### 头部采样（Head Sampling）

头部抽样是一种抽样技术，用于尽早做出抽样决定。采样或删除 Trace 或 Span 的决定不是通过检查整个 Trace 来做出的。

例如，最常见的头部抽样形式是一致概率抽样。它也可以称为确定性采样。在这种情况下，将根据 TraceID 和要采样的所需 Trace 百分比做出采样决策。这可确保以一致的速率（例如所有 Trace的 5%）对整个 Trace 进行采样（不遗漏 Span。

头部采样的好处是：
- 易于理解
- 易于配置
- 高效
- 可以在跟踪收集管道中的任何位置完成

头部采样的主要缺点是无法根据整个 Trace 中的数据做出采样决策。这意味着头部抽样作为一种钝器是有效的，但对于必须考虑整个系统信息的抽样策略来说，这是完全不够的。例如，无法使用头部采样来确保对所有具有误差的迹线进行采样。为此，您需要尾部采样。

### 尾部采样（Tail Sampling）—— 推荐方案

尾部采样是通过考虑 Trace 内的全部或大部分 Span 来决定对 Trace 进行采样。尾部采样允许您根据从 Trace 的不同部分使用的特定条件对 Trace 进行采样，而头部采样则不具有此选项。

如何使用尾部采样的一些示例包括：

- 始终对包含错误的 Trace 进行采样
- 基于总体延迟的采样
- 根据 Trace 中一个或多个 Span 上特定属性的存在或值对 Trace 进行采样; 例如，对源自新部署的服务的更多 Trace 进行采样
- 根据特定条件对 Trace 应用不同的采样率

正如你所看到的，尾部采样有着更高程度的复杂度。对于必须对遥测数据进行采样的大型系统，几乎总是需要使用尾部采样来平衡数据量和数据的有用性。

如今，尾部采样有三个主要缺点：

- 尾部采样可能难以操作。实现尾部采样的组件必须是可以接受和存储大量数据的有状态系统。根据流量模式，这可能需要数十个甚至数百个节点，这些节点都以不同的方式利用资源。此外，如果尾部采样器无法跟上接收的数据量，则可能需要“回退”到计算密集度较低的采样技术。由于这些因素，监控尾部采样组件以确保它们拥有做出正确采样决策所需的资源至关重要。
- 尾部采样可能难以实现。根据您可用的采样技术类型，它并不总是“一劳永逸”的事情。随着系统的变化，您的采样策略也会发生变化。对于大型而复杂的分布式系统，实现采样策略的规则也可以是庞大而复杂的。
- 如今，尾部采样器通常最终属于供应商特定技术领域。如果您使用付费供应商来实现可观测性，则可用的最有效的尾部采样选项可能仅限于供应商提供的内容。

最后，对于某些系统，尾部采样可以与头部采样结合使用。例如，一组生成大量 Trace 数据的服务可能首先使用头部采样仅对一小部分跟踪进行采样，然后在遥测管道中稍后使用尾部采样在导出到后端之前做出更复杂的采样决策。这样做通常是为了保护遥测管道免于过载。

**DCE5 Insight 目前推荐使用尾部采样并优先支持尾部采样。**

尾部采样处理器根据一组定义的策略对链路进行采样。但是，链路的所有跨度（span）必须由同一收集器实例接收，以做出有效的采样决策。

因此，需要对 Insight 的 Global Opentelemetry Collector 架构进行调整以实现尾部采样策略。

## Insight 具体改动

在 Global 集群中的 `insight-opentelemetry-collector` 前面引入具有负载均衡能力的 Opentelemetry Collector Gateway 组件，使得同一组 Trace 能够根据 TraceID 路由到同一个 Opentelemetry Collector 实例。

1. 部署具有负载均衡能力的 OTEL COL Gateway 组件

如果您使用了 Insight 0.25.x 版本，可以通过如下 Helm Upgrade 参数 `--set opentelemetry-collector-gateway.enabled=true` 快速开启，以此跳过如下部署过程。

参照以下 YAML 配置来部署。

??? note "点击查看部署配置"

    ```yaml
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: insight-otel-collector-gateway
    rules:
    - apiGroups: [""]
      resources: ["endpoints"]
      verbs: ["get", "watch", "list"]
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: insight-otel-collector-gateway
      namespace: insight-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: insight-otel-collector-gateway
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: insight-otel-collector-gateway
    subjects:
    - kind: ServiceAccount
      name: insight-otel-collector-gateway
      namespace: insight-system
    ---
    kind: ConfigMap
    metadata:
      labels:
        app.kubernetes.io/component: opentelemetry-collector
        app.kubernetes.io/instance: insight-otel-collector-gateway
        app.kubernetes.io/name: insight-otel-collector-gateway
      name: insight-otel-collector-gateway-collector
      namespace: insight-system
    apiVersion: v1
    data:
      collector.yaml: |
        receivers:
          otlp:
            protocols:
              grpc:
              http:
          jaeger:
            protocols:
              grpc:
        processors:
    
        extensions:
          health_check:
          pprof:
            endpoint: :1888
          zpages:
            endpoint: :55679
        exporters:
          logging:
          loadbalancing:
            routing_key: "traceID"
            protocol:
              otlp:
                # all options from the OTLP exporter are supported
                # except the endpoint
                timeout: 1s
                tls:
                  insecure: true
            resolver:
              k8s:
                service: insight-opentelemetry-collector
                ports:
                  - 4317
        service:
          extensions: [pprof, zpages, health_check]
          pipelines:
            traces:
              receivers: [otlp, jaeger]
              exporters: [loadbalancing]
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app.kubernetes.io/component: opentelemetry-collector
        app.kubernetes.io/instance: insight-otel-collector-gateway
        app.kubernetes.io/name: insight-otel-collector-gateway
      name: insight-otel-collector-gateway
      namespace: insight-system
    spec:
      replicas: 2
      selector:
        matchLabels:
          app.kubernetes.io/component: opentelemetry-collector
          app.kubernetes.io/instance: insight-otel-collector-gateway
          app.kubernetes.io/name: insight-otel-collector-gateway
      template:
        metadata:
          labels:
            app.kubernetes.io/component: opentelemetry-collector
            app.kubernetes.io/instance: insight-otel-collector-gateway
            app.kubernetes.io/name: insight-otel-collector-gateway
        spec:
          containers:
          - args:
            - --config=/conf/collector.yaml
            env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  apiVersion: v1
                  fieldPath: metadata.name
            image: ghcr.m.daocloud.io/openinsight-proj/opentelemetry-collector-contrib:5baef686672cfe5551e03b5c19d3072c432b6f33
            imagePullPolicy: IfNotPresent
            livenessProbe:
              failureThreshold: 3
              httpGet:
                path: /
                port: 13133
                scheme: HTTP
              periodSeconds: 10
              successThreshold: 1
              timeoutSeconds: 1
            name: otc-container
            resources:
              limits:
                cpu: '1'
                memory: 2Gi
              requests:
                cpu: 100m
                memory: 400Mi
            ports:
            - containerPort: 14250
              name: jaeger-grpc
              protocol: TCP
            - containerPort: 8888
              name: metrics
              protocol: TCP
            - containerPort: 4317
              name: otlp-grpc
              protocol: TCP
            - containerPort: 4318
              name: otlp-http
              protocol: TCP
            - containerPort: 55679
              name: zpages
              protocol: TCP
    
            volumeMounts:
            - mountPath: /conf
              name: otc-internal
    
          serviceAccount: insight-otel-collector-gateway
          serviceAccountName: insight-otel-collector-gateway
          volumes:
          - configMap:
              defaultMode: 420
              items:
              - key: collector.yaml
                path: collector.yaml
              name: insight-otel-collector-gateway-collector
            name: otc-internal
    ---
    kind: Service
    apiVersion: v1
    metadata:
      name: insight-opentelemetry-collector-gateway
      namespace: insight-system
      labels:
        app.kubernetes.io/component: opentelemetry-collector
        app.kubernetes.io/instance: insight-otel-collector-gateway
        app.kubernetes.io/name: insight-otel-collector-gateway
    spec:
      ports:
        - name: fluentforward
          protocol: TCP
          port: 8006
          targetPort: 8006
        - name: jaeger-compact
          protocol: UDP
          port: 6831
          targetPort: 6831
        - name: jaeger-grpc
          protocol: TCP
          port: 14250
          targetPort: 14250
        - name: jaeger-thrift
          protocol: TCP
          port: 14268
          targetPort: 14268
        - name: metrics
          protocol: TCP
          port: 8888
          targetPort: 8888
        - name: otlp
          protocol: TCP
          appProtocol: grpc
          port: 4317
          targetPort: 4317
        - name: otlp-http
          protocol: TCP
          port: 4318
          targetPort: 4318
        - name: zipkin
          protocol: TCP
          port: 9411
          targetPort: 9411
        - name: zpages
          protocol: TCP
          port: 55679
          targetPort: 55679
      selector:
        app.kubernetes.io/component: opentelemetry-collector
        app.kubernetes.io/instance: insight-otel-collector-gateway
        app.kubernetes.io/name: insight-otel-collector-gateway
    ```

2. 配置尾部采样规则

!!! note

    需要在原本 insight-otel-collector-config configmap 配置组中增加尾部采样（tail_sampling processors）的规则。

1. 在 `processor` 中增加如下内容，具体规则可调整；参考 [OTel 官方示例](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md#a-practical-example)。

    ```yaml
    ........
    tail_sampling:
      decision_wait: 10s # 等待 10 秒，超过 10 秒后的 traceid 将不再处理
      num_traces: 1500000  # 内存中保存的 trace 数，假设每秒 1000 条 trace，最小不低于 1000 * decision_wait * 2；
                           # 设置过大会占用过多的内存资源，过小会导致部分 trace 被 drop 掉
      expected_new_traces_per_sec: 10
      policies: # 上报策略
        [
            {
              name: latency-policy,
              type: latency,  # 耗时超过 500ms 上报
              latency: {threshold_ms: 500}
            },
            {
              name: status_code-policy,
              type: status_code,  # 状态码为 ERROR 的上报
              status_code: {status_codes: [ ERROR ]}
            }
        ]
    ......
    tail_sampling: # 组合采样
      decision_wait: 10s # 等待 10 秒，超过 10 秒后的 traceid 将不再处理
      num_traces: 1500000  # 内存中保存的 trace 数，假设每秒 1000 条 trace，最小不低于 1000 * decision_wait * 2；
                           # 设置过大会占用过多的内存资源，过小会导致部分 trace 被 drop 掉
      expected_new_traces_per_sec: 10
      policies: [
          {
            name: debug-worker-cluster-sample-policy,
            type: and,
            and:
              {
                and_sub_policy:
                  [
                    {
                      name: service-name-policy,
                      type: string_attribute,
                      string_attribute:
                        { key: k8s.cluster.id, values: [xxxxxxx] },
                    },
                    {
                      name: trace-status-policy,
                      type: status_code,
                      status_code: { status_codes: [ERROR] },
                    },
                    {
                      name: probabilistic-policy,
                      type: probabilistic,
                      probabilistic: { sampling_percentage: 1 },
                    }
                  ]
              }
          }
        ]
    ```

2. 在 `insight-otel-collector-config` **configmap** 中的 otel col pipeline 中激活该 `processor`：

    ```yaml
    traces:
      exporters:
        - servicegraph
        - otlp/jaeger
      processors:
        - memory_limiter
        - tail_sampling # 👈
        - batch
      receivers:
        - otlp
    ```

3. 重启 `insight-opentelemetry-collector` 组件。

4. 部署或更新 Insight-agent，将链路数据的上报地址修改为 `opentelemetry-collector-gateway` LB 的 `4317` 端口地址。

    ```yaml
    ....
        exporters:
          otlp/global:
            endpoint: insight-opentelemetry-collector-gateway.insight-system.svc.cluster.local:4317  # 👈 修改为 gateway/lb 地址
    ```
