---
date: 2023-08-24
---

# DCE 5.0 社区版 v0.10.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.10.0-amd64.tar | v0.10.0 | AMD64 | 6.16GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.10.0-amd64.tar) | 2023-08-24 |
| offline-community-v0.10.0-arm64.tar | v0.10.0 | ARM64 | 5.79GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.10.0-arm64.tar) | 2023-08-24 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "882b5b6e3e9395a64589c9d94af4a0e86a5bb7af7898262451da333ee10cfacbd503a2640cd83078a517b254519a4e4b6fc66fe9ace4c1599e7078b22e5ddbd9  offline-community-v0.10.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.10.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "8ffa2a37c9bc9fcf170878ac5a4e1f7eb32bcf825d43893888fd03a555fae3db5351ce5cda9ebaae33156b47a09fadaa2fead25b166eafa588b9cda979666a38  offline-community-v0.10.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.10.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.10.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.10.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [0.19.2](../../ghippo/intro/release-notes.md#0192) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.20.1](../../kpanda/intro/release-notes.md#0201) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.19.2](../../insight/intro/releasenote.md#0192)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
