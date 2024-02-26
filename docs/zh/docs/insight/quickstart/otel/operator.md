# 通过 Operator 实现应用程序无侵入增强

> 目前只有 Java、NodeJs、Python、.Net、Golang 支持 Operator 的方式无侵入接入。

## 前提条件

请确保 Insight Agent 已经就绪。如若没有，请参考[安装 insight-agent 采集数据](../install/install-agent.md)并确保以下三项就绪：

- 为 Insight-agent 开启 trace 功能
- trace 数据的地址以及端口是否填写正确
- deployment/insight-agent-opentelemetry-operator 和
  deployment/insight-agent-opentelemetry-collector 对应的 Pod 已经准备就绪

## 安装 Instrumentation CR

!!! tip

    从 Insight v0.22.0 版本开始，不再需要手动安装 Instrumentation CR。

在 insight-system 命名空间下安装，不同版本之间有一些细小的差别。

=== "Insight v0.21.x"

    ```bash
    K8S_CLUSTER_UID=$(kubectl get namespace kube-system -o jsonpath='{.metadata.uid}')
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
        image: ghcr.m.daocloud.io/openinsight-proj/autoinstrumentation-java:1.31.0
        env:
          - name: OTEL_JAVAAGENT_DEBUG
            value: "false"
          - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
            value: "true"
          - name: SPLUNK_PROFILER_ENABLED
            value: "false"
          - name: OTEL_METRICS_EXPORTER
            value: "prometheus"
          - name: OTEL_METRICS_EXPORTER_PORT
            value: "9464"
          - name: OTEL_K8S_CLUSTER_UID
            value: $K8S_CLUSTER_UID
      nodejs:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:0.41.1
      python:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.40b0
      dotnet:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-dotnet:1.0.0
      go:
        # Must set the default value manually for now.
        # See https://github.com/open-telemetry/opentelemetry-operator/issues/1756 for details.
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-go-instrumentation/autoinstrumentation-go:v0.2.2-alpha
    EOF
    ```

=== "Insight v0.20.x"

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
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:1.29.0
        env:
          - name: OTEL_JAVAAGENT_DEBUG
            value: "false"
          - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
            value: "true"
          - name: SPLUNK_PROFILER_ENABLED
            value: "false"
          - name: OTEL_METRICS_EXPORTER
            value: "prometheus"
          - name: OTEL_METRICS_EXPORTER_PORT
            value: "9464"
      nodejs:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:0.41.1
      python:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.40b0
      dotnet:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-dotnet:1.0.0-rc.2
      go:
        # Must set the default value manually for now.
        # See https://github.com/open-telemetry/opentelemetry-operator/issues/1756 for details.
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-go-instrumentation/autoinstrumentation-go:v0.2.2-alpha
    EOF
    ```

=== "Insight v0.18.x"

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
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:1.25.0
        env:
          - name: OTEL_JAVAAGENT_DEBUG
            value: "false"
          - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
            value: "true"
          - name: SPLUNK_PROFILER_ENABLED
            value: "false"
          - name: OTEL_METRICS_EXPORTER
            value: "prometheus"
          - name: OTEL_METRICS_EXPORTER_PORT
            value: "9464"
      nodejs:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:0.37.0
      python:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.38b0
      go:
        # Must set the default value manually for now.
        # See https://github.com/open-telemetry/opentelemetry-operator/issues/1756 for details.
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-go-instrumentation/autoinstrumentation-go:v0.2.1-alpha
    EOF
    ```

=== "Insight v0.17.x"

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
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:1.23.0
        env:
          - name: OTEL_JAVAAGENT_DEBUG
            value: "false"
          - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
            value: "true"
          - name: SPLUNK_PROFILER_ENABLED
            value: "false"
          - name: OTEL_METRICS_EXPORTER
            value: "prometheus"
          - name: OTEL_METRICS_EXPORTER_PORT
            value: "9464"
      nodejs:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:0.34.0
      python:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.33b0
    EOF
    ```

=== "Insight v0.16.x"

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
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:1.23.0
        env:
          - name: OTEL_JAVAAGENT_DEBUG
            value: "false"
          - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
            value: "true"
          - name: SPLUNK_PROFILER_ENABLED
            value: "false"
          - name: OTEL_METRICS_EXPORTER
            value: "prometheus"
          - name: OTEL_METRICS_EXPORTER_PORT
            value: "9464"
      nodejs:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:0.34.0
      python:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.33b0
    EOF
    ```

