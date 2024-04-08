---
date: 2023-04-12
hide:
  - navigation
---

# DCE 5.0 社区版 v0.6.1

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.6.1-amd64.tar | v0.6.1 | AMD 64 | 5.89 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.1-amd64.tar) | 2023-04-12 |
| offline-community-v0.6.1-arm64.tar | v0.6.1 | <font color="green">ARM 64</font> | 5.52 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.1-arm64.tar) | 2023-04-12 |

## 校验

进入离线安装包下载目录。

=== "AMD 64"

    执行以下命令校验安装包：

    ```sh
    echo "f452f0b5757220b7630334916209275207c7f4672da80bb2de721d186f57bfc5744155a514a88f0271ec9a02f90f831baa4bcb32fd3b169d0255773916f10c32  offline-community-v0.6.1-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.6.1-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令校验安装包：

    ```sh
    echo "2036e4b4a0d0fa9016b6bc0ceb28b2f6dd7ec9f856f2ef976dacdedd8d9e0500dbf47c7f070d70954fc9a3fd6adf060e550cf52a2343443531c85493e308de9f  offline-community-v0.6.1-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.6.1-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD 64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.6.1-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.6.1-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.15.0](../../ghippo/intro/release-notes.md#v0150) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.16.1](../../kpanda/intro/release-notes.md#v0161) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.15.4](../../insight/intro/releasenote.md#v0154)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
