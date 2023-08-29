# Network Spidernet

This page can download the offline installation packages of various versions of the network Spidernet module.

## Download

| Version | Architecture | File Size |
| --------------------------| ----- |-------- | ------- -------------------------------------------------- -------------------------------------------------- ------| ---------- | ---------- |
| v0.6.0 | AMD64 | 55.47 MB | [:arrow_down: spidernet_v0.6.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.6.0_amd64.tar) | [:arrow_down: spidernet_v0.6.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.6.0_amd64_checksum.sha512sum) | 2023-04-26 |
| v0.5.0 | AMD64 | 51.68 MB | [:arrow_down: spidernet_v0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.5.0_amd64.tar) | [:arrow_down: spidernet_v0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/spidernet_v0.5.0_amd64_checksum.sha512sum) | 2023-04-25 |

## Verification

In the directory where the offline installation package and verification file are downloaded, take `v0.5.0_amd64` as an example, run the following command to verify the integrity:

```sh
echo "$(cat spidernet_v0.5.0_amd64_checksum.sha512sum)" | sha512sum -c
```

After the verification is successful, the printed result is similar to:

```none
spidernet_v0.5.0_amd64.tar: ok
```

## Installation

If you are installing for the first time, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any license key related questions, please contact DaoCloud delivery team.
