---
MTPE: windsonsea
date: 2024-01-18
hide:
  - toc
---

# Operations Management

This page allows you to download the offline packages for different versions of the Operations Management module.

## Download

| Version  | Architecture | File Size | Package     | Checksum File      | Update Date |
|----------|--------------|-----------|-------------|--------------------|-------------|
| [v0.5.1](../../ghippo/intro/release-notes.md) | ARM 64 | 90.85 MB | [:arrow_down: gmagpie_v0.5.1_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.1_arm64.tar) | [:arrow_down: gmagpie_v0.5.1_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.1_arm64_checksum.sha512sum) | 2024-02-01 |
| [v0.5.1](../../ghippo/intro/release-notes.md) | AMD 64 | 96.27 MB | [:arrow_down: gmagpie_v0.5.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.1_amd64.tar) | [:arrow_down: gmagpie_v0.5.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.1_amd64_checksum.sha512sum) | 2024-02-01 |
| [v0.5.0](../../ghippo/intro/release-notes.md) | ARM 64 | 90.51 MB | [:arrow_down: gmagpie_v0.5.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.0_arm64.tar) | [:arrow_down: gmagpie_v0.5.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.0_arm64_checksum.sha512sum) | 2024-01-29 |
| [v0.5.0](../../ghippo/intro/release-notes.md) | AMD 64 | 95.94 MB | [:arrow_down: gmagpie_v0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.0_amd64.tar) | [:arrow_down: gmagpie_v0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.5.0_amd64_checksum.sha512sum) | 2024-01-29 |
| [v0.4.3](../../ghippo/intro/release-notes.md) | AMD 64 | 95.90 MB | [:arrow_down: gmagpie_v0.4.3_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.3_amd64.tar) | [:arrow_down: gmagpie_v0.4.3_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.3_amd64_checksum.sha512sum) | 2023-11-30 |
| [v0.4.2](../../ghippo/intro/release-notes.md) | AMD 64 | 93.79 MB | [:arrow_down: gmagpie_v0.4.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.2_amd64.tar) | [:arrow_down: gmagpie_v0.4.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.2_amd64_checksum.sha512sum) | 2023-10-30 |
| [v0.4.1](../../ghippo/intro/release-notes.md) | AMD 64 | 93.72 MB | [:arrow_down: gmagpie_v0.4.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.1_amd64.tar) | [:arrow_down: gmagpie_v0.4.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.1_amd64_checksum.sha512sum) | 2023-08-29 |
| [v0.3.2](../../ghippo/intro/release-notes.md) | AMD 64 | 91.85 MB | [:arrow_down: gmagpie_v0.3.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.2_amd64.tar) | [:arrow_down: gmagpie_v0.3.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.2_amd64_checksum.sha512sum) | 2023-08-02 |
| [v0.3.0](../../ghippo/intro/release-notes.md) | AMD 64 | 56.90 MB | [:arrow_down: gmagpie_v0.3.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.0_amd64.tar) | [:arrow_down: gmagpie_v0.3.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.0_amd64_checksum.sha512sum) | 2023-06-28 |
| [v0.2.2](../../ghippo/intro/release-notes.md) | AMD64 | 37.1 MB | [:arrow_down: gmagpie_v0.2.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.2.2_amd64.tar) | [:arrow_down: gmagpie_v0.2.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.2.2_amd64_checksum.sha512sum) | 2023-5-30 |

## Validation

Navigate to the directory where the offline packages and checksum files are downloaded,
take `v0.2.2_amd64` as an example, and run the following command to validate the integrity:

```sh
echo "$(cat gmagpie_v0.2.2_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the result will be similar to:

```none
gmagpie_v0.2.2_amd64.tar: ok
```

## Installation

Refer to the [Operation Management installation process](../../ghippo/user-guide/report-billing/gmagpie-offline-install.md) for installation instructions.

If this is your first-time installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization at info@daocloud.io or call 400 002 6898.
For any license-related issues, please contact the DaoCloud delivery team.
