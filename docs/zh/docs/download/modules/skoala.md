---
hide:
  - toc
---

# 微服务引擎 Skoala

本页可下载微服务引擎模块各版本的离线安装包，其中包括：

- Skoala 管理组件的 Helm Chart 和镜像
- Skoala-Init 集群初始化组件的 Helm Chart 和镜像。

## 下载

| 版本 | 架构 | 文件大小 | 安装包 |  校验文件 | 更新日期   |
| --- | ----- | ----- | ------ | ------- | --------- |
| [v0.31.2](../../skoala/intro/release-notes.md) | AMD 64 | 1.6 GB | [:arrow_down: skoala_v0.31.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.31.2_amd64.tar) | [:arrow_down: skoala_v0.31.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.31.2_amd64_checksum.sha512sum) | 2024-01-03 |
| [v0.31.1](../../skoala/intro/release-notes.md) | AMD 64 | 1.6 GB | [:arrow_down: skoala_v0.31.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.31.1_amd64.tar) | [:arrow_down: skoala_v0.31.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.31.1_amd64_checksum.sha512sum) | 2023-12-26 |
| [v0.31.0](../../skoala/intro/release-notes.md) | AMD 64 | 1.6 GB | [:arrow_down: skoala_v0.31.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.31.0_amd64.tar) | [:arrow_down: skoala_v0.31.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.31.0_amd64_checksum.sha512sum) | 2023-12-26 |
| [v0.30.0](../../skoala/intro/release-notes.md) | AMD 64 | 1.34 GB | [:arrow_down: skoala_v0.30.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.30.0_amd64.tar) | [:arrow_down: skoala_v0.30.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.30.0_amd64_checksum.sha512sum) | 2023-12-01 |
| [v0.29.0](../../skoala/intro/release-notes.md) | AMD 64 | 1.34 GB | [:arrow_down: skoala_v0.29.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.29.0_amd64.tar) | [:arrow_down: skoala_v0.29.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.29.0_amd64_checksum.sha512sum) | 2023-11-27 |
| [v0.28.1](../../skoala/intro/release-notes.md) | AMD 64 | 1.34 GB | [:arrow_down: skoala_v0.28.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.1_amd64.tar) | [:arrow_down: skoala_v0.28.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.1_amd64_checksum.sha512sum) | 2023-11-01 |
| [v0.28.0](../../skoala/intro/release-notes.md) | AMD 64 | 1.33 GB | [:arrow_down: skoala_v0.28.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.0_amd64.tar) | [:arrow_down: skoala_v0.28.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.0_amd64_checksum.sha512sum) | 2023-10-27 |

## 校验

在下载离线安装包和校验文件的目录，执行以下命令校验完整性：

```sh
echo "$(cat skoala_v0.28.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
skoala_v0.28.0_amd64.tar: ok
```

## 安装

参阅[微服务引擎离线升级步骤](../../skoala/quickstart/skoala.md#_11)。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
