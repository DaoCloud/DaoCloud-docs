# Using External Container Registry and Chart Repository to Store Images and Chart Packages

This document describes how to use third-party image repositories and chart repositories.

## Steps for External Container Registry and Chart Repository

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `imagesAndCharts` parameter as follows:

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

        # Supported options: chartmuseum, harbor, jfrog
        externalChartRepoType: chartmuseum
        externalChartRepo: https://external-charts.daocloud.io:8081
        externalChartRepoPassword: rootpass123
      ..........
    ```

    !!! note

        - The container registry supports all types of open-source repositories available in the community.

        - The chart repository only supports three types: chartmuseum, harbor, and jfrog.

2. After completing the above configuration, you can proceed with the [deployment of DCE 5.0 Enterprise](../start-install.md).
