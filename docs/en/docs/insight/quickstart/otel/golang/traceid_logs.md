# Writing TraceId and SpanId into Golang Application Logs

This article explains how to write TraceId and SpanId into Golang application logs using OpenTelemetry.
After TraceId and SpanId are written into the logs, you can correlate distributed trace data with log data for more efficient fault diagnosis and performance analysis.

## Install Related Dependencies

If you have already integrated them by following [Enhance Go Applications with OTel SDK](./golang.md), you can skip this step.

```bash
$ go get go.opentelemetry.io/otel/trace
```

## Extract TraceContext Metadata from the Context

The `SpanContextFromContext` function of the OpenTelemetry Trace API extracts TraceContext metadata from the context.
`Context` and returns it as a `SpanContext`. The following example demonstrates how to use this function:

```golang
spanContext := trace.SpanContextFromContext(ctx)
if !spanContext.IsValid() {
        // ctx does not contain a valid span.
        // There is no trace metadata to add.
        return
}
```

The `SpanContext` struct contains the traceID and SpanID, trace flags with sampling information, and state information. You can add this metadata to log events to enrich their context and correlate traces with logs.

## Annotate Log Events

After collecting metadata in the `SpanContext`, you can use it to annotate log events.

### Structured Logs

If you use a structured logger, add the Trace metadata as fields. The following example shows how to annotate log events using the zap logging library:

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

### Unstructured Logs

If you use unstructured logging, you can add the trace metadata as part of the log message. The following example shows how to add trace metadata using the standard library log package (`log`):

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

### Log Annotation Example

The following is a complete example of a `chi` server that extracts trace metadata and annotates the log messages of processed requests:

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

Run the above demo:
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

Afterward, visit `http://localhost:8080/hello` and you will find that the Golang application prints log content as follows, which contains the trace_id and span_id.

```json
{"level":"info","ts":1744102088.9999301,"caller":"go-trace-logs/main.go:108","msg":"request handled","trace_id":"c9fc5dda54cc3c3092911e734e7008ee","span_id":"89b2f138025bc9c2","trace_flags":"01","response_bytes":13}
```

## References
- [Connect Go trace data with logs](https://github.com/openinsight-proj/opentelemetry-go-extra/tree/main/go-trace-logs)
- [OpenTelemetry in Go](https://opentelemetry.io/docs/languages/go/)
