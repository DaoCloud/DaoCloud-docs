---
date: 2023-05-09
---

# DCE 5.0 社区版 v0.7.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.7.0-amd64.tar | v0.7.0 | AMD64 | 5.96GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.7.0-amd64.tar) | 2023-05-09 |
| offline-community-v0.7.0-arm64.tar | v0.7.0 | ARM64 | 5.60GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.7.0-arm64.tar) | 2023-05-09 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "e80596e138a932d0d28101440ae22fbb319f048ad92043507e0202696ebc4a39717e65cbc12b6a6c02f5c9eb8c9fe7d027f381f037b6ae5dc1c21af00106e2b7  offline-community-v0.7.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.7.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "3f68086d55ba413473eb3abae5756779ef22bc264950d0a3ef21714977463e3ac7fa01a574a0488f3a547fc6a2c9d0b979e1e3a02c9632b222f879c5e0a32b78  offline-community-v0.7.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.7.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.7.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.7.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [0.16.1](../../ghippo/intro/release-notes.md#0161) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.17.0](../../kpanda/intro/release-notes.md#0170) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.16.1](../../insight/intro/releasenote.md#0161)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
