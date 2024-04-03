---
hide:
  - toc
---

# MinIO

本页可下载 MinIO 各版本的离线安装包。

## 下载

| 版本 | 架构 | 文件大小 | 安装包 | 校验文件 | 更新日期 |
| ---- | --- | ------ | ------ | ------ | ------- |
| [v0.13.0](../../../middleware/minio/release-notes.md) | ARM 64 | 211.15 MB | [:arrow_down: minio_0.13.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_arm64.tar) | [:arrow_down: minio_0.13.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_arm64_checksum.sha512sum) | 2024-04-03 |
| [v0.13.0](../../../middleware/minio/release-notes.md) | AMD 64 | 220.56 MB | [:arrow_down: minio_0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_amd64.tar) | [:arrow_down: minio_0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_amd64_checksum.sha512sum) | 2024-04-03 |
| [v0.12.0](../../../middleware/minio/release-notes.md) | AMD 64 | 218.97 MB | [:arrow_down: minio_0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.12.0_amd64.tar) | [:arrow_down: minio_0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.12.0_amd64_checksum.sha512sum) | 2024-02-01 |
| [v0.11.0](../../../middleware/minio/release-notes.md) | AMD 64 | 218.84 MB | [:arrow_down: minio_0.11.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.11.0_amd64.tar) | [:arrow_down: minio_0.11.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.11.0_amd64_checksum.sha512sum) | 2024-01-04 |
| [v0.10.0](../../../middleware/minio/release-notes.md) | AMD 64 | 256.16 MB | [:arrow_down: minio_0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.10.0_amd64.tar) | [:arrow_down: minio_0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.10.0_amd64_checksum.sha512sum) | 2023-12-10 |
| [v0.9.0](../../../middleware/minio/release-notes.md) | AMD 64 | 253.79 MB | [:arrow_down: minio_0.9.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.9.0_amd64.tar) | [:arrow_down: minio_0.9.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.9.0_amd64_checksum.sha512sum) | 2023-11-02 |
| [v0.8.1](../../../middleware/minio/release-notes.md) | AMD 64 | 219.92 MB | [:arrow_down: minio_0.8.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.8.1_amd64.tar) | [:arrow_down: minio_0.8.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.8.1_amd64_checksum.sha512sum) | 2023-10-20 |

## 校验

在下载离线安装包和校验文件的目录，执行以下命令校验完整性：

```sh
echo "$(cat mcamel-minio_0.8.1_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
mcamel-minio_0.8.1_amd64.tar: OK
```

## 安装

如果是初次安装，请[申请免费体验](../../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。