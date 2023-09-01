# Multicloud Management Kairship

This page provides offline installation packages for different versions of the Multicloud Management module.

## Download

| Version                                            | Architecture | File Size | Installation Package                                                                                                                             | Checksum File | Update Date |
|-----------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |-----------|
| [v0.11.0](../../kairship/intro/release-notes.md) | AMD64 | 486 MB | [:arrow_down: kairship_v0.11.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.11.0_amd64.tar) | [:arrow_down: kairship_v0.11.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.11.0_amd64_checksum.sha512sum) | 2023-7-31 |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file, execute the following command in the directory:

```sh
echo "$(cat kairship_v0.11.0_amd64_checksum.sha512sum)" | sha512sum -c
```

Upon successful verification, the result will be similar to:

```none
kairship_v0.11.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
For any license key-related inquiries, please contact the DaoCloud delivery team.
