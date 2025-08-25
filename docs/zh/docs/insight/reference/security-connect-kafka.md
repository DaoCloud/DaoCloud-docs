# Insight 和 insight-agent 安全连接到 Kafka

本文主要说明 Insight 和 insight-agent 如何安全连接到 Kafka。

## 关联组件

与 Kafka 数据流相关的组件如下：

| chart         | 组件                            | 说明                  |
|---------------|-------------------------------|---------------------|
| Insight       | Vector                        | 消费 Kafka 中的容器日志等数据  |
|               | Opentelemetry Collector       | 消费 Kafka 中的链路数据     |
| insight-agent | Fluent Bit                    | 采集容器日志等数据并发送到 Kafka |
|               | Agent Opentelemetry Collector | 采集链路数据并发送到 Kafka    |

## Kafka 认证机制

Kafka 支持 TLS 传输加密以及多种认证机制（SASL）：

- TLS（Transport Layer Security）：数据传输安全协议，通过加密技术确保数据在传输过程中不被窃取或篡改，提升通信安全性。
- SASL（Simple Authentication and Security Layer）：是一种用于身份认证的安全机制，支持以下几种验证机制：
    - PLAIN 机制：基于明文用户名和密码的简单认证机制（不建议在非 TLS 流量中使用）。
    - SCRAM 机制：采用哈希算法对用户名与密码进行身份校验的安全认证。
    - GSSAPI 机制：基于 Kerberos 协议的认证机制，它使用票据的方式来验证用户身份。
    - OAUTHBEARER 机制：基于OAuth 2.0的认证机制。

以下将介绍 Kafka 在不同认证机制下，如何配置 Insight 和 insight-agent 的各个组件。

## 安全连接配置

> ⚠️ 前提：需要相关组件使用 Kafka
> 
> 1. 只更新 ConfigMap 可能会存在问题。使用 Helm 更新 insight 或 insight-agent 后，ConfigMap 会重置导致失效，所以此处给出 helm values 设置。
> 2. Helm 升级后，部分组件不会重启，仍需要手动重启。

### Kafka 只开启 SASL 配置

#### insight-agent Chart

1. Fluent-bit

    如果 Kafka 开启了 SASL，在 values 中需要添加对应配置，`rdkafka.*` 中的具体的配置说明参见
    [librdkafka](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md)

    ```yaml
    global:
      exporters:
        logging:
          kafka:
            rdkafkaProps:
              # 以下是添加的配置
              rdkafka.security.protocol: sasl_plaintext
              rdkafka.sasl.mechanism: SCRAM-SHA-512
              rdkafka.sasl.username: dce
              rdkafka.sasl.password: EZns5a1jNpGA
          
    # 如果 global.exporters.auditLog 同样使用 kafka 则添加相同的配置
    ```

2. Agent Opentelemetry collector

    ```yaml
    global:
      exporters:
        trace:
          enable: true
          kafka:
            # 以下是添加的配置
            auth:
              sasl:
                mechanism: SCRAM-SHA-512
                username: dce
                password: EZns5a1jNpGA
    ```

#### Insight Chart

1. Vector

    ```yaml
    global: 
      kafka:
        # 以下是添加的配置 
        vector:
          rdkafkaProps:
            security.protocol: sasl_plaintext
            sasl.mechanism: SCRAM-SHA-512
            sasl.username: dce
            sasl.password: EZns5a1jNpGA
    ```

2. Opentelemetry collector

    ```yaml
    global:
      kafka:
        # 以下是添加的配置
        otelCol:
          auth:
            sasl:
              mechanism: SCRAM-SHA-512
              username: dce
              password: EZns5a1jNpGA
    ```

### Kafka 开启 mTLS

> ⚠️ 使用 mTLS 对应暴露的端口

#### insight-agent Chart

需要首先在 insight-system 下创建一个 Secret，例如 kafka-client-cert：

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kafka-client-cert
  namespace: insight-system
data:
  tls.crt: xxx    # 需对应修改
  tls.key: xxx    # 需对应修改
  ca.crt: xxx     # 需对应修改
