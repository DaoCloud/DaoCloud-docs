# Enhance Go apps with OTel auto-instrumentation

If you don't want to manually change the application code, you can try This page's eBPF-based automatic enhancement method.
This feature is currently in the review stage of donating to the OpenTelemetry community, and does not support Operator injection through annotations (it will be supported in the future), so you need to manually change the Deployment YAML or use a patch.

## Prerequisites

Make sure Insight Agent is ready. If not, see [Install insight-agent to collect data](../install/install-agent.md) and make sure the following three items are in place:

- Enable trace feature for Insight-agent
- Whether the address and port of the trace data are filled in correctly
- Pods corresponding to deployment/opentelemetry-operator-controller-manager and deployment/insight-agent-opentelemetry-collector are ready

## Install Instrumentation CR

Install under the Insight-system namespace, skip this step if it has already been installed.

Note: This CR currently only supports the injection of environment variables (including service name, link reporting address, etc.) required to connect to Insight, and will support the injection of Golang probes in the future.

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

## Change the application deployment file

- Add environment variable annotations

    There is only one such annotation, which is used to add OpenTelemetry-related environment variables, such as link reporting address, cluster id where the container is located, namespace, etc.:

    ```bash
    instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

    The value is divided into two parts by `/`, the first value `insight-system` is the namespace of the CR installed in the second step, and the second value `insight-opentelemetry-autoinstrumentation` is the name of the CR.

- Add golang ebpf probe container

    Here is sample code:

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

    1. Used to add environment variables related to OpenTelemetry.
    2. Assuming this is your Golang application.
    3. Note that it should be consistent with the content of the `command` mentioned above:
       `/usr/local/bin/emojivoto-voting-svc`.

The final generated Yaml content is as follows:

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

## Reference

- [Getting Started with Go OpenTelemetry Automatic Instrumentation](https://github.com/keyval-dev/opentelemetry-go-instrumentation/blob/master/docs/getting-started/README.md)
- [Donating ebpf based instrumentation](https://github.com/open-telemetry/opentelemetry-go-instrumentation/pull/4)
