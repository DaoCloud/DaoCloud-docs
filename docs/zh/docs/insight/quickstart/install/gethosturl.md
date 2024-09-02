# 获取全局服务集群的数据存储地址

可观测性是多集群统一观测的产品，为实现对多集群观测数据的统一存储、查询，
子集群需要将采集的观测数据上报给[全局服务集群](../../../kpanda/user-guide/clusters/cluster-role.md#_2)进行统一存储。
本文提供了在安装采集组件 insight-agent 时必填的存储组件的地址。

## 在全局服务集群安装 insight-agent

如果在全局服务集群安装 insight-agent，推荐通过域名来访问集群：

```shell
export vminsert_host="vminsert-insight-victoria-metrics-k8s-stack.insight-system.svc.cluster.local" # (1)!
export es_host="insight-es-master.insight-system.svc.cluster.local" # (2)!
export otel_col_host="insight-opentelemetry-collector.insight-system.svc.cluster.local" # (3)!
```

## 在其他集群安装 insight-agent

### 通过 Insight Server 提供的接口获取地址

1. [管理集群](../../../kpanda/user-guide/clusters/cluster-role.md#_3)使用默认的 LoadBalancer 方式暴露

    登录全局服务集群的控制台，执行以下命令：

    ```bash
    export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
    curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam'
    ```

    !!! note

        请替换命令中的 `${INSIGHT_SERVER_IP}` 参数。

    获得如下返回值：

    ```json
    {
      "values": {
        "global": {
          "exporters": {
            "logging": {
              "host": "10.6.182.32"
            },
            "metric": {
              "host": "10.6.182.32"
            },
            "auditLog": {
              "host": "10.6.182.32"
            },
            "trace": {
              "host": "10.6.182.32"
            }
          }
        },
        "opentelemetry-operator": {
          "enabled": true
        },
        "opentelemetry-collector": {
          "enabled": true
        }
      }
    }
    ```

    - `global.exporters.logging.host` 是日志服务地址，不需要再设置对应服务的端口，都会使用相应默认值
    - `global.exporters.metric.host` 是指标服务地址
    - `global.exporters.trace.host` 是链路服务地址
    - `global.exporters.auditLog.host` 是审计日志服务地址（和链路使用的同一个服务不同端口）

1. 管理集群禁用 LoadBalancer

    调用接口时需要额外传递集群中任意外部可访问的节点 IP，会使用该 IP 拼接出对应服务的完整访问地址。

    ```bash
    export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
    curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam' --data '{"extra": {"EXPORTER_EXTERNAL_IP": "10.5.14.51"}}'
    ```

    将获得如下的返回值：

    ```json
    {
      "values": {
        "global": {
          "exporters": {
            "logging": {
              "scheme": "https",
              "host": "10.5.14.51",
              "port": 32007,
              "user": "elastic",
              "password": "j8V1oVoM1184HvQ1F3C8Pom2"
            },
            "metric": {
              "host": "10.5.14.51",
              "port": 30683
            },
            "auditLog": {
              "host": "10.5.14.51",
              "port": 30884
            },
            "trace": {
              "host": "10.5.14.51",
              "port": 30274
            }
          }
        },
        "opentelemetry-operator": {
          "enabled": true
        },
        "opentelemetry-collector": {
          "enabled": true
        }
      }
    }
    ```

    - `global.exporters.logging.host` 是日志服务地址
    - `global.exporters.logging.port` 是日志服务暴露的 NodePort
    - `global.exporters.metric.host` 是指标服务地址
    - `global.exporters.metric.port` 是指标服务暴露的 NodePort
    - `global.exporters.trace.host` 是链路服务地址
    - `global.exporters.trace.port` 是链路服务暴露的 NodePort
    - `global.exporters.auditLog.host` 是审计日志服务地址（和链路使用的同一个服务不同端口）
    - `global.exporters.auditLog.host` 是审计日志服务暴露的 NodePort

### 通过 LoadBalancer 连接

1. 若集群中开启 `LoadBalancer` 且为 Insight 设置了 `VIP` 时，您也可以手动执行以下命令获取 `vminsert` 以及 `opentelemetry-collector` 的地址信息：

    ```shell
    $ kubectl get service -n insight-system | grep lb
    lb-insight-opentelemetry-collector               LoadBalancer   10.233.23.12    <pending>     4317:31286/TCP,8006:31351/TCP  24d
    lb-vminsert-insight-victoria-metrics-k8s-stack   LoadBalancer   10.233.63.67    <pending>     8480:31629/TCP                 24d
    ```
    
    - `lb-vminsert-insight-victoria-metrics-k8s-stack` 是指标服务的地址
    - `lb-insight-opentelemetry-collector` 是链路服务的地址

1. 执行以下命令获取 ` elasticsearch` 地址信息：

    ```shell
    $ kubectl get service -n mcamel-system | grep es
    mcamel-common-es-cluster-masters-es-http               NodePort    10.233.16.120   <none>        9200:30465/TCP               47d
    ```

    `mcamel-common-es-cluster-masters-es-http` 是日志服务的地址

### 通过 NodePort 连接

全局服务集群禁用 LB 特性

在该情况下，默认不会创建上述的 LoadBalancer 资源，对应服务名为：

- vminsert-insight-victoria-metrics-k8s-stack（指标服务）
- common-es（日志服务）
- insight-opentelemetry-collector（链路服务）

上面两种情况获取到对应服务的对应端口信息后，进行如下设置：

```shell
--set global.exporters.logging.host=  # (1)!
--set global.exporters.logging.port=  # (2)!
--set global.exporters.metric.host=   # (3)!
--set global.exporters.metric.port=   # (4)!
--set global.exporters.trace.host=    # (5)!
--set global.exporters.trace.port=    # (6)!
--set global.exporters.auditLog.host= # (7)!
```

1. 外部可访问的管理集群 NodeIP
2. 日志服务 9200 端口对应的 NodePort
3. 外部可访问的管理集群 NodeIP
4. 指标服务 8480 端口对应的 NodePort
5. 外部可访问的管理集群 NodeIP
6. 链路服务 4317 端口对应的 NodePort
7. 外部可访问的管理集群 NodeIP
