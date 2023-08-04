---
date: 2023-01-05
---

# DCE 5.0 社区版 v0.4.0-rc2

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-community-v0.4.0-rc2-amd64.tar | v0.4.0-rc2 | AMD64 | 5.73GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.4.0-rc2-amd64.tar) | 2023-01-05 |
| offline-community-v0.4.0-rc2-arm64.tar | v0.4.0-rc2 | ARM64 | 5.16GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.4.0-rc2-arm64.tar) | 2023-01-05 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "a9501539eb5e0241e4c3035e0870637d770b12e18971cb5dae1288682db4aa299fe42c964f556fa80d27e2ea6723b65a741f11f7a5f3696915c0a4f97015480e  offline-community-v0.4.0-rc2-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.4.0-rc2-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "7f79739afd14804172d876d8421b6768ce2d040f225b9d251bdd21118fa58ec9d82204a7a3f660d3673afc77b6be838d60f710a357b047bdbf8b65addd0e5977  offline-community-v0.4.0-rc2-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-community-v0.4.0-rc2-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.4.0-rc2-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-community-v0.4.0-rc2-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [v0.11](../../ghippo/intro/release-notes.md#v011) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [v0.12](../../kpanda/intro/release-notes.md#v012) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [v0.11](../../insight/intro/releasenote.md#v011)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