type: kubernetes.io/tls
```

1. fluent-bit

    需要按照以下配置使用 secret kafka-client-cert 并将 kafka-client-cert 挂载进 fluent-bit 容器内。需要注意的是，默认的卷挂载配置不可丢失！

    ```yaml
    # 如果 global.exporters.auditLog 同样使用 kafka 则添加相同的配置
    global:
      exporters:
        logging:
          kafka:
            # 以下是添加的配置
            rdkafkaProps:
              rdkafka.enable.ssl.certificate.verification: false
              rdkafka.ssl.certificate.location: /certs/tls.crt
              rdkafka.ssl.key.location: /certs/tls.key
              rdkafka.ssl.ca.location: /certs/ca.crt
              rdkafka.security.protocol: ssl

    fluent-bit:
      extraVolumes:
        - name: luascripts
          configMap:
            name: insight-agent-fluent-bit-luascripts-config
            defaultMode: 420
        - name: sysctl-config-volume
          configMap:
            name: fluent-bit-kube-node-tuning-config
            defaultMode: 493
        - name: etcmachineid
          emptyDir: {}
        - name: date-config
          hostPath:
            path: /etc/localtime
        - name: kafka-client-cert                  # 新增
          secret:                                  # 新增
            secretName: kafka-client-cert          # 新增
      extraVolumeMounts:
        - name: date-config
          mountPath: /etc/localtime
          readOnly: true
        - name: luascripts
          mountPath: /fluent-bit/scripts/add_time.lua
          subPath: add_time.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/kube_audit_filter.lua
          subPath: kube_audit_filter.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/container_log_filter.lua
          subPath: container_log_filter.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/update_dmesg.lua
          subPath: update_dmesg.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/update_message_log.lua
          subPath: update_message_log.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/update_systemd.lua
          subPath: update_systemd.lua
        - name: luascripts
          mountPath: /usr/local/share/lua/5.1/common_utils.lua
          subPath: common_utils.lua
        - name: luascripts
          mountPath: /usr/local/share/lua/5.1/json.lua
          subPath: json.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/event_transform.lua
          subPath: event_transform.lua
        - name: kafka-client-cert        # 新增
          mountPath: /certs              # 新增
    ```

2. Agent OpenTelemetry Collector

    需要按照以下配置使用 Secret kafka-client-cert  并将 kafka-client-cert 挂载进 Agent OpenTelemetry Collector 容器组内。

    ```yaml
    global:
      exporters:
        trace:
          kafka:
            # 以下是添加的配置
            tls:
              ca_file: /etc/otel/tls/ca.crt
              cert_file: /etc/otel/tls/tls.crt
              key_file: /etc/otel/tls/tls.key
              insecure_skip_verify: true
              insecure: false

    opentelemetry-collector:
     extraVolumes:
        - name: otelcol-configmap
          configMap:
            name: 'insight-agent-otel-collector-config'
            items:
              - key: config
                path: config.yaml
            defaultMode: 420
        - name: kafka-client-cert            # 新增
          secret:                            # 新增
            secretName: kafka-client-cert    # 新增
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-client-cert            # 新增
          mountPath: /etc/otel/tls           # 新增
    ```

#### Insight Chart

1. Vector

    类似 Fluentbit，Vector 也使用了 librdkafka。如果 Kafka 开启了 mTLS，在 values 中需要添加对应配置：

    ```yaml
    global:
      kafka:
        # 以下是添加的配置
        vector:
          rdkafkaProps:
            enable.ssl.certificate.verification: 'false'  # 新增
            ssl.certificate.location: /certs/tls.crt      # 新增
            ssl.key.location: /certs/tls.key              # 新增
            ssl.ca.location: /certs/ca.crt                # 新增
            security.protocol: ssl                        # 新增

    vector:
      extraVolumes:
        - name: kafka-client-cert          # 新增
          secret:                          # 新增
            secretName: kafka-client-cert  # 新增
      extraVolumeMounts:
        - name: kafka-client-cert          # 新增
          mountPath: /certs                # 新增     
    ```

2. OpenTelemetry Collector

    ```yaml
    global:
      kafka:
        # 以下是添加的配置
        otelCol:
          tls:
            ca_file: /etc/otel/tls/ca.crt
            cert_file: /etc/otel/tls/tls.crt
            key_file: /etc/otel/tls/tls.key
            insecure_skip_verify: true
            insecure: false

    opentelemetry-collector:
      extraVolumes:
        - name: otelcol-configmap
          configMap:
            name: 'insight-otel-collector-config'
            items:
              - key: config
                path: config.yaml
            defaultMode: 420
        - name: kafka-client-cert            # 新增
          secret:                            # 新增
            secretName: kafka-client-cert    # 新增
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-client-cert            # 新增
          mountPath: /etc/otel/tls           # 新增
    ```

### Kafka 同时开始 TLS 和 sasl

#### insight-agent Chart

需要首先在 insight-system 下创建一个 Secret，例如 kafka-cert：

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kafka-cert
  namespace: insight-system
data:
  ca.crt: xxx     # 需对应修改, Kafka 集群服务器的 CA证书
type: Opaque
```

