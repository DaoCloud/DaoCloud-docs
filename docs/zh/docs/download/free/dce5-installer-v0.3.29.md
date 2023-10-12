---
date: 2022-11-21
hide:
  - navigation
---

# DCE 5.0 社区版 v0.3.29

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

[返回下载导览页](../index.md){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-centos7-community-v0.3.29-amd64.tar | v0.3.29 | AMD64 | 9.2 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-community-v0.3.29-amd64.tar) | 2022-12-16 |
| offline-kylin-v10sp2-community-v0.3.29-arm64.tar | v0.3.29 | ARM64 | 6.9 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-community-v0.3.29-arm64.tar) | 2022-12-16 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "988bf4397f555804fb004a83e01169fd4cfb995d0659170197cab4d07c26aefb6c916ce42c0655d207a2ae7bddd5c28c6c66fc7645c67a174a8919e7e040cbd8  offline-centos7-community-v0.3.29-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-centos7-community-v0.3.29-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "86dcb1f8b155d37a19a1b6c81a74a3758f443a79a8ffd95b9f5a634d992932714d8bce9805ab52d9fffbfdcbc82873e7c7132a7d3e9a45d5fe00f46de16ab717  offline-kylin-v10sp2-community-v0.3.29-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-kylin-v10sp2-community-v0.3.29-arm64.tar: OK
    ```
  
## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-centos7-community-v0.3.29-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-kylin-v10sp2-community-v0.3.29-arm64.tar
    ```

- 安装请参阅[社区版安装流程](../../install/community/k8s/online.md#_2)
- 成功安装之后请[申请免费社区体验](../../dce/license0.md)

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [v0.12](../../ghippo/intro/release-notes.md#v012) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [v0.13](../../kpanda/intro/release-notes.md#v013) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [v0.12](../../insight/intro/releasenote.md#v012)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
