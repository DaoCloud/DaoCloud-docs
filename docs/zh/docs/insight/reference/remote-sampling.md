# Remote Sampling Server

insight-agent chart 支持创建一个 [Jaeger's Remote Sampling Server](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/jaegerremotesampling).
OTel SDK 或者 Agent 可以通过配置 sampler:  `jaeger_remote` 连接到这个 Remote Sampling Server.

## 开启 Jaeger's Remote Sampling Server

在安装或者升级 insight-agent chart 时，添加 `--set global.jaegerRemoteSamplingServer.enabled=true` 开启这个能力。

在成功后会部署 `insight-agent-remote-sampling-server-collector` Deployment, 它会暴露两个端口：

- 5778: http-sampling
- 14250: grpc-sampling

通过 API: `http://insight-agent-remote-sampling-server-collector:5778/sampling?service=local-adservice` 访问特定服务的采样规则。

此外，还会下发 ConfigMap `insight-agent-sampling-strategies-config`, 它定义了一个默认的采样规则, **采样服务器支持热加载这个 ConfigMap**：
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

其中 type 支持：

- probabilistic
- ratelimiting


详细的说明见：[Collector Sampling Configuration](https://www.jaegertracing.io/docs/1.28/architecture/sampling/#collector-sampling-configuration).


## OTel SDK 或 Agent 连接 jaeger_remote sampler

在 Insight-agent 开启这个功能后，还需要对 OTel SDK 或 Agent 进行一些配置才能时对应服务的采样规则生效。

首先是给 OTel SDK 或 Agent 添加以下两个环境变量：

```yaml
      - name: OTEL_TRACES_SAMPLER
        value: jaeger_remote
      - name: OTEL_TRACES_SAMPLER_ARG
        value: endpoint=http://insight-agent-remote-sampling-server-collector:5778/sampling,pollingIntervalMs=5000,initialSamplingRate=0.25
```

可以直接在具体服务 Deployment 上添加，或者在 `Instrumentation/insight-opentelemetry-autoinstrumentation` 提前配置好并由 opentelemetry operator 在自动注入时添加。
我们可以在通过 Helm 开启 Remote Sampling Server 的同时将这个两个环境变量一并完成添加。首先获取你当前 Insight-agent  Values 并在以下路径添加：

```yaml
global:
  instrumentationCR:
    spec:
      env: 
        # 在原来的环境变量上补充这两个环境变量
        - name: OTEL_TRACES_SAMPLER
          value: jaeger_remote
        - name: OTEL_TRACES_SAMPLER_ARG
          value: endpoint=http://insight-agent-remote-sampling-server-collector:5778/sampling,pollingIntervalMs=5000,initialSamplingRate=0.25
```

将新的 values 保存为文件：new-values.yaml 然后在升级时 `helm upgrade ... --set global.jaegerRemoteSamplingServer.enabled=true -f new-values.yaml`。

然后是根据编程语言调整 OTel SDK 或 Agent，不同语言配置方式不同，这里只说明 Java 和 Golang。

### Java

对于 Java 应用，只需要重启开启了 OTel Agent 的 Pod.

### Golang

Golang 应用需要重新配置 OTel SDK：添加 `jaegerRemoteSampler`:

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

重启程序即可。