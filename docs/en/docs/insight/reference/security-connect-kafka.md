# Secure Connection from Insight and insight-agent to Kafka

This document mainly describes how Insight and insight-agent securely connect to Kafka.

## Related Components

The components related to the Kafka data flow are as follows:

| chart         | Component                     | Description                                                |
|---------------|-------------------------------|------------------------------------------------------------|
| Insight       | Vector                        | Consume data such as container logs from Kafka              |
|               | OpenTelemetry Collector       | Consume trace data from Kafka                               |
| insight-agent | Fluent Bit                    | Collect data such as container logs and send them to Kafka  |
|               | Agent OpenTelemetry Collector | Collect trace data and send it to Kafka                     |

## Kafka Authentication Mechanisms

Kafka supports TLS transport encryption as well as multiple authentication mechanisms (SASL):

- TLS (Transport Layer Security): A security protocol for data transmission. It uses encryption to ensure that data is not stolen or tampered with during transmission, improving communication security.
- SASL (Simple Authentication and Security Layer): A security mechanism for identity authentication. It supports the following authentication mechanisms:
    - PLAIN: A simple authentication mechanism based on a plaintext username and password (not recommended for non-TLS traffic).
    - SCRAM: Secure authentication that verifies the username and password using a hash algorithm.
    - GSSAPI: An authentication mechanism based on the Kerberos protocol, which verifies user identity by using tickets.
    - OAUTHBEARER: An authentication mechanism based on OAuth 2.0.

The following sections describe how to configure each component of Insight and insight-agent under different Kafka authentication mechanisms.

## Secure Connection Configuration

> ⚠️ Prerequisite: The related components need to use Kafka.
> 
> 1. Updating only the ConfigMap may cause problems. After you update Insight or insight-agent with Helm, the ConfigMap is reset and becomes ineffective, so the helm values settings are provided here.
> 2. After a Helm upgrade, some components are not restarted and still need to be restarted manually.

### Kafka with SASL Enabled Only

#### insight-agent Chart

1. Fluent-bit

    If SASL is enabled for Kafka, you need to add the corresponding configuration in the values. For details about the specific configuration items in `rdkafka.*`, see
    [librdkafka](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md).

    ```yaml
    global:
      exporters:
        logging:
          kafka:
            rdkafkaProps:
              # Configuration added below
              rdkafka.security.protocol: sasl_plaintext
              rdkafka.sasl.mechanism: SCRAM-SHA-512
              rdkafka.sasl.username: dce
              rdkafka.sasl.password: EZns5a1jNpGA
          
    # If global.exporters.auditLog also uses kafka, add the same configuration
    ```

2. Agent OpenTelemetry Collector

    ```yaml
    global:
      exporters:
        trace:
          enable: true
          kafka:
            # Configuration added below
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
        # Configuration added below 
        vector:
          rdkafkaProps:
            security.protocol: sasl_plaintext
            sasl.mechanism: SCRAM-SHA-512
            sasl.username: dce
            sasl.password: EZns5a1jNpGA
    ```

2. OpenTelemetry Collector

    ```yaml
    global:
      kafka:
        # Configuration added below
        otelCol:
          auth:
            sasl:
              mechanism: SCRAM-SHA-512
              username: dce
              password: EZns5a1jNpGA
    ```

### Kafka with mTLS Enabled

> ⚠️ Use the port exposed for mTLS.

#### insight-agent Chart

First, create a Secret in insight-system, for example kafka-client-cert:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kafka-client-cert
  namespace: insight-system
data:
  tls.crt: xxx    # Update accordingly
  tls.key: xxx    # Update accordingly
  ca.crt: xxx     # Update accordingly
