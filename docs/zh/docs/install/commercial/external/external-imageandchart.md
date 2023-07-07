# 使用外接镜像仓库与 Chart 仓库存储镜像与 Chart 包

本文描述如何使用第三方镜像仓库及 Chart 仓库。

## 外接镜像仓库与 Chart 仓库 操作步骤

1. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `imagesAndCharts` 参数，如下：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      imagesAndCharts:
        type: external

        externalImageRepo: https://external-registry.daocloud.io
        externalImageRepoUsername: admin
        externalImageRepoPassword: Harbor12345

        # 支持 chartmuseum, harbor, jfrog
        externalChartRepoType: chartmuseum
        externalChartRepo: https://external-charts.daocloud.io:8081
        externalChartRepoPassword: rootpass123
      ..........
    ```

    !!! note

        - 镜像仓库基本支持社区中开源的所有镜像仓库类型

        - Chart 仓库仅支持 chartmuseum、harbor、jfrog 三种

2. 完成上述配置后，可以继续执行[部署 DCE 5.0 商业版](../start-install.md)。
