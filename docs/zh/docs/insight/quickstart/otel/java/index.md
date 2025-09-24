# 开始监控 Java 应用

本文介绍如何使用 OpenTelemetry Java Agent/SDK 进行自动或手动埋点并上报数据。

## 前提条件

- 获取接入点信息：

    获取集群 `insight-system` 命名空间下 `insight-agent-opentelemetry-collector` 服务对应的 Service 以及 `4317`
    或者 `4318` 端口暴露的地址，假设为：`http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317`，请根据 Service 实际的负载类型进行调整。

## 方式一：使用 OpenTelemetry Java Agent 自动埋点

[OpenTelemetry Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation) 提供了无侵入的接入方式，支持上百种
Java 框架自动上传 Trace 数据，详细的 Java 框架支持列表，请参见
[Supported Libraries and Versions](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md)。

### Kubernetes 场景

在 Kubernetes 环境下的 Java 应用链路接入与监控，请参考[通过 Operator 实现应用程序无侵入增强](../operator.md)文档，通过注解实现自动接入链路。

### 非 Kubernetes 场景

1. 下载 [Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases)。
2. 通过修改 Java 启动的 VM 参数上报链路数据。

=== "gRPC 方式"

    ```bash
    java -javaagent:/path/to/opentelemetry-javaagent.jar \   # 请将路径修改为您文件下载的实际地址。
    -Dotel.resource.attributes=service.name=my-java-demo,service.version=v0.0.1,deployment.environment=test \
    -Dotel.exporter.otlp.protocol=grpc \
    -Dotel.exporter.otlp.endpoint=<endpoint> \   # 替换为前提条件中获取到 4317 端口对应的接入点。
    -Dotel.logs.exporter=none \
    -Dotel.metrics.exporter=none \
    -jar /path/to/your/app.jar     # 替换为您实际jar包的地址。
    ```

=== "HTTP 方式"

    ```bash
    java -javaagent:/path/to/opentelemetry-javaagent.jar\   # 请将路径修改为您文件下载的实际地址。
    -Dotel.resource.attributes=service.name=my-java-demo,service.version=v0.0.1,deployment.environment=test \
    -Dotel.exporter.otlp.protocol=http/protobuf \
    -Dotel.exporter.otlp.traces.endpoint=<traces.endpoint> \   # 替换为前提条件中获取到的 4318 端口对应的接入点。
    -Dotel.logs.exporter=none \
    -Dotel.metrics.exporter=none \
    -jar /path/to/your/app.jar  # 替换为您实际jar包的地址。
    ```

## 方式二：使用 OpenTelemetry Java SDK 手动埋点

