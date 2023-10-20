---
date: 2023-06-06
hide:
  - navigation
---

# DCE 5.0 商业版 v0.8.0

本页可下载 DCE 5.0 商业版的离线安装包和校验文件。

[返回下载导览页](../index.md#_2){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-v0.8.0-amd64.tar | v0.8.0 | AMD64 | 18.43GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-amd64.tar) | 2023-06-06 |
| offline-v0.8.0-arm64.tar | v0.8.0 | ARM64 | 16.99GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-arm64.tar) | 2023-06-06 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "fbd3e646f5849406db1c221ab6956afd0e3dfd76e75394dfaeec06d2f2ec74934801cd7118c4bf2f51a3610dcb69fd7a010c613fcda3339abd20a1630029723e  offline-v0.8.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-v0.8.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "f2854f0a90c2db16b9c206708b140069a953b68a575ce59b1dc656f84cb47c42647697067582e28e16175f4bfbcfcdb6c14d79c3d999c7646f1c58c40f1b35cc  offline-v0.8.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-v0.8.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-v0.8.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-v0.8.0-arm64.tar
    ```

- 安装请参阅[商业版安装流程](../../install/commercial/start-install.md)
- 成功安装之后请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898

## 模块

DCE 5.0 商业版包含以下模块，按需即插即用满足各类应用场景：

| 模块                 | 介绍                                                                     | 最新动态                                                      |
| -------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 全局管理             | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等             | [0.17.1](../../ghippo/intro/release-notes.md#0171)    |
| 容器管理             | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能        | [0.18.1](../../kpanda/intro/release-notes.md#0181)    |
| 可观测性             | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息                     | [0.17.2](../../insight/intro/releasenote.md#0172)     |
| 应用工作台           | 基于容器的 DevOps 应用平台，支持 Jenkins, Tekton, GitOps 等流水线作业    | [0.17.3](../../amamba/intro/release-notes.md#0173)      |
| 多云编排             | 集中管理多云、混合云、跨云资源的应用编排，具备多云灾备、故障恢复等能力   | [0.9.1](../../kairship/intro/release-notes.md#091)         |
| 微服务引擎           | 提供注册发现、服务治理、配置管理、微服务网关等治理能力                   | [0.22.2](../../skoala/intro/release-notes.md#0222)             |
| 服务网格             | 基于 Istio 开源技术构建的面向云原生应用的下一代服务网格                  | [v0.16.2](../../mspider/intro/release-notes.md#v0162)          |
| 中间件 Elasticsearch | 目前首选的全文搜索引擎                                                   | [0.8.0](../../middleware/elasticsearch/release-notes.md#080) |
| 中间件 Kafka         | 基于开源软件 Kafka 提供的分布式消息队列服务                              | [0.6.0](../../middleware/kafka/release-notes.md#060)          |
| 中间件 MinIO         | 一款非常热门的轻量、开源对象存储方案                                     | [0.6.0](../../middleware/minio/release-notes.md#060)          |
| 中间件 MySQL         | 应用最广泛的开源关系数据库                                               | [0.9.0](../../middleware/mysql/release-notes.md#090)           |
| 中间件 RabbitMQ      | 实现了高级消息队列协议 (AMQP) 的开源消息代理软件                         | [0.11.0](../../middleware/rabbitmq/release-notes.md#0110)        |
| 中间件 Redis         | 一款内存数据库缓存服务                                                   | [0.8.0](../../middleware/redis/release-notes.md#080)           |
| 镜像仓库             | 用于存储 K8s、DevOps 和容器应用开发的镜像                                | [0.8.1](../../dce/dce-rn/20230630.md)                            |
| 网络                 | 针对不同的 Linux 内核，支持多种 CNI 组合方案                             | [0.7.0](../../dce/dce-rn/20230630.md)                            |
| 存储                 | 提供统一数据存储服务，支持文件、对象、块、本地存储，轻松接入存储厂商方案 | [v0.10.2](../../dce/dce-rn/20230630.md)                            |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
