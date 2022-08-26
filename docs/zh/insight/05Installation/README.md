# 安装部署流程

## 安装 Elasticsearch

- 添加&更新 Elasticsearch repo

    ```shell
    helm repo add middleware-release https://release.daocloud.io/chartrepo/middleware
    helm repo update
    ```

- 安装Elasticsearch

    ```plaintext
    1. 获取 Elasticsearch version 地址：
        https://release.daocloud.io/harbor/projects/13/helm-charts/elasticsearch/versions
    2. ${ESClusterName} 和 ${InstallESClusterName} 为 Elasticsearch 集群名称
    helm upgrade --install ${InstallESClusterName} --create-namespace -n middleware-system --cleanup-on-fail \
    --set elasticsearch.enabled=true \
    --set elasticsearch.clusterName=${ESClusterName} \
    middleware-release/elasticsearch --version ${version}
    ```

## 安装 Insight

> 注：需要预先安装好 Elasticsearch。

- 添加&更新 Insight repo

    ```shell
    helm repo add insight-release https://release.daocloud.io/chartrepo/insight
    helm repo update
    ```

- 部署 Insight 控制器

    > version 获取地址：https://release.daocloud.io/harbor/projects/7/helm-charts/insight/versions 

    > 因 harbor 未按照创建时间排序，请手动挑选最新版本。

    ```shell
    helm upgrade --install --create-namespace --version v${version} --cleanup-on-fail insight insight-release/insight -n insight-system --set image.repository=release.daocloud.io/insight/insight --set image.tag=v${version} --set server.datasource.elasticsearch.url=http://insight-es-master.middleware-system.svc.cluster.local:9200 --set server.datasource.elasticsearch.searchIndexAlias=insight-es-k8s-logs
    ```

- 卸载 Insight 控制器

    ```shell
    helm uninstall insight -n insight-system
    ```

## 部署 Insight Agent

- 安装 Insight Agent 需要确保 Insight 已经准备就绪。
- 安装 Insight Agent:

    > 使用和安装 Insight 组件的同一版本号。

    ```shell
    helm upgrade
        --install --create-namespace --cleanup-on-fail \
        --version v${version} \
        insight-agent insight-release/insight-agent \
        --set global.exporters.log=日志服务的地址 \
        --set global.exporters.metric=指标服务的地址 \
        --set global.exporters.trace=链路追踪服务的地址 \
        -n insight-system
    ```

在 Global 集群安装 Insight Agent 时，可以不设置 `global.exporters.log`, `global.exporters.metric`, `global.exporters.trace`，使用默认的参数。

- 卸载 Insight Agent

    ```shell
    helm uninstall insight-agent -n <insight-system>
    ```