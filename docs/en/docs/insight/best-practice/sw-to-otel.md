# Simplifying Trace Data Integration with OpenTelemetry and SkyWalking

This article explains how to seamlessly integrate trace data from SkyWalking into the Insight platform, using OpenTelemetry. With zero code modification required, you can transform your existing SkyWalking trace data and leverage Insight's capabilities.

## Understanding the Code Implementation

To ensure compatibility with different distributed tracing implementations, OpenTelemetry provides a way to incorporate components that standardize data processing and output to various backends. While Jaeger and Zipkin are already available, we have contributed the SkyWalkingReceiver to the OpenTelemetry community. This receiver has been refined and is now suitable for use in production environments without any modifications to your application's code.

Although SkyWalking and OpenTelemetry share similarities, such as using Trace to define a trace and Span to mark the smallest granularity, there are differences in certain details and implementations:

|         | SkyWalking     | OpenTelemetry |
|---------|----------------|---------------|
| Data Structure | Span -> Segment -> Trace | Span -> Trace |
| Attribute Information | Tags | Attributes |
| Application Time | Logs | Events |
| Reference Relationship | References | Links |

Now, let's discuss the steps involved in converting SkyWalking trace data to OpenTelemetry trace data. The main tasks include:

1. Constructing OpenTelemetry's TraceId and SpanId
2. Constructing OpenTelemetry's ParentSpanId
3. Retaining SkyWalking's original TraceId, SegmentId, and SpanId in OpenTelemetry Spans

First, let's examine how to construct OpenTelemetry's TraceId and SpanId. Although both SkyWalking and OpenTelemetry use TraceId to link distributed service calls and SpanId to identify each Span, there are significant differences in their implementation specifications. You can find the code implementation on GitHub [here](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L54).

The possible formats for SkyWalking TraceId and SegmentId are illustrated in the image below:

![sw2otel-01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/sw2otel-01.png)

In OpenTelemetry, each Span is unique within a Trace. However, in SkyWalking, a Span is only unique within each Segment. Therefore, we need to combine SegmentId and SpanId to uniquely identify Spans in SkyWalking and convert them to OpenTelemetry's SpanId. You can find the code implementation on GitHub [here](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L272).

Next, let's explore how to construct OpenTelemetry's ParentSpanId. In the case of a single Segment, SkyWalking's ParentSpanId field can be used directly to construct OpenTelemetry's ParentSpanId field. However, when a Trace spans multiple Segments, SkyWalking uses association information represented by ParentTraceSegmentId and ParentSpanId in Reference. Therefore, OpenTelemetry's ParentSpanId needs to be constructed using the information from References. You can find the code implementation on GitHub [here](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L173).

Lastly, let's discuss how to retain SkyWalking's original TraceId, SegmentId, and SpanId in OpenTelemetry Spans. By carrying this original information, we can associate OpenTelemetry's TraceId and SpanId with SkyWalking's TraceId, SegmentId, and SpanId in application logs, enabling trace and log correlation. To achieve this, we include the original TraceId, SegmentId, and ParentSegmentId of SkyWalking in OpenTelemetry Attributes. You can find the code implementation on GitHub [here](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/skywalkingreceiver/skywalkingproto_to_traces.go#L201).

Once this conversion process is complete, we have transformed the entire SkyWalking Segment Object into an OpenTelemetry Trace, as shown below:

![sw2otel-02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/sw2otel-02.png)

# Deploying the Demo

To demonstrate the complete process of collecting and displaying SkyWalking tracing data using OpenTelemetry, we will use a demo application.

First, deploy the OpenTelemetry Agent and enable the following configuration to ensure compatibility with the SkyWalking protocol:

```yaml
# otel-agent config
receivers:
  skywalking:
    protocols:
      grpc:
        endpoint: 0.0.0.0:11800 # Receive trace data reported by the SkyWalking Agent
      http: 
        endpoint: 0.0.0.0:12800 # Receive trace data reported from the front-end / nginx or other HTTP protocols
service: 
  pipelines: 
    traces:      
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

Next, modify the connection of your business application from the SkyWalking OAP Service (e.g., oap:11800) to the OpenTelemetry Agent Service (e.g., otel-agent:11800). This will allow you to start receiving trace data from the SkyWalking probe using OpenTelemetry.

To demonstrate the entire process, we will use the SkyWalking-showcase Demo. This demo utilizes the SkyWalking Agent for tracing, and after being processed by OpenTelemetry, the final results are presented using Jaeger:

![sw2otel-03](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/sw2otel-03.png)

From the architecture diagram of the SkyWalking Showcase, we can observe that the data remains intact even after standardization by OpenTelemetry. In this trace, the request starts from __app/homepage__ , then two requests __/rcmd/__ and __/songs/top__ are initiated simultaneously within the app, distributed to the __recommendation__ and __songs__ services, and finally reach the database for querying, completing the entire request chain.

![sw2otel-04](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/sw2otel-04.png)

Additionally, you can view the original SkyWalking Id information on the Jaeger page, which facilitates correlation with application logs:

![sw2otel-05](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/sw2otel-05.png)

By following these steps, you can seamlessly integrate SkyWalking trace data into OpenTelemetry and leverage the capabilities of the Insight platform.
