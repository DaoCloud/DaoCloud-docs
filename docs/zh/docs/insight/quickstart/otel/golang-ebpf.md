# 使用 OTel 自动探针增强 Go 应用程序（实验性功能）

如果不想手动更改应用代码，您可以尝试使用本文基于 eBPF 的自动增强方式。
该功能目前还处于捐献到 OpenTelemetry 社区的评审阶段，还不支持 Operator 通过注解方式注入（未来会支持），因此需要手动更改 Deployment YAML 或采用 patch 的方式。

## 前提条件

请确保 Insight Agent 已经就绪。如若没有，请参阅[安装 insight-agent 采集数据](../install/install-agent.md)，并确保以下三项就绪：

- 为 Insight-agent 开启 trace 功能
- trace 数据的地址以及端口是否填写正确
- deployment/opentelemetry-operator-controller-manager 和 deployment/insight-agent-opentelemetry-collector 对应的 Pod 已经准备就绪

## 安装 Instrumentation CR

在 Insight-system namespace 下安装，如已安装可跳过此步骤。

注意：该 CR 目前只支持注入对接 Insight 所需要的环境变量（包括服务名、链路上报地址等等），未来会支持注入 Golang 探针。

```bash
kubectl apply -f - <<EOF
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
EOF
```

## 更改应用程序部署文件

- 添加环境变量注解

    这类注解只有一个，用于添加 OpenTelemetry 相关的环境变量，比如链路上报地址、容器所在的集群 id、命名空间等：

    ```console
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

    其中 value 被 __/__ 分成两部分，第一个值 __insight-system__ 是第二步安装的 CR 的命名空间，第二个值 __insight-opentelemetry-autoinstrumentation__ 是这个 CR 的名字。

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
            instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation" # (1)
        spec:
          containers:
            - env:
                - name: GRPC_PORT
                  value: "8080"
                - name: PROM_PORT
                  value: "8801"
              image: docker.l5d.io/buoyantio/emojivoto-voting-svc:v11 # (2)
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
                  value: /usr/local/bin/emojivoto-voting-svc # (3)
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

    1. 用于添加 OpenTelemetry 相关的环境变量
    2. 假设这是您的 Golang 应用程序
    3. 注意与上面 __command__ 内容 __/usr/local/bin/emojivoto-voting-svc__ 保持一致

最终生成的 Yaml 内容如下：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: voting-84b696c897-p9xbp
  generateName: voting-84b696c897-
  namespace: default
  uid: 742639b0-db6e-4f06-ac90-68a80e2b8a11
  resourceVersion: '65560793'
  creationTimestamp: '2022-10-19T07:08:56Z'
  labels:
    app: voting-svc
    pod-template-hash: 84b696c897
    version: v11
  annotations:
    cni.projectcalico.org/containerID: 0a987cf0055ce0dfbe75c3f30d580719eb4fbbd7e1af367064b588d4d4e4c7c7
    cni.projectcalico.org/podIP: 192.168.141.218/32
    cni.projectcalico.org/podIPs: 192.168.141.218/32
    instrumentation.opentelemetry.io/inject-sdk: insight-system/insight-opentelemetry-autoinstrumentation
spec:
  volumes:
    - name: launcherdir
      emptyDir: {}
    - name: kernel-debug
      hostPath:
        path: /sys/kernel/debug
        type: ''
    - name: kube-api-access-gwj5v
      projected:
        sources:
          - serviceAccountToken:
              expirationSeconds: 3607
              path: token
          - configMap:
              name: kube-root-ca.crt
              items:
                - key: ca.crt
                  path: ca.crt
          - downwardAPI:
              items:
                - path: namespace
                  fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.namespace
        defaultMode: 420
  containers:
    - name: voting-svc
      image: docker.l5d.io/buoyantio/emojivoto-voting-svc:v11
      command:
        - /odigos-launcher/launch
        - /usr/local/bin/emojivoto-voting-svc
      ports:
        - name: grpc
          containerPort: 8080
          protocol: TCP
        - name: prom
          containerPort: 8801
          protocol: TCP
      env:
        - name: GRPC_PORT
          value: '8080'
        - name: PROM_PORT
          value: '8801'
        - name: OTEL_TRACES_EXPORTER
          value: otlp
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: >-
            http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317
        - name: OTEL_EXPORTER_OTLP_TIMEOUT
          value: '200'
        - name: SPLUNK_TRACE_RESPONSE_HEADER_ENABLED
          value: 'true'
        - name: OTEL_SERVICE_NAME
          value: voting
        - name: OTEL_RESOURCE_ATTRIBUTES_POD_NAME
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: metadata.name
        - name: OTEL_RESOURCE_ATTRIBUTES_POD_UID
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: metadata.uid
        - name: OTEL_RESOURCE_ATTRIBUTES_NODE_NAME
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: spec.nodeName
        - name: OTEL_PROPAGATORS
          value: jaeger,b3
        - name: OTEL_TRACES_SAMPLER
          value: always_on
        - name: OTEL_RESOURCE_ATTRIBUTES
          value: >-
            k8s.container.name=voting-svc,k8s.deployment.name=voting,k8s.deployment.uid=79e015e2-4643-44c0-993c-e486aebaba10,k8s.namespace.name=default,k8s.node.name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME),k8s.pod.uid=$(OTEL_RESOURCE_ATTRIBUTES_POD_UID),k8s.replicaset.name=voting-84b696c897,k8s.replicaset.uid=63f56167-6632-415d-8b01-43a3db9891ff
      resources:
        requests:
          cpu: 100m
      volumeMounts:
        - name: launcherdir
          mountPath: /odigos-launcher
        - name: kube-api-access-gwj5v
          readOnly: true
          mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      imagePullPolicy: IfNotPresent
    - name: emojivoto-voting-instrumentation
      image: keyval/otel-go-agent:v0.6.0
      env:
        - name: OTEL_TARGET_EXE
          value: /usr/local/bin/emojivoto-voting-svc
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: jaeger:4317
        - name: OTEL_SERVICE_NAME
          value: emojivoto-voting
      resources: {}
      volumeMounts:
        - name: kernel-debug
          mountPath: /sys/kernel/debug
        - name: kube-api-access-gwj5v
          readOnly: true
          mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      imagePullPolicy: IfNotPresent
      securityContext:
        capabilities:
          add:
            - SYS_PTRACE
        privileged: true
        runAsUser: 0
······
```

## 更多参考

- [Go OpenTelemetry Automatic Instrumentation 入门](https://github.com/keyval-dev/opentelemetry-go-instrumentation/blob/master/docs/getting-started/README.md)
- [Donating ebpf based instrumentation](https://github.com/open-telemetry/opentelemetry-go-instrumentation/pull/4)
