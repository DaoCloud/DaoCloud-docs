# 使用 OpenTelemetry 零代码接收 SkyWalking 链路数据

可观测性 Insight 通过 OpenTelemetry 将应用数据进行上报。若您的应用已使用 Skywalking 来采集链路，可参考本文进行零代码改造将链路数据接入 Insight。

## 代码解读

为了能兼容不同的分布式追踪实现，OpenTelemetry 提供了组件植入的方式，让不同的厂商能够经由 OpenTelemetry 标准化数据处理后输出到不同的后端。Jaeger 与 Zipkin 在社区中实现了 JaegerReceiver、ZipkinReceiver。我们也为社区贡献了 SkyWalkingReceiver，并进行了持续的打磨，现在已经具备了在生产环境中使用的条件，而且无需修改任何一行业务代码。

OpenTelemetry 与 SkyWalking 有一些共同点：都是使用 Trace 来定义一次追踪，并使用 Span 来标记追踪里的最小粒度。但是在一些细节和实现上还是会有差别：

| - | Skywalking | OpenTelemetry |
| --- | ------- | ------------ |
| 数据结构  | __span__ -> __Segment__ -> __Trace__ | __Span__ -> __Trace__ |
| 属性信息 | __Tags__ | __Attributes__ |
| 应用时间 | __Logs__ | __Events__ |
| 引用关系 | __References__ | __Links__ |

明确了这些差异后，就可以开始实现将 [SkyWalking Trace](https://skywalking.apache.org/docs/main/latest/en/protocols/trace-data-protocol-v3/) 转换为 [OpenTelemetry Trace](https://opentelemetry.io/docs/reference/specification/overview/)。主要工作包括：

1. 如何构造 OpenTelemetry 的 TraceId 和 SpanId

2. 如何构造 OpenTelemetry 的 ParentSpanId

3. 如何在 OpenTelemetry Span 中保留 SkyWalking 的原始 TraceId、SegmentId、SpanId

首先，我们来看如何构造 OpenTelemetry 的 TraceId 和 SpanId。SkyWalking 和 OpenTelemetry 都是通过 TraceId 串联起各个分布式服务调用，并通过 SpanId 来标记每一个 Span，但是实现规格有较大差异：

> 代码实现见 GitHub：
>
> 1. https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L54
> 2. https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/8107
> 3. https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/8549

具体来讲，SkyWalking TraceId 和 SegmentId 所有可能的格式如下：

![sw2otel-01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/sw2otel-01.png)

其中，在 OpenTelemetry 协议里，Span 在所有 Trace 中都是唯一的，而在 SkyWalking 中，Span 仅在每个 Segment 里是唯一的，这说明要通过 SegmentId 与 SpanId 结合才能在 SkyWalking 中对 Span 做唯一标识，并转换为 OpenTelemetry 的 SpanId。

> 代码实现见 GitHub：
>
> 1. https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L272
> 2. https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/11562

接下来，我们来看如何构造 OpenTelemetry 的 ParentSpanId。在一个 Segment 内部，SkyWalking 的 ParentSpanId 字段可直接用于构造 OpenTelemetry 的 ParentSpanId 字段。但当一个 Trace 跨多个 Segment 时，SkyWalking 是通过 Reference 中的 ParentTraceSegmentId 和 ParentSpanId 表示的关联信息，于是此时需要通过 Reference 中的信息构建 OpenTelemetry 的 ParentSpanId。

> 代码实现见 GitHub：https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L173

最后，我们来看如何在 OpenTelemetry Span 中保留 SkyWalking 的原始 TraceId、SegmentId、SpanId。我们携带这些原始信息是为了能将分布式追踪后端展现的 OpenTelemetry TraceId、SpanId 与应用程序日志中的 SkyWalking TraceId、SegmentId、SpanId 进行关联，打通追踪和日志。我们选择将 SkyWalking 中原有的 TraceId、SegmentId、ParentSegmentId 携带到 OpenTelemetry Attributes 中。

> 代码实现见 GitHub：
>
> 1. https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L201
> 2. https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/12651

经过上述一系列转换后，我们将 SkyWalking Segment Object 完整的转换为了 OpenTelmetry Trace，如下图：

![sw2otel-02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/sw2otel-02.png)

## 部署 Demo

下面我们以一个 Demo 来展示使用 OpenTelemetry 收集、展示 SkyWalking 追踪数据的完整过程。

首先，在部署 OpenTelemetry Agent 之后，开启如下配置，即可在  OpenTelemetry 中拥有兼容 SkyWalking 协议的能力：

```yaml
# otel-agent config
receivers:
  # add the following config
  skywalking:
    protocols:
      grpc:
        endpoint: 0.0.0.0:11800 # 接收 SkyWalking Agent 上报的 Trace 数据
      http: 
        endpoint: 0.0.0.0:12800 # 接收从前端/ nginx 等 HTTP 协议上报的 Trace 数据
service: 
  pipelines: 
    traces:      
      # add receiver __skywalking__ 
      receivers: [skywalking]
      
# otel-agent service yaml
spec:
  ports: 
    - name: sw-http
      port: 12800    
      protocol: TCP    
      targetPort: 12800 
    - name: sw-grpc     
      port: 11800 
      protocol: TCP  
      targetPort: 11800
```

接下来需要将业务应用对接的 SkyWalking OAP Service（如 oap:11800）修改为 OpenTelemetry Agent Service（如 otel-agent:11800），就可以开始使用 OpenTelemetry 接收 SkyWalking 探针的追踪数据了。

我们以 SkyWalking-showcase Demo 为例展示整个效果。它使用 SkyWalking Agent 做追踪，通过 OpenTelemetry 标准化处理后使用 Jaeger 来呈现最终效果：

![sw2otel-03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/sw2otel-03.png)

通过 SkyWalking Showcase 的架构图，可知 SkyWalking 的数据经过 OpenTelemetry 标准化后，依然完整。在这个 Trace 里，请求从 app/homepage 发起，之后在 app 同时发起两个请求 /rcmd/与/songs/top，分发到 recommandation/songs 两个服务中，并最终到达数据库进行查询，从而完成整个请求链路。

![sw2otel-04](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/sw2otel-04.png)

另外，我们也可从 Jaeger 页面中查看到原始 SkyWalking Id 信息，便于与应用日志关联：

![sw2otel-05](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/sw2otel-05.png)
