---
MTPE: windsonsea
Date: 2024-10-16
---

# Writing TraceId and SpanId into Java Application Logs

This article explains how to automatically write TraceId and SpanId into Java application logs using OpenTelemetry. By including TraceId and SpanId in your logs, you can correlate distributed tracing data with log data, enabling more efficient fault diagnosis and performance analysis.

## Supported Logging Libraries

For more information, please refer to the [Logger MDC auto-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/logger-mdc-instrumentation.md).

| Logging Framework | Supported Automatic Instrumentation Versions | Dependencies Required for Manual Instrumentation |
| ------------------ | ----------------------------------------- | ----------------------------------------------- |
| Log4j 1            | 1.2+                                     | None                                           |
| Log4j 2            | 2.7+                                     | [opentelemetry-log4j-context-data-2.17-autoconfigure](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/log4j/log4j-context-data/log4j-context-data-2.17/library-autoconfigure) |
| Logback            | 1.0+                                     | [opentelemetry-logback-mdc-1.0](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/logback/logback-mdc-1.0/library) |

## Using Logback (Spring Boot Project)

Spring Boot projects come with a built-in logging framework and use Logback as the default logging implementation. If your Java project is a Spring Boot project, you can write TraceId into logs with minimal configuration.

Set `logging.pattern.level` in `application.properties`, adding `%mdc{trace_id}` and `%mdc{span_id}` to the logs.

```bash
logging.pattern.level=trace_id=%mdc{trace_id} span_id=%mdc{span_id} %5p ....omited...
```

Here is an example of the logs:

```console
2024-06-26 10:56:31.200 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=1b08f18b8858bb9a  INFO 53724 --- [nio-8081-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-06-26 10:56:31.201 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=1b08f18b8858bb9a  INFO 53724 --- [nio-8081-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-06-26 10:56:31.209 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=1b08f18b8858bb9a  INFO 53724 --- [nio-8081-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 8 ms
2024-06-26 10:56:31.296 trace_id=8f7ebd8a73f9a8f50e6a00a87a20952a span_id=5743699405074f4e  INFO 53724 --- [nio-8081-exec-1] com.example.httpserver.ot.OTServer       : hello world
```

## Using Log4j2

1. Add `OpenTelemetry Log4j2` dependency in `pom.xml`:

    !!! tip

        Please replace `OPENTELEMETRY_VERSION` with the [latest version](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-log4j-context-data-2.17-autoconfigure/versions).

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

2. Modify the `log4j2.xml` configuration, adding `%X{trace_id}` and `%X{span_id}` in the `pattern` to automatically write TraceId and SpanId into the logs:

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

3. If using Logback, add `OpenTelemetry Logback` dependency in `pom.xml`.

    !!! tip

        Please replace `OPENTELEMETRY_VERSION` with the [latest version](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-log4j-context-data-2.17-autoconfigure/versions).

    ```xml
    <dependencies>
      <dependency>
        <groupId>io.opentelemetry.instrumentation</groupId>
        <artifactId>opentelemetry-logback-mdc-1.0</artifactId>
        <version>OPENTELEMETRY_VERSION</version>
      </dependency>
    </dependencies>
    ```

4. Modify the `log4j2.xml` configuration, adding `%X{trace_id}` and `%X{span_id}` in the `pattern` to automatically write TraceId and SpanId into the logs:

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
