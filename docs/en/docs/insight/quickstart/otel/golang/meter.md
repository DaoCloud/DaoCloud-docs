---
MTPE: windsonsea
Date: 2024-10-16
---

# Exposing Metrics for Applications Using OpenTelemetry SDK

> This article is intended for users who wish to evaluate or explore the developing OTLP metrics.

The OpenTelemetry project requires that APIs and SDKs must emit data in the OpenTelemetry Protocol (OTLP) for supported languages.

## For Golang Applications

Golang can expose runtime metrics through the SDK by adding the following methods to enable the metrics exporter within the application:

### Install Required Dependencies

Navigate to your application’s source folder and run the following command:

```bash
go get go.opentelemetry.io/otel \
  go.opentelemetry.io/otel/attribute \
  go.opentelemetry.io/otel/exporters/prometheus \
  go.opentelemetry.io/otel/metric/global \
  go.opentelemetry.io/otel/metric/instrument \
  go.opentelemetry.io/otel/sdk/metric
```

### Create an Initialization Function Using OTel SDK

```go
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

The above method will expose a metrics endpoint for your application at: `http://localhost:8888/metrics`.

Next, initialize it in `main.go`:

```go
func main() {
    // ...
    tp := initMeter()
    // ...
}
```

If you want to add custom metrics, you can refer to the following:

```go
// exposeClusterMetric exposes a metric like "insight_logging_count{} 1"
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

Then, call this method in `main.go`:

```go
// ...
s.exposeLoggingMetric(lservice)
// ...
```

You can check if your metrics are working correctly by visiting `http://localhost:8888/metrics`.

## For Java Applications

For Java applications, you can directly expose JVM-related metrics by using the OpenTelemetry agent with the following environment variable:

```bash
OTEL_METRICS_EXPORTER=prometheus
```

You can then check your metrics at `http://localhost:8888/metrics`.

Next, combine it with a Prometheus `ServiceMonitor` to complete the metrics integration. If you want to expose custom metrics, please refer to [opentelemetry-java-docs/prometheus](https://github.com/open-telemetry/opentelemetry-java-docs/blob/main/prometheus/README.md).

The process is mainly divided into two steps:

- Create a meter provider and specify Prometheus as the exporter.

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
   * Initializes the Meter SDK and configures the Prometheus collector with all default settings.
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

- Create a custom meter and start the HTTP server.

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

    // It is important to initialize the OpenTelemetry SDK as early as possible in your process.
    MeterProvider meterProvider = ExampleConfiguration.initializeOpenTelemetry(prometheusPort);

    PrometheusExample prometheusExample = new PrometheusExample(meterProvider);

    prometheusExample.simulate();

    System.out.println("Exiting");
  }
}
```

After running the Java application, you can check if your metrics are working correctly by visiting `http://localhost:8888/metrics`.

## Insight Collecting Metrics

Lastly, it is important to note that you have exposed metrics in your application, and now you need Insight to collect those metrics.

The recommended way to expose metrics is via [ServiceMonitor](https://github.com/prometheus-operator/prometheus-operator/blob/501d079e3d3769b94dca6684cf155034e468829a/Documentation/design.md#servicemonitor) or PodMonitor.

### Creating ServiceMonitor/PodMonitor

The added ServiceMonitor/PodMonitor needs to have the label `operator.insight.io/managed-by: insight` for the Operator to recognize it:

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
