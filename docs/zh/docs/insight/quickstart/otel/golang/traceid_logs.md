# 将 TraceId 和 SpanId 写入 Golang 应用日志

本文介绍如何使用 OpenTelemetry 将 TraceId 和 SpanId 写入 Golang 应用日志。
TraceId 与 SpanId 写入日志后，您可以将分布式链路数据与日志数据关联起来，实现更高效的故障诊断和性能分析。

## 安装相关依赖
如果你已经按照 [使用 OTel SDK 增强 Go 应用程序](./golang.md) 的方式引入过，则可跳过该步骤。

```bash
$ go get go.opentelemetry.io/otel/trace
```

## 从上下文中提取 TraceContext 元数据

OpenTelemetry Trace API 的 `SpanContextFromContext` 函数从上下文中提取 TraceContext 元数据。`Context` 并以 `SpanContext` 的形式返回它。以下示例演示如何使用该函数：

```golang
spanContext := trace.SpanContextFromContext(ctx)
if !spanContext.IsValid() {
        // ctx does not contain a valid span.
        // There is no trace metadata to add.
        return
}
```

`SpanContext` 结构包含 traceID 和 SpanID、带有采样信息的跟踪标志以及状态信息。您可以将此元数据添加到日志事件中，以丰富其上下文，并关联跟踪和日志。

## 注释日志事件

在 `SpanContext` 中收集元数据后，您可以使用它来注释日志事件。

### 结构化日志

如果您使用的是结构化记录器(structured logger)，请将 Trace 元数据添加为字段。以下示例显示如何使用 zap 日志记录库对日志事件进行注释：

```golang
logger, _ := zap.NewProduction()
defer logger.Sync()
logger = logger.With(
        zap.String("trace_id", spanContext.TraceID().String()),
        zap.String("span_id", spanContext.SpanID().String()),
        zap.String("trace_flags", spanContext.TraceFlags().String()),
)
logger.Info("Failed to fetch URL", zap.String("URL", url))
```

### 非结构化日志
如果您使用的是非结构化日志记录，则可以将跟踪元数据添加为记录消息的一部分。以下示例显示如何使用标准库日志包(`log`) 添加跟踪元数据：

```golang
// Add the metadata following an order you can parse later on
log.Printf(
        "(trace_id: %s, span_id: %s, trace_flags: %s): failed to fetch URL: %s",
        spanContext.TraceID().String(),
        spanContext.SpanID().String(),
        spanContext.TraceFlags().String(),
        url,
)
```

### 日志注释示例
以下是提取跟踪元数据并为已处理请求的日志消息添加注释的 `chi` 服务器的完整示例：

```golang
package main

import (
        "context"
        "net/http"

        "github.com/go-chi/chi"
        "github.com/signalfx/splunk-otel-go/instrumentation/github.com/go-chi/chi/splunkchi"
        "go.opentelemetry.io/otel/trace"
        "go.uber.org/zap"
)

func withTraceMetadata(ctx context.Context, logger *zap.Logger) *zap.Logger {
        spanContext := trace.SpanContextFromContext(ctx)
        if !spanContext.IsValid() {
                // ctx does not contain a valid span.
                // There is no trace metadata to add.
                return logger
        }
        return logger.With(
                zap.String("trace_id", spanContext.TraceID().String()),
                zap.String("span_id", spanContext.SpanID().String()),
                zap.String("trace_flags", spanContext.TraceFlags().String()),
        )
}

func helloHandler(logger *zap.Logger) http.HandlerFunc {
        return func(w http.ResponseWriter, r *http.Request) {
                l := withTraceMetadata(r.Context(), logger)

                n, err := w.Write([]byte("Hello World!\n"))
                if err != nil {
                        w.WriteHeader(http.StatusInternalServerError)
                        l.Error("failed to write request response", zap.Error(err))
                } else {
                        l.Info("request handled", zap.Int("response_bytes", n))
                }
        }
}

func main() {
        logger, err := zap.NewProduction()
        if err != nil {
                panic(err)
        }
        defer logger.Sync()

        router := chi.NewRouter()
        router.Use(splunkchi.Middleware())
        router.Get("/hello", helloHandler(logger))
        if err := http.ListenAndServe(":8080", router); err != nil {
                panic(err)
        }
}
```

运行以上 demo:
```bash
$ go get github.com/signalfx/splunk-otel-go/instrumentation/github.com/go-chi/chi/splunkchi \
          github.com/go-chi/chi \
          go.opentelemetry.io/otel/trace \
          go.uber.org/zap \
          go.opentelemetry.io/otel \ 
          go.opentelemetry.io/otel/sdk/trace \
          go.opentelemetry.io/otel/exporters/otlp/otlptrace \
          go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc \
          go get go.opentelemetry.io/otel/semconv/v1.7.0
$ go run .                                 
```

随后，访问 `http://localhost:8080/hello` 即可发现 golang 应用程序打印日志内容如下，其中包含了 trace_id 和 span_id。

```json
{"level":"info","ts":1744102088.9999301,"caller":"go-trace-logs/main.go:108","msg":"request handled","trace_id":"c9fc5dda54cc3c3092911e734e7008ee","span_id":"89b2f138025bc9c2","trace_flags":"01","response_bytes":13}
```

## 参考
- [Connect Go trace data with logs](https://github.com/openinsight-proj/opentelemetry-go-extra/tree/main/go-trace-logs)
- [OpenTelemetry in Go](https://opentelemetry.io/docs/languages/go/)