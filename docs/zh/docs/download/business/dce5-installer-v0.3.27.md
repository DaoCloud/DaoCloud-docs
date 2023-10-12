---
date: 2022-11-23
---

# DCE 5.0 商业版 v0.3.27

本页可下载 DCE 5.0 商业版的离线安装包和校验文件。

[返回下载导览页](../index.md#_2){ .md-button } [更多历史版本](./dce5-installer-history.md){ .md-button }

## 下载

| 版本名称            | 安装包                                                                                               |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| offline-v0.3.27.tar | [:arrow_down: 下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.3.27.tar) |

## 校验

进入离线安装包下载目录。执行以下命令校验安装包：

```sh
echo "f637ec103af6e77d1af85bf0708bef71aee123ce4ac71c4a0adef539492cdbb1661a479d3e999cd51aa7cb47d49e001565908b237ef7999140e3435f6219bb08  offline-v0.3.27.tar" | sha512sum -c
```

校验成功会打印：

```none
offline-v0.3.27.tar: OK
```

## 安装

成功校验离线包之后，请参阅[商业版安装流程](../../install/commercial/start-install.md)进行安装。

成功安装之后请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。

## 模块

DCE 5.0 商业版包含以下模块，按需即插即用满足各类应用场景：

| 模块       | 介绍                                                                     | 最新动态                                                      |
| ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 全局管理   | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等             | [发布说明](../../dce/dce-rn/20230630.md#_4)                         |
| 容器管理   | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能        | [v0.12.0](../../kpanda/intro/release-notes.md#v0120) |
| 可观测性   | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息                     | [v0.11.1](../../insight/intro/releasenote.md#v0111)  |
| 应用工作台 | 基于容器的 DevOps 应用平台，支持 Jenkins, Tekton, GitOps 等流水线作业    | [发布说明](../../amamba/intro/release-notes.md)        |
| 多云编排   | 集中管理多云、混合云、跨云资源的应用编排，具备多云灾备、故障恢复等能力   | [v0.3.0](../../kairship/intro/release-notes.md)           |
| 微服务引擎 | 提供注册发现、服务治理、配置管理、微服务网关等治理能力                   | [发布说明](../../dce/dce-rn/20230630.md)                            |
| 服务网格   | 基于 Istio 开源技术构建的面向云原生应用的下一代服务网格                  | [v0.10.0](../../mspider/intro/release-notes.md)             |
| 中间件     | 包含 RabbitMQ、Kafka、Elasticsearch、MySQL、Redis、MinIO 等精选中间件    | [发布说明](../../dce/dce-rn/20230630.md)                            |
| 镜像仓库   | 用于存储 K8s、DevOps 和容器应用开发的镜像                                | [发布说明](../../dce/dce-rn/20230630.md)                            |
| 网络       | 针对不同的 Linux 内核，支持多种 CNI 组合方案                             | [发布说明](../../dce/dce-rn/20230630.md)                            |
| 存储       | 提供统一数据存储服务，支持文件、对象、块、本地存储，轻松接入存储厂商方案 | [发布说明](../../dce/dce-rn/20230630.md)                            |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
