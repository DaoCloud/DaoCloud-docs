---
hide:
  - navigation
---

# 全局管理

本页可下载全局管理模块各版本的离线安装包。

## 下载

| 文件名                       | 版本                                                   | 文件大小 | 安装包                                                                                                     | checksum | 更新日期   |
| ------------------------------ | ------------------------------------------------------ | -------- | ---------------------------------------------------------------------------------------------------------- | ----- | ---------- |
| ghippo-0.12.1-amd64.bundle.tar | [v0.12.1](../../ghippo/01ProductBrief/release-notes.md) | 442 MB   | [:arrow_down: 下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.1-amd64.bundle.tar) | [:arrow_down: 下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.1-amd64-checksum.sha512sum) | 2022-11-29 |

## 校验

在下载离线安装包和 checksum 的目录，执行以下命令校验完整性：

```sh
echo "$(cat ghippo-checksum.sha512sum)" | sha512sum -c
```

校验成功会打印：

```none
ghippo.bundle.tar: ok
```

## 安装

参阅[全局管理](../../ghippo/install/offlineInstall.md)安装流程进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或[正版授权](https://qingflow.com/f/e3291647)。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
