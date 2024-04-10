---
date: 2024-04-09
hide:
  - navigation
---

# DCE 5.0 社区版 v0.16.1

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载         | 更新日期  |
| -------------------------- | ------- | --- | ------- | ---------- | -------- |
| offline-community-v0.16.1-amd64.tar | v0.16.1 | AMD 64 | 7.86GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.1-amd64.tar) | 2024-04-09 |
| offline-community-v0.16.1-arm64.tar | v0.16.1 | <font color="green">ARM 64</font> | 7.45GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.1-arm64.tar) | 2024-04-09 |

## 校验

进入离线安装包下载目录。

=== "AMD 64"

    执行以下命令校验安装包：

    ```sh
    echo "e21ba57969b765b0d34645150af38b4870939edd49e49426842703bb34b6459526ba9e472242a0604a8d882f5c341cd5a725268ced9c9941f8aaad7d187dfe8c  offline-community-v0.16.1-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.16.1-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令校验安装包：

    ```sh
    echo "46a1252dd68194699ce27ac821f939c57eccc9ff8979be30b8b65554b4a1ac169960e6493bfebf5f523d059622d7ce4a5388763295383cc7fde36113ee76b87b  offline-community-v0.16.1-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.16.1-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD 64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.16.1-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.16.1-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍            | 最新动态         |
| -------- | -------------- | -------------- |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等      | [0.25.1](../../ghippo/intro/release-notes.md#0251) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.26.1](../../kpanda/intro/release-notes.md#0261) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.25.3](../../insight/intro/releasenote.md#0253)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
