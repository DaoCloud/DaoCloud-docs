# Container Registry

On this page, you can download offline installation packages for different versions of the container registry module.

## Download

| Version                                          | Architecture | File Size | Installation Package                                                                                                              | Checksum File                                                                                                                | Update Date |
|--------------------------------------------------|--------------|-----------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------|
| [v0.10.0](../../kangaroo/release-notes.md) | AMD64        | 293.24 MB | [:arrow_down: kangaroo_v0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.10.0_amd64.tar) | [:arrow_down: kangaroo_0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.10.0_amd64_checksum.sha512sum) | 2023-8-22   |

## Verification

In the directory where you downloaded the offline installation package and checksum file, execute the following command to verify the integrity:

```sh
echo "$(cat kangaroo_0.10.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the result will be similar to:

```none
kangaroo_0.10.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: send an email to info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
