# NVIDIA Dynamo v1.5.0 发布：DaoCloud 是贡献最多的外部贡献者

> 本文基于 NVIDIA 官方发布说明整理：[Dynamo v1.5.0 Release Notes](https://docs.dynamo.nvidia.com/dynamo/v1.5.0/reference/releases/v1-5-0)。
> Dynamo 是 [NVIDIA 开源](https://github.com/ai-dynamo/dynamo)的分布式 LLM 推理平台；文中标注的版本信息与贡献者名单均出自该发布说明，PR 统计数据来自 GitHub 合并记录。

2026 年 9 月 18 日，[Dynamo](https://github.com/ai-dynamo/dynamo) v1.5.0 正式 GA。
这是 Dynamo 作为 NVIDIA 开源分布式推理平台的 **第 18 个功能版本** ，也是迄今为止形态变化最大的一版：
路由从"内置策略"变成"可插拔策略"，Kubernetes 侧完成了 CRD 存储版本与 Endpoint Picker 语言的更替，
KVBM 正式进入废弃流程，AIConfigurator 独立成了 AISimulate。

同时，NVIDIA 在发布说明里把外部贡献者的组织归属完整列了出来 ——
**DaoCloud 以 8 位贡献者排在这份名单的第一位，是本次发布贡献最多的外部贡献者。**

## 先看数字

| 项目 | 数值 | 说明 |
| --- | --- | --- |
| 版本 | v1.5.0 | GA 2026-09-18，功能版本序号第 18 |
| 补丁版本 | v1.5.1 | 2026-10-06 发布，Base Branch `release/1.5.1` |
| 合并 PR | 658 个 | 统计区间 v1.4.2 → v1.5.0 |
| 参与贡献者 | 123 人 | 同上区间 |
| NVIDIA 以外贡献者 | 40 人 | 占全部贡献者的约三分之一 |
| 首次贡献者 | 23 人 | 官方在发布说明中逐一列出 |

658 个 PR、123 位贡献者。按 v1.4.2 与 v1.5.0 两个 tag 的时间推算，发布窗口里平均每天有 30 个左右的 PR 合入。
这个节奏本身就说明了 Dynamo 在 NVIDIA 推理栈里的位置。

## 社区：40 位外部贡献者，DaoCloud 排在名单首位

NVIDIA 官方按 **提交作者邮箱域名或公开 GitHub 主页** 识别了每位外部贡献者的组织归属，并按人数从多到少排列。完整名单如下：

| 组织 | 贡献者人数 | GitHub 账号 |
| --- | --- | --- |
| **DaoCloud** | **8** | [@bzsuni](https://github.com/bzsuni)、[@carlory](https://github.com/carlory)、[@flpanbin](https://github.com/flpanbin)、[@muma378](https://github.com/muma378)、[@panpan0000](https://github.com/panpan0000)、[@weizhoublue](https://github.com/weizhoublue)、[@windsonsea](https://github.com/windsonsea)、[@yankay](https://github.com/yankay) |
| CoreWeave | 4 | @alexeldeib、@houshengbo、@Rexwang8、@ritazh |
| Intel | 3 | @Spycsh、@tthakkal、@VincyZhang |
| Amazon | 3 | @AineshSootha、@jlonge4、@YiqiuLiu |
| Baseten | 2 | @michaelfeil、@shalinkpatel |
| Aliyun | 1 | @xianlubird |
| Arizona State University | 1 | @Change72 |
| Datadog | 1 | @walkoss |
| Gcore | 1 | @Kaonael |
| Georgia Tech | 1 | @Skenix64 |
| H Company | 1 | @h-avsha |
| Microsoft | 1 | @Jont828 |
| Reflection AI | 1 | @joeltg |
| SK Telecom | 1 | @changhyeonnam |
| San Jose State University | 1 | @ayaangazali |
| Stanford University | 1 | @merceod |
| UC San Diego Hao AI Lab | 1 | @vishruthb |
| University of Guelph | 1 | @mgsalem |
| University of Washington | 1 | @Shaoting-Feng |
| Yandex Cloud | 1 | @jellysnack |
| Independent | 5 | @avinash-rafay、@cmdy、@elizabetht、@hnt2601、@Jonny-Skelton |

**DaoCloud 是这份名单里贡献者人数最多的外部组织** ，8 人几乎是第二名 CoreWeave 的两倍，也占了 40 位外部贡献者的五分之一。

如果进一步看实际提交量：按 GitHub 合并记录统计（合并日期 2026-08-27 至 2026-09-19，即 v1.4.2 与 v1.5.0 两个 tag 之间的窗口），
DaoCloud 团队在这个窗口内合并了 **33 个 PR** ，而其他所有外部贡献者加起来约 12 个 —— 单是一家公司，就接近其余外部贡献总量的三倍。

## Dynamo 是什么

在展开 v1.5.0 的细节之前，先用几句话交代背景。

Dynamo 是 NVIDIA 开源的 **分布式推理平台** ，目标是把一堆 GPU 组织成一个可编程、可观测、可弹性伸缩的推理服务。它的核心组件包括：

- **Dynamo Frontend** ：对外的 OpenAI 兼容 API 入口，负责请求校验、分词、工具调用解析、思考模式控制等。
- **Dynamo Router** ：决定一个请求该发给哪个 worker。它关心的问题不是"哪个实例连接数最少"，而是"哪个 worker 已经持有这段前缀的 KV Cache"。
- **Dynamo Planner** ：根据 SLA 和负载决定扩缩容。
- **Dynamo Operator + CRD** ：在 Kubernetes 上编排整套推理拓扑（`DynamoGraphDeployment`、`DynamoGraphDeploymentRequest` 等）。
- **Backend** ：SGLang、TensorRT-LLM、vLLM 三种引擎接入。

如果你正在 Kubernetes 上跑 LLM 推理，Dynamo 解决的就是"Prefill/Decode 怎么拆、KV Cache 怎么复用、流量来了缩哪一边"这类问题。

## v1.5.0 的九个重点变化

### 1. Dynamo Router：Worker 选择从内置策略变成可插拔策略

这是 v1.5.0 最核心的变化。此前 Router 的 worker 选择逻辑是内置的，v1.5.0 把它 **打开成了策略接口** ：

- 新增原生的 `WorkerScorer` 与 `WorkerPicker` 策略，走与内置选择器 **同一条 host selection 路径** ——
  发现、可用性判定、预留、指标、分发仍然由 Dynamo 负责，策略只决定"哪个 worker 胜出"。
- 新增可组合的 `WorkerFilter`，在内置可用性判定之后、scoring 之前执行；如果 filter 把所有可用 worker 都拒掉，返回 HTTP 503。
- 新增 `dynamo-two-tier-cost-fn` 内置策略：先按活跃请求数排序，再按设备侧 KV 前缀重合度排序。
- Session affinity（会话亲和）新增 **hard/soft** 两种模式，通过 `--router-session-affinity-mode` 或
  `DYN_ROUTER_SESSION_AFFINITY_MODE` 配置，默认 hard。soft 模式下会话目标会作为亲和目标继续参与选择，自定义策略可以覆盖它。

KV 索引侧则新增了两级：

- 消费 **Mooncake** 共享缓存事件，为 SGLang HiCache 建立事件驱动索引，热路径上不再需要 HTTP 查询。
- 把 vLLM 原生存储的 KV 事件路由到 Dynamo Router 的 **Disk tier**，并带上 locality 门控。
- 新增 **条件式分离旁路** ：短请求直接发给 decode，跳过 prefill 这一段编排。

### 2. Frontend：工具调用流式化、思考控制、请求校验

- **引导式工具调用（guided tool calls）默认流式输出** ，Qwen3 接入 v2 统一工具调用解析器，保证思考内容排在工具调用之后。
- **思考/推理控制只解析一次** ，统一优先级，并作用于所有 chat-template key；新增部署级默认思考模式，请求级配置仍然优先。
  Gemma 4 的推理解析由 `enable_thinking` 显式门控。
- **错误语义收紧** ：超上下文请求在流打开之前就被拒绝（不再先吐几个 token 再报错），校验失败返回 HTTP 400，
  后端过载保留 503。此外，未知的 `tool_call_parser` 名称在注册阶段就会被拒绝。
- 支持可插拔的 **分词器后端**
  （包括来自 Baseten 的实现），Hugging Face 兜底策略可配置 —— 加载失败不再静默退回 HF。

### 3. 多模态：前端解码、视频感知路由、实时音频

- **前端图像解码** ：encode-prefill-decode 部署可以让 Dynamo Frontend 只解码一次图片，然后通过
  **单次 NIXL 传输** 把 RGB 像素和内容哈希交给 encode worker，像素不再经由 prefill worker 中转。
  解码器默认走 libjpeg-turbo（存在 libturbojpeg 时），视频走 FFmpeg。后端解码仍是默认行为，前端解码视频暂不支持。
- **视频感知路由** ：Qwen 视频输入使用 video-aware KV hashing；vLLM worker 开始接受音频与视频输入。
- **vLLM-Omni** ：新增实时音频流（OpenAI 兼容 `/v1/realtime` WebSocket）与动态 LoRA 的加载、卸载、列举端点。
- 一处值得注意的性能细节：把每个请求的编码缓冲区复用之后，单 token 帧的编码耗时从 **312 ns 降到 232 ns** 。

### 4. Kubernetes：v1beta1 成为存储版本，Rust EPP 取代 Go EPP

对平台团队来说，这是升级时最需要留意的一节：

- **`nvidia.com/v1beta1` 成为 CRD 存储版本**（API server 实际持久化的那个版本），
  DCD/DGD/DGDR/DGDR-scaling-adapter 全部迁移，同时继续服务 v1alpha1。公开示例中的 v1alpha1 副本已删除。
- **Go Endpoint Picker 被移除，Rust EPP 成为默认**，随 Dynamo Frontend 镜像一起分发在 `/epp`；独立镜像计划在后续版本提供。
- **Dynamo Snapshot 独立成 operator 与 chart**，发布为 Snapshot v0.1.0
  （`oci://ghcr.io/ai-dynamo/snapshot/snapshot:0.1.0`），`PodSnapshot`/`PodSnapshotContent` CRD 取代了被移除的
  `DynamoCheckpoint`。生产环境建议单独安装；评估可以用平台 chart 的 `global.snapshot.install=true` 一并拉起。
- **实验性的 GPU Memory Service V1** 带来 checkpoint 生命周期与 SGLang/vLLM 的引擎集成，通过 `--use-v1` 启用。
- Operator 侧新增 `runtimeVersionOverride`、按功能划分的 runtime feature gates、显式多节点角色（`roles`），
  以及 worker 金丝雀健康检查。
- 新增 **llm-d Batch Gateway 示例**：把离线 OpenAI Batch 请求接进推理网关，并且分发会以 frontend
  模型就绪指标作为门控（指标缺失时按预算为零处理，即失败关闭）。
- 新增 **LMCache 聚合服务示例**，用 LMCache MP 作为 KV cache 后端，通过跨 Pod CUDA IPC 与 worker 共享张量。

### 5. 可观测性与容错

- 请求迁移（request migration）的尝试与取消现在 **端到端打点** ，新增 `WorkerOverloaded`
  错误类与 TCP 连接失败分类，迁移会改投其他 worker。
- 请求 trace 记录支持 **原生 S3 sink** ，以 gzip 压缩的 JSONL 批量写入。
- 新增 `dynamo_frontend_model_ready{model}` 指标，声明 frontend 是否能通过一条完整的服务拓扑路由请求；该指标同时把关批量分发。
- worker 存活探针的容忍次数从 1 次放宽到 3 次。

### 6. AISimulate：AIConfigurator 改名并独立成包

AIConfigurator 更名为 **[AISimulate](https://github.com/ai-dynamo/aisimulate)** ，以独立包 v0.12.0 发布，
提供统一 CLI，取代此前的 aiconfigurator wheels 和 `dynamo.replay` 入口。离线 replay 现在返回单一的 `ReplayReport`，按请求捕获需显式开启。

!!! note

    `python -m dynamo.replay` 已被移除且没有兼容垫片，脚本需要迁移到 `aisimulate predict --stack dynamo --config <file>`。

### 7. Recipes：新模型上车

新增 Qwen3.8-2.4T-A95B FP8（GB200/GB300，SGLang 与 vLLM）、Qwen3.5-122B FP8 on H200、Nemotron-3.5-Lightning
（含 B200/GB200/H100/H200 的性能数据）、Nemotron-3-Ultra refresh（12 个部署 profile，256K 与 1M 上下文），以及
GLM-5.3-Flash on vLLM（GB200 NVL72）。DeepSeek-V4 的下载改为按 checkpoint 参数化。DeepSeek-V3.2 FP4
与 Llama-3-70B 的 recipe 被移除。

### 8. 安全：TLS 与 mTLS 覆盖 TCP 和 NATS

TLS 现在覆盖 **TCP 请求面与响应面** 以及 **NATS 传输** ，两边都支持 opt-in 的 mutual TLS。Operator 在
`InfrastructureConfiguration` 中新增 10 个证书路径字段，一次性配置、自动注入成每个 DGD Pod 的 NATS/TCP TLS 环境变量，
并在启动时校验依赖链。Backend SDK 上的管理路由被 worker 生命周期门控。请求处理整体 **失败关闭** ：
不可服务的请求在流打开之前返回类型化的 4xx。

### 9. 实验特性：Sidecar、Triton backend、SGLang RL

这三个特性的接口、默认值和镜像结构在 v1.5.0 中 **可能不经过废弃周期直接变更** ，生产环境请谨慎：

- **Dynamo Sidecar**：跑在标准推理引擎旁边，通过引擎自己的原生 gRPC API 集成 —— 引擎保留自己的 serve 命令，
  Dynamo 独立成进程。SGLang/TensorRT-LLM/vLLM 各有 wheel 安装的启动器，三个 sidecar 打包在一个 CPU-only 多架构镜像里。
- **`dynamo.triton` backend**：把非 LLM 模型（视觉、embedding 等 tensor-in/tensor-out 模型）接入 Dynamo pipeline，
  用 `python -m dynamo.triton` 启动。v1.5.0 不提供预构建镜像，需要按 Triton runtime Dockerfile 自行构建。
- **SGLang RL rollout 契约**：`nvext.detailed_finish_reason` 报告规范的结束原因，`nvext.extra_fields` 携带
  `prompt_token_ids` 与采样 logprobs，引擎原生 pause 与显存控制挂在 `/engine/*` 下，并且 worker 的 `output_ids`
  保留命中的停止 token，确保训练侧看到的就是引擎真实采样的内容。

## 升级前必须知道的事

### 破坏性变更与废弃

- **KVBM 已废弃**，计划在 **v1.7.0** 移除。
- **Go Endpoint Picker 被移除**，使用方需要迁移到 Rust EPP。
- **`DynamoCheckpoint` CRD 被移除**，改用 Snapshot operator 的 `PodSnapshot`。
- **`python -m dynamo.replay` 入口被移除**，迁移到 AISimulate CLI。
- v1.5.1 中还有两个需要动作的变更：通过环境 HTTP 代理拉取请求媒体的 worker 需要设置
  `DYN_MM_TRUST_EGRESS_PROXY=1`；SGLang 图像扩散/视频生成 worker 的本地 `input_reference` 需要
  `DYN_MM_LOCAL_PATH` 指明允许目录。

### 已确认的已知问题

| 影响范围 | 问题 | 状态 |
| --- | --- | --- |
| SGLang | Sidecar 的每一次推理请求都返回 HTTP 500（`'GenerateReqInput' object has no attribute 'batch_size'`），启动、注册、发现均正常 | 上游 SGLang v0.5.19 已修正，目标 v1.6.0；暂无绕过方案 |
| SGLang/TensorRT-LLM/vLLM | 部分 H.264 视频在 PyNvVideoCodec 2.2.3 解码最后一帧时崩溃，该 worker 的后续请求持续失败直至重启 | 目标 v1.6.0；图片与音频输入不受影响 |
| SGLang | 分离式部署下，engine-native `/generate` 请求设置 `return_logprob` 时不返回 prompt logprobs | 本版本无修复计划 |
| SGLang | 使用 `--dcp-size` 启动的 worker 在真实请求上崩溃 | 绕过方案：v1.5.0 中不要设置该参数 |
| Planner | mocker 的 thorough 模式仍会拉起真实 GPU 部署，因缺卡进入 CrashLoopBackOff | 绕过方案：改用 `rapid` 模式 |
| Planner | `dynamo.mocker --aic-perf-model` 启动即崩溃 | 绕过方案：改用 `aisimulate predict` |
| CLI | `python -m dynamo.replay` 不再提供入口 | 迁移到 `aisimulate predict --stack dynamo --config <file>` |
| Frontend | 后端返回请求级错误时，客户端只拿到裸 HTTP 500，看不到失败原因 | — |
| Router | 显式指定 prefill 目标、而该目标被本地抑制时，请求既不分发也不回退到其他 prefill worker | — |
| Upstream | FP8 MoE 版 Qwen3-30B-A3B 在 vLLM 上加载权重崩溃（H100/B200/GB200 均可复现） | 上游问题，非 FP8 版本不受影响 |

官方把破坏性变更与废弃统一维护在
[Deprecations](https://docs.dynamo.nvidia.com/dynamo/v1.5.0/reference/releases/deprecations)
台账，已知问题在 [Known Issues](https://docs.dynamo.nvidia.com/dynamo/v1.5.0/reference/releases/known-issues) 页。

## 版本对齐表

| 组件 | v1.5.0 对齐版本 |
| --- | --- |
| SGLang | v0.5.18 |
| TensorRT-LLM | v1.3.0rc25 |
| vLLM | v0.28.0 |
| NIXL refs/UCX | 与前版一致/v1.21.0 |
| CUDA | SGLang 13.0、TensorRT-LLM 13.1、vLLM 13.0 |

升级路径为 v1.4.x → v1.5.0，官方建议的阅读顺序是：v1.5.0 破坏性变更 → v1.5.0 已知问题 → v1.4.0 破坏性变更。

## DaoCloud 的贡献落在哪里

回到社区这一节。把 DaoCloud 团队在这两个 tag 之间的 33 个合并 PR 摊开看，落点相当分散，但集中在
**平台侧与推理网关** ：

- **Inference Gateway/Rust EPP**：为超长 metadata 头返回 431 并引入类型化的 `MetadataHeaderError`；
  让 standalone EPP 一致地遵循 cache namespace/salt；把调度元数据传递给 `SelectionService`。
- **Router/KV Router 一致性**：让 Rust 侧的 KV Router 环境变量解析与 Python 侧参数对齐 ——
  这类"两种实现漂移"的问题，在同时存在 Rust EPP 与 Go 时代遗留的版本里格外容易出现。
- **Dynamo Operator/CRD**：归一化等价的 worker hash 输入，避免滚动更新时出现虚假的版本差异。
- **Dynamo Planner**：处理虚拟连接器等待中的 pending decision；前端直方图均值按观测次数加权。
- **Frontend**：保留 SGLang worker 的路由提示；尊重显式传入的 `skip_special_tokens`。
- **多模态**：图片 URL 拉取失败时返回 4xx 客户端错误，而不是让它变成 5xx。
- **容器镜像与文档**：在 vLLM/SGLang/TensorRT-LLM 的 runtime 镜像中补上 `libjemalloc2`，并补充前端主机内存调优说明。
- **CI 基建**：测试镜像安装 networkx、为 Triton 测试工作流传入 framework、原生依赖改用浅克隆。

这些改动大部分不是 headline 级别的特性，而是让"能跑"变成"跑得稳"的那一类：错误码语义、两种实现之间的参数一致性、
镜像里缺失的动态链接库、CI 的稳定性。分布式推理平台在生产环境里踩到的坑，往往就是从这些地方冒出来的。

更值得记一笔的是：这 40 位外部贡献者的组织分布里，
**既有 CoreWeave、Intel、Amazon、Microsoft、SK Telecom、Datadog、Yandex Cloud 这样的厂商，也有 Arizona State University、Georgia Tech、Stanford、UC San Diego、University of Washington 等高校实验室** 。
一个开源推理平台能在一个版本的迭代窗口里积累到如此跨度的外部生态，本身就是它正在成为事实标准的信号。

## 结语

Dynamo v1.5.0 的关键词是 **可编程** 和 **平台化** ：Router 把 worker 选择权交给用户策略，
Kubernetes 侧完成了 v1beta1 存储版本与 Rust EPP 的更替，Snapshot 从内嵌组件变成独立 operator，
AISimulate 从子模块变成独立项目。对在 Kubernetes 上做 AI 推理平台的团队来说，这是一次值得认真读一遍破坏性变更的版本。

对 DaoCloud 来说，这次的 8 人名单和 33 个 PR 是一个起点而非终点 ——
我们会在接下来的版本里继续围绕 Router、推理网关和 Kubernetes 编排这条线提交改动。

**参考链接**

- [Dynamo v1.5.0 Release Notes](https://docs.dynamo.nvidia.com/dynamo/v1.5.0/reference/releases/v1-5-0)
- [Dynamo v1.5.0 Known Issues](https://docs.dynamo.nvidia.com/dynamo/v1.5.0/reference/releases/known-issues)
- [ai-dynamo/dynamo on GitHub](https://github.com/ai-dynamo/dynamo)
- [AISimulate on GitHub](https://github.com/ai-dynamo/aisimulate)
- [ai-dynamo/snapshot on GitHub](https://github.com/ai-dynamo/snapshot)
