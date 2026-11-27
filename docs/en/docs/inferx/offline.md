# Install Turbo Inference in Offline Environment

*[InferX]: The development codename for Turbo Inference

## Download and Extract Turbo Inference Offline Package

1. Helm
2. [helm-cm-push](https://github.com/chartmuseum/helm-push)
3. [dt](https://github.com/vmware-labs/distribution-tooling-for-helm)
4. inferx charts and images tgz
5. values.yaml
6. README.md

### Extracted Directory Structure

```text
.
├── bin/                        # Executable tools
│   ├── dt
│   ├── helm
│   └── helm-cm-push
├── examples/                   # Example configuration files
│   ├── inference-scheduling/
│   ├── multi-node/
│   └── pd-disaggregation/
├── inferx-0.1.0.wrap.tgz       # InferX Charts and images package file
└── README.md                   # Project documentation
```

## Sync Turbo Inference to Offline Image Registry

1.  Login to the offline registry (optional)

    ```bash
    bin/dt auth login demo.harbor.io --username ${username} --password ${password}
    ```

2. Sync Turbo Inference charts & images

    ```bash
    bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --yes
    ```

3. Skip TLS verification (optional)

    ```bash
    bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --insecure --yes
    ```

## Deploy Turbo Inference values.yaml

Configure the following parameters based on your actual environment and create a custom values file. For a configuration example, refer to values.yaml in the `examples/` directory:

<details>
<summary>Full values.yaml example (click to expand/collapse)</summary>

```yaml title="values.yaml"
# Chart-root escape hatch for arbitrary manifests (ConfigMap, Secret, …).
# Each list item is a full document; string values are rendered with tpl.
extraObjects: []

# Dynamo backend composition (DynamoGraphDeployment + helpers).
# When enabled, typically disable llm-d-modelservice / inferencepool and keep llm-d-infra for Gateway.
dynamo:
  enabled: false
  # Per-model monitoring, scoped to the current DGD like llm-d's model monitor.
  # Disable Dynamo platform monitors for the same endpoints when enabling this.
  monitoring:
    podMonitor:
      enabled: false
      labels:
        operator.insight.io/managed-by: insight
      interval: 30s
      frontend:
        port: http
        path: /metrics
      worker:
        port: system
        path: /metrics
      nixl:
        enabled: false
        port: nixl
        path: /metrics
  # Optional per-type image overrides. When unset, the chart uses the
  # Chart images annotation, which the catalog release tooling keeps in
  # sync with the chart.
  # Thin shared defaults injected into worker (prefill/decode/worker) podTemplates when fields are unset.
  defaults:
    # Optional shared fallback; explicit and per-type images take precedence.
    # image: ""
    affinity: {}
    volumes: []
    volumeMounts: []
    envFrom: []
    probes:
      startupProbe: {}
      livenessProbe: {}
      readinessProbe: {}
  extras:
    pvc:
      create: false
      name: model-cache
      accessModes:
        - ReadWriteMany
      size: 3000Gi
      storageClassName: ""
    httpRoute:
      enabled: true
      # Defaults to {{ .Release.Name }}-inference-gateway when empty.
      parentGatewayName: ""
      # Defaults to {{ dgd.metadata.name }}-frontend when empty.
      backendServiceName: ""
      backendPort: 8000
  dgd:
    apiVersion: nvidia.com/v1beta1
    metadata:
      name: ""
      labels: {}
      annotations: {}
    # Raw DynamoGraphDeploymentSpec (components, env, backendFramework, …).
    spec: {}

llm-d-infra:
  enabled: true
  llm-d-infra:
    # -- Gateway configuration
    # @default -- See below
    gateway:
      # -- Gateway class that determines the backend used
      # Currently supported values: "kgateway" or "agentgateway-v2" for kgateway, "istio"
      gatewayClassName: istio

      # -- String to fully override common.names.fullname
      fullnameOverride: ""

      # -- String to partially override common.names.fullname
      nameOverride: "inference-gateway"

llm-d-router-gateway:
  enabled: true
  llm-d-router-gateway:
    router:
      modelServers:
        type: vllm
        targetPorts:
          - number: 8000
        matchLabels:
          app: inferx
      epp:
        replicas: 1
        image:
          registry: ghcr.m.daocloud.io
          repository: llm-d/llm-d-router-endpoint-picker
          tag: v1.0.0
          pullPolicy: IfNotPresent
        extProcPort: 9002
        pluginsConfigFile: "inferx-default-plugins.yaml"
        pluginsCustomConfig:
          inferx-default-plugins.yaml: |
            apiVersion: llm-d.ai/v1
            kind: EndpointPickerConfig
            plugins:
            - type: queue-scorer
            schedulingProfiles:
            - name: default
              plugins:
              - pluginRef: queue-scorer
                weight: 1.0
          pd-config.yaml: |
            # ALWAYS DO PD IN THIS EXAMPLE (THRESHOLD 0)
            apiVersion: llm-d.ai/v1
            kind: EndpointPickerConfig
            plugins:
            - type: prefill-filter
            - type: decode-filter
            - type: max-score-picker
            - type: queue-scorer
            - type: always-disagg-pd-decider
            - type: disagg-profile-handler
              parameters:
                deciders:
                  prefill: always-disagg-pd-decider
            schedulingProfiles:
            - name: prefill
              plugins:
              - pluginRef: prefill-filter
              - pluginRef: queue-scorer
                weight: 1.0
              - pluginRef: max-score-picker
            - name: decode
              plugins:
              - pluginRef: decode-filter
              - pluginRef: queue-scorer
                weight: 1.0
              - pluginRef: max-score-picker
        flags:
          # -- Interval to refresh metrics from inference endpoints
          refresh-metrics-interval: 1s
          # -- Interval to flush Prometheus metrics, must be greater than refresh-metrics-interval
          metrics-staleness-threshold: 5s
      monitoring:
        # Prometheus ServiceMonitor will be created when enabled for EPP metrics collection
        prometheus:
          enabled: true
          auth:
            enabled: false
          # additional labels for the ServiceMonitor
          extraLabels:
            operator.insight.io/managed-by: insight
    # Options: ["gke", "istio", "none"]
    provider:
      name: istio

    httpRoute:
      create: true # a flag to indicate whether to create the httproute as part of the chart or not.
      inferenceGatewayName: ""
      requestTimeout: "1800s"

llm-d-modelservice:
  enabled: true
  llm-d-modelservice:
    modelArtifacts:
      # name is the value of the model parameter in OpenAI requests
      # Required
      name: ""
      # Labels that will be added to the pods serving the model.
      # These should match the labels of any associated InferencePool
      # In addition, the label llm-d.ai/role will be added with the value 'prefill'
      # or 'decode' depending on the role of the pod.
      labels:
        app: inferx
        llm-d.ai/inference-serving: "true"
      # model URI. One of:
      #   hf://model/name - model as defined on Hugging Face
      #   pvc://pvc_name/path/to/model - model on existing persistant storage volume
      #   oci:// not yet supported
      uri: ""
      # size of volume to create to hold the model
      size: 5Mi
      # name of secret containing credentials for accessing the model (e.g., HF_TOKEN)
      authSecretName: ""
      # location where model volume will be mounted (used when mountModelVolume: true)
      mountPath: /model-cache

    # When true, a LeaderWorkerSet is used instead of a Deployment
    multinode: true
    # Global accelerator configuration
    # Supported types: nvidia, huawei, intel-i915, intel-xe, intel-gaudi, amd, google, cpu
    accelerator:
      # Type of accelerator to use
      type: nvidia
      # Enable Dynamic Resource Allocation (DRA) for accelerators
      # When true, uses resourceClaimTemplates instead of device plugin resources
      dra: false
      # Resource names for different accelerator types (used when dra: false)
      resources:
        nvidia: "nvidia.com/gpu"
        huawei: "huawei.com/npu"
        hami: "nvidia.com/vgpu"
        intel-i915: "gpu.intel.com/i915"
        intel-xe: "gpu.intel.com/xe"
        intel-gaudi: "habana.ai/gaudi"
        amd: "amd.com/gpu"
        google: "google.com/tpu"

    # Describe routing requirements. In addition to service level routing (OpenAI model name, service port)
    # also describes elements for Gateway API Inference Extension configuration
    routing:
      # port the inference engine (vLLM) listens
      # when a sidecar (proxy) is used it will listen on this port and forward to VLLM on proxy.targetPort
      servicePort: 8000
      # Configuration of VLLM routing sidecar
      # cf. https://github.com/llm-d/llm-d-routing-sidecar/
      proxy:
        enabled: false
        image:
          registry: ghcr.m.daocloud.io
          repository: llm-d/llm-d-router-disagg-sidecar
          tag: v1.0.0
        imagePullPolicy: IfNotPresent
        # target port on which VLLM should listen
        targetPort: 8200
        # Specify a connector. For example, `nixl`, `nixlv2`
        connector: nixlv2
        # Boolean: adds the `--secure-proxy` flag to the routingSidecar with your chosen value.  Arg is ommitted by default for compatability with legacy sidecar images.
        secure: false

    decode:
      create: false

    prefill:
      create: false

    encode:
      create: false
```

</details>

| Note | Description |
| -------- | ---- |
| Label consistency | `router.modelServers.matchLabels.app` under `llm-d-router-gateway` must match `modelArtifacts.labels.app` under `llm-d-modelservice`. It is recommended to use the Helm Release Name, otherwise the model service Pods may not be matched or multiple Pods may be matched. |
| Non-istio environment | Set `provider.name` under `llm-d-router-gateway` to `none`, and adjust `gateway.gatewayClassName` under `llm-d-infra` accordingly. |
| Inference scheduling plugins | `epp.pluginsConfigFile` supports the built-in `inferx-default-plugins.yaml`, `pd-config.yaml`, and `default-plugins.yaml`, where `pd-config.yaml` is used for PD disaggregation scenarios. |
| Model weights | `modelArtifacts.uri` supports both `hf://model/name` (Hugging Face) and `pvc://pvc_name/path/to/model` (persistent storage). |
| PD disaggregation | After setting `routing.proxy.enabled` to `true`, the proxy sidecar will be injected into the decode pod; you also need to set `decode.create` to `true`. |

### Install Turbo Inference

```bash
bin/helm install inferx oci://demo.harbor.io/test_repo/inferx --version 0.1.0 --namespace public --create-namespace -f values.yaml
```

### Install via Kpanda UI (Optional)

To install graphically via Kpanda, first push the Chart to a Chart Museum-compatible repository:

```bash
bin/helm fetch oci://demo.harbor.io/test_repo/inferx --version 0.1.0
bin/helm-cm-push inferx-0.1.0.tgz https://demo.harbor.io/chartrepo/test_repo --username ${username} --password ${password}
```

After the above commands execute successfully, add the corresponding Helm repository in the Kpanda **Helm Apps** -> **Helm Charts** page, then deploy Turbo Inference in **Helm Apps** -> **Helm Templates**.
