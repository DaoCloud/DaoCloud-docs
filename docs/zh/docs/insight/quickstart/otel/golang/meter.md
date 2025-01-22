# 使用 OTel SDK 为应用程序暴露指标

> 本文仅供希望评估或探索正在开发的 OTLP 指标的用户参考。

OpenTelemetry 项目要求以必须在 OpenTelemetry 协议 (OTLP) 中发出数据的语言提供 API 和 SDK。

## 针对 Golang 应用程序

Golang 可以通过 sdk 暴露 runtime 指标，具体来说，在应用中添加以下方法开启 metrics 暴露器：

### 安装相关依赖

切换/进入到应用程序源文件夹后运行以下命令：

```golang
go get go.opentelemetry.io/otel \
  go.opentelemetry.io/otel/attribute \
  go.opentelemetry.io/otel/exporters/prometheus \
  go.opentelemetry.io/otel/metric/global \
  go.opentelemetry.io/otel/metric/instrument \
  go.opentelemetry.io/otel/sdk/metric
```

### 使用 OTel SDK 创建初始化函数

```golang
import (
    .....

    "go.opentelemetry.io/otel/attribute"
    otelPrometheus "go.opentelemetry.io/otel/exporters/prometheus"
    "go.opentelemetry.io/otel/metric/global"
    "go.opentelemetry.io/otel/metric/instrument"
    "go.opentelemetry.io/otel/sdk/metric/aggregator/histogram"
    controller "go.opentelemetry.io/otel/sdk/metric/controller/basic"
    "go.opentelemetry.io/otel/sdk/metric/export/aggregation"
    processor "go.opentelemetry.io/otel/sdk/metric/processor/basic"
    selector "go.opentelemetry.io/otel/sdk/metric/selector/simple"
)
func (s *insightServer) initMeter() *otelPrometheus.Exporter {
    s.meter = global.Meter("xxx")

    config := otelPrometheus.Config{
        DefaultHistogramBoundaries: []float64{1, 2, 5, 10, 20, 50},
        Gatherer:                   prometheus.DefaultGatherer,
        Registry:                   prometheus.NewRegistry(),
        Registerer:                 prometheus.DefaultRegisterer,
    }

    c := controller.New(
        processor.NewFactory(
            selector.NewWithHistogramDistribution(
                histogram.WithExplicitBoundaries(config.DefaultHistogramBoundaries),
            ),
            aggregation.CumulativeTemporalitySelector(),
            processor.WithMemory(true),
        ),
    )

    exporter, err := otelPrometheus.New(config, c)
    if err != nil {
        zap.S().Panicf("failed to initialize prometheus exporter %v", err)
    }

    global.SetMeterProvider(exporter.MeterProvider())

    http.HandleFunc("/metrics", exporter.ServeHTTP)

    go func() {
        _ = http.ListenAndServe(fmt.Sprintf(":%d", 8888), nil)
    }()

    zap.S().Info("Prometheus server running on ", fmt.Sprintf(":%d", port))
    return exporter
}
```

以上方法会为您的应用暴露一个指标接口: http://localhost:8888/metrics

随后，在 main.go 中对其进行初始化：

```golang
func main() {
······
    tp := initMeter()
······
}
```

此外，如果想添加自定义指标，可以参考：

```golang
// exposeClusterMetric expose metric like "insight_logging_count{} 1"
func (s *insightServer) exposeLoggingMetric(lserver *log.LogService) {
    s.meter = global.Meter("insight.io/basic")

    var lock sync.Mutex
    logCounter, err := s.meter.AsyncFloat64().Counter("insight_log_total")
    if err != nil {
        zap.S().Panicf("failed to initialize instrument: %v", err)
    }
 
    _ = s.meter.RegisterCallback([]instrument.Asynchronous{logCounter}, func(ctx context.Context) {
        lock.Lock()
        defer lock.Unlock()
        count, err := lserver.Count(ctx)
        if err == nil || count != -1 {
            logCounter.Observe(ctx, float64(count))
        }
    })
}
```

随后，在 main.go 调用该方法：

```golang
······
s.exposeLoggingMetric(lservice)
······
```

您可以通过访问 http://localhost:8888/metrics 来检查您的指标是否正常工作。

## 针对 Java 应用程序

Java 在使用 otel agent 在完成链路的自动接入的基础上，通过添加环境变量：

