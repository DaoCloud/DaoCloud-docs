# Fluent Bit 根据 Kubernetes Namespace Name 路由至不同的 Topic

Fluent Bit 根据 Kubernetes Namespace Name 发送到不同 Topic 的使用场景主要是在容器化应用环境中，基于 Kubernetes 平台，实现日志的分类管理与精准传输。

具体来说，在大型的 Kubernetes 集群中，不同的 Namespace 可能用于部署不同的应用、服务或项目，例如开发、测试、生产环境可能各自有独立的 Namespace。通过 Fluent Bit 根据 Namespace Name 将日志发送到不同的 Topic ，可以实现以下功能：

1. 日志隔离：不同 Namespace 的日志分别发送到不同 Topic ，避免日志混淆，便于对特定应用或服务的日志进行单独分析和排查问题。
2. 权限管理：根据 Topic 来控制对不同 Namespace 日志的访问权限，满足安全合规要求。例如，生产环境的日志可能需要更严格的访问控制，通过不同 Topic 可以更方便地进行权限设置。
3. 日志处理优化：可以针对不同 Topic 的日志采用不同的处理策略。例如，对于重要业务的日志进行更详细的分析和存储，而对于测试环境的日志可以采用更轻量级的处理方式。
4. 多租户支持：在多租户的 Kubernetes 环境中，每个租户的应用部署在不同的 Namespace ，通过将日志发送到不同 Topic ，可以实现租户间日志的隔离和独立管理。
5. 监控与告警：可以针对不同 Topic 的日志设置不同的监控规则和告警策略。例如，当某个 Namespace 的日志出现异常时，能够及时触发告警，方便运维人员快速响应。

## 实现思路
借助 Fluent Bit Kafka output 根据 [topic_key][1] 动态路由到不同 Topic 的能力实现。

## 实现步骤
1. 在现有 `insight-agent-Fluent Bit-luascripts-config` Configmap 中对 Lua 脚本 `container_log_filter.lua` 中增加如下逻辑(可根据实际需求调整), 该逻辑将从 `kubernetes.namespace_name` 取值并赋值给 `router` 字段。

    ```diff
          annotations = record["kubernetes"]["annotations"]
          if(annotations == nil) then
            debugLog("miss annotations in kubernetes, skip filter")
            return 1, timestamp, record
          end
    
    +      if(record["kubernetes"]["namespace_name"] ~= nil and record["kubernetes"]["namespace_name"] ~= '') then
    +        record['router'] = record["kubernetes"]["namespace_name"]
    +      end
    ```

2. 在现有 `insight-agent-Fluent Bit-config` Configmap 中对  Kafka Output 增加 `topic_key` 配置并开启 `dynamic_topic`:
```diff
        Topics      insight-logs
        format      json
        # topic_key 优先于 Topics
+       dynamic_topic On
+       topic_key   router
```

3. 重启 Fluentbit，观察 kafka 中 topic 是否被创建或有数据写入。

[1]: https://docs.fluentbit.io/manual/pipeline/outputs/kafka