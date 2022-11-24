---
date: 2022-11-17
hide:
  - navigation
---

# DCE 5.0 社区版 v0.3.28

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 版本名称                      | 安装包                                                                                                         |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| offline-community-v0.3.28.tar | [下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.28.tar) |

## 校验

进入离线安装包下载目录。执行以下命令校验安装包：

```sh
echo "4e1d839ee51f6ff837e2363576cd7ccb794bf81de5fac3c840d14781abc3e077f9014466a3f21d29b83af12643e59e4fa310ecd08831266d2b361ba9e9b81933  offline-community-v0.3.28.tar" | sha512sum -c
```

校验成功会打印：

```none
offline-community-v0.3.28.tar: OK
```

## 安装

成功校验离线包之后，解压缩 tar 包：

```sh
tar -zxvf offline-community-v0.3.28.tar
```

然后参阅[社区版安装流程](../../install/offline-install-community.md#_2)进行安装。

成功安装之后请[申请免费社区体验](../../dce/license0.md)。

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                   |
| -------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [v0.11](../../ghippo/01ProductBrief/release-notes.md#v011) |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [v0.12](../../kpanda/03ProductBrief/release-notes.md#v012) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [v0.11](../../insight/03ProductBrief/releasenote.md#v011)  |

## 更多

- [在线文档](https://docs.daocloud.io/dce/what-is-dce/)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
