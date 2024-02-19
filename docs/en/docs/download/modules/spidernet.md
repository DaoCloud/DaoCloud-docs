---
MTPE: windsonsea
date: 2024-01-18
hide:
  - toc
---

# Network

This page allows you to download the offline packages of various versions of the network Spidernet module.

## Download

| Version  | Architecture | File Size |  Package      | Checksum File | Update Date |
|----------|--------------|-----------|---------------|----------|-------------|
| [v0.13.0](../../network/intro/releasenotes.md#v0130) | AMD 64 | 65.71 MB | [:arrow_down: spidernet_v0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.13.0_amd64.tar) | [:arrow_down: spidernet_v0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.13.0_amd64_checksum.sha512sum) | 2024-01-28 |
| [v0.12.0](../../network/intro/releasenotes.md#v0121) | AMD 64 | 64.03 MB | [:arrow_down: spidernet_v0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.12.0_amd64.tar) | [:arrow_down: spidernet_v0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.12.0_amd64_checksum.sha512sum) | 2023-12-26 |
| [v0.6.0](../../network/intro/releasenotes.md#v060) | AMD64 | 55.47 MB | [:arrow_down: spidernet_v0.6.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.6.0_amd64.tar) | [:arrow_down: spidernet_v0.6.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.6.0_amd64_checksum.sha512sum) | 2023-04-26 |
| [v0.5.0](../../network/intro/releasenotes.md#v050) | AMD64 | 51.68 MB | [:arrow_down: spidernet_v0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.5.0_amd64.tar) | [:arrow_down: spidernet_v0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.5.0_amd64_checksum.sha512sum) | 2023-04-25 |

## Validation

In the directory where the offline packages and checksum files are downloaded,
take `v0.5.0_amd64` as an example, run the following command to validate the integrity:

```sh
echo "$(cat spidernet_v0.5.0_amd64_checksum.sha512sum)" | sha512sum -c
```

After the validation is successful, the output is similar to:

```none
spidernet_v0.5.0_amd64.tar: ok
```

## Installation

If you are installing for the first time, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any license key related questions, please contact DaoCloud delivery team.
