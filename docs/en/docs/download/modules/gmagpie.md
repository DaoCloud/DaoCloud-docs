# Operations Management

This page allows you to download the offline packages for different versions of the Operations Management module.

## Download

| Version  | Architecture | File Size | Package     | Checksum File      | Update Date |
|----------|--------------|-----------|-------------|--------------------|-------------|
| [v0.4.1](../../ghippo/intro/release-notes.md) | AMD 64 | 93.72MB | [:arrow_down: gmagpie_v0.4.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.1_amd64.tar) | [:arrow_down: gmagpie_v0.4.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.1_amd64_checksum.sha512sum) | 2023-08-29 |
| [v0.3.2](../../dce/dce-rn/20230630.md) | AMD 64 | 91.85 MB | [:arrow_down: gmagpie_v0.3.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.2_amd64.tar) | [:arrow_down: gmagpie_v0.3.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.2_amd64_checksum.sha512sum) | 2023-08-02 |
| [v0.3.0](../../dce/dce-rn/20230630.md)       | AMD64        | 56.90 MB   | [:arrow_down: gmagpie_v0.3.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.0_amd64.tar)         | [:arrow_down: gmagpie_v0.3.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.0_amd64_checksum.sha512sum)           | 2023-06-28   |
| [v0.2.2](../../ghippo/user-guide/report-billing/index.md) | AMD64        | 37.1 MB    | [:arrow_down: gmagpie_v0.2.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.2.2_amd64.tar)           | [:arrow_down: gmagpie_v0.2.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.2.2_amd64_checksum.sha512sum)          | 2023-5-30    |

## Validation

Navigate to the directory where the offline packages and checksum files are downloaded,
take `v0.2.2_amd64` as an example, and run the following command to validate the integrity:

```sh
echo "$(cat gmagpie_v0.2.2_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the result will be similar to:

```none
gmagpie_v0.2.2_amd64.tar: ok
```

## Installation

Refer to the [Global Management installation process](../../ghippo/install/offline-install.md) for installation instructions.

If this is your first-time installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization at info@daocloud.io or call 400 002 6898.
For any license-related issues, please contact the DaoCloud delivery team.
