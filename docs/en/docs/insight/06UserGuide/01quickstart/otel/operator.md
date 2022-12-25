# Implement non-intrusive enhancement of applications via Operator

At present, only Java, NodeJs, Python, and .Net support the non-intrusive access of Operator, and Golang will be improved in the future.

## Prerequisites

Make sure insight-agent is ready. If not, please refer to [Install insight-agent to collect data](../installagent.md) and make sure the following three items are in place:

- Enable trace function for insight-agent
- Whether the address and port of the trace data are filled in correctly
- Pods corresponding to deployment/opentelemetry-operator-controller-manager and deployment/insight-agent-opentelemetry-collector are ready

## Install Instrumentation CR

Install under the Insight-System namespace, if it is already installed, you can skip this step (Insight 0.13.0+ can also skip this step):

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
    image: ghcr.m.daocloud.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:0.33b0
EOF
```

## Add annotations to automatically access links

After the above is ready, you can access link tracking for the application through annotations (Annotation). Otel currently supports accessing links through annotations. Depending on the service language, different pod annotations need to be added.
Each service can add one of two types of annotations:

- Only inject environment variable annotations

    There is only one such annotation, which is used to add otel-related environment variables, such as link reporting address, cluster id where the container is located, namespace, etc. (this annotation is very useful when the application does not support automatic probe language)

    ```bash
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

    The value is divided into two parts by /, the first value (insight-system) is the namespace of the CR installed in the previous step, and the second value (insight-opentelemetry-autoinstrumentation) is the name of the CR.

- Automatic probe injection and environment variable injection annotations

    There are currently 4 such annotations, corresponding to 4 different programming languages: java, nodejs, python, dotnet. After using it, automatic probes and otel default environment variables will be injected into the first container under spec.pod:

    1. Java application

        ```bash
        instrumentation.opentelemetry.io/inject-java: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    2. NodeJs application

        ```bash
        instrumentation.opentelemetry.io/inject-nodejs: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    3. Python application

        ```bash
        instrumentation.opentelemetry.io/inject-python: "insight-system/insight-opentelemetry-autoinstrumentation"
        ```

    4. Dotnet application

        ```bash
       Not supported yet, community bug fixes...
       ```

## Automatic injection example Demo

Note that annotations are added under spec.annotations.

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
      -name: myapp
        image: jaegertracing/vertx-create-span:operator-e2e-tests
        ports:
          - containerPort: 8080
            protocol: TCP
```

The final generated Yaml content is as follows:

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
        -cp
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
    -name: myapp
      image: ghcr.io/pavolloffay/spring-petclinic:latest
      env:
        - name: OTEL_JAVAAGENT_DEBUG
          value: 'true'
        - name: OTEL_INSTRUMENTATION_JDBC_ENABLED
          value: 'true'
        - name: SPLUNK_PROFILER_ENABLED
          value: 'false'
        - name: JAVA_TOOL_OPTIONS
          value: '-javaagent:/otel-auto-instrumentation/javaagent.jar'
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
            k8s.container.name=myapp,k8s.deployment.name=my-deployment-with-sidecar,k8s.deployment.uid=8de6929d-dda0-436c-bca1-604e9ca7ea4e,k8s.namespace.name=default,k8s.node. name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME),k8s.pod.uid=$(OTEL_RESOURCE_ATTRIBUTES_POD_UID),k8s.replicaset.name=my-deployment-with-sidecar-565bd877pld,k8 =190d5f6e-ba7f-4794-b2e6-390b5879a6c4
        - name: OTEL_PROPAGATORS
          value: jaeger, b3
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

## Trace query

How to query the connected services, refer to [Trace Query](../../04dataquery/tracequery.md).
