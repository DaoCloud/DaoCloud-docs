---
date: 2024-05-09
hide:
  - navigation
---

# DCE 5.0 社区版 v0.17.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载         | 更新日期  |
| -------------------------- | ------- | --- | ------- | ---------- | -------- |
| offline-community-v0.17.0-amd64.tar | v0.17.0 | AMD 64 | 7.61 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.17.0-amd64.tar) | 2024-05-09 |
| offline-community-v0.17.0-arm64.tar | v0.17.0 | <font color="green">ARM 64</font> | 7.21 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.17.0-arm64.tar) | 2024-05-09 |

## 校验

进入离线安装包下载目录。

=== "AMD 64"

    执行以下命令校验安装包：

    ```sh
    echo "2c88ae3bad973140cccf5019f0bcee87e12795d644bd101111d1436080ce95d5281d33fcf28df50da0718b28fb42ee82f3ea8dea2ddcdc723e6258e26411396f  offline-community-v0.17.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.17.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令校验安装包：

    ```sh
    echo "b3f6d61fa072de06b7daa142238d2a02716c28588e63ebe632a45b4933a4e481f4049318b7facf0c6c235d3810ed8628b33f59543d2579e5df3d8e9d0aefffa3  offline-community-v0.17.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.17.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD 64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.17.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.17.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍            | 最新动态         |
| -------- | -------------- | -------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.26.0](../../ghippo/intro/release-notes.md#0260) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.27.0](../../kpanda/intro/release-notes.md#0270) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.26.0](../../insight/intro/releasenote.md#0260)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