1. fluent-bit

    将 kafka-cert 挂载进 fluent-bit 容器内。需要注意的是，默认的卷挂载配置不可丢失！

    ```yaml
    # 如果 global.exporters.auditLog 同样使用 kafka 则添加相同的配置
    global:
      exporters:
        logging:
          kafka:
            rdkafkaProps:                                        # 新增
              rdkafka.security.protocol: sasl_ssl                # 新增
              rdkafka.enable.ssl.certificate.verification: false # 新增
              rdkafka.ssl.ca.location: /certs/ca.crt             # 新增
              rdkafka.sasl.mechanisms: SCRAM-SHA-512             # 新增
              rdkafka.sasl.username: dce                         # 新增
              rdkafka.sasl.password: VFRlKIx47CEl                # 新增

    fluent-bit:
      extraVolumes:
        - name: luascripts
          configMap:
            name: insight-agent-fluent-bit-luascripts-config
            defaultMode: 420
        - name: sysctl-config-volume
          configMap:
            name: fluent-bit-kube-node-tuning-config
            defaultMode: 493
        - name: etcmachineid
          emptyDir: {}
        - name: date-config
          hostPath:
            path: /etc/localtime
        - name: kafka-cert                         # 新增
          secret:                                  # 新增
            secretName: kafka-cert                 # 新增
      extraVolumeMounts:
        - name: date-config
          mountPath: /etc/localtime
          readOnly: true
        - name: luascripts
          mountPath: /fluent-bit/scripts/add_time.lua
          subPath: add_time.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/kube_audit_filter.lua
          subPath: kube_audit_filter.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/container_log_filter.lua
          subPath: container_log_filter.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/update_dmesg.lua
          subPath: update_dmesg.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/update_message_log.lua
          subPath: update_message_log.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/update_systemd.lua
          subPath: update_systemd.lua
        - name: luascripts
          mountPath: /usr/local/share/lua/5.1/common_utils.lua
          subPath: common_utils.lua
        - name: luascripts
          mountPath: /usr/local/share/lua/5.1/json.lua
          subPath: json.lua
        - name: luascripts
          mountPath: /fluent-bit/scripts/event_transform.lua
          subPath: event_transform.lua
        - name: kafka-cert               # 新增
          mountPath: /certs              # 新增
    ```

2. Agent OpenTelemetry Collector

    需要按照以下配置使用 Secret kafka-client-cert  并将 kafka-client-cert 挂载进 Agent OpenTelemetry Collector 容器组内。

    ```yaml
    global:
      exporters:
        trace:
          kafka:
            # 以下是添加的配置
            tls:
              ca_file: /etc/otel/tls/ca.crt
              insecure_skip_verify: true
              insecure: false
            auth:
              sasl:
                mechanism: SCRAM-SHA-512
                username: dce
                password: VFRlKIx47CEl

    opentelemetry-collector:
      extraVolumes:
        - name: otelcol-configmap
          configMap:
            name: 'insight-agent-otel-collector-config'
            items:
              - key: config
                path: config.yaml
            defaultMode: 420
        - name: kafka-cert            # 新增
          secret:                     # 新增
            secretName: kafka-cert    # 新增
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-cert            # 新增
          mountPath: /etc/otel/tls    # 新增
    ```

