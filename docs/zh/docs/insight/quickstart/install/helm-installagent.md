# 通过 Helm 部署 Insight Agent 

本文描述了在命令行中通过 Helm 命令安装 Insight Agent 社区版的操作步骤。

## 安装 Insight Agent

1. 使用以下命令添加镜像仓库的地址

    ```shell
    helm repo add insight https://release.daocloud.io/chartrepo/insight
    helm repo upgrade
    helm search repo  insight/insight-agent --versions
    ```

2. 安装 __Insight Agent__ 需要确保全局管理集群中的 __Insight Server__ 正常运行，执行以下安装命令安装 __Insight Agent__ 社区版，该配置不启用 Tracing 功能：

    ```shell
    helm upgrade --install --create-namespace --cleanup-on-fail \
        --version ${version} \      # 请指定部署版本
        insight-agent  insight/insight-agent \
        --set global.exporters.logging.elasticsearch.host=10.10.10.x \    # 请替换“10.10.10.x" 为全局管理集群或外置的 Elasticsearch 的地址
        --set global.exporters.logging.elasticsearch.port=32517 \     # 请替换“32517" 为全局管理集群或外置的 Elasticsearch 暴露的端口
        --set global.exporters.logging.elasticsearch.user=elastic \     # 请替换“elastic" 为全局管理集群或外置的 Elasticsearch 的用户名
        --set global.exporters.logging.elasticsearch.password=dangerous \  # 请替换“dangerous" 为全局管理集群或外置的 Elasticsearch 的密码
        --set global.exporters.metric.host=${vminsert_address} \    # 请替换“10.10.10.x" 为全局管理集群中 vminsert 的地址
        --set global.exporters.metric.port=${vminsert_port} \    # 请替换“32517" 为全局管理集群中 vminsert 的地址
        --set global.exporters.auditLog.host=${opentelemetry-collector address} \     # 请替换“32517" 为全局管理集群中 opentelemetry-collector 的端口
        --set global.exporters.auditLog.port=${otel_col_auditlog_port}\   # 请替换“32517" 为全局管理集群中 opentelemetry-collector 容器端口为 8006 的 service 对外访问的地址
        -n insight-system
    ```

    !!! info

        可参考 __如何获取连接地址__ 获取地址信息。

3. 执行以下命令确认安装状态：

    ```shell
    helm list -A
    kubectl get pods -n insight-system
    ```

### 如何获取连接地址

#### 在全局管理集群安装 Insight Agent

如果 Agent 是安装在管理集群，推荐通过域名来访问集群：

```shell
export vminsert_host="vminsert-insight-victoria-metrics-k8s-stack.insight-system.svc.cluster.local" # 指标
export es_host="insight-es-master.insight-system.svc.cluster.local" # 日志
export otel_col_host="insight-opentelemetry-collector.insight-system.svc.cluster.local" # 链路
```

#### 在工作集群安装 Insight Agent

=== "全局管理集群使用默认的 LoadBalancer"

    全局管理集群使用默认的 LoadBalancer 方式暴露服务时，登录全局管理集群的控制台，执行以下命令：

    ```shell
    export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
    curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam'
    ```

    将获得如下的返回值：

    ```shell
    {"global":{"exporters":{"logging":{"output":"elasticsearch","elasticsearch":{"host":"10.6.182.32"},"kafka":{},"host":"10.6.182.32"},"metric":{"host":"10.6.182.32"},"auditLog":    {"host":"10.6.182.32"}}},"opentelemetry-operator":{"enabled":true},"opentelemetry-collector":{"enabled":true}}
    ```

    其中：

    - __global.exporters.logging.elasticsearch.host__ 是日志服务地址【不需要再设置对应服务的端口，都会使用相应默认值】；
    - __global.exporters.metric.host__ 是指标服务地址；
    - __global.exporters.trace.host__ 是链路服务地址；
    - __global.exporters.auditLog.host__ 是审计日志服务地址 (和链路使用的同一个服务不同端口)；

=== "登录全局管理集群的控制台操作"

    登录全局管理集群的控制台，执行以下命令：

    ```shell
    kubectl get service -n insight-system | grep lb
    kubectl get service -n mcamel-system | grep es
    ```

    其中：

    - __lb-vminsert-insight-victoria-metrics-k8s-stack__ 是指标服务的地址；
    - __lb-insight-opentelemetry-collector__ 是链路服务的地址;
    - __mcamel-common-es-cluster-masters-es-http__ 是日志服务的地址;

=== "全局管理集群使用 Nodeport"

    全局管理集群使用 Nodeport 方式暴露服务时，登录全局管理集群的控制台，执行以下命令：

    ```shell
    kubectl get service -n insight-system
    kubectl get service -n mcamel-system
    ```

    其中：

    - __vminsert-insight-victoria-metrics-k8s-stack__ 是指标服务的地址；
    - __insight-opentelemetry-collector__ 是链路服务的地址;
    - __mcamel-common-es-cluster-masters-es-http__ 是日志服务的地址;

## 升级 Insight Agent

1. 登录目标集群的控制台，执行以下命令备份 `--set` 参数。

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent.yaml
    ```

2. 执行以下命令更新仓库。

    ```shell
    helm repo upgrade
    ```

3. 执行以下命令进行升级。

    ```shell
    helm upgrade insight-agent insight/insight-agent \
    -n insight-system \
    -f ./insight-agent.yaml \
    --version ${version}   # 指定升级版本
    ```

4. 执行以下命令确认安装状态：

    ```shell
    kubectl get pods -n insight-system
    ```

## 卸载 Insight Agent

```shell
helm uninstall insight-agent -n insight-system --timeout 10m
```
