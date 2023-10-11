---
date: 2023-01-03
---

# DCE 5.0 商业版 v0.3.30

本页可下载 DCE 5.0 商业版的离线安装包和校验文件。

[返回下载首页](../index.md){ .md-button }

## 下载

| 文件名                      | 版本    | 架构 | 文件大小 | 下载                                           | 更新日期   |
| ----------------------------- | ------- | -------- | ---------------------------------------------- | ---------- | ----------------------------- |
| offline-centos7-v0.3.30-amd64.tar | v0.3.30 | AMD64 | 16.33GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-v0.3.30-amd64.tar) | 2023-01-03 |
| offline-kylin-v10sp2-v0.3.30-arm64.tar | v0.3.30 | ARM64 | 14.96GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-v0.3.30-arm64.tar) | 2023-01-03 |

## 校验

进入离线安装包下载目录。

=== "AMD64"

    执行以下命令校验安装包：

    ```sh
    echo "08ccfce8e3f551e82bdb89f26d0e9bb9b0f40e02cd5bcd0db8662c70d22932f24b2958ab3ea71e0ec497d8ad75a1cc134cdd24eabbfe9003c3c120c83d4d0417  offline-centos7-v0.3.30-amd64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-centos7-v0.3.30-amd64.tar: OK
    ```

=== "ARM64"

    执行以下命令校验安装包：

    ```sh
    echo "a970526876754b763d8cc3df32ac522075ad2e08989a9bbad08b3a9be75366be6208f6e8d2865ee05c07291545373ef045bfc6fb31179df1ad2140b2b8741998  offline-kylin-v10sp2-v0.3.30-arm64.tar" | sha512sum -c
    ```

    校验成功会打印：

    ```none
    offline-kylin-v10sp2-v0.3.30-arm64.tar: OK
    ```

## 安装

成功校验离线包之后，

=== "AMD64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-centos7-v0.3.30-amd64.tar
    ```

=== "ARM64"

    执行以下命令解压缩 tar 包：

    ```sh
    tar -zxvf offline-kylin-v10sp2-v0.3.30-arm64.tar
    ```

- 安装请参阅[商业版安装流程](../../install/commercial/start-install.md)
- 成功安装之后请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898

## 模块

DCE 5.0 商业版包含以下模块，按需即插即用满足各类应用场景：

| 模块                 | 介绍                                                                     | 最新动态                                                      |
| -------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 全局管理             | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等             | [v0.13](../../ghippo/intro/release-notes.md#v013)    |
| 容器管理             | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能        | [v0.14](../../kpanda/intro/release-notes.md#v014)    |
| 可观测性             | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息                     | [v0.13](../../insight/intro/releasenote.md#v013)     |
| 应用工作台           | 基于容器的 DevOps 应用平台，支持 Jenkins, Tekton, GitOps 等流水线作业    | [v0.12](../../amamba/intro/release-notes.md#v012)      |
| 多云编排             | 集中管理多云、混合云、跨云资源的应用编排，具备多云灾备、故障恢复等能力   | [v0.5](../../kairship/intro/release-notes.md#v05)         |
| 微服务引擎           | 提供注册发现、服务治理、配置管理、微服务网关等治理能力                   | [v0.16](../../skoala/intro/release-notes.md#v016)             |
| 服务网格             | 基于 Istio 开源技术构建的面向云原生应用的下一代服务网格                  | [v0.12](../../mspider/intro/release-notes.md#v012)          |
| 中间件 Elasticsearch | 目前首选的全文搜索引擎                                                   | [v0.4](../../middleware/elasticsearch/release-notes.md#v04) |
| 中间件 Kafka         | 基于开源软件 Kafka 提供的分布式消息队列服务                              | [v0.2](../../middleware/kafka/release-notes.md#v02)          |
| 中间件 MinIO         | 一款非常热门的轻量、开源对象存储方案                                     | [v0.2](../../middleware/minio/release-notes.md#v02)          |
| 中间件 MySQL         | 应用最广泛的开源关系数据库                                               | [v0.5](../../middleware/mysql/release-notes.md#v05)           |
| 中间件 RabbitMQ      | 实现了高级消息队列协议 (AMQP) 的开源消息代理软件                         | [v0.7](../../middleware/rabbitmq/release-notes.md#v07)        |
| 中间件 Redis         | 一款内存数据库缓存服务                                                   | [v0.4](../../middleware/redis/release-notes.md#v04)           |
| 镜像仓库             | 用于存储 K8s、DevOps 和容器应用开发的镜像                                | [发布说明](../../kangaroo/release-notes.md)                            |
| 网络                 | 针对不同的 Linux 内核，支持多种 CNI 组合方案                             | [发布说明](../../network/modules/spiderpool/releasenotes.md)                            |
| 存储                 | 提供统一数据存储服务，支持文件、对象、块、本地存储，轻松接入存储厂商方案 | [发布说明](../../storage/hwameistor/releasenotes.md)                            |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