type: kubernetes.io/tls
```

1. fluent-bit

    Use the secret kafka-client-cert as follows and mount kafka-client-cert into the fluent-bit container. Note that the default volume mount configuration must not be lost!

    ```yaml
    # If global.exporters.auditLog also uses kafka, add the same configuration
    global:
      exporters:
        logging:
          kafka:
            # Configuration added below
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
        - name: kafka-client-cert                  # Newly added
          secret:                                  # Newly added
            secretName: kafka-client-cert          # Newly added
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
        - name: kafka-client-cert        # Newly added
          mountPath: /certs              # Newly added
    ```

2. Agent OpenTelemetry Collector

    Use the Secret kafka-client-cert as follows and mount kafka-client-cert into the Agent OpenTelemetry Collector container group.

    ```yaml
    global:
      exporters:
        trace:
          kafka:
            # Configuration added below
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
        - name: kafka-client-cert            # Newly added
          secret:                            # Newly added
            secretName: kafka-client-cert    # Newly added
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-client-cert            # Newly added
          mountPath: /etc/otel/tls           # Newly added
    ```

#### Insight Chart

1. Vector

    Like Fluentbit, Vector also uses librdkafka. If mTLS is enabled for Kafka, you need to add the corresponding configuration in the values:

    ```yaml
    global:
      kafka:
        # Configuration added below
        vector:
          rdkafkaProps:
            enable.ssl.certificate.verification: 'false'  # Newly added
            ssl.certificate.location: /certs/tls.crt      # Newly added
            ssl.key.location: /certs/tls.key              # Newly added
            ssl.ca.location: /certs/ca.crt                # Newly added
            security.protocol: ssl                        # Newly added

    vector:
      extraVolumes:
        - name: kafka-client-cert          # Newly added
          secret:                          # Newly added
            secretName: kafka-client-cert  # Newly added
      extraVolumeMounts:
        - name: kafka-client-cert          # Newly added
          mountPath: /certs                # Newly added     
    ```

2. OpenTelemetry Collector

    ```yaml
    global:
      kafka:
        # Configuration added below
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
        - name: kafka-client-cert            # Newly added
          secret:                            # Newly added
            secretName: kafka-client-cert    # Newly added
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-client-cert            # Newly added
          mountPath: /etc/otel/tls           # Newly added
    ```

### Kafka with TLS and SASL Enabled Simultaneously

#### insight-agent Chart

First, create a Secret in insight-system, for example kafka-cert:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kafka-cert
  namespace: insight-system
data:
  ca.crt: xxx     # Update accordingly, the CA certificate of the Kafka cluster server
type: Opaque
```

1. fluent-bit

    Mount kafka-cert into the fluent-bit container. Note that the default volume mount configuration must not be lost!

    ```yaml
    # If global.exporters.auditLog also uses kafka, add the same configuration
    global:
      exporters:
        logging:
          kafka:
            rdkafkaProps:                                        # Newly added
              rdkafka.security.protocol: sasl_ssl                # Newly added
              rdkafka.enable.ssl.certificate.verification: false # Newly added
              rdkafka.ssl.ca.location: /certs/ca.crt             # Newly added
              rdkafka.sasl.mechanisms: SCRAM-SHA-512             # Newly added
              rdkafka.sasl.username: dce                         # Newly added
              rdkafka.sasl.password: VFRlKIx47CEl                # Newly added

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
        - name: kafka-cert                         # Newly added
          secret:                                  # Newly added
            secretName: kafka-cert                 # Newly added
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
        - name: kafka-cert               # Newly added
          mountPath: /certs              # Newly added
    ```

2. Agent OpenTelemetry Collector

    Use the Secret kafka-client-cert as follows and mount kafka-client-cert into the Agent OpenTelemetry Collector container group.

    ```yaml
    global:
      exporters:
        trace:
          kafka:
            # Configuration added below
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
        - name: kafka-cert            # Newly added
          secret:                     # Newly added
            secretName: kafka-cert    # Newly added
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-cert            # Newly added
          mountPath: /etc/otel/tls    # Newly added
    ```

#### Insight Chart

1. Vector

    ```yaml
    global:
      kafka:
        # Configuration added below
        vector:
          rdkafkaProps:
            security.protocol: sasl_ssl                  # Newly added
            enable.ssl.certificate.verification: 'false' # Newly added
            ssl.ca.location: /certs/ca.crt               # Newly added
            sasl.mechanism: SCRAM-SHA-512                # Newly added
            sasl.username: dce                           # Newly added
            sasl.password: VFRlKIx47CEl                  # Newly added

    vector:
      extraVolumes:                 # Newly added
        - name: kafka-cert          # Newly added
          secret:                   # Newly added
            secretName: kafka-cert  # Newly added
      extraVolumeMounts:            # Newly added
        - name: kafka-cert          # Newly added
          mountPath: /certs         # Newly added 
    ```

2. OpenTelemetry Collector

    ```yaml
    global:
      kafka:
        # Configuration added below
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
        - name: kafka-cert                   # Newly added
          secret:                            # Newly added
            secretName: kafka-cert           # Newly added
      extraVolumeMounts:
        - name: otelcol-configmap
          mountPath: /conf/insight
        - name: kafka-cert                   # Newly added
          mountPath: /etc/otel/tls           # Newly added
    ```

## References

### Enable SASL for the Built-in Kafka

By default, DCE 5.0 only installs the Cluster Operator. If you want to use the Kafka built into DCE 5.0, you can enable the User Operator and the SASL configuration as follows.

1. Update the Kafka CR

    Edit the Kafka CR with `kubectl edit kafka -n mcamel-system mcamel-common-kafka-cluster` and update it as follows:

    ```yaml
    spec:
      entityOperator:           # Newly added
        userOperator: {}        # Newly added
      kafka:
        listeners:
        - authentication:        # Newly added
            type: scram-sha-512  # Newly added
          name: plain
          port: 9092
          tls: false
          type: nodeport
        - authentication:        # Newly added
            type: scram-sha-512  # Newly added
          name: tls
          port: 9093
          tls: false
          type: internal
    ```

    After the update is complete, wait until the Kafka instance and the newly added entityOperator are both running properly.

