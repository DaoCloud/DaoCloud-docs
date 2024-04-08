---
MTPE: windsonsea
date: 2024-01-18
hide:
  - toc
---

# MinIO

This page provides downloadable offline packages for various versions of MinIO.

## Download

| Version | Architecture | File Size | Package   | Checksum File | Updated Date |
| ------ | ------------ | --------- | ---------- | ------------ | ------------ |
| [v0.13.0](../../../middleware/minio/release-notes.md) | <font color="green">ARM 64</font> | 211.15 MB | [:arrow_down: minio_0.13.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_arm64.tar) | [:arrow_down: minio_0.13.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_arm64_checksum.sha512sum) | 2024-04-03 |
| [v0.13.0](../../../middleware/minio/release-notes.md) | AMD 64 | 220.56 MB | [:arrow_down: minio_0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_amd64.tar) | [:arrow_down: minio_0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.13.0_amd64_checksum.sha512sum) | 2024-04-03 |
| [v0.12.0](../../../middleware/minio/release-notes.md) | AMD 64 | 218.97 MB | [:arrow_down: minio_0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.12.0_amd64.tar) | [:arrow_down: minio_0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.12.0_amd64_checksum.sha512sum) | 2024-02-01 |
| [v0.11.0](../../../middleware/minio/release-notes.md) | AMD 64 | 218.84 MB | [:arrow_down: minio_0.11.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.11.0_amd64.tar) | [:arrow_down: minio_0.11.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.11.0_amd64_checksum.sha512sum) | 2024-01-04 |
| [v0.10.0](../../../middleware/minio/release-notes.md) | AMD 64 | 256.16 MB | [:arrow_down: minio_0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.10.0_amd64.tar) | [:arrow_down: minio_0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.10.0_amd64_checksum.sha512sum) | 2023-12-10 |
| [v0.9.0](../../../middleware/minio/release-notes.md) | AMD 64 | 253.79 MB | [:arrow_down: minio_0.9.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.9.0_amd64.tar) | [:arrow_down: minio_0.9.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.9.0_amd64_checksum.sha512sum) | 2023-11-02 |
| [v0.8.1](../../../middleware/minio/release-notes.md) | AMD 64 | 219.92 MB | [:arrow_down: minio_0.8.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.8.1_amd64.tar) | [:arrow_down: minio_0.8.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-minio_0.8.1_amd64_checksum.sha512sum) | 2023-10-20 |

## Validation

To validate the integrity of the downloaded offline package and checksum file, run the following command in the directory where they are located:

```sh
echo "$(cat minio_0.8.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the printed result will be similar to:

```none
minio_0.8.1_amd64.tar: OK
```

## Installation

If this is your first time installing MinIO, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please reach out to the DaoCloud delivery team.
