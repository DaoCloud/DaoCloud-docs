# insight 安全的连接 Kafka

本文主要说明 Insight-agent, Insight chart 在安装时如何给要连接 kafka 的组件配置 TLS 或者 sasl.

## Insight-agent

在 Insight-agent 部署的组件中 Fluentbit 和 Opentelemetry collector 都支持将观测数据发送给指定的 Kafka 集群。以下是按组件分别说明
如何在 Insight-agent chart values 中配置 TLS 或 sasl 参数。 

### Fluentbit

如果 Kafka 开启了 `sasl`, 在 values 中需要添加对应配置，`rdkafka.*` 中的具体的配置说明：
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
          rdkafka.sasl.password: DEtPwFZx1Wnl
```

如果 Kafka 开启了 mTLS, values 中需要添加对应配置：

需要注意，`rdkafka.ssl.*` 中指定的证书位置需要通过 `fluent-bit.extraVolumes` 和 `fluent-bit.extraVolumeMounts` 挂载需要的 secret。

```yaml
global:
  exporters:
    logging:
      kafka:
        rdkafkaProps:
          # 以下是添加的配置
          rdkafka.enable.ssl.certificate.verification: false
          rdkafka.ssl.certificate.location: /certs/some.cert
          rdkafka.ssl.key.location: /certs/some.key
          rdkafka.ssl.ca.location: /certs/some-bundle.crt
          rdkafka.security.protocol: ssl

fluent-bit:
  # 以下是添加的配置
  extraVolumes:
    - name: certificates
      secret:
        secretName: kafka-certificates
  # 以下是添加的配置
  extraVolumeMounts:
    - name: kafka-certificates
      mountPath: /certs
```

如果 Kafka 同时开启了 TLS 和 sasl, values 中需要添加对应配置：
```yaml
global:
  exporters:
    logging:
      kafka:
        rdkafkaProps:
          # 以下是添加的配置
          rdkafka.security.protocol: sasl_ssl
          rdkafka.ssl.ca.location: /fluent-bit/etc/tls/ca.crt
          rdkafka.sasl.mechanisms: PLAIN
          rdkafka.sasl.username: alice
          rdkafka.sasl.password: alice-secret

fluent-bit:
  # 以下是添加的配置
  extraVolumes:
    - name: certificates
      secret:
        secretName: kafka-certificates
  # 以下是添加的配置
  extraVolumeMounts:
    - name: kafka-certificates
      mountPath: /certs
```

### Opentelemetry collector

如果 Kafka 开启了 `sasl`, values 中以下位置添加相关的配置：
```yaml
global:
  exporters:
    trace:
      kafka:
        # 以下是添加的配置
        auth:
          sasl:
            mechanism: PLAIN
            username: alice
            password: alice-secret
```

如果 Kafka 开启了 mTLS, values 中需要添加对应配置：

需要注意，`tls.*` 中指定的证书位置需要通过 `opentelemetry-collector.extraVolumes` 和 `opentelemetry-collector.extraVolumeMounts` 挂载需要的 secret。
更多的配置可以参考：[documents](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/kafkaexporter)。

```yaml
global:
  exporters:
    trace:
      kafka:
        # 以下是添加的配置
        tls:
          ca_file: /etc/otel/tls/cluster.ca.crt
          cert_file: client.crt
          key_file: client.key
          insecure_skip_verify: true
          insecure: false

opentelemetry-collector:
  # 以下是添加的配置
  extraVolumes:
    - name: certificates
      secret:
        secretName: kafka-certificates
  # 以下是添加的配置
  extraVolumeMounts:
    - name: kafka-certificates
      mountPath: /etc/otel/tls
```

如果 Kafka 同时开启了 TLS 和 sasl, values 中需要添加对应配置：
```yaml
global:
  exporters:
    trace:
      kafka:
        # 以下是添加的配置
        tls:
          ca_file: /etc/otel/tls/cluster.ca.crt
          insecure_skip_verify: true
          insecure: false
        auth:
          sasl:
            mechanism: PLAIN
            username: alice
            password: alice-secret

opentelemetry-collector:
  # 以下是添加的配置
  extraVolumes:
    - name: certificates
      secret:
        secretName: kafka-certificates
  # 以下是添加的配置
  extraVolumeMounts:
    - name: kafka-certificates
      mountPath: /etc/otel/tls
```


## Insight

在 Insight chart 中部署的 Vector 和 Opentelemetry collector 都支持从 Kafka 集群获取观测数据。以下是按组件分别说明如何配置。 

### Vector

类似 Fluentbit, Vector 也使用了[librdkafka](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md),
如果 Kafka 开启了 `sasl`, values  中需要添加对应配置：

```yaml
global:
  kafka:
    vector:
      rdkafkaProps:
        # 以下是添加的配置
        security.protocol: sasl_plaintext
        sasl.mechanism: SCRAM-SHA-512
        sasl.username: dce
        sasl.password: DEtPwFZx1Wnl
```
其他的可以参考 librdkafka 中的文档说明。


### Opentelemetry collector

在 Insight chart values 中的配置与在 Insight-agent chart 的配置类似，只是位置有所变化，以 Kafka 同时开启了 TLS 和 sasl 为例：
```yaml
global:
  kafka:
    otelCol:
      # 以下是添加的配置
      auth:
        sasl:
          mechanism: PLAIN
          username: alice
          password: alice-secret
      tls:
        ca_file: /etc/otel/tls/cluster.ca.crt
        cert_file: client.crt
        key_file: client.key
        insecure_skip_verify: true
        insecure: false
```