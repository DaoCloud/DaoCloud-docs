# Expose metrics for applications using OTel SDK

> This page is intended as a reference only for users wishing to evaluate or explore OTLP metrics under development.

The OpenTelemetry project requires APIs and SDKs to be available in languages ​​that must emit data in the OpenTelemetry Protocol (OTLP).

## For Golang applications

Golang can expose runtime metrics through sdk. Specifically, add the following method to the application to enable the metrics exposer:

### Install related dependencies

After switching/going into the application source folder run the following command:

```golang
go get go.opentelemetry.io/otel\
  go.opentelemetry.io/otel/attribute\
  go.opentelemetry.io/otel/exporters/prometheus \
  go.opentelemetry.io/otel/metric/global\
  go.opentelemetry.io/otel/metric/instrument \
  go.opentelemetry.io/otel/sdk/metric
```

### Create an initialization feature using the OpenTelemetry SDK

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

The above method will expose a metrics interface for your application: http://localhost:8888/metrics

Then, initialize it in main.go:

```golang

func main() {
······
    tp := initMeter()
······
}
```

In addition, if you want to add custom metrics, you can refer to:

```golang
// exposeClusterMetric expose metric like "insight_logging_count{} 1"
func (s *insightServer) exposeLoggingMetric(lserver *log. LogService) {
    s.meter = global.Meter("insight.io/basic")

    var lock sync.Mutex
    logCounter, err := s.meter.AsyncFloat64().Counter("insight_log_total")
    if err != nil {
        zap.S().Panicf("failed to initialize instrument: %v", err)
    }
 
    _ = s.meter.RegisterCallback([]instrument.Asynchronous{logCounter}, func(ctx context.Context) {
        lock. Lock()
        defer lock. Unlock()
        count, err := lserver. Count(ctx)
        if err == nil || count != -1 {
            logCounter. Observe(ctx, float64(count))
        }
    })
}
```

Then, call the method in main.go:

```golang
······
s. exposeLoggingMetric(lservice)
······
```

You can check that your metrics are working by visiting http://localhost:8888/metrics.

## For Java applications

On the basis of using otel agent to complete the automatic connection of the link, Java adds environment variables:

```bash
OTEL_METRICS_EXPORTER=prometheus
```

You can directly expose JVM related metrics, you can check if your metrics are working by visiting http://localhost:8888/metrics.

Then, cooperate with prometheus serviceMonitor to complete the access of metrics.
See [opentelemetry-java-docs/prometheus](https://github.com/open-telemetry/opentelemetry-java-docs/blob/main/prometheus/README.md) if you want to expose custom metrics.

Mainly divided into the following two steps:

- Create a meter provider and specify prometheus as exporter.

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

- Customize meter and open http server

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
        Meter meter = meterProvider. get("PrometheusExample");
        meter
            .gaugeBuilder("incoming. messages")
            .setDescription("No of incoming messages awaiting processing")
            .setUnit("message")
            .buildWithCallback(result -> result.record(incomingMessageCount, Attributes.empty()));
      }

      void simulate() {
        for (int i = 500; i > 0; i--) {
          try {
            System.out.println(
                i + " Iterations to go, current incomingMessageCount is: " + incomingMessageCount);
            incomingMessageCount = ThreadLocalRandom.current().nextLong(100);
            Thread. sleep(1000);
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

        prometheusExample. simulate();

        System.out.println("Exiting");
      }
    }
    ```

Then, after the java application is running, you can check that your metrics are working by visiting http://localhost:8888/metrics.

## Insight collection metrics

Last but not least, you have exposed metrics in your application and now you need Insight to collect them.

The recommended way to expose metrics is via [servicemonitor](https://github.com/prometheus-operator/prometheus-operator/blob/501d079e3d3769b94dca6684cf155034e468829a/Documentation/design.md#servicemonitor) or podmonitor.

### Create servicemonitor/podmonitor

The added servicemonitor/podmonitor needs to be marked with __label: "operator.insight.io/managed-by": "insight"__ 
to be recognized by the Operator:

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
