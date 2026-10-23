# Upgrade Notes

This page describes the considerations for upgrading ClawOS from v0.3.3 to v0.5.3.

## Upgrade from v0.3.3 to v0.5.3

### Upgrade images for existing instances

The default OpenClaw instance images are different between v0.3.3 and v0.5.3:

- v0.3.3: `release.daocloud.io/agentclaw/openclaw:2026.4.7`
- v0.5.3: `release.daocloud.io/agentclaw/openclaw:2026.7.1`

In v0.5.3, `openclawPrevious` is `2026.6.10`. It is not the target image for upgrading existing instances.

!!! note

    After the upgrade, update each existing instance so that its OpenClaw container uses `2026.7.1`.

### SkillHub configuration

SkillHub is disabled by default in v0.5.3. To enable it, set the following values:

```yaml
skillhub:
  enabled: true
  # A node IP or domain reachable by OpenClaw instances when npx clawhub install is run
  publicHost: <reachable cluster node IP or domain>

skillhubChart:
  enabled: true
  secrets:
    scannerLlmApiKey: <LLM API key>
    scannerLlmBaseUrl: http://<internal model gateway>:<port>/v1
    scannerLlmModel: openai/public/minimax-m25
  scanner:
    analyzers:
      llmProvider: openai
      useLlm: true
      useBehavioral: true
      enableMeta: true
```

The following values are important:

- `skillhub.publicHost` must be a node IP reachable by OpenClaw instances. NodePort listens on every cluster node; the master node is not required.
- `skillhubChart.secrets.scannerLlmApiKey`, `scannerLlmBaseUrl`, `scannerLlmModel`, and `scanner.analyzers.llmProvider` configure LLM analysis for Skill Scanner.
- `scannerLlmBaseUrl` must point to an OpenAI-compatible `/v1` endpoint. `scannerLlmModel` uses the LiteLLM route format, such as `openai/public/minimax-m25`.
- When `useLlm`, `useBehavioral`, and `enableMeta` are all enabled, Scanner combines LLM, behavioral, and meta analysis results.
