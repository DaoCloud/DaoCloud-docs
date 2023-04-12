# Insight

On this page, you can download the offline installation packages of each version of the observability module.

## Download

| Version | Architecture | File Size | Pack | MD5 file | Date |
| ------------------- | ----- |-------- | --------------- | ---------- | ---------- |
| [v0.13.1](../../insight/intro/releasenote.md) | AMD64 | 2.41GB | [:arrow_down: insight_v0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64.tar) | [:arrow_down: insight_v0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64_checksum.sha512sum) | 2022 -12-30 |

## Validation

In the directory where the offline installation package and verification file are downloaded, execute the following command to verify the integrity:

```sh
echo "$(cat insight_v0.13.1_amd64_checksum.sha512sum)" | sha512sum -c
```

After the verification is successful, the printed result is similar to:

```none
insight_v0.13.1_amd64.tar: ok
```

## Install

Refer to [Observability](../../insight/user-guide/quickstart/offline-install.md) installation process to install.

If you are installing for the first time, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any license key related questions, please contact DaoCloud delivery team.
