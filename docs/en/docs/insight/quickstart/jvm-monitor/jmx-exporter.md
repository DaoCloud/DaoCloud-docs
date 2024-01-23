# Use JMX Exporter to expose JVM monitoring metrics

JMX-Exporter provides two usages:

1. Start a standalone process. Specify parameters when the JVM starts, expose the RMI interface of JMX, JMX Exporter calls RMI to obtain the JVM runtime status data,
    Convert to Prometheus metrics format, and expose ports for Prometheus to collect.
2. Start the JVM in-process. Specify parameters when the JVM starts, and run the jar package of JMX-Exporter in the form of javaagent.
    Read the JVM runtime status data in the process, convert it into Prometheus metrics format, and expose the port for Prometheus to collect.

!!! note

     Officials do not recommend the first method. On the one hand, the configuration is complicated, and on the other hand, it requires a separate process, and the monitoring of this process itself has become a new problem.
     So This page focuses on the second usage and how to use JMX Exporter to expose JVM monitoring metrics in the Kubernetes environment.

The second usage is used here, and the JMX Exporter jar package file and configuration file need to be specified when starting the JVM.
The jar package is a binary file, so it is not easy to mount it through configmap. We hardly need to modify the configuration file.
So the suggestion is to directly package the jar package and configuration file of JMX Exporter into the business container image.

Among them, in the second way, we can choose to put the jar file of JMX Exporter in the business application mirror,
You can also choose to mount it during deployment. Here is an introduction to the two methods:

## Method 1: Build the JMX Exporter JAR file into the business image

The content of prometheus-jmx-config.yaml is as follows:

```yaml title="prometheus-jmx-config.yaml"
...
ssl: false
lowercaseOutputName: false
lowercaseOutputLabelNames: false
rules:
- pattern: ".*"
```

!!! note

    For more configuration items, please refer to the bottom introduction or [Prometheus official documentation](https://github.com/prometheus/jmx_exporter#configuration).

Then prepare the jar package file, you can find the latest jar package download address on the Github page of [jmx_exporter](https://github.com/prometheus/jmx_exporter) and refer to the following Dockerfile:

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

Notice:

- Start parameter format: -javaagent:=:
- Port 8088 is used here to expose the monitoring metrics of the JVM. If it conflicts with Java applications, you can change it yourself

## Method 2: mount via init container container

We need to make the JMX exporter into a Docker image first, the following Dockerfile is for reference only:

```shell
FROM alpine/curl:3.14
WORKDIR /app/
# Copy the previously created config file to the mirror
COPY prometheus-jmx-config.yaml ./
# Download jmx prometheus javaagent jar online
RUN set -ex; \
     curl -L -O https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.17.2/jmx_prometheus_javaagent-0.17.2.jar;
```

Build the image according to the above Dockerfile: __docker build -t my-jmx-exporter .__ 

Add the following init container to the Java application deployment Yaml:

??? note "Click to view YAML file"

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
          - name: sidecar  # Share the agent folder
            emptyDir: {}
          restartPolicy: Always
    ```

After the above modification, the sample application my-demo-app has the ability to expose JVM metrics.
After running the service, we can access the prometheus format metrics exposed by the service through `http://lcoalhost:8088`.

Then, you can refer to [Java Application Docking Observability with JVM Metrics](./legacy-jvm.md).