```bash
OTEL_METRICS_EXPORTER=prometheus
```

就可以直接暴露 JVM 相关指标，您可以通过访问 http://localhost:8888/metrics 来检查您的指标是否正常工作。

随后，再配合 prometheus serviceMonitor 即可完成指标的接入。
如果想暴露自定义指标请参阅 [opentelemetry-java-docs/prometheus](https://github.com/open-telemetry/opentelemetry-java-docs/blob/main/prometheus/README.md)。

主要分以下两步：

- 创建 meter provider，并指定 prometheus 作为 exporter。

    ```java
    /*
    * Copyright The OpenTelemetry Authors
    * SPDX-License-Identifier: Apache-2.0
    */

    package io.opentelemetry.example.prometheus;

    import io.opentelemetry.api.metrics.MeterProvider;
    import io.opentelemetry.exporter.prometheus.PrometheusHttpServer;
    import io.opentelemetry.sdk.metrics.SdkMeterProvider;
    import io.opentelemetry.sdk.metrics.export.MetricReader;

    public final class ExampleConfiguration {
    
      /**
      * Initializes the Meter SDK and configures the prometheus collector with all default settings.
      *
      * @param prometheusPort the port to open up for scraping.
      * @return A MeterProvider for use in instrumentation.
      */
      static MeterProvider initializeOpenTelemetry(int prometheusPort) {
        MetricReader prometheusReader = PrometheusHttpServer.builder().setPort(prometheusPort).build();
    
        return SdkMeterProvider.builder().registerMetricReader(prometheusReader).build();
      }
    }

    ```

- 自定义 meter 并开启 http server

    ```java
    package io.opentelemetry.example.prometheus;

    import io.opentelemetry.api.common.Attributes;
    import io.opentelemetry.api.metrics.Meter;
    import io.opentelemetry.api.metrics.MeterProvider;
    import java.util.concurrent.ThreadLocalRandom;

    /**
    * Example of using the PrometheusHttpServer to convert OTel metrics to Prometheus format and expose
    * these to a Prometheus instance via a HttpServer exporter.
    *
    * <p>A Gauge is used to periodically measure how many incoming messages are awaiting processing.
    * The Gauge callback gets executed every collection interval.
    */
    public final class PrometheusExample {
      private long incomingMessageCount;

      public PrometheusExample(MeterProvider meterProvider) {
        Meter meter = meterProvider.get("PrometheusExample");
        meter
            .gaugeBuilder("incoming.messages")
            .setDescription("No of incoming messages awaiting processing")
            .setUnit("message")
            .buildWithCallback(result -> result.record(incomingMessageCount, Attributes.empty()));
      }

      void simulate() {
        for (int i = 500; i > 0; i--) {
          try {
            System.out.println(
                i + " Iterations to go, current incomingMessageCount is:  " + incomingMessageCount);
            incomingMessageCount = ThreadLocalRandom.current().nextLong(100);
            Thread.sleep(1000);
          } catch (InterruptedException e) {
            // ignored here
          }
        }
      }

      public static void main(String[] args) {
        int prometheusPort = 8888;

        // it is important to initialize the OpenTelemetry SDK as early as possible in your process.
        MeterProvider meterProvider = ExampleConfiguration.initializeOpenTelemetry(prometheusPort);

        PrometheusExample prometheusExample = new PrometheusExample(meterProvider);

        prometheusExample.simulate();

        System.out.println("Exiting");
      }
    }
    ```

随后，待 java 应用程序运行之后，您可以通过访问 http://localhost:8888/metrics 来检查您的指标是否正常工作。

## Insight 采集指标

最后重要的是，您已经在应用程序中暴露出了指标，现在需要 Insight 来采集指标。

推荐的指标暴露方式是通过 [servicemonitor](https://github.com/prometheus-operator/prometheus-operator/blob/501d079e3d3769b94dca6684cf155034e468829a/Documentation/design.md#servicemonitor) 或者 podmonitor。

### 创建 servicemonitor/podmonitor

添加的 servicemonitor/podmonitor 需要打上 __label："operator.insight.io/managed-by": "insight"__ 才会被 Operator 识别：

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: example-app
  labels:
    operator.insight.io/managed-by: insight
spec:
  selector:
    matchLabels:
      app: example-app
  endpoints:
  - port: web
  namespaceSelector:
    any: true
```
