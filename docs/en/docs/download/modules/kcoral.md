# Application Backup

This page provides offline installation packages for different versions of the Application Backup module.

## Download

| Version                                       | Architecture | File Size | Installation Package                                                                                                             | Checksum File                                                                                                                            | Updated Date |
|-----------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |------------|
| [v0.4.0](../../dce/dce-rn/20230731.md) | AMD64        | 59.29 MB    | [:arrow_down: kcoral_v0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.4.0_amd64.tar) | [:arrow_down: kcoral_v0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.4.0_amd64_checksum.sha512sum) | 2023-08-08   |

## Checksum

To verify the integrity of the downloaded offline installation package and checksum file,
take `v0.4.0_amd64` as an example, run the following command in the directory:

```sh
echo "$(cat kcoral_v0.4.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the result will be similar to:

```none
kcoral_v0.4.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization:
email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
