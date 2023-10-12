---
date: 2023-01-03
hide:
  - navigation
---

# DCE 5.0 社区版 v0.3.30

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.3.30-amd64.tar | v0.3.30 | AMD64 | 5.73GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.30-amd64.tar) | 2023-01-03 |
| offline-community-v0.3.30-arm64.tar | v0.3.30 | ARM64 | 5.16GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.30-arm64.tar) | 2023-01-03 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "469c98d6a60c7055f3e4159ffcdb6f65bb44cade4345400ad1b4067f8c3c89ef057983accaf413f76dc71b9a5592e0ef97600fa731bd715acacbdab1c653601b  offline-community-v0.3.30-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.3.30-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "9d965d49d3b09231fadae7fe713da7284b408e36f6d24d2863678dc4edf239abedc68a47e5d020bf02688ad197803a908db379e481340e13c86735fa29fd8d14  offline-community-v0.3.30-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.3.30-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.3.30-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.3.30-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [v0.13](../../ghippo/intro/release-notes.md#v013) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [v0.14](../../kpanda/intro/release-notes.md#v014) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [v0.13](../../insight/intro/releasenote.md#v013)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
