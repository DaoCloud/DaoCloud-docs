---
MTPE: windsonsea
date: 2024-01-18
hide:
  - toc
---

# Container Registry

On this page, you can download offline packages for different versions of the container registry module.

## Download

| Version  | Architecture | File Size | Package     | Checksum File      | Update Date |
|----------|--------------|-----------|-------------|--------------------|-------------|
| [0.14.0](../../kangaroo/intro/release-notes.md) | AMD 64 | 295.53 MB | [:arrow_down: kangaroo_0.14.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.14.0_amd64.tar) | [:arrow_down: kangaroo_0.14.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.14.0_amd64_checksum.sha512sum) | 2023-12-29 |
| [0.13.1](../../kangaroo/intro/release-notes.md) | AMD 64 | 297.59MB | [:arrow_down: kangaroo_0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.13.1_amd64.tar) | [:arrow_down: kangaroo_0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.13.1_amd64_checksum.sha512sum) | 2023-12-01 |
| [0.13.0](../../kangaroo/intro/release-notes.md) | AMD 64 | 299.82MB | [:arrow_down: kangaroo_0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.13.0_amd64.tar) | [:arrow_down: kangaroo_0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.13.0_amd64_checksum.sha512sum) | 2023-11-28 |
| [0.12.1](../../kangaroo/intro/release-notes.md) | AMD 64 | 299.24MB | [:arrow_down: kangaroo_0.12.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.1_amd64.tar) | [:arrow_down: kangaroo_0.12.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.1_amd64_checksum.sha512sum) | 2023-11-03 |
| [0.12.0](../../kangaroo/intro/release-notes.md) | AMD 64 | 299.24MB | [:arrow_down: kangaroo_0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.0_amd64.tar) | [:arrow_down: kangaroo_0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.0_amd64_checksum.sha512sum) | 2023-10-29 |
| [0.11.0](../../kangaroo/intro/release-notes.md) | AMD 64 | 296.23MB | [:arrow_down: kangaroo_0.11.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.11.0_amd64.tar) | [:arrow_down: kangaroo_0.11.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.11.0_amd64_checksum.sha512sum) | 2023-09-04 |
| [v0.10.0](../../kangaroo/intro/release-notes.md) | AMD64        | 293.24 MB | [:arrow_down: kangaroo_v0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.10.0_amd64.tar) | [:arrow_down: kangaroo_0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.10.0_amd64_checksum.sha512sum) | 2023-8-22   |

## Validation

In the directory where you downloaded the offline package and checksum file,
take v0.10.0 as an example and run the following command to validate the integrity:

```sh
echo "$(cat kangaroo_0.10.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the result will be similar to:

```none
kangaroo_0.10.0_amd64.tar: ok
```

## Installation

Refer to [Offline Upgrade Container Registry Module](../../kangaroo/intro/upgrade.md) for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization: send an email to info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
