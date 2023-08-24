---
date: 2023-08-24
---

# DCE 5.0 商业版 v0.10.0

本页可下载 DCE 5.0 商业版的离线安装包和校验文件。

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-v0.10.0-amd64.tar | v0.10.0 | AMD64 | 20.97GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-amd64.tar) | 2023-08-24 |
| offline-v0.10.0-arm64.tar | v0.10.0 | ARM64 | 17.32GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-arm64.tar) | 2023-08-24 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "048a8d2e9c50a3f2b1c101736e512ff728056fb941a3411d5ad8f27d14988e79776ac13216ccfcb2997e862f39d8bef4e12ec7a9d7953f2f10a99784a7b64dec  offline-v0.10.0-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-v0.10.0-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "e02b9160349dcda8cad6be20d5840aff7e40d8573bd9b3e642bac61981cdcc2d0919834e8eda33cb29f01a06620f60e7daa9073d45098ea9ef202e93762092d9  offline-v0.10.0-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-v0.10.0-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-v0.10.0-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-v0.10.0-arm64.tar
    ```

- 安装请参阅[商业版安装流程](../../install/commercial/start-install.md)
- 成功安装之后请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898

## 模块

DCE 5.0 商业版包含以下模块，按需即插即用满足各类应用场景：

| 模块                 | 介绍                                                                     | 最新动态                                                      |
| -------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 全局管理             | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等             | [0.19.2](../../ghippo/intro/release-notes.md#0192)    |
| 容器管理             | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能        | [0.20.1](../../kpanda/intro/release-notes.md#0201)    |
| 可观测性             | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息                     | [0.19.2](../../insight/intro/releasenote.md#0192)     |
| 应用工作台           | 基于容器的 DevOps 应用平台，支持 Jenkins, Tekton, GitOps 等流水线作业    | [0.19.4](../../amamba/intro/release-notes.md#0194)      |
| 多云编排             | 集中管理多云、混合云、跨云资源的应用编排，具备多云灾备、故障恢复等能力   | [0.11.1](../../kairship/intro/release-notes.md#0111)         |
| 微服务引擎           | 提供注册发现、服务治理、配置管理、微服务网关等治理能力                   | [0.26.2](../../skoala/intro/release-notes.md#0262)             |
| 服务网格             | 基于 Istio 开源技术构建的面向云原生应用的下一代服务网格                  | [v0.18.0](../../mspider/intro/release-notes.md#v0180)          |
| 中间件 Elasticsearch | 目前首选的全文搜索引擎                                                   | [0.9.3](../../middleware/elasticsearch/release-notes.md#093) |
| 中间件 Kafka         | 基于开源软件 Kafka 提供的分布式消息队列服务                              | [0.7.3](../../middleware/kafka/release-notes.md#073)          |
| 中间件 MinIO         | 一款非常热门的轻量、开源对象存储方案                                     | [0.7.3](../../middleware/minio/release-notes.md#073)          |
| 中间件 MySQL         | 应用最广泛的开源关系数据库                                               | [0.10.3](../../middleware/mysql/release-notes.md#0103)           |
| 中间件 RabbitMQ      | 实现了高级消息队列协议 (AMQP) 的开源消息代理软件                         | [0.12.3](../../middleware/rabbitmq/release-notes.md#0123)        |
| 中间件 Redis         | 一款内存数据库缓存服务                                                   | [0.10.0](../../middleware/redis/release-notes.md#0100)           |
| 镜像仓库             | 用于存储 K8s、DevOps 和容器应用开发的镜像                                | [0.10.1](../../dce/dce-rn/20230630.md)                            |
| 网络                 | 针对不同的 Linux 内核，支持多种 CNI 组合方案                             | [0.8.1](../../dce/dce-rn/20230630.md)                            |
| 存储                 | 提供统一数据存储服务，支持文件、对象、块、本地存储，轻松接入存储厂商方案 | [v0.10.4](../../dce/dce-rn/20230630.md)                            |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
