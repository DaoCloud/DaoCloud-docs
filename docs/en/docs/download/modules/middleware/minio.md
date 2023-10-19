# MinIO

This page provides downloadable offline installation packages for various versions of MinIO.

## Download

| Version                                                     | Architecture | File Size | Installation Package                                                                                                 | Checksum File                                                                                                           | Update Date |
|------------------------------------------------------------|--------------|-----------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-------------|
| [v0.8.1](../../../middleware/minio/release-notes.md) | AMD 64       | 219.91MB  | [:arrow_down: minio_0.8.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/minio_0.8.1_amd64.tar) | [:arrow_down: minio_0.8.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/minio_0.8.1_amd64_checksum.sha512sum) | 2023-10-11   |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file, run the following command in the directory where they are located:

```sh
echo "$(cat minio_0.8.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the printed result will be similar to:

```none
minio_0.8.1_amd64.tar: OK
```

## Installation

If this is your first time installing MinIO, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please reach out to the DaoCloud delivery team.
