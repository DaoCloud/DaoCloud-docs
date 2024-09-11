# 使用 JMX Exporter 暴露 JVM 监控指标

JMX-Exporter 提供了两种用法:

1. 启动独立进程。JVM 启动时指定参数，暴露 JMX 的 RMI 接口，JMX Exporter 调用 RMI 获取 JVM 运行时状态数据，
   转换为 Prometheus metrics 格式，并暴露端口让 Prometheus 采集。
2. JVM 进程内启动(in-process)。JVM 启动时指定参数，通过 javaagent 的形式运行 JMX-Exporter 的 jar 包，
   进程内读取 JVM 运行时状态数据，转换为 Prometheus metrics 格式，并暴露端口让 Prometheus 采集。

!!! note

    官方不推荐使用第一种方式，一方面配置复杂，另一方面因为它需要一个单独的进程，而这个进程本身的监控又成了新的问题，
    所以本文重点围绕第二种用法讲如何在 Kubernetes 环境下使用 JMX Exporter 暴露 JVM 监控指标。

这里使用第二种用法，启动 JVM 时需要指定 JMX Exporter 的 jar 包文件和配置文件。
jar 包是二进制文件，不好通过 configmap 挂载，配置文件我们几乎不需要修改，
所以建议是直接将 JMX Exporter 的 jar 包和配置文件都打包到业务容器镜像中。

其中，第二种方式我们可以选择将 JMX Exporter 的 jar 文件放在业务应用镜像中，
也可以选择在部署的时候挂载进去。这里分别对两种方式做一个介绍：

## 方式一：将 JMX Exporter JAR 文件构建至业务镜像中

prometheus-jmx-config.yaml 内容如下：

```yaml title="prometheus-jmx-config.yaml"
...
ssl: false
lowercaseOutputName: false
lowercaseOutputLabelNames: false
rules:
- pattern: ".*"
```

!!! note

    更多配置项请参考底部介绍或[Prometheus 官方文档](https://github.com/prometheus/jmx_exporter#configuration)。

然后准备 jar 包文件，可以在 [jmx_exporter](https://github.com/prometheus/jmx_exporter) 的 Github 页面找到最新的 jar 包下载地址并参考如下 Dockerfile:

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

注意：

- 启动参数格式：-javaagent:=:
- 这里使用了 8088 端口暴露 JVM 的监控指标，如果和 Java 应用冲突，可自行更改

## 方式二： 通过 init container 容器挂载

我们需要先将 JMX exporter 做成 Docker 镜像, 以下 Dockerfile 仅供参考：

```shell
FROM alpine/curl:3.14
WORKDIR /app/
# 将前面创建的 config 文件拷贝至镜像
COPY prometheus-jmx-config.yaml ./
# 在线下载 jmx prometheus javaagent jar
RUN set -ex; \
    curl -L -O https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.17.2/jmx_prometheus_javaagent-0.17.2.jar;
```

根据上面 Dockerfile 构建镜像： __docker build -t my-jmx-exporter .__ 

在 Java 应用部署 Yaml 中加入如下 init container：

??? note "点击展开 YAML 文件"

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
          - name: sidecar  #共享 agent 文件夹
            emptyDir: {}
          restartPolicy: Always
    ```

经过如上的改造之后，示例应用 my-demo-app 具备了暴露 JVM 指标的能力。
运行服务之后，我们可以通过 `http://lcoalhost:8088` 访问服务暴露出来的 prometheus 格式的指标。

接着，您可以参考 [已有 JVM 指标的 Java 应用对接可观测性](./legacy-jvm.md)。