## 与服务网格产品 Mspider 链路串联场景

如果您开启了服务网格的链路追踪能力，需要额外增加一个环境变量注入的配置：

### 操作步骤如下

1. 登录 DCE5.0，进入 __容器管理__ 后选择进入目标集群，
2. 点击左侧导航栏选择 __自定义资源__ ，查找 __instrumentations.opentelemetry.io__ 后进入详情页。
3. 选择 __insight-system__ 命名空间后，编辑 __insight-opentelemetry-autoinstrumentation__ ，在 __spec:env:__ 下添加以下内容：

    ```yaml
        - name: OTEL_SERVICE_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['app'] 
    ```

    ![otel-mesh](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/otel-mesh.png)

=== "完整示例如下（For Insight v0.21.x）"

    ```bash
    K8S_CLUSTER_UID=$(kubectl get namespace kube-system -o jsonpath='{.metadata.uid}')
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
        - name: OTEL_SERVICE_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['app'] 
      sampler:
        # Enum: always_on, always_off, traceidratio, parentbased_always_on, parentbased_always_off, parentbased_traceidratio, jaeger_remote, xray
        type: always_on
      java:
        image: ghcr.m.daocloud.io/openinsight-proj/autoinstrumentation-java:1.31.0
        env:
          - name: OTEL_JAVAAGENT_DEBUG
            value: "false"
          - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
            value: "true"
          - name: SPLUNK_PROFILER_ENABLED
            value: "false"
          - name: OTEL_METRICS_EXPORTER
            value: "prometheus"
          - name: OTEL_METRICS_EXPORTER_PORT
            value: "9464"
          - name: OTEL_K8S_CLUSTER_UID
            value: $K8S_CLUSTER_UID
      nodejs:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:0.41.1
      python:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.40b0
      dotnet:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-dotnet:1.0.0
      go:
        # Must set the default value manually for now.
        # See https://github.com/open-telemetry/opentelemetry-operator/issues/1756 for details.
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-go-instrumentation/autoinstrumentation-go:v0.2.2-alpha
    EOF
    ```

## 添加注解，自动接入链路

以上就绪之后，您就可以通过注解（Annotation）方式为应用程序接入链路追踪了，Otel 目前支持通过注解的方式接入链路。根据服务语言，需要添加上不同的 pod annotations。
每个服务可添加两类注解之一：

- 只注入环境变量注解

    这类注解只有一个，用于添加 otel 相关的环境变量，比如链路上报地址、容器所在的集群 id、命名空间等（这个注解在应用不支持自动探针语言时十分有用）

    ```console
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

    其中 value 被 / 分成两部分，第一个值 (insight-system) 是上一步安装的 CR 的命名空间，第二个值 (insight-opentelemetry-autoinstrumentation) 是这个 CR 的名字。

- 自动探针注入以及环境变量注入注解

    这类注解目前有 4 个，分别对应 4 种不同的编程语言：java、nodejs、python、dotnet，使用它后就会对 spec.pod 下的第一个容器注入自动探针以及 otel 默认环境变量：

    === "Java 应用"

        ```bash
          instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    === "NodeJs 应用"

        ```bash
        instrumentation.opentelemetry.io/inject-nodejs: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    === "Python 应用"

        ```bash
        instrumentation.opentelemetry.io/inject-python: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    === "Dotnet 应用"

        ```bash
        instrumentation.opentelemetry.io/inject-dotnet: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

!!! tip

    opentelemetry operator 在注入探针时会自动添加一些 OTEL 相关环境变量，同时也支持这些环境变量的覆盖。这些环境变量的覆盖优先级：

    original container env vars -> language specific env vars -> common env vars -> instrument spec configs' vars.

    但是需要避免手动覆盖 OTEL_RESOURCE_ATTRIBUTES_NODE_NAME, 它在 operator 内部作为一个 Pod 是否已经注入探针的标识，如果手动
    添加了，探针可能无法注入。


## 自动注入示例 Demo

注意这个 annotations 是加在 spec.annotations 下的。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  selector:
    matchLabels:
      app: my-app
  replicas: 1
  template:
    metadata:
      labels:
        app: my-app
      annotations:
        instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation"
    spec:
      containers:
      - name: myapp
        image: jaegertracing/vertx-create-span:operator-e2e-tests
        ports:
          - containerPort: 8080
            protocol: TCP
```

