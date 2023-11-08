---
date: 2023-11-08
hide:
  - navigation
---

# DCE 5.0 社区版 v0.12.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载         | 更新日期   |
| -------------------------- | ------- | --- | ------- | ---------- | -------- |
| offline-community-v0.12.0-amd64.tar | v0.12.0 | AMD64 | 6.03 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.12.0-amd64.tar) | 2023-09-08 |
| offline-community-v0.12.0-arm64.tar | v0.12.0 | ARM64 | 5.65 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.12.0-arm64.tar) | 2023-09-08 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "54326e5b62cd7bb2711904adff5d2128e647dcd0993ae7109645889d3c923a8c590ae6d1623a85e846e9a0acf7f0149936c686a1544f7b933d4444b33916d876  offline-community-v0.12.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.12.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "25b7688637e57eea4488386a28f9357601ff53f497f439808a34a91e02ba2ceb8f7b92a74fd7184602efdb853e81472f8de7b53a04f9a93903f0131a4acac1be  offline-community-v0.12.0-arm64.tar" | sha512sum -c
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
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [0.21.0](../../ghippo/intro/release-notes.md#0210) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.22.0](../../kpanda/intro/release-notes.md#0220) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.21.1](../../insight/intro/releasenote.md#insight-server-v0210)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
