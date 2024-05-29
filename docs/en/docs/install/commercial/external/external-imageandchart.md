---
MTPE: windsonsea
date: 2024-05-11
hide:
  - toc
---

# Use External Container Registry and Chart Repository

This document describes how to use third-party container registry and chart repositories.

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

        externalChartRepoType: chartmuseum # (1)!
        externalChartRepo: https://external-charts.daocloud.io:8081
        externalChartRepoPassword: rootpass123
      ..........
    ```

    1. Supported options: chartmuseum, harbor, jfrog

    !!! note

        - The container registry supports all types of open-source repositories available in the community.
        - The chart repository only supports three types: chartmuseum, harbor, and jfrog.

2. After completing the above configuration, you can proceed with the [deployment of DCE 5.0 Enterprise](../start-install.md).
