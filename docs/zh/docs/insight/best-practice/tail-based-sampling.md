# 尾部采样方案

尾部采样处理器根据一组定义的策略对链路进行采样。但是，链路的所有跨度（span）必须由同一收集器实例接收，以做出有效的采样决策。

因此，需要对 Insight 的 Global Opentelemetry Collector  架构进行调整以实现尾部采样策略。

## 具体改动

在 Global Opentelemetry Collector 前面引入具有  Load Balancer 功能的 Otel Col。


## 改动步骤

### 部署具有 Load Balance 能力的 OTEL COL 组件

??? note "点击查看部署配置"

    ```yaml
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: insight-otel-collector-lb
    rules:
    - apiGroups: [""]
      resources: ["endpoints"]
      verbs: ["get", "watch", "list"]
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: insight-otel-collector-lb
      namespace: insight-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: insight-otel-collector-lb
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: insight-otel-collector-lb
    subjects:
    - kind: ServiceAccount
      name: insight-otel-collector-lb
      namespace: insight-system
    ---
    kind: ConfigMap
    metadata:
      labels:
        app.kubernetes.io/component: opentelemetry-collector
        app.kubernetes.io/instance: insight-otel-collector-lb
        app.kubernetes.io/name: insight-otel-collector-lb
      name: insight-otel-collector-lb-collector
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
        app.kubernetes.io/instance: insight-otel-collector-lb
        app.kubernetes.io/name: insight-otel-collector-lb
      name: insight-otel-collector-lb
      namespace: insight-system
    spec:
      replicas: 2
      selector:
        matchLabels:
          app.kubernetes.io/component: opentelemetry-collector
          app.kubernetes.io/instance: insight-otel-collector-lb
          app.kubernetes.io/name: insight-otel-collector-lb
      template:
        metadata:
          labels:
            app.kubernetes.io/component: opentelemetry-collector
            app.kubernetes.io/instance: insight-otel-collector-lb
            app.kubernetes.io/name: insight-otel-collector-lb
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
    
          serviceAccount: insight-otel-collector-lb
          serviceAccountName: insight-otel-collector-lb
          volumes:
          - configMap:
              defaultMode: 420
              items:
              - key: collector.yaml
                path: collector.yaml
              name: insight-otel-collector-lb-collector
            name: otc-internal
    ---
    kind: Service
    apiVersion: v1
    metadata:
      name: insight-opentelemetry-collector-lb
      namespace: insight-system
      labels:
        app.kubernetes.io/component: opentelemetry-collector
        app.kubernetes.io/instance: insight-otel-collector-lb
        app.kubernetes.io/name: insight-otel-collector-lb
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
        app.kubernetes.io/instance: insight-otel-collector-lb
        app.kubernetes.io/name: insight-otel-collector-lb
    ```

### 配置尾部采样规则

!!! note

    需要在原本 insight-otel-collector-config configmap 配置组中增加尾部采样（tail_sampling processors）的规则。

1. 在 `processor` 中增加如下内容，具体规则可调整；参考：[官方示例](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md#a-practical-example)

    ```yaml
    ........
    tail_sampling:
      decision_wait: 10s # 等待 10 秒，超过 10 秒后的 traceid 将不再处理
      num_traces: 1500000  # 内存中保存的 trace 数，假设每秒 1000 条 trace，最小不低于 1000 * decision_wait * 2；设置过大会占用过多的内存资源，过小会导致部分 trace 被 drop 掉
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
    # 组合采样
    tail_sampling:
      decision_wait: 10s # 等待 10 秒，超过 10 秒后的 traceid 将不再处理
      num_traces: 1500000  # 内存中保存的 trace 数，假设每秒 1000 条 trace，最小不低于 1000 * decision_wait * 2；设置过大会占用过多的内存资源，过小会导致部分 trace 被 drop 掉
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

2. 在 otel col pipeline 中激活该 `processor` ：

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

4. 在部署 Insight-agent 时，将链路数据的上报地址修改为 `otel-col` LB 的 `4317` 端口地址。

    ```yaml
    ....
        exporters:
          otlp/global:
            endpoint: insight-opentelemetry-collector-lb.insight-system.svc.cluster.local:4317  # 👈 修改为 lb 地址
    ```