最终生成的 Yaml 内容如下：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-deployment-with-sidecar-565bd877dd-nqkk6
  generateName: my-deployment-with-sidecar-565bd877dd-
  namespace: default
  uid: aa89ca0d-620c-4d20-8bc1-37d67bad4ea4
  resourceVersion: '2668986'
  creationTimestamp: '2022-04-08T05:58:48Z'
  labels:
    app: my-pod-with-sidecar
    pod-template-hash: 565bd877dd
  annotations:
    cni.projectcalico.org/containerID: 234eae5e55ea53db2a4bc2c0384b9a1021ed3908f82a675e4a92a49a7e80dd61
    cni.projectcalico.org/podIP: 192.168.134.133/32
    cni.projectcalico.org/podIPs: 192.168.134.133/32
    instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation"
spec:
  volumes:
    - name: kube-api-access-sp2mz
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
    - name: opentelemetry-auto-instrumentation
      emptyDir: {}
  initContainers:
    - name: opentelemetry-auto-instrumentation
      image: >-
        ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java
      command:
        - cp
        - /javaagent.jar
        - /otel-auto-instrumentation/javaagent.jar
      resources: {}
      volumeMounts:
        - name: opentelemetry-auto-instrumentation
          mountPath: /otel-auto-instrumentation
        - name: kube-api-access-sp2mz
          readOnly: true
          mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      imagePullPolicy: Always
  containers:
    - name: myapp
      image: ghcr.io/pavolloffay/spring-petclinic:latest
      env:
        - name: OTEL_JAVAAGENT_DEBUG
          value: 'true'
        - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
          value: 'true'
        - name: SPLUNK_PROFILER_ENABLED
          value: 'false'
        - name: JAVA_TOOL_OPTIONS
          value: ' -javaagent:/otel-auto-instrumentation/javaagent.jar'
        - name: OTEL_TRACES_EXPORTER
          value: otlp
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: http://insight-agent-opentelemetry-collector.svc.cluster.local:4317
        - name: OTEL_EXPORTER_OTLP_TIMEOUT
          value: '20'
        - name: OTEL_TRACES_SAMPLER
          value: parentbased_traceidratio
        - name: OTEL_TRACES_SAMPLER_ARG
          value: '0.85'
        - name: SPLUNK_TRACE_RESPONSE_HEADER_ENABLED
          value: 'true'
        - name: OTEL_SERVICE_NAME
          value: my-deployment-with-sidecar
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
        - name: OTEL_RESOURCE_ATTRIBUTES
          value: >-
            k8s.container.name=myapp,k8s.deployment.name=my-deployment-with-sidecar,k8s.deployment.uid=8de6929d-dda0-436c-bca1-604e9ca7ea4e,k8s.namespace.name=default,k8s.node.name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME),k8s.pod.uid=$(OTEL_RESOURCE_ATTRIBUTES_POD_UID),k8s.replicaset.name=my-deployment-with-sidecar-565bd877dd,k8s.replicaset.uid=190d5f6e-ba7f-4794-b2e6-390b5879a6c4
        - name: OTEL_PROPAGATORS
          value: jaeger,b3
      resources: {}
      volumeMounts:
        - name: kube-api-access-sp2mz
          readOnly: true
          mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        - name: opentelemetry-auto-instrumentation
          mountPath: /otel-auto-instrumentation
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      imagePullPolicy: Always
  restartPolicy: Always
  terminationGracePeriodSeconds: 30
  dnsPolicy: ClusterFirst
  serviceAccountName: default
  serviceAccount: default
  nodeName: k8s-master3
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  schedulerName: default-scheduler
  tolerations:
    - key: node.kubernetes.io/not-ready
      operator: Exists
      effect: NoExecute
      tolerationSeconds: 300
    - key: node.kubernetes.io/unreachable
      operator: Exists
      effect: NoExecute
      tolerationSeconds: 300
  priority: 0
  enableServiceLinks: true
  preemptionPolicy: PreemptLowerPriority
```

## 链路查询

如何查询已经接入的服务，参考[链路查询](../../user-guide/trace/trace.md)。
