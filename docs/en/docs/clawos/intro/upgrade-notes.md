# Upgrade Notes

This page describes the considerations for upgrading ClawOS from v0.3.3 to v0.5.3.

## Upgrade from v0.3.3 to v0.5.3

### Upgrade images for existing instances

The default OpenClaw instance images are different between v0.3.3 and v0.5.3:

- v0.3.3: `release.daocloud.io/agentclaw/openclaw:2026.4.7`
- v0.5.3: `release.daocloud.io/agentclaw/openclaw:2026.7.1`

In v0.5.3, `openclawPrevious` is `2026.6.10`. It is not the target image for upgrading existing instances.

!!! note

    Upgrading the AgentClaw Helm Chart only updates the instance template and default image configuration. It does not automatically update existing AgentInstance Deployments. After the upgrade, update or restart each existing instance so that its OpenClaw container uses `2026.7.1`.

Before upgrading, confirm that `release.daocloud.io/agentclaw/openclaw:2026.7.1` is accessible from the environment. If the image cannot be pulled, updated instances will enter `ImagePullBackOff`.

### SkillHub configuration

During the upgrade, enable both the ClawOS SkillHub integration and the SkillHub subchart by default:

```yaml
skillhub:
  enabled: true
  # A node IP or domain reachable when an OpenClaw instance runs npx clawhub install
  publicHost: <reachable cluster node IP or domain>

skillhubChart:
  enabled: true
  secrets:
    bootstrapAdminPassword: <SkillHub admin password>
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

- `skillhub.publicHost` must be a node IP or domain reachable when an OpenClaw instance runs `npx clawhub install`. NodePort listens on every cluster node; the master node is not required.
- `skillhubChart.secrets.scannerLlmApiKey`, `scannerLlmBaseUrl`, `scannerLlmModel`, and `scanner.analyzers.llmProvider` configure LLM analysis for Skill Scanner. Do not commit a real API key to the values file.
- `scannerLlmBaseUrl` must point to an OpenAI-compatible `/v1` endpoint. `scannerLlmModel` uses the LiteLLM route format, such as `openai/public/minimax-m25`.
- When `useLlm`, `useBehavioral`, and `enableMeta` are all enabled, Scanner combines LLM, behavioral, and meta analysis results.

Before enabling SkillHub, confirm the following:

1. The released AgentClaw Chart package contains the `charts/skillhub` subchart; otherwise Helm dependency rendering fails.
2. SkillHub, PostgreSQL, Redis, and Scanner images are available in the environment.
3. A usable StorageClass/PV is available for SkillHub PVCs.
4. With the default `global.ghippo.applyCR=true`, the cluster has the `ghippo.io/v1alpha1/GProductProxy` CRD. If the CRD is unavailable, set `global.ghippo.applyCR=false`; otherwise Helm deployment fails.

### manager component

v0.5.3 adds and enables the NetworkPolicy manager by default:

```yaml
manager:
  enabled: true
```

The manager requires access to Kpanda and Clusterpedia, as well as Lease, ConfigMap, and Event permissions. If NetworkPolicy manager is not used in the environment, or its dependencies/API/RBAC are not ready, disable it in the upgrade values:

```yaml
manager:
  enabled: false
```

Otherwise, the manager Pod may fail to start or repeatedly restart.
