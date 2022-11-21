---
date: 2022-11-17
hide:
  - navigation
---

# DCE 5.0 社区版

本页可下载 DCE 5.0 社区版的离线安装包和校验文件。

## 下载

| 版本/名称 | 文件大小 | 下载                                                                                                         | 更新日期   |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------ | ---------- |
| v0.3.28   | 5.8 GB   | [点击下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.28.tar) | 2022-11-11 |
| 校验文件  | 0.6 KB   | [点击下载](./checksum.txt.zip)                                                                               | 2022-11-11 |

## 校验

解压缩 `checksum.txt.zip`，将 txt 文件与 tar 包置于同一个目录。执行以下命令校验安装包：

```sh
echo "$(cat checksum.txt)" | sha512sum -c
```

校验成功会打印：

```none
offline-community-v0.3.28.tar: OK
```

## 安装

成功校验离线包之后，请参阅[社区版安装流程](../../install/install-dce-community.md)进行安装。

成功安装之后请[申请免费社区体验](../../dce/license0.md)。

## 模块

DCE 5.0 社区版默认包含以下模块：

| 模块     | 介绍                                                              | 最新动态                                                      |
| -------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| 全局管理 | 负责用户访问控制、权限、企业空间、审计日志、个性化外观设置等      | [发布说明](../../release/rn5.0.md#_4)                         |
| 容器管理 | 管理集群、节点、工作负载、Helm 应用、CRD、命名空间等 K8s 核心功能 | [v0.12.0](../../kpanda/03ProductBrief/release-notes.md#v0120) |
| 可观测性 | 提供丰富的仪表盘、场景监控、数据查询、告警等图文信息              | [v0.11.1](../../insight/03ProductBrief/releasenote.md#v0111)  |

## 更多

- [在线文档](../../dce/what-is-dce.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
