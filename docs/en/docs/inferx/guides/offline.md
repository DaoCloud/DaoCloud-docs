# Install InferX in Offline Environment

## Download and Extract InferX Offline Package

1. helm
2. [helm-cm-push](https://github.com/chartmuseum/helm-push)
3. [dt](https://github.com/vmware-labs/distribution-tooling-for-helm)
4. inferx charts & images tgz
5. example values yaml
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

## Sync InferX to Offline Image Registry

### Login to Offline Registry (Optional)

```bash
bin/dt auth login demo.harbor.io --username ${username} --password ${password}
```

### Sync InferX Charts & Images

```bash
bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --yes
```

### Skip TLS Verification (Optional)

```bash
bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --insecure --yes
```

## Deploy InferX

Configure the following parameters according to your actual environment and create a custom values file. Configuration examples can be found in the values files under the `examples/` directory.

### Prepare Helm Values YAML

| Full Path | Default Value | Description |
|--------|-------|------|
| `llm-d-infra.llm-d-infra.gateway.gatewayClassName` | `istio` | Configure gatewayclass, supports istio, gatewayclass |
| `inferencepool.inferencepool.inferenceExtension.pluginsConfigFile` | `inferx-default-plugins.yaml` | Configure the inferencepool plugin config file yaml name. Built-in options: inferx-default-plugins.yaml, pd-config.yaml, default-plugins.yaml |
| `inferencepool.inferencepool.inferencePool.apiVersion` | `inference.networking.k8s.io/v1` | Configure the inferencePool version supported by gatewayclass. Can be set to inference.networking.k8s.io/v1 or inference.networking.x-k8s.io/v1alpha2 |
| `inferencepool.inferencepool.inferencePool.modelServers.matchLabels.app` | `inferx` | Configure the Label selector for inferencepool and model service Pods. Must match the `app` label of model service Pods. Recommended to use Helm Release Name, otherwise model service Pods may not be matched or multiple may be matched. Can be set via `llm-d-modelservice.llm-d-modelservice.modelArtifacts.labels.app` |
| `inferencepool.inferencepool.provider.name` | `istio` | Configure the provider used by inferencepool. Currently supports istio, none. Set to none for non-istio environments |
| `llm-d-modelservice.llm-d-modelservice.modelArtifacts.labels.app` | `inferx` | Configure labels for model service Pods. Ensure inferencepool.inferencepool.inferencePool.modelServers.matchLabels.app matches this. Recommended to use Helm Release Name |
| `llm-d-modelservice.llm-d-modelservice.modelArtifacts.uri` | `-` | Configure model weights, supports HF, PVC |
| `llm-d-modelservice.llm-d-modelservice.modelArtifacts.name` | `-` | Configure model name, used to identify vllm served-model-name. Only effective when modelCommand is not custom |
| `llm-d-modelservice.llm-d-modelservice.accelerator.type` | `nvidia` | Configure hami vgpu usage |
| `llm-d-modelservice.llm-d-modelservice.routing.proxy.enabled` | `false` | Configure PD disaggregation proxy sidecar. The sidecar will be injected into the decode pod |

### Install InferX

```bash
bin/helm install inferx oci://demo.harbor.io/test_repo/inferx --version 0.1.0 --namespace public --create-namespace -f values.yaml
```

### Install via Kpanda UI (Optional)

To install graphically via Kpanda, first push the Chart to a Chart Museum-compatible repository:

```bash
bin/helm fetch oci://demo.harbor.io/test_repo/inferx --version 0.1.0
bin/helm-cm-push inferx-0.1.0.tgz https://demo.harbor.io/chartrepo/test_repo --username ${username} --password ${password}
```

After the above commands execute successfully, add the corresponding Helm repository in Kpanda Helm Applications -> Helm Repositories, then deploy InferX in Helm Applications -> Helm Templates.
