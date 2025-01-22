---
hide:
  - toc
---

# 网络 Spidernet

本页可下载网络 Spidernet 模块各版本的离线安装包。

## 下载

| 版本 |  架构  | 文件大小 | 安装包 | 校验文件 | 更新日期 |
| ---- | ----- | ------ | ------ | ------ | ------- |
| [v0.16.2](../../network/intro/release-notes.md) | AMD 64 | 63.76 MB | [:arrow_down: spidernet_v0.16.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.16.2_amd64.tar) | [:arrow_down: spidernet_v0.16.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.16.2_amd64_checksum.sha512sum) | 2024-11-28 |
| [v0.16.1](../../network/intro/release-notes.md) | AMD 64 | 63.76 MB | [:arrow_down: spidernet_v0.16.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.16.1_amd64.tar) | [:arrow_down: spidernet_v0.16.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.16.1_amd64_checksum.sha512sum) | 2024-10-29 |
| [v0.16.0](../../network/intro/release-notes.md) | AMD 64 | 63.76 MB | [:arrow_down: spidernet_v0.16.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.16.0_amd64.tar) | [:arrow_down: spidernet_v0.16.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.16.0_amd64_checksum.sha512sum) | 2024-09-26 |
| [v0.15.0](../../network/intro/release-notes.md) | AMD 64 | 63.50 MB | [:arrow_down: spidernet_v0.15.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.15.0_amd64.tar) | [:arrow_down: spidernet_v0.15.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.15.0_amd64_checksum.sha512sum) | 2024-05-23 |
| [v0.14.0](../../network/intro/release-notes.md) | AMD 64 | 63.43 MB | [:arrow_down: spidernet_v0.14.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.14.0_amd64.tar) | [:arrow_down: spidernet_v0.14.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.14.0_amd64_checksum.sha512sum) | 2024-04-29 |
| [v0.13.0](../../network/intro/release-notes.md) | AMD 64 | 65.71 MB | [:arrow_down: spidernet_v0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.13.0_amd64.tar) | [:arrow_down: spidernet_v0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.13.0_amd64_checksum.sha512sum) | 2024-01-28 |
| [v0.12.0](../../network/intro/release-notes.md) | AMD 64 | 64.03 MB | [:arrow_down: spidernet_v0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.12.0_amd64.tar) | [:arrow_down: spidernet_v0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.12.0_amd64_checksum.sha512sum) | 2023-12-26 |
| [v0.6.0](../../network/intro/release-notes.md) | AMD64 | 55.47 MB | [:arrow_down: spidernet_v0.6.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.6.0_amd64.tar) | [:arrow_down: spidernet_v0.6.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.6.0_amd64_checksum.sha512sum) | 2023-04-26 |
| [v0.5.0](../../network/intro/release-notes.md) | AMD64 | 51.68 MB | [:arrow_down: spidernet_v0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.5.0_amd64.tar) | [:arrow_down: spidernet_v0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.5.0_amd64_checksum.sha512sum) | 2023-04-25 |

## 校验

在下载离线安装包和校验文件的目录，以 `v0.5.0_amd64` 为例，执行以下命令校验完整性：

```sh
echo "$(cat spidernet_v0.5.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
spidernet_v0.5.0_amd64.tar: ok
```

## 安装

参阅[离线升级网络模块](../../network/intro/offline.md)进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
