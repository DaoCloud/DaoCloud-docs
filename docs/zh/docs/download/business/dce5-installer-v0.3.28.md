---
date: 2022-11-23
hide:
  - navigation
---

# DCE 5.0 商业版 v0.3.28

本页可下载 DCE 5.0 商业版的离线安装包。

[返回下载导览页](../index.md#_2){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 版本名称            | 文件大小 | 安装包                                                                                               | 更新日期   |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------------- | ---------- |
| offline-v0.3.28.tar | 21 GB    | [:arrow_down: 下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.3.28.tar) | 2022-11-18 |

## 校验

进入离线安装包下载目录。执行以下命令校验安装包：

```sh
echo "88d89872d04d95ee44073c70460c2eb3ae4785a150fbfce672a5882c6f7d77f0d8f58359c5c8695e80d7e5fce93431c0c5ec6b710c080f4840d8adbb25daeb55  offline-v0.3.28.tar" | sha512sum -c
```

校验成功会打印：

```none
offline-v0.3.28.tar: OK
```

## 安装

成功校验离线包之后，解压缩 tar 包：

```sh
tar -zxvf offline-v0.3.28.tar
```

然后参阅[安装 DCE 5.0 商业版](../../install/index.md#_3)进行安装。
如果是初次安装，请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。

## 模块

DCE 5.0 商业版包含以下模块，按需即插即用满足各类应用场景：

| 模块                 | 介绍                                                                     | 模块版本                                                      |
| -------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 全局管理             | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等             | [v0.11](../../ghippo/intro/release-notes.md#v011)    |
| 容器管理             | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能        | [v0.12](../../kpanda/intro/release-notes.md#v012)    |
| 可观测性             | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息                     | [v0.11](../../insight/intro/releasenote.md#v011)     |
| 应用工作台           | 基于容器的 DevOps 应用平台，支持 Jenkins, Tekton, GitOps 等流水线作业    | [v0.9](../../amamba/intro/release-notes.md#v09)      |
| 多云编排             | 集中管理多云、混合云、跨云资源的应用编排，具备多云灾备、故障恢复等能力   | [v0.3](../../kairship/intro/release-notes.md#v03)         |
| 微服务引擎           | 提供注册发现、服务治理、配置管理、微服务网关等治理能力                   | [v0.11](../../skoala/intro/release-notes.md#v011)             |
| 服务网格             | 基于 Istio 开源技术构建的面向云原生应用的下一代服务网格                  | [v0.10](../../mspider/intro/release-notes.md#v010)          |
| 中间件 Elasticsearch | 目前首选的全文搜索引擎                                                   | [v0.3](../../middleware/elasticsearch/release-notes.md#v034) |
| 中间件 Kafka         | 基于开源软件 Kafka 提供的分布式消息队列服务                              | [v0.1](../../middleware/kafka/release-notes.md#v012)          |
| 中间件 MinIO         | 一款非常热门的轻量、开源对象存储方案                                     | [v0.1](../../middleware/minio/release-notes.md#v012)          |
| 中间件 MySQL         | 应用最广泛的开源关系数据库                                               | [v0.4](../../middleware/mysql/release-notes.md#v04)           |
| 中间件 RabbitMQ      | 实现了高级消息队列协议 (AMQP) 的开源消息代理软件                         | [v0.6](../../middleware/rabbitmq/release-notes.md#v06)        |
| 中间件 Redis         | 一款内存数据库缓存服务                                                   | [v0.2](../../middleware/redis/release-notes.md#v02)           |
| 镜像仓库             | 用于存储 K8s、DevOps 和容器应用开发的镜像                                | [发布说明](../../kangaroo/release-notes.md)                            |
| 网络                 | 针对不同的 Linux 内核，支持多种 CNI 组合方案                             | [发布说明](../../network/modules/spiderpool/releasenotes.md)                            |
| 存储                 | 提供统一数据存储服务，支持文件、对象、块、本地存储，轻松接入存储厂商方案 | [发布说明](../../storage/hwameistor/releasenotes.md)                            |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
