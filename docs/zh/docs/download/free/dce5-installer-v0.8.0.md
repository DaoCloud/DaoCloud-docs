---
date: 2023-06-06
---

# DCE 5.0 社区版 v0.8.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.8.0-amd64.tar | v0.8.0 | AMD64 | 6.01GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.8.0-amd64.tar) | 2023-06-06 |
| offline-community-v0.8.0-arm64.tar | v0.8.0 | ARM64 | 5.64GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.8.0-arm64.tar) | 2023-06-06 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "886f1e1622115e3d2bfa6e41e26ba3c02419177ee7cae422000b28f6e9cd9b2b370a8a737be90328ee1b048c02811b4b31443638960b3cd24acf9ce0b9848320  offline-community-v0.8.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.8.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "73ccc2305196caa7c8152369016b5bc2fa38f874028f94961482ec5610158c7e7e8b4c3f7a335e473a28953e5ffeff27bb6ee7d132b3b1ae8e49ddd711993c21  offline-community-v0.8.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.8.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.8.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.8.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [0.17.1](../../ghippo/intro/release-notes.md#0171) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.18.1](../../kpanda/intro/release-notes.md#0181) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.17.2](../../insight/intro/releasenote.md#0172)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