2. Create a Kafka User

    The authentication mechanisms supported by a Kafka user include scram-sha-512, tls, and tls-external.

    - scram-sha-512: Generates a secret containing the SASL SCRAM-SHA-512 credentials.
    - tls: Generates a secret containing a user certificate, which is used for two-way TLS authentication.
    - tls-external: Does not generate a user certificate, but prepares for two-way TLS authentication with an externally generated user certificate.

    You can create a Kafka User with a random password or with a specified password.

    __Method 1: Create a kafka user with a random password__

    ```shell
    cat << EOF | kubectl apply -f -
    apiVersion: kafka.strimzi.io/v1beta2
    kind: KafkaUser
    metadata:
      name: dce
      namespace: mcamel-system
      labels:
        strimzi.io/cluster: mcamel-common-kafka-cluster  # Must match the Kafka cluster name
    spec:
      authentication:
        type: scram-sha-512
    EOF
    ```

    After the Kafka user is created, a secret with the same name is created by default in the current namespace mcamel-system. You can view the generated random password with the command:
    `kubectl get secrets -n mcamel-system dce -o jsonpath='{.data.password}' |base64 -d`

    **Method 2: Create a kafka user with a specified password**

    ```shell
    # Create a secret and specify the password. Replace secret-name as needed.
    kubectl create secret generic -n mcamel-system ${secret-name} --from-literal=${password-key}=${password-value}

    # For example, if the secret name is dce1, password-key is password, and password-value is Daocloud
    kubectl create secret generic -n mcamel-system dce1 --from-literal=password=Daocloud

    # Then you can apply the following kafka user yaml
    cat << EOF | kubectl apply -f -
    apiVersion: kafka.strimzi.io/v1beta2
    kind: KafkaUser
    metadata:
      name: dce1
      namespace: mcamel-system
      labels:
        strimzi.io/cluster: mcamel-common-kafka-cluster  # Must match the Kafka cluster name
    spec:
      authentication:
        type: scram-sha-512
        password:
          valueFrom:
            secretKeyRef:
             name: dce1  # Replace with the Secret name
             key: password   # Replace with the password-key, that is, the key that stores the password in the Secret
    EOF
    ```

### Enable mTLS for the Built-in Kafka

Edit the Kafka CR:

```yaml
# Edit kafka
kubectl edit kafka -n mcamel-system mcamel-common-kafka-cluster
```

Update it as follows:

```yaml
spec:
  entityOperator:
    userOperator: {}
  kafka:
    listeners:
    - authentication: # Newly added
        type: tls     # Newly added
      name: mtls      # Newly added
      port: 9094      # Newly added
      tls: true       # Newly added
      type: nodeport  # Newly added
```

Create a Kafka User that uses TLS authentication:

```yaml
cat << EOF | kubectl apply -f -
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaUser
metadata:
  name: dce
  namespace: mcamel-system
  labels:
    strimzi.io/cluster: mcamel-common-kafka-cluster  # Must match the Kafka cluster name
spec:
  authentication:
    type: tls
EOF
```

Then use the corresponding fields user.key, user.crt, and the root certificate ca.crt in the generated secret dce. Obtain them with the following script:

```yaml
kubectl get secret dce -n mcamel-system -o jsonpath='{.data.user\.key}' | base64 --decode 
kubectl get secret dce -n mcamel-system -o jsonpath='{.data.user\.crt}' | base64 --decode 
kubectl get secret dce -n mcamel-system -o jsonpath='{.data.ca\.crt}' | base64 --decode 
```

### Enable TLS and SASL Simultaneously for the Built-in Kafka

Edit the Kafka CR:

```yaml
# Edit kafka
kubectl edit kafka -n mcamel-system mcamel-common-kafka-cluster
```

Update it as follows:

```yaml
spec:
  entityOperator:            # Newly added
    userOperator: {}         # Newly added
  kafka:
    listeners:
      - authentication:        # Newly added
          type: scram-sha-512  # Newly added
        name: tlssasl          # Newly added
        port: 9095             # Newly added
        tls: true              # Newly added, the difference from enabling SASL alone
        type: nodeport         # Newly added
```

### redpanda-console Configuration

The built-in addon redpanda-console does not expose the Kafka security configuration by default, so you need to configure it manually.
The following is how to configure redpanda-console when SASL is enabled for Kafka:

1. Install redpanda-console from the App Store.
2. Edit the spec.template.spec.containers field in the redpnada-console deployment and add the following information:

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
