---
date: 2022-11-23
---

# DCE 5.0 社区版 v0.3.27

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 版本名称                      | 安装包                                                                                                         |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| offline-community-v0.3.27.tar | [:arrow_down: 下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.27.tar) |

## 校验

进入离线安装包下载目录。执行以下命令校验安装包：

```sh
echo "7a2f07fd9d09c827347d2994c0b6d4852f55e1f6de149e7b95e29625c4081eba3d415d3dbb261d226d8179c3251ac8e67c2de898d3eb6a58ff218f79fd31d42e  offline-community-v0.3.27.tar" | sha512sum -c
```

校验成功会打印：

```none
offline-community-v0.3.27.tar: OK
```

## 安装

成功校验离线包之后，解压缩 tar 包：

```sh
tar -zxvf offline-community-v0.3.28.tar
```

然后参阅[社区版安装流程](../../install/community/k8s/online.md#_2)进行安装。

成功安装之后请[申请免费社区体验](../../dce/license0.md)。

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                      |
| -------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [发布说明](../../dce/dce-rn/20230630.md#_4)                         |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [v0.12.0](../../kpanda/intro/release-notes.md#v0120) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [v0.11.1](../../insight/intro/releasenote.md#v0111)  |

## 更多

- [在线文档](../../dce/index.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
