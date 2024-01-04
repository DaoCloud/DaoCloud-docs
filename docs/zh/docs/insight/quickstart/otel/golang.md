# 使用 OTel SDK 增强 Go 应用程序

本文包含如何在 Go 应用程序中设置 OpenTelemetry 增强的说明。

OpenTelemetry 也简称为 OTel，是一个开源的可观测性框架，可以帮助在 Go 应用程序中生成和收集遥测数据：链路、指标和日志。

## 使用 OTel SDK 增强 Go 应用

### 安装相关依赖

必须先安装与 OpenTelemetry exporter 和 SDK 相关的依赖项。如果您正在使用其他请求路由器，请参考[请求路由](#_3)。
切换/进入到应用程序源文件夹后运行以下命令：

```golang
go get go.opentelemetry.io/otel@v1.19.0 \
  go.opentelemetry.io/otel/trace@v1.19.0 \
  go.opentelemetry.io/otel/sdk@v1.19.0 \
  go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin@v0.46.1 \
  go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.19.0 \
  go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.19.0
```

### 使用 OTel SDK 创建初始化函数

为了让应用程序能够发送数据，需要一个函数来初始化 OpenTelemetry。在 __main.go__ 文件中添加以下代码片段:

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

### 在 main.go 中初始化跟踪器

修改 main 函数以在 main.go 中初始化跟踪器。另外当您的服务关闭时，应该调用 __TracerProvider.Shutdown()__ 确保导出所有 Span。该服务将该调用作为主函数中的延迟函数：

```golang
func main() {
  	// start otel tracing
  	if shutdown := retryInitTracer(); shutdown != nil {
			defer shutdown()
		}
    ......
}
```

### 为应用添加 OTel Gin 中间件

通过在 __main.go__ 中添加以下行来配置 Gin 以使用中间件:

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

### 运行应用程序

- 本地调试运行

    > 注意: 此步骤仅用于本地开发调试，生产环境中 Operator 会自动完成以下环境变量的注入。

    以上步骤已经完成了初始化 SDK 的工作，现在如果需要在本地开发进行调试，需要提前获取到 insight-system 命名空间下 insight-agent-opentelemerty-collector 的地址，假设为： __insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317__ 。

    因此，可以在你本地启动应用程序的时候添加如下环境变量：

    ```bash
    OTEL_SERVICE_NAME=my-golang-app OTEL_EXPORTER_OTLP_ENDPOINT=http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317 go run main.go...
    ```

- 生产环境运行

请参考[通过 Operator 实现应用程序无侵入增强](./operator.md) 中 __只注入环境变量注解__ 相关介绍，为 deployment yaml 添加注解：

```console
instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
```

如果无法使用注解的方式，您可以手动在 deployment yaml 添加如下环境变量：

```yaml
······
env:
  - name: OTEL_EXPORTER_OTLP_ENDPOINT
    value: 'http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317'
  - name: OTEL_SERVICE_NAME
    value: "your depolyment name" # (1)
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

1. 修改此值

## 请求路由

### OpenTelemetry gin/gonic 增强

```golang
# Add one line to your import() stanza depending upon your request router:
middleware "go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin"
```

然后注入 OpenTelemetry 中间件：

```golang
router.Use(middleware.Middleware("my-app"))
```

### OpenTelemetry gorillamux 增强

```golang
# Add one line to your import() stanza depending upon your request router:
middleware "go.opentelemetry.io/contrib/instrumentation/github.com/gorilla/mux/otelmux"
```

然后注入 OpenTelemetry 中间件：

```golang
router.Use(middleware.Middleware("my-app"))
```

### gRPC 增强

同样，OpenTelemetry 也可以帮助您自动检测 gRPC 请求。要检测您拥有的任何 gRPC 服务器，请将拦截器添加到服务器的实例化中。

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

需要注意的是，如果你的程序里面使用到了 Grpc Client 调用第三方服务，你还需要对 Grpc Client 添加拦截器：

```golang
  	[...]

	conn, err := grpc.Dial(addr, grpc.WithTransportCredentials(insecure.NewCredentials()),
		grpc.WithUnaryInterceptor(otelgrpc.UnaryClientInterceptor()),
		grpc.WithStreamInterceptor(otelgrpc.StreamClientInterceptor()),
	)
```

### 如果不使用请求路由

```golang
import (
  "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
)
```

在将 http.Handler 传递给 ServeMux 的每个地方，您都将包装处理程序函数。例如，将进行以下替换：

```golang
- mux.Handle("/path", h)
+ mux.Handle("/path", otelhttp.NewHandler(h, "description of path"))
---
- mux.Handle("/path", http.HandlerFunc(f))
+ mux.Handle("/path", otelhttp.NewHandler(http.HandlerFunc(f), "description of path"))
```

通过这种方式，您可以确保使用 othttp 包装的每个函数都会自动收集其元数据并启动相应的跟踪。

## 自定义 Span

很多时候，OpenTelemetry 提供的中间件不能帮助我们记录更多内部调用的函数，需要我们自定义 Span 来记录

```golang
 ······
	_, span := otel.Tracer("GetServiceDetail").Start(ctx,
		"spanMetricDao.GetServiceDetail",
		trace.WithSpanKind(trace.SpanKindInternal))
	defer span.End()
  ······
```

## 向 span 添加自定义属性和事件

也可以将自定义属性或标签设置为 Span。要添加自定义属性和事件，请按照以下步骤操作：

### 导入跟踪和属性库

```golang
import (
    ...
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/trace"
)
```

### 从上下文中获取当前 Span

```golang
span := trace.SpanFromContext(c.Request.Context())
```

### 在当前 Span 中设置属性

```golang
span.SetAttributes(attribute.String("controller", "books"))
```

### 为当前 Span 添加 Event

添加 span 事件是使用 span 对象上的 __AddEvent__ 完成的。

```golang
span.AddEvent(msg)
```

## 记录错误和异常

```golang
import "go.opentelemetry.io/otel/codes"

// 获取当前 span
span := trace.SpanFromContext(ctx)

// RecordError 会自动将一个错误转换成 span even
span.RecordError(err)

// 标记这个 span 错误
span.SetStatus(codes.Error, "internal error")
```

## 参考

有关 Demo 演示请参考：

- [otel-grpc-examples](https://github.com/openinsight-proj/otel-grpc-examples/tree/no-metadata-grpcgateway-v1.11.1)
- [opentelemetry-demo/productcatalogservice](https://github.com/open-telemetry/opentelemetry-demo/tree/main/src/productcatalogservice)
- [opentelemetry-collector-contrib/demo](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/examples/demo)
