---
MTPE: windsonsea
Date: 2024-10-16
---

# Exposing JVM Monitoring Metrics Using JMX Exporter

JMX Exporter provides two usage methods:

1. **Standalone Process**: Specify parameters when starting the JVM to expose a JMX RMI interface. The JMX Exporter calls RMI to obtain the JVM runtime state data, converts it into Prometheus metrics format, and exposes a port for Prometheus to scrape.
2. **In-Process (JVM process)**: Specify parameters when starting the JVM to run the JMX Exporter jar file as a javaagent. This method reads the JVM runtime state data in-process, converts it into Prometheus metrics format, and exposes a port for Prometheus to scrape.

!!! note

    The official recommendation is not to use the first method due to its complex configuration and the requirement for a separate process, which introduces additional monitoring challenges. Therefore, this article focuses on the second method, detailing how to use JMX Exporter to expose JVM monitoring metrics in a Kubernetes environment.

In this method, you need to specify the JMX Exporter jar file and configuration file when starting the JVM. Since the jar file is a binary file that is not ideal for mounting via a configmap, and the configuration file typically does not require modifications, it is recommended to package both the JMX Exporter jar file and the configuration file directly into the business container image.

For the second method, you can choose to include the JMX Exporter jar file in the application image or mount it during deployment. Below are explanations for both approaches:

## Method 1: Building JMX Exporter JAR File into the Business Image

The content of `prometheus-jmx-config.yaml` is as follows:

```yaml title="prometheus-jmx-config.yaml"
...
ssl: false
lowercaseOutputName: false
lowercaseOutputLabelNames: false
rules:
- pattern: ".*"
```

!!! note

    For more configuration options, please refer to the introduction at the bottom or [Prometheus official documentation](https://github.com/prometheus/jmx_exporter#configuration).

Next, prepare the jar file. You can find the latest jar download link on the [jmx_exporter](https://github.com/prometheus/jmx_exporter) GitHub page and refer to the following Dockerfile:

```shell
FROM openjdk:11.0.15-jre
WORKDIR /app/
COPY target/my-app.jar ./
COPY prometheus-jmx-config.yaml ./
RUN set -ex; \
    curl -L -O https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.17.2/jmx_prometheus_javaagent-0.17.2.jar;
ENV JAVA_TOOL_OPTIONS=-javaagent:/app/jmx_prometheus_javaagent-0.17.2.jar=8088:/app/prometheus-jmx-config.yaml
EXPOSE 8081 8999 8080 8888
ENTRYPOINT java $JAVA_OPTS -jar my-app.jar
```

Note:

- The format for the startup parameter is: `-javaagent:=:`
- Here, port 8088 is used to expose JVM monitoring metrics; you may change it if it conflicts with the Java application.

## Method 2: Mounting via Init Container

First, we need to create a Docker image for the JMX Exporter. The following Dockerfile is for reference:

```shell
FROM alpine/curl:3.14
WORKDIR /app/
# Copy the previously created config file into the image
COPY prometheus-jmx-config.yaml ./
# Download the jmx prometheus javaagent jar online
RUN set -ex; \
    curl -L -O https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.17.2/jmx_prometheus_javaagent-0.17.2.jar;
```

Build the image using the above Dockerfile: `docker build -t my-jmx-exporter .`

Add the following init container to the Java application deployment YAML:

??? note "Click to expand YAML file"

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-demo-app
      labels:
        app: my-demo-app
    spec:
      selector:
        matchLabels:
          app: my-demo-app
      template:
        metadata:
          labels:
            app: my-demo-app
        spec:
          imagePullSecrets:
          - name: registry-pull
          initContainers:
          - name: jmx-sidecar
            image: my-jmx-exporter
            command: ["cp", "-r", "/app/jmx_prometheus_javaagent-0.17.2.jar", "/target/jmx_prometheus_javaagent-0.17.2.jar"]  ➊
            volumeMounts:
            - name: sidecar
              mountPath: /target
          containers:
          - image: my-demo-app-image
            name: my-demo-app
            resources:
              requests:
                memory: "1000Mi"
                cpu: "500m"
              limits:
                memory: "1000Mi"
                cpu: "500m"
            ports:
            - containerPort: 18083
            env:
            - name: JAVA_TOOL_OPTIONS
              value: "-javaagent:/app/jmx_prometheus_javaagent-0.17.2.jar=8088:/app/prometheus-jmx-config.yaml" ➋
            volumeMounts:
            - name: host-time
              mountPath: /etc/localtime
              readOnly: true
            - name: sidecar
              mountPath: /sidecar
          volumes:
          - name: host-time
            hostPath:
              path: /etc/localtime
          - name: sidecar  # Shared agent folder
            emptyDir: {}
          restartPolicy: Always
    ```

With the above modifications, the example application `my-demo-app` now has the capability to expose JVM metrics. After running the service, you can access the Prometheus formatted metrics at `http://localhost:8088`.

Next, you can refer to [Connecting Existing JVM Metrics of Java Applications to Observability](./legacy-jvm.md).
