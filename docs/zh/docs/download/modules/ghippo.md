---
hide:
  - navigation
---

# 全局管理

本页可下载全局管理模块各版本的离线安装包。

## 下载

| 文件名                       | 版本                                                   | 架构 | 文件大小 | 安装包                                                                                                     | 更新日期   |
| ------------------------------ | ------------------------------------------------------ | ----- |-------- | ---------------------------------------------------------------------------------------------------------- | ---------- |
| ghippo-0.12.1-amd64.bundle.tar | [0.12.1](../../ghippo/01ProductBrief/release-notes.md) | AMD 64 | 441.88MB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.1-amd64.bundle.tar) | 2022-12-20 |
| ghippo-0.12.1-amd64.bundle.tar | [v0.12.1](../../ghippo/01ProductBrief/release-notes.md) | AMD 64 | 442 MB   | [:arrow_down: 下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.1-amd64.bundle.tar) | 2022-11-29 |

## 校验

在下载离线安装包的目录，执行以下命令校验完整性：

```sh
echo "16f3f5549e3f776d46642e94bb4675ab847f5fa3489ee3b7c65ce9c8d36e451989aada4f7042d4c078ea7dcf321b1920b97c6568d3262e234d8c7ed775f9ac70  dist/offline/ghippo-0.12.1.bundle.tar" | sha512sum -c
```

校验成功会打印：

```none
ghippo.tar: ok
```

## 安装

参阅[全局管理](../../ghippo/install/offlineInstall.md)安装流程进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或[正版授权](https://qingflow.com/f/e3291647)。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
