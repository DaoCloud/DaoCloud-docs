# Feature Gates

## Overview

We use the Feature Gates mechanism to control the enablement and disablement of different features. Feature Gates are configured via the `--feature-gates` option when starting Kubernetes components (such as API Server, Controller Manager, Kubelet, etc.). These features may be at different development stages (Alpha, Beta, or GA) and are introduced or removed in different versions.

Feature Gates are a set of key-value pairs that describe Amamba features. You can use the --feature-gates flag in various Amamba components to enable or disable these features.

Each Amamba component supports enabling or disabling a set of feature gates related to that component. Use the -h parameter to view all feature gates supported by all components. To set feature gates for components such as apiserver, use the --feature-gates parameter and pass a list of feature setting key-value pairs:

```
--feature-gates=...,ReleaseStats=true
```

You can also enable it by configuring in amamba-config:

```yaml
configMap:
  apiServerConfig:
    featureGates:
      - ReleaseStats=true
```

The following table summarizes the feature gates that can be set on different Amamba components.

- After introducing a feature or changing its release stage, the "Since" column will contain the Kubernetes version.
- The "Until" column (if not empty) contains the last Kubernetes version where you can still use the feature gate.
- If a feature is in Alpha or Beta state, you can find that feature in the Alpha and Beta feature gates table.
- If a feature is in a stable state, you can find all stages of that feature in the Graduated and Deprecated feature gates table.
- The Graduated and Deprecated feature gates table also lists deprecated and removed features.

## Alpha and Beta Feature Gates

| Feature             | Default | Stage | Since | Until |
|---------------------|---------|-------|-------|-------|
| UpstreamPipeline        | false   | Alpha | 0.38  | -     |
| AdminGlobalBuildParameter        | false   | Alpha | 0.38  | -     |
| PipelineAdvancedParameters        | false   | Alpha | 0.38  | -     |
| ReleaseStats        | false   | Alpha | 0.36  | -     |
| DAGv2               | false   | Alpha | 0.27  | 0.27  |
| DAGv2               | true    | Beta  | 0.28  | 0.30  |
| DAGv2               | true    | GA    | 0.30  | -     |
| Gitlab              | false   | Beta  | 0.24  | -     |
| Jira                | false   | Beta  | 0.24  | -     |
| KairshipApplication | false   | Beta  | 0.21  | -     |

## Graduated and Deprecated Feature Gates

| Feature             | Default | Stage | Since | Until |
|---------------------|---------|-------|-------|-------|
|                     |         |       |       |       |

# Use Features

## Feature Gates List

Each feature gate is used to enable or disable a specific feature:

- `ReleaseStats`:
   Show the statistical list of release information based on pipelines.

- `DAGv2`:
   Use the new pipeline editing UI.

- `Gitlab`:
   Support managing GitLab projects on the UI.

- `Jira`:
   Support viewing Jira projects on the UI.

- `KairshipApplication`:
   Support managing multi-tenant-level multicloud applications.

- `PipelineAdvancedParameters`:
   Support the multi-select, git branch, image tag, artifact version, and global parameter types in the pipeline configuration options.

- `AdminGlobalBuildParameter`:
   Support configuring global parameters of pipelines in Workbench Management.

- `UpstreamPipeline`:
   Support specifying the upstream pipeline and run ID when running a pipeline through OpenAPI, so as to keep the same triggering user.
