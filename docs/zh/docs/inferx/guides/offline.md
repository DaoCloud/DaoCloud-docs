# 离线环境安装 Inferx

## 下载并解压 Inferx 离线包
1. helm
2. [helm-cm-push](https://github.com/chartmuseum/helm-push)
3. [dt](https://github.com/vmware-labs/distribution-tooling-for-helm)
4. inferx charts & images tgz
5. example values yaml
6. README.md

### 解压后的目录结构如下：
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
├── inferx-0.1.0.wrap.tgz       # InferX Charts 及镜像打包文件
└── README.md                   # 项目说明文档
```

## 同步 Inferx 到离线镜像仓库

#### 登录离线 Registry (可选)
```bash
bin/dt auth login demo.harbor.io --username ${username} --password ${password}
```

### 同步 Inferx charts & images
```bash
bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --yes
```
#### 跳过 TLS 验证 (可选)
```bash
bin/dt unwrap inferx-0.1.0.wrap.tgz oci://demo.harbor.io/test_repo --insecure --yes
```

## 部署 Inferx

请根据实际环境配置以下参数，并创建自定义 values 文件。配置示例可参考 `examples/` 目录中的 values 文件。

### 准备 helm values yaml
| 完整路径                                                                     | 默认值                              | 说明                                                                                                                                                                                                |    
|--------------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `llm-d-infra.llm-d-infra.gateway.gatewayClassName`                       | `istio`                          | 配置 gatewayclass，支持 istio， gatewayclass                                                                                                                                                            |                                                          |
| `inferencepool.inferencepool.inferenceExtension.pluginsConfigFile`       | `inferx-default-plugins.yaml`    | 配置 inferencepool plugin 配置文件的 yaml 名称，目前内置 inferx-default-plugins.yaml，pd-config.yaml，default-plugins.yaml                                                                                        |
| `inferencepool.inferencepool.inferencePool.apiVersion`                   | `inference.networking.k8s.io/v1` | 配置 gatewayclass 支持的 inferencePool 版本，可以指定为 inference.networking.k8s.io/v1 或者 inference.networking.x-k8s.io/v1alpha2                                                                               |
| `inferencepool.inferencepool.inferencePool.modelServers.matchLabels.app` | `inferx`                         | 配置 inferencepool 与模型服务 Pod 的 Label 选择器，需与模型服务 Pod 的 `app` 标签一致，建议使用 Helm Release Name，否则将无法匹配到模型服务 Pod 或者匹配到多个模型服务 Pod，可以通过 `llm-d-modelservice.llm-d-modelservice.modelArtifacts.labels.app` 设置， |
| `inferencepool.inferencepool.provider.name`                              | `istio`                          | 配置 inferencepool 使用的 provider，目前支持 istio， none，非 istio 环境设置为 none 即可                                                                                                                              |
| `llm-d-modelservice.llm-d-modelservice.modelArtifacts.labels.app`        | `inferx`                         | 配置模型服务 Pod 的 labels， 请确保 inferencepool.inferencepool.inferencePool.modelServers.matchLabels.app 与此一致，建议使用 Helm Release Name                                                                       |
| `llm-d-modelservice.llm-d-modelservice.modelArtifacts.uri`               | `-`                              | 配置模型权重，支持 HF，PVC                                                                                                                                                                                  |
| `llm-d-modelservice.llm-d-modelservice.modelArtifacts.name`              | `-`                              | 配置模型名称，用于标识 vllm served-model-name， 仅在 modelCommand 非 custom 时有效                                                                                                                                  |
| `llm-d-modelservice.llm-d-modelservice.accelerator.type`                 | `nvidia`                         | 配置使用 hami vgpu                                                                                                                                                                                    |
| `llm-d-modelservice.llm-d-modelservice.routing.proxy.enabled`            | `false`                          | 配置 PD 分离 proxy sidecar，sidecar 会注入到 decode pod                                                                                                                                                    |


### 安装 Inferx 
```bash
bin/helm install inferx oci://demo.harbor.io/test_repo/inferx --version 0.1.0 --namespace public --create-namespace -f values.yaml
```
### kpanda 界面安装 (可选)

如需通过 Kpanda 进行图形化安装，请先将 Chart 推送至支持 Chart Museum 仓库：

```bash
bin/helm fetch oci://demo.harbor.io/test_repo/inferx --version 0.1.0
bin/helm-cm-push inferx-0.1.0.tgz https://demo.harbor.io/chartrepo/test_repo --username ${username} --password ${password}
```

上述命令执行成功后，请将对应 Helm 仓库添加至 Kpanda Helm 应用->Helm 仓库 界面，随后可在 Helm 应用->Helm 模板中完成 Inferx 部署。