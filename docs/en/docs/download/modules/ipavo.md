---
MTPE: windsonsea
date: 2024-10-12
hide:
  - toc
---

# Ipavo

On this page, you can download the offline packages of each version of the Ipavo module.

## Download

| Version  | Architecture | Size | Package     | Checksum      | Date |
|----------|--------------|-----------|-------------|--------------------|-------------|
| [v0.13.0](../../insight/intro/release-notes.md) | <font color="green">ARM 64</font> | 50.32 MB | [:arrow_down: ipavo_v0.13.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_arm64.tar) | [:arrow_down: ipavo_v0.13.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_arm64_checksum.sha512sum) | 2024-10-28 |
| [v0.13.0](../../insight/intro/release-notes.md) | AMD 64 | 52.65 MB | [:arrow_down: ipavo_v0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_amd64.tar) | [:arrow_down: ipavo_v0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_amd64_checksum.sha512sum) | 2024-10-28 |
| v0.12.4 | AMD 64 | 51 MB | [:arrow_down: ipavo_v0.12.4_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_amd64.tar) | [:arrow_down: ipavo_v0.12.4_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_amd64_checksum.sha512sum) | 2024-10-12 |
| v0.12.4 | <font color="green">ARM 64</font> | 51 MB | [:arrow_down: ipavo_v0.12.4_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_arm64.tar) | [:arrow_down: ipavo_v0.12.4_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_arm64_checksum.sha512sum) | 2024-10-12 |

## Verification

In the directory where the offline packages and checksum files are downloaded,
take `v0.12.4_amd64` as an example, run the following command to validate the integrity:

```sh
echo "$(cat ipavo_v0.12.4_amd64_checksum.sha512sum)" | sha512sum -c
```

After the verification is successful, the output is similar to:

```none
ipavo_v0.12.4_amd64.tar: ok
```

If you are installing for the first time, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any license key related questions, please contact DaoCloud delivery team.
