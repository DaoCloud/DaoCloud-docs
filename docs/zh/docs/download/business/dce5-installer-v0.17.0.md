---
date: 2024-05-09
hide:
  - navigation
---

# DCE 5.0 商业版 v0.17.0

本页可下载 DCE 5.0 商业版的离线安装包和校验文件。

[返回下载导览页](../index.md#_2){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名 | 版本 | 架构 | 文件大小 | 下载 | 更新日期 |
| ----- | --- | ---- | ------ | --- | -------- |
| offline-v0.17.0-amd64.tar | v0.17.0 | AMD 64 | 26.89 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar) | 2024-05-09 |
| offline-v0.17.0-arm64.tar | v0.17.0 | <font color="green">ARM 64</font> | 23.45 GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-arm64.tar) | 2024-05-09 |

## 校验

进入离线安装包下载目录。

=== "AMD 64"

    执行以下命令校验安装包：

    ```sh
    echo "7bbe92a32e740811c75e9159c73a7736bf52ad4cd737555fe147ccfe8907759ddfb8e8bf43780702c568beb6fe5c651a1f1fc0a59f48044d049de3ef521b8b41  offline-v0.17.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-v0.17.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令校验安装包：

    ```sh
    echo "0f78091b373ca817a8ea6e41e6f028d3538c87e93e70653ebb9b019bbb25619ddbd72853ada5a8f186639c4e970132bab2b75cb53f52762bdaed9f55cee0f848  offline-v0.17.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-v0.17.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD 64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-v0.17.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-v0.17.0-arm64.tar
    ```

- 安装请参阅[商业版安装流程](../../install/commercial/start-install.md)
- 成功安装之后请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898

## 模块

DCE 5.0 商业版包含以下模块，按需即插即用满足各类应用场景：

| 模块 | 介绍 | 最新动态 |
| ---- | --- | ------ |
| 全局管理 | 负责用户访问控制、权限、工作空间与层级、审计日志、个性化外观设置等 | [0.26.0](../../ghippo/intro/release-notes.md#v0260) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [0.27.0](../../kpanda/intro/release-notes.md#v0270) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息 | [0.26.0](../../insight/intro/release-notes.md#v0260) |
| 应用工作台 | 基于容器的 DevOps 应用平台，支持 Jenkins, Tekton, GitOps 等流水线作业 | [0.26.1](../../amamba/intro/release-notes.md#v0260) |
| 多云编排 | 集中管理多云、混合云、跨云资源的应用编排，具备多云灾备、故障恢复等能力 | [0.18.0](../../kairship/intro/release-notes.md#v0180) |
| 微服务引擎 | 提供注册发现、服务治理、配置管理、微服务网关等治理能力 | [0.36.1](../../skoala/intro/release-notes.md#v0361) |
| 服务网格 | 基于 Istio 开源技术构建的面向云原生应用的下一代服务网格 | [v0.25.0](../../mspider/intro/release-notes.md#v0250) |
| 中间件 Elasticsearch | 目前首选的全文搜索引擎 | [0.16.0](../../middleware/elasticsearch/release-notes.md#v0160) |
| 中间件 Kafka | 基于开源软件 Kafka 提供的分布式消息队列服务 | [0.14.0](../../middleware/kafka/release-notes.md#v0140) |
| 中间件 MinIO | 一款非常热门的轻量、开源对象存储方案 | [0.14.0](../../middleware/minio/release-notes.md#v0140) |
| 中间件 MySQL | 应用最广泛的开源关系数据库 | [0.17.1](../../middleware/mysql/release-notes.md#v0170) |
| 中间件 RabbitMQ | 实现了高级消息队列协议 (AMQP) 的开源消息代理软件 | [0.19.0](../../middleware/rabbitmq/release-notes.md#v0190) |
| 中间件 Redis | 一款内存数据库缓存服务 | [0.17.0](../../middleware/redis/release-notes.md#v0170) |
| 镜像仓库 | 用于存储 K8s、DevOps 和容器应用开发的镜像 | [0.17.0](../../kangaroo/intro/release-notes.md#v0170) |
| 网络 | 针对不同的 Linux 内核，支持多种 CNI 组合方案 | [0.13.0](../../network/intro/release-notes.md#v0130) |
| 存储 | 提供统一数据存储服务，支持文件、对象、块、本地存储，轻松接入存储厂商方案 | [v0.14.4](../../storage/hwameistor/release-notes.md#v0144) |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