[OpenTelemetry Java SDK](https://github.com/open-telemetry/opentelemetry-java) 是 OpenTelemetry Java Agent
实现的基础，同时提供了丰富的自定义能力。当 OpenTelemetry Java Agent 的埋点不满足您的场景或者需要增加一些自定义业务埋点时，可以使用以下方式接入。

1. 引入 Maven POM 依赖：

    ```xml
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-api</artifactId>
        </dependency>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-sdk-trace</artifactId>
        </dependency>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-exporter-otlp</artifactId>
        </dependency>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-sdk</artifactId>
        </dependency>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-semconv</artifactId>
            <version>1.30.0-alpha</version>
        </dependency>
    </dependencies>

    <dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-bom</artifactId>
            <version>1.30.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
    </dependencyManagement>
    ```

2. 获取 OpenTelemetry Tracer:

    ```golang
    import io.opentelemetry.api.OpenTelemetry;
    import io.opentelemetry.api.common.Attributes;
    import io.opentelemetry.api.trace.Tracer;
    import io.opentelemetry.api.trace.propagation.W3CTraceContextPropagator;
    import io.opentelemetry.context.propagation.ContextPropagators;
    import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter;
    import io.opentelemetry.sdk.OpenTelemetrySdk;
    import io.opentelemetry.sdk.resources.Resource;
    import io.opentelemetry.sdk.trace.SdkTracerProvider;
    import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;
    import io.opentelemetry.semconv.resource.attributes.ResourceAttributes;

    public class OpenTelemetrySupport {

        static {
            // 获取OpenTelemetry Tracer
            Resource resource = Resource.getDefault()
                    .merge(Resource.create(Attributes.of(
                            ResourceAttributes.SERVICE_NAME, "", // 应用名。
                            ResourceAttributes.SERVICE_VERSION, "", // 版本号。
                    )));
            
            SdkTracerProvider sdkTracerProvider = SdkTracerProvider.builder()
                    .addSpanProcessor(BatchSpanProcessor.builder(OtlpGrpcSpanExporter.builder()
                            .setEndpoint("insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317") // 请将endpoint 地址替换为实际获取的接入点信息。
                            .build()).build())
                    .setResource(resource)
                    .build();
            
            OpenTelemetry openTelemetry = OpenTelemetrySdk.builder()
                    .setTracerProvider(sdkTracerProvider)
                    .setPropagators(ContextPropagators.create(W3CTraceContextPropagator.getInstance()))
                    .buildAndRegisterGlobal();

            tracer = openTelemetry.getTracer("OpenTelemetry Tracer", "1.0.0");
        }

        private static Tracer tracer;

        public static Tracer getTracer() {
            return tracer;
        }
    }
    ```

3. 创建 Span：

    ```golang
    import io.opentelemetry.api.trace.Span;
    import io.opentelemetry.api.trace.StatusCode;
    import io.opentelemetry.context.Scope;

    public class Main {
        
        public static void parentMethod() {
            Span span = OpenTelemetrySupport.getTracer().spanBuilder("parent span").startSpan();
            try (Scope scope = span.makeCurrent()) {
                span.setAttribute("good", "job");
                childMethod();
            } catch (Throwable t) {
                span.setStatus(StatusCode.ERROR, "handle parent span error");
            } finally {
                span.end();
            }
        }

        public static void childMethod() {
            Span span = OpenTelemetrySupport.getTracer().spanBuilder("child span").startSpan();
            try (Scope scope = span.makeCurrent()) {
                span.setAttribute("hello", "world");
            } catch (Throwable t) {
                span.setStatus(StatusCode.ERROR, "handle child span error");
            } finally {
                span.end();
            }
        }

        public static void main(String[] args) {
            parentMethod();
        }
    }
    ```

## 方法三：同时使用 Java Agent 和 Java SDK 埋点

您可以在使用Java Agent获得自动埋点能力的同时，使用Java SDK添加自定义业务埋点。

1. 下载 [Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases)。

2. 在[方法二](#opentelemetry-java-sdk)的 Maven 依赖基础上新增如下依赖。

    ```xml
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-extension-annotations</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk-extension-autoconfigure</artifactId>
        <version>1.23.0-alpha</version>
    </dependency>
    ```

    !!! tip

        其中 `opentelemetry-sdk-extension-autoconfigure` 完成了 SDK 的自动配置，将 Java Agent 的配置传递到 Java SDK 中.

3. 修改 Java 代码以获取 OpenTelemetry Tracer

    同时使用 Java Agent 和 Java SDK 埋点时，无需再使用[方法二](#opentelemetry-java-sdk)中的 OpenTelemetrySupport 类获取 Tracer。

    ```java
    OpenTelemetry openTelemetry = GlobalOpenTelemetry.get();
    Tracer tracer = openTelemetry.getTracer("instrumentation-library-name", "1.0.0");
    ```

4. 参考以下内容修改 Controller 代码和 Service 代码

    === "Controller 代码"

        建议使用如下代码中的第一种和第二种方式：

        ```java
        package com.xxx.console.controller;
        import com.xxx..console.service.UserService;
        import io.opentelemetry.api.GlobalOpenTelemetry;
        import io.opentelemetry.api.OpenTelemetry;
        import io.opentelemetry.api.trace.Span;
        import io.opentelemetry.api.trace.StatusCode;
        import io.opentelemetry.api.trace.Tracer;
        import io.opentelemetry.context.Context;
        import io.opentelemetry.context.Scope;
        import io.opentelemetry.extension.annotations.SpanAttribute;
        import io.opentelemetry.extension.annotations.WithSpan;
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.web.bind.annotation.RequestMapping;
        import org.springframework.web.bind.annotation.RestController;

        import java.util.concurrent.ExecutorService;
        import java.util.concurrent.Executors;

        /**
        * 参考文档：
        * 1. https://opentelemetry.io/docs/java/manual_instrumentation/
        */
        @RestController
            @RequestMapping("/user")
            public class UserController {

                @Autowired
                private UserService userService;

                private ExecutorService es = Executors.newFixedThreadPool(5);

                // 第一种：自动埋点，基于 API 手工添加信息
                @RequestMapping("/async")
                public String async() {
                    System.out.println("UserController.async -- " + Thread.currentThread().getId());
                    Span span = Span.current();
                    span.setAttribute("user.id", "123456");
                    userService.async();
                    child("vip");
                    return "async";
                }

                // 第二种：通过注解创建埋点
                @WithSpan
                private void child(@SpanAttribute("user.type") String userType) {
                    System.out.println(userType);
                    biz();
                }

                // 第三种：获得 Tracer 纯手工埋点
                private void biz() {
                    Tracer tracer = GlobalOpenTelemetry.get().getTracer("tracer");
                    Span span = tracer.spanBuilder("biz (manual)")
                        .setParent(Context.current().with(Span.current())) // 可选，自动设置
                        .startSpan();

                    try (Scope scope = span.makeCurrent()) {
                        span.setAttribute("biz-id", "111");

                        es.submit(new Runnable() {
                            @Override
                            public void run() {
                                Span asyncSpan = tracer.spanBuilder("async")
                                    .setParent(Context.current().with(span))
                                    .startSpan();
                                try {
                                    Thread.sleep(1000L); // some async jobs
                                } catch (Throwable e) {
                                }
                                asyncSpan.end();
                            }
                        });

                        Thread.sleep(1000); // fake biz logic
                        System.out.println("biz done");
                        OpenTelemetry openTelemetry = GlobalOpenTelemetry.get();
                        openTelemetry.getPropagators();
                    } catch (Throwable t) {
                        span.setStatus(StatusCode.ERROR, "handle biz error");
                    } finally {
                        span.end();
                    }
                }

            }
        ```

    === "Service 代码"

        ```java
        package com.xxx.console.service;
        import org.springframework.scheduling.annotation.Async;
        import org.springframework.stereotype.Service;

        @Service
        public class UserService {

            @Async
            public void async() {
                System.out.println("UserService.async -- " + Thread.currentThread().getId());
                System.out.println("my name is async");
                System.out.println("UserService.async -- ");
            }
        }
        ```

6. 通过修改 Java 启动的 VM 参数上报链路数据。

    ```bash
    -javaagent:/path/to/opentelemetry-javaagent.jar    //请将路径修改为您文件下载的实际地址。
    -Dotel.resource.attributes=service.name=<appName>     //<appName> 为应用名。
    -Dotel.exporter.otlp.endpoint=<endpoint>
    ```

7. 启动应用。

## 其他用例参考

1. Java 应用的 JVM 进行监控：已经暴露 JVM 指标和仍未暴露 JVM 指标的 Java 应用如何与可观测性 Insight 对接。

    - 如果您的 Java 应用未开始暴露 JVM 指标，您可以参考如下文档：

        - [使用 JMX Exporter 暴露 JVM 监控指标](./jvm-monitor/jmx-exporter.md)
        - [使用 OpenTelemetry Java Agent 暴露 JVM 监控指标](./jvm-monitor/otel-java-agent.md)

    - 如果您的 Java 应用已经暴露 JVM 指标，您可以参考文档：
      [已有 JVM 指标的 Java 应用对接可观测性](./jvm-monitor/legacy-jvm.md)

2. [将 TraceId 和 SpanId 写入 Java 应用日志](./mdc.md), 实现链路数据与日志数据关联。
