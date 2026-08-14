# 升级注意事项

本页说明将 ClawOS 从 v0.3.3 升级到 v0.5.3 时需要注意的事项。

## 从 v0.3.3 升级到 v0.5.3

### 存量实例镜像升级

v0.3.3 和 v0.5.3 的默认 OpenClaw 实例镜像不同：

- v0.3.3：`release.daocloud.io/agentclaw/openclaw:2026.4.7`
- v0.5.3：`release.daocloud.io/agentclaw/openclaw:2026.7.1`

`openclawPrevious` 在 v0.5.3 中为 `2026.6.10`，不属于本次存量实例统一升级目标。

!!! note

    升级 AgentClaw Helm Chart 只会更新实例模板和默认镜像配置，不会自动修改已经存在的 AgentInstance Deployment。升级完成后，需要对系统中的存量实例逐个执行更新或重启，使 OpenClaw 容器镜像切换到 `2026.7.1`。

升级前请确认 `release.daocloud.io/agentclaw/openclaw:2026.7.1` 在当前环境可访问。镜像不可拉取会导致实例更新后进入 `ImagePullBackOff`。

### SkillHub 配置

升级时默认同时开启 ClawOS 的 SkillHub 能力和 SkillHub 子 Chart：

```yaml
skillhub:
  enabled: true
  # 集群外执行 npx clawhub install 时可访问的节点 IP 或域名
  publicHost: <集群可访问的节点 IP 或域名>

skillhubChart:
  enabled: true
  secrets:
    bootstrapAdminPassword: <SkillHub 管理员密码>
    scannerLlmApiKey: <LLM API key>
    scannerLlmBaseUrl: http://<内网模型网关>:<端口>/v1
    scannerLlmModel: openai/public/minimax-m25
  scanner:
    analyzers:
      llmProvider: openai
      useLlm: true
      useBehavioral: true
      enableMeta: true
```

其中：

- `skillhub.publicHost` 必须填写集群中可被 OpenClaw 实例执行 `npx clawhub install` 访问的节点 IP 或域名。NodePort 会监听集群中的每个节点，不要求填写 master 节点。
- `skillhubChart.secrets.scannerLlmApiKey`、`scannerLlmBaseUrl`、`scannerLlmModel` 和 `scanner.analyzers.llmProvider` 用于配置 Skill Scanner 的 LLM 分析。生产环境不要把真实 API key 提交到 values 文件。
- `scannerLlmBaseUrl` 应指向 OpenAI 兼容的 `/v1` 端点；`scannerLlmModel` 使用 LiteLLM 路由格式，例如 `openai/public/minimax-m25`。
- `useLlm`、`useBehavioral` 和 `enableMeta` 同时开启时，Scanner 会组合 LLM 分析、行为分析和 meta 分析结果。

启用 SkillHub 前，还需要确认：

1. 发布的 AgentClaw Chart 包含 `charts/skillhub` 子 Chart，否则 Helm 依赖渲染会失败。
2. SkillHub、PostgreSQL、Redis、Scanner 依赖的镜像在当前环境可拉取。
3. 集群有可用的 StorageClass/PV，满足 SkillHub 的 PVC 要求。
4. 默认 `global.ghippo.applyCR=true` 时，集群已安装 `ghippo.io/v1alpha1/GProductProxy` CRD。没有该 CRD 时，应关闭 `global.ghippo.applyCR`，否则 Helm 部署会失败。

### manager 组件

v0.5.3 默认新增并启用 NetworkPolicy manager：

```yaml
manager:
  enabled: true
  serviceAccount:
    create: true
```

manager 需要访问 Kpanda 和 Clusterpedia，并使用 Lease、ConfigMap、Event 以及 ClusterPedia resources 相关权限。`manager.enabled=true` 且 `manager.serviceAccount.create=true` 时，Chart 会自动创建 manager 专用的 ServiceAccount、ClusterRole 和 ClusterRoleBinding，无需预先手工创建这些 RBAC 资源。

升级时请确认执行 Helm 的身份有权限创建或更新集群级的 ClusterRole 和 ClusterRoleBinding。如果将 `manager.serviceAccount.create` 设置为 `false`，则需要提前提供已绑定上述权限的 ServiceAccount，否则 Helm 升级可能失败，或 manager Pod 因权限不足无法正常运行。

如果当前环境不部署 NetworkPolicy manager，或 Kpanda/Clusterpedia 服务地址不可访问，可以在升级参数中关闭：

```yaml
manager:
  enabled: false
```

否则 manager Pod 可能启动失败或反复重启。
