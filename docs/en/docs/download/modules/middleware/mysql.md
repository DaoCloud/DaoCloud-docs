# MySQL

This page provides downloadable offline packages for various versions of MySQL.

## Download

| Version                                                       | Architecture | File Size | Installation Package                                                                                                               | Checksum File | Date       |
|------------------------------------------------------------| ------------- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |------------|
| [v0.11.1](../../../middleware/mysql/release-notes.md) | AMD 64 | 1.17GB | [:arrow_down: mysql_0.11.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mysql_0.11.1_amd64.tar) | [:arrow_down: mysql_0.11.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mysql_0.11.1_amd64_checksum.sha512sum) | 2023-10-12 |

## Validation

To validate the integrity of the downloaded offline package and checksum file, run the following command in the directory:

```sh
echo "$(cat mysql_0.11.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the printed result will be similar to:

```none
mysql_0.11.1_amd64.tar: OK
```

## Installation

If this is your first installation, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization at info@daocloud.io or call 400 002 6898.
For any license key-related questions, please contact the DaoCloud delivery team.
