# PostgreSQL

This page provides downloadable offline installation packages for various versions of PostgreSQL.

## Download

| Version                                                       | Architecture | File Size | Installation Package                                                                                                               | Checksum File | Date       |
|------------------------------------------------------------| ------------- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |------------|
| [v0.5.1](../../../middleware/postgresql/release-notes.md)     | AMD 64 | 296.23MB | [:arrow_down: postgresql_0.5.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/postgresql_0.5.1_amd64.tar) | [:arrow_down: postgresql_0.5.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/postgresql_0.5.1_amd64_checksum.sha512sum) | 2023-10-10 |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file, execute the following command in the directory:

```sh
echo "$(cat postgresql_0.5.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the printed result will be similar to:

```none
postgresql_0.5.1_amd64.tar: OK
```

## Installation

If this is your first installation, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization at info@daocloud.io or call 400 002 6898.
For any license key-related questions, please contact the DaoCloud delivery team.
