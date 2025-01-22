---
date: 2024-03-14
hide:
  - navigation
---

# DCE 5.0 社区版 v0.15.2

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载         | 更新日期  |
| -------------------------- | ------- | --- | ------- | ---------- | -------- |
| offline-community-v0.15.2-amd64.tar | v0.15.2 | AMD 64 | 7.50 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.15.2-amd64.tar) | 2024-03-14 |
| offline-community-v0.15.2-arm64.tar | v0.15.2 | <font color="green">ARM 64</font> | 7.05 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.15.2-arm64.tar) | 2024-03-14 |

## 校验

进入离线安装包下载目录。

=== "AMD 64"

    执行以下命令校验安装包：

    ```sh
    echo "e345aaaa30bf36dcab235f8d268ba68fed0e8b15a33b7ad8ac9b1655cb8cb3b381efb49d662df4dc90d70cfb8cb38a987941e09f4bf7c544f46f71279843ac94  offline-community-v0.15.2-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.15.2-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令校验安装包：

    ```sh
    echo "46e576cc7a001a3515f54467da2e7bcc7e22928160ae69f17cff48cedaa2e80daec7c07d3213dc89b1b4de2283f221951c7814bcbba1d0eaa0d810e7310f4893  offline-community-v0.15.2-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.15.2-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD 64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.15.2-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.15.2-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍            | 最新动态         |
| -------- | -------------- | -------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.24.0](../../ghippo/intro/release-notes.md#v0240) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.25.1](../../kpanda/intro/release-notes.md#v0250) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.24.0](../../insight/intro/release-notes.md#v0240)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
