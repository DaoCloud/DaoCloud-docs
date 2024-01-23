---
date: 2023-11-08
hide:
  - navigation
---

# DCE 5.0 社区版 v0.12.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载         | 更新日期  |
| -------------------------- | ------- | --- | ------- | ---------- | -------- |
| offline-community-v0.12.0-amd64.tar | v0.12.0 | AMD64 | 6.03 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.12.0-amd64.tar) | 2023-09-08 |
| offline-community-v0.12.0-arm64.tar | v0.12.0 | ARM64 | 5.65 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.12.0-arm64.tar) | 2023-09-08 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "9e7298e2706ea70d08db71098843edf9fbf775835fc047bb4cbe01328ca49d7f40b7d8b7a01fbd48c0d9df3d21bc22393a55351238be59ac89eb4815816c4961  offline-community-v0.12.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.12.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "2fcf216c566b9e57b88bf8af9cfc5e18d86ec8a713b862a9973c38ac87ff054868a245d27e1da825528a26f7c46bc44b34b33391aa1dd36006d454c0b56c72a3  offline-community-v0.12.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.12.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.12.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.12.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍            | 最新动态         |
| -------- | -------------- | --------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.21.0](../../ghippo/intro/release-notes.md#v0210) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.22.0](../../kpanda/intro/release-notes.md#v0220) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.21.1](../../insight/intro/releasenote.md#insight-server-v0210)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
