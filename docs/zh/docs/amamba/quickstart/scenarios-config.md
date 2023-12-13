# Jenkins 场景配置

Jenkins 分为 master 和 agent。master 主要用于存储配置，插件和协调，agent 和 master 之间通过
agent 这个 Pod 里的 jnlp 容器通信。流水线的工作都在 agent 上，是资源消耗大户。

本文推荐的配置是基于客户并行运行的所有流水线时不会导致整个集群资源崩溃，尤其是 jenkins master
不会出现被驱逐等异常情况。能够并行多少条流水线主要取决于实际 agent 的资源消耗和 K8s 集群资源的大小。

## 场景 1：并行 50 条流水线

### master 配置

```yaml
resources:
  requests:
    cpu: "2"
    memory: "2Gi"
  limits:
    cpu: "2"
    memory: "2Gi"
  JavaOpts: |-
        -XX:+PrintFlagsFinal -XX:MaxRAMPercentage=70.0
        -XX:MinHeapFreeRatio=8 -XX:MaxHeapFreeRatio=15
        -XX:MinRAMPercentage=20.0 -XX:-UseAdaptiveSizePolicy
        -XX:-ShrinkHeapInSteps
        -Dhudson.slaves.NodeProvisioner.initialDelay=20
        -Dhudson.slaves.NodeProvisioner.MARGIN=50
        -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85
        -Dhudson.model.LoadStatistics.clock=5000
        -Dhudson.model.LoadStatistics.decay=0.2
        -Dhudson.slaves.NodeProvisioner.recurrencePeriod=5000
        -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true
        -Dio.jenkins.plugins.casc.ConfigurationAsCode.initialDelay=10000
        -Djenkins.install.runSetupWizard=false  
        -XX:+UseConcMarkSweepGC
        -XX:+UseStringDeduplication -XX:+ParallelRefProcEnabled
        -XX:+DisableExplicitGC -XX:+UnlockDiagnosticVMOptions
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
    memory: "3Gi"
  limits:
    cpu: "2"
    memory: "3Gi"
  JavaOpts: |-
    -XX:+PrintFlagsFinal -XX:MaxRAMPercentage=70.0
    -XX:MinHeapFreeRatio=8 -XX:MaxHeapFreeRatio=15
    -XX:MinRAMPercentage=20.0 -XX:-UseAdaptiveSizePolicy
    -XX:-ShrinkHeapInSteps
    -Dhudson.slaves.NodeProvisioner.initialDelay=20
    -Dhudson.slaves.NodeProvisioner.MARGIN=50
    -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85
    -Dhudson.model.LoadStatistics.clock=5000
    -Dhudson.model.LoadStatistics.decay=0.2
    -Dhudson.slaves.NodeProvisioner.recurrencePeriod=5000
    -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true
    -Dio.jenkins.plugins.casc.ConfigurationAsCode.initialDelay=10000
    -Djenkins.install.runSetupWizard=false  
    -XX:+UseConcMarkSweepGC
    -XX:+UseStringDeduplication -XX:+ParallelRefProcEnabled
    -XX:+DisableExplicitGC -XX:+UnlockDiagnosticVMOptions
    -XX:+UnlockExperimentalVMOptions
    -javaagent:/otel-auto-instrumentation/javaagent.jar
```

### agent 配置

> 参照[场景 1](#agent) 的 agent 配置

## 场景 3：并行 200 条流水线

### master 配置

```yaml
resources:
  requests:
    cpu: "2"
    memory: "3Gi"
  limits:
    cpu: "2"
    memory: "3Gi"
  JavaOpts: |-
    -XX:+PrintFlagsFinal -XX:MaxRAMPercentage=70.0
    -XX:MinHeapFreeRatio=8 -XX:MaxHeapFreeRatio=15
    -XX:MinRAMPercentage=20.0 -XX:-UseAdaptiveSizePolicy
    -XX:-ShrinkHeapInSteps
    -Dhudson.slaves.NodeProvisioner.initialDelay=20
    -Dhudson.slaves.NodeProvisioner.MARGIN=50
    -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85
    -Dhudson.model.LoadStatistics.clock=5000
    -Dhudson.model.LoadStatistics.decay=0.2
    -Dhudson.slaves.NodeProvisioner.recurrencePeriod=5000
    -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true
    -Dio.jenkins.plugins.casc.ConfigurationAsCode.initialDelay=10000
    -Djenkins.install.runSetupWizard=false  
    -XX:+UseConcMarkSweepGC
    -XX:+UseStringDeduplication -XX:+ParallelRefProcEnabled
    -XX:+DisableExplicitGC -XX:+UnlockDiagnosticVMOptions
    -XX:+UnlockExperimentalVMOptions
    -javaagent:/otel-auto-instrumentation/javaagent.jar
```

### agent 配置

> 参照[场景 1](#agent) 的 agent 配置

### 注意事项

- 当 Jenkins Pod 因为 OOM 重启时，建议加大 Master 的内存。
  为了保证 QoS，建议 Master 的内存和 cpu 的 request 和 limit 保持一致。
- 当流水线模块接口调用存在超时情况时，建议加大 Master 的CPU。
- 当 Master 内存配置超过 __4G__ 时，建议修改 __JavaOpts__ 中的 __-XX:+UseConcMarkSweepGC__ 为 __-XX:+UseG1GC__ 。
