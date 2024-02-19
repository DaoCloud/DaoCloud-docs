---
date: 2024-02-04
hide:
  - navigation
---

# DCE 5.0 社区版 v0.15.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载         | 更新日期  |
| -------------------------- | ------- | --- | ------- | ---------- | -------- |
| offline-community-v0.15.0-amd64.tar | v0.15.0 | AMD64 | 7.44 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.15.0-amd64.tar) | 2024-02-04 |
| offline-community-v0.15.0-arm64.tar | v0.15.0 | ARM64 | 7.05 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.15.0-arm64.tar) | 2024-02-04 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "b9e9f58e9ee76c85dc87e83d6efc5470120ee5732d89f66da44fd243170b73c3d473dc57f8426fabe157612d1228351e7a9c4f47e71c66c35e4525728e2630a8  offline-community-v0.15.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.15.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "291fbee4cc0415463bbf87c5674a428e3f5d14c43309c6dfafdca5ad2b7f69cb0be087010bd5a7a63e4c04f05d16259fd0e5251b11f0f939d892064a6d952ad8  offline-community-v0.15.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.15.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.15.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.15.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍            | 最新动态         |
| -------- | -------------- | -------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.24.0](../../ghippo/intro/release-notes.md#0240) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.25.1](../../kpanda/intro/release-notes.md#0251) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.24.0](../../insight/intro/releasenote.md#0240)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
