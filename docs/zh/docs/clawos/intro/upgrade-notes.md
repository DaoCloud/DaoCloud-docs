# 升级注意事项

本页说明将 ClawOS 从 v0.3.3 升级到 v0.5.3 时需要注意的事项。

## 从 v0.3.3 升级到 v0.5.3

### 存量实例镜像升级

v0.3.3 和 v0.5.3 的默认 OpenClaw 实例镜像不同：

- v0.3.3：`release.daocloud.io/agentclaw/openclaw:2026.4.7`
- v0.5.3：`release.daocloud.io/agentclaw/openclaw:2026.7.1`

`openclawPrevious` 在 v0.5.3 中为 `2026.6.10`，不属于本次存量实例统一升级目标。

!!! note

    升级完成后，需要对系统中的存量实例逐个执行更新，使 OpenClaw 容器镜像切换到 `2026.7.1`。

### SkillHub 配置

v0.5.3 默认关闭 ClawOS 的 SkillHub 能，如需开启，请设置以下values:

```yaml
skillhub:
  enabled: true
  # 集群外执行 npx clawhub install 时可访问的节点 IP 或域名
  publicHost: <集群可访问的节点 IP 或域名>

skillhubChart:
  enabled: true
  secrets:
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

- `skillhub.publicHost` 必须填写集群中可被 OpenClaw 实例访问的节点 IP。NodePort 会监听集群中的每个节点，不要求填写 master 节点。
- `skillhubChart.secrets.scannerLlmApiKey`、`scannerLlmBaseUrl`、`scannerLlmModel` 和 `scanner.analyzers.llmProvider` 用于配置 Skill Scanner 的 LLM 分析。
- `scannerLlmBaseUrl` 应指向 OpenAI 兼容的 `/v1` 端点；`scannerLlmModel` 使用 LiteLLM 路由格式，例如 `openai/public/minimax-m25`。
- `useLlm`、`useBehavioral` 和 `enableMeta` 同时开启时，Scanner 会组合 LLM 分析、行为分析和 meta 分析结果。
