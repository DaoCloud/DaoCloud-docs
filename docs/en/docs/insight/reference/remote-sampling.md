# Create a Remote Sampling Server

The insight-agent chart supports creating a [Jaeger's Remote Sampling Server](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/jaegerremotesampling).
The OTel SDK or Agent can connect to this Remote Sampling Server by configuring `sampler: jaeger_remote`.

## Enable Jaeger's Remote Sampling Server

When installing or upgrading the insight-agent chart, add `--set global.jaegerRemoteSamplingServer.enabled=true` to enable this capability.

Once enabled, the `insight-agent-remote-sampling-server-collector` Deployment is created, which exposes two ports:

- 5778: http-sampling
- 14250: grpc-sampling

Access the sampling rules of a specific service through the API `http://insight-agent-remote-sampling-server-collector:5778/sampling?service=local-adservice`.

In addition, the ConfigMap `insight-agent-sampling-strategies-config` is delivered, which defines a default sampling rule.
__The sampling server supports hot reloading of this ConfigMap__:

```json
{
  "service_strategies": [
    {
      "service": "foo",
      "type": "probabilistic",
      "param": 0.1,
      "operation_strategies": [
        {
          "operation": "op1",
          "type": "probabilistic",
          "param": 0.2
        },
        {
          "operation": "op2",
          "type": "probabilistic",
          "param": 0.4
        }
      ]
    }
  ],
  "default_strategy": {
    "type": "probabilistic",
    "param": 0.5,
    "operation_strategies": [
      {
        "operation": "/health",
        "type": "probabilistic",
        "param": 0.0
      },
      {
        "operation": "/metrics",
        "type": "probabilistic",
        "param": 0.0
      }
    ]
  }
}
```

`type` supports:

- probabilistic
- ratelimiting

For details, see [Collector Sampling Configuration](https://www.jaegertracing.io/docs/1.28/architecture/sampling/#collector-sampling-configuration).


## Connect the OTel SDK or Agent to the jaeger_remote Sampler

After you enable this capability in insight-agent, you still need to configure the OTel SDK or Agent for the sampling rules of the corresponding service to take effect.

First, add the following two environment variables to the OTel SDK or Agent:

```yaml
      - name: OTEL_TRACES_SAMPLER
        value: jaeger_remote
      - name: OTEL_TRACES_SAMPLER_ARG
        value: endpoint=http://insight-agent-remote-sampling-server-collector:5778/sampling,pollingIntervalMs=5000,initialSamplingRate=0.25
```

You can add them directly to the Deployment of the specific service, or configure them in advance in `Instrumentation/insight-opentelemetry-autoinstrumentation` so that the OpenTelemetry Operator adds them during auto-instrumentation.
You can also add these two environment variables together while enabling the Remote Sampling Server through Helm. First, obtain your current insight-agent values and add the following at the path below:

```yaml
global:
  instrumentationCR:
    spec:
      env: 
        # Add these two environment variables to the existing ones
        - name: OTEL_TRACES_SAMPLER
          value: jaeger_remote
        - name: OTEL_TRACES_SAMPLER_ARG
          value: endpoint=http://insight-agent-remote-sampling-server-collector:5778/sampling,pollingIntervalMs=5000,initialSamplingRate=0.25
```

Save the new values as the file new-values.yaml,
and then run `helm upgrade ... --set global.jaegerRemoteSamplingServer.enabled=true -f new-values.yaml` when upgrading.

Then adjust the OTel SDK or Agent according to the programming language. The configuration differs by language, so only Java and Golang are described here.

### Java

For Java applications, you only need to restart the Pod on which the OTel Agent is enabled.

### Golang

For Golang applications, you need to reconfigure the OTel SDK and add `jaegerRemoteSampler`:

```shell
go install go.opentelemetry.io/contrib/samplers/jaegerremote
```

```go
	jaegerRemoteSampler := jaegerremote.New(
		"your-service-name",
		jaegerremote.WithSamplingServerURL("http://{sampling_service_host_name}:5778/sampling"),
		jaegerremote.WithSamplingRefreshInterval(10*time.Second),
		jaegerremote.WithInitialSampler(trace.TraceIDRatioBased(0.5)),
	)

	tp := trace.NewTracerProvider(
		trace.WithSampler(jaegerRemoteSampler),
		...
	)
	otel.SetTracerProvider(tp)
```

Finally, restart the program.
