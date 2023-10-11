---
hide:
  - navigation
---

# 可观测性 Insight

本页可下载可观测性模块各版本的离线安装包。

[返回下载首页](../index.md){ .md-button }

## 下载

| 版本                                                   | 架构 | 文件大小 | 安装包                                                                                                     |  校验文件 | 更新日期   |
| ------------------------------------------------------ | ----- |-------- | ---------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [v0.19.1](../../insight/intro/releasenote.md) | AMD 64 | 2.64 GB | [:arrow_down: insight_v0.19.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.19.1_amd64.tar) | [:arrow_down: insight_v0.19.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.19.1_amd64_checksum.sha512sum) | 2023-08-04 |
| [v0.13.1](../../insight/intro/releasenote.md) | AMD64 | 2.41 GB | [:arrow_down: insight_v0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64.tar) | [:arrow_down: insight_v0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64_checksum.sha512sum) | 2022-12-30 |

## 校验

在下载离线安装包和校验文件的目录，以 v0.13.1_amd64 为例，执行以下命令校验完整性：

```sh
echo "$(cat insight_v0.13.1_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
insight_v0.13.1_amd64.tar: ok
```

## 安装

参阅[可观测性](../../insight/quickstart/install/offline-install.md)安装流程进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
