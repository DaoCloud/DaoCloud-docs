# OCI 正在悄悄"占领一切"：AI 时代的镜像、Chart、模型与 WASM 如何走向同一条分发路径

在云原生技术的演进历程中，一场悄无声息的革命正在发生：**OCI（Open Container Initiative，开放容器倡议）**
不再仅仅是容器镜像的标准，而是正在成为云原生生态系统中所有工件（Artifacts）的统一分发协议。从传统的容器镜像，
到 Helm Charts、AI 模型，再到 WebAssembly 模块，几乎所有类型的云原生工件都在向 OCI 规范靠拢。

这种趋势不是偶然的。它源于 OCI 规范本身的巧妙设计，以及云原生社区对统一分发标准的迫切需求。
本文将深入探讨 OCI 如何从容器镜像标准演变为云原生生态的通用分发协议，以及这一变化对 AI
时代基础设施的深远影响。

## OCI：从容器标准到通用分发协议

### OCI 的起源与演进

OCI 诞生于 2015 年，最初目标是为容器运行时和镜像格式创建开放的行业标准。项目由 Docker、CoreOS、
Google、Microsoft 等公司联合发起，旨在避免容器生态的碎片化。

**OCI 的核心规范包括：**

- **[OCI Runtime Specification](https://github.com/opencontainers/runtime-spec)**：定义容器运行时的标准接口
- **[OCI Image Specification](https://github.com/opencontainers/image-spec)**：定义容器镜像的格式
- **[OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)**：定义镜像的分发协议

其中，**Distribution Specification** 是本文的重点。它最初为容器镜像分发而设计，但其简洁而强大的
设计使其具备了支持任意工件类型的潜力。

### Distribution Spec 的核心设计

OCI Distribution Specification 定义了一套基于 HTTP 的 RESTful API，用于在仓库（Registry）
和客户端之间传输工件。其核心概念包括：

1. **Registry**：存储和分发工件的服务器
2. **Repository**：工件的命名空间，如 `library/nginx`
3. **Manifest**：工件的元数据和内容清单
4. **Blob**：工件的实际内容层
5. **Tag**：工件的版本标识符

**关键 API 端点：**

```text
# 上传 blob
PUT /v2/<name>/blobs/uploads/<uuid>

# 获取 manifest
GET /v2/<name>/manifests/<reference>

# 上传 manifest
PUT /v2/<name>/manifests/<reference>

# 列出 tags
GET /v2/<name>/tags/list
```

这套 API 的简洁性和扩展性使其能够支持各种类型的工件，而不仅仅是容器镜像。

## 容器镜像：OCI 的原生领域

容器镜像是 OCI 规范的原生支持对象。一个典型的容器镜像由多个层（Layers）组成，每层是一个
文件系统的变更集。

**容器镜像的 OCI Manifest 示例：**

```json
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.manifest.v1+json",
  "config": {
    "mediaType": "application/vnd.oci.image.config.v1+json",
    "size": 7023,
    "digest": "sha256:b5b2b2c507a0944348e0303114d8d93aaaa081732b86451d9bce1f432a537bc7"
  },
  "layers": [
    {
      "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
      "size": 32654,
      "digest": "sha256:e692418e4cbaf90ca69d05a66403747baa33ee08806650b51fab815ad7fc331f"
    },
    {
      "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
      "size": 16724,
      "digest": "sha256:3c3a4604a545cdc127456d94e421cd355bca5b528f4a9c1905b15da2eb4a4c6b"
    }
  ]
}
```

这种分层设计不仅实现了镜像的增量更新和高效存储，也为其他类型工件的 OCI 化提供了灵感。

## Helm Charts：拥抱 OCI 的先行者

Helm 是 Kubernetes 的包管理器，用于定义、安装和升级复杂的 Kubernetes 应用。传统上，
Helm Charts 通过专用的 Chart 仓库（Chart Repository）分发，使用自定义的 HTTP API。

### 从 Chart Repository 到 OCI Registry

从 Helm 3 开始，Helm 引入了对 OCI Registry 的支持，允许将 Charts 存储在符合 OCI
标准的容器镜像仓库中。这一转变带来了诸多好处：

**优势：**

1. **统一存储**：Charts 和镜像可以存储在同一个 Registry
2. **复用工具**：可以使用现有的镜像仓库基础设施和工具
3. **标准协议**：利用 OCI 的安全、认证和传输机制
4. **简化运维**：无需维护单独的 Chart 仓库

### Helm Chart 的 OCI 存储示例

**推送 Helm Chart 到 OCI Registry：**

```bash
# 打包 chart
helm package mychart/

# 推送到 OCI registry
helm push mychart-0.1.0.tgz oci://registry.example.com/helm-charts

# 从 OCI registry 拉取
helm pull oci://registry.example.com/helm-charts/mychart --version 0.1.0

# 从 OCI registry 安装
helm install myrelease oci://registry.example.com/helm-charts/mychart --version 0.1.0
```

**Helm Chart 的 OCI Manifest：**

Helm Chart 在 OCI 中使用特殊的 `mediaType` 来标识：

```json
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.manifest.v1+json",
  "config": {
    "mediaType": "application/vnd.cncf.helm.config.v1+json",
    "size": 117,
    "digest": "sha256:8ec7c0f2f6860037c19b54c3cfbab48d9b4b21b485a93d87b64690fdb68c2111"
  },
  "layers": [
    {
      "mediaType": "application/vnd.cncf.helm.chart.content.v1.tar+gzip",
      "size": 3654,
      "digest": "sha256:5f8b8e0b4a6....."
    }
  ]
}
```

注意 `mediaType` 使用了 `application/vnd.cncf.helm.*` 前缀，这是 CNCF 为 Helm 定义的专用媒体类型。

## AI 模型：OCI 在 AI 时代的新战场

随着 AI/ML 工作负载在云原生环境中的爆发式增长，模型的分发和版本管理成为新的挑战。传统的
模型仓库（如 Hugging Face Hub、ModelScope）使用自定义的 API 和存储格式，但社区正在
探索使用 OCI 作为统一的模型分发标准。

### 为什么 AI 模型需要 OCI？

AI 模型具有以下特点，使其非常适合 OCI 分发：

1. **大文件**：模型文件通常很大（几 GB 到几十 GB）
2. **版本化**：模型需要频繁更新和版本管理
3. **依赖关系**：模型可能依赖特定的运行时和库
4. **分层存储**：模型可以分解为多个文件（权重、配置、词汇表等）
5. **云原生部署**：模型需要在 Kubernetes 中部署和更新

### OCI 模型存储的实践

多个项目正在探索将 AI 模型存储在 OCI Registry 中：

**1. ONNX Runtime**

ONNX Runtime 支持从 OCI Registry 拉取 ONNX 模型：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: onnx-inference
spec:
  containers:
  - name: onnx-server
    image: mcr.microsoft.com/onnxruntime/server:latest
    env:
    - name: MODEL_URI
      value: "oci://registry.example.com/models/resnet50:v1.0"
```

**2. KServe 和 Seldon**

KServe（前身为 KFServing）支持从 OCI Registry 加载模型：

```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: resnet-predictor
spec:
  predictor:
    model:
      storageUri: "oci://registry.example.com/models/resnet50:v1.0"
      runtime: tensorflow
```

**3. MLflow 和 OCI**

MLflow 社区正在讨论将模型注册表（Model Registry）与 OCI 集成，使模型可以像容器镜像
一样推送和拉取。

### AI 模型的 OCI Manifest 示例

一个 AI 模型在 OCI 中的 Manifest 可能如下：

```json
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.manifest.v1+json",
  "config": {
    "mediaType": "application/vnd.oci.image.config.v1+json",
    "size": 342,
    "digest": "sha256:abc123..."
  },
  "layers": [
    {
      "mediaType": "application/vnd.ai.model.pytorch.weights.v1+tar",
      "size": 5368709120,
      "digest": "sha256:model-weights-hash",
      "annotations": {
        "org.opencontainers.image.title": "model.pth"
      }
    },
    {
      "mediaType": "application/vnd.ai.model.config.v1+json",
      "size": 1234,
      "digest": "sha256:config-hash",
      "annotations": {
        "org.opencontainers.image.title": "config.json"
      }
    },
    {
      "mediaType": "application/vnd.ai.model.tokenizer.v1+json",
      "size": 456789,
      "digest": "sha256:tokenizer-hash",
      "annotations": {
        "org.opencontainers.image.title": "tokenizer.json"
      }
    }
  ],
  "annotations": {
    "org.opencontainers.image.created": "2025-01-15T10:30:00Z",
    "org.opencontainers.image.authors": "model-team@example.com",
    "ai.model.framework": "pytorch",
    "ai.model.version": "2.0",
    "ai.model.architecture": "transformer",
    "ai.model.task": "text-generation"
  }
}
```

注意：

- 使用自定义 `mediaType` 来标识不同类型的模型文件
- 使用 `annotations` 来存储模型的元数据（框架、版本、任务类型等）
- 模型被分解为多个层：权重、配置、tokenizer 等

## WebAssembly：下一代云原生运行时的分发

WebAssembly（WASM）正在成为容器之外的另一种云原生运行时选择。WASM 模块具有轻量、
快速启动、沙箱隔离等优势，在边缘计算和 Serverless 场景中越来越受欢迎。

### WASM 为什么需要 OCI？

WASM 模块的分发面临与容器类似的挑战：

1. **版本管理**：需要跟踪模块的版本和更新
2. **依赖管理**：WASM 模块可能依赖其他模块或运行时库
3. **多平台支持**：WASM 需要支持不同的平台和运行时
4. **云原生集成**：WASM 需要在 Kubernetes 等平台中部署

### OCI for WASM：wasm-to-oci

社区开发了 [wasm-to-oci](https://github.com/engineerd/wasm-to-oci) 项目，允许将 WASM
模块打包成 OCI 镜像并推送到 Registry。

**推送 WASM 模块到 OCI Registry：**

```bash
# 将 WASM 模块推送到 OCI registry
wasm-to-oci push hello.wasm registry.example.com/wasm/hello:v1.0

# 从 OCI registry 拉取 WASM 模块
wasm-to-oci pull registry.example.com/wasm/hello:v1.0 --out hello.wasm
```

### runwasi 和 OCI WASM 镜像

[runwasi](https://github.com/containerd/runwasi) 是 containerd 的 WASM 运行时实现，
支持直接从 OCI Registry 拉取和运行 WASM 模块。

**在 Kubernetes 中运行 OCI WASM 镜像：**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: wasm-app
  annotations:
    module.wasm.image/variant: compat-smart  # 使用 WASM 运行时
spec:
  runtimeClassName: wasmtime  # 指定 WASM 运行时
  containers:
  - name: wasm-container
    image: registry.example.com/wasm/hello:v1.0
```

### WASM 的 OCI Manifest 示例

WASM 模块在 OCI 中的 Manifest：

```json
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.manifest.v1+json",
  "config": {
    "mediaType": "application/vnd.wasm.config.v1+json",
    "size": 234,
    "digest": "sha256:config-hash"
  },
  "layers": [
    {
      "mediaType": "application/vnd.wasm.content.layer.v1+wasm",
      "size": 1234567,
      "digest": "sha256:wasm-module-hash",
      "annotations": {
        "org.opencontainers.image.title": "module.wasm"
      }
    }
  ],
  "annotations": {
    "org.opencontainers.image.created": "2025-01-20T15:00:00Z",
    "wasm.runtime": "wasmtime",
    "wasm.version": "1.0.0"
  }
}
```

注意 `mediaType` 使用了 `application/vnd.wasm.*` 前缀来标识 WASM 内容。

## OCI Artifacts：通用工件规范

为了正式支持非镜像工件，OCI 社区推出了 **OCI Artifacts** 规范。这个规范扩展了 OCI
Image Specification，允许任意类型的工件使用 OCI Distribution API。

### OCI Artifacts 的核心概念

**关键特性：**

1. **自定义 mediaType**：工件可以定义自己的 media type
2. **Annotations**：丰富的元数据支持
3. **Referrers API**：工件之间的引用关系（如签名、SBOM）
4. **Index 支持**：多平台和多变体工件

### Artifacts Specification

OCI Artifacts 使用与镜像相同的 Manifest 格式，但允许：

- `config.mediaType` 可以是任意值（不仅限于 `application/vnd.oci.image.config.v1+json`）
- `layers[].mediaType` 可以是任意值
- 不需要 `config` 是有效的镜像配置

**通用 Artifact Manifest 示例：**

```json
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.oci.image.manifest.v1+json",
  "artifactType": "application/vnd.example.artifact.v1",
  "config": {
    "mediaType": "application/vnd.oci.empty.v1+json",
    "size": 2,
    "digest": "sha256:44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a"
  },
  "layers": [
    {
      "mediaType": "application/vnd.example.data.v1.tar+gzip",
      "size": 123456,
      "digest": "sha256:data-layer-hash"
    }
  ]
}
```

注意：

- `artifactType` 字段明确标识工件类型
- `config.mediaType` 使用了空配置（`application/vnd.oci.empty.v1+json`）
- `layers` 包含实际的工件内容

### 社区采用 OCI Artifacts 的例子

许多项目已经采用 OCI Artifacts 来存储和分发非镜像工件：

| 项目 | 工件类型 | 用途 |
| --- | --- | --- |
| **Helm** | Helm Charts | Kubernetes 应用包 |
| **Notary v2** | 签名 | OCI 工件的内容信任 |
| **ORAS** | 任意文件 | 通用工件分发 |
| **Cosign** | 签名和证书 | 镜像和工件签名 |
| **Syft** | SBOM | 软件物料清单 |
| **Trivy** | 漏洞数据库 | 安全扫描 |
| **Tekton** | Pipeline 定义 | CI/CD 工件 |
| **Flux** | GitOps 配置 | 配置管理 |

## ORAS：OCI Registry 的瑞士军刀

[ORAS (OCI Registry As Storage)](https://oras.land/) 是微软开发的工具，专门用于
将任意工件推送到 OCI Registry。ORAS 大大简化了 OCI Artifacts 的使用。

### ORAS 基本用法

**推送任意文件到 OCI Registry：**

```bash
# 推送单个文件
oras push registry.example.com/myrepo/config:v1.0 config.yaml

# 推送多个文件
oras push registry.example.com/myrepo/app:v1.0 \
  app.yaml:application/yaml \
  config.json:application/json \
  README.md:text/markdown

# 拉取工件
oras pull registry.example.com/myrepo/config:v1.0

# 查看工件元数据
oras manifest fetch registry.example.com/myrepo/config:v1.0
```

**附加元数据（Annotations）：**

```bash
oras push registry.example.com/myrepo/dataset:v1.0 \
  dataset.csv:application/csv \
  --annotation "org.opencontainers.image.created=$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
  --annotation "org.example.dataset.rows=1000000" \
  --annotation "org.example.dataset.format=csv"
```

### ORAS 在 AI/ML 中的应用

ORAS 特别适合在 AI/ML 场景中分发数据集和模型：

```bash
# 推送训练数据集
oras push registry.example.com/ml/datasets/imagenet:2024 \
  train.tar.gz:application/gzip \
  validation.tar.gz:application/gzip \
  metadata.json:application/json \
  --annotation "dataset.size=100GB" \
  --annotation "dataset.samples=1281167"

# 推送训练好的模型
oras push registry.example.com/ml/models/resnet50:v1.0 \
  model.onnx:application/onnx \
  config.json:application/json \
  --annotation "model.framework=pytorch" \
  --annotation "model.accuracy=0.95"
```

## 统一分发的优势

OCI 成为通用分发协议带来了诸多好处：

### 1. 基础设施统一

**之前：**

- 容器镜像 → Docker Hub / Harbor
- Helm Charts → Chart Museum
- AI 模型 → Hugging Face / S3
- WASM 模块 → 自定义存储

**现在：**

- 所有工件 → OCI Registry（Harbor / JFrog Artifactory / AWS ECR / Azure ACR）

**好处：**

- 单一认证和授权系统
- 统一的网络和存储基础设施
- 统一的备份和灾难恢复
- 简化的运维和监控

### 2. 工具生态统一

**可复用的工具链：**

- **推送/拉取**：`docker push/pull`、`crane`、`skopeo`、`oras`
- **镜像同步**：[Distribution](https://github.com/distribution/distribution)、Harbor、Dragonfly
- **安全扫描**：Trivy、Clair、Grype
- **签名验证**：Cosign、Notary v2
- **漏洞管理**：Harbor、Quay、JFrog Xray

### 3. 安全性统一

OCI Registry 提供的安全机制可以应用于所有工件：

- **访问控制**：基于 RBAC 的细粒度权限
- **内容信任**：使用 Notary v2 或 Cosign 签名
- **漏洞扫描**：扫描所有类型的工件
- **审计日志**：跟踪工件的访问和变更
- **加密存储**：静态和传输中的加密

### 4. 云原生集成

统一的分发协议使得云原生平台的集成更加简单：

**Kubernetes 原生支持：**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-artifact-pod
spec:
  runtimeClassName: wasmtime
  containers:
  # 容器镜像
  - name: app
    image: registry.example.com/apps/webapp:v1.0
  
  initContainers:
  # WASM 模块
  - name: wasm-init
    image: registry.example.com/wasm/init:v1.0
  
  volumes:
  # Helm Chart（通过 init 容器拉取）
  - name: config
    emptyDir: {}
```

**GitOps 工作流：**

Flux 和 ArgoCD 可以监控 OCI Registry 中的所有工件类型，实现统一的 GitOps 工作流。

## 挑战与限制

尽管 OCI 统一分发带来诸多好处，但也面临一些挑战：

### 1. Registry 兼容性

并非所有 Registry 都完全支持 OCI Artifacts：

- **完全支持**：Harbor 2.8+、Distribution 3.x、Zot、Azure ACR、AWS ECR
- **部分支持**：Docker Hub（有限的 artifact 支持）
- **不支持**：一些旧版本的私有 Registry

**解决方案：**

- 升级到支持 OCI Artifacts 的 Registry 版本
- 使用 [OCI Conformance](https://github.com/opencontainers/oci-conformance) 测试 Registry 兼容性

### 2. 大文件处理

AI 模型和数据集通常非常大（几十 GB），对 Registry 的存储和传输能力提出挑战：

**问题：**

- 上传/下载时间长
- 存储成本高
- 网络带宽占用大

**解决方案：**

- 使用分层存储减少重复数据
- 启用 Registry 缓存和 CDN
- 使用 P2P 分发（如 Dragonfly）
- 实现增量上传和断点续传

### 3. 元数据标准化

不同类型的工件需要不同的元数据，但目前缺乏统一的标准：

**问题：**

- AI 模型的元数据（框架、精度、任务类型）没有标准格式
- WASM 模块的运行时要求没有统一定义
- 不同工具对 annotations 的使用不一致

**解决方案：**

- 社区制定特定领域的元数据规范（如 [AI Model Registry Spec](https://github.com/AI-Model-Registry)）
- 使用命名空间来组织 annotations（如 `ai.model.*`、`wasm.*`）
- 开发验证工具确保元数据的一致性

### 4. 工具成熟度

虽然 OCI 工具生态正在快速发展，但针对特定工件类型的工具仍然不够成熟：

**需要改进的领域：**

- AI 模型的版本管理和血缘追踪
- WASM 模块的依赖解析
- 大型工件的高效传输
- 跨 Registry 的工件同步

## AI 时代的 OCI：展望未来

随着 AI 工作负载在云原生环境中的普及，OCI 作为统一分发协议的重要性将继续增长。
我们可以预见以下趋势：

### 1. AI 模型仓库标准化

社区正在努力制定 AI 模型在 OCI Registry 中的标准格式：

**可能的标准化方向：**

- 统一的模型 Manifest 格式
- 标准化的模型元数据（框架、版本、精度等）
- 模型血缘和来源追踪
- 模型依赖关系管理

**潜在项目：**

- [ONNX 模型 Zoo](https://github.com/onnx/models) 迁移到 OCI
- Hugging Face 支持 OCI Registry
- MLflow 与 OCI 集成

### 2. 多模态工件管理

未来的应用可能需要同时使用多种类型的工件：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-app
spec:
  template:
    spec:
      containers:
      - name: inference-server
        image: registry.example.com/apps/inference:v1.0  # 容器镜像
      initContainers:
      - name: model-loader
        image: registry.example.com/loader:v1.0
        env:
        - name: MODEL_URI
          value: oci://registry.example.com/models/llm:v2.0  # AI 模型
        - name: WASM_PLUGIN_URI
          value: oci://registry.example.com/wasm/tokenizer:v1.0  # WASM 插件
      - name: config-loader
        image: registry.example.com/loader:v1.0
        env:
        - name: CONFIG_URI
          value: oci://registry.example.com/configs/app:v1.0  # 配置文件
```

### 3. 边缘计算和分布式 AI

在边缘计算场景中，OCI 的分层和增量更新特性特别有价值：

- **模型更新**：只传输变更的层，减少带宽占用
- **多版本共存**：不同边缘节点运行不同版本的模型
- **离线分发**：在网络受限环境中预先缓存工件

### 4. 供应链安全

OCI 的统一分发为软件供应链安全提供了基础：

**SLSA 和 SBOM：**

```bash
# 为模型生成 SBOM
syft registry.example.com/models/resnet50:v1.0 -o spdx > sbom.json

# 将 SBOM 推送到 Registry（作为 artifact）
oras push registry.example.com/models/resnet50:v1.0-sbom sbom.json

# 签名模型
cosign sign registry.example.com/models/resnet50:v1.0

# 验证签名
cosign verify registry.example.com/models/resnet50:v1.0
```

**Referrers API：**

OCI Referrers API 允许工件之间建立引用关系，实现完整的供应链追踪：

```text
registry.example.com/models/resnet50:v1.0
  ├── signature (Cosign)
  ├── sbom (Syft)
  ├── vulnerability scan (Trivy)
  └── provenance (SLSA)
```

## 最佳实践

如果你计划采用 OCI 作为统一分发协议，以下是一些最佳实践：

### 1. 选择合适的 Registry

**评估标准：**

- 完整的 OCI Artifacts 支持
- 大文件处理能力
- 高可用性和性能
- 安全和合规性
- 成本效益

**推荐的 Registry：**

- **Harbor**：功能全面的开源 Registry，支持复制、扫描、签名
- **AWS ECR / Azure ACR / GCP Artifact Registry**：云托管，与云服务集成好
- **JFrog Artifactory**：企业级，支持多种工件类型
- **Zot**：轻量级，专为 OCI Artifacts 优化

### 2. 定义命名规范

为不同类型的工件制定清晰的命名规范：

```text
# 容器镜像
registry.example.com/apps/webapp:v1.0

# Helm Charts
registry.example.com/charts/mychart:1.2.3

# AI 模型
registry.example.com/models/resnet50:v1.0

# WASM 模块
registry.example.com/wasm/tokenizer:v1.0

# 配置和数据
registry.example.com/configs/app-config:latest
```

### 3. 使用标签和元数据

充分利用 OCI 的 annotations 功能：

```bash
oras push registry.example.com/models/bert:v1.0 \
  model.onnx \
  --annotation "org.opencontainers.image.created=$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
  --annotation "org.opencontainers.image.authors=ml-team@example.com" \
  --annotation "org.opencontainers.image.source=https://github.com/example/bert" \
  --annotation "ai.model.framework=pytorch" \
  --annotation "ai.model.framework.version=2.0.0" \
  --annotation "ai.model.task=text-classification" \
  --annotation "ai.model.language=english" \
  --annotation "ai.model.accuracy=0.95" \
  --annotation "ai.model.dataset=glue"
```

### 4. 实施安全策略

**访问控制：**

- 使用细粒度的 RBAC
- 为不同团队和项目创建独立的 Repository
- 定期审计访问日志

**内容信任：**

```bash
# 签名所有生产工件
cosign sign registry.example.com/models/production-model:v1.0

# 要求验证签名
cosign verify registry.example.com/models/production-model:v1.0 \
  --certificate-identity-regexp 'https://github.com/example/*' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

**漏洞扫描：**

- 扫描所有推送到 Registry 的工件
- 为高危漏洞设置阻断策略
- 定期重新扫描已存储的工件

### 5. 优化大文件传输

对于 AI 模型等大文件：

- 启用 Registry 的分块上传
- 使用 CDN 加速下载
- 在边缘节点部署 Registry 缓存
- 考虑使用 P2P 分发（Dragonfly、Kraken）

## 结论

OCI 正在从容器镜像标准演变为云原生生态系统的通用分发协议。从 Helm Charts 到 AI 模型，
再到 WebAssembly 模块，越来越多的工件类型正在拥抱 OCI 规范。这种统一带来了基础设施、
工具、安全性和云原生集成的诸多优势。

在 AI 时代，模型的分发和版本管理成为新的挑战。OCI 的分层存储、内容寻址、版本管理等
特性使其成为理想的解决方案。随着社区的持续努力，我们可以期待 OCI 在 AI/ML 场景中
发挥越来越重要的作用。

**关键要点：**

1. OCI Distribution Specification 的简洁设计使其能够支持任意类型的工件
2. Helm、WASM、AI 模型等正在快速采用 OCI 作为分发标准
3. 统一分发协议带来基础设施、工具、安全性的显著优势
4. OCI Artifacts 和 ORAS 大大简化了非镜像工件的分发
5. AI 时代对统一、高效、安全的工件分发有更高要求

**对 AI 基础设施的影响：**

- 模型与代码一样进行版本管理和分发
- 模型可以像容器一样签名和验证
- 模型与应用的部署流程统一
- 供应链安全覆盖从代码到模型的全链路

OCI 的"占领"不是偶然的，它是云原生社区对统一、开放、标准化的追求。在 AI 蓬勃发展的
今天，OCI 提供了一个坚实的基础，让我们能够以一致、安全、高效的方式管理和分发所有类型的
云原生工件。

## 参考资料

### 规范和标准

- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)
- [OCI Image Specification](https://github.com/opencontainers/image-spec)
- [OCI Artifacts Specification](https://github.com/opencontainers/artifacts)
- [OCI Referrers API](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#listing-referrers)

### 工具和项目

- [ORAS (OCI Registry As Storage)](https://oras.land/)
- [Helm OCI Support](https://helm.sh/docs/topics/registries/)
- [wasm-to-oci](https://github.com/engineerd/wasm-to-oci)
- [runwasi](https://github.com/containerd/runwasi)
- [Harbor](https://goharbor.io/)
- [Cosign](https://github.com/sigstore/cosign)
- [Notation (Notary v2)](https://notaryproject.dev/)

### Registry 实现

- [Distribution](https://github.com/distribution/distribution) - OCI 参考实现
- [Harbor](https://github.com/goharbor/harbor) - 云原生 Registry
- [Zot](https://github.com/project-zot/zot) - OCI-native Registry
- [Dragonfly](https://d7y.io/) - P2P 镜像和文件分发系统

### 相关文章和博客

- [CNCF Blog: OCI Artifacts](https://www.cncf.io/blog/2021/11/10/oci-artifacts/)
- [Helm OCI Support Announcement](https://helm.sh/blog/storing-charts-in-oci/)
- [Microsoft: ORAS Overview](https://cloudblogs.microsoft.com/opensource/2021/07/12/oras-oci-artifacts-registry/)
