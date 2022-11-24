---
date: 2022-11-24
hide:
  - navigation
---

# DCE 5.0 社区版 v0.2.0-1199-g36cd2b90

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 版本名称 | 安装包 |
| ----- | ----- |
| offline-centos7-community-v0.2.0-1199-g36cd2b90-amd64.tar | [下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-community-v0.2.0-1199-g36cd2b90-amd64.tar) |

## 校验

进入离线安装包下载目录。执行以下命令校验安装包：

```sh
echo "88d89872d04d95ee44073c70460c2eb3ae4785a150fbfce672a5882c6f7d77f0d8f58359c5c8695e80d7e5fce93431c0c5ec6b710c080f4840d8adbb25daeb55" | sha512sum -c
```

校验成功会打印：

```none
offline-centos7-community-v0.2.0-1199-g36cd2b90-amd64.tar: OK
```

## 安装

成功校验离线包之后，解压缩 tar 包：

```sh
tar -zxvf offline-centos7-community-v0.2.0-1199-g36cd2b90-amd64.tar
```

然后参阅[社区版安装流程](../../install/offline-install-community.md#_2)进行安装。

成功安装之后请[申请免费社区体验](../../dce/license0.md)。

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [发布说明](../../release/rn5.0.md#_4)                         |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [v0.12.0](../../kpanda/03ProductBrief/release-notes.md#v0120) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [v0.11.1](../../insight/03ProductBrief/releasenote.md#v0111)  |

## 更多

- [在线文档](https://docs.daocloud.io/dce/what-is-dce/)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
