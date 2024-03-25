# Tail Sampling Scheme

The tail sampling processor samples the links according to a set of defined policies. However,
all spans of the link must be received by the same collector instance in order to make effective sampling decisions.

Therefore, adjustments need to be made to the Global Opentelemetry Collector architecture of Insight to implement tail sampling policies.

## Specific Changes

Introducing an Otel Col with LB capability in front of the Global Opentelemetry Collector.

## Steps for Changes

### Deploy OTEL COL Component with LB Capability

Refer to the following YAML to deploy the component.

??? note "Click to view deployment configuration"

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

### Configure Tail Sampling Rules

!!! note

    Tail sampling rules need to be added to the existing insight-otel-collector-config configmap configuration group.

1. Add the following content in the `processor` section, and adjust the specific rules as needed; refer to the
   [OTel official example](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md#a-practical-example).

    ```yaml
    ........
    tail_sampling:
      decision_wait: 10s # Wait for 10 seconds, traces older than 10 seconds will no longer be processed
      num_traces: 1500000  # Number of traces saved in memory, assuming 1000 traces per second, should not be less than 1000 * decision_wait * 2;
                           # Setting it too large may consume too much memory resources, setting it too small may cause some traces to be dropped
      expected_new_traces_per_sec: 10
      policies: # Reporting policies
        [
            {
              name: latency-policy,
              type: latency,  # Report traces that exceed 500ms
              latency: {threshold_ms: 500}
            },
            {
              name: status_code-policy,
              type: status_code,  # Report traces with ERROR status code
              status_code: {status_codes: [ ERROR ]}
            }
        ]
    ......
    tail_sampling: # Composite sampling
      decision_wait: 10s # Wait for 10 seconds, traces older than 10 seconds will no longer be processed
      num_traces: 1500000  # Number of traces saved in memory, assuming 1000 traces per second, should not be less than 1000 * decision_wait * 2;
                           # Setting it too large may consume too much memory resources, setting it too small may cause some traces to be dropped
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

2. Activate this `processor` in the otel col pipeline:

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

3. Restart the `insight-opentelemetry-collector` component.

4. When deploying the Insight-agent, modify the reporting address of the link data to the `4317` port address of the `otel-col` LB.

    ```yaml
    ....
        exporters:
          otlp/global:
            endpoint: insight-opentelemetry-collector-lb.insight-system.svc.cluster.local:4317  # 👈 Modify to lb address
    ```
