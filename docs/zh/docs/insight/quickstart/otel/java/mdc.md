# 将 TraceId 和 SpanId 写入 Java 应用日志

本文介绍如何使用 OpenTelemetry 将 TraceId 和 SpanId 自动写入 Java 应用日志。
TraceId 与 SpanId 写入日志后，您可以将分布式链路数据与日志数据关联起来，实现更高效的故障诊断和性能分析。

## 支持的日志库

更多信息，请参见 [Logger MDC auto-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/logger-mdc-instrumentation.md)。

| 日志框架 | 支持自动埋点的版本 | 手动埋点需要引入的依赖 |
| ------- | --------------- | ------------------ |
| Log4j 1 | 1.2+ | 无|
| Log4j 2 | 2.7+  | [opentelemetry-log4j-context-data-2.17-autoconfigure](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/log4j/log4j-context-data/log4j-context-data-2.17/library-autoconfigure) |
| Logback | 1.0+  | [opentelemetry-logback-mdc-1.0](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/logback/logback-mdc-1.0/library) |

## 使用 Logback（SpringBoot 项目）

Spring Boot 项目内置了日志框架，并且默认使用 Logback 作为其日志实现。如果您的 Java 项目为 SpringBoot 项目，只需少量配置即可将 TraceId 写入日志。

在 `application.properties` 中设置 `logging.pattern.level`，添加 `%mdc{trace_id}` 与 `%mdc{span_id}` 到日志中。

```bash
logging.pattern.level=trace_id=%mdc{trace_id} span_id=%mdc{span_id} %5p ....省略...
```

以下为日志示例：

```console
2024-06-26 10:56:31.200 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=1b08f18b8858bb9a  INFO 53724 --- [nio-8081-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-06-26 10:56:31.201 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=1b08f18b8858bb9a  INFO 53724 --- [nio-8081-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-06-26 10:56:31.209 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=1b08f18b8858bb9a  INFO 53724 --- [nio-8081-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 8 ms
2024-06-26 10:56:31.296 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=5743699405074f4e  INFO 53724 --- [nio-8081-exec-1] com.example.httpserver.ot.OTServer       : hello world
```

## 使用 Log4j2

1. 在 `pom.xml` 中添加 `OpenTelemetry Log4j2` 依赖:

    !!! tip

        请将 `OPENTELEMETRY_VERSION` 替换为[最新版本](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-log4j-context-data-2.17-autoconfigure/versions)

    ```xml
    <dependencies>
      <dependency>
        <groupId>io.opentelemetry.instrumentation</groupId>
        <artifactId>opentelemetry-log4j-context-data-2.17-autoconfigure</artifactId>
        <version>OPENTELEMETRY_VERSION</version>
        <scope>runtime</scope>
      </dependency>
    </dependencies>
    ```

1. 修改 `log4j2.xml` 配置，在 `pattern` 中添加 `%X{trace_id}` 与 `%X{span_id}`，可以将 `TraceId` 与 `SpanId` 自动写入日志:

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <Configuration>
      <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
          <PatternLayout
              pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} trace_id=%X{trace_id} span_id=%X{span_id} trace_flags=%X{trace_flags} - %msg%n"/>
        </Console>
      </Appenders>
      <Loggers>
        <Root>
          <AppenderRef ref="Console" level="All"/>
        </Root>
      </Loggers>
    </Configuration>
    ```

1. 使用 Logback 在 `pom.xml` 中添加 `OpenTelemetry Logback` 依赖。

    !!! tip

        请将 `OPENTELEMETRY_VERSION` 替换为[最新版本](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-log4j-context-data-2.17-autoconfigure/versions)

    ```xml
    <dependencies>
      <dependency>
        <groupId>io.opentelemetry.instrumentation</groupId>
        <artifactId>opentelemetry-logback-mdc-1.0</artifactId>
        <version>OPENTELEMETRY_VERSION</version>
      </dependency>
    </dependencies>
    ```

1. 修改 `log4j2.xml` 配置，在 `pattern` 中添加 `%X{trace_id}` 与 `%X{span_id}`，可以将 `TraceId` 与 `SpanId` 自动写入日志:

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <configuration>
      <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
          <pattern>%d{HH:mm:ss.SSS} trace_id=%X{trace_id} span_id=%X{span_id} trace_flags=%X{trace_flags} %msg%n</pattern>
        </encoder>
      </appender>

      <!-- Just wrap your logging appender, for example ConsoleAppender, with OpenTelemetryAppender -->
      <appender name="OTEL" class="io.opentelemetry.instrumentation.logback.mdc.v1_0.OpenTelemetryAppender">
        <appender-ref ref="CONSOLE"/>
      </appender>

      <!-- Use the wrapped "OTEL" appender instead of the original "CONSOLE" one -->
      <root level="INFO">
        <appender-ref ref="OTEL"/>
      </root>

    </configuration>
    ```
