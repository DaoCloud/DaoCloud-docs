# 特性门控（Feature Gates）

## 概述

我们使用 Feature Gates 机制来控制不同特性的启用与禁用。Feature Gates 是在 Kubernetes 组件（如 API Server、Controller Manager、Kubelet 等）启动时通过 `--feature-gates` 选项配置的。这些特性可能处于不同的开发阶段（Alpha、Beta 或 GA），并在不同版本中引入或移除。

特性门控是描述 Amamba 特性的一组键值对。你可以在 Amamba 的各个组件中使用 --feature-gates 标志来启用或禁用这些特性。

每个 Amamba 组件都支持启用或禁用与该组件相关的一组特性门控。 使用 -h 参数来查看所有组件支持的完整特性门控。 要为诸如 apiserver 之类的组件设置特性门控，请使用 --feature-gates 参数， 并向其传递一个特性设置键值对列表：

```
--feature-gates=...,ReleaseStats=true
```

也可以通过在 amamba-config 中配置开启：

```yaml
configMap:
  apiServerConfig:
    featureGates:
      - ReleaseStats=true
```

下表总结了在不同的 Amamba 组件上可以设置的特性门控。

- 引入特性或更改其发布阶段后，"开始（Since）" 列将包含 Kubernetes 版本。
- "结束（Until）" 列（如果不为空）包含最后一个 Kubernetes 版本，你仍可以在其中使用特性门控。
- 如果某个特性处于 Alpha 或 Beta 状态，你可以在 Alpha 和 Beta 特性门控表中找到该特性。
- 如果某个特性处于稳定状态， 你可以在已毕业和废弃特性门控表中找到该特性的所有阶段。
- 已毕业和废弃特性门控表还列出了废弃的和已被移除的特性。

## Alpha 和 Beta 状态的特性门控

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

## 已毕业和废弃特性门控表

| Feature             | Default | Stage | Since | Until |
|---------------------|---------|-------|-------|-------|
|                     |         |       |       |       |

# 使用特性

## 特性门控列表

每个特性门控均用于启用或禁用某个特定的特性：

- `ReleaseStats`:
   展示基于流水线的发版信息统计列表。

- `DAGv2`:
   使用新的流水线编辑界面。

- `Gitlab`:
   支持在界面上管理Gitlab项目。

- `Jira`:
   支持在界面上查看Jira项目。

- `KairshipApplication`:
   支持管理多租户级别的多云应用。

- `PipelineAdvancedParameters`:
   支持在流水线配置选项-多选、git分支、镜像标签、制品版本和全局参数类型的参数。

- `AdminGlobalBuildParameter`:
   支持在工作台管理中配置流水线的全局参数。

- `UpstreamPipeline`:
   支持通过OpenAPI的方式在运行流水线的时候指定上游的流水线和运行ID，以保持相同的触发用户。