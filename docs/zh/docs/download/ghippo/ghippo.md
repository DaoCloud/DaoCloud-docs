---
date: 2022-11-21
hide:
  - navigation
---

# 全局管理

本页可下载[全局管理](../../ghippo/01ProductBrief/WhatisGhippo.md)模块的离线安装包和校验文件。

## 下载

| 版本/名称 | 文件大小 | 下载                                                                                               | 更新日期   |
| --------- | -------- | -------------------------------------------------------------------------------------------------- | ---------- |
| v0.5.6   | 2 GB    | [点击下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.3.28.tar) | 2022-11-21 |
| 校验文件  | 0.6 KB   | [点击下载](./checksum.txt.zip)                                                                     | 2022-11-21 |

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

成功校验离线包之后，请参阅[商业版安装流程](../../install/Air-Gap-install-full/start-install.md)进行安装。

成功安装之后请进行[正版授权](https://qingflow.com/f/e3291647)。

## 更多

- [全局管理介绍](../../ghippo/01ProductBrief/WhatisGhippo.md)
- [报告 bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
