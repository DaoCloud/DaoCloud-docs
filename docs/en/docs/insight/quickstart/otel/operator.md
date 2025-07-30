---
MTPE: windsonsea
Date: 2024-10-16
---

# Enhance Applications Non-Intrusively with Operators

Currently, only Java, Node.js, Python, .NET, and Golang support non-intrusive integration through the Operator approach.

## Prerequisites

Please ensure that the insight-agent is ready. If not, please refer to
[Install insight-agent for data collection](../install/install-agent.md)
and make sure the following three items are ready:

- Enable trace functionality for insight-agent
- Check if the address and port for trace data are correctly filled
- Ensure that the Pods corresponding to deployment/insight-agent-opentelemetry-operator and
  deployment/insight-agent-opentelemetry-collector are ready

## Install Instrumentation CR

!!! tip

    Starting from Insight v0.22.0, there is no longer a need to manually install the Instrumentation CR.

Install it in the insight-system namespace. There are some minor differences between different versions.

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

## Works with the Service Mesh Product (Mspider)

If you enable the tracing capability of the Mspider(Service Mesh), you need to add an additional environment variable injection configuration:

### The operation steps

1. Log in to DCE 5.0, then enter __Container Management__ and select the target cluster.
2. Click __CRDs__ in the left navigation bar, find __instrumentations.opentelemetry.io__, and enter the details page.
3. Select the __insight-system__ namespace, then edit __insight-opentelemetry-autoinstrumentation__, and add the following content under `spec:env:`:

    ```yaml
        - name: OTEL_SERVICE_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['app'] 
    ```

    The complete example (for Insight v0.21.x) is as follows:

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

## Add annotations to automatically access traces

After the above is ready, you can access traces for the application through annotations (Annotation). 
Otel currently supports accessing traces through annotations. Depending on the service language, 
different pod annotations need to be added. Each service can add one of two types of annotations:

- Only inject environment variable annotations

    There is only one such annotation, which is used to add otel-related environment variables, such as link reporting address, cluster id where the container is located, and namespace (this annotation is very useful when the application does not support automatic probe language)

    ```yaml
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

    The value is divided into two parts by `/`, the first value (insight-system) is the namespace of 
    the CR installed in the previous step, and the second value (insight-opentelemetry-autoinstrumentation) 
    is the name of the CR.

- Automatic probe injection and environment variable injection annotations

    There are currently 4 such annotations, corresponding to 4 different programming languages: java, nodejs, 
    python, dotnet. After using it, automatic probes and otel default environment variables will be 
    injected into the first container under spec.pod:

    === "Java"

        ```yaml
        instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    === "Node.js"

        ```yaml
        instrumentation.opentelemetry.io/inject-nodejs: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    === "Python"

        ```yaml
        instrumentation.opentelemetry.io/inject-python: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    === ".NET"

        ```yaml
        instrumentation.opentelemetry.io/inject-dotnet: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    === "Golang"

        Since Go's automatic detection requires the setting of [OTEL_GO_AUTO_TARGET_EXE](https://github.com/open-telemetry/opentelemetry-go-instrumentation/blob/main/docs/how-it-works.md), 
        you must provide a valid executable path through annotations or Instrumentation resources. 
        Failure to set this value will result in the termination of Go's automatic detection injection, 
        leading to a failure in the connection trace.

        ```yaml
        instrumentation.opentelemetry.io/inject-go: "insight-system/insight-opentelemetry-autoinstrumentation"
        instrumentation.opentelemetry.io/otel-go-auto-target-exe: "/path/to/container/executable"
        ```
        
        Go's automatic detection also requires elevated permissions. The following permissions are automatically set and are necessary.
        
        ```yaml
        securityContext:
          privileged: true
          runAsUser: 0
        ```

!!! tip

    The OpenTelemetry Operator automatically adds some OTel-related environment variables when 
    injecting probes and also supports overriding these variables. The priority order for overriding 
    these environment variables is as follows:

    ```text
    original container env vars -> language specific env vars -> common env vars -> instrument spec configs' vars
    ```

    However, it is important to avoid manually overriding __OTEL_RESOURCE_ATTRIBUTES_NODE_NAME__ .
    This variable serves as an identifier within the operator to determine if a pod has already
    been injected with a probe. Manually adding this variable may prevent the probe from being
    injected successfully.

## Automatic injection Demo

Note that the `annotation` is added under spec.annotations.

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
        image: ghcr.io/pavolloffay/spring-petclinic:latest
        ports:
          - containerPort: 8080
            protocol: TCP
```

The final generated YAML is as follows:

