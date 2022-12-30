---
hide:
  - navigation
---

# 可观测性 Insight

本页可下载可观测性模块各版本的离线安装包。

## 下载

| 文件名                       | 版本                                                   | 架构 | 文件大小 | 安装包                                                                                                     | 更新日期   |
| ------------------------------ | ------------------------------------------------------ | ----- |-------- | ---------------------------------------------------------------------------------------------------------- | ---------- |
| insight_v0.13.1_amd64.tar | [v0.13.2](../../insight/03ProductBrief/releasenote.md) | AMD 64 | 2.41GB | [:arrow_down: 下载](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64.tar) | 2022-12-30 |

## 校验

在下载离线安装包的目录，执行以下命令校验完整性：

```sh
echo "cb246c2fb275780a87bb37f915cf58fb3097aa99606afd112aff2c0bb7716816ed96ca10260a0dffed0228bb33fa466310b10e8dad6c49c12351fbe48036bbbf  dist/offline/insight_v0.13.1_amd64.tar" | sha512sum -c
```

校验成功会打印：

```none
insight.tar: ok
```

## 安装

参阅[可观测性](../../insight/06UserGuide/01quickstart/offlineInstall.md)安装流程进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或[正版授权](https://qingflow.com/f/e3291647)。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
