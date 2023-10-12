---
date: 2023-04-07
---

# DCE 5.0 社区版 v0.6.0

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.6.0-amd64.tar | v0.6.0 | AMD64 | 5.89GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.0-amd64.tar) | 2023-04-07 |
| offline-community-v0.6.0-arm64.tar | v0.6.0 | ARM64 | 5.52GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.0-arm64.tar) | 2023-04-07 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "2419aaef4d003f51d35aed7f35fc4b311ac728330ad91e52aa4adcbeb5c60b3106ffa8f94f7669d32e868e80d87ae3b1f2eef55c3d69211199f9cdfb677cc809  offline-community-v0.6.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.6.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "494fb0c10f4ad693519f3153ef97a3072fecd348eb56ec28582eab59ef78f3a98c14479abdb6e2064c204924f8bc60ee0b717644b96bee7f2f132b7f53ade86c  offline-community-v0.6.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.6.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.6.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.6.0-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [0.15.0](../../ghippo/intro/release-notes.md#v0150) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.16.0](../../kpanda/intro/release-notes.md#v0160) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [0.15.4](../../insight/intro/releasenote.md#v0154)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
