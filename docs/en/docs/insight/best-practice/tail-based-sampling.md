---
MTPE: WANG0608GitHub
Date: 2024-09-25
---

# About Trace Sampling and Configuration

Using distributed tracing, you can observe how requests flow through various systems in a distributed
system. Undeniably, it is very useful for understanding service connections, diagnosing latency issues,
and providing many other benefits.

However, if most of your requests are successful and there are no unacceptable delays or errors, do you
really need all this data? Therefore, you only need to achieve the right insights through appropriate
data sampling rather than a large amount or complete data.

The idea behind sampling is to control the traces sent to the observability collector, thereby reducing
collection costs. Different organizations have different reasons for sampling, including why they want
to sample and what types of data they wish to sample. Therefore, we need to customize the sampling strategy:

- Cost Management: If a large amount of telemetry data needs to be stored, it incurs higher computational and storage costs.
- Focus on Interesting Traces: Different organizations prioritize different data types.
- Filter Out Noise: For example, you may want to filter out health checks.

It is important to use consistent terminology when discussing sampling. A Trace or Span is considered **sampled** or **unsampled**:

- **Sampled**: A Trace or Span that is processed and stored. It is chosen by the sampler to represent the overall data, so it is considered **sampled**.
- **Unsampled**: A Trace or Span that is not processed or stored. Because it was not selected by the sampler, it is considered **unsampled**.

## What Are the Sampling Options?

### Head Sampling

Head sampling is a sampling technique used to make a sampling decision as early as possible.
A decision to sample or drop a span or trace is not made by inspecting the trace as a whole.

For example, the most common form of head sampling is Consistent Probability Sampling. This is also be
referred to as Deterministic Sampling. In this case, a sampling decision is made based on the trace ID
and the desired percentage of traces to sample. This ensures that whole traces are sampled - no missing
spans - at a consistent rate, such as 5% of all traces.

The upsides to head sampling are:
- Easy to understand
- Easy to configure
- Efficient
- Can be done at any point in the trace collection pipeline

The primary downside to head sampling is that it is not possible to make a sampling decision based on
data in the entire trace. This means that while head sampling is effective as a blunt instrument, but
it is completely insufficient for sampling strategies that must consider information from the entire
system.
For example, you cannot ensure that all traces with an error within them are sampled with head sampling
alone. For this situation and many others, you need tail sampling.

### Tail Sampling (Recommended)

Tail sampling is where the decision to sample a trace takes place by considering all or most of the
spans within the trace. Tail Sampling gives you the option to sample your traces based on specific
criteria derived from different parts of a trace, which isn’t an option with Head Sampling.

Some examples of how to use tail sampling include:

- Always sampling traces that contain an error
- Sampling traces based on overall latency
- Sampling traces based on the presence or value of specific attributes on one or more spans in a trace;
  for example, sampling more traces originating from a newly deployed service
- Applying different sampling rates to traces based on certain criteria, such as when traces only come
  from low-volume services versus traces with high-volume services

As you can see, tail sampling allows for a much higher degree of sophistication in how you sample data.
For larger systems that must sample telemetry, it is almost always necessary to use Tail Sampling to
balance data volume with the usefulness of that data.

There are three primary downsides to tail sampling today:

- Tail sampling can be difficult to implement. Depending on the kind of sampling techniques available
  to you, it is not always a “set and forget” kind of thing. As your systems change, so too will your
  sampling strategies. For a large and sophisticated distributed system, rules that implement sampling
  strategies can also be large and sophisticated.
- Tail sampling can be difficult to operate. The component(s) that implement tail sampling must be stateful
  systems that can accept and store a large amount of data. Depending on traffic patterns, this can require
  dozens or even hundreds of compute nodes that all utilize resources differently. Furthermore, a tail sampler
  might need to “fall back” to less computationally intensive sampling techniques if it is unable to keep up
  with the volume of data it is receiving. Because of these factors, it is critical to monitor tail-sampling
  components to ensure that they have the resources they need to make the correct sampling decisions.
- Tail samplers often end up as vendor-specific technology today. If you’re using a paid vendor for Observability,
  the most effective tail sampling options available to you might be limited to what the vendor offers.

Finally, for some systems, tail sampling might be used in conjunction with Head Sampling. For example,
a set of services that produce an extremely high volume of trace data might first use head sampling to
sample only a small percentage of traces, and then later in the telemetry pipeline use tail sampling to
make more sophisticated sampling decisions before exporting to a backend. This is often done in the
interest of protecting the telemetry pipeline from being overloaded.

**DCE5 Insight currently recommends using tail sampling and prioritizes support for tail sampling.**

The tail sampling processor samples traces based on a defined set of strategies. However, all spans of a trace
must be received by the same collector instance to make effective sampling decisions.

Therefore, adjustments need to be made to the Global OpenTelemetry Collector architecture of Insight to implement
the tail sampling strategy.

## Specific Changes to Insight

Introduce an Opentelemetry Collector Gateway component with load balancing capabilities in front of
the `insight-opentelemetry-collector` in the Global cluster, allowing the same group of Traces to be
routed to the same Opentelemetry Collector instance based on the TraceID.

1. Deploy an OTEL COL Gateway component with load balancing capabilities.

    If you are using Insight V0.25.x, you can quickly enable this by using the Helm Upgrade parameter
    `--set opentelemetry-collector-gateway.enabled=true`, thereby skipping the deployment process
    described below.

    Refer to the following YAML to deploy the component.

    ??? note "Click to view deployment configuration"

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

1. Configure Tail Sampling Rules

    !!! note

        Tail sampling rules need to be added to the existing insight-otel-collector-config configmap configuration group.

1. Add the following content in the `processor` section, and adjust the specific rules as needed, refer to the
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

1. Activate the `processor` in the `otel col pipeline` within the `insight-otel-collector-config` **configmap**:

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

1. Restart the `insight-opentelemetry-collector` component.

1. When deploying the insight-agent, modify the reporting address of the link data to the `4317` port address of the `otel-col` LB.

    ```yaml
    ....
        exporters:
          otlp/global:
            endpoint: insight-opentelemetry-collector-lb.insight-system.svc.cluster.local:4317  # 👈 Modify to lb address
    ```

## Reference
- [sampling](https://opentelemetry.io/docs/concepts/sampling/)