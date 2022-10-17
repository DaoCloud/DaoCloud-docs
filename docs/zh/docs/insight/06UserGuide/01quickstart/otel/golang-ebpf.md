# 使用 OpenTelemetry(ebpf based) 自动探针增强 Go 应用程序
如果不想手动更改你的应用代码，你可以使用本文的自动增强的方式。该功能目前还处于捐献到 Otel 社区的阶段，还不支持 Operator 通过注解方式注入（未来会支持），因此你需要手动更改 deployment yaml 或者 patch 的方式。

## 前提条件
请确保 Insight Agent 已经就绪，如若没有，请参考 [安装 insight-agent 采集数据](../installagent.md) 并确保以下三项就绪：
- Insight-agent 是否开始了 trace 功能？
- trace 数据的地址以及端口是否填写正确？
- opentelemetry-operator-controller-manager-xxx 以及 insight-agent-opentelemetry-collector- xxx 这两个 pod 是否已经准备就绪？

## 安装CR
在 Insight-system namespace下安装，如已安装可跳过该步骤。

注意：该 CR 目前只支持注入对接 Insight 所需要的环境变量（包括服务名，链路上报地址等等），未来会支持注入 Golang 探针。

```yaml
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: insight-opentelemetry-autoinstrumentation
  namespace: insight-system
spec:
  # https://github.com/open-telemetry/opentelemetry-operator/blob/main/docs/api.md#instrumentationspecresource
  resource:
    addK8sUIDAttributes: true
  env:
    - name: OTEL_EXPORTER_OTLP_ENDPOINT
      value: http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317
  sampler:
    # Enum: always_on, always_off, traceidratio, parentbased_always_on, parentbased_always_off, parentbased_traceidratio, jaeger_remote, xray
    type: always_on
  java:
    image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:1.17.0
    env:
      - name: OTEL_JAVAAGENT_DEBUG
        value: "false"
      - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
        value: "true"
      - name: SPLUNK_PROFILER_ENABLED
        value: "false"
  nodejs:
    image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:0.31.0
  python:
    image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.34b0
  dotnet:
    image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-dotnet:0.3.1-beta.1
```

## 更改应用程序部署文件
- 添加环境变量注解
这类注解只有一个，用于添加 otel 相关的环境变量，比如链路上报地址，容器所在的集群 id, 命名空间等：
```bash
instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
```

其中 value 被 / 分成两部分，第一个值(insight-system) 是第二步安装的 CR 的命名空间，第二个值(insight-opentelemetry-autoinstrumentation) 是这个 CR 的名字
- 添加 golang ebpf 探针容器
以下是示例代码：
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: voting
  namespace: emojivoto
  labels:
    app.kubernetes.io/name: voting
    app.kubernetes.io/part-of: emojivoto
    app.kubernetes.io/version: v11
spec:
  replicas: 1
  selector:
    matchLabels:
      app: voting-svc
      version: v11
  template:
    metadata:
      labels:
        app: voting-svc
        version: v11
      annotations:
        instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation" # 👈
    spec:
      containers:
        - env:
            - name: GRPC_PORT
              value: "8080"
            - name: PROM_PORT
              value: "8801"
          image: docker.l5d.io/buoyantio/emojivoto-voting-svc:v11 # 假设这是你的 Golang 应用程序
          name: voting-svc
          command:
            - /usr/local/bin/emojivoto-voting-svc
          ports:
            - containerPort: 8080
              name: grpc
            - containerPort: 8801
              name: prom
          resources:
            requests:
              cpu: 100m
        - name: emojivoto-voting-instrumentation
          image: docker.m.daocloud.io/keyval/otel-go-agent:v0.6.0
          env:
            - name: OTEL_TARGET_EXE
              value: /usr/local/bin/emojivoto-voting-svc # 注意与上面 /usr/local/bin/emojivoto-voting-svc 保持一致
          securityContext:
            runAsUser: 0
            capabilities:
              add:
                - SYS_PTRACE
            privileged: true
          volumeMounts:
            - mountPath: /sys/kernel/debug
              name: kernel-debug
      volumes:
        - name: kernel-debug
          hostPath:
            path: /sys/kernel/debug
```

## 更多请参考
- https://github.com/keyval-dev/opentelemetry-go-instrumentation/blob/master/docs/getting-started/README.md
- https://github.com/open-telemetry/opentelemetry-go-instrumentation/pull/4
