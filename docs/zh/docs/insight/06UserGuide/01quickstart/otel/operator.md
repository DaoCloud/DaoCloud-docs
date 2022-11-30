# 通过 Operator 实现应用程序无侵入增强

> 目前只有 Java、NodeJs、Python、.Net 支持 Operator 的方式无侵入接入，Golang 后续会完善。

## 前提条件

请确保 Insight Agent 已经就绪。如若没有，请参考[安装 insight-agent 采集数据](../installagent.md) 并确保以下三项就绪：

- 为 Insight-agent 开启 trace 功能
- trace 数据的地址以及端口是否填写正确
- deployment/opentelemetry-operator-controller-manager 和 deployment/insight-agent-opentelemetry-collector 对应的 Pod 已经准备就绪

## 安装 Instrumentation CR

在 Insight-System 命名空间下安装，如已安装可跳过该步骤：

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
    image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python::0.33b0
EOF
```

## 添加注解，自动接入链路

以上就绪之后，您就可以通过注解（Annotation）方式为应用程序接入链路追踪了，Otel 目前支持通过注解的方式接入链路。根据服务语言，需要添加上不同的 pod annotations。
每个服务可添加两类注解之一：

- 只注入环境变量注解

    这类注解只有一个，用于添加 otel 相关的环境变量，比如链路上报地址、容器所在的集群 id、命名空间等（这个注解在应用不支持自动探针语言时十分有用）

    ```bash
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

    其中 value 被 / 分成两部分，第一个值(insight-system) 是上一步安装的 CR 的命名空间，第二个值(insight-opentelemetry-autoinstrumentation) 是这个 CR 的名字。

- 自动探针注入以及环境变量注入注解

    这类注解目前有 4 个，分别对应 4 种不同的编程语言：java、nodejs、python、dotnet，使用它后就会对 spec.pod 下的第一个容器注入自动探针以及 otel 默认环境变量：

    1. Java 应用

        ```bash
          instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    2. NodeJs 应用

        ```bash
        instrumentation.opentelemetry.io/inject-nodejs: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    3. Python 应用

        ```bash
        instrumentation.opentelemetry.io/inject-python: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    4. Dotnet 应用

        ```bash
       暂不支持，社区bug修复中... 
       ```

## 自动注入示例 Demo

> 注意这个 annotations 是加在 spec.annotations 下的。

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
    instrumentation.opentelemetry.io/inject-java: 'true'
    sidecar.opentelemetry.io/inject: 'false'
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

如何查询已经接入的服务，参考[链路查询](../../04dataquery/tracequery.md)。