#### Insight Chart

1. Vector

    ```yaml
    global:
      kafka:
        # 以下是添加的配置
        vector:
          rdkafkaProps:
            security.protocol: sasl_ssl                  # 新增
            enable.ssl.certificate.verification: 'false' # 新增
            ssl.ca.location: /certs/ca.crt               # 新增
            sasl.mechanism: SCRAM-SHA-512                # 新增
            sasl.username: dce                           # 新增
            sasl.password: VFRlKIx47CEl                  # 新增

    vector:
      extraVolumes:                 # 新增
        - name: kafka-cert          # 新增
          secret:                   # 新增
            secretName: kafka-cert  # 新增
      extraVolumeMounts:            # 新增
        - name: kafka-cert          # 新增
          mountPath: /certs         # 新增 
    ```

2. OpenTelemetry Collector

    ```yaml
    global:
      kafka:
        # 以下是添加的配置
        otelCol:
          tls:
            ca_file: /etc/otel/tls/ca.crt
            insecure_skip_verify: true
            insecure: false
          auth:
            sasl:
              mechanism: SCRAM-SHA-512
              username: dce
              password: VFRlKIx47CEl

    opentelemetry-collector:
     extraVolumes:
        - name: otelcol-configmap
          configMap:
            name: 'insight-otel-collector-config'
            items:
              - key: config
                path: config.yaml
            defaultMode: 420
        - name: kafka-cert                   # 新增
          secret:                            # 新增
            secretName: kafka-cert           # 新增
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-cert                   # 新增
          mountPath: /etc/otel/tls           # 新增
    ```

## 参考内容

### 内置 Kafka 开启 sasl 配置

DCE5 默认只安装了 Cluster Operator。如果要使用 DCE5 内置的 Kafka，则可按照以下方式开启 User Operator 和 SASL 配置。

1. 更新 Kafka CR

    通过 `kubectl edit kafka -n mcamel-system mcamel-common-kafka-cluster` 编辑 Kafka CR，按照如下内容更新：

    ```yaml
    spec:
      entityOperator:           # 新增
        userOperator: {}        # 新增
      kafka:
        listeners:
        - authentication:        # 新增
            type: scram-sha-512  # 新增
          name: plain
          port: 9092
          tls: false
          type: nodeport
        - authentication:        # 新增
            type: scram-sha-512  # 新增
          name: tls
          port: 9093
          tls: false
          type: internal
    ```

    更新完成后，等待 Kafka 实例以及新增的 entityOperator 均正常运行。

