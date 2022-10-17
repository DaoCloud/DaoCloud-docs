# 使用 OpenTelemetry SDK 增强 Go 应用程序
本文档包含有关如何在 Go 应用程序中设置 OpenTelemetry 增强的说明。

OpenTelemetry，也简称为 OTel，是一个开源的可观察性框架，可以帮助你从你的 Go 应用程序中生成和收集遥测数据——跟踪、指标和日志。

# 使用 OpenTelemetry SDK 增强 Go 应用程序
## 安装相关依赖
必须先安装与 OpenTelemetry 导出器和 SDK 相关的依赖项。如果您正在使用其他请求路由器，请参考[请求路由](#请求路由)。
切换/进入到应用程序源文件夹后运行以下命令：
```bash
go get go.opentelemetry.io/otel \
  go.opentelemetry.io/otel/trace \
  go.opentelemetry.io/otel/sdk \
  go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin \
  go.opentelemetry.io/otel/exporters/otlp/otlptrace \
  go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc \
```

## 使用 OpenTelemetry SDK 创建初始化函数
为了让你的应用程序能够发送数据，我们需要一个函数来初始化 OpenTelemetry。在您的 `main.go` 文件中添加以下代码片段:
```golang
package main

import (
  "context"
  "fmt"
  "io/ioutil"
  "net"
  "os"
  "strings"

  "github.com/sirupsen/logrus"
  "go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc"
  "go.opentelemetry.io/otel"
  "go.opentelemetry.io/otel/attribute"
  otelcodes "go.opentelemetry.io/otel/codes"
  "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
  "go.opentelemetry.io/otel/propagation"
  sdktrace "go.opentelemetry.io/otel/sdk/trace"
  "go.opentelemetry.io/otel/trace"
)

var (
  log     *logrus.Logger
)

func initTracerProvider() *sdktrace.TracerProvider {
  ctx := context.Background()

  exporter, err := otlptracegrpc.New(ctx)
  if err != nil {
    log.Fatalf("OTLP Trace gRPC Creation: %v", err)
  }
  tp := sdktrace.NewTracerProvider(sdktrace.WithBatcher(exporter))
  otel.SetTracerProvider(tp)
  otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(propagation.TraceContext{}, propagation.Baggage{}))
  return tp
}
```

## 在 main.go 中初始化跟踪器
修改 main 函数以在 main.go 中初始化跟踪器，并且需要注意，当您的服务关闭时，您应该调用 `TracerProvider.Shutdown()` 确保导出所有跨度。该服务将该调用作为主函数中的延迟函数：
```golang
func main() {
    cleanup := initTracer()
    defer func() {
        if err := cleanup.Shutdown(context.Background()); err != nil {
            log.Fatalf("Tracer Provider Shutdown: %v", err)
        }
    }()
    ......
}
```

## 为你的应用程序添加 OpenTelemetry Gin 中间件
通过在 `main.go` 中添加以下行来配置 Gin 以使用中间件:

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

## 运行你的应用程序
- 本地调试运行
> 注意: 此步骤仅用于本地开发调试，生产环境中 Operator 会自动完成以下环境变量的注入

以上步骤已经完成了初始化 SDK 的工作，现在如果需要在本地开发进行调试的话，你需要提前获取到 insight-system 命名空间下 insight-agent-opentelemerty-collector 的地址，假设为：`insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317`

因此，你可以在你本地启动应用程序的时候添加上如下环境变量:
```bash
OTEL_SERVICE_NAME=my-golang-app
OTEL_EXPORTER_OTLP_ENDPOINT=http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317
```

- 生产环境运行
请参考 [通过 Operator 实现应用程序无侵入增强](./operator.md) 中 `只注入环境变量注解` 相关介绍。

# 请求路由
## OpenTelemetry gin/gonic 增强
```golang
# Add one line to your import() stanza depending upon your request router:
middleware "go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin"
```
然后注入 OpenTelemetry 中间件：
```golang
router.Use(middleware.Middleware("my-app"))
```

## OpenTelemetry gorillamux 增强
```golang
# Add one line to your import() stanza depending upon your request router:
middleware "go.opentelemetry.io/contrib/instrumentation/github.com/gorilla/mux/otelmux"
```
然后注入 OpenTelemetry 中间件：
```golang
router.Use(middleware.Middleware("my-app"))
```

## 如果您不使用请求路由
```golang
import (
  "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
)
```
在您将 http.Handler 传递给 ServeMux 的每个地方，您都将包装处理程序函数。例如，您将进行以下替换：
```golang
- mux.Handle("/path", h)
+ mux.Handle("/path", otelhttp.NewHandler(h, "description of path"))
---
- mux.Handle("/path", http.HandlerFunc(f))
+ mux.Handle("/path", otelhttp.NewHandler(http.HandlerFunc(f), "description of path"))
```

通过这种方式，您可以确保使用 othttp 包装的每个函数都会自动收集其元数据并启动相应的跟踪。

# 向 span 添加自定义属性和自定义事件
也可以将自定义属性或标签设置为跨度。要添加自定义属性和事件，请按照以下步骤操作：
## 导入跟踪和属性库
```golang
import (
    ...
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/trace"
)
```

## 从上下文中获取当前跨度
```golang
span := trace.SpanFromContext(c.Request.Context())
```

## 在当前跨度中设置属性
```golang
span.SetAttributes(attribute.String("controller", "books"))
```

## 为当前跨度添加 Event
添加 span 事件是使用 span 对象上的 `AddEvent` 完成的。
```golang
span.AddEvent(msg)
```

# gRPC 增强
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

# 记录错误和异常
```goalng
import "go.opentelemetry.io/otel/codes"

// 获取当前 span
span := trace.SpanFromContext(ctx)

// RecordError 会自动将一个错误转换成 span even
span.RecordError(err)

// 标记这个 span 错误
span.SetStatus(codes.Error, "internal error")
```

# 参考
完成 Demo 演示请参考：[opentelemetry-demo/productcatalogservice/](https://github.com/open-telemetry/opentelemetry-demo/tree/main/src/productcatalogservice)
