# Cloud Edge Collaboration Kant

This page provides offline installation packages for different versions of the Cloud Edge Collaboration module.

## Download

| Version     | Architecture | File Size | Package      | Checksum File | Update Date |
|-------------| ----- |-----------|---------------| ---------- |-----------|
| [v0.4.0](../../kant/intro/release-notes.md) | AMD64 | 94.2 MB   | [:arrow_down: kant_0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kant_0.4.0_amd64.tar) | [:arrow_down: kant_0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kant_0.4.0_amd64_checksum.sha512sum) | 2023-9-19 |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file,
 run the following command in the directory:

```sh
echo "$(cat kant_0.4.0_amd64_checksum.sha512sum)" | sha512sum -c
```

Upon successful verification, the result will be similar to:

```none
kant_0.4.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
For any license key-related inquiries, please contact the DaoCloud delivery team.
