---
hide:
  - toc
---

# Application Backup

This page provides offline packages for different versions of the Application Backup module.

## Download

| Version   | Architecture | File Size | Package   | Checksum File | Updated Date |
|-----------| ------------ | --------- | --------- | ------------  | -----------  |
| [v0.7.0](../../kpanda/intro/release-notes.md) | AMD 64 | 59.40 MB | [:arrow_down: kcoral_v0.7.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.7.0_amd64.tar) | [:arrow_down: kcoral_v0.7.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.7.0_amd64_checksum.sha512sum) | 2023-12-01 |
| [v0.6.1](../../kpanda/intro/release-notes.md) | AMD 64 | 59.38 MB | [:arrow_down: kcoral_v0.6.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.1_amd64.tar) | [:arrow_down: kcoral_v0.6.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.1_amd64_checksum.sha512sum) | 2023-11-07 |
| [v0.6.0](../../kpanda/intro/release-notes.md) | AMD 64 | 59.38 MB | [:arrow_down: kcoral_v0.6.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.0_amd64.tar) | [:arrow_down: kcoral_v0.6.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.0_amd64_checksum.sha512sum) | 2023-10-26 |
| [v0.5.0](../../kpanda/intro/release-notes.md) | AMD 64 | 59.30 MB | [:arrow_down: kcoral_v0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.5.0_amd64.tar) | [:arrow_down: kcoral_v0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.5.0_amd64_checksum.sha512sum) | 2023-09-01 |
| [v0.4.0](../../kpanda/intro/release-notes.md) | AMD64 | 59.29 MB | [:arrow_down: kcoral_v0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.4.0_amd64.tar) | [:arrow_down: kcoral_v0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.4.0_amd64_checksum.sha512sum) | 2023-08-08 |

## Validation

To validate the integrity of the downloaded offline package and checksum file,
take `v0.4.0_amd64` as an example, run the following command in the directory:

```sh
echo "$(cat kcoral_v0.4.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the result will be similar to:

```none
kcoral_v0.4.0_amd64.tar: ok
```

## Installation

Refer to the [Offline Upgrade Backup and Restore Module](../../kpanda/user-guide/backup/offline-upgrade.md) for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization:
email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
