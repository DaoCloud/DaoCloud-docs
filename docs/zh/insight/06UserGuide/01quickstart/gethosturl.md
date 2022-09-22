# 获取 host 地址

本页说明如何分别在`全局服务集群`和`管理集群`安装 insight-agent。

## 在`全局服务集群`安装 insight-agent

在 `全局管理集群` 安装时，推荐通过域名来访问集群：

```yaml
export vminsert_host="vminsert-insight-victoria-metrics-k8s-stack.insight-system.svc.cluster.local" // 指标
export es_host="insight-es-master.insight-system.svc.cluster.local" // 日志
export otel_col_host="insight-opentelemetry-collector.insight-system.svc.cluster.local" // 链路
```

## 在`管理集群`安装 insight-agent

可以通过以下几种方式来安装 insight-agent。

### 通过接口获取

参照以下步骤通过接口获取 insight-agent。

1. 登录`全局管理集群`访问后台，执行以下命令获取 `host` 地址：

    ```bash
    export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
    curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam'
    ```

2. 执行完以上命令后，获得如下返回值：

    ```
    `{"values":"{\"global\":{\"exporters\":{\"logging\":{\"host\":\"10.6.182.32\"},\"metric\":{\"host\":\"10.6.182.32\"},\"auditLog\":{\"host\":\"10.6.182.32\"},\"trace\":{\"host\":\"10.6.182.32\"}}},\"opentelemetry-operator\":{\"enabled\":true},\"opentelemetry-collector\":{\"enabled\":true}}"}`
    ```

### 通过 LoadBalancer 连接

请确认您的集群已安装负载均衡器。参照以下步骤通过 LoadBalancer 连接 insight-agent：

1. 在命令行中执行以下命令：

    ```
    kubectl get service -n insight-system | grep lb
    ```

2. 执行完获得相应服务的地址信息：

    - `lb-insight-es-master` 是日志服务的地址
    - `lb-vminsert-insight-victoria-metrics-k8s-stack` 是指标服务的地址
    - `lb-insight-opentelemetry-collector` 是链路服务的地址

### 通过 NodePort 连接

通过 NodePort 连接 insight-agent 的具体步骤如下：

1. 在命令行工具中执行一下命令：

    ```
    kubectl get service -n insight-system
    ```

2. 执行完获得相应服务的地址信息：

    - `global.exporters.logging.port` 是日志服务 9200 端口对应的 NodePort
    - `global.exporters.metric.port` 是指标服务 8480 端口对应的 NodePort
    - `global.exporters.trace.port` 是链路服务 4317 端口对应的 NodePort
    - `global.exporters.auditLog.port` 是链路服务 8006 端口对应的 NodePort