2. 创建 Kafka User

    Kafka 用户支持的身份验证机制包括 scram-sha-512、tls 和 tls-external。

    - scram-sha-512：生成一个包含 SASL SCRAM-SHA-512 凭据的密钥。
    - tls：生成一个包含用户证书的密钥，用于双向 TLS 身份验证。
    - tls-external：不生成用户证书，但为使用外部生成的用户证书进行双向 TLS 身份验证做好准备。

    可选择创建随机密码的 Kafka User，也可创建指定密码的 Kafka User

    **方式一：创建随机密码的 kafka user**

    ```shell
    cat << EOF | kubectl apply -f -
    apiVersion: kafka.strimzi.io/v1beta2
    kind: KafkaUser
    metadata:
      name: dce
      namespace: mcamel-system
      labels:
        strimzi.io/cluster: mcamel-common-kafka-cluster  # 必须匹配Kafka集群名称
    spec:
      authentication:
        type: scram-sha-512
    EOF
    ```

    Kafka user 创建完成后，会在当前命名空间 mcamel-system 下默认创建同名的 secret。可使用命令查看生成的随机密码：
    `kubectl get secrets -n mcamel-system dce -o jsonpath='{.data.password}' |base64 -d`

    **方法二 创建指定密码的 kafka user**

    ```shell
    # 创建 secret，指定密码。需自定更新 secret-name,
    kubectl create secret generic -n mcamel-system ${secret-name} --from-literal=${password-key}=${password-value}

    # 举例说明：例如 secret 名称为 dce1，password-key 为 password，password-value 为 Daocloud
    kubectl create secret generic -n mcamel-system dce1 --from-literal=password=Daocloud

    # 那么，可下发以下的 kafka user yaml
    cat << EOF | kubectl apply -f -
    apiVersion: kafka.strimzi.io/v1beta2
    kind: KafkaUser
    metadata:
      name: dce1
      namespace: mcamel-system
      labels:
        strimzi.io/cluster: mcamel-common-kafka-cluster  # 必须匹配 Kafka 集群名称
    spec:
      authentication:
        type: scram-sha-512
        password:
          valueFrom:
            secretKeyRef:
             name: dce1  # 替换为 Secret 名称
             key: password   # 替换为password-key，即 Secret 中存储密码的键
    EOF
    ```

### 内置 Kafka 开启 mTLS 配置

编辑 Kafka CR：

```yaml
# 编辑 kafka
kubectl edit kafka -n mcamel-system mcamel-common-kafka-cluster
```

按照如下内容更新：

```yaml
spec:
  entityOperator:
    userOperator: {}
  kafka:
    listeners:
    - authentication: # 新增
        type: tls     # 新增
      name: mtls      # 新增
      port: 9094      # 新增
      tls: true       # 新增
      type: nodeport  # 新增
```

创建使用 TLS 验证的 Kafka User：

```yaml
cat << EOF | kubectl apply -f -
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaUser
metadata:
  name: dce
  namespace: mcamel-system
  labels:
    strimzi.io/cluster: mcamel-common-kafka-cluster  # 必须匹配Kafka集群名称
spec:
  authentication:
    type: tls
EOF
```

后续则使用生成的 secert dce 中 user.key、user.crt 和根证书 ca.crt 对应字段。按照下方脚本获取：

```yaml
kubectl get secret dce -n mcamel-system -o jsonpath='{.data.user\.key}' | base64 --decode 
kubectl get secret dce -n mcamel-system -o jsonpath='{.data.user\.crt}' | base64 --decode 
kubectl get secret dce -n mcamel-system -o jsonpath='{.data.ca\.crt}' | base64 --decode 
```

### 内置 Kafka 同时开启 TLS 和 SASL 配置

编辑 Kafka CR：

```yaml
# 编辑 kafka
kubectl edit kafka -n mcamel-system mcamel-common-kafka-cluster
```

按照如下内容更新：

```yaml
spec:
  entityOperator:            # 新增
    userOperator: {}         # 新增
  kafka:
    listeners:
      - authentication:        # 新增
          type: scram-sha-512  # 新增
        name: tlssasl          # 新增
        port: 9095             # 新增
        tls: true              # 新增，与单纯开启SASL的区别
        type: nodeport         # 新增
```

### redpanda-console 配置

默认内置的 addon redpanda-console 未暴露 Kafka 的 安全配置，需要手动配置。
以下是 Kafka 开启 sasl 情况下 redpanda-console 的配置方法：

1. 应用商店中安装 redpanda-console
2. 编辑 redpnada-console deployment 中的 spec.template.spec.containers 字段，添加以下信息：

    ```yaml
        env:
        - name: KAFKA_TLS_ENABLED
          value: "false"
        - name: KAFKA_SASL_ENABLED
          value: "true"
        - name: KAFKA_SASL_MECHANISM
          value: SCRAM-SHA-512
        - name: KAFKA_SASL_USERNAME
          value: dce1
        - name: KAFKA_SASL_PASSWORD
          value: Daocloud
    ```
   
