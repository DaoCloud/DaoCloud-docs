# 离线环境安装推理加速

*[InferY]: 推理加速服务的开发代号

## 下载并解压推理加速离线包

1. Helm
2. [helm-cm-push](https://github.com/chartmuseum/helm-push)
3. [dt](https://github.com/vmware-labs/distribution-tooling-for-helm)
4. inferx charts 和 images tgz
5. values.yaml
6. README.md

### 解压后的目录结构

```text
.
├── bin/                        # 可执行工具
│   ├── dt                      
│   ├── helm                    
│   └── helm-cm-push            
├── examples/                   # 示例配置文件
│   ├── inference-scheduling/
│   ├── multi-node/
│   └── pd-disaggregation/
├── inferx-0.1.0.wrap.tgz       # Charts 及镜像打包文件
└── README.md                   # 项目说明文档
```

## 同步推理加速到离线镜像仓库

1.  登录离线 Registry (可选)

    ```bash
    bin/dt auth login demo.harbor.io --username ${username} --password ${password}
    ```

2. 同步推理加速 charts & images

    ```bash
    bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --yes
    ```

3. 跳过 TLS 验证 (可选)

    ```bash
    bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --insecure --yes
    ```

## 部署推理加速 values.yaml

根据实际环境配置以下参数，并创建自定义 values 文件。配置示例可参考 `examples/` 目录中的 values.yaml：

<details>
<summary>values.yaml 完整示例（点击展开/收起）</summary>

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

| 注意事项 | 说明 |
| -------- | ---- |
| Label 一致性 | `llm-d-router-gateway` 下 `router.modelServers.matchLabels.app` 必须与 `llm-d-modelservice` 下 `modelArtifacts.labels.app` 一致，建议使用 Helm Release Name，否则将无法匹配到模型服务 Pod 或者匹配到多个模型服务 Pod。 |
| 非 istio 环境 | 将 `llm-d-router-gateway` 下 `provider.name` 设置为 `none`，并同步调整 `llm-d-infra` 下 `gateway.gatewayClassName`。 |
| 推理调度插件 | `epp.pluginsConfigFile` 支持内置的 `inferx-default-plugins.yaml`、`pd-config.yaml`、`default-plugins.yaml`，其中 `pd-config.yaml` 用于 PD 分离场景。 |
| 模型权重 | `modelArtifacts.uri` 支持 `hf://model/name`（Hugging Face）与 `pvc://pvc_name/path/to/model`（持久化存储）两种形式。 |
| PD 分离 | 将 `routing.proxy.enabled` 设置为 `true` 后，proxy sidecar 会注入到 decode pod，同时需将 `decode.create` 设置为 `true`。 |

### 安装推理加速

```bash
bin/helm install inferx oci://demo.harbor.io/test_repo/inferx --version 0.1.0 --namespace public --create-namespace -f values.yaml
```

### 在 Kpanda 界面安装 (可选)

如需通过 Kpanda 进行图形化安装，请先将 Chart 推送至支持 Chart Museum 仓库：

```bash
bin/helm fetch oci://demo.harbor.io/test_repo/inferx --version 0.1.0
bin/helm-cm-push inferx-0.1.0.tgz https://demo.harbor.io/chartrepo/test_repo --username ${username} --password ${password}
```

上述命令执行成功后，请将对应 Helm 仓库添加至 Kpanda **Helm 应用** -> **Helm 仓库** 界面，随后可在 **Helm 应用** -> **Helm 模板** 中完成推理加速部署。
