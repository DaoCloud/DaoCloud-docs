---
MTPE: windsonsea
date: 2024-01-18
hide:
  - toc
---

# PostgreSQL

This page provides downloadable offline packages for various versions of PostgreSQL.

## Download

| Version | Architecture | File Size | Package   | Checksum File | Updated Date |
| ------ | ------------ | --------- | ---------- | ------------ | ------------ |
| [v0.11.0](../../../middleware/postgresql/release-notes.md) | <font color=green>ARM 64</font> | 1.41 GB | [:arrow_down: postgresql_0.11.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.11.0_arm64.tar) | [:arrow_down: postgresql_0.11.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.11.0_arm64_checksum.sha512sum) | 2024-05-08 |
| [v0.11.0](../../../middleware/postgresql/release-notes.md) | AMD 64 | 1.46 GB | [:arrow_down: postgresql_0.11.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.11.0_amd64.tar) | [:arrow_down: postgresql_0.11.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.11.0_amd64_checksum.sha512sum) | 2024-05-08 |
| [v0.10.0](../../../middleware/postgresql/release-notes.md) | <font color="green">ARM 64</font> | 1.41 GB | [:arrow_down: postgresql_0.10.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.10.0_arm64.tar) | [:arrow_down: postgresql_0.10.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.10.0_arm64_checksum.sha512sum) | 2024-04-03 |
| [v0.10.0](../../../middleware/postgresql/release-notes.md) | AMD 64 | 1.46 GB | [:arrow_down: postgresql_0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.10.0_amd64.tar) | [:arrow_down: postgresql_0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.10.0_amd64_checksum.sha512sum) | 2024-04-03 |
| [v0.9.0](../../../middleware/postgresql/release-notes.md) | AMD 64 | 1.38 GB | [:arrow_down: postgresql_0.9.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.9.0_amd64.tar) | [:arrow_down: postgresql_0.9.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.9.0_amd64_checksum.sha512sum) | 2024-02-01 |
| [v0.8.0](../../../middleware/postgresql/release-notes.md) | AMD 64 | 1.38 GB | [:arrow_down: postgresql_0.8.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.8.0_amd64.tar) | [:arrow_down: postgresql_0.8.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.8.0_amd64_checksum.sha512sum) | 2024-01-04 |
| [v0.7.0](../../../middleware/postgresql/release-notes.md) | AMD 64 | 1.38 GB | [:arrow_down: postgresql_0.7.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.7.0_amd64.tar) | [:arrow_down: postgresql_0.7.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.7.0_amd64_checksum.sha512sum) | 2023-12-10 |
| [v0.6.0](../../../middleware/postgresql/release-notes.md) | AMD 64 | 1.37 GB | [:arrow_down: postgresql_0.6.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.6.0_amd64.tar) | [:arrow_down: postgresql_0.6.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.6.0_amd64_checksum.sha512sum) | 2023-11-02 |
| [v0.5.1](../../../middleware/postgresql/release-notes.md) | AMD 64 | 819.03 MB | [:arrow_down: postgresql_0.5.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.5.1_amd64.tar) | [:arrow_down: postgresql_0.5.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-postgresql_0.5.1_amd64_checksum.sha512sum) | 2023-10-20 |

## Validation

To validate the integrity of the downloaded offline package and checksum file, run the following command in the directory:

```sh
echo "$(cat postgresql_0.5.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the printed result will be similar to:

```none
postgresql_0.5.1_amd64.tar: OK
```

## Installation

If this is your first installation, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization at info@daocloud.io or call 400 002 6898.
For any license key-related questions, please contact the DaoCloud delivery team.
