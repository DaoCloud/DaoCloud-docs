---
MTPE: windsonsea
date: 2024-01-11
hide:
  - toc
---

# Cluster Inspection

This page provides offline packages for different versions of the Cluster Inspection module.

## Download

| Version | Architecture | Size | Package | Checksum | Date |
|---------|--------------|-----------|----------|--------------|--------------|
| [v0.10.0](../../kpanda/intro/release-notes.md) | AMD 64 | 252.95 MB | [:arrow_down: kcollie_v0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.10.0_amd64.tar) | [:arrow_down: kcollie_v0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.10.0_amd64_checksum.sha512sum) | 2024-09-29 |
| [v0.6.1](../../kpanda/intro/release-notes.md) | AMD 64 | 174.34 MB | [:arrow_down: kcollie_v0.6.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.6.1_amd64.tar) | [:arrow_down: kcollie_v0.6.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.6.1_amd64_checksum.sha512sum) | 2024-01-03 |
| [v0.6.0](../../kpanda/intro/release-notes.md) | AMD 64 | 174.30 MB | [:arrow_down: kcollie_v0.6.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.6.0_amd64.tar) | [:arrow_down: kcollie_v0.6.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.6.0_amd64_checksum.sha512sum) | 2024-01-02 |
| [v0.5.2](../../kpanda/intro/release-notes.md) | AMD 64 | 216.70 MB | [:arrow_down: kcollie_v0.5.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.5.2_amd64.tar) | [:arrow_down: kcollie_v0.5.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.5.2_amd64_checksum.sha512sum) | 2023-10-26 |
| [v0.5.1](../../kpanda/intro/release-notes.md) | AMD 64 | 211.94 MB | [:arrow_down: kcollie_v0.5.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.5.1_amd64.tar) | [:arrow_down: kcollie_v0.5.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.5.1_amd64_checksum.sha512sum) | 2023-10-20 |
| [v0.5.0](../../kpanda/intro/release-notes.md) | AMD 64 | 216.64 MB | [:arrow_down: kcollie_v0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.5.0_amd64.tar) | [:arrow_down: kcollie_v0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.5.0_amd64_checksum.sha512sum) | 2023-09-01 |
| [v0.4.0](../../kpanda/intro/release-notes.md) | AMD64 | 205.11 MB | [:arrow_down: kcollie_v0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.4.0_amd64.tar) | [:arrow_down: kcollie_v0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.4.0_amd64_checksum.sha512sum) | 2023-08-08 |

## Verification

To verify the integrity of the downloaded offline package and checksum file,
take `v0.4.0_amd64` as an example, run the following command in the directory:

```sh
echo "$(cat kcollie_v0.4.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the result will be similar to:

```none
kcollie_v0.4.0_amd64.tar: ok
```

## Installation

Refer to the [Offline Upgrade Cluster Inspection Module](../../kpanda/user-guide/inspect/offline-upgrade.md) for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
