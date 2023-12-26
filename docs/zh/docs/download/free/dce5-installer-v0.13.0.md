---
date: 2023-12-07
hide:
  - navigation
---

# DCE 5.0 社区版 v0.13.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.13.0-amd64.tar | v0.13.0 | AMD64 | 6.96GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.13.0-amd64.tar) | 2023-12-07 |
| offline-community-v0.13.0-arm64.tar | v0.13.0 | ARM64 | 6.57GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.13.0-arm64.tar) | 2023-12-07 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "18e286418b6aa0da03280fd5e2745f1aa2cfc9c0e8b09a7c76f0a397e4eafb2c06f9f3344d19df2a85b739a961f8f1957d2d91c4a04239fd44dc15cb3d4a52ab  offline-community-v0.13.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.13.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "bde7028f83e58ff6a8211b0b5339ecb98b4014c0325b93d101c06cffc5766cd2ea59b9b8a148fab7007c88b861eb9e63278bb489d78ad0a097117efa1f39018f  offline-community-v0.13.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.13.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.13.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.13.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.22.1](../../ghippo/intro/release-notes.md#0221) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.23.0](../../kpanda/intro/release-notes.md#0230) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.22.0](../../insight/intro/releasenote.md#0220)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
