---
MTPE: windsonsea
date: 2024-01-18
hide:
  - toc
---

# Insight

On this page, you can download the offline packages of each version of the Insight module.

## Download

| Version  | Architecture | File Size | Package     | Checksum File      | Update Date |
|----------|--------------|-----------|-------------|--------------------|-------------|
| [v0.26.0](../../insight/intro/release-notes.md) | <font color="green">ARM 64</font> | 2.36 GB | [:arrow_down: insight_v0.26.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.26.0_arm64.tar) | [:arrow_down: insight_v0.26.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.26.0_arm64_checksum.sha512sum) | 2024-05-06 |
| [v0.26.0](../../insight/intro/release-notes.md) | AMD 64 | 2.44 GB | [:arrow_down: insight_v0.26.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.26.0_amd64.tar) | [:arrow_down: insight_v0.26.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.26.0_amd64_checksum.sha512sum) | 2024-05-06 |
| [v0.25.2](../../insight/intro/releasenote.md) | <font color="green">ARM 64</font> | 2.68 GB | [:arrow_down: insight_v0.25.2_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.25.2_arm64.tar) | [:arrow_down: insight_v0.25.2_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.25.2_arm64_checksum.sha512sum) | 2024-04-02 |
| [v0.25.2](../../insight/intro/releasenote.md) | AMD 64 | 2.77 GB | [:arrow_down: insight_v0.25.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.25.2_amd64.tar) | [:arrow_down: insight_v0.25.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.25.2_amd64_checksum.sha512sum) | 2024-04-02 |
| [v0.24.0](../../insight/intro/releasenote.md) | AMD 64 | 2.75 GB | [:arrow_down: insight_v0.24.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.24.0_amd64.tar) | [:arrow_down: insight_v0.24.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.24.0_amd64_checksum.sha512sum) | 2024-02-18 |
| [v0.23.1](../../insight/intro/releasenote.md) | AMD 64 | 2.69 GB | [:arrow_down: insight_v0.23.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.23.1_amd64.tar) | [:arrow_down: insight_v0.23.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.23.1_amd64_checksum.sha512sum) | 2024-01-31 |
| [v0.22.1](../../insight/intro/releasenote.md) | AMD 64 | 2.70 GB | [:arrow_down: insight_v0.22.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.22.1_amd64.tar) | [:arrow_down: insight_v0.22.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.22.1_amd64_checksum.sha512sum) | 2023-12-19 |
| [v0.22.0](../../insight/intro/releasenote.md) | AMD 64 | 2.70 GB | [:arrow_down: insight_v0.22.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.22.0_amd64.tar) | [:arrow_down: insight_v0.22.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.22.0_amd64_checksum.sha512sum) | 2023-12-04 |
| [v0.19.1](../../insight/intro/releasenote.md#v0190) | AMD 64 | 2.64 GB | [:arrow_down: insight_v0.19.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.19.1_amd64.tar) | [:arrow_down: insight_v0.19.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.19.1_amd64_checksum.sha512sum) | 2023-08-04 |
| [v0.13.1](../../insight/intro/releasenote.md) | AMD64 | 2.41 GB | [:arrow_down: insight_v0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64.tar) | [:arrow_down: insight_v0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64_checksum.sha512sum) | 2022 -12-30 |

## Validation

In the directory where the offline packages and checksum files are downloaded,
take `v0.13.1_amd64` as an example, run the following command to validate the integrity:

```sh
echo "$(cat insight_v0.13.1_amd64_checksum.sha512sum)" | sha512sum -c
```

After the validation is successful, the output is similar to:

```none
insight_v0.13.1_amd64.tar: ok
```

## Installation

Refer to [Offline upgrade Insight module](../../insight/quickstart/install/offline-install.md)
for installation instructions.

If you are installing for the first time, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any license key related questions, please contact DaoCloud delivery team.
