# 为 RabbitMQ 添加自定义插件

## 问题描述

RabbitMQ 有很多插件，但是在安装 RabbitMQ 时，只能安装默认的插件，如果需要安装其他插件，需要在安装完成后，手动安装。

## 解决方案

在创建的 RabbitMQ 的 yaml 中，增加 initContainer，用于下载插件，然后将插件挂在到 RabbitMQ 的插件目录中，最后在 rabbitmq 的 config 中，增加了插件的配置，并在启用的插件模块中启用插件。

## 示例

这里以 rabbitmq_message_timestamp-3.8.0.ez 为例，主要做的内容如下：

- 增加了 initContainer，用于下载插件
- 然后将插件挂在到 RabbitMQ 的插件目录中
- 在 rabbitmq 的 config 中，增加了插件的配置
- 并在启用的插件模块中启用插件

> 修改示例实例代码

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
          - name: management
            port: 15672
            protocol: TCP
            targetPort: 15672
          - name: prometheus
            port: 15692
            protocol: TCP
            targetPort: 15692
    statefulSet:
      spec:
        template:
          spec:
          # 以下为增加部分
+           volumes:
+             - name: community-plugins
+               emptyDir: { }
+           initContainers:
+             - command:
+                 - sh
+                 - -c
+                 - curl -L -v https://github.com/rabbitmq/rabbitmq-message-timestamp/releases/download/v3.8.0/rabbitmq_message_timestamp-3.8.0.ez --output rabbitmq_message_timestamp-3.8.0.ez
+               image: docker.m.daocloud.io/curlimages/curl:7.70.0
+               imagePullPolicy: IfNotPresent
+               name: copy-community-plugins
+               resources:
+                 limits:
+                   cpu: 100m
+                   memory: 500Mi
+                 requests:
+                   cpu: 100m
+                   memory: 500Mi
+               terminationMessagePolicy: FallbackToLogsOnError
+               volumeMounts:
+                 - mountPath: /community-plugins/
+                   name: community-plugins
        # 以上为增加部分
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
                # 以下为增加部分
+               volumeMounts:
+                 - mountPath: /opt/rabbitmq/community-plugins
+                   name: community-plugins
                # 以上为增加部分
  persistence:
    storage: 1Gi
    storageClassName: hwameistor-storage-lvm-hdd
  rabbitmq:
+   envConfig: |
+     PLUGINS_DIR=/opt/rabbitmq/plugins:/opt/rabbitmq/community-plugins
      # 以上一行为增加部分
    additionalConfig: |

      log.console.level = info
      default_user=rabbitmq
      default_pass=UE81O6Y4^w$iWP86g
      cluster_partition_handling = pause_minority
      vm_memory_high_watermark_paging_ratio = 0.99
      disk_free_limit.relative = 1.0
      collect_statistics_interval = 10000
    additionalPlugins:
+     - rabbitmq_message_timestamp  # 增加次插件启用
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

这里的插件采用 github 官方作为下载地址，生成使用，建议自行维护插件位置，以免下载失败。

## 注意事项

目前支持手工在 YAML 编辑自定义资源的方式增加对应的插件，存在一定的操作风险性，建议谨慎操作。
