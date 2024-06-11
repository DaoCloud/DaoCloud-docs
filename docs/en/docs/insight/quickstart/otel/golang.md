# Enhance Go applications with OTel SDK

This page contains instructions on how to set up OpenTelemetry enhancements in a Go application.

OpenTelemetry, also known simply as OTel, is an open-source observability framework that helps generate and collect telemetry data: traces, metrics, and logs in Go apps.

## Enhance Go apps with the OpenTelemetry SDK

### Install related dependencies

Dependencies related to the OpenTelemetry exporter and SDK must be installed first. If you are using another request router, please refer to [request routing](#request-routing).
After switching/going into the application source folder run the following command:

```golang
go get go.opentelemetry.io/otel@v1.8.0 \
  go.opentelemetry.io/otel/trace@v1.8.0 \
  go.opentelemetry.io/otel/sdk@v1.8.0 \
  go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin@v0.33.0 \
  go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.7.0 \
  go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.4.1
```

### Create an initialization feature using the OpenTelemetry SDK

In order for an application to be able to send data, a feature is required to initialize OpenTelemetry. Add the following code snippet to the __main.go__ file:

```golang
import (
	"context"
	"os"
	"time"

	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.7.0"
	"go.uber.org/zap"
	"google.golang.org/grpc"
)

var tracerExp *otlptrace.Exporter

func retryInitTracer() func() {
	var shutdown func()
	go func() {
		for {
			// otel will reconnected and re-send spans when otel col recover. so, we don't need to re-init tracer exporter.
			if tracerExp == nil {
				shutdown = initTracer()
			} else {
				break
			}
			time.Sleep(time.Minute * 5)
		}
	}()
	return shutdown
}

func initTracer() func() {
	// temporarily set timeout to 10s
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	serviceName, ok := os.LookupEnv("OTEL_SERVICE_NAME")
	if !ok {
		serviceName = "server_name"
		os.Setenv("OTEL_SERVICE_NAME", serviceName)
	}
	otelAgentAddr, ok := os.LookupEnv("OTEL_EXPORTER_OTLP_ENDPOINT")
	if !ok {
		otelAgentAddr = "http://localhost:4317"
		os.Setenv("OTEL_EXPORTER_OTLP_ENDPOINT", otelAgentAddr)
	}
	zap.S().Infof("OTLP Trace connect to: %s with service name: %s", otelAgentAddr, serviceName)

	traceExporter, err := otlptracegrpc.New(ctx, otlptracegrpc.WithInsecure(), otlptracegrpc.WithDialOption(grpc.WithBlock()))
	if err != nil {
		handleErr(err, "OTLP Trace gRPC Creation")
		return nil
	}

	tracerProvider := sdktrace.NewTracerProvider(
		sdktrace.WithBatcher(traceExporter),
		sdktrace.WithSampler(sdktrace.AlwaysSample()),
    sdktrace.WithResource(resource.NewWithAttributes(semconv.SchemaURL)))

	otel.SetTracerProvider(tracerProvider)
	otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(propagation.TraceContext{}, propagation.Baggage{}))

	tracerExp = traceExporter
	return func() {
		// Shutdown will flush any remaining spans and shut down the exporter.
		handleErr(tracerProvider.Shutdown(ctx), "failed to shutdown TracerProvider")
	}
}

func handleErr(err error, message string) {
	if err != nil {
		zap.S().Errorf("%s: %v", message, err)
	}
}
```

### Initialize tracker in main.go

Modify the main feature to initialize the tracker in main.go. Also when your service shuts down, you should call __TracerProvider.Shutdown()__ to ensure all spans are exported. The service makes the call as a deferred feature in the main function:

```golang
func main() {
  	// start otel tracing
  	if shutdown := retryInitTracer(); shutdown != nil {
			defer shutdown()
		}
    ......
}
```

### Add OpenTelemetry Gin middleware to the application

Configure Gin to use the middleware by adding the following line to __main.go__ :

```golang
import (
    ....
  "go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin"
)

func main() {
    ......
    r := gin.Default()
    r.Use(otelgin.Middleware("my-app"))
    ......
}
```

### Run the application

- Local debugging and running

    > Note: This step is only used for local development and debugging. In the production environment, the Operator will automatically complete the injection of the following environment variables.

    The above steps have completed the work of initializing the SDK. Now if you need to develop and debug locally, you need to obtain the address of insight-agent-opentelemerty-collector in the insight-system namespace in advance, assuming: __insight-agent-opentelemetry-collector .insight-system.svc.cluster.local:4317__ .

    Therefore, you can add the following environment variables when you start the application locally:

    ```bash
    OTEL_SERVICE_NAME=my-golang-app OTEL_EXPORTER_OTLP_ENDPOINT=http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317 go run main.go...
    ```

- Running in a production environment 

    Please refer to the introduction of __Only injecting environment variable annotations__ in [Achieving non-intrusive enhancement of applications through Operators](./operator.md) to add annotations to deployment yaml:

    ```console
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

    If you cannot use annotations, you can manually add the following environment variables to the deployment yaml:

```yaml
······
env:
  - name: OTEL_EXPORTER_OTLP_ENDPOINT
    value: 'http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317'
  - name: OTEL_SERVICE_NAME
    value: "your depolyment name" # modify it.
  - name: OTEL_K8S_NAMESPACE
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.namespace
  - name: OTEL_RESOURCE_ATTRIBUTES_NODE_NAME
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: spec.nodeName
  - name: OTEL_RESOURCE_ATTRIBUTES_POD_NAME
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.name
  - name: OTEL_RESOURCE_ATTRIBUTES
    value: 'k8s.namespace.name=$(OTEL_K8S_NAMESPACE),k8s.node.name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME)'
······
```

## Request Routing

### OpenTelemetry gin/gonic enhancements

```golang
# Add one line to your import() stanza depending upon your request router:
middleware "go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin"
```

Then inject the OpenTelemetry middleware:

```golang
router. Use(middleware. Middleware("my-app"))
```

### OpenTelemetry gorillamux enhancements

```golang
# Add one line to your import() stanza depending upon your request router:
middleware "go.opentelemetry.io/contrib/instrumentation/github.com/gorilla/mux/otelmux"
```

Then inject the OpenTelemetry middleware:

```golang
router. Use(middleware. Middleware("my-app"))
```

### gRPC enhancements

Likewise, OpenTelemetry can help you auto-detect gRPC requests. To detect any gRPC server you have, add the interceptor to the server's instantiation.

```golang
import (
  grpcotel "go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
)
func main() {
  [...]

    s := grpc.NewServer(
        grpc.UnaryInterceptor(grpcotel.UnaryServerInterceptor()),
        grpc.StreamInterceptor(grpcotel.StreamServerInterceptor()),
    )
}
```

It should be noted that if your program uses Grpc Client to call third-party services, you also need to add an interceptor to Grpc Client:

```golang
  	[...]

	conn, err := grpc.Dial(addr, grpc.WithTransportCredentials(insecure.NewCredentials()),
		grpc.WithUnaryInterceptor(otelgrpc.UnaryClientInterceptor()),
		grpc.WithStreamInterceptor(otelgrpc.StreamClientInterceptor()),
	)
```

### If not using request routing

```golang
import (
  "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
)
```

Everywhere you pass http.Handler to ServeMux you will wrap the handler function. For example, the following replacements would be made:

```golang
- mux.Handle("/path", h)
+ mux.Handle("/path", otelhttp.NewHandler(h, "description of path"))
---
- mux.Handle("/path", http.HandlerFunc(f))
+ mux.Handle("/path", otelhttp.NewHandler(http.HandlerFunc(f), "description of path"))
```

In this way, you can ensure that each feature wrapped with othttp will automatically collect its metadata and start the corresponding trace.

## database enhancements

### Golang Gorm

The OpenTelemetry community has also developed middleware for database access libraries, such as Gorm:
```golang
import (
    "github.com/uptrace/opentelemetry-go-extra/otelgorm"
    "gorm.io/driver/sqlite"
    "gorm.io/gorm"
)

db, err := gorm.Open(sqlite.Open("file::memory:?cache=shared"), &gorm.Config{})
if err != nil {
    panic(err)
}

otelPlugin := otelgorm.NewPlugin(otelgorm.WithDBName("mydb"), # Missing this can lead to incomplete display of database related topology
    otelgorm.WithAttributes(semconv.ServerAddress("memory"))) # Missing this can lead to incomplete display of database related topology
if err := db.Use(otelPlugin); err != nil {
    panic(err)
}
```

### Custom Span

In many cases, the middleware provided by OpenTelemetry cannot help us record more internally called features, and we need to customize Span to record

```golang
 ······
	_, span := otel.Tracer("GetServiceDetail").Start(ctx,
		"spanMetricDao.GetServiceDetail",
		trace.WithSpanKind(trace.SpanKindInternal))
	defer span.End()
  ······
```

### Add custom properties and custom events to span

It is also possible to set a custom attribute or tag as a span. To add custom properties and events, follow these steps:

### Import Tracking and Property Libraries

```golang
import (
    ...
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/trace"
)
```

### Get the current Span from the context

```golang
span := trace.SpanFromContext(c.Request.Context())
```

### Set properties in the current Span

```golang
span.SetAttributes(attribute. String("controller", "books"))
```

### Add an Event to the current Span

Adding span events is done using __AddEvent__ on the span object.

```golang
span.AddEvent(msg)
```

## Log errors and exceptions

```golang
import "go.opentelemetry.io/otel/codes"

// Get the current span
span := trace.SpanFromContext(ctx)

// RecordError will automatically convert an error into a span even
span.RecordError(err)

// Flag this span as an error
span.SetStatus(codes.Error, "internal error")
```

## References

For the Demo presentation, please refer to:

- [otel-grpc-examples](https://github.com/openinsight-proj/otel-grpc-examples/tree/no-metadata-grpcgateway-v1.11.1)
- [opentelemetry-demo/productcatalogservice](https://github.com/open-telemetry/opentelemetry-demo/tree/main/src/productcatalogservice)
- [opentelemetry-collector-contrib/demo](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/examples/demo)
