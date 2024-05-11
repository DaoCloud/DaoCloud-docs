---
MTPE: windsonsesa
date: 2024-05-11
---

# Jenkins Configuration Scenarios

Jenkins is divided into master and agent components. The master primarily handles configuration storage, plugin management, and coordination, while agents communicate with the master through the jnlp container inside the agent pod. Pipeline tasks are executed on agents, which are significant resource consumers.

The configurations recommended here are designed to prevent cluster resource crashes during concurrent execution of all pipelines, especially to avoid issues like eviction of the Jenkins master. The number of pipelines that can run in parallel largely depends on the resource consumption of the actual agents and the capacity of the Kubernetes cluster.

## Scenario 1: Running 50 Concurrent Pipelines

### Master Configuration

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

### Agent Configuration

Adjust based on the actual resource consumption of the pipelines, as the primary resource usage comes from the agents.

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "256Mi"
  limits:
    cpu: "100m"
    memory: "128Mi"
```

## Scenario 2: Running 100 Concurrent Pipelines

### Master Configuration

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

### Agent Configuration

Refer to the agent configuration in [Scenario 1](#agent).

## Scenario 3: Running 200 Concurrent Pipelines

### Master Configuration

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
    -XX:MinRAMPercentage:20.0 -XX:-UseAdaptiveSizePolicy
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

### Agent Configuration

Refer to the agent configuration in [Scenario 1](#agent).

!!! note 

    - When the Jenkins Pod restarts due to OOM, consider increasing the master's memory.
      To ensure QoS, it's recommended that the master's memory and CPU requests and limits remain consistent.
    - If there are timeouts in pipeline module interface calls, consider increasing the master's CPU
    - When the master's memory configuration exceeds __4G__,
      it is advisable to change __JavaOpts__ from __-XX:+UseConcMarkSweepGC__ to __-XX:+UseG1GC__
