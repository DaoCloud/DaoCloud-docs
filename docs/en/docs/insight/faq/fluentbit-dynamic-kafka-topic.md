# Fluent Bit Routes Logs to Different Topics Based on the Kubernetes Namespace Name

The use case of Fluent Bit sending logs to different Topics based on the Kubernetes Namespace Name is mainly found in containerized application environments, where it enables categorized log management and precise log delivery on the Kubernetes platform.

Specifically, in large Kubernetes clusters, different Namespaces may host different applications, services, or projects. For example, development, testing, and production environments may each have their own Namespaces. By having Fluent Bit send logs to different Topics based on the Namespace Name, you can achieve the following:

1. Log isolation: Logs from different Namespaces are sent to different Topics to prevent log mixing, making it easier to analyze and troubleshoot the logs of specific applications or services.
2. Access control: Access to logs from different Namespaces can be controlled per Topic to meet security and compliance requirements. For example, logs from the production environment may require stricter access control, and using different Topics makes permission configuration more convenient.
3. Optimized log processing: Different processing strategies can be applied to logs in different Topics. For example, logs of critical services can be analyzed and stored in more detail, while logs of test environments can be handled in a lighter-weight way.
4. Multi-tenant support: In multi-tenant Kubernetes environments, each tenant's applications are deployed in different Namespaces. Sending logs to different Topics enables log isolation and independent management between tenants.
5. Monitoring and alerting: Different monitoring rules and alerting policies can be configured for logs in different Topics. For example, when logs in a Namespace show anomalies, alerts can be triggered promptly so that operations staff can respond quickly.

## Implementation Approach

This is achieved by leveraging the Fluent Bit Kafka output's ability to dynamically route logs to different Topics based on [topic_key][1].

## Implementation Steps

1. In the existing `insight-agent-Fluent Bit-luascripts-config` Configmap, add the following logic to the Lua script `container_log_filter.lua` (adjust it as needed). This logic reads the value from `kubernetes.namespace_name` and assigns it to the `router` field.

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

2. In the existing `insight-agent-Fluent Bit-config` Configmap, add the `topic_key` configuration to the Kafka Output and enable `dynamic_topic`:

    ```diff
            Topics      insight-logs
            format      json
            # topic_key takes precedence over Topics
    +       dynamic_topic On
    +       topic_key   router
    ```

3. Restart Fluent Bit and check whether the topic is created in Kafka or data is written to it.

[1]: https://docs.fluentbit.io/manual/pipeline/outputs/kafka
