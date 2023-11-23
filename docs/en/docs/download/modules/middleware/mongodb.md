# MongoDB

This page provides offline packages for various versions of MongoDB.

## Download

| Version                                                     | Architecture | File Size | Installation Package                                                                                                               | Checksum File | Update Date |
|------------------------------------------------------------|--------------|-----------|----------------------------------------------------------------------------------------------------------------------------------|---------------|-------------|
| [v0.3.1](../../../middleware/mongodb/release-notes.md)     | AMD64        | 293.24 MB | [:arrow_down: mongodb_0.3.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mongodb_0.3.1_amd64.tar) | [:arrow_down: mongodb_0.3.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mongodb_0.3.1_amd64_checksum.sha512sum) | 2023-10-10 |

## Validation

To validate the integrity of the downloaded offline package and checksum file, run the following command in the directory:

```sh
echo "$(cat mongodb_0.3.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the printed result will be similar to:

```none
mongodb_0.3.1_amd64.tar: OK
```

## Installation

If this is your first time installing, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
