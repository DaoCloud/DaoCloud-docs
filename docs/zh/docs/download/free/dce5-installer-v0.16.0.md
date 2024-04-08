---
date: 2024-04-08
hide:
  - navigation
---

# DCE 5.0 社区版 v0.16.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.16.0-amd64.tar | v0.16.0 | AMD 64 | 7.86GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.0-amd64.tar) | 2024-04-08 |
| offline-community-v0.16.0-arm64.tar | v0.16.0 | <font color="green">ARM 64</font> | 7.45GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.0-arm64.tar) | 2024-04-08 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "3d26f2068f0341fe3e3418158b9d9a5244eb1c0cc443909592903040a8929736a1944ff5ae196404fa6362e60515014d50dc6128ef65714597ff1b1cca42620b  offline-community-v0.16.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.16.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "a01cc80ae0405e858cfa56b2ffd7a8dd8267744edc2ab31c60e8e3ba46de5afe87880d909d2157f47c2ba062380faab965d761cc7216b9031dd3e33dea7de4eb  offline-community-v0.16.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.16.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.16.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.16.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.25.1](../../ghippo/intro/release-notes.md#0251) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.26.1](../../kpanda/intro/release-notes.md#0261) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.25.3](../../insight/intro/releasenote.md#0253)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
