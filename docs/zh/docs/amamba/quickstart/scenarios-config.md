# Jenkins 场景配置

Jenkins 分为 master 和 agent。master 主要用于存储配置，插件和协调，agent 和 master 之间通过 agent 这个 Pod 里的 jnlp 容器通信。流水线的工作都在 agent 上，是资源消耗大户。

本文推荐的配置是基于客户并行运行的所有流水线时不会导致整个集群资源崩溃，尤其是 jenkins master 不会出现被驱逐等异常情况。能够并行多少条流水线主要取决于实际 agent 的资源消耗和 K8s 集群资源的大小。

## 场景 1：并行 50 条流水线

### master 配置

```yaml
resources:
  requests:
    cpu: "1"
    memory: "2Gi"
  limits:
    cpu: "2"
    memory: "4Gi"
  JavaOpts: |-
    -XX:MaxRAMPercentage=70.0 
    -XX:MaxRAM=3g
    -Dhudson.slaves.NodeProvisioner.initialDelay=20
    -Dhudson.slaves.NodeProvisioner.MARGIN=50
    -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85
    -Dhudson.model.LoadStatistics.clock=5000
    -Dhudson.model.LoadStatistics.decay=0.2
    -Dhudson.slaves.NodeProvisioner.recurrencePeriod=5000
    -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true
    -Dio.jenkins.plugins.casc.ConfigurationAsCode.initialDelay=10000
    -Djenkins.install.runSetupWizard=false
    -XX:+UseG1GC
    -XX:+UseStringDeduplication
    -XX:+ParallelRefProcEnabled
    -XX:+DisableExplicitGC
    -XX:+UnlockDiagnosticVMOptions
    -XX:+UnlockExperimentalVMOptions
    -javaagent:/otel-auto-instrumentation/javaagent.jar
```

### agent 配置

> 请参照实际的流水线消耗资源设置，因为主要的资源消耗都是来自 agent。

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "256Mi"
  limits:
    cpu: "100m"
    memory: "128Mi"
```

## 场景 2：并行 100 条流水线

### master 配置

```yaml
resources:
  requests:
    cpu: "2"
    memory: "4Gi"
  limits:
    cpu: "2"
    memory: "8Gi"
  JavaOpts: |-
    -XX:MaxRAMPercentage=70.0 
    -XX:MaxRAM=6g
    -Dhudson.slaves.NodeProvisioner.initialDelay=20
    -Dhudson.slaves.NodeProvisioner.MARGIN=50
    -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85
    -Dhudson.model.LoadStatistics.clock=5000
    -Dhudson.model.LoadStatistics.decay=0.2
    -Dhudson.slaves.NodeProvisioner.recurrencePeriod=5000
    -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true
    -Dio.jenkins.plugins.casc.ConfigurationAsCode.initialDelay=10000
    -Djenkins.install.runSetupWizard=false
    -XX:+UseG1GC
    -XX:+UseStringDeduplication
    -XX:+ParallelRefProcEnabled
    -XX:+DisableExplicitGC
    -XX:+UnlockDiagnosticVMOptions
    -XX:+UnlockExperimentalVMOptions
    -javaagent:/otel-auto-instrumentation/javaagent.jar
```

### agent 配置

> 参照场景 1 的 agent 配置

## 场景 3：并行 200 条流水线

### master 配置

```yaml
resources:
  requests:
    cpu: "4"
    memory: "8Gi"
  limits:
    cpu: "8"
    memory: "12Gi"
  JavaOpts: |-
    -XX:MaxRAMPercentage=70.0 
    -XX:MaxRAM=10g
    -Dhudson.slaves.NodeProvisioner.initialDelay=20
    -Dhudson.slaves.NodeProvisioner.MARGIN=50
    -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85
    -Dhudson.model.LoadStatistics.clock=5000
    -Dhudson.model.LoadStatistics.decay=0.2
    -Dhudson.slaves.NodeProvisioner.recurrencePeriod=5000
    -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true
    -Dio.jenkins.plugins.casc.ConfigurationAsCode.initialDelay=10000
    -Djenkins.install.runSetupWizard=false
    -XX:+UseG1GC
    -XX:+UseStringDeduplication
    -XX:+ParallelRefProcEnabled
    -XX:+DisableExplicitGC
    -XX:+UnlockDiagnosticVMOptions
    -XX:+UnlockExperimentalVMOptions
    -javaagent:/otel-auto-instrumentation/javaagent.jar
```

### agent 配置

> 参照场景 1 的 agent 配置
