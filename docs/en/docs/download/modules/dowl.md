# Security Management

This page provides offline installation packages for different versions of the Dowl security management module.

## Download

| Version                                            | Architecture | File Size | Installation Package                                                                                                                             | Checksum File | Update Date |
|-----------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |-----------|
| [v0.4.0](../../dowl/release-notes.md) | AMD64 | 163 MB | [:arrow_down: dowl_v0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dowl_v0.4.0_amd64.tar) | [:arrow_down: dowl_v0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dowl_v0.4.0_amd64_checksum.sha512sum) | 2023-8-25 |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file, execute the following command in the directory:

```sh
echo "$(cat dowl_v0.4.0_amd64_checksum.sha512sum)" | sha512sum -c
```

Upon successful verification, the result will be similar to:

```none
dowl_v0.4.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
For any license key-related inquiries, please contact the DaoCloud delivery team.
