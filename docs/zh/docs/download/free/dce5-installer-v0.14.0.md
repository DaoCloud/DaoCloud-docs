---
date: 2024-01-09
hide:
  - navigation
---

# DCE 5.0 社区版 v0.14.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载         | 更新日期  |
| -------------------------- | ------- | --- | ------- | ---------- | -------- |
| offline-community-v0.14.0-amd64.tar | v0.14.0 | AMD64 | 7.3 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.14.0-amd64.tar) | 2024-01-09 |
| offline-community-v0.14.0-arm64.tar | v0.14.0 | ARM64 | 6.9 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.14.0-arm64.tar) | 2024-01-09 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "e29a7441c5bba74a76b2ca22c698c86d8720d89b40eddab2d0eedcddad79ebfdc5c91cc0b743f714102a279f26985f14e3e1691bf91d78dd617c135dcf7204ff  offline-community-v0.14.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.14.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "e793ff6ee9f2ea69f4a4c7e7c1a75e303098f9125a89360a6ca9b355e53b419e5029f721a608aa4c83921eb047098c436288653f25b900cb8cc32989c965d466  offline-community-v0.14.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.14.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.14.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.14.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍            | 最新动态         |
| -------- | -------------- | -------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等 | [0.23.0](../../ghippo/intro/release-notes.md#v0230) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.24.1](../../kpanda/intro/release-notes.md#v0241) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息 | [0.23.0](../../insight/intro/releasenote.md#v0230) |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
