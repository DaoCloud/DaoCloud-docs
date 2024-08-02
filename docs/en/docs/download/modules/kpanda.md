---
MTPE: windsonsea
date: 2024-01-18
hide:
  - toc
---

# Container Management

This page provides offline packages for different versions of the Container Management module.

## Download

| Version  | Architecture | File Size | Package | Checksum File | Update Date |
|----------|--------------|-----------|---------|----------|-------------|
| [0.29.0](../../kpanda/intro/release-notes.md) | AMD 64 | 759.13 MB | [:arrow_down: kpanda_0.29.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.29.0_amd64.tar) | [:arrow_down: kpanda_0.29.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.29.0_amd64_checksum.sha512sum) | 2024-07-03 |
| [0.28.1](../../kpanda/intro/release-notes.md) | AMD 64 | 675.40MB | [:arrow_down: kpanda_0.28.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.28.1_amd64.tar) | [:arrow_down: kpanda_0.28.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.28.1_amd64_checksum.sha512sum) | 2024-06-05 |
| [0.28.0](../../kpanda/intro/release-notes.md) | AMD 64 | 675.40 MB | [:arrow_down: kpanda_0.28.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.28.0_amd64.tar) | [:arrow_down: kpanda_0.28.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.28.0_amd64_checksum.sha512sum) | 2024-06-04 |
| [0.27.0](../../kpanda/intro/release-notes.md) | AMD 64 | 678.82 MB | [:arrow_down: kpanda_0.27.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.27.0_amd64.tar) | [:arrow_down: kpanda_0.27.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.27.0_amd64_checksum.sha512sum) | 2024-05-06 |
| [0.25.1](../../kpanda/intro/release-notes.md) | AMD 64 | 589.01 MB | [:arrow_down: kpanda_0.25.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.1_amd64.tar) | [:arrow_down: kpanda_0.25.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.1_amd64_checksum.sha512sum) | 2024-02-02 |
| [0.25.0](../../kpanda/intro/release-notes.md) | AMD 64 | 589.01 MB | [:arrow_down: kpanda_0.25.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.0_amd64.tar) | [:arrow_down: kpanda_0.25.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.0_amd64_checksum.sha512sum) | 2024-01-31 |
| [0.23.0](../../kpanda/intro/release-notes.md) | AMD 64 | 616.29 MB | [:arrow_down: kpanda_0.23.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.23.0_amd64.tar) | [:arrow_down: kpanda_0.23.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.23.0_amd64_checksum.sha512sum) | 2023-12-04 |
| [0.22.2](../../kpanda/intro/release-notes.md) | AMD 64 | 615.81 MB | [:arrow_down: kpanda_0.22.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.22.2_amd64.tar) | [:arrow_down: kpanda_0.22.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.22.2_amd64_checksum.sha512sum) | 2023-11-14 |
| [0.21.1](../../kpanda/intro/release-notes.md) | AMD 64 | 716.15 MB | [:arrow_down: kpanda_0.21.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.21.1_amd64.tar) | [:arrow_down: kpanda_0.21.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.21.1_amd64_checksum.sha512sum) | 2023-09-15 |

## Verification

To verify the integrity of the downloaded offline package and checksum file,
take `v0.22.2_amd64` as an example, run the following command in the directory:

```sh
echo "$(cat kpanda_v0.22.2_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the result will be similar to:

```none
kpanda_v0.22.2_amd64.tar: ok
```

## Installation

Refer to the [Offline Upgrade Container Management Module](../../kpanda/intro/offline-upgrade.md) for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization:
email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
