# Add custom plugins for RabbitMQ

## Problem Description

RabbitMQ has many plug-ins, but when installing RabbitMQ, only the default plug-ins can be installed. If you need to install other plug-ins, you need to install them manually after the installation is complete.

## solution

In the yaml of RabbitMQ created, add initContainer to download the plugin, then hang the plugin in the plugin directory of RabbitMQ, and finally add the configuration of the plugin in the config of rabbitmq, and enable the plugin in the enabled plugin module .

## Example

Here, taking rabbitmq_message_timestamp-3.8.0.ez as an example, the main content is as follows:

- Added initContainer for downloading plugins
- Then hang the plugin in the plugin directory of RabbitMQ
- In the config of rabbitmq, the configuration of the plug-in is added
- and enable the plugin in the enabled plugins module

> Modify the sample instance code

```yaml
-

```yaml
apiVersion: rabbitmq.com/v1beta1
kind: RabbitmqCluster
metadata:
  ...
status:
  ...
spec:
  image: docker.m.daocloud.io/library/rabbitmq:3.9.25-management-alpine
  override:
    service:
      spec:
        ports:
          - name: amqp
            port: 5672
            protocol: TCP
            targetPort: 5672
          -name: management
            port: 15672
            protocol: TCP
            targetPort: 15672
          -name: prometheus
            port: 15692
            protocol: TCP
            targetPort: 15692
    statefulSet:
      spec:
        template:
          spec:
          # The following is the added part
+ volumes:
+ - name: community-plugins
+ emptyDir: { }
+ initContainers:
+ - command:
+ -sh
+ - -c
+ - curl -L -v https://github.com/rabbitmq/rabbitmq-message-timestamp/releases/download/v3.8.0/rabbitmq_message_timestamp-3.8.0.ez --output rabbitmq_message_timestamp-3.8.0.ez
+ image: docker.m.daocloud.io/curlimages/curl:7.70.0
+ imagePullPolicy: IfNotPresent
+ name: copy-community-plugins
+ resources:
+ limits:
+ cpu: 100m
+ memory: 500Mi
+ requests:
+ cpu: 100m
+ memory: 500Mi
+ terminationMessagePolicy: FallbackToLogsOnError
+ volumeMounts:
+ - mountPath: /community-plugins/
+ name: community-plugins
        # The above is the added part
            containers:
              - name: rabbitmq
                ports:
                  - containerPort: 5672
                    name: amqp
                    protocol: TCP
                  - containerPort: 15672
                    name: management
                    protocol: TCP
                  - containerPort: 15692
                    name: prometheus
                    protocol: TCP
                resources: {}
                # The following is the added part
+ volumeMounts:
+ - mountPath: /opt/rabbitmq/community-plugins
+ name: community-plugins
                # The above is the added part
  persistence:
    storage: 1Gi
    storageClassName: hwameistor-storage-lvm-hdd
  rabbitmq:
+ envConfig: |
+ PLUGINS_DIR=/opt/rabbitmq/plugins:/opt/rabbitmq/community-plugins
      # The above line adds part
    additionalConfig: |

      log.console.level = info
      default_user=rabbitmq
      default_pass=UE81O6Y4^w$iWP86g
      cluster_partition_handling = pause_minority
      vm_memory_high_watermark_paging_ratio = 0.99
      disk_free_limit.relative = 1.0
      collect_statistics_interval = 10000
    additionalPlugins:
+ - rabbitmq_message_timestamp # Increase the number of times the plugin is enabled
      - rabbitmq_peer_discovery_k8s
      - rabbitmq_prometheus
      - rabbitmq_management
  replicas: 1
  resources:
    limits:
      cpu: 200m
      memory: 512Mi
    requests:
      cpu: 200m
      memory: 512Mi
  secretBackend: {}
  service:
    type: ClusterIP
  terminationGracePeriodSeconds: 604800
  tls: {}
```

The plug-in here uses the official github as the download address, and it is generated and used. It is recommended to maintain the plug-in location by yourself to avoid download failure.

## Precautions

Currently, it is supported to manually edit custom resources in YAML to add corresponding plug-ins. There are certain operational risks, and it is recommended to operate with caution.