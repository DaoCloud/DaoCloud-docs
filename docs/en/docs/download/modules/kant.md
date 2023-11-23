# Cloud Edge Collaboration Kant

This page provides offline packages for different versions of the Cloud Edge Collaboration module.

## Download

| Version     | Architecture | File Size | Package      | Checksum File | Update Date |
|-------------| ----- |-----------|---------------| ---------- |-----------|
| [0.5.0](../../kant/intro/release-notes.md) | AMD 64 | 92.49MB | [:arrow_down: kant_0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kant_0.5.0_amd64.tar) | [:arrow_down: kant_0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kant_0.5.0_amd64_checksum.sha512sum) | 2023-10-27 |
| [0.5.0](../../kant/intro/release-notes.md) | AMD 64 | 28.4MB  | [:arrow_down: kantadm_installation_0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kantadm_installation_0.5.0_amd64.tar) | [:arrow_down: kantadm_installation_0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kantadm_installation_0.5.0_amd64_checksum.sha512sum) | 2023-10-27 |
| [0.5.0](../../kant/intro/release-notes.md) | ARM 64 | 28.1MB  | [:arrow_down: kantadm_installation_0.5.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kantadm_installation_0.5.0_arm64.tar) | [:arrow_down: kantadm_installation_0.5.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kantadm_installation_0.5.0_arm64_checksum.sha512sum) | 2023-10-27 |

## Validation

To validate the integrity of the downloaded offline package and checksum file,
 run the following command in the directory:

```sh
echo "$(cat kant_0.5.0_amd64_checksum.sha512sum)" | sha512sum -c
```

Upon successful validation, the result will be similar to:

```none
kant_0.5.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
For any license key-related inquiries, please contact the DaoCloud delivery team.