```diff
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
    app: my-app
  annotations:
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
+   - name: opentelemetry-auto-instrumentation-java
+     emptyDir:
+       sizeLimit: 200Mi      
+ initContainers:
+   - name: opentelemetry-auto-instrumentation-java
+     image: ghcr.m.daocloud.io/openinsight-proj/autoinstrumentation-java:1.45.0-eb49d21116a1d8fbf0d9080adddad3a367e68a5e
+     imagePullPolicy: IfNotPresent
+     command:
+       - cp
+       - /javaagent.jar
+       - /otel-auto-instrumentation-java/javaagent.jar
+     resources:
+       limits:
+         cpu: 500m
+         memory: 64Mi
+       requests:
+         cpu: 50m
+         memory: 64Mi
+     terminationMessagePath: /dev/termination-log
+     terminationMessagePolicy: File
+     volumeMounts:
+       - name: opentelemetry-auto-instrumentation-java
+         mountPath: /otel-auto-instrumentation-java
+       - name: kube-api-access-sp2mz
+         readOnly: true
+         mountPath: /var/run/secrets/kubernetes.io/serviceaccount
  containers:
    - name: myapp
      image: ghcr.io/pavolloffay/spring-petclinic:latest
      imagePullPolicy: Always
      ports:
        - containerPort: 8080
          protocol: TCP
+     env:
+       - name: OTEL_JAVAAGENT_DEBUG
+         value: "false"
+       - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
+         value: "true"
+       - name: SPLUNK_PROFILER_ENABLED
+         value: "false"
+       - name: JAVA_TOOL_OPTIONS
+         value: ' -javaagent:/otel-auto-instrumentation-java/javaagent.jar'
+       - name: OTEL_EXPORTER_OTLP_ENDPOINT
+         value: http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317
+       - name: OTEL_NODE_IP
+         valueFrom:
+           fieldRef:
+             apiVersion: v1
+             fieldPath: status.hostIP
+       - name: OTEL_POD_IP
+         valueFrom:
+           fieldRef:
+             apiVersion: v1
+             fieldPath: status.podIP
+       - name: OTEL_K8S_CLUSTER_UID
+         value: 416d133f-d00a-43e1-b859-f1839a5a93ee
+       - name: OTEL_EXPORTER_OTLP_PROTOCOL
+         value: grpc
+       - name: OTEL_K8S_NAMESPACE_NAME
+         valueFrom:
+           fieldRef:
+             apiVersion: v1
+             fieldPath: metadata.namespace
+       - name: OTEL_LOGS_EXPORTER
+         value: none
+       - name: OTEL_METRICS_EXPORTER
+         value: prometheus
+       - name: OTEL_EXPORTER_PROMETHEUS_PORT
+         value: "9464"
+       - name: OTEL_SERVICE_NAME
+         value: my-app
+       - name: OTEL_RESOURCE_ATTRIBUTES_POD_NAME
+         valueFrom:
+           fieldRef:
+             apiVersion: v1
+             fieldPath: metadata.name
+       - name: OTEL_PROPAGATORS
+         value: tracecontext,baggage,b3,b3multi,jaeger,xray,ottrace
+       - name: OTEL_TRACES_SAMPLER
+         value: always_on
+       - name: OTEL_RESOURCE_ATTRIBUTES_POD_UID
+         valueFrom:
+           fieldRef:
+             apiVersion: v1
+             fieldPath: metadata.uid
+       - name: OTEL_RESOURCE_ATTRIBUTES_NODE_NAME
+         valueFrom:
+           fieldRef:
+             apiVersion: v1
+             fieldPath: spec.nodeName
+       - name: OTEL_RESOURCE_ATTRIBUTES
+         value: k8s.container.name=myapp,k8s.deployment.name=my-app,k8s.deployment.uid=25ce570c-8401-4f07-b8a9-dd64fcf3a1d1,k8s.namespace.name=default,k8s.node.name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME),k8s.pod.uid=$(OTEL_RESOURCE_ATTRIBUTES_POD_UID),k8s.replicaset.name=my-app-54fc75999c,k8s.replicaset.uid=56358d62-1321-4a62-b2e9-34132988efa0,service.instance.id=default.$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME).myapp,service.version=latest
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
        - name: kube-api-access-sp2mz
          readOnly: true
          mountPath: /var/run/secrets/kubernetes.io/serviceaccount
+       - name: opentelemetry-auto-instrumentation-java
+         mountPath: /otel-auto-instrumentation-java
```

🔔 Automatically injected YAML may not be entirely consistent across different versions."

## Trace query

How to query the connected services, refer to [Trace Query](../../user-guide/trace/trace.md).

## Installing Multiple Instrumentation CRs to Support Differentiated Configuration

The previously mentioned instrumentation CR is a built-in, general-purpose configuration provided by Insight.
In real-world scenarios, to meet differentiated configuration needs, you can install multiple Instrumentation CRs
with different names and reference them as needed.

Typical use cases include:

1. **Environment isolation** : Different configurations for sampling rate, exporter endpoints, etc., in dev/test/prod environments.
2. **Team/business unit isolation** : Different teams may have separate requirements for telemetry data storage or resource tagging.
3. **Service type differentiation** : Frontend, backend, and data-processing services may require different sampling rates or metric scopes.
4. **Granular sampling strategy** : Apply lower sampling for high-throughput services and full sampling for critical paths to reduce overhead.
5. **Canary releases and testing** : Use a new CR to test configuration changes, and gradually replace the old configuration after validation.
6. **Namespace isolation** : Use separate CRs for services in different namespaces to avoid configuration interference.
7. **Compliance requirements** : EU services need to send data to collectors within the EU to comply with GDPR.
8. **Resource tagging differentiation** : Add custom tags (e.g., `team: a`, `env: prod`) for different service groups.

**Core principle** : Use multiple CRs to "divide and conquer," avoiding the limitations of a single configuration when handling multidimensional needs.

### Examples

1. Create another `insight-opentelemetry-autoinstrumentation-debug` Instrumentation CR for Project Group B to test a new Java Agent version:

    ```yaml
    apiVersion: opentelemetry.io/v1alpha1
    kind: Instrumentation
    metadata:
      name: insight-opentelemetry-autoinstrumentation-debug # 👈 Used to distinguish between different Instrumentation CRs
      namespace: insight-system
    spec:
      java:
        image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:my-debug-xx.xx # 👈 Image version for testing
        ······
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
        ······  
    ```

2. Update the service’s annotation to use `insight-system/insight-opentelemetry-autoinstrumentation-debug`:

    ```yaml
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation-debug"
    ```
