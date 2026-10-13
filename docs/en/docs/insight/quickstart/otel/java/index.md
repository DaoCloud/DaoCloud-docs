---
MTPE: windsonsea
Date: 2024-10-16
---

# Start Monitoring Java Applications

This article explains how to use OpenTelemetry Java Agent/SDK for automatic or manual instrumentation and report data.

## Prerequisites

- Obtain the access point information:

    Obtain the address exposed by the Service `insight-agent-opentelemetry-collector` in the `insight-system` namespace of the cluster on port `4317`
    or `4318`. Assume it is: `http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317`. Adjust it according to the actual load type of the Service.

## Method 1: Automatic Instrumentation with OpenTelemetry Java Agent

[OpenTelemetry Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation) provides a non-intrusive way to integrate and supports
the automatic upload of Trace data for hundreds of Java frameworks. For the detailed list of supported Java frameworks, refer to
[Supported Libraries and Versions](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md).

### Kubernetes Scenario

For integrating and monitoring Java application traces in a Kubernetes environment, refer to the document
[Non-intrusive Enhancement of Applications via Operator](../operator.md), which explains how to automatically integrate traces through annotations.

### Non-Kubernetes Scenario

1. Download the [Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases).
2. Report trace data by modifying the VM parameters used to start Java.

=== "gRPC"

    ```bash
    java -javaagent:/path/to/opentelemetry-javaagent.jar \   # Change the path to the actual location where you downloaded the file.
    -Dotel.resource.attributes=service.name=my-java-demo,service.version=v0.0.1,deployment.environment=test \
    -Dotel.exporter.otlp.protocol=grpc \
    -Dotel.exporter.otlp.endpoint=<endpoint> \   # Replace it with the access point corresponding to port 4317 obtained in the prerequisites.
    -Dotel.logs.exporter=none \
    -Dotel.metrics.exporter=none \
    -jar /path/to/your/app.jar     # Replace it with the actual path of your jar package.
    ```

=== "HTTP"

    ```bash
    java -javaagent:/path/to/opentelemetry-javaagent.jar\   # Change the path to the actual location where you downloaded the file.
    -Dotel.resource.attributes=service.name=my-java-demo,service.version=v0.0.1,deployment.environment=test \
    -Dotel.exporter.otlp.protocol=http/protobuf \
    -Dotel.exporter.otlp.traces.endpoint=<traces.endpoint> \   # Replace it with the access point corresponding to port 4318 obtained in the prerequisites.
    -Dotel.logs.exporter=none \
    -Dotel.metrics.exporter=none \
    -jar /path/to/your/app.jar  # Replace it with the actual path of your jar package.
    ```

## Method 2: Manual Instrumentation with OpenTelemetry Java SDK

[OpenTelemetry Java SDK](https://github.com/open-telemetry/opentelemetry-java) is the foundation of the OpenTelemetry Java Agent
and also provides rich customization capabilities. When the instrumentation of OpenTelemetry Java Agent does not meet your scenario or you need to add some custom business instrumentation, you can integrate it in the following ways.

1. Add the Maven POM dependency:

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

2. Obtain an OpenTelemetry Tracer:

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
            // Obtain an OpenTelemetry Tracer
            Resource resource = Resource.getDefault()
                    .merge(Resource.create(Attributes.of(
                            ResourceAttributes.SERVICE_NAME, "", // application name.
                            ResourceAttributes.SERVICE_VERSION, "", // version number.
                    )));
            
            SdkTracerProvider sdkTracerProvider = SdkTracerProvider.builder()
                    .addSpanProcessor(BatchSpanProcessor.builder(OtlpGrpcSpanExporter.builder()
                            .setEndpoint("insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317") // Replace the endpoint address with the access point information actually obtained.
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

3. Create a Span:

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

## Method 3: Use Both Java Agent and Java SDK for Instrumentation

You can use the Java SDK to add custom business instrumentation while using the Java Agent to obtain the automatic instrumentation capability.

1. Download the [Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases).

2. Add the following dependencies on top of the Maven dependencies in [Method 2](#method-2-manual-instrumentation-with-opentelemetry-java-sdk).

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

        Among them, `opentelemetry-sdk-extension-autoconfigure` completes the automatic configuration of the SDK and passes the Java Agent configuration to the Java SDK.

3. Modify the Java code to obtain an OpenTelemetry Tracer.

    When using both the Java Agent and the Java SDK for instrumentation, you no longer need to use the OpenTelemetrySupport class in [Method 2](#method-2-manual-instrumentation-with-opentelemetry-java-sdk) to obtain the Tracer.

    ```java
    OpenTelemetry openTelemetry = GlobalOpenTelemetry.get();
    Tracer tracer = openTelemetry.getTracer("instrumentation-library-name", "1.0.0");
    ```

4. Modify the Controller code and the Service code with reference to the following content.

    === "Controller Code"

        It is recommended to use the first and second approaches in the following code:

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
        * References:
        * 1. https://opentelemetry.io/docs/java/manual_instrumentation/
        */
        @RestController
            @RequestMapping("/user")
            public class UserController {

                @Autowired
                private UserService userService;

                private ExecutorService es = Executors.newFixedThreadPool(5);

                // Approach 1: automatic instrumentation, manually add information based on the API
                @RequestMapping("/async")
                public String async() {
                    System.out.println("UserController.async -- " + Thread.currentThread().getId());
                    Span span = Span.current();
                    span.setAttribute("user.id", "123456");
                    userService.async();
                    child("vip");
                    return "async";
                }

                // Approach 2: create instrumentation through annotations
                @WithSpan
                private void child(@SpanAttribute("user.type") String userType) {
                    System.out.println(userType);
                    biz();
                }

                // Approach 3: obtain a Tracer for purely manual instrumentation
                private void biz() {
                    Tracer tracer = GlobalOpenTelemetry.get().getTracer("tracer");
                    Span span = tracer.spanBuilder("biz (manual)")
                        .setParent(Context.current().with(Span.current())) // optional, set automatically
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

    === "Service Code"

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

6. Report trace data by modifying the VM parameters used to start Java.

    ```bash
    -javaagent:/path/to/opentelemetry-javaagent.jar    //Change the path to the actual location where you downloaded the file.
    -Dotel.resource.attributes=service.name=<appName>     //<appName> is the application name.
    -Dotel.exporter.otlp.endpoint=<endpoint>
    ```

7. Start the application.

## Other Use Cases

1. Monitoring the JVM of Java applications: How Java applications that have already exposed JVM metrics and those that have not yet exposed JVM metrics can connect with observability Insight.

    - If your Java application has not yet started exposing JVM metrics, you can refer to the following documents:

        - [Exposing JVM Monitoring Metrics Using JMX Exporter](./jvm-monitor/jmx-exporter.md)
        - [Exposing JVM Monitoring Metrics Using OpenTelemetry Java Agent](./jvm-monitor/otel-java-agent.md)

    - If your Java application has already exposed JVM metrics, you can refer to 
      [Connecting Existing JVM Metrics of Java Applications to Observability](./jvm-monitor/legacy-jvm.md)

2. [Writing TraceId and SpanId into Java Application Logs](./mdc.md) to correlate trace data with log data.
