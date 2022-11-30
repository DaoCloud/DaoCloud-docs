# 全局管理

本页可下载全局管理模块各版本的离线安装包。

## 下载

| 文件名                       | 版本                                                   | 文件大小 | 安装包                                                                                                     | 更新日期   |
| ------------------------------ | ------------------------------------------------------ | -------- | ---------------------------------------------------------------------------------------------------------- | ---------- |
| ghippo-0.12.1-amd64.bundle.tar | [v0.12.1](../../ghippo/01ProductBrief/release-notes.md) | 442 MB   | [点击下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.1-amd64.bundle.tar) | 2022-11-29 |

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

成功安装之后请[申请免费体验](../../dce/license0.md)或[正版授权](https://qingflow.com/f/e3291647)。
