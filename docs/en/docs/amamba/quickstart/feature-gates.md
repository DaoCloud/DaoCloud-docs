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
