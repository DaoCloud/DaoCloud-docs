---
MTPE: windsonsea
date: 2024-01-11
hide:
  - toc
---

# Workbench

This page provides downloads for the offline package of different versions of the Workbench module.

## Downloads

| Version | Architecture | File Size | Package   | Checksum File | Updated Date |
| ------ | ------------ | --------- | ---------- | ------------ | ------------ |
| [v0.25.2](../../amamba/intro/release-notes.md) | <font color="green">ARM 64</font> | 353.54 MB | [:arrow_down: amamba_v0.25.2_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.2_arm64.tar) | [:arrow_down: amamba_v0.25.2_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.2_arm64_checksum.sha512sum) | 2024-04-17 |
| [v0.25.2](../../amamba/intro/release-notes.md) | AMD 64 | 370.19 MB | [:arrow_down: amamba_v0.25.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.2_amd64.tar) | [:arrow_down: amamba_v0.25.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.2_amd64_checksum.sha512sum) | 2024-04-17 |
| [v0.25.0](../../amamba/intro/release-notes.md) | <font color="green">ARM 64</font> | 353.54 MB | [:arrow_down: amamba_v0.25.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.0_arm64.tar) | [:arrow_down: amamba_v0.25.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.0_arm64_checksum.sha512sum) | 2024-04-02 |
| [v0.25.0](../../amamba/intro/release-notes.md) | AMD 64 | 370.19 MB | [:arrow_down: amamba_v0.25.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.0_amd64.tar) | [:arrow_down: amamba_v0.25.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.25.0_amd64_checksum.sha512sum) | 2024-04-02 |
| [v0.24.0](../../amamba/intro/release-notes.md) | <font color="green">ARM 64</font> | 350.38 MB | [:arrow_down: amamba_v0.24.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.24.0_arm64.tar) | [:arrow_down: amamba_v0.24.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.24.0_arm64_checksum.sha512sum) | 2024-02-01 |
| [v0.24.0](../../amamba/intro/release-notes.md) | AMD 64 | 367.01 MB | [:arrow_down: amamba_v0.24.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.24.0_amd64.tar) | [:arrow_down: amamba_v0.24.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.24.0_amd64_checksum.sha512sum) | 2024-02-01 |
| [v0.23.0](../../amamba/intro/release-notes.md) | AMD 64 | 353.13 MB | [:arrow_down: amamba_v0.23.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.23.0_amd64.tar) | [:arrow_down: amamba_v0.23.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.23.0_amd64_checksum.sha512sum) | 2024-01-03 |
| [v0.22.1](../../amamba/intro/release-notes.md) | AMD 64 | 340.77 MB | [:arrow_down: amamba_v0.22.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.22.1_amd64.tar) | [:arrow_down: amamba_v0.22.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.22.1_amd64_checksum.sha512sum) | 2023-12-22 |
| [v0.22.0](../../amamba/intro/release-notes.md) | AMD 64 | 340.76 MB | [:arrow_down: amamba_v0.22.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.22.0_amd64.tar) | [:arrow_down: amamba_v0.22.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.22.0_amd64_checksum.sha512sum) | 2023-12-19 |
| [0.19.5](../../amamba/intro/release-notes.md) | AMD 64 | 773.93 MB | [:arrow_down: amamba_0.19.5_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_0.19.5_amd64.tar) | [:arrow_down: amamba_0.19.5_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_0.19.5_amd64_checksum.sha512sum) | 2023-08-30 |

## Validation

In the directory where you downloaded the offline packages and checksum files,
run the following command to validate the integrity:

```sh
echo "$(cat amamba_v0.19.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, it will print a result similar to:

```none
amamba_v0.19.0_amd64.tar: ok
```

## Installation

Refer to the [Offline Upgrade](../../amamba/offline-upgrade.md) page for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
